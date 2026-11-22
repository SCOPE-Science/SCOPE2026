---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For fixed 0<a<b,d>0, z-y=d and lambda=b-a, the exact change V=by/(ax),W=bd/(lambda x),d tau/dt=x gives classical LV equations V_tau=lambda V(1-W),W_tau=aW(V-1), and physical dt/dtau=(lambda/(bd))W. H=a f(V)+lambda f(W) has compact regular positive levels. Each inverse branch V=v_±(q_h(W)) supplies original-time density B_h(W)=1/(1-v_-)+1/(v_+-1). Near branch endpoints B-1=O(q^-1/2), in the bulk its excess is O(1/q)+exponentially small. The w-variable change has controlled Jacobian outside [1/2,2] and bounded middle error, proving I_h=h/lambda+O(log h) and T(h)=h/(abd)+O(log h). Thus lambda W/h approaches U(0,1) in total variation at O(log h/h); its reciprocal hX/(bd)=1/U approaches Pareto(1,1) in TV with same bound. The high-V branch has O(log h/h) physical mass and typical low-V branch V→0, so state→(0,0,d) in probability; integrating periodic log derivatives proves positive exact means bd/lambda,ad/lambda,bd/lambda. Independent check: Performed independent symbolic differentiation of V and W from the displayed mass-action system: both transformed derivative differences simplify identically to zero. Rechecked the endpoint inverse f(s)=s-1-log s derivative bounds, rescaled interval length, and exact normalization w*/(a lambda)=1/(abd). Prior finite-energy quadrature in source verification is supplemental only.

## originality

PASS

Best-of-knowledge: examined primary source evidence, actual same-object implications, and published mathematical findings. Earlier constructions, generic formulas and independent source results are credited; the surviving quantitatively specified theorem is not implied by the directly inspected antecedents. No certification of absolute historical priority is asserted.

## value

PASS

A physical-time chemical concentration converging to an explicit heavy-tailed Pareto law in total variation despite typical collapse to a boundary equilibrium is a substantive invariant-measure phenomenon. The exact nonzero means clarify rare-excursion lack of uniform integrability, and the error rate makes the result quantitatively usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
