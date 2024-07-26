import pandas as pd

# Provided data as a list of percentages
percentages = [
    69.996, 70.377, 70.757, 71.134, 71.508, 71.879, 72.247, 72.612, 72.974, 73.333, 73.602, 73.613,
    73.623, 73.633, 73.643, 73.653, 73.663, 73.673, 73.682, 73.692, 73.738, 73.89, 74.042, 74.194,
    74.344, 74.494, 74.644, 74.793, 74.942, 75.089, 75.3, 75.701, 76.097, 76.488, 76.875, 77.257,
    77.636, 78.008, 78.377, 78.742, 79.057, 79.234, 79.409, 79.583, 79.757, 79.928, 80.099, 80.269,
    80.438, 80.606, 80.772, 80.944, 81.119, 81.299, 81.483, 81.671, 81.862, 82.058, 82.256, 82.459,
    82.664, 82.873, 83.084, 83.298
]

# Generate the year values starting from 1960 to 2023
years = list(range(1960, 1960 + len(percentages)))

# Check if the lengths match
if len(years) == len(percentages):
    # Create a DataFrame
    df = pd.DataFrame({
        "Year": years,
        "Percentage": percentages
    })

    # Convert the Year column to datetime format (setting to January 1st of each year for simplicity)
    df["Year"] = pd.to_datetime(df["Year"], format='%Y')

    # Save the DataFrame to a CSV file
    csv_file_path = "usa_urban_population.csv"
    df.to_csv(csv_file_path, index=False)


    print(f"Data has been successfully saved to {csv_file_path} and {excel_file_path}")
else:
    print("Error: The lengths of the years and percentages do not match.")
