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

# Reproducible verification

With SymPy 1.14.0, run `python verify.py`. It reconstructs the four-dimensional quotient and each of the seven distinct entry formulas, checks all 28 exact positive-root counts using Sturm's theorem and the positivity of their denominators, confirms the all-branch negative witness after \(m=6+t,h=10\), and compares the orbit formulas against 105 exact entries of full Laplacian rational matrices. The direct checks span integers \(m=2,3,4,5,6\) and three strictly positive rational steps; the unbounded claims are established by the symbolic polynomial and spectral/Taylor arguments, not by these finite checks. Internal stages and arbitrary graph topologies are not verified. Independent audit remains unperformed.
