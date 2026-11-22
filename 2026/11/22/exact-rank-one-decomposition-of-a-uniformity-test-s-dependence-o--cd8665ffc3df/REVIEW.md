# Self-review

## Correctness — PASS

Under the fully specified continuous simple null, the probability integral transform yields independent uniforms. Expanding the two quadratic Hilbert statistics into diagonal and degenerate off-diagonal pieces gives the exact covariance identity (1). Independently checked polynomial integrals give the six displayed rational contractions. The separate Watson identity and the derivative factorizations prove both correlation inequalities for every \(n\ge2\). The standard-library rational checker passed 13,510 checks, including independent direct-statistic evaluation, without using simulations as infinite proof. Boundary \(n=1\) has deterministic Watson statistic and is explicitly excluded from the correlations.

## Originality — PASS, with residual priority risk

Ebner–Liebenberg–Visagie (2021, arXiv:2108.06391) defines the exact characterization statistic, its limiting Gaussian law and its empirical power comparisons against the classical tests. Inspection of the full manuscript's definitions, limit calculations, simulation sections and conclusion identified neither the exact cross-covariances nor the rank-one contribution fractions. Hwang–Kuriki (2024, arXiv:2404.06040) treats generalized classical EDF quadratic processes, not the weighted-indicator statistic. Existing exact Cramér–von Mises/Watson cross-correlations concern two different kernels, so they do not imply this three-way theorem without new integrals. Literature searches and relevant existing mathematical research records were checked by statement, not only by keyword. Historical priority is not exhaustively settled; a general formula from another source might have evaluated the same particular cross-kernel.

## Value — PASS

The 2021 paper compared the new omnibus statistic against classical Cramér–von Mises and Watson procedures in the same applications, leaving unquantified how redundant their joint signals are under a simple null. Exact covariance for every sample size is useful in analyzing combined or multiscale calibrations. The stronger structural statement identifies that over 76.9% of the covariance with Cramér–von Mises is carried by the sample-mean component, while Watson retains a substantially weaker but nonzero coupling. This is a motivated, parameter-free joint-null comparison, rather than a free-standing arbitrary integral. It does not establish independence, a power benefit or combined-test critical values.

## Scope and remaining risks

Only fully specified continuous simple nulls. No composite-null parameter fitting, simultaneous local-alternative analysis or joint distribution. The method is a standard degenerate-kernel identity; possible earlier unlocated explicit cross-kernel evaluation is the main originality risk.

Self-review: passed. Independent audit: not yet performed.
