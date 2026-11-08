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
# Reproducibility and verification

Run `python3 checker.py` with Python 3 and no external dependencies. In the prepared package the script reports 40 exact slope-period cases, 2,550 fixed-point instances, and 12 independent cylinder transport approximations; each asserted identity passed. Exact arithmetic uses `fractions.Fraction`, so the checks are not floating-point comparisons.

The first family of tests enumerates all words of periods \(1\) through \(8\) at slopes \(2,3,4,5/2,7/3\), computes the unique point fixed by each word contraction, checks its \(n\)-th return, and compares the empirical mean and the self-similar absolute-deviation recurrence to the closed formula. The second family approximates the invariant measure with every depth-11 cylinder midpoint and computes the prescribed monotone-coupling cost; the proof bounds its deviation from the true \(W_1\) by \(H^{-11}/2\). The theorem for arbitrary real \(H\) and all periods is proved in `RESULT.md`, not inferred from these finite checks.

No external mathematical certification or independent audit was performed. The exact \(W_1\) law is for the full fixed-point census, not for a primitive cycle selected by one initial condition.
