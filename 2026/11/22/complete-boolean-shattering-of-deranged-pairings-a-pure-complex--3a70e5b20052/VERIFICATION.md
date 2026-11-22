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

# Verification

Run `python3 verify_cocktail_shattering.py` from the directory containing the code. Python 3 standard library suffices. The program uses recursive first-unmatched-vertex enumeration to generate all complete pairings, separately uses Boolean hypothesis bitsets to realize query labels, and checks the structural and inclusion-exclusion formulas.

The completed run enumerated every edge-query support of size at most \(n-1\) for \(n=2,3,4,5\), totaling 104,500 supports. For each support of size at most \(n-2\) it additionally verified every labeling, including all-positive, all-negative, and inconsistent-positive configurations on supports with intersecting edges. It reproduced the all-degree face polynomials and the perfect-matching count from inclusion-exclusion, finishing with `COCKTAIL_TRACE_PASS 104500 direct support checks`.

The general proof relies on the residual minimum-degree argument, Dirac's theorem, a four-vertex one-factorization, and a top-face completion bijection. The finite exhaustive checks do not prove the unrestricted result and should not be mistaken for an independent mathematical audit. No independent audit has been performed.
