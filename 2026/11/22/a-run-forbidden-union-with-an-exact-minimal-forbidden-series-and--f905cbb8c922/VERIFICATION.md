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

# Verification and reproducibility

Execute `python3 CHECKER.py` from this directory. The script enumerates all binary words of each length from one through sixteen, for run thresholds two through five, evaluates exact minimal forbidden status by the independent prefix/suffix criterion, and cross-checks the coefficients of the proposed rational generating series by a finite recurrence. The resulting 64 exact integer comparisons pass.

The checker is a bounded falsification check, not a proof of the theorem for infinitely many run thresholds or word lengths. The general proof derives the complete generating function by a unique alternating-run decomposition; derives both entropy values from the relevant renewal/finite-state presentations; and proves exactly two maximizing ergodic measures by invariant-component ergodicity and the Parry uniqueness theorem. The case of run threshold two, where the intersection is a periodic two-point orbit, is treated separately.

Potential independent validation should examine the unique-minimal-obstruction argument, the effect of boundary fragments on entropy of the bounded-run shift, and the derivation of the entropy-gap asymptotic. No independent audit or external certification has occurred.
