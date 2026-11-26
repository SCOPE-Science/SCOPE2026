---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Cut the cycle at the absorbing target and use interval endpoints 0 and m; each reset returns to the interior starting site and counts one step. Solving the discrete harmonic recurrence gives the cosh ratio F(s). With s=1-r, a cycle between renewals succeeds with probability F(s); its expected duration, including a reset on failure, is sum_{k>=0} s^k*Pr(T>k)=(1-F(s))/r. This gives the stated mean. The even and odd cosh quotients satisfy the printed ODE (in the odd case the divided-out cosh(t/2) introduces the extra w coefficient); coefficient comparison gives c_1(j)=j(j+epsilon) and the recurrence. For d=a-b, alpha-beta=d(m-d); the numerator N of the mean excess has no constant or linear term and its quadratic coefficient is mu*(5*mu+5-m^2)/6. Thus the right derivative has that sign. For beta small (b=0,1), all higher terms come only from P_a and its shift. For b>=2, a nonnegative quadratic term implies alpha/beta>=4, including b=2 even by the integrality of a. For 3<=j<=b+1 the coefficient ratio is at least 4^(j-1)>j*(2*j-1), whereas the required threshold is at most j*(2*j-1) since alpha-q>=mu. Beyond b+1 all remaining coefficients of N are nonnegative and the leading one is positive. This proves strict worsening at every 0<r<1 on the entire weak reverse side, not just for small resets. In particular for m=5,d=1 the polynomial gives H=4+4*w^2/(1+2*w), strictly larger than 4 even though the derivative is zero; for d=1 the strict-improvement condition is m>=6. Frozen verification notes and script were inspected, not run; the proof supplies the infinite claim.

## originality

FAIL

Exact scientific coverage in two earlier-dated indexed records. The October 26 record uses the identical walk and full-step reset cost, states the identical strict global exclusion including equality and the identical phase line, and further classifies the whole improving interval and cutoff. The October 18 gambler's-ruin record gives the equivalent result on the interval obtained by cutting the cycle at its absorbing target, including the exact derivative coefficient and essentially the same parity-Chebyshev coefficient certificate. This is demonstrable statement and proof coverage, not a verdict based on title, date alone, unavailable literature, or a merely local prior test.

## value

FAIL

The global-versus-local distinction is meaningful for resetting, but this package adds no demonstrated substantive advance over the already available result for the same walk. Its alternate ratio estimate establishes the same positivity certificate already present for the equivalent interval, while the earlier cycle result additionally resolves the beneficial interval and distance nesting. The frozen finding gives neither a strengthened classification nor a distinct proof mechanism that would make the repeated theorem valuable as a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
