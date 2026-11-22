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

# Reproducibility and limits

Run `python verify.py` using Python 3.10+, SymPy and NumPy. The checker symbolically reconstructs cardinal and step polynomials and their derivative identities, verifies the analytic variation formulas and the monotonicity logarithmic derivative, and uses rational integer square-root enclosures for the unique crossing and optimal gain. It independently tests 4,000 real data vectors by constructing the cubic polynomial afresh and integrating the absolute derivative between its critical points. Numerical tests complement but do not prove the infinite-family statements; those follow from the proof in `RESULT.md`. The displayed exact-rational checks establish sign certificates only at the two printed rational test points and use the proved monotonicity to enclose the unique crossing.

The checker does not establish publication novelty, unrestricted asymmetric optimality, any result at polynomial degree greater than three, or independent mathematical validation.
