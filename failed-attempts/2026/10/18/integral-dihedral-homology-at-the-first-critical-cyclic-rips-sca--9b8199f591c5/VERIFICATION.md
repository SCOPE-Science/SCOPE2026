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

PASS

For a clique containing 0, the forward and backward extremal distances a,b satisfy a+b≤r or a+b≥2r. The former puts the clique in a window, and the latter forces a=b=r and no further vertices. The window complex collapses to the original cycle: at each window length s from r down to 2, every endpoint pair {i,i+s} belongs to a unique s-window (2s<3r). Pair faces containing the endpoints and missing i+1 with their extensions by i+1, in descending cardinality. The free-face test follows from the uniqueness of the window and the removal of larger cofaces; the survivors are precisely the shorter windows. The inclusion of the original cycle, unlike the choice of collapse, is equivariant. In the pair only the r triangles remain, with their cyclic orientations; their three forward edges each expand in their windows to r consecutive positive edges. Every relative generator therefore maps to the same primitive cycle generator. Rotation permutes the r generators without sign, including wraparound, and reflection reverses orientation, so the integral kernel is exactly the signed augmentation lattice. Fixed-index counts yield both traces, including the even/odd reflection split. For r=1 the whole triangle is contractible, consistent with the summation map being an isomorphism. After barycentric subdivision the rational quotient cellular chains are the rational coinvariants; exactness by finite-group averaging identifies rational homology with the corresponding coinvariants, zero in reduced degrees because the single rotation acts transitively on the augmentation indices. Both frozen scripts were inspected but not executed; their bounded mod-two and trace tests are not the reason for the all-r integral conclusion.

## originality

FAIL

Resultary 5fa1191ef272 gives the identical graph-metric complex, specified dihedral action, integral signed kernel, and character for every r≥2. The differences, r=1 and rational homology of the full quotient, are immediate consequences of the filled simplex and the stated representation with rational averaging. This determines current statement-level coverage, not a priority claim: the dated equivalent indexed record is later than the frozen one.

## value

FAIL

The integral dihedral lattice is a meaningful invariant at a natural scale, but the exact computation is already covered. The r=1 endpoint and rational quotient are routine deductions, with no separate surviving invariant such as integral quotient torsion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
