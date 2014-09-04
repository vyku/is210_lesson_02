#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import expectation

TOKEN = "Spanish"
LEN = len(TOKEN)
IDX = expectation.FISHY.index(TOKEN)
FLEMISH = expectation.FISHY[:IDX] + "Flemish" + expectation.FISHY[IDX + LEN:]
		  
print FLEMISH