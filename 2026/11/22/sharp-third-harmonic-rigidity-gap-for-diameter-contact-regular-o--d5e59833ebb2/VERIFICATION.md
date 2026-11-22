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
# Reproduction and limits

In an extracted package, run `python3 verify.py`. The standalone verifier uses only Python standard-library `math` and an independent Cartesian rigidity-matrix construction. It checks full eigenvalue agreement at five odd orders, the three-dimensional motion kernel, 148 third-mode selections in odd sizes 7 through 301, determinant identities, and the rate approaching the stated algebraic constant. It reports 233 finite assertions passed; the package captures the implementation rather than an unverifiable external log.

The infinite proof uses the chord-derivative formula, explicit parity determinants, fixed-frequency limits and uniform exclusion of growing frequencies. Finite tests are corroboration only. Independent external audit is not performed. No external certification or repository update is asserted.
