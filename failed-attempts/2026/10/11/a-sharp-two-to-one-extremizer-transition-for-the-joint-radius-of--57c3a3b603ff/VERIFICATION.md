---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Independently reconstructed the exact objective (|<u,x>|^4+|<v,x>|^4)/2. Projection to span{u,v} strictly improves objective for a nonzero perpendicular component. For 0<c<1, relative-phase alignment optimizes the second overlap and reduces the unit-vector problem to G(theta)=[cos^4(theta)+cos^4(theta-phi)]/2 on 0<=theta<=phi=arccos c. With y=cos(2theta-phi) ranging through [c,1], G=(2-c^2+2cy+(2c^2-1)y^2)/4. When 0<c<1/2, its strict concave vertex y*=c/(1-2c^2) is in (c,1) with exactly two angle/ray preimages. When 1/2<=c<1, derivative of this quadratic on [c,1] is positive except possibly at the endpoint c=1/2,y=1, giving only the bisector ray. Endpoints c=0 (two orthogonal generator rays) and c=1 (the common ray) are handled separately. Substitution yields R^2=(1-c^2)^2/[2(1-2c^2)] below c=1/2 and (1+c)^2/4 above. The exact squared branch difference is (1+c)^2(1-2c)^2/[4(1-2c^2)], leading to 1-y*=6delta+O(delta^2), angular splitting 2sqrt(3delta)+O(delta^(3/2)) and radius excess 3delta^2+O(delta^3). Independent SymPy expansion confirmed all polynomial identities, boundary values and second derivatives 19/2 vs 1/2. Finite rational sample checks are only corroboration; the polynomial and phase argument prove the full stated range and dimensional generality.

## originality

FAIL

A DISTINCT currently published finding, “Sharp overlap transition for the p-joint numerical radius of two rank-one projections” (Resultary/2026, record 4d7babb11eed, dated 2026-10-11), proves a stronger theorem for EVERY real p>=1 on the identical projection-pair object and balanced mean. Its p=2 specialization is literally this R(P,Q); Section 4 states exactly the two algebraic radius branches, the c=1/2 threshold, two vs one maximizing complex ray and all endpoint cases, while its stationary-ray equation and quadratic reduction yield the submitted explicit theta_± and the square-root separation by Taylor expansion. It also determines a broader c_p=1-1/p threshold and C1/not-C2 transition. Thus the submitted result is covered in full as a mathematical special case and routine local expansion. The two entries have the same printed publication date (2026-10-11), and their intraday priority was NOT determined; this review establishes scientific coverage as of the audit, not a fabricated historical ordering. Earlier Dragomir 2006, Feki 2024 and Aljawi et al. 2026 supply definitions/general bounds but need not be claimed to establish this exact formula. The matching Resultary finding 57c3a3b603ff is the assessed record itself and not independent evidence.

## value

FAIL

An exact extremizer transition for the smallest noncommuting projection pair is a natural and potentially valuable invariant in isolation. But the assessed p=2 claim, both branches, and 1-vs-2 maximizing rays are already part of the DISTINCT published, strictly broader p-joint theorem for all real p>=1. Its additional printed square-root angular splitting and quadratic gain are straightforward Taylor expansions of the same prior exact quadratic optimizer and branch difference; they do not constitute an independent new classification, structural lemma, counterexample, or unknown invariant. The correct result therefore lacks distinct scientific contribution relative to strong published coverage, rather than being dismissed for being finite/simple. Its singular coefficients might be useful exposition but do not change the decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
