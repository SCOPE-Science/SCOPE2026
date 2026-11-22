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

Execute `python3 CHECKER.py`. The code has no external package dependencies, no network calls, and uses only integer dictionary operations for multivariate homogeneous polynomials. Expected successful output is present in `CHECKER_OUTPUT.txt`.

The checker reconstructs all 13 residue triple sums from ordered triples in the Singer difference set; forms the exact polynomial \(85(\sum a_i^2)^3-16\sum T_m(a)^2\); verifies its 24 order chambers; and tests the strictly positive coefficient constraints that prove the global magnitude inequality and its unique equality case. It also checks the three equal-residue triple-sum relations and the coherence of the 13 cyclic-character phases.

Limits: integer symbolic checks establish the stated complete finite expansion, not an a priori general result for other difference sets or Fourier moments. The external arXiv papers were examined for comparison, not used as premises in the finite arithmetic proof. No independent audit has been performed.
