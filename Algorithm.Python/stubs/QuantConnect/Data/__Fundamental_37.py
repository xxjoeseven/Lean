from .__Fundamental_38 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class LongTermDebtPaymentsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The cash outflow for debt initially having maturity due after one year or beyond the normal operating cycle, if longer.

    

    LongTermDebtPaymentsCashFlowStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LongTermDebtTotalCapitalRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Refers to the ratio of Long Term Debt to Total Capital. Morningstar calculates the ratio by using the underlying data reported in the

                Balance Sheet within the company filings or reports:    Long-Term Debt And Capital Lease Obligation / (Long-Term Debt And Capital

                Lease Obligation + Total Shareholder's Equity)

    

    LongTermDebtTotalCapitalRatio(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    OneYear: float

    SixMonths: float

    ThreeMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LongTermInvestmentsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Often referred to simply as "investments". Long-term investments are to be held for many years and are not intended to be

                disposed in the near future. This group usually consists of four types of investments.

    

    LongTermInvestmentsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LongTermProvisionsBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Provisions are created to protect the interests of one or both parties named in a contract or legal document which is a preparatory

                action or measure. Long-term provision is expired beyond one accounting PeriodAsByte.

    

    LongTermProvisionsBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LossAdjustmentExpenseIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Losses generally refer to (1) the amount of reduction in the value of an insured's property caused by an insured peril, (2) the amount

                sought through an insured's claim, or (3) the amount paid on behalf of an insured under an insurance contract.  Loss Adjustment

                Expenses is expenses incurred in the course of investigating and settling claims that includes any legal and adjusters' fees and the

                costs of paying claims and all related expenses.

    

    LossAdjustmentExpenseIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LossonExtinguishmentofDebtIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Loss on extinguishment of debt is the accounting loss that results from a debt extinguishment. A debt shall be accounted for as

                having been extinguished in a number of circumstances, including when it has been settled through repayment or replacement by

                another liability. It generally results in an accounting gain or loss. Amount represents the difference between the fair value of the

                payments made and the carrying amount of the debt at the time of its extinguishment.

    

    LossonExtinguishmentofDebtIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class LossRatio(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A measure of operating performance for Insurance companies, as it shows the relationship between the premiums earned and the

                expenses related to claims. A number of 1 or lower is preferred, as this means the premiums exceed the expenses. Calculated as:

                Benefits, Claims and Loss Adjustment Expense, Net / Net Premiums Earned

    

    LossRatio(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    OneYear: float

    ThreeMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class MachineryFurnitureEquipmentBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Fixed assets specifically dealing with tools, equipment and office furniture. This item is usually not available for the insurance and

                utility industries.

    

    MachineryFurnitureEquipmentBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class MaintenanceAndRepairsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of maintenance and repair expenses in the current period associated with the revenue generation. Mainly

                for fixed assets. This item is usually only available for transportation industry.

    

    MaintenanceAndRepairsIncomeStatement(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    OneMonth: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    TwoMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class MaterialsAndSuppliesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Aggregated amount of unprocessed materials to be used in manufacturing or production process and supplies that will be

                consumed. This item is typically available for the utility industry.

    

    MaterialsAndSuppliesBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class MineralPropertiesBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    A fixed asset that represents strictly mineral type properties.  This item is typically available for mining industry.

    

    MineralPropertiesBalanceSheet(store: IDictionary[str, Decimal])
    """
    def GetPeriodValue(self, period: str) -> float:
        pass

    def SetPeriodValue(self, period: str, value: float) -> None:
        pass

    @staticmethod # known case of __new__
    def __new__(self, store: System.Collections.Generic.IDictionary[str, float]) -> None:
        pass

    NineMonths: float

    SixMonths: float

    ThreeMonths: float

    TwelveMonths: float

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]
