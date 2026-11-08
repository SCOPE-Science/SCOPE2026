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

The analytic derivation in `RESULT.md` covers the continuum of \(0<h<2\), all \(p\in(0,1)\) where stated, every finite iteration for fair sampling, and the exact alternating stability threshold. It does not rely on extrapolating finite computational observations.

The standalone file `verify.py` uses Python's standard-library `fractions.Fraction` to perform exact-rational matrix checks for the two constituent maps, equal-weight conditional Gram identity, covariance transfer characteristic determinant at rational parameter grids, all sample paths through eight steps for selected initial vectors, and alternating trace classifications. Running `python3 verify.py` against the supplied file printed: `PASS: 1302 exact-rational assertions`.

These calculations are not an independent audit, do not prove algebraic identities for real parameter continua by themselves, and do not prove literature novelty. No computer-assisted infinite/exhaustive certification is asserted.
