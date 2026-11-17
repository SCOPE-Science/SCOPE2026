---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The finite Euler identity is pre-existing. Define a(n)=mu(n)^2 n/phi(n) and h multiplicative with h(p)=1/(p-1), h(p²)=-p/(p-1), h(p^e)=0 for e>=3. Independent rational checks for n<=300 show a=1*h and 900 exact product checks t=0,1,2. Analytically the local h series has absolutely summable deviations for Re(s)>1/2; local factor at s=1 is exactly 1 and derivative H'(1)=sum_p log p/[p(p-1)] with positive sign. Thus A(y)=sum_{n<=y}a(n)=y+O_epsilon(y^(1/2+epsilon)). For t<1, F_t=1*(n^(t-1)a(n)) and summability of positive coefficients/d yields linear mean with C_t=product_p(1+p^(t-1)/(p-1)). For t>1, Abel summation gives A_t(y)=y^t/t+O(y^(t-1/2+epsilon)) and reversing divisor summation gives zeta(t) X^t/t plus the stated X^max(1,t-1/2)+epsilon remainder, valid for fixed t. At t=1, F_1=tau*h; Dirichlet's hyperbola summatory tau formula and convergent weighted h tails give the explicit coefficient (2gamma-1+sum log p/[p(p-1)]). No claim of a uniform transition window or optimal error.

## originality

PASS

Pain's full published mathematical treatment yields the same prime-product identity for all real t (his s=-t) but its inspected Sections 2–4 and Appendix A do not state the infinite summatory phase law or second-term coefficient. Classical divisor hyperbola asymptotics and Euler products are tools, not the same claimed complete parametric result. Existing related GCD-weighted means have a different summand. Historical equivalence remains a residual risk because the argument uses classical methods.

## value

PASS

This is a natural real deformation of a named arithmetic divisor weight. The critical pole collision yields a sharp exponent change from X to X log X to X^t, a universal supercritical leading constant and an explicit non-obvious prime derivative at the boundary. Those quantitative, family-wide exact facts are useful to analytic-number-theoretic comparison; it is more than a renaming of the Euler product, despite its elementary convolution proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
