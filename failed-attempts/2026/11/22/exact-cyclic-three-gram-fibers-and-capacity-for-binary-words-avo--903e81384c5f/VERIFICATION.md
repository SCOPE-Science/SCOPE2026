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

A nonzero source is a rotation class of positive zero gaps, including periodic repetition and the single-one case. One counts 010 at each one, 101 at each unit gap, 001 and 100 once per longer gap, and 000 by remaining gap excess. This gives (R,t,r,0,t,r−t,0,0), including wrap-around below length three. A rotation of order d fixes precisely lists repeated d times with d dividing r,t,R; the reduced block need not be primitive (the word 'primitive' at RESULT.md line 30 is inapt, but the formula correctly counts all reduced blocks). The singleton distinctions follow from one long gap, one excess zero in equal-length gaps, or a unique short gap with no excess. For at least two long and two short gaps, one versus two cyclic runs of long gaps produces distinct profiles of gap types and thus distinct source necklaces in the same read fiber. For one short gap it anchors distinct excess locations; with no short gap and excess at least two, concentrating versus splitting the excess gives distinct sources. The series, first ambiguity at n=8, and growth constants follow. A new bitmask reproduction checked all oriented signatures and 147 observed fiber sizes over n=1..16, both series, and the ambiguity boundary; /workspace/branches/replay-cyclic.py. The related-work assertion about non-implication from four-gram work is independently false, as explained under originality.

## originality

FAIL

Verified broader coverage: the 2026-11-02 cyclic four-gram fiber theorem treats the identical source and the finer observation. Its explicit parameterization and exact multiplicities specialize by marginalization and one Vandermonde identity to the precise three-gram formula, and its exact feasibility and singleton cases immediately give the remaining classifications. This is a demonstrated implication, not an inference from similar titles or dates.

## value

FAIL

The read-length-three reconstruction question is natural and the formulas are convenient, but every asserted invariant is mechanically obtained from the exact prior higher-read description on the same source: project the feasible tuples, collapse the fiber sum by Vandermonde, and apply the singleton test to the one surviving refinement. No independently useful unknown exact fact remains within this claim. A standalone presentation or new finite replay does not repair that lack of a distinct mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
