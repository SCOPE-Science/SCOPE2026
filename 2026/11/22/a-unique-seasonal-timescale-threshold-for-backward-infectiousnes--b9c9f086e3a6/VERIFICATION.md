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

The infinite-past survival integral converges by a positive hazard lower bound and is the continuous periodic solution of A'=1-gamma A between switches. The period map contracts by exp(-(a+b)h), so the periodic solution is unique. Writing u=exp(-ah), v=exp(-bh), the phase-entry deviations from 1/a and 1/b are (1/b-1/a)(1-v)/(1-uv) and (1/a-1/b)(1-u)/(1-uv), giving the claimed pointwise inequalities and mean by integrating the phase transients. For Q=(1-u)(1-v)/(1-uv), the addition law for sinh also gives Q/h=2/[h coth(ah/2)+h coth(bh/2)]. Each h coth(k h) is strictly increasing for k>0 because sinh(x)cosh(x)>x for x>0. Hence the mean strictly increases for unequal hazards (constant for equal hazards). The expansion Q/h=ab/(a+b)-a^2 b^2 h^2/[12(a+b)]+O(h^4) and Q=1+O(exp(-min(a,b)h)) give both stated endpoints and corrections. Their reciprocals give the open crossover interval; its endpoint transmission rates achieve equality only as a limit, not at a positive finite h. The infection multiplier exp([2 lambda-a-b]h) gives negative per-time growth throughout that open interval, independently of the averaged kernel. Direct one-period backward-survival integration, summing past periods geometrically, reproduced the example by midpoint quadrature; closed-form substitution refines h*=1.91906667452146 and mean values 0.8985767662 and 1.0068835911 at h=1 and 2. The supplied checker was inspected, not executed. This is an index crossing, not a change in invasion stability or an inference from incidence.

## originality

PASS

Best of current knowledge: pass the exact two-phase switching-duration classification and its separation from the invariant negative growth exponent. Neither the scalar invasion calculation nor the general periodic residual-lifetime construction is new. Forward and backward orientation differ pointwise, but cannot by themselves make the period-average result distinct. The closest inspected forward formula is for a different, smooth hazard family; the matched period-average classification and exact crossing are not established by the inspected prior statements.

## value

PASS

This is a precise counterexample to using a period-averaged, nonstationary kernel mass as an invasion criterion. It fixes the two rates and changes only the calendar scale, locating the entire unique crossover while true scalar decay retains the same exponent. The exact interval and asymptotes make it a useful calibration check beyond a single numerical example. The result does not give an epidemiological scheduling recommendation or establish a threshold in observed transmission data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
