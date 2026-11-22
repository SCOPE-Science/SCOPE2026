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

The mathematical proof in `RESULT.md` is complete conditional on the classical finite Coxeter Eulerian polynomial formulas and the standard classification of finite irreducible Coxeter groups. The standalone `verify.py` independently enumerates the complete signed-permutation type-B and type-D descent distributions at ranks four through seven and compares every Fourier character with the induced-even-component criterion and Fibonacci rank. It also exhaustively checks all labelled subcubic trees with at most five vertices and the degree-four star counterboundary. The verifier is not offered as a proof for infinite orders; the parabolic factorization and parity-boundary recursion supply the proof.

Limitations: no complete all-order multiplier distribution, no inverse norm, no independent mathematical audit or proof that an unindexed equivalent does not exist.
