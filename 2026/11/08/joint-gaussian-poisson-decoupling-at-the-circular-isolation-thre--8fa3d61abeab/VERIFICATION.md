---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For uniform n-point circular spacings, a graph is connected unless at least two gaps exceed r, hence K=max(1,H), while each isolated vertex corresponds exactly to two adjacent long gaps. With E_i independent Exp(1), gaps E_i/S_n, t_n=nr_n=(log n+x)/2, the fixed-threshold binomial exceedance B has mean c sqrt(n) and variance asymptotic c sqrt(n), with normalized CLT. The random-threshold discrepancy is O_P(log n)=o_P(n^(1/4)), via |S_n−n|=O_P(sqrt(n)); thus K has the stated Gaussian limit. Given H=h long gaps, long-gap locations are uniform and the kth falling factorial moment of singleton vertices is (h)_k(h−1)_k/(n−1)_k, tending c^(2k) when h/sqrt(n)→c. Conditional Poisson and unconditional Gaussian therefore decouple. Dirichlet simplex gives a_j=(1−jr)_+^(n−1); E[HI]=2n a2+n(n−2)a3, E[H]=n a1, E[I]=n a2 and Cov(K,I)=Cov(H,I)−P(H=0)E I→2c². Independent exact evaluation at x=0 for n=100,1000,10000,100000 showed covariance 0.714,1.168,1.551,1.783 approaching 2. This convergence experiment does not prove the limit; analytic expansion does.

## originality

PASS

Huillet (2003) gives exact uniform conditional cyclic compositions and different asymptotic regimes, which are credited. The inspected primary full text does not identify this critical intermediate joint limit or its residual cross-covariance, while other circular results concern edge–isolate or two-vertex-component covariance rather than K versus I.

## value

PASS

The half-connectivity logarithmic window yields two different physically natural scales—mesoscopic components of order sqrt(n) with n^(1/4) Gaussian noise and order-one Poisson isolates—and reveals asymptotic independence despite a nonzero raw covariance. This sharp mixed-limit and residual dependence invariant is meaningful in continuum geometric probability, not a routine small-n sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
