---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For ka=3 the full 2x2 Cournot Jacobian, differentiated before diagonal restriction, has eigendirections (1,1),(1,-1) with transverse eigenvalue 4(1-2eta u), eta=(2+c)/(2+c+d), where diagonal u follows u->4u(1-u). The arcsine invariant law is ergodic via circle-doubling conjugacy; the logarithm is integrable despite at most one zero. Jensen cosine integral yields lambda=log(2eta) for eta>=1/2 and lambda=log(2(1-eta+sqrt(1-2eta))) otherwise, including the singular neutral boundary eta=1/2. For d∈[0,1], s=2+c>2 implies eta>s/(s+1)>2/3, yielding strict lambda>log(4/3), approached at c->0,d=1. For d=s exactly the two coordinates acquire the same multiplicative factor, conserving x/y; expansion d->s± gives linear/square-root one-sided cusps. Almost-everywhere statement is with respect to the natural invariant diagonal logistic measure, not all trajectories.

## originality

PASS

Askar–Alshamrani (2024) define the same cost-adjusted symmetric Cournot map, logistic diagonal and transverse exponent criterion, while Bischi–Stefanini–Gardini (1998) note transverse instability at a specific ratio. These are credited. The sharp all-physical-parameter lower bound log(4/3), full analytic continuation formula and exceptional neutral-coupling cusp are not presented in the inspected source sections. Although Jensen is classical and the calculation is short, it answers a specific, nontrivial stability question with a sharp universal constant.

## value

PASS

A sharp positive transverse Lyapunov gap uniformly forbids robust chaotic synchronization in the physical substitute-products domain; the exact exceptional extension d=s conserves output ratio and has different left/right exponents with square-root singularity. These directly sharpen parameter stability margins and identify a singular boundary not resolved by a numerical transverse criterion, despite classical Jensen machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
