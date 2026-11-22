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

# Reproduction and scope

Extract the files in the same finding package into one directory, then run `python verify.py`. Python 3 and its standard library are sufficient. The script reports the assertion count and smallest positive exact mean gap.

The executed script passed 455 exact assertions. It constructs path-occupancy laws by independent first-choice recursion, independently enumerates all permutations and all inclusion-maximal independent vertex sets of wheels with 3 through 6 rim vertices, and checks the two distributions match the mixture formulas. It checks complete finite wheel CDFs and exact mean inequalities for all rim sizes from 3 through 43; for 8 through 43, the smallest gap is \(799/24570>0\), attained at rim length 12.

The script also verifies the rational endpoint inequalities used in the analytic proof: the real cubic root lies in \((33/25,133/100)\); the associated complex-root ratio is less than \(2/3\); the cycle-static mean density is below \(0.42\) for all sizes at least 20; and the sequential cycle mean density exceeds \(0.43\) from size 20 on. The infinite proof also uses the algebraic root identities and the factorial error formula displayed in RESULT.md. Computation alone does not validate those logical derivations or prove the infinite result; they have been explicitly assessed from their definitions in the self-review.

No external independent assessment has been performed. The novelty comparison is limited to the identified and materially inspected literature and indexed mathematical records, not an exhaustive search of all publications.
