---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For q>=3,n>=3 set m=n-1 and r=q-1. The overlap digraph on words with <=2 nonzero positions is balanced, strongly connected, and has q outgoing edges at vertices of weight 0 or 1 and one outgoing edge at weight 2. Directed BEST with canonical 0^n edge gives ((q-1)!)^(1+mr)*t_o. Forced weight-two zero-appending edges contract to transitions on (a,j), yielding rooted Laplacian qI-S tensor I_r-R tensor J_r. Splitting color into constants and sum-zero gives t_o=q^(m(r-1))*det(qI_m-S-(q-1)R). The triangularization by columns of cumulative ones and endpoint-distance order gives determinant q^floor(m/2), including m=1. Independently constructed the reduced full integer Laplacians and computed exact determinants for q=2..5 and n=2..8; all match. This finite matrix check is not an all-q/n proof. BEST counts rooted cyclic tours uniquely via sole 0^n window.

## originality

PASS

The binary specialization q=2 is already enumerated by older published binary weight<=2 universal-cycle findings and is expressly not claimed new. Known nonbinary bounded symbol-SUM-weight de Bruijn decoding constructions and random universal-cycle sampling do not state the Hamming-weight<=2, separately labeled nonzero symbols, all-q,n product formula. No equivalent q>=3 count or stronger covering theorem was located in targeted searches and inspected material; best-of-knowledge PASS, not a priority guarantee.

## value

PASS

Sparse constrained universal cycles are natural de Bruijn/Eulerian objects. The exact nonbinary Hamming-weight-two global count is an independently useful enumeration, with a nontrivial factorized directed Matrix–Tree determinant that separates color and position. It is not a mere binary renaming: q>=3 has independently labeled nonzeros and extra positive-degree and color components; the exact count could support coding/decoding or uniform generation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
