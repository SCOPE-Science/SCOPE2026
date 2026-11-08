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

The analytic proof establishes convergence by an exact geometric-series identity, oscillatory averaging, and the pointwise bound \(\big||K_{n,j}|-|D_n|\big|\le1\). It proves the first interior constant positive via elementary inequalities. Run `python verify_notch.py` to replay the finite identity tests and the quantitative quadrature check; the program needs NumPy. The quadrature only confirms the positive numerical scale and is not treated as an infinite-band proof. The displayed decimal for the integral is not a formally rounded enclosure.
