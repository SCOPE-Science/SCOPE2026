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

Invertible affine coordinates z=(1−s)x and q=((1−s)(y+sx)−s)/(2−s) produce exact skew map q′=sq, z′=1−2|z|+(2−s)q. Moving escape bounds I_n=[−1−q s^n,1+q s^n] separate unbounded trajectories. For q∈[−1,0] bands map inside themselves; q<−1 has an explicit divergent super-solution. For q>0 each branch maps its half-band onto I_{n+1}; 2^N disjoint inverse cylinders each of length 2^{1−N}(1+q s^N), with stage-j gaps count 2^j length 2(1−s)q(s/2)^j. Thus positive measure 2, perfect nowhere dense, geometric exit law, and by affine Jacobian and Fubini infinite 2D bounded area. Independently verified rational pullback-survival length/gap formulas at three (s,q) pairs; the unrestricted proof is algebraic.

## originality

PASS

The 2024 original border-collision normal-form Proposition 10.1 treats the single invariant line (q=0), whereas this theorem classifies all initial-condition fibers q∈R, gives positive-measure Cantor sets and exact escape-time laws. The trapping/attractor literature does not imply the all-fiber moving-band census.

## value

PASS

The exact global geometry of bounded forward orbits in a noninvertible two-saddle border collision is a natural dynamical question. Positive-measure nowhere-dense Cantor sets on every positive transverse section, a parameter-independent length and geometric escape distribution provide a distinctive nontrivial complete classification beyond an invariant-line tent-map observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
