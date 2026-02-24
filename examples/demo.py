from src.hybrid_ads_boolean import hybrid_ads_boolean
from src.weighted_median import weighted_median


if __name__ == "__main__":

    arr = [3, 2, 1, 4, 5]
    result = hybrid_ads_boolean(arr, Pmax=2, Pmin=2)

    print("Hybrid ADS Results:")
    print(result)

    values = [4, 5, 6, 7, 8]
    weights = [3, 2, 4, 6, 5]

    wm = weighted_median(values, weights)

    print("Weighted Median:")
    print(wm)
