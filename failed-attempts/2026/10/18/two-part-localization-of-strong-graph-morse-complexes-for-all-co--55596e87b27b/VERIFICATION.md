---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

FAIL

The proof as frozen contains a false identity in the localization step (RESULT.md line 52): restricting a full order to the first two parts need not produce exactly the same matching. For A={x,x'}, B={y}, C={z}, use x<y<z<x'. The full order produces only (y,x), but the restricted order also produces (x',y). This is a defect in the submitted proof, not a counterexample to the Finding: every full-order pair lies before the first vertex of a third part and survives restriction, so only containment in the restricted matching is needed by downward closure. Conversely an order on a chosen pair can be extended with other vertices last; each later vertex sees at least two earlier neighbours, one from each part, also for singleton parts. In a fixed bipartite order starting in A, let x be its first vertex and y the first B vertex. If at least two A vertices precede y then all pairs target y. If only x precedes y, inspect the next vertex, if any. If it belongs to B then all pairs target x; if it belongs to A then (y,x) is the unique arrow in that direction and all other arrows target y. Together with the symmetric orders, these are contained in the displayed base/flap facets; the facet witness orders are valid. For a,b>=2, distinct same-family patches are disjoint and opposite patches meet in the two orientation vertices only. In each flap the paired lower face contains the tip and another base vertex, so cannot be in another patch, and descending size removes every coface except the specified one. Base collapse pairs subsets of size at least two avoiding a chosen root with their root extensions; all flap edges already remain fixed. The resulting patch trees are joined at orientation vertices and form a connected graph with (V,E)=(2ab,4ab-a-b). For one singleton the entire complex is the other patch and collapses to a point by leaf deletions; for two singletons the complex is two isolated vertices. The equivariant cycle lattice follows from the short exact simplicial chain sequence from the direct sum of pairwise overlap complexes to the direct sum of patch complexes to the union. Map each overlap generator labelled (v,w) to its copy in the w patch minus its copy in the v patch. This is natural even under part swaps; H_1 of a patch vanishes and H_0 is one copy of Z, giving exactly the displayed incidence kernel. H_0 follows from the component set. Thus the stated theorem is independently recoverable by the specific correction above. Inspected verify_faces.py, verify_collapses.py, both recorded outputs and VERIFICATION.md; no source script run. Finite face/mod-2 and free-face checks do not prove localization universally or check equivariance. Scope is the full complex of the unfilled simple graph, not the clique complex.

## originality

FAIL

The principal exact localization is already covered on all-nonsingleton inputs by a distinct indexed theorem using the same order argument, and the unrestricted statement follows by induced restriction. The claimed pair-collapse and labelled integral module are also covered by distinct indexed statements; the singleton collapses are obtained directly from the published star facets. These are actual coverage and implication findings, not conclusions about which record originated the ideas. The later and same-date labels are not used to infer discovery order. No nonroutine surviving remainder was found.

## value

PASS

The principal structural result explains a strong topological obstruction on a connected natural graph family, gives a one-dimensional model and records its integral symmetry, all of substantive mathematical use. Once the overlapping indexed results are accounted for, the elementary singleton bookkeeping and direct sums alone do not justify a repaired new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
