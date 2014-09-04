#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 15: Other Numeric Types"""

from decimal import Decimal
from fractions import Fraction

FLOATVAR = 0.1
DECIMALVAR = Decimal(0.1)
FRACTIONVAR = Fraction(1, 10)

DF_EQUALITY = (DECIMALVAR == FRACTIONVAR)
ARE_INEQUAL = (DECIMALVAR != FRACTIONVAR != FLOATVAR)
