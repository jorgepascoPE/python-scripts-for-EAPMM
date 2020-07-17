import sys
import pandas as pd
from os import mkdir


def cut_rows(lead, contact, account, request, visit):
    """Cut rows to 10k of independent and dependent datasets"""
    NUMBER_OF_ROWS = 10000

    lead_df = pd.read_csv(lead)
    contact_df = pd.read_csv(contact)
    account_df = pd.read_csv(account)
    request_df = pd.read_csv(request)
    visit_df = pd.read_csv(visit)

    # Remove rows with undesired name values and blank lines
    contact_df = contact_df[(contact_df["Name"]
                             != "Household Member Last Name") & (contact_df["Id"].notnull())]

    # Sample contact and lead (independent datasets) to 10k
    contact_df = contact_df.sample(n=NUMBER_OF_ROWS)
    lead_df = lead_df.sample(n=NUMBER_OF_ROWS)

    # Filter Account with Contact.Id in new Contact df
    account_df = account_df[account_df["Contact.Id"].isin(contact_df["Id"])]

    # Filter Request and Visit with AccountId in new Account df
    request_df = request_df[request_df["AccountId"].isin(account_df["Id"])]
    visit_df = visit_df[visit_df["AccountId"].isin(account_df["Id"])]

    # Create directory
    mkdir("./filtered/")

    # Export CSVs
    lead_df.to_csv(f"./filtered/{lead}", index=False)
    contact_df.to_csv(f"./filtered/{contact}", index=False)
    account_df.to_csv(f"./filtered/{account}", index=False)
    request_df.to_csv(f"./filtered/{request}", index=False)
    visit_df.to_csv(f"./filtered/{visit}", index=False)


if __name__ == "__main__":
    try:
        lead = sys.argv[1]
        contact = sys.argv[2]
        account = sys.argv[3]
        request = sys.argv[4]
        visit = sys.argv[5]
    except:
        print(
            f"Usage: python3 ./{__file__} <lead.csv> <contact_csv> <account_csv> <request_csv> <visit_csv>")
        sys.exit(1)

    cut_rows(lead, contact, account, request, visit)
