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

The three-state Markov coding A=(0,1/2), B=(1/2,2/3), C=(2/3,1) has marked transitions A→A,B,C; B→C; C→A,B. Its matrix M(z) has characteristic polynomial t(t²−t−2z). The exact trace polynomial has coefficients m/(m−j)*binom(m−j,j)*2^j. Subtract the all-A fixed point and the two alternating B/C boundary encodings at even m (one fixed point 2/3 counted twice). The remaining weighted point counts are E_{m,j}; Möbius inversion by repeated orbit counts and division by n gives every primitive cycle N_{n,k}. Direct independent symbolic traces for n=2..8 agree with coefficients, while the inspected exact rational checker covers 2..12 by another method. The Perron eigenvalue (1+sqrt(1+8e^t))/2 has log-derivatives 1/3 and 2/27. Primitive periods differing from full-period traces contribute exponentially less, giving a valid MGF Gaussian limit. Bhattacharya Cor.4.11 is genuinely applicable to unimodal patterns, as read in its full proof. No claim concerns other maps or local CLT.

## originality

PASS

Bhattacharya Cor.4.11 gives equality of unfolding and classical over-rotation numbers for unimodal/bimodal patterns, not a complete primitive-cycle multiplicity table for a fixed full tent map. Existing forcing and over-rotation interval results classify attainable types, and the unmarked dynamical zeta cannot recover a crossing-weighted distribution. The exact marked boundary correction and Möbius spectrum remain best-of-knowledge new.

## value

PASS

How many primitive cycles realize each unfolding fraction is the natural multiplicity refinement of the existence spectrum on the paradigmatic full tent map. The complete integer formula and Gaussian distribution of the statistic for random long cycles quantify typical orbit geometry and provide a concrete test case for weighted zeta methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
