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

# Reproducible checks

Run the included `check_wheel_chords.py` under Python 3.9+ without external packages. It enumerates all spanning-tree edge subsets for rim orders \(3\le m\le8\), independently forms the overlap histogram for every ordered pair, and verifies it coefficientwise against exact integer transfer-matrix powers. The exhaustive finite range consists of 5,688,628 ordered pairs. It checks the known diametral complementary-tree count, the number of diagonal pairs and the known wheel-tree total as boundary controls. It computes exact integer polynomial moments for rim sizes 20, 40 and 80 to compare with the constants of the proved asymptotic law.

The finite checks do not certify the infinite theorem. Its all-order proof uses a state-transfer bijection, an explicit correction for the unique extra all-rim edge set, and a Perron eigenvalue analytic expansion. The independent mathematical audit channel remains unperformed.
