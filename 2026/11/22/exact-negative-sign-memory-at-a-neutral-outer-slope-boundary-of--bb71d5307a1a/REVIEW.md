# Self-review

## Correctness — PASS
The proof identifies the exact Markov cells, their transition probabilities and stationary mass, and uses the expanding primitive graph for uniqueness of the absolutely continuous law. A full-branch central return induces independent uniform waiting times of lengths \(1,\ldots,m\), so a direct renewal recursion and residual-life weighting give the claimed all-integer formula for \(0\le n\le m\). The sign of the finite difference establishes the exact minimizing lag including the exceptional tie at \(m=2\). The limit is a uniform exponential limit and the trough is strictly negative. An independent exact-rational 493-case Markov verification supports, but does not replace, these analytical steps.

## Originality — PASS within inspected evidence
The same family originated with García-Grimaldo and Campos-Cantón (2021). The fully accessible 2023 Electronics article addresses hardware implementation, bifurcation diagrams, Lyapunov exponents and histograms; it does not state this exact sign-statistics result. The extended 2023 thesis analyzes the source family in chapter 3 and numerical autocorrelation of other pseudorandom outputs in chapter 6, not this formula for the neutral-outer-slope Markov subfamily. published-finding corpus comparisons concern prime-three cycles, Lyapunov floors or other maps' renewal statistics; none implies the explicit model-specific lag formula and universal anticorrelation minimum. Standard renewal theory is a proof method, not the prior computation of the model-specific law. The full 2021 source and 2022 comparative chapter could not be inspected in full, so publication priority remains qualified by these sources and any unindexed work.

## Value — PASS
The original PWL family is presented as a candidate for pseudorandom-output applications. The exact stationary sign-memory phenomenon is quantitatively distinctive: one-step sign-flip frequency tends to zero, yet at lags of order the inner slope a persistent negative covariance approaches a universal constant. The formula and sharp lag location give structural information that finite Lyapunov/histogram studies do not, while making no cryptographic-security assertion. The integer-slope/outer-unit slice is natural because it yields a finite Markov renewal decomposition with a nontrivial large-slope limit.

## Residual limitations
The analysis is restricted to the stated boundary family and lags through the inner integer slope. It makes no statement about all stationary measures or other hardware bit extractions. Earlier publisher full text, and any unindexed equivalents, remain possible novelty risks. The complete proof is self-contained in the attached result.

Self-review: passed. Independent audit: not yet performed.
