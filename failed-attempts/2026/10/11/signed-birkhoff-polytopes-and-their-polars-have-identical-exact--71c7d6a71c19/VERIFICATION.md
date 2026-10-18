---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Kohl–Olsen–Sanyal source describes BB(n) as full-dimensional convex hull of all signed permutation matrices and supplies complete facet normals eps⊗e_i and e_i⊗eps with support 1. Both families have squared Frobenius norm n and are centrally symmetric spanning sets. Origin-centered enclosing balls of radius sqrt n contain all vertices; any ± antipodal contact forces radius at least sqrt n and unique center 0. Opposite facet slabs of width 2/sqrt n force inradius <=1/sqrt n and, as normals span, force unique incenter 0; equal-normal-length facets yield contact at all faces. Polarity swaps vertex and facet roles, repeating the argument for C(n). n=1 gives [-1,1]. No John/Löwner general optimal ellipsoid claim or metric invariance under nonsingular transforms.

## originality

FAIL

The 2020 primary source already gives the complete signed permutation vertex set and all facet inequalities of BB(n), with polar C(n). Their norm sqrt n and central symmetry are visibly immediate, and polar duality transfers both. The claimed exact radii, unique centers and every vertex/facet contact are elementary consequences of the source’s explicit complete descriptions, so matching number text is not required for coverage. No new structural/optimization ingredient remains.

## value

FAIL

Computing Euclidean norms of already classified signed-permutation vertices and rank-one sign facet normals, then applying standard antipodal ball/slab and polar correspondences, is a routine textbook deduction from stronger published structural data. No new difficult optimization, motivated classification, or independently useful unknown metric invariant survives beyond this mechanical substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
