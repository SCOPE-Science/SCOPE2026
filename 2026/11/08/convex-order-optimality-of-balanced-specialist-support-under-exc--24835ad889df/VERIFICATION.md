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
# Verification

The mathematical proof in RESULT.md is based on an exchangeable local transfer, conditional hypergeometric stochastic ordering, and exact pairwise moments. It is valid for every integer \(a,b\ge2\) and for every exchangeable retention distribution; the finite test below is not an infinite certificate.

Execute `python verify.py` with Python 3 (standard library only). It independently generates exact fixed-count survivor histograms both through a bivariate generating polynomial and by enumerating retained-subset combinations. It checks 1,244 distributions, 354 comparable distinct majorization pairs, 44,829 integer stop-loss inequalities, 3,945 exact rational variance identities, 2,529 strict interior-stage gaps, and a five-taxon example. The tested scope is \(2\le a\le5\) and \(2\le b\le7\); arbitrary sizes rely on the analytic proof, not extrapolated experiments. Source comparison and review are not independent audits. No external validation has been performed.
