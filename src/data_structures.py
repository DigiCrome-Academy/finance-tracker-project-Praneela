
from typing import List, Dict, Tuple, Set, Optional


def store_transaction_categories() -> List[str]:
    return ["Groceries","Rent","Utilities","Travel","Entertainment"]
    
def add_category(categories : list[str] , category : str) -> None:
    return categories.append(category)

def category_budget_mapping() -> Dict[str,float]:
    return {
        "Groceries" : 400.0,
        "Rent" : 1500.0,
        "Utilities" : 200.0,
        "Travel" : 500.0,
        "Entertainment" : 300.0
    }
    
def create_transaction_record(transactionId : int, merchant: str, amount: float) -> Tuple[int,str,float]:
    return(transactionId, merchant, amount)

def create_merchant_set() -> Set[str]:
    return{"Target", "Walmart", "Amazon", "NetFlix" , "ebay" }

def create_transaction_history() -> List[Dict[str,str]]:
    
    return [
        {"id": "T001", "merchant": "Walmart", "amount": "45.60", "category": "Groceries"},
        {"id": "T002", "merchant": "Amazon", "amount": "120.00", "category": "Electronics"},
        {"id": "T003", "merchant": "Netflix", "amount": "15.99", "category": "Entertainment"}
    ]

    
def filter_transaction_by_category(history: List[Dict[str,str]], category: str) -> List[Dict[str,str]]:
    for tx in history:
        if tx["category"].lower() == category.lower():
            return tx
    return None

def search_transaction_by_merchant(history: List[Dict[str, str]], merchant: str) -> Optional[Dict[str, str]]:
    
    for tx in history:
        if tx["merchant"].lower() == merchant.lower():
            return tx        
    return None