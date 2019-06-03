# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Assignment: Create an algorithm using Python
# author @pbarden
# 
# Instructions: Determine if a department store customer purchase exceededs credit limit
# Must include: Account number, account balance, amount to purchase, credit limit
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Account():
    """
    A class used to represent a customer account
    ...
    Attributes
    ----------
    number : str
        the customer's account number (default 00000000)
    balance : float
        the customer's current account balance (default 0)
    limit : int
        the customer's credit limit tied to the account (default 0)

    Methods
    -------
    getApproval(cart)
        prints the approval decision based on available balance and cart total
    """
    def __init__(self, acct_no='00000000', acct_bal=0, c_limit=0):
        """
        Parameters
        ----------
        number : str, optional
            the customer's account number (default 00000000)
        balance : str, optional
            the customer's current account balance (default 0)
        limit : int, optional, optional
            the customer's credit limit tied to the account (default 0)
        
        If arguments for account number, account balance or credit limit aren't 
        passed in, the default values are used - zeros, zeros, zeros across the board
        """
        self.number = acct_no
        self.balance = float(acct_bal)
        self.limit = c_limit
    
    def __str__(self):
        """
        Returns a formatted string to display available account information
        """
        return ('Account number: %s\nAccount balance: $%.2f\nCredit limit: $%.2f' % (self.number, self.balance, self.limit))
    
    def getApproval(self, cart=0):
        """
        Prints the approval decision based on available balance and cart total

        Parameters
        ----------
        cart : float, optional
            current cart value
    
        If an argument for cart value isn't passed in, the default values are used
        """
        if (self.limit - self.balance) >= cart:
            print('TRANSACTION APPROVED')
        else:
            print('TRANSACTION DECLINED')
    
def CollectInfo():
    """
    Collects information required to create an account object and get an approval status

    Returns all 4 variables entered by user after prompts
    """
    acct_no = input('Enter the customer account number:\n')
    acct_bal = float(input('Enter the customer\'s current account balance:\n'))
    prods_cost = float(input('Enter the total cost of all products in customer cart:\n'))
    cred_limit = int(input('Enter the account credit limit:\n'))
    return acct_no, acct_bal, prods_cost, cred_limit

if __name__ == "__main__":
    # Assigns the input values from CollectInfo() to variables
    account_number, account_balance, cart_value, credit_limit = CollectInfo()

    # Creates an Account object using info collected above
    active_account = Account(account_number, account_balance, credit_limit)

    # Prints the account information for visual validation
    print(active_account)

    # Prints the approval status using account info and current purchase total
    active_account.getApproval(cart_value)