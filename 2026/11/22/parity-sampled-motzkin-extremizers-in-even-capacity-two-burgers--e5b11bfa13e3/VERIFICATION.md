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

The frozen pointwise assertion that complement alone preserves entry time is false: at n=6, x=(0,0,2,0,2,1) is still outside the free language after one update, at (1,0,0,2,1,1), and has tau=2; its complement starts outside the congested language but enters it in one update, at (2,0,2,0,2,1). The replacement RESULT.md uses the correct involution A(x)_i=2-x_(-i); J_i(Ax)=J_(-i-1)(x) makes it commute with the update. Thus equal sector counts and the central theorem survive. Independently, the height recurrence takes sliding parity maxima. At n/2-1 these windows have one full parity class, and the drift gives the monotone inequalities for invariant rigid-shift recurrence; conversely any periodic state must belong to the invariant union eventually reached. At the penultimate time an increasing window at mass n-1 is exactly the height-gap-two exception. A marked exception strictly exceeds all of its next n-1 heights; integer heights and drift -1 preclude a second such exception. The first and last pair restrictions give the rooted count 2(K^L)_00+(K^L)_01, including L=0. The single between-pair boundary correction gives K=T²+e_0 e_0^T; the resolvent and the odd Motzkin recurrence reduce its count series to 2O. This proves the two populations and sharpness; the excursion asymptotic and span-one local limit of variance 2/3 give the stated probabilities.

## originality

PASS

The corrected statement credits the existing map and traffic phases; the distinct part is the exact even-ring, capacity-two, near-critical last-entry census and limit. The accessible same-map and closest census statements do not give it. The symmetry correction concerns correctness and does not expand the novelty claim.

## value

PASS

The two closest noncritical conserved masses are dynamically natural, not an arbitrary sample. Their sharp entry-time populations and positive limiting fraction distinguish how often slow relaxation persists, and the parity-sampled walk with a rank-one correction explains why those populations are Motzkin numbers rather than just tabulating them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
