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

# Reproduction and limits

The accompanying `check.py` requires Python 3 and `sympy`. Running `python check.py` computes the stationary generator identities and derivatives symbolically, independently reconstructs fourth moments for a grid of rational parameters using `fractions.Fraction` elimination rather than substituting the claimed fourth-moment formula, checks positivity and identities in those rational cases, and tests peak ordering on an explicit deterministic sample grid. It prints `PASS 2668 exact-rational, symbolic, and deterministic numerical assertions` when successful.

The code establishes reproducibility and spot-checks the equations. The all-parameter proof rests on exact stationary generator identities, symmetry, and the derivative sign polynomials described in RESULT.md. No simulation, finite enumeration, or automated check proves bibliographic originality or independently validates the research. A plausible 2022 primary source could only be inspected through its published abstract, so implicit-priority risk remains.
