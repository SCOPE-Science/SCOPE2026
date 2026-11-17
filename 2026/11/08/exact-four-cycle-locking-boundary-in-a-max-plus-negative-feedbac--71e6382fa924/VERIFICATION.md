---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For the complete real plane, 3/2<t<2, the periodic-max argument bounds any period-dividing-four orbit in [-1,1]^2. If x-t>=y on an orbit, forced consecutive states contradict four-periodicity, so the scalar recurrence a_{k+2}=max(a_{k+1}+1-t,1-max(0,2a_k)) applies. The finite D,S,H branch partition gives 3^4=81 affine mode systems; all except DDDD are nonsingular and DDDD contradicts t>1. The inspected exact Fraction solver enumerates feasible words HHHH plus rotations HSDD and HSHD (nine words total); HHHH is fixed, the other two cycles are primitive. At 5/3 the cycles coalesce; below neither exists. Strict-branch Jacobian products equal zero and [[4,0],[4,0]], respectively. Independently evaluated exact rational cycles at t=5/3,7/4,19/10, including collision; finite samples are not the proof—the symbolic 81-branch elimination plus analytic global reduction is. No Floquet differentiability asserted on the switching boundary.

## originality

PASS

The 2023 Yamazaki–Ohmori primary paper gives the unnormalized finite-step max-plus negative-feedback map and numerical four-state phase locking, not an all-real-states exact primitive-period-four census or sharp border t=5/3 and the two return matrices. The separate rational negative-feedback limit map and infinite-step oscillator are different dynamics. Best-of-knowledge survival; 2015 Gibo–Ito precursor full text was not accessed.

## value

PASS

An exact global switching-border phase transition for a natural finite-step ultradiscrete oscillator resolves a numerical four-state locking observation, distinguishes an attracting cycle from an unstable one, and supplies a complete interval-wide primitive-four classification rather than a parameter sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
