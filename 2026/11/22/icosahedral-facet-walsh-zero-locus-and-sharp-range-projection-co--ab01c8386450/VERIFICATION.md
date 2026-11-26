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

Expanding the three sign factors per triangle and summing uses five facets per vertex and two per edge, giving 20−10|S|+8(e−t). Complementation reverses every facet sign; reducing modulo eight leaves only sizes 2, 6, 10. The size-two zeros are exactly the 36 nonedges, and size six requires e−t=5. An independent exact calculation from the cyclic coordinate families (0,±1,±φ), with φ²=φ+1, uses squared distance four for edges and 3-cliques for faces. Direct face signs, the structural formula and the integer Walsh transform agree on all modes. The calculation reproduces all bins of the signed spectrum, the 724 six-set zeros by (e,t), and all bins of the inverse Walsh transform of the nonzero-mode mask. Rank is 3300 and nullity 796; on the orthogonal complement of the kernel the multiplier moduli range from two to twenty, yielding the pseudoinverse norm and condition number. In the convolution matrix of the range projection, every row and column has the same absolute sum, 56232/4096, so this is both endpoint norms. For any projection onto W, its translation conjugates fix W pointwise and map into W. Their average still has those two properties and commutes with translations. The joint character spaces are one-dimensional over either scalar field, forcing the average to be identity on the surviving modes and zero on the others. Since translation is isometric, averaging cannot increase either endpoint norm. Thus the all-projections minimum follows analytically, not from checking a numerical kernel. Exact replay: independent_icosahedron.py with independent_run.txt; the frozen verifier was inspected, not executed.

## originality

PASS

The distinct contribution is the exact facet-incidence zero set, complete signed spectrum, and sharp numerical range-projection norm for this specific graph, not the geometry or the projection averaging principle. The strongest inspected prior six-set statement describes a 200-element family contained in the new 724-element six-set zero family; it neither refers to the Walsh observable nor determines the other zeros or norm.

## value

PASS

Facet convolution is a natural symmetric operator on vertex-set functions. Its null modes identify precisely which character signals it erases, while the endpoint projection constant is the exact cost of extracting its attainable range in the two endpoint norms even with unrestricted choice of projection. Those invariants are not determined by the vertex-facet incidence counts or by the Hilbert condition number. The zero criterion and independent exhaustive census give structural and quantitative information for a fixed, natural object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
