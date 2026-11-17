# Reproduction

Requirements: a C++17 compiler, Python 3.10 or later, and SymPy for the optional symbolic determinant check.

From the package root:

```sh
g++ -std=c++17 -O2 checks/sweep184.cpp -o /tmp/sweep184-check
/tmp/sweep184-check
python3 checks/transfer.py
python3 checks/symbolic.py
```

The first program performs an independent exhaustive evaluation of the original sequential rule, the three image constraints, and the constructive inverse, for every circumference from three through eighteen. The second evaluates the integer transfer matrices and the recurrence. The third checks the rational determinant identity exactly. The corresponding `.out` files record the expected output. The all-circumference theorem is established mathematically in `RESULT.md`; the programs are bounded verification aids.
