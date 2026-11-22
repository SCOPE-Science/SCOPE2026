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

Poisson periodization of (1+kappa|x|)exp(-kappa|x|)/(4kappa³) yields sampled discrete symbol f(theta)=(A+Bcos theta)/(1+r²-2rcos theta)² with r=exp(-kappa/n), a=kappa/n, A=1-r^4-4ar² and B=2r[a(1+r²)-(1-r²)]. Positivity follows from positive alias Fourier terms; B>0 since a>tanh a, and f(0),f(pi)>0 imply A>B. Polynomial division of D² by A+Bcos theta gives W+Vcos theta+R/(A+Bcos theta), with R>0; the geometric Fourier expansion with eta=-B/(A+sqrt(A²-B²)) and cyclic periodization proves the stated exact Q_0d for ALL n≥3. For d>=2, the two signed geometric terms have parity (-1)^d and cannot cancel (including odd n and antipodal n even). For d=1, the even-n bound Ht>V/2 makes Q01 negative; for odd n, positive geometric factor increases with n so Q01≤Q01(n=3)<0 from a positive 3x3 exchangeable covariance. Therefore Qij nonzero with sign (-1)^cyclic_distance for every distinct pair. The order-one symbol inverse is tridiagonal, and summing the geometric tail proves the claimed finite-sample error bound; small a gives t→2-sqrt(3). Independent high-precision inversions of the periodic covariance for n=4,5,7,12 and kappa=1,3,0.8,5 respectively reproduced every sign and nearest-neighbor contrast. Finite tests are not the all-n proof.

## originality

PASS

The exact observed-field sample covariance inverse is not the sparse finite-difference/SPDE CAR precision in the main comparison paper. The closest published SCOPE fractional Matérn result establishes a four-site positive opposite entry for s>1, which is a weaker special sign witness rather than the entire formula, every-pair noncancellation, or exponential truncation estimate. Gupta/Fuentes-derived circular covariance and classical ARMA inverse methods are ingredients and potential priority aliases; no actual stronger covering statement was found in the inspected texts.

## value

PASS

The complete versus sparse Gaussian conditional-dependence graph distinction for a natural sampled smooth circular random field is consequential to exact graphical modelling. All-pair signs, exact inverse coefficients and finite-sample locality error distinguish the field from its common CAR approximation and go well beyond a routine small matrix inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
