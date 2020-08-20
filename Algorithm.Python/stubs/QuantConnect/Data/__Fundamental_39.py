from .__Fundamental_40 import *
import typing
import System.IO
import System.Collections.Generic
import System
import QuantConnect.Data.Fundamental
import QuantConnect.Data
import QuantConnect
import datetime


class MorningstarSectorCode(System.object):
    """ Helper class for the AssetClassification's MorningstarSectorCode field QuantConnect.Data.Fundamental.AssetClassification.MorningstarSectorCode. """
    BasicMaterials: int
    CommunicationServices: int
    ConsumerCyclical: int
    ConsumerDefensive: int
    Energy: int
    FinancialServices: int
    Healthcare: int
    Industrials: int
    RealEstate: int
    Technology: int
    Utilities: int
    __all__: list


class MortgageAndConsumerloansBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    It means the aggregate amount of mortgage and consumer loans.  This item is typically available for the insurance industry.

    

    MortgageAndConsumerloansBalanceSheet(store: IDictionary[str, Decimal])
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


class MortgageLoanBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a lien on real estate to protect a lender.  This item is typically available for bank industry.

    

    MortgageLoanBalanceSheet(store: IDictionary[str, Decimal])
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


class NaturalGasFuelAndOtherBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The amount for the natural gas, fuel and other items related to the utility industry, which might include oil and gas wells, the

                properties to exploit oil and gas or liquefied natural gas sites.

    

    NaturalGasFuelAndOtherBalanceSheet(store: IDictionary[str, Decimal])
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


class NegativeGoodwillImmediatelyRecognizedIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Negative Goodwill recognized in the Income Statement. Negative Goodwill arises where the net assets at the date of acquisition,

                fairly valued, falls below the cost of acquisition.

    

    NegativeGoodwillImmediatelyRecognizedIncomeStatement(store: IDictionary[str, Decimal])
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


class NetBusinessPurchaseAndSaleCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net change between Purchases/Sales of Business.

    

    NetBusinessPurchaseAndSaleCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetCashFromDiscontinuedOperationsCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The net cash from (used in) all of the entity's discontinued operating activities, excluding those of continued operations, of the

                reporting entity.

    

    NetCashFromDiscontinuedOperationsCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetCommonStockIssuanceCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The increase or decrease between periods of common stock.

    

    NetCommonStockIssuanceCashFlowStatement(store: IDictionary[str, Decimal])
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


class NetDebtBalanceSheet(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    This is a metric that shows a company's overall debt situation by netting the value of a company's liabilities and

                debts with its cash and other similar liquid assets. It is calculated using [Current Debt] + [Long Term Debt] - [Cash and Cash

                Equivalents].

    

    NetDebtBalanceSheet(store: IDictionary[str, Decimal])
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


class NetForeignCurrencyExchangeGainLossCashFlowStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate amount of realized and unrealized gain or loss resulting from changes in exchange rates between currencies.

                (Excludes foreign currency transactions designated as hedges of net investment in a foreign entity and inter-company foreign

                currency transactions that are of a long-term nature, when the entities to the transaction are consolidated, combined, or accounted

                for by the equity method in the reporting entity's financial statements. For certain entities, primarily banks, which are dealers in

                foreign exchange, foreign currency transaction gains or losses, may be disclosed as dealer gains or losses.)

    

    NetForeignCurrencyExchangeGainLossCashFlowStatement(store: IDictionary[str, Decimal])
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

    Store: typing.List[QuantConnect.Data.Fundamental.PeriodField]


class NetForeignExchangeGainLossIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    The aggregate foreign currency translation gain or loss (both realized and unrealized) included as part of revenue. This item is

                usually only available for insurance industry.

    

    NetForeignExchangeGainLossIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeCommonStockholdersIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Net income minus the preferred dividends paid as presented in the Income Statement.

    

    NetIncomeCommonStockholdersIncomeStatement(store: IDictionary[str, Decimal])
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


class NetIncomeContinuousOperationsIncomeStatement(QuantConnect.Data.Fundamental.MultiPeriodField):
    """
    Revenue less expenses and taxes from the entity's ongoing operations and before income (loss) from: Preferred Dividends;

                Extraordinary Gains and Losses; Income from Cumulative Effects of Accounting Change; Discontinuing Operation; Income from Tax

                Loss Carry forward; Other Gains/Losses.

    

    NetIncomeContinuousOperationsIncomeStatement(store: IDictionary[str, Decimal])
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
