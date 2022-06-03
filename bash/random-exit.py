#!/usr/bin/env python

# Ejecutar ./retry.sh ./random-exit.py
import sys
import random

value=random.randint(0, 3)
print('Returning: ' + str(value))
sys.exit(value)