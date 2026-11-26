---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Conditioning on the first-site native winner gives the subdensity a exp(-ks), not a density normalized to one. The post-opening native-win probability for site 2 has the factor c/h, and for s>t the extra invasion-free factor is exp(-d(s-t)); those disjoint cases give the displayed P_T. The convolution satisfies J'(u)+(k+d)J(u)=1-exp(-hu), hence the derivative factors into a positive prefactor times F(T-t)-G(t). With positive rates F is strictly increasing for u>0 and G strictly increasing; the signs at t=0 and t=T are opposite. The implicit derivative is a strictly positive ratio below one. J(u)=hu^2/2+O(u^3) first forces t_T=O(T^2) and then gives dT^2/2; as T grows both time intervals diverge by the crossing equation, and J tends to 1/(k+d). Matching exponentials yields the specified slope and negative logarithmic offset. The two objective limits and their difference follow from the same integral, and at d=0 the bracket is strictly negative for t>0. Independently integrated the split density and maximized the illustration in /workspace/checks/scalar_checks.py, obtaining 0.349542502738..., 0.397028630291... and 0.340658177084...; the uploaded program was inspected, not executed. These conclusions concern only nonadaptive deterministic releases in the stipulated irreversible independent-clock model.

## originality

PASS

The distinct claim is the all-positive-rates interior optimizer and its two horizon laws for one gated native source with irreversible competing arrivals. Neither a standard exponential-race identity nor the existence of habitat timing or priority-effect studies supplies this specific optimum and asymptotic balance.

## value

PASS

The minimal model isolates a natural tension: an opening delay protects the second site from invasion before propagule supply starts, but leaves less time after the source is ready. It gives a rigorous benchmark for a fixed schedule, with a quadratic delay at short horizons, a nontrivial fractional delay at long horizons, and a strictly positive limiting advantage over immediate opening. This is useful as a timing counterexample and baseline, not a field-effect or adaptive-management prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
