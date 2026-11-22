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

The proof establishes the exact complete spectrum for every prime power \(q\) and every \(n\ge4\). The standalone file `check_spectrum.py` independently constructs adjacency matrices from the defining projective incidence relation over prime fields and checks all eigenvalues (with multiplicities) and valencies for \((n,q)=(4,2),(4,3),(5,2)\). The attached `check_output.txt` is the actual output of this execution with `OPENBLAS_NUM_THREADS=1`. NumPy is required for replay. Full generality is analytic; floating-point outputs are supplementary checks. Neither expert review nor independent audit has been performed.
