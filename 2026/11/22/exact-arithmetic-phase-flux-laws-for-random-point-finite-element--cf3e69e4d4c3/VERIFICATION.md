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

The nodal flux balance and telescoping endpoint increments give reciprocal flux equal to the average sampled resistivity. With at most one jump per open cell this differs from the physical resistance by S_n/n, a sum of centered independent Bernoulli terms, with aligned jumps deterministic. The resistivities are uniformly bounded above and away from zero; strict Jensen gives exactly the variance-zero equality case, and the uniform reciprocal expansion gives the displayed bias and risk. Exact stiffness integration instead reciprocates each arithmetic cell average of conductivity, so the resistance defect is nonnegative and yields the reported deterministic error. Under the stated joint rational independence, the phase orbit has the full torus as its limit set and is Weyl equidistributed. The centered Bernoulli laws vary continuously, with matching laws at phases 0 and 1; bounded reciprocal linearization then gives precisely the listed subsequential laws and the Cesàro mixture. Integrating each phase produces density 1-|z| on [-1,1], variance 1/6 and the squared sinc characteristic function. An independent exact two-jump example at n=4 gives T=7/12, q=12/7, V=5/72, positive randomized bias 664/31185 and exact-integration flux 160/89. The uploaded verifier was inspected, not executed.

## originality

PASS

The supported distinction is the exact physical-flux law and its mesh-phase and averaged distributional consequences in this one-dimensional layered model, not randomized quadrature assembly, torus equidistribution, or the general Bernoulli representation of a one-cell indicator. The nearest inspected results share ingredients but do not establish that combination.

## value

PASS

A natural interface discretization admits a sharp comparison that norm bounds do not capture: the random physical flux has second-order mean bias but generically first-order fluctuations, whereas exact ordinary P1 assembly has a first-order flux defect. The same model shows how one can have no marginal weak limit yet have a fully explicit averaged law and mean-square constant. These are useful quantitative diagnostics for this discretization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
