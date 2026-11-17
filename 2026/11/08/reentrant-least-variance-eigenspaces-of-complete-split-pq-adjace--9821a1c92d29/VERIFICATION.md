---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Reconstructed every vertex of the PQ adjacency polytope as an ordered eligible pair (i,j), N=p²+2pq+q, n=p+q, and its exact block covariance C=((D/N-ww^T/N², B/N-ww^T/N²), symmetric) with B=[[Jp,J],[J,Iq]], w=(n 1p,(p+1)1q). Orthogonal symmetric/antisymmetric diagonalization gives C+= (D+B)/N -2ww^T/N² and C-=(D-B)/N=L/N. Mode multiplicities sum to 2n, including two normal zero modes. Independent exact full-matrix spectrum for (5,5),(5,6),(5,10),(8,3) matched eigenvalues 0(2), n/N(2p-1),p/N(q-1),(p+2)/N(q-1),n(p²+2p+q)/N²(1). Last vs p/N differs by -H_p(q)/N² where H_p=-q²+p(p-2)q-2p², producing all exact integer thresholds and ties (5,5),(5,10). All eigenvalues interpreted in the standard ambient Euclidean embedding and uniform distinct-vertex law.

## originality

PASS

Best-of-knowledge independent source and logical implication comparison supports an exact new statement after explicit credit for known techniques and partial cases. Historical priority is not certified and residual access risks are retained.

## value

PASS

Exact covariance eigenspaces and conditioning are natural quantitative geometry of a well-studied graph polytope; the least-variance mode changes twice in a single parameter family and only special integer sizes tie. This is a structural, complete classification, not merely recomputing the known Laplacian spectrum or normalized volumes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
