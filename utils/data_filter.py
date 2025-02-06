import pandas as pd


def filter_data(data: pd.DataFrame, filters):
    vote_average, genre, original_language, year, budget = filters

    filtered_data = data[
        (
            (data["vote_average"] >= vote_average[0])
            & (data["vote_average"] <= vote_average[1])
        )
        & ((data["year"] >= year[0]) & (data["year"] <= year[1]))
        & ((data["revenue"] >= budget[0]) & (data["revenue"] <= budget[1]))
        & (data["adult"] == False)
    ]

    if genre != "All":
        filtered_data = filtered_data[
            filtered_data["genres"].str.contains(genre, na=False)
        ]

    if original_language != "All":
        filtered_data = filtered_data[
            filtered_data["original_language"] == original_language
        ]

    return filtered_data
