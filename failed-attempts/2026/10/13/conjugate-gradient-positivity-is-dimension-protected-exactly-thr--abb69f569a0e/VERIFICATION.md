---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n<=2 the first CG iterate alpha*b is nonnegative, while exact CG terminates at the inverse-positive Stieltjes solution in at most two steps. For n=3 the assigned rational A has SPD Sylvester minors (2,4,46) and A^{-1} positive; direct independent exact conjugate-gradient recurrences give x_2=(9076,9469,-32)/3219. Therefore its small-dimension/iteration threshold and concrete witness are mathematically correct.

## originality

FAIL

FAIL decisively: a previously published October 4 Resultary theorem proves the identical dimension<=2 protection and dimension-three second-iterate failure over Stieltjes systems, with a sharper one-parameter threshold a>4. The assigned October 13 witness and minimality are covered as a special case or parallel illustration, regardless of differing matrix entries or signs.

## value

FAIL

FAIL: the small dimension/iteration threshold and positive-cone escape are natural mathematical questions, but they were already fully classified and refined by the October 4 published theorem. Checking an additional rational witness supplies no independent structural lemma, sharp new invariant, or motivated boundary beyond known work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
