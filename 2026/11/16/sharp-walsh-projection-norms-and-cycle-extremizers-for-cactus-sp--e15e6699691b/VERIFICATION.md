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

The self-contained standard-library-only script `check_cactus_fourier.py` supplies exact finite checks. Invoke `python3 check_cactus_fourier.py`. It enumerates trees from scratch using union-find over edge subsets, independently takes full Walsh transforms by butterfly operations, tests the product formula coefficientwise, and checks convolution rank, minimal nonzero multiplier, and endpoint projection norms. It covers 5,648 exact frequencies over ten cactus instances, as well as 5,739 integer cycle-length configurations (up to 24 vertices) for the extremal inequality, and binomial identities through cycle length 79.

Expected success marker: `CACTUS_FOURIER_ALL_EXACT_CHECKS_PASS`. The universal statements are proved by block decomposition, sign counting, and discrete concavity in `RESULT.md`; these finite tests cannot themselves certify universality or historical novelty. No independent audit has been performed.
