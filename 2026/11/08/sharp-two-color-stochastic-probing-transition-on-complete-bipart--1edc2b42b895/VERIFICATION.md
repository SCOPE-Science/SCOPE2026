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

# Verification protocol and limits

Run `python verify.py` using the standard Python 3 interpreter. The verifier uses `fractions.Fraction` for exact rational arithmetic and independently inverts the full shifted-Laplacian matrix before comparing its entries with the proposed closed form. It checks the matrix-level variance for all canonical two-color count combinations on graph sizes up to five per part and rational shifts, then checks the complete integer-maximization reduction and stability boundary on a larger rational grid of part sizes and shifts. The recorded execution output is in `VERIFY_OUTPUT.txt`.

Observed output: 10,067 exact assertions passed; the star example gave optimal variance \(1/4\) and conventional variance \(5/16\). The parameter-uniform proof rests on explicit matrix inversion, a positive integer second-difference and concave quadratic maximization. These finite tests do not establish the theorem for arbitrary sizes or real shifts. Literature comparisons leave a possible specialist precedence risk; no independent scientific audit has been performed.
