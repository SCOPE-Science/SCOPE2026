# Independent mathematical audit

## correctness

PASS

For the truncated quadratic on the three-state nilpotent shift, the diagonals are r=1−h+h²/2, b=γh(1−h), c=γ²h²/2. An independent norm argument avoids any possible ambiguity about the determinant crossing. With J the reversal matrix, B=JT is real symmetric with rows (0,0,r),(0,r,b),(r,b,c). Thus the condition is I±B positive semidefinite. For 0<h<2 the leading blocks are diag(1,1±r)>0 and the remaining Schur complements are 1±c−r²−b²/(1±r). The plus complement is strictly positive since 1+r−2(1−h)²=3h(2−h)/2>0. Solving the minus complement for γ² gives exactly F(h); a zero there forces norm equality. At h=0 the step is identity, at h=2 an off-diagonal forces norm greater than 1 unless γ=0, and h>2 has scalar radius greater than 1. In particular h=1 is regular even though b=0. The independent SymPy replay at /workspace/reviews/replay-2-3.py verifies the determinant identity, derivative, resultant and rational witness. C'(h)=9(h−4/3)²+4 makes the critical root unique, and F'(h) changes from positive to negative there with nonzero slope. F(0)=2, F(2)=0; horizontal sections give all four parameter regimes, including the detached interval, its fold and the isolated positive critical step. The symmetric-generator criterion gives the true all-time Euclidean threshold √2, and the supplied 10/7 witness is strict at h=1/2. The replay gives γ_*²≈2.0946107542350062 (the last displayed auxiliary digit in the source is slightly off); the exact formula and quoted γ_*≈1.4472770136483914 agree. No same-finite-time physical expansion or integration accuracy is required for the contrast.

## originality

PASS

Qualified credit for the exact quadratic-RK, index-three maximum and full step-region classification, not for the stability polynomial, Schur/Gram tests or the continuous logarithmic norm.

## value

PASS

For the smallest defective shift with two nontrivial Jordan terms, the result determines exactly when an order-two step is nonexpansive, including where decreasing the timestep can destroy that property and the finite shear beyond which no positive step works. This is an exact benchmark for energy-based timestep reasoning on a spectrally fixed, nonnormal problem, not an accuracy claim. The role of N² distinguishes it from a routine reuse of the planar derivative-zero mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
