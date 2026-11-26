---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The fixed line follows from w'=w+y, and substitution gives the exact lag-two recurrence for n≥2. In the interior box y1=O(s²), y2=O(s³), and subsequent y's contract by at most ab s²<1/2 while w<1. Thus their total is less than 2s for small s, closing the bootstrap. The logarithmic forcing remains bounded uniformly over the box. The positive Perron projection of (u2,u1,u0) grows at least as a constant times log(1/s), so it dominates the bounded discounted forcing and gives a positive rho-clock. At the endpoint, the prescribed Y sequence decays at least geometrically; d_n≤2Y_n for n≥2 makes the tail operator a self-map, increasing because d_n<sqrt(2). Its zero-tail iterates converge coordinatewise with dominated sums, and the fixed recurrence propagates strict positivity from y0,y1,y2. The initialization (5) exactly produces y1,y2, with x0 and 1−z0 asymptotic to s/(b sqrt(2)), and x_n<1 ensures positivity of z. The ratio bound gives d_n/y_n→1. In logarithms, subtract the constant log(ab sqrt(2))/3; the Perron part is its growing beta-mode plus a vanishing remainder (the future discounted forcing is bounded by a constant times the supremum of the remaining errors), while the stable convolution tends to zero because both other roots have modulus sqrt(2/beta)<1. The log-majorant gives L_*>0 by the same initial Perron-projection domination. Thus the multiplicative prefactor is correct. Independent exact rational root brackets and a bounded finite-tail replay corroborate the algebra and initial conditions but not the infinite existence or asymptotics. Replay: /workspace/branches/57043f8b-fa81-48d0-a5b5-21feb86759db/own_recurrence_check.py.

## originality

PASS

The map, the location of the fixed line, and the elementary interior clock mechanism through the parabolic subsystem are credited or directly recognizable. The realized positive boundary trajectories and the changed rate plus prefactor are the distinguishing claim.

## value

PASS

A proven positive trajectory reaching the vanishing memory factor only in the limit answers whether the modified asymptotic clock is realized, rather than merely suggested by formal substitution. The limiting memory feeds back as an extra factor of y_n and changes both the scale and the first prefactor, isolating an explicit boundary mechanism in an existing model. No full separatrix or hardware behavior is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
