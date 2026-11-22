# Research assessment

## Correctness

PASS. The Weibull scale profile gives \(n^{-1}\sum_jY_j=1\), providing an exactly universal small-\(t\) empirical minCF interval \((0,1/n]\). The Bessel integral and a one-saddle Laplace expansion give the leading term. A deterministic integral tail estimate establishes the uniform inequality. The positive first correction follows from clipping at \(t=1/M\), its linear right derivative and endpoint Laplace integration. Its exponential dependence on \(M\) proves eventual reverse ordering. Finite checks (66 assertions) verified the identities and sample cases but were not used as the asymptotic proof.

## Originality

PASS, with historical-priority limitations. The primary source, Meintanis–Milošević–Jiménez-Gamero (arXiv:2310.12348, sections 3–6 and appendix), proves invariance, null asymptotics and fixed-weight consistency; those statements do not imply the weight-varying saddle/correction or its sample-ranking consequence. Matsui–Meintanis (arXiv:2307.03429) treats equivariance but no high-weight minCF theorem. Falk–Stupfler's minCF theory supplies foundational transform properties and could potentially be combined with classical Laplace asymptotics; abstract-level examination of that source was not an exclusionary full-text assessment. Targeted indexed literature and research-record searches found no directly covering statement. The possibility of older general-kernel Laplace results is a residual priority risk, not a claim of mathematical independence.

## Value

PASS. The test's large-weight behavior is not simply that its statistic becomes small: its dominant term is **exactly sample-independent** while its first distinguishing contribution encodes a sample extreme. The joint uniform bound gives a concrete sample-size/weight relationship, and the reversal of the conventional large-statistic ordering diagnoses the loss of balanced goodness-of-fit information at extreme weights. This offers a mathematically motivated tuning limitation for a published invariant procedure without asserting that its fixed-weight results are false.

## Scope and outstanding risks

The proof concerns fixed datasets for the second-order formula, and uniform first-order collapse for \(\gamma/n^2\to\infty\). No exact asymptotic test-power theorem at moving weight is claimed. Full global priority cannot be certified, and an independently reviewed proof is not available.

Self-review: passed. Independent audit: not yet performed.
