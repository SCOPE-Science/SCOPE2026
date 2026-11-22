---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Exponential normalization yields uniform simplex volume and independent Laplace contrasts; the Monge chamber is one of q! equally likely strict orders, recovering the known volume. Conditioning on a coordinate-zero simplex face changes the selected contrast CDF to uniform (0,1/2) or (1/2,1), giving exact incomplete beta/binomial tails and correct intrinsic simplex face-height h_q. For a comparison slack g_i the intrinsic gradient has length 2; one-sided coarea applied before exponential normalization yields A(W_i)/V=2q E[f(Z_(i))(q+sum_{j=1}^{q-1}|Zj|+|Z_(i)|)], with S conditional mean q+sum|D|. Summing over sorted Laplace Z and using E f(Z)=1/4, E|Z|f(Z)=1/8 and E|Z|=1 gives exact q(q-1)(2q-1)/2. Order-statistic quantile convergence gives f(Z_(i))→min(u,1-u) and resulting triangular factor 4; binomial CLT gives the centered Gaussian coordinate profile. Independently checked exact coordinate complementarity and aggregate coarea sum for every q=2..100, independent of repository code. The published volume is not reclassified as a novel fact.

## originality

PASS

Best-of-knowledge PASS after inspecting the frozen proof, searching mathematical aliases/general implications, comparing related primary theorems and published results at statement-level. The contribution is the specific final claim, not its openly credited combinatorial, signal-processing or probabilistic prerequisites. Inaccessible or less-indexed literature remains explicitly a residual risk.

## value

PASS

Determines the full first Steiner/surface coefficient and its decomposition into inequivalent natural facet families, exposing a nontrivial two-scale boundary measure with exponential individual variation, triangular bulk wall profile and Gaussian transition. The exact invariant of a canonical Monge optimization polytope is naturally useful without any larger theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
