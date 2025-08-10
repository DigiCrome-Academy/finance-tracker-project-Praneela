from __future__ import annotations
import numpy as np
from typing import List, Dict, Tuple


class FinancialAnalyzer:
    """
    Provides analytical and forecasting tools for financial data using NumPy.
    """

    @staticmethod
    def calculate_moving_averages(expenses: List[float], window: int = 3) -> np.ndarray:
        """
        Calculates moving averages for spending trends.

        Args:
            expenses (List[float]): List of expense values.
            window (int): Rolling window size. Defaults to 3.

        Returns:
            np.ndarray: Moving average values.
        """
        arr = np.array(expenses, dtype=float)
        if window <= 0 or window > len(arr):
            raise ValueError("Invalid window size.")
        cumsum = np.cumsum(arr)
        cumsum[window:] = cumsum[window:] - cumsum[:-window]
        return cumsum[window - 1:] / window

    @staticmethod
    def analyze_spending_patterns(expenses: List[float]) -> Dict[str, float]:
        """
        Performs statistical analysis of expenses.

        Args:
            expenses (List[float]): Expense values.

        Returns:
            Dict[str, float]: Mean, standard deviation, min, max.
        """
        arr = np.array(expenses, dtype=float)
        return {
            "mean": np.mean(arr),
            "std_dev": np.std(arr),
            "min": np.min(arr),
            "max": np.max(arr)
        }

    @staticmethod
    def project_future_balance(balances: List[float], months_ahead: int = 6) -> np.ndarray:
        """
        Forecasts future balances using linear regression.

        Args:
            balances (List[float]): Historical monthly balances.
            months_ahead (int): Number of months to project.

        Returns:
            np.ndarray: Projected balances for given months ahead.
        """
        arr = np.array(balances, dtype=float)
        x = np.arange(len(arr))
        slope, intercept = np.polyfit(x, arr, 1)
        future_x = np.arange(len(arr), len(arr) + months_ahead)
        return slope * future_x + intercept

    @staticmethod
    def calculate_portfolio_metrics(returns: List[float], risk_free_rate: float = 0.02) -> Dict[str, float]:
        """
        Calculates portfolio performance metrics.

        Args:
            returns (List[float]): Periodic returns (e.g., monthly % returns as decimals).
            risk_free_rate (float): Risk-free rate (annualized). Defaults to 0.02.

        Returns:
            Dict[str, float]: Average return, volatility, Sharpe ratio.
        """
        arr = np.array(returns, dtype=float)
        avg_return = np.mean(arr)
        volatility = np.std(arr)
        sharpe_ratio = (avg_return - (risk_free_rate / 12)) / volatility if volatility != 0 else np.nan
        return {
            "average_return": avg_return,
            "volatility": volatility,
            "sharpe_ratio": sharpe_ratio
        }

    @staticmethod
    def optimize_budget_allocation(categories: List[str], expenses: List[float], total_budget: float) -> Dict[str, float]:
        """
        Optimizes budget allocation proportionally based on past expenses.

        Args:
            categories (List[str]): Budget categories.
            expenses (List[float]): Historical expenses for each category.
            total_budget (float): Total available budget.

        Returns:
            Dict[str, float]: Optimized allocation per category.
        """
        exp_arr = np.array(expenses, dtype=float)
        if np.sum(exp_arr) == 0:
            return {cat: total_budget / len(categories) for cat in categories}

        proportions = exp_arr / np.sum(exp_arr)
        allocation = proportions * total_budget
        return {cat: alloc for cat, alloc in zip(categories, allocation)}

    @staticmethod
    def correlation_between_expenses(expense_matrix: List[List[float]]) -> np.ndarray:
        """
        Computes correlation coefficients between multiple expense categories.

        Args:
            expense_matrix (List[List[float]]): 2D list where each row is a category's expense history.

        Returns:
            np.ndarray: Correlation matrix.
        """
        arr = np.array(expense_matrix, dtype=float)
        return np.corrcoef(arr)