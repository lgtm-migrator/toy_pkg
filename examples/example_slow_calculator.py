"""
Slow example
============

This example also runs useless computations but mimics
a slow example by using the lazy versions of the calculator
module.
"""

#########################################################
# Load functions
from toy_pkg.lazy_calculator import lazy_add, lazy_subtract

#########################################################
# Perform some relatively long computations
#
# Perform 1 + 1 and sleep for 10 seconds...
result = lazy_add(1, 1, 10)
assert result == 2

# Perform 10 - 7 and sleep for 10 seconds...
result = lazy_subtract(10, 7, 10)
assert result == 3
