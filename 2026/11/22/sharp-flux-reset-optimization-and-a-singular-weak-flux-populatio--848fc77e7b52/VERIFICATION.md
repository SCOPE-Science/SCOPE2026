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

The Poisson renewal integral gives a density matrix and r+i ad_H is invertible for r>0. Independently distribute the phase clockwise by a diagonal gauge and diagonalize the resulting circulant in the Fourier basis, with dimensionless E_k=2 cos(Phi/3−2*pi*k/3). Let d_k=E_(k+1)−E_k cyclically. The sums of d_k and d_k² are 0 and 18, the sum of pairwise products of squared gaps is 81, and their signed product is 6*sqrt(3)*sin(Phi). The reset population difference is (2*sqrt(3)*u/9) times sum d_k/(u²+d_k²); combining terms gives the signed numerator and Q in the Finding. The Fourier route checked the diagonal normalization and 30 parameter pairs, including extremely small rate and sine flux. Direct differentiation verifies the optimizer polynomial. Descartes' one sign change together with the endpoint signs proves a unique positive simple root and a maximum. Equivalently h=x(x³+11x²+27x+81)/(108(x+1)) is strictly increasing for x>0, giving a smooth optimizer there. At that root the fixed-rate flux derivative has the sign of x(x+9)²−108h=8x²(x+9)/(x+1)>0. The h=1 factorization gives the unique maximizing rate and |bias|=0.24306121012757808026… . Near h=0 the implicit root is 4h/3+O(h²); setting u=(2/sqrt(3))|s|+O(|s|³) in the formula gives 1/(3 sqrt(3)). At s=0 every positive rate has zero bias, so no exchange of optimization and flux removal is valid.

## originality

PASS

The distinct result is the rate-and-flux optimization of a stationary directional occupation imbalance, including the genuinely singular optimized weak-flux limit. The known general stationary reset resolvent and its evaluation on this triangle are not credited as a new reset framework. The closest triangle-and-Poisson studies optimize a different objective under a different dynamical map.

## value

PASS

The homogeneous triangle is a minimal loop with a gauge-invariant phase. The optimization determines whether directed population imbalance can persist under weak symmetry breaking when the reset scale is tuned, and gives the measurable rate scale and absolute bound. The singular limit distinguishes near-degenerate dynamics from setting the phase to a symmetry value at the outset; it is substantive beyond the routine stationary resolvent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
