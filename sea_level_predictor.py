import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

MAX_PLOT_YEAR = 2050
ADJUST_PLOT_YEAR = 2000

def draw_plot():

    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.plot(df["Year"], df["CSIRO Adjusted Sea Level"], "o", color="0.3")

    # Create first line of best fit
    line1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    line1_years = range(df["Year"].min(), MAX_PLOT_YEAR+1)
    line1_data = list(map(lambda x: line1.intercept + line1.slope * x, line1_years))
    plt.plot(line1_years, line1_data, "y")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= ADJUST_PLOT_YEAR].copy()
    line2 = linregress(x=df_2000["Year"], y=df_2000["CSIRO Adjusted Sea Level"])
    line2_years = range(ADJUST_PLOT_YEAR, MAX_PLOT_YEAR+1)
    plt.plot(line2_years, line2.intercept + line2.slope * line2_years, "r")

    # Add labels and title
    plt.xlabel(xlabel="Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
