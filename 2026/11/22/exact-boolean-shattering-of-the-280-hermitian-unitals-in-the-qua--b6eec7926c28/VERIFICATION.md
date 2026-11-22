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

# Reproduction of exact finite checks

Run `python3 verify_hermitian.py` using Python 3.10 or later. The observed successful output was:

```
HERM: 21 points; 280 nonsingular Hermitian unitals; six-set traces {64: 23520}
HERM: contained-support census [21, 210, 1330, 5880, 17640, 23520, 10080, 2520, 280]
HERM: five-set multiplicity Counter({2: 17640})
HERM: six-set multiplicity Counter({1: 23520})
```

Independently compile `verify_triangles.cpp` with `c++ -O3 -std=c++17 verify_triangles.cpp -o verify_triangles` and run `./verify_triangles`. The observed successful output was:

```
TRIANGLES: 21 points, 21 lines, 280 unitals
SHATTERED: 1 21 210 1330 5880 17640 23520 (higher 0)
FULL-TRACES: all 23520 six-subsets; five-incidence multiplicity 2, six multiplicity 1
```

Both scripts contain assertions that reject incorrect intermediate counts. They reconstruct \(\mathbb F_4\) from polynomial multiplication, do not use a supplied incidence list and have no external package dependencies. The Python script also directly checks equality of the Hermitian and line-triangle constructions and separately computes every 64-trace support. The C++ script checks every support occurring inside a unital of cardinality one through nine. Larger subsets need not be enumerated for shattering because uniqueness of a unital through six contained points gives a formal seven-query obstruction, and the family is hereditary. The computation verifies the finite lemma only; it does not establish historical priority or larger-field analogues.
