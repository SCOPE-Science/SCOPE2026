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
# Reproduction and scope

In a directory containing `verify_exhaustive.py`, `verify_independent.cpp`, and `isomorphism_certificate.json`, run:

```
python3 verify_exhaustive.py
c++ -std=c++17 -O2 verify_independent.cpp -o check
./check
```

The first command tests all 512 candidate subsets of \(C_3\square C_3\) and all 4,096 candidate subsets of \(C_3\square C_4\) by cardinality, then enumerates all minimum-code jumps/slides and checks the 120-coordinate certificate. The second command independently recomputes minimum size, counts, move edges and component shape by integer-neighborhood bitmasks. The expected outputs are provided verbatim in `verify_exhaustive.log` and `verify_independent.log`. Both were executed from these source paths. No assertion is made for larger cyclic orders or independent third-party audit.
