#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

FISHY = inquisition.SPANISH.replace("surprise", "haddock")

TOKEN = "Spanish"
LEN = len(TOKEN)
IDX = FISHY.index(TOKEN)
FLEMISH = FISHY[:IDX] + "Flemish" + FISHY[IDX + LEN:]