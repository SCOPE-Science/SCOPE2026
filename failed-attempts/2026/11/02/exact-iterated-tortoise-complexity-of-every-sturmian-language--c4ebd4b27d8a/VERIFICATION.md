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

Prefix sums of the mechanical factor are floor(β+jα); their n distinct internal jumps give n+1 different phase cells, all realized by density and with the endpoints assigned to the right cell. For an interior jump at j<n the two changed letters are 01→10, and immediately before the jump the moving one has rank floor(jα)+1. Deleting the first k ones and appending them either erases this change or gives a strict lexicographic increase. At j=n the increase is strict even if both images are sorted: their one-counts differ; when the common prefix contains k ones the final bit changes after identical prefix deletions. Hence no nonlocal collision goes undetected by the adjacent erased cuts. Exactly min(n−1,floor(k/α)) are erased; jα=k is impossible. This includes n=1 and large k. Both mechanical one-counts occur, so Abelian complexity is 2 and equality ends at floor(k/α)+1.

## originality

FAIL

An earlier indexed record gives the same profile and threshold for all k≥2 and explicitly includes k=1 by the same proof. The hypothesis sets and binary operation coincide; changing the nominal starting iteration from 2 to 1 adds no unsupported or new case. The adjacent-phase proof in the earlier record already treats k=1.

## value

FAIL

The exact profile of a natural language answers a motivated question and would be useful if new. But the profile and the cutoff are both already available; k=1 is only an explicitly stated specialization and the proof does not supply an additional classification or useful new remainder. The finite checks are corroborations of the covered result, not an independent contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
