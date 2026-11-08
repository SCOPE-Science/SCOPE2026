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

# Verification procedure

The theorem is proved by a finite reversible birth–death identity and a rigorous central-binomial asymptotic. Run `python3 checker.py` in the same directory. The script has no nonstandard dependencies. It constructs the two jump rates as rational numbers, checks their reversible ratios, and independently solves the finite-state absorbing generator by rational Gaussian elimination before comparing the exact first-passage sum. It also evaluates numerical finite-size ratios to the proved asymptotic for four fixed choices of \(q\) and several susceptible-population sizes. The observed checker result was `PASS: 260 checks`.

Sample normalized ratios at \(S=240\) for \(q=2,3,4,5\) were approximately \(1.01260594,1.00365705,0.99999121,0.99661825\), respectively. These are diagnostics, not a proof of the infinite limit. The Gaussian localization and tail estimates in `RESULT.md` supply the infinite limit. The time unit is one global voter-selection opportunity, so conversion to one clock per individual requires division by \(S+2\) in the mean time. No assertion of external independent confirmation is made.
