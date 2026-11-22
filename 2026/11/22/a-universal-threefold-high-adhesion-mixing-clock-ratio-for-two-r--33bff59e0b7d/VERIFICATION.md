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

Run `python3 verify.py` using the Python standard library. The code recomputes both off-rotation first-order increment measures for every deck size from four through eight using exact rational arithmetic, tests the geometric ordering of block midpoint keys, and checks that the midpoint rule's measure is exactly three times the block-weighted measure outside the rotation subgroup. It verifies the summed departure rate formula and constructs exact rational right-coset generators for five and six cards, checking row sums, column sums, and irreducibility. It also evaluates sample continuous-time total-variation distances by the Poisson-series formula.

Observed checker outcome: PASS for deck sizes four through eight, including exact coset checks for five and six cards. These are finite checks, not an exhaustive proof for every possible deck size. The universal ratio, the singular-perturbation limit, and the mixing-time asymptotic are derived analytically in `RESULT.md`. The standalone checker makes no claim to certify a theorem or to constitute independent validation.

The proof assumes binomial cut before bond sampling, independent bond survival, and the exact two release rules given in the cited primary source. It excludes the zero-rescaled-time boundary layer and concurrent large-deck limits.
