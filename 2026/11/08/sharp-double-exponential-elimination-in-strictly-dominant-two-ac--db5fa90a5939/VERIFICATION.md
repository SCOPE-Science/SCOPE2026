---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

From the exact logarithmic fitness replicator, u=log((1-x)/x),v=log((1-y)/y) obey u_dot=alpha log(1+e^v)+alpha0 log(1+e^-v) and v_dot=beta log(1+e^u)+beta0 log(1+e^-u). Both derivatives have positive global minima and at-most-linear growth, so interior global solutions have u,v→+infty. For sufficiently large time, u_dot=alpha v+rA(v), v_dot=beta u+rB(u) with rA,rB positive bounded and →0. W=√beta u+√alpha v, Z=√beta u-√alpha v yield W_dot=√(alpha beta)W+F, Z_dot=-√(alpha beta)Z+G. Variation of constants gives finite L>0 and W-Le^(lambda t)→0, Z→0 (not merely little-o of e^lambda t), proving the stronger multiplicative asymptotics and ratio. Independent bounded log-odds ODE integrations agree; no finite integration proves t→infty.

## originality

PASS

Ruiz-Serra, Ay and Harré (2026) analyze the same log-evidence dynamics and prove qualitative inversion/elimination of dominant strategies, but their inspected accessible full HTML sections and appendix do not state the orbit-dependent sharp two-player physical-time rate or positive amplitude. The older Ay–Erb model introduces linear/log-linear replicators and its abstract mentions explicit solutions; full original text was not accessible through lawful sources, an explicit priority risk. The new asymptotic statement is strictly stronger than just elimination; different titles and failed search alone are not counted as novelty proof.

## value

PASS

The exponent √(alpha beta) is a quantitative boundary-growth invariant for a genuine four-parameter game family, and the positive trajectory-dependent amplitude with additive o(1) log-odds remainder controls actual probabilities multiplicatively. It separates singular log-evidence flow from ordinary exponential replicator extinction. This exact asymptotic can inform asymptotic numerical analysis and dynamics rather than just rebranding dominance inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
