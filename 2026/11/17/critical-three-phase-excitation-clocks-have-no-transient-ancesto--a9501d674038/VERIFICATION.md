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

# Verification notes

Proof checks: The target-state predecessor constraint is exhaustive because only \(1\) advances to \(2\), only resting \(0\) can advance to \(1\), and only \(2\) or resting \(0\) can yield target \(0\). These choices do not alter the excited-source set. The phase-edge saturation argument uses all three time phases, counts each cross-class edge once, and uses no unproved connectivity assumption beyond that stated. The final strict inequality is essential for optional resting-source choices.

The standalone Python program `verify_critical_clocks.py` enumerates complete finite state spaces (not random samples) for the named small graphs and thresholds; it verifies the formula, clock phase balance, unique critical incoming edges, and the subcritical six-vertex example. The exact captured output is in `verify_critical_clocks.txt`. All-size correctness follows from the displayed mathematical argument, not simulation. No independent audit has been performed.
