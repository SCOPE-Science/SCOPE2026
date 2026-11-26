---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Forth and back give F[N(A)]=N(F(A)). At a singleton source, N(A) is a clique; in the target, the neighborhood of a set of size greater than one contains nonadjacent distinct singletons. Thus atoms go to atoms. N(A) is the union of its atoms' neighborhoods, and target singleton probes recover a world from its neighborhood. This forces direct image on all worlds. Back to the full target world forces the atom map to be onto, and an onto atom map lifts any adjacent target world by choosing representatives including one in the given source world. Counting fibers or inclusion-exclusion gives the displayed formulas; composition and the case n=m follow. An independent rerun, python3 /workspace/independent_checks.py (check 2), examined 826113 functions using successor-image equality and found rows (1,0,0), (1,2,0), (1,6,6). This only checks the tiny finite cases.

## originality

FAIL

The earlier exact two-atom-target classification mechanically implies the full classification by singleton-separating binary projections. A distinct later catalogue entry also states the exact finite result inside its arbitrary-set theorem; that overlap is not evidence of earlier priority.

## value

FAIL

The classification is a natural way to understand these frames, but in this record the advance beyond the earlier two-atom target is just testing each target atom by a binary projection. The count and category statements are routine once these projections are applied. No independent valuable remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
