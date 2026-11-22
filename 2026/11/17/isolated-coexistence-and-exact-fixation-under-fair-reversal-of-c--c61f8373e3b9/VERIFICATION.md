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

For 0<a,b,c<1, the globally synchronized fair sign map X_i*=X_i(1+sigma(AX)_i) preserves the simplex and each coordinate is a bounded martingale. Summable expected conditional quadratic variations imply X_infty,i*(AX_infty)_i=0 for every i. A has rank two, positive kernel span(b,c,a); its common fixed set consists exactly of three vertices and r=(b,c,a)/(a+b+c), because any two positive species with the third zero interact nontrivially. The weighted geometric mean H(x)=prod_i x_i^{r_i} contracts under each sign by weighted AM-GM and has a unique global maximum at r, excluding convergence to r from any x!=r including boundary points. The limit is a vertex and E X_infty,i=x_i gives P(I=i)=x_i. On winning event, Cesaro continuity of log(1+sigma_k (AX_{k-1})_j) and the full-probability sign SLLN yield the claimed half-log(1-A_ji^2) rates. Invariance plus almost-sure convergence shows every stationary law is a mixture of the four fixed points. Independently verified at a=1/2,b=1/3,c=1/4 that r=(4,3,6)/13 and exact conditional martingale and quadratic variation identities hold. No result is claimed for correlated in time, biased signs, or independent edge switching.

## originality

PASS

Qualified best-of-knowledge originality after searches for identical and stronger implications, exact records, primary material, and same-object aliases; relevant previous methods are acknowledged. No inspected prior theorem logically implies the exact correlated-sign r-exception, probabilities and exponents. This is a genuine change of noise correlation structure, not a parameter substitution in independent-edge fixation.

## value

PASS

A global sign reversal preserves a unique positive cyclic coexistence fixed state even though all other compositions fixate with their exact initial shares and explicit extinction rates. The classification sharply separates common-environment correlation from independent pair fluctuations and is the natural complete small cyclic (nontransitive) Volterra case, including all invariant laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
