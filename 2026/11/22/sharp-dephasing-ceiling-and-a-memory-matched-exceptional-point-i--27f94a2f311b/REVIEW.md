# Self-review

## Correctness (PASS)
The proposed clock and clipping rule uniquely specify a normalized causal kernel. Its exact finite-dimensional memory embedding follows by convolution differentiation and yields the stated eigenvalues. Weighted dissipativity proves strict stability; a sharp discriminant inequality proves the global rate ceiling and its complete equality case. Noncancellation of the dominant coherence mode and an exact matched-rate modulus derivative prove the actual observable rate, the exceptional-point signal, and CP-divisibility. The embedded `verify.py` passed 270 RK4-to-exact comparisons plus spectral, monotonicity and EP checks. Numerical tests are supporting regressions, not infinite proofs.

## Originality (PASS, qualified)
The closest primary source [1] analyzes uniform sampling of all previous times, in which coherence decays algebraically, and explicitly leaves nonuniform kernels open. The classical general-kernel source [2] does not imply quantum Bohr-frequency decay and the CP-divisibility theorem. The more recent non-Markovian exceptional-point source [3] treats colored Gaussian quantum baths, not reset-to-past trajectories; its readout considerations are explicitly addressed by the noncancellation proof. Targeted mathematical index comparisons cover power-biased quantum history kernels, uniformly history-reset qubits, and an exponential-memory dichotomous bath. None of the inspected statements implies the clipped exponential-age qubit's sharp, globally rate-optimal dephasing ceiling and no-backflow exceptional point. A generic unindexed 2x2 memory-embedding result might nevertheless subsume part of the claim; publication priority requires independent checking.

## Value (PASS)
The object is a natural, normalized finite-memory alternative to the recently studied uniformly history-reset qubit. The sharp equality locus furnishes a physically interpretable optimal matching principle rather than only a formula. The exceptional point proves that defective relaxation modes need not cause distinguishability revivals, separating two often conflated temporal signatures. The restriction to clipped exponential sampling and one qubit is material and explicitly disclosed.

## Boundaries and literature
Arbitrary Hamiltonians with many different gaps, renormalized truncated exponential kernels, and nonexponential memory are not covered. Related literature is itemized in RESULT.md and originality comparisons in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
