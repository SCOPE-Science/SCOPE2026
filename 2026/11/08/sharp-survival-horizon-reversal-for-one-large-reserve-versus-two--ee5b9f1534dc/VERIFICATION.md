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

# Computational verification and limits

The attached `verify.py` is standalone; run `python verify.py` with `sympy` and `mpmath` available. It computes the 2-by-2 transient Markov resolvent *directly* and compares it symbolically to the analytic survival transform. Its exact symbolic assertions include the threshold identities and the \(e\)-width gap. It separately compares direct matrix-exponential survival values with the closed formula for 30 distinct rational rate pairs at five strictly positive times each, and checks the explicit ranking-reversal example. In the packaged run it reported `PASS 401 exact symbolic/numerical assertions` and a normalized crossover time of approximately `2.0154308462756488843`.

The finite computational grid is supplementary. The proof of all-deadline dominance and exactly one crossing uses the analytic derivative of the two-state hazard; it does not rest on numeric extrapolation. The rate law and statistical independence are premises, not experimentally validated facts. Historical originality still requires independent review, particularly because some nearby journal full texts were inaccessible.
