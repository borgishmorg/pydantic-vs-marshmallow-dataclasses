from decimal import Decimal
from enum import Enum, unique
from timeit import timeit
from uuid import UUID

from pydantic import Field, RootModel
from pydantic.dataclasses import dataclass

from .common import ATTEMPTS, DESERIALIZED_ORDER


@unique
class OrderStatus(Enum):
    NEW = "new"
    SUCCESS = "success"
    FAIL = "fail"


@dataclass
class Item:
    id: str
    title: str
    quantity: Decimal = Field(ge=Decimal("0"), decimal_places=3)
    price: Decimal = Field(ge=Decimal("0"), decimal_places=2)


@dataclass(kw_only=True)
class Cart:
    id: str | None = None
    items: list[Item]


@dataclass
class Order:
    id: UUID
    status: OrderStatus
    cart: Cart
    metadata: str | None = None

OrderModel = RootModel[Order]

if __name__ == "__main__":
    order = Order(**DESERIALIZED_ORDER)
    assert OrderModel(order).model_dump(mode="json") == DESERIALIZED_ORDER

    load_time = timeit(lambda: Order(**DESERIALIZED_ORDER), number=ATTEMPTS)

    dump_time = timeit(lambda: OrderModel(order).model_dump(mode="json"), number=ATTEMPTS)

    order_model = OrderModel(order)
    dump_no_model_time = timeit(lambda: order_model.model_dump(mode="json"), number=ATTEMPTS)

    print(f"pydantic load time: {load_time:.6}s")
    print(f"pydantic dump time: {dump_time:.6}s")
    print(f"pydantic dump (no model) time: {dump_no_model_time:.6}s")
