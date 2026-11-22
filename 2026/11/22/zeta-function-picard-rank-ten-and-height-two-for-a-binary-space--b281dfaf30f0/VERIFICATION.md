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

The reproducible point counter enumerates complete finite fields through extension degree thirteen and uses a disjoint projective-chart decomposition, not Monte Carlo sampling. A separate direct evaluator exhaustively checks the original homogeneous equation for extension degrees one through five. The second script reconstructs the degree-22 Frobenius polynomial, checks the functional equation and factorization, verifies two unused extension traces, proves irreducibility of the degree-twelve factor via a finite-field gcd certificate, and checks its Newton polygon.

Execute from the directory containing the files:

```sh
g++ -O3 -std=c++17 verify_points.cpp -o verify_points
./verify_points > point_counts.txt
python3 verify_frobenius.py
```

All these checks completed without error. The height and Picard-rank conclusions additionally use standard proven theorems for K3 surfaces; the supplied finite computation alone does not establish those theorems. Independent audit has not been performed.
