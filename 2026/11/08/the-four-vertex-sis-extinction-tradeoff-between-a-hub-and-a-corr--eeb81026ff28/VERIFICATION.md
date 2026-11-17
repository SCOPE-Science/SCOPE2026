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

Constructed full 16-state continuous-time SIS generators independently from infected->healthy rate1 and infected-neighbor->healthy transmission rate lambda. For k=1..4 direct symbolic inversions of the 15x15 transient generators reproduced all four exact rational mean-gap polynomials N1,N2,N3=N4 with strictly positive coefficients for every lambda>0; independently evaluated Taylor powers at lambda=1 for first nonzero t^(3,4,5,6) coefficients -1/12,+1/72,-1/120,-1/180 and checked exact means at lambda 1/2,1,2. Source symbolic verifier supplies the general lambda^2 Taylor identities, with actual formula inspected. Positive tail integral plus negative initial difference for k1,3,4 guarantees a later positive difference and at least one crossing, but not exactly one.

## originality

PASS

The full-occupancy and uniform-triple mean comparisons are already known, but the exact short-time survival signs, forced later crossing, and k=1,2 mean equations give a substantive surviving claim, not implied by the published full-occupancy mean theorem.

## value

PASS

The first nonisomorphic equal-edge trees are a natural exact finite contact-process benchmark. A rigorous all-rate mean-survival ranking can oppose finite-deadline probability rankings, with a nontrivial dependence on initial infected count; these precise short-time signs matter for interpreting extinction risk rather than merely repeating a known mean formula. Substantive time-domain structure remains after crediting earlier full-occupancy means.

The dated certificate retains the supplied scientific assessment, sources and limitations.
