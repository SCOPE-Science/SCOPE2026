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

# Verification and scientific limits

The proof identifies the full group-independent domain constraint, chooses disjoint matching edges in every nonidentity regular translation, and uses a local forbidden pattern of exactly three independent Boolean bits (probability \(1/8\)). The proof applies to any finite group and is not inferred from finite experiments.

The standalone `verify.py` checks all partial-map pairs by direct composition for cyclic groups of orders one through four and the nonabelian symmetric group on three letters and the dihedral group of order eight; it independently recomputes the domain constraints and all label-pair raw counts. Verified ordered totals: \(4,31,184,1021,21013,343897\); all checks print `VERIFY_OK`. Direct execution on the packaged script is required for reproducibility.

The exponential constant is an explicit safe uniform bound, not an optimal rate. The regularity hypothesis, shared zero correction, and order of quantifiers are essential. The historical literature comparison does not constitute exhaustive publication-priority certification. Independent audit has not been performed.
