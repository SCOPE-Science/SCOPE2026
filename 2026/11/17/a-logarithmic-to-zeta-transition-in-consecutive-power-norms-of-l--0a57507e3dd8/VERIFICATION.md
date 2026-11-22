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

For the specified bounded backward shift on complex ell^1, W^k e_j=(j/(j-k))^alpha e_{j-k} for k<j. The exact coefficient of T^{n+1}-T^n on each distinct output coordinate is delta(b_{n,k-1}-b_{n,k}), giving the exact positive column maximum over 1<=j<=n+2 with d_{n,k}=|b_{n,k}-b_{n,k-1}|. Independently verified by rational finite-dimensional operator iterations for n=0..5 and alpha=1,2, delta=1/3 (12 cases), not merely logs. Stirling plus the exact binomial ratio imply sigma_n^2 d_{n,k}->g(s)=|s|phi(s) centrally with a Gaussian polynomial envelope and sum_k d_{n,k}=2 max b_{n,k}=O(1/sigma). For alpha>1, reindex h=j-k, apply dominated summability of h^-alpha to obtain zeta(alpha)g(s), leading coefficient delta^alpha/(1-delta)*n^{alpha-1}. For alpha=1, harmonic sum over h<=eta sigma_n gives (1/2)log n while h>eta sigma_n contributes only O_eta(1); the sharp coefficient is delta/[2(1-delta)] g(s). Columns outside [mu/2,2mu] are negligible by Chernoff; within, Gaussian flank escape is excluded using the envelope and summability/tail split. g has exactly two global maxima s=+-1, value 1/sqrt(2pi e). Spectral radius/eigenvectors and renewal lower bound for lack of absolute Cesaro boundedness use their stated regimes. The proof is infinite dimensional via exact columns plus analytic local limits, not an inference from the 87 finite checks.

## originality

PASS

This exact same shift family is known for 0<alpha<1, but the critical alpha=1 logarithmic constant and every alpha>1 zeta constant fall outside its theorem and require a different nonintegrable-kernel analysis. No compared primary source or Resultary theorem covers the endpoint/supercritical sharp limits.

## value

PASS

The same operator family exhibits a genuinely singular mathematical boundary when alpha reaches one; an integrable fractional Gaussian integral switches to a harmonic-logarithmic contribution, then zeta(alpha) times power growth. Exact sharp constants and location of norming columns are natural operator-norm invariants with plausible use in ergodic/operator asymptotics; they are not a routine continuation of the previous alpha<1 result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
