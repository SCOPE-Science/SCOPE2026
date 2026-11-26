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

For a nonempty indexed independent set, a token can move clockwise by two exactly when its next gap is at least four, and the other end of each such gap supplies the reverse-direction move. This includes the one-token case, where the gap is n; for n≥5 the two destinations differ, and moving different tokens removes different sites. Counting a distinguished occupied site counts each size-k state exactly k times, regardless of symmetry; the n anchor positions and coefficient of W^k thus give n/k and sum to the asserted derivative series. For the maximum let n=4h+r. The h long gaps consume 4h sites and leave at most one short gap. Weak compositions of r into the h gaps give the all-long terms; one short gap adds n at r=2 and n(h+1) at r=3, reproducing all residues. Every positive half-degree t≤h is realized by t long gaps with the surplus in one, and the empty state realizes zero. Each edge is oriented uniquely by the clockwise move; after fixing its 01000 five-site block the other n−5 vertices form a free path, including the empty path at n=5, giving nFₙ₋₃. Nonempty frozen sets have gaps only 2 and 3, equivalent to maximal independent sets. Independently, W(z,0)=z²+z³ and the logarithmic derivative of 1−z²−z³ gives the Perrin power sums, including their specified initial values.

## originality

PASS

The supported distinct contribution is the degree distribution and the extremal populations and edge total for the strict two-step rule, not the Perrin frozen count, ordinary circular compositions, or the vertex count. In the inspected literature the related moves differ, or the distance parameter constrains token separation rather than the move itself.

## value

PASS

On a labelled ring the distinction between exactly two and at most two affects legal transitions and creates a different frozen sector. A complete all-length degree polynomial gives the move-choice counts at every occupancy, including the highest-mobility population and the whole graph's size in edges. It is an exact reconfiguration invariant of the standard nearest-neighbor exclusion model, not merely the known frozen-state total or a few cycle examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
