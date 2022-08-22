from decimal import Decimal
from typing import Optional
from enum import Enum
from pydantic import BaseModel
from datetime import date


class OpetationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OpertationBase(BaseModel):
    date: date
    kind: OpetationKind
    amount: Decimal
    description: Optional[str]


class Operation(OpertationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OpertationBase):
    pass

class OperationUpdate(OpertationBase):
    pass
