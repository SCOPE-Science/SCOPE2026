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

# Reproducible exact checks

The all-length theorem follows from the disjoint-occurrence inclusion–exclusion proof in `RESULT.md`. Its nonstandard ingredients are the unique maximum-packing witness and the parity sum of all maximum packings at residue one; both are proved there, not assumed from experiments.

To replay the independent finite checks in an environment with Python 3 and a C++17 compiler:

```sh
python3 check_fwht.py
c++ -std=c++17 -O2 check_inclusion.cpp -o check_inclusion
./check_inclusion
```

Expected messages:

```text
FWHT_OK: 528 complete spectra, all divisibility/gap/parity tests passed
INCLUSION_OK: 12276 direct character sums equal inclusion-exclusion, sharp witnesses verified
```

The Python checker uses direct forbidden-factor membership and an integer Walsh–Hadamard transform, checks Parseval and all claimed modular and sharp gap invariants for all binary unbordered words of pattern lengths two through six and ambient lengths one through twelve. The C++ checker computes coefficients via disjoint-interval inclusion–exclusion and also via a separate direct character sum over admissible words for six patterns and lengths one through ten. It checks the full-prefix witness value. Both programs passed when executed from these exact source files.

No finite check certifies the universal quantifiers. Neither a formal proof-assistant certificate nor an external mathematical audit is asserted. The full zero set for nonmultiple lengths and any conclusion for bordered patterns remain outside scope.
