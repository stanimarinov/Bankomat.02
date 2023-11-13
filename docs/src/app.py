
from bankomat.db import DB
from bankomat.account import Account, Accounts


if __name__=="__main__":

    db = DB()

    accounts_dict = db.get_all_accounts()

    accounts = Accounts.from_list_of_dict(accounts_dict)
    print(accounts)

    accounts[0].balance = 0
    for account in accounts:
        print(account)