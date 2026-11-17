---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The count generator is the standard four-rate K_(m,n) zealot model; stationary first moments from Lp=q-p+(1-q)/m and Lq=p-q-p/n give Ep=n/(m+n-1), Eq=(n-1)/(m+n-1). Stationary E(p-q)^2=O(1/m+1/n) synchronizes the two part fractions. Rescaled generator converges to (theta-x)f'(x)+x(1-x)f''(x)/2; polynomial moments recur μ_k=(2theta+k-1)μ_(k-1)/(k+1), uniquely giving Beta(2theta,2-2theta) as m,n→∞ at interior ratio. The proof accommodates the transient corner and boundary cases; earlier stronger full derivation independently verifies same generator and joint limit. Finite checks are not used as an infinite convergence proof.

## originality

FAIL

FAIL: A published November 2 full theorem gives the same network, fixed positive zealot in the m part, fixed negative in n part, independent rate-one neighbor-copying, exact stationary first moments, all within/between-side pair correlations and the joint Beta(2(1-ρ),2ρ) limit with ρ=m/(m+n). Since theta=n/(m+n)=1-ρ, this is precisely the submitted Beta(2theta,2(1-theta)). An additional November 8 published theorem obtains the same Beta limit and even an exact finite variance. No surviving new assertion in this final submitted claim.

## value

FAIL

FAIL: the entire claimed finite means, synchronization, joint limit and skew shape are already explicit stronger prior results for exactly the same Markov chain; repeating their consequences without a new mathematical invariant or restriction is a covered recomputation, not independently valuable research content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
