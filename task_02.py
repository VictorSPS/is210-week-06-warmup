#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Interacting with an existing list and using
   operators del, slice, append and extend.
"""

import data
BALLETS = data.BALLETS

del BALLETS[11]
BALLETS[2] = 'Swan Lake'
BALLETS.append('Herman Schmerman')
BALLETS.extend(['Don Quixote', 'Sylvia'])
