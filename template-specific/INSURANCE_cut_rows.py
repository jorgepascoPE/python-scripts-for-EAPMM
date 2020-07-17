import sys
import pandas as pd


def filter_rows(file_to_filter, min_date):
    """Filter rows by a certain AGENCY_NAME and a min Date"""
    unfiltered = pd.read_csv(file_to_filter)
    print('unfiltered length: ', len(unfiltered.index))

    # filter by agency name
    filtered = unfiltered.loc[unfiltered['Agent.AGENCY_NAME']
                              == 'Levin Insurance Agency']

    # filter by date
    if (min_date):
        filtered['commencement'] = pd.to_datetime(
            unfiltered['commencement'], format='"%Y-%m-%d"')

        filtered = filtered.loc[filtered['commencement'] >= min_date]

    print('filtered length: ', len(filtered.index))
    filtered.to_csv('./filtered.csv', index=False)


if __name__ == '__main__':
    try:
        file_to_filter = sys.argv[1]
        min_year = sys.argv[2] if (len(sys.argv) == 3) else None
        min_date = f'{min_year}-01-01' if min_year else None
    except IndexError as e:
        print(f'Usage: {__file__} <file_to_filter> <min_year>')
        print(e)
        sys.exit(1)

    filter_rows(file_to_filter, min_date)
