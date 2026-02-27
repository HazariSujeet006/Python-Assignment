import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Line of best fit (1880 → latest year, extend to 2050)
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_extended = pd.Series(range(df["Year"].min(), 2051))
    plt.plot(
        years_extended,
        result.slope * years_extended + result.intercept
    )

    # 4. Line of best fit (2000 → latest year, extend to 2050)
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = pd.Series(range(2000, 2051))
    plt.plot(
        years_recent,
        result_recent.slope * years_recent + result_recent.intercept
    )

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # 6. Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()
