# Self-review

## Correctness
PASS. The four explicit planar-iterate identities establish every return branch without an unproved finite enumeration. Their intervals partition the section modulo endpoints, with absolute slopes \(d^2\) and \(d\) and total branch lengths one. Cylinder lengths factor exactly, proving the iid Bernoulli return law. The finite-mean suspension is invariant and ergodic; an explicit positive-area strip maps to its section generic set. Abramov's theorem and rational roof moments give the entropy and return-count variance; differentiation across the section establishes the positive Lyapunov exponent, and branch rank collapse establishes the negative-infinite exponent. `check.py` provides independent *computational reconstruction*, not independent mathematical audit.

## Originality
PASS within inspected literature, with residual priority risk. Simpson's 2026 first-return theorem treats the same encompassing border-collision model and supplies the general return-time partition framework, but does not calculate this integer-slice Bernoulli law, its dual slope distribution, its explicit entropy, physical measure or visit-count variance. Simpson's 2024 preprint/2025 article concerns qualitative bifurcations, not these quantitative invariants. Published related rank-one cases with **both** determinant branches zero are distinguishable: their right branch is a translation on an attracting interval, whereas the present right branch has determinant \(d\ge2\), complex eigenvalues of modulus \(\sqrt d>1\), and two different induced branch slopes. Standard Bernoulli, Abramov and renewal theorems provide methods but not the specialized formulas by themselves. A potential older parameter-specific computation remains a priority risk.

## Value
PASS. A new 2026 analysis explicitly proposes exploiting one-dimensional return maps to understand robust-chaos and mode-locking structures in a zero-determinant border-collision family. The theorem obtains an exactly evaluable invariant probability, metric entropy, Lyapunov exponent and Gaussian visit-frequency fluctuations in the genuinely expanding-focus regime, where qualitative return partitions alone do not give statistical laws. The two slope classes distinguish this slice from previously published rank-one/rank-one renewal examples. Its scope is narrow but natural and supplies a benchmark for studying statistical stability away from the integer determinant slice.

## Limits
The result is not a classification of all invariant measures, global attraction, topological entropy, noninteger parameters or perturbations. It does not show that the original planar dynamics is itself an iid Bernoulli process. The main relevant 2026 return-map theorem supplies a powerful reduction and may allow an alternative derivation; a separate independent historical-priority review is still needed.

Self-review: passed. Independent audit: not yet performed.
