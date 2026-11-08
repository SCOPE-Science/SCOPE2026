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
# Verification scope

The accompanying `verify.py` uses integer root-residue counts, not floating-point thresholds. Actual executed output:
```
SPARSE_CHIRP_CYCLOTOMIC_PASS cases= 331112
BOUNDARY_VANISHING_EXAMPLE 5 U [2, 3] u 1 v 3
BOUNDARY_VANISHING_EXAMPLE 7 U [0, 3, 4] u 1 v 0
BOUNDARY_VANISHING_EXAMPLE 11 U [4, 5, 6, 7] u 1 v 7
SPARSE_CHIRP_BOUNDARY_PASS examples=3
```

This exact program exhausts all eligible subsets for primes 5, 7 and 11 and tests seeded finite samples in 13, 17 and 19. For prime \(p\), the cyclotomic polynomial \(1+t+\cdots+t^{p-1}\) implies that a root sum with integer coefficients vanishes if and only if its \(p\) residue counts are equal. The program tests precisely that condition. No finite computation proves the theorem for unbounded primes; see the symbolic proof for the uniform statement.

The spectral lifting formula and the cyclotomic norm argument were checked mathematically and are not computationally certified. Independent audit has not been performed.
