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

An arbitrary nonnegative initial x is absorbed after one iterate into K=∏[α_i/D_i,U_i], where U_i>=max(x_i(0),α_i/(1-β_i)) and D_i=1+Σ c_ij U_j^h. Log transformation G_i(z)=log F_i(e^z) gives absolute Jacobian row sum <=(β_i x_i+α_i hS_i/(1+S_i)^2)/F_i=1-α_i[1+(1-h)S_i]/[(1+S_i)^2F_i] <=1-δ_i, δ_i=α_i/[D_i²(β_i U_i+α_i)]>0 for 0<h<=1. Banach contraction on complete log K establishes unique fixed point and geometric convergence from time 1, and any other fixed point must lie in K. For h>1, scalar f(x)=α/(1+x^h) with α>h/(h-1)^(1+1/h) has an equilibrium t with f'(t)<-1; IVT on f²(x)-x yields a prime-two orbit. For h=2, symmetric dimer r±=(a±sqrt(a²-4))/2, a>2, has 2-step eigenvalues 4/a² and 4(1-2ε)²/a²<1 for 0<=ε<=1; IFT extends small positive β. Independent recomputation of Jacobian deficit and several exact diagonal cycles corroborated algebra. These sample checks do not prove the all-network theorem, which is analytical.

## originality

PASS

Best-of-knowledge comparison of the exact mathematical statement/implications with named primary sources and published research; no independently earlier equivalent or dominating theorem found among inspected material. Same-day matching Resultary entries were excluded as independent prior evidence. Specific inaccessible texts and older alias risks are retained; negative searches are not treated as proof of uniqueness.

## value

PASS

A uniform network-size/topology independent global-attraction threshold at the natural Hill exponent h=1, with an explicit rate and a sharp existence counterexample for every h>1, is a structurally meaningful boundary between unconditional monotonic relaxation and possible oscillation for inhibitory networks. It is not a mere contraction-mapping exercise because the logarithmic Jacobian row estimate and coupling-uniform sharpness are the substantive elements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
