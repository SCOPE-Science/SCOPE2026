---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With y=1+x and D=1+y² the first three z-derivatives at z=-x have numerators 4y, 4(3y²-1), and 48y(y²-1) over D²,D³,D⁴. They give nonnegative divided differences through order three by simplex integration, including coincident nodes. Triangular resolvent expansion therefore gives positivity for every DAG of the stated depth. For a four-state shortest route of length three, any four-transition walk would contain a removable repetition; thus Q⁴ contributes only three transitions and a negative hold (at least the source), giving strict positivity from the coefficient -1/4 when the cubic coefficient vanishes. Shorter routes use coefficients 1 and 1/2, unreachable entries are zero by reachability block structure, and conservation follows from Q1=0. For the five-state witness invert the transient denominator D I/2 - h(1+h)N + h²N²/2 modulo N⁴. Transient coefficients agree with the derivative expressions. Subtracting their partial sums from 1 gives the four absorbing numerators over D to powers 1 through 4: h(h+2), h²(h²+4h+2), h⁴(h²+6h+6), h⁴(h⁴+8h³+12h²-4). The last quartic is strictly increasing on h>0 and crosses zero exactly once. The transient block has three internal superdiagonal ones, not four as one incidental sentence says; the displayed generator and N⁴=0 calculation are correct.

## originality

PASS

Bounded best-of-knowledge assessment of the joint topology/minimality/exact-threshold theorem; the map and eventual-positivity framework are not new.

## value

PASS

The graph-depth condition gives an all-step guarantee at arbitrary dimension and rates, and the exact minimal witness quantifies a reliability failure for a natural L-stable alternative to the exponential. Neither is a full-solver guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
