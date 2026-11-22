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

For 1<p<infinity, -1<gamma<p-1, delta>-1, logistic y=log(x/(1-x)) with Uf=xf is an onto isometry into L^p(R,rho dy), rho=e^{-pAy}(1+e^y)^{p(A-B)}, A=(p-1-gamma)/p>0, B=(delta+1)/p>0. It transforms the singular Cesaro operator into H g(y)=integral_-infty^y g(s)ds. The conjugated translation semigroup R_t has exact sup weight ratio exp[-t min(A,B)], proving ||H||=1/min(A,B) by long tail plateau lower tests; strict positive convolution/translation norm arguments rule out a norm-attaining nonzero L^p input. H is the graph-norm inverse of derivative D on weighted Sobolev domain. For spectral reciprocal zeta=1/lambda, D-zeta has explicit one-sided decaying inverses outside the two limiting rates; between rates, a one-dimensional kernel if A<B and a codimension-one annihilator if A>B. On boundary lines, escaping localized plane waves force nonclosed dense range, while H itself has dense nonclosed range at lambda=0. Hence reciprocal closed strip spectrum and Fredholm essential circles Gamma_A union Gamma_B; the eigenvector and functional transform correctly back to x coordinates. Independently evaluated two rational Jacobi endpoint regimes: p=5/2,gamma=-1/4,delta=3/4 gives A=B=7/10; p=2,gamma=-2/5,delta=4/5 gives (A,B)=(7/10,9/10), sharp norm 10/7. Finite diagnostics only confirm algebra, not operator Fredholmness.

## originality

PASS

Qualified best-of-knowledge originality after searches for identical and stronger implications, exact records, primary material, and same-object aliases; relevant previous methods are acknowledged. The weighted result is a genuine extension as a theorem on an enlarged natural Banach family. Its basic first-order Fredholm method is not novel as a general theorem; unindexed weighted versions remain a priority risk.

## value

PASS

Jacobi endpoint powers independently move the two exponential decay rates, creating nonempty weighted Fredholm crescents even at p=2 where unweighted L^2 has one boundary circle. The exact norm, eigenvalue/cokernel phases and weighted range functional give a reusable quantitative classification of a natural singular integral operator, not an arbitrary finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
