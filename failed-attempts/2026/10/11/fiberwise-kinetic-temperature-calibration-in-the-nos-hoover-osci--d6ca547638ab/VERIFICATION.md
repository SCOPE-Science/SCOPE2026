---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The assigned normalized Nosé–Hoover vector field is xdot=-y-xz, ydot=x, zdot=alpha(x^2-1), alpha>0. For compactly supported invariant mu, invariance gives E[LH(y)]=0 and E[LK(z)]=0 for every one-variable C1 antiderivative: L H(y)=H′(y)x and L K(z)=alpha K′(z)(x^2-1). Continuous test functions on the compact coordinate ranges determine conditional expectations, proving E[x|y]=0 and E[x^2|z]=1, including all bounded Borel tests by measure uniqueness/monotone class. Mean x^2=1 then gives Var(x^2)=E[(x^2-1)^2]=alpha^-2 E[zdot^2]. If this variance vanished, support invariance and continuity force x=+1 or -1 along every support orbit, hence ydot=x forces unbounded y, contradicting compactness. Strict variance with mean 1 yields positive mass in x^2<1 and x^2>1. Every nonempty compact invariant set carries an invariant measure by time averaging, so it intersects both regions. No ergodicity or numerical trajectory exhaustion is assumed.

## originality

FAIL

Published October 4, 2026 Sprott A/Nosé–Hoover theorem covers the central October 11 fiberwise law and kinetic-nullcline crossing for the exact same positive-parameter family. Set U=sqrt(alpha)*y, V=sqrt(alpha)*x, W=z, a=alpha. Then (Udot,Vdot,Wdot)=(V,-U-VW,V^2-a) identically, with no time rescaling. Under the pushforward of ANY compact invariant measure, E[V^2|W]=a transfers to E[x^2|z]=1. The earlier theorem states strictly positive mass on |V|<sqrt(a) and |V|>sqrt(a), which is precisely the assigned |x|<1/>1 law. Every nonempty compact invariant K supports an invariant probability, giving the assigned set crossing. Its strict crossing proof is the same constant-nonzero-momentum/unbounded-position argument. Additional E[x|y]=0 follows immediately from the same standard generator antiderivative test for coordinate y; the variance formula is the squared equation zdot=alpha(x^2-1) combined with E[x^2]=1. Neither residue yields an original substantive theorem.

## value

FAIL

The Nosé–Hoover thermostat and its conditional kinetic-temperature calibration are natural objects and invariants. Nevertheless, the earlier October 4 result establishes exactly the fiberwise identity and the |x|=1 two-sided crossing for every positive-parameter invariant probability, and even supplies new radial-shell balance and covariance information. The assigned strict speed defect is a rewriting of zdot=alpha(x^2-1), while E[x|y]=0 is the universal one-coordinate stationary transport identity, verified by the same antiderivative trick. The compact-set corollary is standard existence of invariant measures on nonempty compact invariant sets. There is no new parameter regime, independent structural classification, sharper bound, or substantive nonlinear phenomenon beyond the stronger published theorem. Correctness and a physical interpretation do not independently make this covered restatement scientifically valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
