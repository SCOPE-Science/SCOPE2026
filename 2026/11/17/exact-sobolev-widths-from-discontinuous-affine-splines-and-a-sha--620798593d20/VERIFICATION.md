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

For H1(0,1) Neumann cosine coefficients a_n, projection away from constants and normalized affine ell(t)=sqrt(12)(t-1/2) has squared residual sum|a_n|²-|sum v_n a_n|², with v_n=0 for even n, |v_n|²=96/(n^4 pi^4) for odd n. The derivative energy is pi²sum n²|a_n|². For even sector n=2 alone saturates 1/(4pi²); for odd sector q=96/pi^4>27/32 and C=sum_{odd n>=3}|v_n|²/(n²/4-1)<=4(1-q)/5 prove strict suboptimality via Cauchy-Schwarz. Scaling gives each cell h_j/(2pi), and the global sharp seminorm norm H/(2pi) with precisely endpoint-matched cos(2pi cycle)-1 contributions on longest cells. For uniform N cells, cos(2pi Nx) is orthogonal to both affine basis functions on each cell and reaches full H1 constant 1/sqrt(1+(2pi N)^2), matching the known singular value of H1->L2 at index 2N; the projection-zero equality condition forces a global cosine. I independently diagonalized truncated cosine Gram error operators K=4,20,100,500 with maximum squared eigenvalue 1/(4pi²), and checked algebraic equalities. Infinite H1 assertion rests on Fourier energy/completeness and strict odd-mode gap, not finite truncation.

## originality

PASS

Best-of-knowledge PASS for the exact nonasymptotic 2N-dimensional uniform broken-affine spline width and arbitrary-mesh complete seminorm equality family. Yang–Zhang 2026 compares the same k=1,mu=-1,s=1 exceptional regime but states asymptotic A/B bounds and numerical studies, not the exact finite-N identity or all-mesh extremizers. Classic n-width singular values and Poincaré Fourier methods are prior tools but do not themselves assert this specific spline optimality.

## value

PASS

This establishes a rare exact optimality of an elementary finite-element subspace at every even dimension, not merely asymptotic approximation order, together with sharp nonuniform cell-size error and a full equality classification. Those precise constants and extremizers are useful for sharp interpolation/approximation and benchmark discretization studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
