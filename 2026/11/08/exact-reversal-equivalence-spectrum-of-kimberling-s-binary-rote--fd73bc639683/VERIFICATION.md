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

# Reproducibility and boundaries

Execute `python3 verify.py` using Python 3 and the standard library only. The script directly derives the two-letter Tribonacci factor closure from substitution, the complete thirteen-element six-letter factor language from fourth iterates, and exact binary languages for lengths one to eleven by the bounded-image argument in `RESULT.md`. Assertions check the factor counts, palindrome list, reversal-pair counts, twenty length-ten factors and the reversal-disjointness cutoff. A separate expanded-prefix comparison is only a consistency test, not a proof that no unseen factors occur.

The infinite part follows from the ten-letter disjointness plus the prefix/suffix inheritance of reversal pairs. The formula for ordinary factor complexity \(2n\) is invoked as an established cited theorem rather than independently reproved here. No external audit, formal theorem-prover certificate or third-party revalidation is asserted.
