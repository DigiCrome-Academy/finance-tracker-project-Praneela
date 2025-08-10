
from datetime import datetime
from typing import Dict, Optional

class InvestmentPortfolio:
    
    class Holding:
        
        def __init__(self, symbol: str,shares: float, purchase_price: float, current_price: float, purchase_date : datetime) -> None:
            self.symbol = symbol
            self.shares = shares
            self.purchase_price = purchase_price
            self.current_price = current_price
            self.purchase_date = purchase_date
            
        def market_value(self) -> float:
            return self.shares * self.current_price
        
        def cost_basis(self) -> float:
            return self.shares * self.purchase_price
        
        def gain_loss(self) -> float:
            return self.market_value() - self.cost_basis()
        
        def return_percentage(self) -> float:
            if self.cost_basis() == 0:
                return 0.0
            return (self.gain_loss() / self.cost_basis()) * 100
        
        def __init_(self,portfolio_name: str, cash_balance: float = 0.0) -> None:
            self.portfolio_name = portfolio_name
            self.cash_balance  = cash_balance
            self.holdings: Dict[str, InvestmentPortfolio.Holding] = {}
            
        def add_holding(self, symbol: str,  shares: float, purchase_price: float,
                        current_price: float, purchase_date: datetime) -> None:
            
            if symbol in self.holdings:
                existing = self.holdings[symbol]
                total_shares = existing.shares + shares
                weighted_price = (
                    (existing.shares * existing.purchase_price + shares * purchase_price) / total_shares
                )
                
                existing.shares = total_shares
                existing.purchase_price = weighted_price
                existing.current_price = current_price
            else:
                self.holdings[symbol] = self.Holding(
                    symbol, shares, purchase_price, current_price, purchase_date
                )
                
        def remove_holding(self, symbol: str) -> bool:
            return self.holdings.pop(symbol,None) is not None
        
        def update_prices(self, price_update: Dict[str, float]) -> None:
            for symbol, price in price_update.items():
                if symbol in self.holdings:
                    self.holdings[symbol].current_price = price
        
        def calculate_total_value(self) -> float:
            total = self.cash_balance
            for holding in self.holdings.values():
                total += holding.market_value()
            return total
        
        def get_asset_allocation(self) -> Dict[str, float]:
            total_value = self.calculate_total_value()
            
            if total_value == 0:
                return {}
            
            allocation = {
                symbol: (holding.market_value() / total_value) * 100
                for symbol, holding in self.holdings.items()
            }
            
            if self.cash_balance > 0:
                allocation["CASH"] = (self.cash_balance / total_value) * 100
            return allocation

        def best_performer(self) -> Optional[Holding]:
            if not self.holdings:
                return None
            return max(self.holdings.values, key = lambda h: h.return_percentage())
        
        def worst_performer(self) -> Optional[Holding]:
            if not self.holdings:
                return None
            return min(self.holdings.values() , key = lambda h : h.return_percentage())  
        
        def __str__(self) -> str:
            return (f"InvestmentPortfolio ('{self.portfolio_name}') - "
            f"Total Value: ${self.calculate_total_value():.2f} ")
            
            
                
        
                
            
            
            
        
            