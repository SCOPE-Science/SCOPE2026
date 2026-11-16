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

Run `python check_icosahedral_cubic.py` in the extracted package with Python 3, NumPy and SymPy. The script asserts symbolic conference-matrix squaring and the associated eigenvalue multiplicities; checks the exact Funk--Hecke integral \(a_6(c)\), its two nontrivial roots, and the degree-two/four icosahedral design moments. It independently forms and compares the full seven-by-seven cap Gram matrices at seven thresholds using deterministic rotated spherical quadrature.

In the completed replay the largest recorded seven-threshold spectral discrepancy was below \(5\times10^{-15}\); the checker ended with `ICOSAHEDRAL_CUBIC_CAP_PASS point_conference=6x6 moment_degrees=2,4 cap_tests=7 tight_radii=2`.

The theorem covers every \(0<c<1\) by proof, not by finite testing. Limits: no independent audit or formal theorem prover; no classification for other center sets, non-mixture unions, or other harmonic degrees. The point-vanishing subspace is an established result credited to Hitchin.
