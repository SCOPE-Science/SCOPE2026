---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Differentiating v=beta*S/N,h=beta*I/N yields v'=v(a-h), h'=h(v-(gamma-a)); F(v,h) is coercive with a unique center and closed positive nonzero levels. Physical I=(N/beta0)e^{-at}h and incidence c=(N/beta0)e^{-at}vh. Exact logarithmic growth signs are v-gamma and v-h-(gamma-a). Restriction of F to each crossing locus has a unique minimum, and transversal crossing away from equality gives exactly one minimum and maximum per transformed period. Equal energy is tangential without a strict extremum. Independent numerical algebra gave a=b=0.5, h_c=sqrt(2)/4, E_c=0.11299357795674864, E_I=0.15342640972002736; for (v,h)=(0.93,0.5), E=0.11971175613744506 falls strictly between, witnessing incidence-only oscillatory peak regime. Finite tests do not establish perpetual cycling; the integral and orbit geometry do.

## originality

PASS

Crucial direct predecessor found and materially read: the 2026-10-13 published theorem on the IDENTICAL exponentially forced closed SIR model already proves the Lotka–Volterra reduction, exact prevalence threshold and geometric attenuation, not merely a different control law. After normalization v=gamma*Q,h=a*P, its E>gamma+a is precisely F(v,h)>F(gamma,a). These elements are NOT original. The present final two-observable threshold theorem is nonetheless strictly stronger in a material direction: it gives the exact necessary-and-sufficient INCIDENCE threshold E>E_c, proves a unique incidence max/min each cycle, and identifies a nonempty E_c<E≤E_I regime with incidence waves but no prevalence peaks. The predecessor proves only at least one incidence maximum for E>E_I and offers no converse or E_c. This specific exact incidence phase boundary is a natural and independently valuable uncaptured mathematical fact. The source's literature narrative omits that direct predecessor; this omission is documented explicitly and must be corrected in any further scholarly release, though the mathematical claim as a stronger two-threshold theorem survives.

## value

PASS

Sharp observable-specific separation is important in dynamical epidemiology: incidence peaks can recur even while prevalence decreases monotonically, and the exact energy window determines when this happens. This nontrivial boundary is not the already-known log-linear forcing, LV reduction, or damping law. Meaningful all-initial-data exact classification; not an empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
