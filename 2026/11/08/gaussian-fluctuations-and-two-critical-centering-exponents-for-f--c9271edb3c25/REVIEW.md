# Scientific review

## Correctness — PASS

The independent exponential-clock construction gives exact Bernoulli first-discovery probabilities. The proof directly establishes a positive limiting variance and a Lyapunov bound \(O(N^{-1/2})\) for the triangular array at times within \(N^{-1/2}\) of the unique mean root, then inverts the fixed-time CLT using monotonicity. The centering expansion follows from the generalized harmonic-sum Euler--Maclaurin formula and a smooth endpoint Riemann-sum bound. The exceptional \(3/4\) boundary follows from a genuinely nonzero negative second-order coefficient. An extracted numerical checker completed 45 assertions, including finite subset enumeration and Gaussian-scale simulation. Infinite claims are analytical, not inferred from the finite checks.

## Originality — PASS (subject to historical-priority uncertainty)

The nearest motivating work, Müller--Šebek (arXiv:2607.08551v1), presents first-order deterministic limits for the same diffuse Zipf family. In contrast this result tracks \(\sqrt N\)-scale hitting times and the first two finite-size centering terms, including a unique threshold-parameter cancellation curve. Chebunin--Zuyev's functional missing-mass CLT treats a fixed infinite-frequency urn, so its hypotheses do not directly match the finite normalized triangular array or supply these threshold centering coefficients. Targeted scientific-source comparisons found no directly covering statement; that does not establish absolute historical priority. The motivating primary source could be inspected for definitions and initial formulas, but its later sections were inaccessible after the initial read, and broader unlocated inverse-CLT literature is a residual risk.

## Mathematical value — PASS

Replacing the finite mean root by a simple first-order deterministic center is often necessary for inference or approximation. This theorem identifies exactly when that simplification changes the asymptotic Gaussian law, with the exceptional cancellation curve revealing a second sharp transition. The transitions at \(1/2\) and \(3/4\) are consequences of finite-support Zipf normalization competing with sampling noise, rather than an arbitrary parameter restriction or a textbook CLT by itself.

## Limits and closest literature

The theorem covers fixed \(s\in(0,1)\), fixed \(\theta\in(0,1)\), independent exponential clocks, and a fixed arrival-rate parameter. It does not claim moving-parameter limits, a discrete-time version, or moment convergence. The closest primary sources are Müller--Šebek (2026), Chebunin--Zuyev (2020/2022), and the earlier infinite-urn work of Karlin. Priority and proof remain open to independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
