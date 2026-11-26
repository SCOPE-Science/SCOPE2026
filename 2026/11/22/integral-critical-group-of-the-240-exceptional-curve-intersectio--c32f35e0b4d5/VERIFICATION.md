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

For exceptional classes E,F on a degree-one del Pezzo surface, K_S²=1 and E·K_S=F·K_S=−1, so (E+K_S)·(F+K_S)=E·F−1. Under the classical positive-definite E8 model this makes the intersection-one relation precisely orthogonality on all 240 roots. An independent integer replay generated the 240 signed roots, matched antipodal fibres, and counted common neighbors on the 120-fibre quotient: parameters (120,63,30,36). The full graph replaces each fibre vertex with an independent pair, so it is connected, is 126-regular and has 15120 edges. The quotient adjacency eigenvalues 63,3,−9 give full nonzero Laplacian eigenvalues 120^84,126^120,144^35 by doubling on the fibre-constant space and adding 126 on the difference space. The matrix-tree product is 2^508·3^393·5^83·7^120. The separately built reduced 239-square matrix gave exact prime-local valuation multiplicities at 2: (0:120,2:9,3:26,4:50,6:26,7:8); at 3: (0:36,1:48,2:120,3:35); at 5: (0:156,1:83); at 7: (0:119,1:120). Their sums give the determinant valuations, excluding missed torsion; putting the prime lists in increasing order reproduces every stated factor, including 36 units and exponent 120960. Vanishing row and column sums split off one zero from a full Laplacian by integral operations, which also explains the equivalence between the reduced cokernel and full torsion cokernel.

## originality

PASS

The all-root graph, the 126 orthogonality degree and the projective quotient are known. The strongest nearby exact group uses all intersection multiplicities, not adjacency for intersection one. The strongest broader Laplacian Smith theorem inspected applies to isotropic projective points, not the norm-one mod-2 classes of E8 roots. The quotient reduction would make a known full quotient Smith form relevant, but none was found in the read comparisons; neither the quotient parameters nor the prior weighted graph gives the claimed integral factors.

## value

PASS

Intersection one is a natural distinguished relation on the entire uniform exceptional-curve configuration; its root interpretation makes the graph useful independently of surface moduli. The full integral invariant refines the known strongly regular quotient parameters and spectrum, including substantial 2- and 3-power structure not recoverable from their tree order alone. It is not an arbitrary subgraph or a replacement of an already evaluated weighted group by new terminology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
