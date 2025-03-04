# pylint: disable=R0801
"""Common methods and models for tests"""
import os
import sys
import pytest
import time

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../general/")

import test_counterfactualexplainer as tcf
import test_limeexplainer as tlime


@pytest.mark.benchmark(
    group="counterfactuals", min_rounds=10, timer=time.time, disable_gc=True, warmup=True
)
def test_counterfactual_match(benchmark):
    """Counterfactual match"""
    benchmark(tcf.test_counterfactual_match)


@pytest.mark.benchmark(
    group="counterfactuals", min_rounds=10, timer=time.time, disable_gc=True, warmup=True
)
def test_non_empty_input(benchmark):
    """Counterfactual non-empty input"""
    benchmark(tcf.test_non_empty_input)


@pytest.mark.benchmark(
    group="counterfactuals", min_rounds=10, timer=time.time, disable_gc=True, warmup=True
)
def test_counterfactual_match_python_model(benchmark):
    """Counterfactual match (Python model)"""
    benchmark(tcf.test_counterfactual_match_python_model)

# @pytest.mark.benchmark(
#     group="lime", min_rounds=10, timer=time.time, disable_gc=True, warmup=True
# )
# def test_non_empty_input(benchmark):
#     """Counterfactual match (Python model)"""
#     benchmark(tlime.test_non_empty_input)