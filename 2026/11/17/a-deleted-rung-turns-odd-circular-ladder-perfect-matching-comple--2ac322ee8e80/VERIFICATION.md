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

# Reproducibility and verification

Run `python3 verify_perfect_matching_ladders.py` with Python 3.9 or later and no third-party packages. The checker independently constructs the vertex/edge graph of each punctured circular ladder and each straight ladder. Backtracking enumerates full perfect matchings. A separate face enumerator produces their downward closures, and mod-two linear algebra reduces explicit simplicial boundary columns.

For odd punctured circumferences 3, 5, 7, 9, and 11 the checker tests the exact union/intersection identities; the target intersection must agree face-by-face with the perfect-matching complex of the induced straight ladder. Mod-two Betti numbers in the first four cases are, respectively, a single generator in dimensions 0, 1, 2, and 3. The 11-column case is checked structurally without homology reduction. Straight ladders of even lengths 2, 4, 6, and 8 are checked by the same method; their mod-two Betti numbers are one in degrees 0 through 3.

The file `verification_output.txt` is the literal output of the checker. The universal and integral conclusion is proved by the paired-horizontal-edge lemma, cone covers, exact intersections, and homotopy pushout argument in RESULT.md; no finite sample is extrapolated to a universal claim. This program does not check possible independent bibliographic priority, even-circumference cases, or other kinds of edge deletion.
