---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The unfilled graph hypothesis gives the full t-skeleton plus precisely the (t+2)-subsets with an edge; there are no higher cells. Contraction by augmentation in the exterior chains gives degree-t cycles wedge^(t+1) W, where W is the vertex augmentation lattice. Fixing edge uv, its difference e_v-e_u is one of the integral basis vectors e_a-e_u of W. The boundaries of the top simplices containing uv span exactly (e_v-e_u) wedge wedge^t W. Summing over edges therefore gives the saturated boundary image: the edge-difference subgroup U is the kernel of the canonical surjection W to W_C, and the exterior quotient is wedge^(t+1) W_C. This proves naturality and torsion-freeness, and counting top faces minus boundary rank gives B_(t+1). The t-skeleton collapses after quotienting the contractible star of one vertex to a wedge of t-spheres. For t>=2 the based homotopy classes of attachments from a wedge of t-spheres are classified by the matrix in H_t (Hurewicz); pre- and post-composition with self-equivalences implement the two unimodular changes of basis without changing the homotopy cofiber. Saturation makes every nonzero diagonal a unit, leaving the two types of spheres. This also handles edgeless graphs and the t=n-2 endpoint; for t>=n-1 one can delete to a vertex. The illustrative cycle and two-disjoint-edge ranks agree by direct counting. Inspected verify.py, which tests only finite mod-two ranks; no source checker was executed. The theorem itself is correct; the inaccurate bounded-independence comparison in the source's prior-work section is addressed under originality.

## originality

FAIL

A distinctly indexed all-tolerance record, f6b5c138b0b0, directly covers the entire Finding with identical graph and tolerance conventions. Its natural integral lattice, lower rank, contractible range, and upper rank after Pascal's identity are the same. It even uses the same exterior-boundary and attaching-matrix proof. The catalogue date alone cannot establish which came first; the failure is demonstrable duplicate coverage, not a claim about priority or copying. No scientifically distinct remainder of the Finding survives that comparison.

## value

PASS

The mathematical statement is intrinsically useful: for every unfilled finite graph the component lattice controls the lower spheres and the top multiplicity follows from a concrete independence count, with an integral homotopy conclusion beyond existing general Leray bounds. This assesses the substance of the theorem, not any additional contribution over the distinct already matching result; no such remainder was found.

The dated certificate retains the supplied scientific assessment, sources and limitations.
