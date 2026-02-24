from typing import List, Dict


def hybrid_ads_boolean(arr: List[int], Pmax: int, Pmin: int) -> Dict[str, int]:
    """
    Hybrid Adaptive Distinct Set (ADS) Boolean Selection.

    Computes:
        - Median
        - p-th maximum
        - p-th minimum

    using threshold decomposition restricted to distinct values.
    """

    if not arr:
        raise ValueError("Input array must not be empty.")

    N = len(arr)
    arr_sorted = sorted(arr)
    distinct_thresholds = sorted(set(arr_sorted))

    results = {
        "median": 0,
        "pmax": 0,
        "pmin": 0
    }

    prev_threshold = 0

    for t in distinct_thresholds:
        width = t - prev_threshold
        prev_threshold = t

        ones = sum(1 for x in arr_sorted if x >= t)
        zeros = N - ones

        # Median rule
        if ones > zeros:
            results["median"] += width

        # p-th maximum rule
        if ones >= Pmax:
            results["pmax"] += width

        # p-th minimum rule
        if zeros < Pmin:
            results["pmin"] += width

    return results
src/weighted_median.py
from typing import List, Tuple


def weighted_median(values: List[int], weights: List[float]) -> int:
    """
    Computes the weighted median using cumulative weight crossing.

    The weighted median is the smallest value whose cumulative
    weight is at least half of the total weight.
    """

    if not values or not weights:
        raise ValueError("Values and weights must not be empty.")

    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same length.")

    if any(w <= 0 for w in weights):
        raise ValueError("All weights must be positive.")

    pairs: List[Tuple[int, float]] = sorted(
        zip(values, weights),
        key=lambda x: x[0]
    )

    total_weight = sum(weights)
    threshold = total_weight / 2

    cumulative = 0.0

    for value, weight in pairs:
        cumulative += weight
        if cumulative >= threshold:
            return value

    return pairs[-1][0]
