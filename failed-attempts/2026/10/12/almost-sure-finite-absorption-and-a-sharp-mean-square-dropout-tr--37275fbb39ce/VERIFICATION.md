---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The update maps are failure (x,e)->(x,x+e) and success (x,e)->(-e,0). Two consecutive successes annihilate the state and occur almost surely. Conditioning on first success gives a_k=q^k+sum_{t=2}^k p q^(t-1)(t-1)^2 a_(k-t); hence A(z)=(1-qz)^2/((1-qz)^3-pqz^2(1+qz)). The positive aperiodic kernel has a unique smallest simple positive root giving the growth rate. W_p(1)=q(2-p)/p^2 crosses one at p=2/3; at criticality the GF pole residue is 2/5. Independent exact Bernoulli trace enumeration verified finite moments. Source theorem correct only for scalar unit step, zero memory, independent on/off compressors.

## originality

FAIL

Failed originality: previously published 2026-10-04 exact same scalar Bernoulli error-feedback recurrence establishes sharp mean-square stability iff 0<s<2p/(2-p), with the explicit two-state success/failure matrices, full moment operator and geometric-waiting-time multiplier E[(1-Js)^2]. Setting s=1 yields exactly the p=2/3 frontier. Two-success finite absorption is immediate from the printed s=1 matrices, and critical 2/5 limit is routine eigenprojection/partial fractions of that known second-moment operator. The conjunction is a straightforward refinement of the established complete boundary, not independent new core mathematics.

## value

FAIL

Failed independent value despite correctness: the main mean-square transition is an exact corollary of the earlier same-model sharp step-size theorem, while the two-consecutive-success absorption and critical constant follow by short elementary matrix and rational generating-function calculations; the already known boundary dominates the proposed gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
