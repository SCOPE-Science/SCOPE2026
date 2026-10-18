---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

All classical complete strict profiles for n=2 (16) and n=3 (6^6=46656) can be exhaustively enumerated since each profile has n! possible perfect matchings. Independent exact implementation tested blocking pairs and full argmin sets, confirming 40056 equality, 5400 proper E subset G, and 1200 proper G subset E, with zero disjoint/nonnested cases. Stable-matching multiplicities by 1/2/3 were 34080/11484/1092. For the explicit four-couple witness direct enumeration of all 24 assignments found exactly two stable matchings with ranks (2,4,3,1,1,1,2,1) and (2,2,2,1,3,1,2,3), objectives (15,4) and (16,3), disjoint singleton argmins. Exhaustive enumeration is a complete finite proof for n≤3, not an infinite extrapolation.

## originality

FAIL

Decisive prior coverage: an October 4, 2026 published result titled "Sharp coincidence boundary for egalitarian and minimum-regret stable marriage" proves for every complete strict instance n≤3 that E and R are nested, prints exactly the same 46656-profile classification 40056/5400/1200 and stable-count marginal 34080/11484/1092, and constructs a different four-couple conflicting witness. The full prior RESULT.md was read. The submitted October 13 record repeats the same theorem, numbers and sharpness; changing labels or the particular witness does not produce an original mathematical claim.

## value

PASS

The first market size at which two canonical stable-matching fairness criteria must conflict, together with an exhaustive small-market incidence table, is a naturally motivated sharp boundary. This is intrinsically useful matching theory, although in this instance the exact result is already published; the originality axis (FAIL) controls rejection and no claim of new value/novelty is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
