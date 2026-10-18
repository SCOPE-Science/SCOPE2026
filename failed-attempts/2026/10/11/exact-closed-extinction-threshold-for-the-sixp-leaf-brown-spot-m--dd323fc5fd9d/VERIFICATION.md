---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For positive κ,π,δ,μ,Rx,Rc,σ,ε,i, admissible nonnegative S+I>0, Ydot≥κ−CY gives uniform positivity; Ndot=κ−μN−I/i bounds S,I,P, and X is bounded via Xdot. Differentiating V=I+(Rx/ε)X yields exact Vdot=−(RxX+RcI) I/(S+I)−c(1−R0)I, checked term by term against frozen verify.py and independent substitution. For R0<=1, LaSalle on eventually compact interior closure forces I=X=0 and Hurwitz S,P relaxes to E0; at equality, direct V control and Hurwitz forcing establish Lyapunov stability. For R0>1 infected matrix determinant εc(1−R0)<0 yields a positive eigenvalue. This is a valid full critical sharpness proof, not a simulation.

## originality

FAIL

Primary 2023 SAME-SYSTEM paper Theorem2.2 and pp9607–9608 proof explicitly assert critical R0=1 global attraction and subcritical global attraction, and Theorem2.1 treats the reproduction-number bifurcation. Although those published derivations contain inconsistent R0>1 wording and an invalid transient equilibrium substitution, the final threshold implication is already asserted; the newly correct proof alone cannot make the same final mathematical statement original.

## value

PASS

A complete correct proof of a practically motivated four-state epidemiological global threshold, repairing a published invalid Lyapunov computation and handling the nonhyperbolic equality case, is scientifically instructive and useful, even though the final statement is already in the literature. Value does not override O failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
