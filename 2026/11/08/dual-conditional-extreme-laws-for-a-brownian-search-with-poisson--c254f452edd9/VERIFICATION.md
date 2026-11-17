---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The REPAIRED final theorem is the singular low-rate Bernoulli crossover, NOT the earlier full set of conditional Gumbel/geometric claims. With z=kappa a and L=kappa m->u>0, killed-interval first-exit probabilities are A=sinh(L-z)/sinh L, B=sinh z/sinh L; half-line absorption-without-reset p=e^-z. Exact renewal gives P(M>m)=B/(A+B), P(N=0,M>m)=p-A. Expanding yields A=1-z coth u+o(z), B=z csch u+o(z), p=1-z+o(z), and hence conditional zero-reset e^-u; P(N>=2|M>m)<=q²/P(M>m)=O(z), so the remaining mass tends to one reset. At fixed r>0 p-A=O(e^-2L), tail is Theta(e^-L), proving noncommuting limits. Independent numerical substitution with u=2, r from 1 to 1e-4 confirms convergence but analytic bound proves the result. All changed scientific file bytes supplied and hashes verified.

## originality

PASS

The original joint p_m q_m^n renewal law, count-conditioned Gumbel, and high-maximum size-biased geometric mechanism are covered by the published Oct 25 Erlang-clocks theorem and its stated one-exponential-stage specialization: the original broad novelty claim cannot survive unchanged. The final revised theorem retains only a distinct two-parameter singular regime r downarrow0 and kappa*m->u, with a Bernoulli zero/one reset law and exact e^-u zero-reset mass. The predecessor fixes reset parameters before taking high m and does not analyze this noncommuting joint scaling. This is a genuinely narrower corrected claim, not a disclaimer attached to the covered original.

## value

PASS

Spatial maximum and number of completed resets measure excursion exposure and resource cost in a natural first-passage search. The limiting positive probability of zero resets at an extremely high threshold contrasts sharply with the known fixed-rate conditional law assigning zero no-reset mass. Explicit u-dependent Bernoulli weights mark a meaningful singular boundary not mechanically described by the earlier fixed-rate conditional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
