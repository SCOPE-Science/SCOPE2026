---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Condition on the independent stiffness path, using the adapted integrating-factor form e^(-A_t) times the integral of e^(A_s) against the thermal Brownian motion. The conditional mean is bounded by |x0| and the variance by 2Dt. In a common unit-time Brownian coupling put H=t^(1+p/2). Almost surely the endpoint b(1) is nonzero: on the last fixed fraction of the unit path the backward rescaled integral admits an integrable exponential majorant, and the contribution from before that fraction is O(H exp(-cH)) for path-dependent c>0. The scaled conditional variance therefore tends to D/(kappa sigma^p |b(1)|^p); the fixed baseline term in the new integrand tends to zero and the scaled initial term vanishes. This establishes the joint mixture, and continuous multiplication establishes the independent self-normalized limit. The half-normal small-ball density and E|Z|^(2/p) give the stated constant; symmetry gives the Cauchy law at p=2. Bounded moment truncations prove divergence at and above the threshold without assuming convergence of unbounded moments. The packaged numerical checker was inspected, not executed; its samples are not evidence of uniform integrability or an infinite-time proof.

## originality

FAIL

A distinct published Resultary record, Brownian-powered stochastic traps have sharp heavy-tailed scaling laws (0700df2bd162), establishes the same principal theorem under a change of units. The remaining self-normalized display and divergence of renormalized moments follow immediately from the published joint convergence. This is a finding of verified equivalent coverage, not an assertion that the distinct record predates the frozen record or a claim about who proved the theorem first.

## value

PASS

As mathematics, the limit identifies the typical fluctuation scale in a nonstationary model where raw moments are influenced by rare small stiffness, and the independent self-normalization explains the source of the heavy tails. The endpoint concentration, not the textbook normal-ratio identity, is the substantive content. This assessment of scientific interest does not credit the frozen package with a separate contribution beyond the matched published theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
