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

# Verification of exact critical-coupling identities

The proof uses a common \(H^2\oplus\mathbb C^2\) realization and reconstructs the multiplier model, the rank-two defect and its logarithmic-concavity slack. The necessary complete-Pick obstruction is a degree-two/three coefficient matrix of a congruent normalized kernel. Exact algebra gives \(\det D_b=(a^2-1)^2-b^2\), \(\det E_b=-a^6b^2\), and \(\det[\widehat Q_b(i,j)]_{i,j=2,3}=-b^2/a^4\). The positive CNP case at \(b=0\) is proved by a nonnegative rational generating-function recurrence, not by numerical evidence.

Run `python checker.py` with Python 3 and the standard library only. The checker regenerates the finite coefficient matrix by independent bivariate polynomial multiplication truncated at degree three, verifies both defect determinants, and checks 53 admissible exact rational parameter pairs. It also samples finitely many recurrence terms as a supplementary guard. The checker is a regression test, not a proof for the continuum of parameters.

No independent audit has been performed. The endpoints \(|b|=a^2-1\), nonreal \(b\), and general rank-two defect shifts are outside the theorem.
