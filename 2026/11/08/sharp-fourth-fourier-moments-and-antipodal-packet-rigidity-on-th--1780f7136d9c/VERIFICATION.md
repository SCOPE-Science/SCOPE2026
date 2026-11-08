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

The proof establishes the sharp inequality and characterizes all nonzero equality cases for every odd prime. The supplementary program `CHECK.py` reconstructs the exact pair-sum convolution and the independent residue-block decomposition for \(p=3,5,7\), compares the two fourth moments on 15 deterministic Gaussian-integer or packet patterns, confirms the upper bound in those cases, and verifies 12 further equality configurations (constant packets and nonzero phase-frequency packets). It separately compares a direct numerical average of the extension polynomial with the pair-sum fourth moment for two prime moduli, to check normalization. The output is `PRIME_SQUARE_HYPERBOLA_PASS primes=3,5,7 patterns=27 sharp_ratio=3p/2`.

The code uses floating-point only for the nonzero-frequency exponential examples and direct extension average. Their checks use strict small absolute tolerances; the main proof requires no floating-point computation. The exact convolution comparisons on Gaussian-integer inputs corroborate the algebraic fiber classification but do not certify the result for infinitely many primes. No independent audit or external certification is asserted.
