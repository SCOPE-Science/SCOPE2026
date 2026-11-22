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

The complete proof uses simple-root Hensel lifting, disjoint root residue classes, and exact intersections of nested prime-adic balls; it is valid for every odd prime and every positive depth.

Run `python verify.py` (standard library only) to reproduce eleven exact-integer finite-index tests at primes 3, 5, and 7. The tests check 1,228 marginal-tail, mixed-tail, and cross-moment identities through depths four to six, including quadratic pairs irreducible over the rationals, exact shared roots, a root separation of depth two, and both signs of covariance. All tests passed in this package preparation.

The finite checks are corroboration only; the infinite and all-prime assertions rest on the proof in `RESULT.md`. No outside independent audit or certification is claimed. The result assumes every root modulo the prime is simple and does not treat repeated-root valuation trees.
