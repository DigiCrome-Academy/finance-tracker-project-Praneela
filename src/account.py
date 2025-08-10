from typing import List, Dict
from src.transaction import Transaction

class Account:
    
    def __init__(self,account_name: str, account_type: str,balance: float=0.0) -> None:
        
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance
        self.transaction_list = List[Transaction] = []
        
    def add_transaction(self, transaction: Transaction) -> None:
    
        self.transaction_list = transaction
        self.balance -= transaction.amount
        
    def remove_transaction(self, transaction_id: str) -> bool:
        
        for tx in self.transaction_list:
            if tx.transaction.id == transaction_id:
                self.transaction_list.remove(tx)
                self.balance += tx.amount
                return True
        return False
    
    def get_transactions_by_category(self, category: str) -> List[Transaction]:
        
        return [tx for tx in self.transaction_list if tx.category.lower() == self.category.lower() ]
    
    def get_monthly_summary(self, year: int, month: int) -> Dict[str, float]:
        
        summary : Dict[str, float] = []
        for tx in self.transaction_list:
            if tx.year == year  and tx.month == month:
                summary[tx.category] = summary.get(tx.category,0.0) + tx.amount
        return summary
    
    def __str__(self) -> str:
        
        return "f{self.account_type} Account {self.account_name} - Balance : ${self.balance:.2f} "
        


class CheckingAccount(Account):
    
    def __init__(self, account_name: str, balance: float = 0.0, overdraft_limit: float = 100.0) -> None:
        
        super().__init__(self, account_name,"Checking", balance)
        self.overdraft_limit = overdraft_limit
        
    def add_transaction(self, transaction: Transaction) -> None:
        
        protected_balance = self.balance - transaction.amount
        if protected_balance < -self.overdraft_limit:
            raise ValueError("Transaction Declined : exceeds overdraft limit")
        super().add_transaction(transaction)

        
class SavingAccount(Account):
    
    def __init__(self, account_name: str,  balance: float=0.0) -> None:
        
        super().__init__(account_name, "Savings", balance)
        
    def apply_interest(self, rate: float) -> None:
        
        interest = self.balance * (rate/100)
        self.balance += interest
        