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

# Verification notes

The proof reduces any real zero of \(\sum_j w_j e^{-2\pi i\xi\cdot c_j}\) to closing three complex vectors of prescribed positive lengths. Strict triangle inequalities give exactly two relative phase configurations, related by complex conjugation. The external angles of the weight triangle give a shortest circular covering arc of \(\pi+\gamma_*\); projecting the sites proves the diameter lower bound. Conversely, choosing three planar site projections to realize that shortest arc with a diameter edge proves sharpness without collinearity. Solving the rank-two phase congruences establishes the full affine lattice formula and its Euclidean least-norm minimization. These are symbolic arguments valid for all claimed frequencies and weights, not a numerical extrapolation.

To replay supplementary tests, save the embedded files with their relative paths and run `python3 checks/tri_atomic_zeros.py`. The program depends only on Python's standard library, uses a deterministic seed, and checks phasor cancellation, 500 random weighted noncollinear configurations, explicit equality cases and nontriangle lower estimates. It does not exhaust continuous parameters or prove the theorem.

Scientific limitations: exact arithmetic proof is in RESULT.md; the checker uses floating-point evaluations, so numerical agreement is merely corroborative. The zero-coset formula applies to rank-two triples; collinear triples may have no real zeros. No assertion is made for complex weights, nonreal frequencies, or four or more atoms. Independent mathematical validation has not been conducted.
