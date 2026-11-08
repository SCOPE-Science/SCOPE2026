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
Run `python verify_triangle_osborne.py` with Python 3. The recorded output is `PASS 10005 exact-geometry and numerical-matrix checks`.

The program exhausts all sequences of update indices through length eight, conditioned on each first index, in exact rational arithmetic. It checks that the number of paths with a given number of switches equals \(\binom{n-1}{k}2^k\), and that each path has the expected norm-squared contraction. It separately checks preservation of the product of the three matrix edge weights and agreement of actual Osborne updates with the logarithmic projections on three numerical inputs.

The checked finite lengths are not an exhaustive proof of the infinite-time law. The proof uses the three pairwise projection angles, independence of the switch indicators and geometric waiting-time limit theory. The \(\ell_1\)-residual CLT depends on the stated generic condition and an analytic uniform norm comparison. No independent verification has been performed.
