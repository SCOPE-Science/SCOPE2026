---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For fixed marked set P with k=|P| and N=n-k, each unmarked vertex independently has one of two disjoint extreme arc signatures of probability t=2^-k. Hence (A,B,N-A-B) is exactly multinomial(t,t,1-2t). The unused cross-arc variables are independent fair bits, so H|A,B ~ Bin(AB,1/2), and N t->lambda gives independent Poisson(lambda) counts. In rank two, the complete two-round Ehrenfeucht–Fraisse invariant is the set of color/orientation profiles. With k->infinity and N->infinity, only the optional A-present and B-present profiles survive, yielding twelve subset-sum limits on dyadic n=2^m,k=m. The rank-three χ is exactly H>0; its limiting probability h(1)=1-E[2^-AB]≈0.289156 is strictly between e^-1(1-e^-1) and e^-1, an empty adjacent rank-two interval. Algebraic endpoint bounds and the EF characterization were independently checked. An independent exact multinomial normalization and χ limit computation corroborated formulas, not infinite completeness.

## originality

PASS

PASS best of knowledge. The exact conditional orientation of two opposite rare unmarked types and its strict rank-two/rank-three probability gap are not implied by published rank-two profile/saturation theorems for uncolored independent multitournaments, sparse random successor orders, or Larrauri's sparse relational structures. The basic Poisson-thinning and EF-profile methods are acknowledged as classical; the new joint construction and full twelve-value logical spectrum are the asserted content.

## value

PASS

A single fixed unary/binary vocabulary gives a rigorous first-order quantifier-rank probability hierarchy, with a complete lower-rank limiting spectrum and an explicit first separated higher-rank probability. This is a natural logical expressivity and random finite-structure boundary rather than a trivial Poisson count of one rare event; the cross-arc conditional kernel is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
