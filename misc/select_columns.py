import pandas as pd
import sys


def select_columns(file_to_trim, trimmed_file):
    """Keep columns of a dataset based on the columns of another one."""
    trimmed = pd.read_csv(trimmed_file)
    to_trim = pd.read_csv(file_to_trim)
    to_trim_name = file_to_trim[:len(file_to_trim) - 5]  # Remove the .csv

    columns = list(trimmed.columns.values)
    new_df = pd.DataFrame()
    for column in columns:
        new_df[column] = to_trim[column]
    new_df.to_csv(f"./{to_trim_name}-trimmed.csv", index=False)
    print("Success")


if __name__ == "__main__":
    try:
        file_to_trim = sys.argv[1]
        trimmed_file = sys.argv[2]
    except IndexError as e:
        print(f'Usage: {__file__} <file_to_trim> <correctly_trimmed_file>')
        sys.exit(1)

    select_columns(file_to_trim, trimmed_file)
