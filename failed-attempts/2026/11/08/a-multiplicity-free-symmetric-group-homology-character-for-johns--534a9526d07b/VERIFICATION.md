---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Inspected the full all-parameter star/top-clique and Frobenius-characteristic argument in frozen RESULT.md and its independent finite checker source. For 3<=k<=n-3, maximal Johnson cliques are stars (fixed (k-1)-subset) and tops (fixed (k+1)-subset); faces of size>=3 lie uniquely in one, allowing elementary collapse to a connected 2-core. The hypersimplex's simply connected triangular 2-skeleton spanning the entire Johnson 1-skeleton gives pi1=0. Equivariant Euler characteristic then isolates actual H2 (not merely virtual Euler class), with signed edge module h_(k-1) h_(n-k-1) e2. Frobenius/Pieri or equivalent Jacobi-Trudi telescoping cancels 2-row/3-row partitions and yields each S^(n-j-2,j,1,1) once for 1<=j<=min(k,n-k)-1. Verified the n=6,k=3 dimensions 10+9=19 and denominator boundary k>n/2 through complement equivariance. Finitely tested characters are corroboration only; all-parameter scope follows from the symbolic proof. No integral Specht splitting claimed.

## originality

FAIL

FAIL decisively: the Oct 25 published Johnson-graph clique/Rips S_n homology theorem gives the SAME universal Specht decomposition in exactly the same parameter range. Nov 1 additionally gives the all-weight complete cycle-type character. The present alternative Euler derivation cannot be accepted as original mathematical final claim.

## value

FAIL

FAIL as submitted: the representation-theoretic refinement would be a substantive natural invariant, but the complete multiplicity-free Specht formula was published earlier for all the same n,k; the present theorem and no-invariants corollary add no unknown fact. A distinct character calculation is verification, not new mathematical value in the submitted final statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
