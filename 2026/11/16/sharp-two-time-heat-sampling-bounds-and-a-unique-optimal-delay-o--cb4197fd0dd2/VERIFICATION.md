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

Fourier–Plancherel on the longitudinal Z variable yields the exact fiber M_t(ω)=[[1,0],[q cosh(t/3),q sinh(t/3)]] for q=e^{-t(1−2cosω/3)}, bounded away from zero for each fixed t>0. Its Gram form is diag(1,0)+q² vv*, nondecreasing in q², so the sharp essential lower endpoint is ω=π and upper endpoint ω=0. Putting r=e^{-2t/3} gives M_-=[[1,0],[r²(1+r)/2,r²(1−r)/2]], M_+=[[1,0],[(1+r)/2,(1−r)/2]], hence exact traces and determinants and both quadratic eigenvalue bounds. Fourier inversion gives the bounded explicit recovery formula for f_1. Differentiating the lower characteristic root gives critical polynomial P=3r^6−3r^5+5r^4−5r^3+5r²+4r−4; its stated derivative decomposition is strictly positive on [0,1]. P(0)<0<P(2/3), critical eigenvalue lies on the small branch, and the boundary lower bound tends to zero at both ends, proving a unique global optimum. Independently verified the polynomial resultant identity exactly using SymPy and r*=0.6377325420915736, t*=0.6747544448314551, A*=0.004882704478092798.

## originality

PASS

The Fourier fiber and generic dynamical sampling stability conditions are classical, but the exact two-rail unweighted normalized-Laplacian A(t), B(t) and globally A-optimal sextic delay are a different objective from the published Cartesian strip D-optimal determinant delay, even in transverse width two. The ordinary integer-line even-site problem has a spectral blind spot absent here. The 2026 graph Paley–Wiener source was only accessible partly; its unknown complete contents and older one-rail observability calculations remain risks.

## value

PASS

Observing only one entire rail at two times is a concrete natural undersampling design. The sharp worst-case recovery energy, explicit inverse and unique delay maximizing the lower frame bound provide an optimal robustness parameter for every ℓ² input. It is not just sampling injectivity, a generic Vandermonde criterion, or an arbitrary scalar optimization; the physically meaningful worst-case stability objective and full continuous spectral extremum are resolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
