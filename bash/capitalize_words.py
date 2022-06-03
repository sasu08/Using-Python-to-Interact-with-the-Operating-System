#!/usr/bin/env python3

# Ejecutar text.txt | ./capitalize_words.py

import sys

for line in sys.stdin:
    words = line.strip.split()
    print(' '.join([word.capitalize() for word in words]))