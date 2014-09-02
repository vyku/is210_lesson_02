#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import expectation

TOKEN = "Spanish"
INDEX = expectation.FISHY.index(TOKEN)
FLEMISH = expectation.FISHY[:INDEX] + "Flemish" + expectation.FISHY[INDEX + len(TOKEN):]
