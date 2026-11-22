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

For h>0, 0<w<4, the actual degree-nine source field in RESULT.md shears under z=y+w(x^2-h)x/(2h) to xdot=z+w(h-x^2)x/(2h), zdot=-x+w(h-2x^2-z^2)z/(2h). Thus q=(x^2+z^2)/h satisfies qdot=wq(1-q), giving global forward completeness for q0>0. The directional ratio u=z/x satisfies u_dot=-1-(w/2)q u-u^2, the Riccati equation for psi_ddot+(w/2)q(t)psi_dot+psi=0. The q-equation is Fuchsian, and the explicit q^(i/w)|1-q|^(1/4+i*sqrt(1-w^2/16)/w) hypergeometric F and conjugate solve it with nonzero Wronskian: near q=1 the time Wronskian is 2iΩ|1-q|^(1/2)(1+o(1)), and Abel propagates nonzero throughout each interval. Projective normalization uniquely recovers the physical (x,z) for both q<1 and q>1, including x=0 crossings. The stated coefficient A from (F,G) and Abar gives phase arg[A(|1-q|/q)^(iΩ/w)]; logistic c(t)=c0e^(-wt) proves exact phase drift -Ωt. The limit as q→1 agrees with the explicit circular phase arg[x+i(z+wx/4)/Ω] and O(e^(-wt)) phase-aligned convergence, showing whole punctured-plane isochrons. No assertion at origin, w=0, or w>=4. Fresh independent numerical integration of reduced original-time ODE and logistic radius corroborated to ~5e-12 across three w and nine starts; the actual source CHECK.py was inspected, not trusted as proof. The all-data conclusion follows from the analytic reconstruction, not bounded numerical tests.

## originality

PASS

Best-of-knowledge original extension from the source oscillator’s known algebraic attracting oval and on-cycle time law to an explicit Gauss basis and asymptotic phase for every nonzero off-cycle initial condition. No inspected prior theorem for the same vector field determines this full-basin phase, and a global phase of a different oscillator does not imply it. Classical Riccati/hypergeometric methods are credited.

## value

PASS

The exact whole-basin isochron coordinate of an explicit nontrivial algebraic polynomial oscillator is a natural dynamic invariant, distinct from its already tabulated attracting cycle and Floquet data. It supplies explicit transient positions, asymptotic phase comparison and global synchronization coordinates in original physical time, a reusable motivated structural result; it is not a mere relabeling of on-cycle phase or an unmotivated finite coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
