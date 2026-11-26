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

The graph edge, not the graph metric, is modified. With e={0,d}, the common neighbors are the integers in [d-p,p] other than 0 and d: in representatives in [-p,p], the distances to d cannot use a wraparound edge to gain an extra neighbor; differences within the resulting set also cannot wrap to distance at most p under n>=4p+2. Consecutive vertices in this set differ by at most three. For p>=3 the leftmost vertex is dominated by its successor: every vertex to the right adjacent to the leftmost is at least as close to the successor. Pair faces containing the leftmost vertex by toggling the successor, largest first, then iterate. The link is a single vertex for (p,d)=(2,2), and two isolated vertices for (2,1). Lifting the link pairs by adjoining e does not introduce cofaces from the retained complex; after the lifted pairs only e and its triangle with the surviving link vertex remain to be paired. Independently, a length-q edge in the intact qth power lies in the unique maximal (q+1)-vertex interval simplex, with no second length-q edge in that simplex, so the same toggle argument reduces q one power at a time. In the exceptional deleted square there are two missing triangles, and the remaining triangles can be paired with their respective distinct free length-two edges. The retained consecutive edges form a spanning path and the two surviving chords raise its cycle rank to two. These are uniform arguments, including both p=2 edge types. Inspected VERIFICATION.md and VERIFY.py (finite interval checks, relative free-face tests and the explicit rank calculation); did not execute the frozen verifier.

## originality

PASS

The intact collapse is already a special case of Adamaszek's Proposition 2.2, and its proof also supplies the outermost-edge mechanism. For d>=2 the local common-neighbor graph has a universal vertex strictly between 0 and d, so the standard cone-link reduction is enough; these alone do not justify an originality claim. The contribution that survives is the uniform classification including d=1: this link has no global cone vertex, yet admits a relative elementary collapse through successive domination unless p=2, where the homotopy type changes. Neither the inspected cyclic-graph theorems nor the distinct exact corpus matches give that classification. This is a best-of-knowledge assessment, not a global priority claim.

## value

PASS

For the canonical finite cyclic flag model, one-edge perturbations are a natural robustness question: does the inclusion itself preserve topology, and which edge type fails first? The result distinguishes an actual relative collapse from mere equality of abstract homotopy types, and the exceptional squared nearest edge adds a full independent loop. The sharpness in p, including the nearest-neighbor link without a single cone vertex, is the substantive boundary; reproducing the known intact circle would not have value by itself. No optimal bound on n, multiple-fault robustness, or recomputed-metric stability is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
