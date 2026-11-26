---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independently differentiated Y=(p+qx)/(1-x) along the flow to obtain Y'=ΛY and checked Y(x+a)=((Λ+aq)Y+aq²)/(Λ-a(Y+q)). A finite flow starting below one stays below one; the pre-pulse Y(t)=y exp(Λt) reaches the cap-activation value Λ/a-q only at t_c=log(H_c)/Λ. This gives exactly the saturation interval [t_c,T], a singleton at T=t_c. On the nonsaturating part the derivative is a strictly positive variational factor times f(x_t)-f(x_t+a)=a(p-q+2q x_t+qa), whose sign can change only from minus to plus. There are no interior nonsaturating maxima. Comparing HP_a(y) with P_a(Hy) over their positive denominators gives sign(H_*-H). The numerator in H_*-1 factors as (q+y)[Λ(q-y)-aq(q+y)] over a positive denominator, giving the stated strict parameter criterion. The threshold gap is Λ²/{a[aq(q+y)+Λy]}>0; both thresholds are positive, H_c>1, and H_*=1 cannot be a tie at any T>0. For proportional reach, the transformed terminal state is [Hy+Hqθ exp(-Λt)]/(1-θ), strictly decreasing in t. The exact witness gives both transformed endpoint values 10 at H=45, hence terminal adoption 9/10; H_c=100. The plateau's left endpoint is fixed in calendar time, so the proof's phrase 'grows continuously backward in calendar time' should be understood relative to the horizon endpoint. The formula and classification are correct. VERIFICATION.md and verify.py were inspected; python3 verify.py from the package directory is the optional exact-rational replay path, not the universal proof.

## originality

PASS

No technical statement inspected supplies the exact nonsaturation switch and cap classification plus the contrasting fixed-proportion result. The Bass flow, the equivalent normalized logistic flow and projective algebra are standard; the gap is the complete timed-pulse optimization, not any of those ingredients or an empirical marketing law. Historical priority remains provisional.

## value

PASS

A complete boundary and equality classification for a natural one-intervention model is more informative than a single early-seeding intuition or a single worked trajectory. It distinguishes a true reversal of strict endpoint optimality from the later cap plateau and shows the reversal disappears under a different, natural definition of campaign reach. The two definitions are not cost-equivalent and no empirical profitability or optimal advertising intervention is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
