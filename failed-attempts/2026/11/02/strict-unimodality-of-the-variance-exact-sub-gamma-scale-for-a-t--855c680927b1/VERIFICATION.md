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

The normalized cumulant remainder is M=F/(32t²), with F>32t². On 0<t<1/c, feasibility is equivalent to c≥Ψ(t); beyond that interval Ψ(t)<1/t≤c, so the unrestricted supremum is the correct sharp scale and is independent of λ. The derivative is N/(t²F²). Independent exact arithmetic confirmed the degree 4–11 normalized coefficients (0,0,99520,882112,-4769408,-240640896,-4342095552,-59940771264). Retaining the pure powers of 5 in the binomial convolution gives T_n≤−5^n Q_n for n≥12. The stated recurrence and Q_12=25718/25 imply positivity for all n≥12. Consequently N/t^7 has a positive reciprocal term, a constant, and strictly negative positive-power terms; it decreases with strictly negative derivative from +infinity to −infinity. Its zero is simple, giving the strict peak and c_*>41/48, the latter number being f_3/32. Independent exact-rational endpoint evaluation confirmed the interval: take degree-80 lower exponential sums, upper bounds obtained by adding the first omitted term divided by 1−z/82, and propagate through 32t³F′−32t²F−F² using F′ lower/F upper for the lower bound and the reverse for the upper bound. The lower bound at 473723111/10^9 is positive (about 1.13×10^−8) and the upper bound at 473723113/10^9 negative (about −2.62×10^−8).

## originality

FAIL

The October 18 Resultary theorem 33a2f59ff992 already proves strict global unimodality, uniqueness and negative second derivative at the optimizer for the same objective over a probability range containing 1/40; it explicitly gives the same numerical maximizer and scale at 1/40. The fixed-law proof also specializes the earlier coefficient method, since N=−1024t^4 H_q at q=1/40 for the earlier derivative numerator H_q=M_q(M_q−1)−tM_q′. The exact rational endpoints are not in the inspected prior finding, but certify a narrow numerical bracket about an already proved and located maximizer, not the claimed uniqueness gap.

## value

FAIL

Certifying uniqueness and nondegeneracy for a motivated example would resolve a useful question if unknown, but those facts and the location are already available from a broader theorem using the same derivative structure. The narrow rational bracket is correct; standard finite Taylor-tail arithmetic at two selected endpoints gives no new threshold, decision or consequence tied to these endpoints. No separately motivated valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
