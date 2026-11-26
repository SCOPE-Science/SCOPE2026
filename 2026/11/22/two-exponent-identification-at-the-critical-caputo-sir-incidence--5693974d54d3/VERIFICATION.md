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

For the positive-rate constant-parameter Caputo model with R(0)=0, write S and I as local Volterra integral equations. The continuous solution differs from its initial data by O(t^alpha). Polynomial substitution and I^alpha t^(k alpha)=[Gamma(1+k alpha)/Gamma(1+(k+1)alpha)]t^((k+1)alpha) inductively give every finite expansion: a bounded O(t^q) error integrates to O(t^(q+alpha)). This includes the ordinary-order endpoint. In the normalized basis s1=-x0 and i1=x0-gamma B; the leading incidence coefficient is x0[c(A-B)-gamma], with c=beta/N, A=S(0), B=I(0), x0=cAB. At cancellation gamma=c(A-B)>0, i1=cB^2, s2=0 and i2=-gamma i1. Multiplying the two expansions gives x2=-c i1(gamma A+H2 x0) and x3=c gamma i1 x0(H3-H2): the A gamma^2 i1 terms cancel. Strict midpoint log-convexity of Gamma proves H3/H2>1 for all alpha>0. When both candidates are generic, or both critical, the first nonzero exponent alone fixes their common order. In the mixed pairing equality would force generic order 2alpha (only feasible for alpha<=1/2); after the common first term the generic remainder is O(t^(4alpha)), incompatible with the nonzero t^(3alpha) term. This covers alpha=1/2 versus ordinary SIR and the critical order-one case. Independently expanded the raw-power Volterra products symbolically, including the positive exact t^(3/2) coefficient (12*pi-32)/(3*pi^(3/2)) in the frozen example; replay python3 -B /workspace/branches/independent_replay.py 4. This does not test fitting or stability. Frozen check.py and recorded output were inspected, not executed.

## originality

PASS

Pass only the critical-case calculation and exclusion of a different order across the generic/critical comparison as the distinct increment. The same model, first incidence coefficient, cancellation condition, leading-exponent technique and generic inference are already present in prior work. The inspected primary result does not resolve the missing third-power comparison at cancellation.

## value

PASS

The critical surface is forced by a physically admissible cancellation in the observable, and is an explicit exception to a published leading-order criterion. The nonzero next coefficient resolves a real ambiguity in the leading exponent, including apparent ordinary-time behavior at order 1/2, and completes the exact-data identification in the stated class. It is not claimed to recover the other parameters, handle time-varying rates or give a stable statistical method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
