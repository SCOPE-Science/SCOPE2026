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

Forward projection of t+tau retains its fractional part when it is in the closed window and otherwise sends it to the next integer. Until the first reset the motion is exactly rotation. Every irrational orbit hits the open hole by minimality, uniformly in the initial phase by a finite subcover of inverse images of the hole. For rational p/q, rotation traverses q grid points in each coset modulo 1/q, so every phase hits a hole longer than 1/q. In both finite-hit regimes the zero cycle visits r distinct phases before its unique reset, and a lift from zero takes elapsed time mr+ceil(r beta) over that period, not r tau. The invariant probability is uniform on the cycle since every phase enters it in bounded time. In the rational remaining regime write eta=(q-1)/q+h, with 0<=h<1/q. The safe grid cosets are exactly those with residue in [0,h] modulo 1/q, giving q closed intervals of length h (q singleton endpoints if h=0). Other phases reach zero within q steps; this proves the claimed survivor and projecting masses, the invariant-probability alternatives and the exact undelayed period mq+p. For irrational beta, if rho_i are the successive strict upper records at times r_i, then r=r_i throughout [rho_(i-1),rho_i), with the initial interval starting at zero. The average extra delay (1-rho_i)/r_i strictly decreases along i, establishing positive jumps exactly at the records. The positive discrepancy is d/[r tau(tau+d/r)], where d=1-rho_i<1-eta, and d>=c/r under the stated Diophantine condition. These give the two error bounds and the endpoint limit. Replay: RESULT.md lines 49–63 and the rational coset description above. The supplied finite verification script was read but not executed; its irrational cases check first hits and resets, not an independent staircase or jump-size computation.

## originality

PASS

The supported contribution is the exact capture and physical-time rate classification of the single-interval periodic observation clock, including the width staircase and strict record-jump rule. The projection law and the underlying geometry/minimality of rotations are not new. The strongest inspected neighbouring clock results use finite phase sets or aperiodic clocks, not this closed continuum window with its width-dependent rotation hole.

## value

PASS

The classification answers an identified gap between a lattice firing formula and a periodic clock with continuous availability within windows. The boundary distinction between a unique rational survivor cycle and a continuum, and the exact plateau heights in physical rather than iteration time, are useful quantitative information about that model. The value does not depend on novelty of irrational minimality or any claimed physiological application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
