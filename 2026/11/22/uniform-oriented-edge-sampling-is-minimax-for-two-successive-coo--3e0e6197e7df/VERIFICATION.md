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

## Reproduction

With Python 3 and this finding's `verify.py` in the same directory, execute `python3 verify.py`. It uses only the standard library and exact rational arithmetic. The observed result is: `PASS: 45 graph/coupling cases, exact rational pair and matrix identities, spectra inequalities.`

The script tests cyclic, complete, complete bipartite, cube, and Petersen graphs with three rational coupling strengths each. For each case it evaluates every ordered pair of coordinates including repeated pairs; reconstructs expected squared-energy loss from actual update matrices; verifies the spectral formula and equality restrictions; and checks the factorization on 25 rational spectral arguments. These finite checks cannot establish a claim for arbitrary graphs. The universal quantifiers are discharged by the explicit energy identity, the constant-vector obstruction, adjacency simultaneous diagonalization, and the positive factorization in `RESULT.md`.

The unconditional self-review was completed; no external or independent validation has been carried out. Novelty remains subject to further literature review.
