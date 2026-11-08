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

Run `python verify.py` with SymPy (see `requirements.txt`). The program constructs \(M_n\) and the exact \(p_{n,r}\) polynomials, then checks five disjoint-triple cubic conditions and three conditions for each of the two intersecting-triple quadratics, all in exact arithmetic after substituting \(n=9+t\). Strictly positive numerator coefficients and strictly positive denominators certify every parameter \(n\ge9\); no finite sampling is extrapolated to infinity. It separately builds the actual Kneser adjacency graph for \(n=9,10,11\) and checks 1,845 entries of its first five adjacency powers against recurrence predictions. Observed output: `VERIFY_OK 11 universal shifted-sign certificates; 1845 direct adjacency-power entries; positivity for all integer n>=9`. Independent validation has not been performed.
