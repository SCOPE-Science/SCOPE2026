# Scientific review

## Correctness — PASS

The theorem defines mixed-population payoff differences and sign-change counting precisely. Conditioning whether two opposite-type focal individuals are included in each other's interaction group gives the exact hypergeometric comparison identity, with inclusion probability \((n-1)/(N-1)\). This makes the payoff difference a polynomial of degree at most \(n-1\) in the population cooperator count. Strictly increasing positive returns at the fixed terminal critical value force negative and positive endpoint signs. The parity-improved upper bound follows from the count of intervening zeros; the rational family provides sharpness, strict increase and aggregate zero. The Fermi product identity gives equal single-mutant fixation probabilities for every selection intensity. An independent exact-fraction checker passed 19 construction sizes and additional polynomial-degree cases.

Risk: The finite numerical checks alone would not cover arbitrarily large \(n\); the explicit inequalities and polynomial argument in the proof supply the general conclusion. The assertion does not cover fixed noncritical terminal returns or non-Fermi updates for the fixation corollary.

## Originality — PASS (literature-bounded)

Wang et al. (2026) state a terminal-return criterion for aggregate selection under weak selection; this does not determine the number of mixed-state sign reversals. Hauert and McAvoy (2024) study linear multiplication-factor dependence, whose limited curvature does not imply the sharp all-group-size monotone-schedule construction. Wu, Traulsen and Gokhale (2013) already supply the general polynomial degree observation, so the degree-only bound is background rather than claimed novelty. A relevant prior finding about convex payoff differences requires geometric synergy factors, while a separate finite-mutation finding concerns changes in stationary abundance rather than this zero-mutation parity-sharp local-selection census. The exact parity bound combined with rational strict-economies-of-scale attainment and terminal-neutral fixation was not identified in searched published claims or inspected primary sections.

Risk: General mathematical observations about Bernstein/hypergeometric polynomials can yield parts of this proof, and unindexed prior literature might contain an equivalent monotone-return construction. No historical uniqueness claim or independent validation is made.

## Value — PASS

The number of local evolutionary selection reversals is an intrinsic measure of complexity of a population game's fitness landscape. The source's surprising terminal-return criterion does not constrain this complexity; even strictly increasing multiplication factors and increasing total public benefit attain a parity-sharp sequence of successive local reversals. The theorem supplies a natural complete maximum and constructive witnesses for every group size, showing a precise limitation of reasoning from long-run homogeneous-state abundance alone. This is a structural finite-population classification rather than an arbitrary isolated parameter computation.

Risk: The attaining multipliers are specifically constructed, and no empirical prevalence or independent practical application is claimed.

## Closest literature and limits

Scientific comparisons are documented in `AUDIT.json`; the three inspected primary full-text sources appear in `RESULT.md`. The deterministic proof, exact rational code and scope limitations are complete, but research literature searches are not comprehensive certification.

Self-review: passed. Independent audit: not yet performed.
