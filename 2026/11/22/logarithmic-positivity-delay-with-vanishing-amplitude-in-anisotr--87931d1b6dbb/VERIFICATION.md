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

# Reproducibility and verification

The derivation in `RESULT.md` is analytic. Its nonstandard steps consist of an explicit Boolean-character spectral decomposition, strict zero counting for an exponential polynomial, and a decreasing integral-factor inequality. No computer enumeration is used to prove uniqueness for the continuum of parameters.

Run `python CHECK.py` with Python 3's standard library to reproduce the supplementary checks. An extracted run passed **348** cases, separately constructing the weighted four-by-four Laplacian, diagonalizing it via Jacobi rotations, checking all kernel entries and row sums, testing strict root brackets and sign recovery, and sampling weak-coupling asymptotics. The checks are floating-point comparisons, not interval certificates and not substitutes for the proof.

The cutoff \(\alpha=1\) and the weak-edge limit \(a/b\to0\) are analytical boundaries. No claim is made for zero conductances inside the theorem: with an edge pair deleted, the graph disconnects and the positive-time classification changes discontinuously. The proposed originality comparison is bounded by the accessible historical material; independent validation has not been performed.
