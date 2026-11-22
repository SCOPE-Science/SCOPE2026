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

Run `python3 verify.py` from the directory containing the extracted files. The script checks exact rational identities for the threshold, population shares, second moments, slack ratios, common divergence coefficient and first cost-gap coefficient, and numerically solves the source's original two-station waiting-cost equations at several near-critical arrival rates. The proof of existence, uniqueness, asymptotics and analytic remainder is contained in `RESULT.md`; numerical agreement alone cannot certify the limiting statements.

Only the source's deterministic continuum-game equilibrium and **approximate** queue penalty are evaluated. No direct validation of real-world waiting time, stochastic heavy traffic, or independent scientific audit is claimed.
