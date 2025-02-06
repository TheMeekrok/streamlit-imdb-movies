import pandas as pd
import altair as alt
import streamlit as st


def most_popular_film(data: pd.DataFrame):
    st.markdown(
        """
            ### The most popular film (defined by the biggest `popularity` value)

            ```python
                film = data.loc[data["popularity"].idxmax()]
            ``` 
        """
    )

    film = data.loc[data["popularity"].idxmax()]

    st.write(film)
    st.markdown("*the most popular film*")


def vote_average_distribution(data: pd.DataFrame):
    st.markdown(
        """
            ### Vote Average Distribution

            There are a bunch of films that have a 0 vote value, so we've dropped them.

            ```python
                vote_average = data.loc[data["vote_average"] != 0, ["vote_average"]]
            ```
        """
    )

    vote_average = data.loc[data["vote_average"] != 0, ["vote_average"]]

    chart = (
        alt.Chart(vote_average)
        .mark_bar(opacity=0.7)
        .encode(
            x=alt.X("vote_average:Q", bin=alt.Bin(maxbins=20), title="Vote average"),
            y=alt.Y("count()", title="Frequency"),
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("*vote_average distribution*")
    st.markdown(
        """
            As we can see, a lot of films are having meduim ratings and less films
            are having low and high ratings. So the average vote value obeys the
            law of **normal distribution**. This is typical for this kind of cases,
            since people tend to evaluate everything subjectively.
        """
    )


def scatter_budget_vs_revenue(data: pd.DataFrame):
    st.markdown(
        """
            ### Budget vs revenue

            We've also excluded films with unknown `budget` and `revenue` (equal to zero)

            ```python
            budget_vs_revenue = data.loc[
                (data["budget"] != 0) & (data["revenue"] != 0),
                ["budget", "revenue", "title"],
            ]
            ```
        """
    )

    budget_vs_revenue = data.loc[
        (data["budget"] != 0) & (data["revenue"] != 0),
        ["budget", "revenue", "title"],
    ]

    chart = (
        alt.Chart(budget_vs_revenue)
        .mark_circle(size=60, opacity=0.7)
        .encode(
            x=alt.X("budget:Q", title="Budget (in USD)"),
            y=alt.Y("revenue:Q", title="Revenue (in USD)"),
            tooltip=["title", "budget", "revenue"],
            color="revenue",
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)
    st.markdown("*budget vs revenue*")

    st.markdown(
        """
            As we can see, even films with a fairly high budget turn
            out to be quite unprofitable, in contrast, films with a relatively
            low budget show their success and turn out to be profitable. This means
            that the success of a film primarily depends on its idea and team,
            and not on the budget.
        """
    )


def scatter_runtime_vs_budget(data: pd.DataFrame):
    st.markdown(
        """
            ### Runtime vs budget

            Now we will create a scatter chart to see the dependence of the
            `runtime` on its `budget`. We've also excluded films with
            unknown `budget` and `runtime` (equal to zero)

            ```python
                budget_vs_runtime = data.loc[
                    (data["budget"] != 0) & (data["runtime"] != 0),
                    ["budget", "runtime", "title"],
                ]
            ```
        """
    )

    budget_vs_runtime = data.loc[
        (data["budget"] != 0) & (data["runtime"] != 0),
        ["budget", "runtime", "title"],
    ]

    chart = (
        alt.Chart(budget_vs_runtime)
        .mark_circle(size=60, opacity=0.7)
        .encode(
            x=alt.X("budget:Q", title="Budget (in USD)"),
            y=alt.Y("runtime:Q", title="Runtime (min)"),
            tooltip=["title", "budget", "runtime"],
            color="runtime",
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)
    st.markdown("*budget vs runtime*")

    st.markdown(
        """
            As we can see, the length of a film does not correlate much
            with its budget. We can assume that the film industry has
            standardized some standard of film running time. We can also
            observe that the more money allocated to a film, the less
            variation in the length of the film. this can be justified
            by the fact that the more expensive the film, the more restrictions
            are imposed on it, including a carefully verified duration
        """
    )


def bar_month_vs_revenue(data: pd.DataFrame):
    months_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    st.markdown(
        """
            ### Month vs revenue

            We've build a dependence between the month a film was released and its revenue. G
            stands for one billon.

            We see that the highest grossing films are located in the months of June and December,
            that is, half of the year. We will outline several reasons for this. June and December
            are the time of summer holidays, which means viewers have a
            little more time to spend their leisure time watching movies.

            ```python
                month_revenue = (
                pd.DataFrame(
                    {
                        "release_month": pd.Categorical(
                            pd.to_datetime(
                                data["release_date"], format="mixed"
                            ).dt.month_name(),
                            categories=months_order,
                            ordered=True,
                        ),
                        "revenue": data["revenue"],
                    }
                )
                .dropna()
                .groupby("release_month", as_index=False)["revenue"]
                .sum()
            )

            ```
        """
    )

    month_revenue = (
        pd.DataFrame(
            {
                "release_month": pd.Categorical(
                    pd.to_datetime(
                        data["release_date"], format="mixed"
                    ).dt.month_name(),
                    categories=months_order,
                    ordered=True,
                ),
                "revenue": data["revenue"],
            }
        )
        .dropna()
        .groupby("release_month", as_index=False)["revenue"]
        .sum()
    )

    chart = (
        alt.Chart(month_revenue)
        .mark_bar()
        .encode(
            x=alt.X("release_month", title="Release month"),
            y=alt.Y("revenue", title="Revenue", axis=alt.Axis(format=".0s")),
            color="revenue",
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown(
        """
            June and December are the time when so-called "blockbusters" are released, which
            are more likely to collect a lot of money, for example "Avatar" (2009) or
            "Star Wars: The Force Awakens" (2015).
        """
    )


def original_language_distribution(data: pd.DataFrame):
    st.markdown(
        """
            ### Original language distribution

            Now let's group and summarize the films that were released in one specific
            language.

            ```python
            original_language = data.loc[data["vote_average"] != 0, ["original_language"]]

            chart = (
                alt.Chart(data)
                .mark_bar(opacity=0.7)
                .encode(
                    x=alt.X(
                        "original_language:N",
                        title="Original language",
                    ),
                    y=alt.Y("count()", title="Amount"),
                )
            )
            ```
        """
    )

    original_language = data.loc[data["vote_average"] != 0, ["original_language"]]

    chart = (
        alt.Chart(original_language)
        .mark_bar(opacity=0.7)
        .encode(
            x=alt.X(
                "original_language:N",
                title="Original language",
            ),
            y=alt.Y("count()", title="Amount"),
            color="count()",
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("*original_language distribution*")
    st.markdown(
        """
            If we turn on the original_language "All" display,
            we can watch the absolute majority of films released in English `(en)`.

            We can also limit `vote_average` to count and infer which language the
            top rated movies were released in.
        """
    )


def scatter_budget_vs_popularity(data: pd.DataFrame):
    st.markdown(
        """
            ### Budget vs popularity

            $$success_{absolute} = vote_{average} * vote_{count} * popularity$$

            $$success_{normilized} = (success - min(success)) / max(success)$$
            
            ```python
                budget_vs_popularity = pd.DataFrame(
                    {
                        "title": data.title,
                        "budget": data.loc[data["budget"] != 0, "budget"],
                        "success": (
                            data.loc[data["vote_average"] != 0, "vote_average"]
                            * data.loc[data["vote_count"] != 0, "vote_count"]
                            * data.loc[data["popularity"] != 0, "popularity"]
                        ),
                    }
                ).dropna()

                budget_vs_popularity["success"] = (
                    (budget_vs_popularity["success"] - budget_vs_popularity["success"].min())
                    / budget_vs_popularity["success"].max()
                    * 100
                )
            ```
        """
    )

    budget_vs_popularity = pd.DataFrame(
        {
            "title": data.title,
            "budget": data.loc[data["budget"] != 0, "budget"],
            "success": (
                data.loc[data["vote_average"] != 0, "vote_average"]
                * data.loc[data["vote_count"] != 0, "vote_count"]
                * data.loc[data["popularity"] != 0, "popularity"]
            ),
        }
    ).dropna()

    budget_vs_popularity["success"] = (
        (budget_vs_popularity["success"] - budget_vs_popularity["success"].min())
        / budget_vs_popularity["success"].max()
        * 100
    )

    base = (
        alt.Chart(budget_vs_popularity)
        .mark_circle()
        .encode(
            x=alt.X(
                "budget:Q",
                title="Budget",
            ),
            y=alt.Y("success:Q", title="Success"),
            tooltip=["title", "budget", "success"],
        )
    )

    scatter = base.encode(
        color="success",
        tooltip=["title", "budget", "success"],
    )

    line = base.mark_line(color="red").transform_regression(
        "budget", "success", method="quad"
    )

    st.altair_chart(alt.layer(scatter, line), use_container_width=True)
