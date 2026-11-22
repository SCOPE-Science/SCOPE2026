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

The reproducibility program `verify_transport.py` uses exact fractions to test the identities, margin constraints, nonnegativity, and degree counts. Its optional numerical optimization checks use SciPy to solve feasible masked rectangular transportation problems and compare their distances to the proved lower bounds. Run `python verify_transport.py` from the directory containing this file. The program reports `RECTANGULAR_TRANSPORT_FACE_PASS` if successful. The code was run against its actual embedded-file contents after packaging; both finite numerical and exact diagnostics are not infinite proofs. The analytical proof is in `RESULT.md`. Source priority outside the inspected literature is not independently established.
