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

# Verification scope

The proof is self-contained and applies to every integer period and exceptional count in the stated domain. A separately executable checker `cyclic_resistance_verify.py` calculates every circular pair interaction and direct two-arc effective resistance with exact fractions on 16,028 exhaustive instances, including both contrast signs and all equality cases, and compares 30 exact inverse-Laplacian instances on smaller cycles. It was executed with standard-library Python and SymPy available; numerical Monte Carlo estimates do not enter the proof.

## Reproduction

Run `python3 cyclic_resistance_verify.py` from the directory containing this document. Successful checks print two lines beginning `PASS`. If SymPy is unavailable, the independent grounded-Laplacian part announces a skip; the 16,028 exact-rational standard-library checks still execute. The analytic argument in `RESULT.md` is the infinite-family verification, not these bounded tests.

## Limits

Proof assumptions: undirected nearest-neighbor cycle, exactly two positive resistance levels, fixed count of one exceptional level, and continuous-time edge rates equal to reciprocal resistance. Historical originality checks are provisional. No external independent scientific audit is represented.
