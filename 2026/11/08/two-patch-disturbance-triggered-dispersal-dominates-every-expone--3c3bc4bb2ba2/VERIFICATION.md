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

# Reproducibility and limits

Execute `python CHECK.py` from this directory with Python 3.10+ and SymPy. All 127 assertions in the packaged checker passed on the checked version. The decisive all-discount identity was verified symbolically by subtracting the independently constructed two- and three-state resolvents from its positive-factor form. Separate five-state labelled-patch generators were generated from local transition rules and their exact discounted survival values compared with the symmetry-reduced generators for multiple rational parameter configurations and discounts.

For the pointwise survival witness, the checker uses exact `Fraction` arithmetic rather than floating-point matrix exponentials. With uniformization rate \(8\) at deadline \(t=2\), the partial coefficient sum through \(n=80\) obeys \(-98<W_{80}<-97\), and a geometric tail envelope is less than \(1/1000\). Thus the sign of the true survival difference is rigorously negative.

The general theorem depends on the matrix derivation, finite-state transience, and positivity of an explicit polynomial for all stated parameters. Numerical examples alone would not establish it. No external independent audit or empirical calibration was performed. The theorem does not assert deterministic-time survival ordering and does not extend automatically to three or more patches.
