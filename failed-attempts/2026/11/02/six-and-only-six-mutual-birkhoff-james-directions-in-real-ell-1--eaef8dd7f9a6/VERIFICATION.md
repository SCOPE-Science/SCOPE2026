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

Independently derived the criterion in RESULT.md (1): the left and right derivatives of the convex function ||u+tv||_1 at zero are A−B and A+B, with A the signed sum on supp(u) and B the sum of absolute values off it, so zero is a minimizer exactly when |A|≤B. An axis forces every neighbor to lie in the complementary two-plane (apply the criterion in the reverse direction); at most two mutual lines fit in that plane because a full-support line there has just one possible outgoing orthogonal line, and there are just two axes otherwise. With a full-support line normalized to (a,b,c)>0, every two-support neighbor is the balanced difference on its support; any full-support neighbor has a sign type corresponding to a=b+c, b=a+c, or c=a+b. At most one such equality holds, and lines of the same sign type are not adjacent. This bounds that case by five. Among only two-supported lines each support has at most one per sign type, and a mutual pair on one support forces both lines to be balanced by the two directional equations. All six prescribed lines are adjacent in pairs: same-support sums cancel, and different supports give equality of shared and off-support magnitudes. Thus the proof covers all real projective lines and yields literal uniqueness. CHECK.py was inspected, not executed; its finite clique check is corroborative, and its derivative test compares equivalent signed-support expressions, not an independent continuous computation.

## originality

FAIL

An inspected distinct October 18 Resultary record explicitly states and proves the same maximum, unique six projective directions, same real ℓ1^3 space, both orthogonality directions, and unrestricted real coordinates. This is exact indexed coverage, independent of any claim about historical priority or status as a journal publication.

## value

FAIL

Knowing the maximum with rigidity for a concrete nonsmooth norm is useful, but the frozen record adds no new classification, boundary or proof mechanism to the exact indexed result. The finite signed-support check does not turn the known theorem into a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
