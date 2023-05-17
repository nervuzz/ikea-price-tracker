from decimal import Decimal

from pydantic import BaseModel, HttpUrl


class Category(BaseModel):
    name: str
    key: int
    url: HttpUrl
    imageUrl: HttpUrl


class ProductAvailability(BaseModel):
    type2: str
    status: str
    store: str | None


class CurrentPrice(BaseModel):
    prefix: str
    wholeNumber: str
    separator: str
    decimals: str
    suffix: str
    isRegularCurrency: bool


class SalesPrice(BaseModel):
    currencyCode: str
    numeral: Decimal
    isBreathTaking: bool
    discount: str
    current: CurrentPrice


class Product(BaseModel):
    id: str
    name: str
    typeName: str
    mainImageUrl: HttpUrl
    contextualImageUrl: HttpUrl
    pipUrl: HttpUrl
    itemNo: str
    itemNoGlobal: str
    availability: list[ProductAvailability]
    ratingValue: float
    ratingCount: int
    salesPrice: SalesPrice


class ProductListPage(BaseModel):
    category: Category
    productWindow: list[Product]
    productCount: int
    plannerWindow: list[str | int | None]
    plannerCount: int
    # filters2: list
    # sortOrders: dict


class IKEApiResponse(BaseModel):
    usergroup: str | list[str | int | None]
    testActivationTriggers: dict
    productListPage: ProductListPage
