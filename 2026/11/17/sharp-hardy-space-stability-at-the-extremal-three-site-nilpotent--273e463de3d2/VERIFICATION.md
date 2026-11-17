---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and mathematical checks

The claim is fully analytical. Set \(A=\sqrt2J_3\), expand \(f=a+bz+cz^2+\cdots\), form the displayed triangular matrix, and verify the Frobenius identity. Parseval and the unit-Schur constraint bound the tail. Schwarz–Pick applied to the first Schur transform yields the exact second-coefficient upper bound.

For asymptotic stability, the proof demonstrates that every sequence with \(\|f(A)\|\to2\) has \(a,b\to0\), \(|c|\to1\). With the coefficient of the quadratic term real and positive, form \(H=MM^*\) and expand its simple maximal eigenvalue at \(4|c|^2\); the first correction is \(2|a|^2+4|b|^2\). The exact Hilbert norm identity then yields the upper constant \(\sqrt2\).

For the lower bound, the explicitly stated degree-two Blaschke function has first Taylor terms \(0,-t,1-t^2\), exact Hardy norm one and distance squared \(2t^2\). Its top singular value squared is \(2[t^2+(1-t^2)^2+(1-t^2)\sqrt{1+t^4}]\). Direct matrix computations at \(t=0.1,0.01,0.001\) produced deficit divided by \(t^2\) of about \(0.995000125,0.999950000,0.999999500\); these are nonessential consistency checks. The proof uses the exact expression, not the computed samples.

Unproved limits: there is no optimal global all-deficit coefficient, no matrix-valued extension, no general higher-block theorem and no independent mathematical validation.
