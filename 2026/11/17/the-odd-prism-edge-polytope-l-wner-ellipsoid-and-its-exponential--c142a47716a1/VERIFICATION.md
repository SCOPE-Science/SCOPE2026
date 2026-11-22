---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For connected odd-rim C_m x K2, the unsigned incidence columns span the 2m-dimensional ambient space and edge differences span the zero-sum L of dimension 2m-1, with unique symmetry center mu=(1/m)1. Fourier decomposition of orbit covariance gives eigenvalues [(1-x)(1+cos 2pi k/m)+2x]/m (symmetric k=1..m-1), [(1-x)(1+cos 2pi k/m)]/m (antisymmetric k=0..m-1). The root-of-unity product yields determinant F_m(u)^2(1-u²)^m/(2m)^(2m-1), u=sqrt(x). Strict concavity of log det, a positive derivative at x=0 and zero endpoint determinant ensure a unique interior optimizer satisfying ((1-u)/(1+u))^m=(1-2u)/(1+2u). At stationarity two edge-orbit leverage scores coincide and their weighted mean is dimension d; hence all 3m edge points contact the John/Löwner covariance ellipsoid globally, not only among symmetric rivals. Setting delta=1/2-u and expanding stationarity proves x=1/4-3^{-m}+O(m9^{-m}) for odd m. Independent numerical diagonalisation and leverage/determinant checks for m=3,5,7,9,11,19 agreed to numerical tolerance, including first exponential coefficient.

## originality

PASS

Best-of-knowledge PASS. D-optimal signed-Laplacian spanning-tree cyclic-ladder design is a different determinant problem; on odd nonbipartite prisms no vertex sign switching converts unsigned signless incidence to signed Laplacian. A same-day full RESULT for *ordinary wheel* edge polytope has a different graph and one-third algebraic spoke law; the exact 1/4 geometric correction here is neither its special case nor an implication of general John design theory. Ordinary/symmetric edge polytopes are carefully distinguished.

## value

PASS

The complete semiaxis and contact solution for a natural infinite family of nonbipartite graph-edge polytopes, especially a sharp exponentially small optimal spoke-weight deficit, is a motivated exact convex-geometric invariant and highlights nonbipartite parity effects not captured by signed-Laplacian design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
