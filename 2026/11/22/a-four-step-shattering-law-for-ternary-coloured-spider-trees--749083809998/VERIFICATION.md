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
# Reproducibility

The standalone script `spider_vc_certificate.py` is pure standard-library Python. Run it in this directory and compare its stdout with `spider_vc_verification_output.txt`.

The script reconstitutes exactly twenty feasible leaf-to-hub signatures at length four and checks that their transition graph stays closed. It computes every maximally feasible signature weight at lengths four and eight and verifies the entire twenty-entry vector identity \(D_8=D_4+3\), the finite certificate needed for an unlimited four-step induction. It also checks direct coloured-trace realization on 58,624 marked support instances across all seven sorted three-arm spiders with at most six edges outside the hub. The independently evaluated brute routine enumerates actual proper three-colourings and compares against the signature method, rather than repeating its hub recurrence for the comparison target. The equal-arm dimensions for lengths one through twelve and selected asymmetric extensions are checked as supplementary diagnostics.

No numerical sampling establishes the infinite result by itself: the independent variable is removed through the exact max-plus recurrence and its translation symmetry. The test script does not constitute external formal verification or an independent mathematical audit, and no claim is made for other palettes or trees with more than three arms.
