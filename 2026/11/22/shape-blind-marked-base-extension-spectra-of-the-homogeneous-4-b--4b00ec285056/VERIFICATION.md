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

# Verification

Run `python3 verify.py` with Python 3 and no external dependencies. It enumerates every labelled reduced tree with 3 through 7 leaves using all admissible graft sites. Canonical complete nontrivial split families independently identify the labelled tree topology; all unlabeled classes through six leaves are determined by canonical internal adjacency/leaf-degree signatures. For every six-leaf shape the test explicitly generates all ordered pairs of new leaves and checks the refined 4-valent statistics against the recurrence. It also directly confirms the recurrence has no negative counts for \(3\le n\le11\) and short arities through five. The actual captured output is embedded in `verification_output.txt`. Its success marker is `ALL_SHAPE_AND_EXTENSION_CHECKS_OK`.

The finite computations are cross-checks; the proof for every arity is the inverse-leaf-deletion bijection and induction in RESULT.md. No full-scale historical mathematical priority guarantee is claimed.
