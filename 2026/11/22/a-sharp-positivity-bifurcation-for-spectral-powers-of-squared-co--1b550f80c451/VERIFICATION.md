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

With Haar probability normalization, the Fourier multipliers are 1,a,a,b,b and otherwise 0. For t>0 the powered operator is convolution by 1+2a^t cos θ+2b^t cos 2θ; a nonnegative approximate identity detects any continuous negative part. Minimizing in x=cos θ gives the vertex branch A(t)=1−2b^t−(a²/b)^t/4 up to t_0, then F(t)=1−2a^t+2b^t. A is strictly concave, starts at −5/4 and ends positive for ρ<1: with x=−log ρ, the comparison for b^t_0 in RESULT.md line 55 has positive slope at least 4/3−log 6/log 4>0 by 6³<4⁴. For the equality case ρ=1, the endpoint slope, which concavity alone does not supply, is A'(1)=F'_1(1)=(log(27/32))/3<0. Thus there is one earlier zero and positivity through t_0, also at ρ=1. In the late branch F=1−2q^c+2q, q=b^t, its unique unconstrained minimum is at q=c^{1/(1−c)}. The minimum increases strictly with c, and c decreases strictly with ρ: the numerator of dc/dx in line 65 starts at (log 4)/3−log(3/2)>0 and increases. As ρ→0, c→1/2 and the minimum tends to 1/2; at ρ=1, F(1)=0 and the negative derivative gives a negative minimum. This proves one critical ρ. To see rigorously that the minimum is in the late branch for ρ≥ρ_c, note t_*(1)>1 and Fρ(1)≥0. Continuity prevents a crossing of t_*=1 on the negative-minimum interval, and at ρ_c<1 one has Fρ_c(1)>0, so t_*(ρ_c)>1 as well. Since t_0≤1, the two late roots bound exactly the stated hole, with u=1 only at ρ=1. At criticality the minimum touches zero without a hole; F_tt>0 and F_ρ<0 follow from stationarity and b'/a'≤1, b<a, t_c>1. Scaling t−t_c by √(ρ−ρ_c) gives simple roots ±K in the rescaled leading quadratic and the stated errors. No statement about order positivity at time zero on the full space is needed.

## originality

PASS

The positivity-hole phenomenon in spectral powers is not specific to this result. Credit the same-date Bernstein–Durrmeyer classification as material qualitative overlap without inferring their order. The distinct contribution is the exact positivity diagram for the parameterized squared-cosine convolution family, in particular the unique transition in ρ and nondegenerate fold of the two endpoints. No equivalent or stronger effective classification was found in the inspected statements.

## value

PASS

This elementary normalized positive kernel is a natural Fourier model distinguishing order positivity from spectral positivity. The contribution is a complete two-parameter picture: onset, re-entrant loss, recovery and the sharp transition between one and two intervals, including the isolated touching case. The exact constants and uniform fold are useful for testing when positive time evolution is not preserved by spectral interpolation. A single example of disconnection would add substantially less in light of the Bernstein–Durrmeyer comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
