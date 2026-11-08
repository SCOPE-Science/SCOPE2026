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
# Reproducibility and scope

The included `check_symbolic.py` was executed successfully with SymPy: it recomputes all \(11\) connected simple graph classes up to four vertices, \(43\) unordered root pairs, and \(18\) strictly unequal pairs, and checks all-parameter coefficient positivity and simultaneous ties. The included standard-library `check_witness.py` was independently executed: it computes exactly the final and peak expectations from the five-vertex graph with infection-to-recovery ratio \(\beta=2\), then verifies all optimal-seed sets. Both rely on the exact absorbing first-event recurrence given in `RESULT.md`.

These are finite exhaustive and exact symbolic verifications of the stated finite-order and fixed-witness claims; they are **not** simulations, proofs about larger graphs, empirical validations, or independent scientific audits. No external certification was conducted. Literature novelty remains conditional on the inspected sources.
