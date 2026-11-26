# Independent mathematical audit

## correctness

PASS

The Schur complement is positive by the SPD hypothesis; independent scalar and planar noises realize the specified mobility. With F(phi)=-R(phi)Jh/m, Ito's formula gives dF=(R(phi)h/m)dphi+Theta R(phi)Jh dt, the latter term being exactly the Stratonovich correction. A cycle separates into the endpoint difference and a conditional-mean-zero independent-driver stochastic integral; the cross-covariance is zero, not an assumption of independence of the two displacements. The angular first harmonic gives the mean; its second harmonic gives the signed aa^T term and integral of the rotated traceless Schur complement. Division by tau yields covariance per time (not half that tensor). Complete cycles are iid; the uniformly bounded partial-cycle second moment gives the covariance limit and negligible CLT remainder, and a maximal fourth-moment bound gives the almost sure drift for all times. In the K=kI case the axes are parallel/perpendicular to a; the positive Schur-complement contribution and negative angular contribution combine to the stated square gap. The derivative has the sign of 1+4z-exp(2z), whose only strictly positive zero is unique by strict concavity and the positive slope at zero; the gap vanishes at both ends. Independently checked the benchmark matrix by scalar angular moments and quadrature, and root 0.6282156043130848385 and coefficient 0.4072643775890737501 by high-precision bisection. Replay: python3 -B /workspace/branches/frozen_review_replay.py 2. This confirms the optimizer only in the isotropic K case with h nonzero and is not an optimization of sorting fidelity. Frozen script and requirements inspected, not executed.

## originality

FAIL

The distinct 2026-10-26 Resultary record states and proves the same general coupled deterministic-periodic centered tensor and CLT, with equivalent drift and exactly the same noise and reset protocol. The specialization to K=kI and its positive drift-aligned gap follow algebraically. The earlier text does not explicitly maximize that gap; its maximization is a direct scalar calculation from the covered formula, not evidence that the tensor or anisotropy law is distinct. This is statement coverage, not a priority or authorship determination.

## value

FAIL

The centered dispersion tensor is a worthwhile observable, but it and the positive gap are already covered. The new scalar peak calculation is a routine optimization of a one-variable profile directly supplied by that coverage; it addresses only the gap, not a new sorting/diffusion tradeoff or regime. No separate value-bearing remainder or repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
