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

Reassessed the complete replacement repairs/4/RESULT.md. The displayed limits survive unchanged. The original incorrectly called s_alpha-1 a fraction of the extinction time: it is the coefficient in units of n, and division by T_(m,n)/n gives the actual limit (s_alpha-1)/s_alpha above threshold. The replacement also uses monotonic comparison rather than invoking a law of large numbers at exactly s=1/2. Independent reconstruction: disjoint site clocks and the strong Markov property give n-1 independent rate-two holding times and one rate-one hold, independent across blocks. Conditioning on the gamma stage and tilting its density by e^g produces the reported exact Poisson-tail expression (and the rate-two/rate-one normalization). Minimizing the joint rate reduces to j(g)+(s-g)_+; derivatives 1-1/g below s and 2-1/g above s yield the unique split including (1,0) at s=1. The open and closed tail half-spaces have the same infimum, so the probability exponent is exact. Independence gives the maximum threshold; strict uniqueness and compact sublevel sets give a rate gap for every split away from the minimizer with total time near the threshold. The gap survives multiplication by m=exp[(alpha+o(1))n], controlling the actual selected last domain. As an additional check, given T_j=t the preterminal time has density proportional to g^(n-2)e^-g on 0<g<t (a rate-one gamma truncated at t), consistent with concentration at min(1,t/n) in units of n. Inverse differentiation at s=1 gives left second derivative -1 and right 0, and the independent Poisson gap coupling yields the stated discrete-sweep extinction-time limit. The frozen script and its finite checks were inspected, not executed; supporting files need no change.

## originality

PASS

The repaired finding takes no credit for the kinetics, the finite-domain rate structure, a product CDF for arbitrary deterministic run lengths, or general large-deviation methods. It supplies the critical change of the dominant rare-event mechanism when many equal deterministic domains simultaneously grow, with a joint limit for the last domain. The closest indexed same-sector result randomizes the lengths and controls a different extreme-value regime. The frozen reference to an unnamed earlier exact CDF and fastest/slowest law was not traceable to a source in the scope examined and was replaced by a derivation and comparisons to identifiable sources, not by a denial that such work exists.

## value

PASS

Equally spaced permanent seeds define a motivated competition between run length and number of independent runs. The exact threshold and the joint law in the last domain distinguish collective erosion from a single macroscopic last-spin delay, a mechanism that cannot be inferred from the typical block's speed or an average absorption time. The result remains first order and conditional on the stated irreversible dynamics; the correction makes the mechanical interpretation numerically accurate without overstating its scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
