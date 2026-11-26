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

For the periodic solution, write each demeaned output as η(A cos(ωt)+B sin(ωt)). Its orientation is the sign of the determinant A_q B_c−B_q A_c, with positive ∮Q dC counterclockwise; the integral is πη² times that determinant. Expanding by pathway pairs gives πη²ω N_c(ω²)/D(ω²), with D positive and deg N_c≤m−2. As an independent rigidity check, put s_j=−1/τ_j² and D_j=∏_{i≠j}(1−τ_i²/τ_j²). Then N_c(s_j)/(τ_j² D_j q_j)=Σ_{i≠j} q_i(c_j/q_j−c_i/q_i)/(τ_j+τ_i). If N_c is zero, evaluate at a maximal c_j/q_j: positivity of all coefficients forces every ratio equal. Thus rank is m−1, and c=q+εv stays positive for sufficiently small ε>0 for any numerator preimage v. Taking a polynomial with prescribed simple positive squared-frequency roots makes every designated root a reversal and exhausts them. Proportional weights give zero area at all frequencies; with m=2 a nonproportional pair has nonzero constant numerator and no reversal. Pairwise arithmetic gives the stated three-pathway coefficients (−3/4,21/2); on common denominator 3800 the four-pathway coefficients are (3800,−9500,3800). The result needs fixed common sinusoidal forcing, periodic steady state, and these affine linear response observables; it does not identify field pathways. Frozen checker.py lines 16–25 and 76–112 was read, not run; VERIFICATION.md records finite corroboration, not the arbitrary-m proof.

## originality

PASS

Best-of-knowledge pass for the joint arbitrary-m cap and positive fixed-q, fixed-τ realization theorem, not for the observation that hydrological mixing affects hysteresis or for interlacing of positive-residue rational sums. Available material on the closest distinct comparators concerns single-loop shape or hydrological timescales, not the number and programmable locations of frequency-indexed orientation reversals. The early hydrology full-text comparisons remain access-limited.

## value

PASS

Transforms a qualitative timescale effect into an exact expressivity bound for a natural common-input model, with a nontrivial positive-weight realizability converse for any prescribed admissible reversal pattern. For r observed orientation reversals the within-model minimum of r+2 pathways is informative, without promising pathway identification from storm data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
