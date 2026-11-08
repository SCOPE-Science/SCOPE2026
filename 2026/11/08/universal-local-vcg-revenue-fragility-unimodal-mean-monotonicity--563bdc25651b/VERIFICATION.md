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

The mathematical derivations use the two-bidder VCG externality identity and integration of an explicit triangular difference density. `checker.py` is executable from the extracted package with Python 3 and SymPy and performs exhaustive finite-grid externality comparisons (7,776), symbolic integration checks (nine identities), and uniform-model numerical sanity comparisons (700,000), plus an exact two-peak comparison and 120,000 atomless bimodal simulations. These finite and numerical checks do not establish the continuous theorem; analytical arguments in `RESULT.md` do. Distribution-free assumptions are item exchangeability within rows, iid rows and atomless row differences. The general mean-revenue result assumes a symmetric unimodal gap density, and the explicit atomless bimodal model witnesses the need for an additional shape condition. The finite-shock functions additionally require iid Uniform\((0,1)\) cells and no truncation of the shocked entry. Independently performed audit: none.
