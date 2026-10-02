# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Scientific disposition

- Correctness: PASS. The spectral theorem represents the normalized autocorrelations as moments of a probability measure on \([0,1]\). Quadratic Hermite interpolation at the two canonical support pairs gives the stated lower and upper expectation bounds whenever the third derivative is nonnegative. Substitution of powers and of the finite-horizon variance polynomial gives the later-lag and sample-mean formulas. The long-run lower bound follows by monotone approximation of \((1+x)/(1-x)\), and the explicit two-point family with an atom tending to one preserves the first two moments while sending long-run variance to infinity. The actual verifier was inspected and an independent exact check reproduced the canonical moments and worked lag-three interval.
- Originality: FAIL. The mathematical core is already covered at the implication level by two established ingredients: reversible-chain autocovariances are a compactly supported moment sequence, and classical Markov--Krein/truncated Hausdorff theory gives best upper and lower expectations under finitely many moment constraints via canonical finitely supported measures. The displayed later-lag and finite-horizon formulas are direct substitutions into that general theorem; the long-run dichotomy is an elementary two-point specialization. Exact wording in the MCMC literature is therefore unnecessary under the audit's implication standard.
- Value: FAIL. The chain-specific formulas are useful diagnostics, but after the published moment representation is combined with standard two-moment extremal theory they are routine substitutions and elementary two-point algebra. Under the shared value bar, correctness, sharpness, and reproducibility do not turn that mechanically implied specialization into a separate mathematical gap.

Acceptance requires all three axes to pass. The complete original package is retained as failed evidence and is not a validated finding.

## Preserved evidence

The original result, slogan, metadata history, and reproducibility artifacts remain part of the archived package. The dated independent-audit files record the scientific comparison and residual risks.
