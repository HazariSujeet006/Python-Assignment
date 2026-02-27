import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data")

    # 1. Number of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentage with advanced education earning >50K
    advanced = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education = df[advanced]
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education = df[~advanced]
    lower_education_rich = round(
        (lower_education["salary"] == ">50K").mean() * 100, 1
    )

    # 6. Minimum work hours
    min_work_hours = df["hours-per-week"].min()

    # 7. % earning >50K among those who work min hours
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Country with highest % earning >50K
    country_salary = df.groupby("native-country")["salary"]
    country_percent = country_salary.apply(
        lambda x: (x == ">50K").mean() * 100
    )

    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(
        country_percent.max(), 1
    )

    # 9. Most popular occupation for >50K in India
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
