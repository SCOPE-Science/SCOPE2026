---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A vertex with at most one successor satisfies any Delta formula; if branching vertices are independent, every successor of a branching vertex satisfies Delta p, proving validity. Conversely, for an arc v->u between branching vertices, choose a second successor w of v and two successors a,b of u. Acyclicity of the simple underlying forest and the exclusion of reversed arcs guarantee that the successor sets of u and w are disjoint and do not intersect the successors of v: any collision would give a triangle or a four-cycle, or require an opposite arc on an already oriented edge. Set p constant on the successors of v and w but different on a and b. This gives a failure at v, including if w is a sink. For the census, a planted head when the parent sends into it is of type C or D; a planted tail sending to its parent is of type A or B_1. Incoming-child and outgoing-child sets at the planted vertex therefore contribute the exact stated factors: outgoing count at most 0 or 1 for A or C, at least 1 or 2 for B_1 or D; in the latter cases all children must be nonbranching, and the root contributes q. Separating labels by unordered sets gives the exponential factors. The true root has the zero-parent-outgoing states C+D; marking a root multiplies each n-vertex contribution by n. Each coefficient is uniquely determined from lower z powers. With zero branches the outdegree sum n-1 gives one sink and all edges point to it; Cayley gives n^(n-1), also correct at n=1. Two adjacent branching vertices require the endpoints plus three distinct additional neighbors, and at order five the unique possible shape has central degrees 2 and 3, with 5·4·3 choices and a unique invalid orientation for each. Independently, I enumerated parent maps toward label 0 and each orientation through order 7, evaluated both nested Delta formulas as full Boolean valuation masks, and tallied branching by exact outdegree. I separately expanded ordinary rational z-polynomials through order 9; the totals match, and the independent refined coefficients through order 7 agree at five q values (degree at most floor((n-1)/2)). This check reproduces the 60 invalid orientations at order five and all given polynomials. The frozen script compares its refined EGF to hard-coded values, not to branch counts freshly tallied by its own enumeration; this limits what its code alone establishes, but the independent tally supplies that check.

## originality

PASS

The result under review correctly stakes the contribution on the exact census over all labelled trees and all their orientations, with the branch mark. Credit the modal criterion as a forest specialization of the known frame correspondence and credit the earlier outward-tree enumeration on its own restricted domain. The inspected sources do not supply an equivalent all-orientations census.

## value

PASS

This is an exact labelled census for a naturally specified modal-validity class, not merely a rediscovered frame condition or a table of small orders. Tracking the branch count gives an invariant of all orientations, exposes exactly how the first modal failures arise, and provides an all-order scheme that can be used in probabilistic or asymptotic enumeration. The two directions of the planted parent edge encode information absent from the prior rooted outward census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
