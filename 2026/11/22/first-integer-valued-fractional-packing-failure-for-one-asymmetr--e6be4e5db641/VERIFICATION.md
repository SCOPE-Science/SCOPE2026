---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

The following two standalone methods rederive the finite census and check exact certificates:

```
python3 CHECK.py
g++ -O2 -std=c++17 ALTERNATE.cpp -o alternate
./alternate
```

`CHECK.py` requires only standard-library modules and the accompanying `CERTIFICATES.json`. It enumerates every constrained word of lengths one through seven, constructs each error shadow from individual downward flips, independently compares compatibility to directed support differences, enumerates all maximal cliques, checks the ten optimal codebooks and their reversal statistics, and verifies every primal and dual rational inequality and objective using arbitrary-precision fractions. The size counts and fractional values are proved only within this finite range.

`ALTERNATE.cpp` independently constructs the length-seven graph from integer bitmasks, enumerates every maximal compatible clique, and checks the optimum, the number of maximizers, the common core and reversal-fixed maximizers. It does not read the Python graph or use its implementation.

The expected terminal output markers are `VERIFY_OK` and `ALTERNATE_OK`. The search terminates when the candidate/excluded sets have been exhausted; a timeout, sampling run or solver status alone is not used as mathematical evidence. The primal/dual witnesses are exact rational numbers, not floating-point tolerances. These checks provide an inspectable computational certificate, not an independently performed mathematical audit.
