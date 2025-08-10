from __future__ import annotations
from datetime import datetime
from typing import Dict,Any

class Transaction:
    
    def __init__(self,
                    transaction_id: str,
                    date: datetime,
                    amount: float,
                    category: str,
                    merchant: str,
                    description: str,
                    account_type: str) -> None:
        
    
        self._validate_required_fields(transaction_id, amount, category, merchant, account_type)
        self._validate_amount(amount)
        
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount    
        self.category = category
        self.merchant = merchant
        self.description = description
        self.account_type = account_type
    
    
    def __str__(self) -> str:
        
        return(f"Transaction({self.transaction_id}, {self.date.date()}, "
                f"${self.amount:.2f}, {self.category}, {self.merchant} )")
        
    def __repr__(self) -> str:
        return(f"Transaction(transaction_id={self.transaction_id!r}, date={self.date!r}, "
                f"amount = {self.amount!r}, category={self.category!r}, "
                f"merchant = {self.merchant!r}, description={self.description!r}, "
                f"account_type = {self.account_type!r})")       
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Transaction):
            return NotImplemented
        return self.transaction_id == other.transaction_id
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Transaction):
            return NotImplemented
        if self.date == other.date:
            return self.amount < other.datetime
        return self.date < other.date
    
    @property
    def month(self) -> int:
        return self.date.month
    
    @property
    def month(self) -> int:
        return self.date.year
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the transaction to a dictionary.

        Returns:
            Dict[str, Any]: Serialized transaction.
        """
        return {
            "transaction_id": self.transaction_id,
            "date": self.date.isoformat(),
            "amount": self.amount,
            "category": self.category,
            "merchant": self.merchant,
            "description": self.description,
            "account_type": self.account_type
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Transaction:
        """
        Deserializes a transaction from a dictionary.

        Args:
            data (Dict[str, Any]): Serialized transaction.

        Returns:
            Transaction: Transaction instance.
        """
        return cls(
            transaction_id=data["transaction_id"],
            date=datetime.fromisoformat(data["date"]),
            amount=float(data["amount"]),
            category=data["category"],
            merchant=data["merchant"],
            description=data.get("description", ""),
            account_type=data["account_type"]
        )
        
    @staticmethod
    def _validate_required_fields(transaction_id: str, date: datetime, amount: float, 
                                  category: str, merchant: str, account_type: str) -> None:
        """Validates that required fields are provided."""
        if not all([transaction_id, date, category, merchant, account_type]):
            raise ValueError("Missing required transaction fields.")
        
    @staticmethod
    def _validate_amount(amount: float) -> None:
        """Validates that the amount is within a reasonable range."""
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > 1_000_000:
            raise ValueError("Amount exceeds allowed limit.")
   