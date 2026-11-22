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

# Reproducibility

Run `python3 VERIFY.py` with Python 3 and no external packages. The program builds finite permutation groups and actual labelled actions, constructs the complete list of equivariant maps independently of the table-of-marks formula, and checks regularity by searching for actual inner inverses \(g\) such that \(fgf=f\). It compares the independently computed rank profiles with the claimed formula for all ten cases and checks the iff criterion for regularity of the entire monoid. It concludes with `REGULAR_EQUIVARIANT_RANK_TESTS_PASSED` on success.

The ten tests include the trivial action on three points; four cyclic-group actions with mixed stabilizer types; four distinct symmetric-group actions; and an action containing isomorphic natural orbits represented through different conjugate stabilizers. Example checks include \(14\) regular elements among \(16\) for a \(C_2\)-action with a free orbit and two fixed points, and \(36\) regular elements among \(48\) for a mixed \(S_3\)-action.

The program verifies finite cases only. The unrestricted finite-group theorem follows from the mathematical proof, not from an exhaustive enumeration across all groups. No independent mathematical audit has been performed.
