---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The six poles have weights 1/15 and eight cube points 3/40; the exact spherical moments through degree four give E_X*E_X=I for all nine harmonics of degree at most two. The addition kernel K(t)=1+3t+5P2(t)=(15t²+6t−3)/2 therefore yields projector B=E_X E_X*. For five deletions T, smallest retained Gram eigenvalue is 1−λmax(B_T). Any erased opposite cube pair has top eigenvalue 9/10; a same-hemisphere pole/cube pair violates positivity of (4/5)I−B_pair; an opposite pole pair has top 4/5 but nonzero coupling to every third erased node forces strict increase. Avoiding these pair patterns forces precisely one erased pole and all four cube points in its opposite hemisphere, exactly six T. Square Fourier modes of the four deleted cube points give 4/5 twice, 1/2, 3/5 once before constant-mode pole coupling; the remaining two eigenvalues are 3/5±(√3−1)/(5√2), below 4/5. Thus the E-optimum 1/5 and full equality spectrum follow by analytic exhaustive pair exclusion. Inspected the full packaged checker: a separate direct nine-function evaluation enumerates all C(14,9)=2002 masks and exactly six winners; exact SymPy kernel-moment identities are supplementary, not the sole proof.

## originality

PASS

The exact weighted 5-erasure E-optimality/equality spectrum for the complete degree≤2 Lebedev 14 grid is not entailed by published exact-degree unweighted ranks or broad quadrature rules in the sources examined.

## value

PASS

The 14-node positive cubature is a natural fixed sensing pool for the nine-dimensional quadratic spherical harmonic space. Its exact sharp tolerance to deletion of five nodes, complete characterization of six optimal minimal-cardinality samplers, and exact lower stability eigenvalue are mathematically substantive finite optimal-design facts with direct interpolation significance. The finite problem is exhaustive by proof, not merely a recomputed table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
