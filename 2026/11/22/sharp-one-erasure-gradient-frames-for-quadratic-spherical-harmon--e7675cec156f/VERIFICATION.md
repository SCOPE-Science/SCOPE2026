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

# Reproduction and scope of verification

`check.py` is a standalone NumPy program. Run `python check.py`. It builds an orthonormal trace-free symmetric matrix basis, constructs regular simplex coordinates from the symmetric projector, and assembles intrinsic tangent gradients at every retained vertex. Complete numerical Gram spectra were matched for intact and one-vertex-deleted frames in every dimension from \(d=3\) through \(d=9\). For every one of those dimensions, all numbers of retained vertices \(1\le k<d\) were separately tested for the predicted nullity \((d-k)(d-k+1)/2\). The recorded output contains seven successive `PASS` lines.

The separate reproducible `symbolic_check.py` uses SymPy to verify the paired-block trace, determinant and discriminant against their factored rational formulas in the theorem; run `python symbolic_check.py` and expect `SYMBOLIC_IDENTITIES_PASS`. These finite evaluations and algebraic checks corroborate the written all-dimensional proof; neither finite numerical testing nor symbolic simplification alone establishes the nullity classification or the spectral theorem. The proof's nonstandard steps are the cross-sector projection identity and the exact paired-plane decomposition, both derived explicitly in `RESULT.md`.

No outside expert or independent mathematical audit was performed.
