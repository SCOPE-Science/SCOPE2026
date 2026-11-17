---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Solving coexistence conditions gives P=(1/2,1/2), prey nullcline slope -1 and continuous J=[[-1/2,-1/2],[1/2,-1/4]], trace -3/4 and det 3/8 with discriminant -15/16. Euler A_h=I+hJ has determinant 1-3h/4+3h²/8 and reaches unity at h=2. The complex pair lambda=(1+i sqrt15)/4 crosses outwards with d|lambda|/dh=3/8 and avoids resonances orders 1-4. In local centered coordinates the quadratic tensor B is explicit; choosing q=(1,-lambda), the dual ell and H11=(I-A)^-1 B(q,qbar), H20=(lambda²I-A)^-1 B(q,q) gives c=23/6-25i sqrt15/18 and d=Re(lambda_bar c)=-17/4 (all independently verified symbolically). The local Neimark--Sacker theorem then yields an attracting small invariant circle for h>2 close and a repelling fixed point, with radial scale 3(h-2)/34. This asserts a local bifurcation, not global orbit behavior.

## originality

PASS

The initiating Chan-Lopez--Martin-Ruiz--Castellanos 2026 theorem provides the general Euler spectral identity and geometric location of unit-circle crossings, but does not give this self-limited quadratic system exact nonlinear Lyapunov coefficient, supercritical stability or radius. Khan studies other discrete predator-prey recurrences. The nonlinear realization survives the direct implication comparison; it is not credited as a first discovery of Euler-induced spectral crossings.

## value

PASS

An exact negative Lyapunov coefficient is the substantive boundary between a mere spectral crossing and a verified attracting oscillatory state. The simple quadratic predator-self-limited flow offers a transparent counterpoint to continuous-flow Hopf-nullcline localization and an analytically quantified discretization artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
