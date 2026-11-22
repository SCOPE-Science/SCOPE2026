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

# Verification instructions and checked scope

The following files are complete, self-contained scientific artifacts: `clebsch_threshold2_a.cpp`, `clebsch_threshold2_b.cpp`, `clebsch_threshold2_symmetry.py`, `clebsch_threshold2_crosscheck.py`, and the corresponding four `.log` files.

Compile and replay the two C++17 programs and run the two Python 3 scripts using the commands under "Verification" in `RESULT.md`. The first program directly walks all disjoint excited/refractory configurations and rejects unresolved trajectories. The second independently constructs and peels the complete \(3^{16}\)-vertex functional graph, propagating cycle identity and first-entry depth along the reversed peel. The cross-check script asserts that their population tables and basin spectra agree exactly and sum to \(3^{16}\). The symmetry script checks the full 1,920-element automorphism group, both orbit classes and the affine-plane geometry of all four-cycle phase sets.

Verified results are one fixed point, 90 primitive four-cycles, 360 nonconstant periodic configurations, 43,046,360 transient configurations, sharp entry depth seven and exactly 150,400 states reaching zero for the first time at the seventh update. Every one of the 90 nonconstant basins has size 644 (60 cycles) or 676 (30 cycles), and the one fixed-point basin has size 42,987,801.

No probabilistic sampling substitutes for a complete proof here. The classification does not imply anything about the ten-regular Clebsch complement, other graphs, other thresholds, or arbitrary numbers of colors. Faithful execution and local code review remain the conditions of the finite computational proof. No independent external audit or formal proof assistant validation has been performed.
