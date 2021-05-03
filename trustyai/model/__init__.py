# pylint: disable = import-error, too-few-public-methods, invalid-name
"""General model classes"""
from java.util.concurrent import CompletableFuture, ForkJoinPool
from jpype import JImplements, JOverride, JProxy
from org.kie.kogito.explainability.model import (
    PerturbationContext as _PerturbationContext,
    Feature as _Feature,
    FeatureFactory as _FeatureFactory,
    Output as _Output,
    PredictionInput as _PredictionInput,
    PredictionOutput as _PredictionOutput,
    Prediction as _Prediction,
    Value as _Value,
    Type as _Type,
)

PerturbationContext = _PerturbationContext
Feature = _Feature
FeatureFactory = _FeatureFactory
Output = _Output
PredictionInput = _PredictionInput
PredictionOutput = _PredictionOutput
Prediction = _Prediction
Value = _Value
Type = _Type


class InnerSupplier:
    """Wraps the Python predict function in a Java Supplier"""

    def __init__(self, _inputs, predict_fun):
        self.inputs = _inputs
        self.predict_fun = predict_fun

    def get(self):
        """The Supplier interface get method"""
        return self.predict_fun(self.inputs)


@JImplements("org.kie.kogito.explainability.model.PredictionProvider", deferred=True)
class PredictionProvider:
    """Python transformer for the TrustyAI Java PredictionProvider"""

    def __init__(self, predict_fun):
        self.predict_fun = predict_fun

    @JOverride
    def predictAsync(self, inputs):
        """Python implementation of the predictAsync interface method"""
        supplier = InnerSupplier(inputs, self.predict_fun)
        proxy = JProxy("java.util.function.Supplier", inst=supplier)
        future = CompletableFuture.supplyAsync(proxy, ForkJoinPool.commonPool())
        return future