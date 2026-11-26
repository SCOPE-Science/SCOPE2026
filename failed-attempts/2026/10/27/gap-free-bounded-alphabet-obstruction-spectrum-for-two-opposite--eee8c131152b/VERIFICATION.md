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

Downward closure allows a disjoint split. Assigning each edge to the endpoint on which its dependency acts gives an orientation of outdegree at most one. In the converse direction a component with at most as many edges as vertices is a tree or unicyclic: orient edges toward a root or toward its cyclically oriented cycle. A minimal failing edge set must have its non-isolated part connected and no leaves. Removing a nonbridge would preserve failure if e≥v+2, so e=v+1; e≥2ℓ and e≥2r make the two occupied shore sizes differ by at most one. Simplicity and bipartiteness rule out e<6, including all graphs with at most four occupied vertices. One shore of size one permits only forests, and K₂,₂ is itself unicyclic. Three internally disjoint paths of lengths 2,2,2t−2 use t and t+1 vertices and give every permitted even size 2t+2; a cycle of length 2t with a noncycle bipartite chord gives every permitted odd size 2t+1, starting at t=3. Deleting any theta edge leaves a connected unicyclic graph, including the t=2 even boundary. These witnesses meet the balance bounds, and finite downward closure yields the sharp at-most-size result, not an exact-size coherence assertion. A fresh eight-rectangle enumeration used disjoint-set unions to keep component slack v−e, starting each vertex at slack 1, subtracting 1 on an internal edge and merging slacks as s₁+s₂−1 on a joining edge. It tested minimal failures by deleting each occupied bit from the mask and agreed with all claimed spectra; K₄,₄ yielded 48, 288, 432, 816 at sizes 6, 7, 8, 9. The frozen checker was inspected, not executed.

## originality

FAIL

The exact two-alphabet obstruction spectrum, including the empty cases and both sharp endpoints, is already covered by the distinct indexed Resultary record 2a96c3a15333. That record additionally counts minimum witnesses and discusses exact-size coherence. This is a coverage decision; the later archive date does not determine priority or provenance.

## value

FAIL

The sharp finite-alphabet detection bound and the absence of missing sizes would be valuable as a new exact result. Here the entire interval and both tight endpoints are already covered. The finite verification and the at-most-size restatement do not provide an additional mathematical result beyond that spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
