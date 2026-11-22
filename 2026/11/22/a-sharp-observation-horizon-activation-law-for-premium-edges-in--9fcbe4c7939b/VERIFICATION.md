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

# Reproducibility and proof limits

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The script evaluates the symbolic derivative numerator in 17 sizes, exact characteristic-polynomial identities in seven sizes, direct symmetric-matrix heat-kernel projections and boundary gradients, numerical budget-constrained scalar optima on both sides of the analytical threshold, and large-size root convergence. In the reviewed environment the executable printed `VERIFY_OK 849 checks` with no assertion failures.

The mathematical claim concerns every integer \(m\ge3\), price \(r>1\), budget \(B>0\), and observation time \(t>0\). Finite numerical tests alone cannot establish that quantification. The proof in RESULT.md provides strict global convexity, exact boundary derivatives, an explicit monotonicity certificate for the threshold, and the limiting root argument. No independent proof review or external audit has been performed.
