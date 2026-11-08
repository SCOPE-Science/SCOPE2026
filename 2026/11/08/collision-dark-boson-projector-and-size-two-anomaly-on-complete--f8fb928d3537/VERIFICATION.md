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

# Verification record

The analytic proof in `RESULT.md` is the verification of every integer \(a,b\ge2\). Exact finite checkers are included as reproducible regression tests and do not certify the infinite statement independently.

From the directory containing this file, with Python and `sympy` installed, execute:

```
python verification/check_biclique.py
python verification/check_krylov.py
```

The first constructs the physical distinct-pair projector as a rational matrix, verifies \(P^2=P=P^\mathsf T\), verifies annihilation by the complete hopping generator, and checks exact ranks and capture probabilities for \((a,b)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)\).

The second independently constructs the full symmetric-pair hopping operator in a rational, generally unnormalized coordinate basis. Its stacked collision-observation operators at powers zero through four determine the entire dark subspace by exact row rank, for \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). Five powers suffice because the symmetric two-body Hamiltonian has at most five distinct energies. The test does not rely on the analytic projector construction.

Observed terminal check markers: `BICLIQUE_EXACT_OK` and `KRYLOV_INDEPENDENT_OK`. Both scripts were run against their embedded source contents during the package verification. There is no claim of external validation, proof assistant certification, general numerical enumeration, or experimentally measured loss.
