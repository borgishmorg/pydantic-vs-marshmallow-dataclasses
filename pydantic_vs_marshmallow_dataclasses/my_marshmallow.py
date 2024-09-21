from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum, unique
from timeit import timeit
from uuid import UUID

from marshmallow import fields, validate
from marshmallow_dataclass import class_schema

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
    quantity: Decimal = field(metadata={
        "marshmallow_field": fields.Decimal(places=3, as_string=True),
        "validate": validate.Range(Decimal("0")),
    })
    price: Decimal = field(metadata={
        "marshmallow_field": fields.Decimal(places=2, as_string=True),
        "validate": validate.Range(Decimal("0")),
    })


@dataclass(kw_only=True)
class Cart:
    id: str | None = None
    items: list[Item]


@dataclass
class Order:
    id: UUID
    status: OrderStatus = field(metadata={"by_value": True})
    cart: Cart
    metadata: str | None = None


OrderSchema = class_schema(Order)()


if __name__ == "__main__":
    order = OrderSchema.load(DESERIALIZED_ORDER)
    assert OrderSchema.dump(order) == DESERIALIZED_ORDER

    load_time = timeit(lambda: OrderSchema.load(DESERIALIZED_ORDER), number=ATTEMPTS)
    dump_time = timeit(lambda: OrderSchema.dump(order), number=ATTEMPTS)

    print(f"marshmallow load time: {load_time:.6}s")
    print(f"marshmallow dump time: {dump_time:.6}s")
