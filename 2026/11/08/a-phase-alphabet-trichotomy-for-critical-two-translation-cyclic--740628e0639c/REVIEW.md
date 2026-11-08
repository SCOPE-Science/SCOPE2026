# Mathematical review

## Correctness

**PASS.** The exact Gram conditions reduce by a complete \(N/2\)-point discrete Fourier transform to the pointwise half-cycle relation \(c(j+N/2)=-c(j)\). Unimodularity then reduces this to the alternating ratio condition \(H(j-k)=-H(j)\). The translation orbits have order \(t=N/\gcd(N,k)\), forcing even \(t\); a half-cycle displacement makes \(H(j)^2=(-1)^{t/2}\). Independent choices of two ratio signs per translation orbit and arbitrary first-half phases give a complete bijection and exact count, with no omitted boundary cases (including \(N=2\) and non-subgroup translation pairs). The all-length argument is analytic. A separate exact-integer checker exhaustively validates small cases and constructs larger witnesses; these checks are supplementary, not a substitute for the proof.

## Originality

**PASS relative to inspected evidence, with residual priority uncertainty.** Asipchuk–De Carli–Rodriguez (arXiv:2605.16139, Theorems 1.1 and 1.3 and Sections 3–5) give subgroup-driven block decompositions and special sufficient orthogonality constructions, but not the present exact all-\(k\), all-\(q\) phase-alphabet threshold or solution count. Nicola (arXiv:2305.02738) classifies maximally ambiguity-localized Gabor orthonormal bases, imposing an extremal localization condition absent here. The finite prime-field classification (arXiv:1712.09120) concerns a different setting. Publicly indexed finite-Gabor results about sparse windows, cyclic STFT zero patterns, frame operators and tomography concern different invariants and neither imply nor tabulate this sharp alphabet trichotomy. No claim of exhaustive publication priority is made: an unindexed polyphase-filter formulation is a substantive remaining risk.

## Value

**PASS.** The problem is a natural critically sampled, phase-quantized Gabor design: one wants an orthonormal analysis/synthesis basis using exactly two time translates and the half-frequency modulation subgroup while controlling the alphabet used for the window. The sharp result separates impossible, binary-feasible, and genuinely quadrature-required translation steps by the two-adic order of the step, and classifies all designs rather than just constructing one. Exact counts and torus components are meaningful structural information for quantized window design; no downstream performance guarantee beyond orthonormality is asserted.

## Limits

Neither a complete arbitrary-lattice Gabor classification nor a robustness or localization theorem is claimed. Repeated or earlier treatments under another name remain possible; independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
