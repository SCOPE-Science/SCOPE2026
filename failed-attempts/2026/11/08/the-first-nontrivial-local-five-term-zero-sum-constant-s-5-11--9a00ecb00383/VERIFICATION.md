---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each coarse residue profile, avoiding a witness is equivalent to satisfying all affine constraints on fine digits for exactly the five-index selections whose coarse sums are divisible by five. Independent replay with python3 /workspace/reproductions/2.py avoids the frozen Gaussian elimination: a zero-sum selection taking part of a residue class makes every fine digit in that class equal by a one-index swap; for classes never taken in part only their total digit matters. Exhaustively testing at most four field variables and accounting for the free digits recovers all 12 profiles and ranks (six each of 2 and 8) among the 286 length-ten profiles, and no solutions among the 364 length-eleven profiles. The only two coarse-zero five-subsets of the displayed obstruction each sum to 25. The frozen C++ code checks aggregate counts and ranks, not individual profiles; this does not affect the proof or independent replay.

## originality

FAIL

A distinct, earlier indexed finding gives the same exact constant under equivalent hypotheses and the identical obstruction up to reordering. The auxiliary rank/profile presentation does not make that headline theorem new.

## value

FAIL

An initial proof of this prime conjecture case would be a meaningful exact result. In light of the earlier exhaustive theorem and obstruction census, the remaining coarse projections and small affine ranks do not establish a separate motivated gap, downstream use or significant new mathematical conclusion. The independent certificate is useful for checking correctness, not sufficient scientific value for the original finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
