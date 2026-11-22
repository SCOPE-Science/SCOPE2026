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

# Reproducibility and scope
The standalone \(\texttt{check_catalan_energy.py}\) uses Python 3's standard library and takes no input files. Execute \(\texttt{python3 check_catalan_energy.py}\) to reconstruct complete modular sum histograms for depths \(1\) through \(8\), independently compare the unit-support set to actual Catalan values for depths \(1\) through \(6\), and check all displayed maxima, minima, full energy identities, and cyclic digit-weight correlations.

Expected energy values, in increasing depth order: \(27,154,916,5488,32920,197512,1185064,7110376\). The checker outputs a final PASS line. Direct enumeration is a finite consistency check; the proof of all-depth identities and the singular continuous measure is mathematical and appears in RESULT.md. The external independent audit has not been performed.
