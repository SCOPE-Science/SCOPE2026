# Scientific review — fractional-moment shift defect staircase

## Correctness — PASS

The precise domain is \(m\ge2\) integer, \(a>0\), \(m-2<\alpha<m-1\), and real \(\eta>-a\). The weights are positive and bounded. The defect is diagonal and its signs reduce to one finite-difference quotient. A unit-cube derivative representation proves both signs without numerical assumptions. Its weighted-mean quotient has derivative strictly exceeding \(\alpha/(m-\alpha)\), by the strict Cauchy--Schwarz inequality. This yields all-index threshold monotonicity, the full positive-rank and kernel classification, and the large-parameter counting law. The diagonal tail is nonzero to leading order \(n^{-m}\), proving compactness and the exact quasi-Schatten cutoff. The packaged standard-library diagnostic makes 888 finite consistency checks; it is not relied upon for any infinite conclusion.

## Originality — PASS, qualified

The strongest direct comparison, Suciu (arXiv:2611.20171v1, Sections 1–3), establishes general higher-order lifting mechanisms, defines the defect, and gives other weighted-shift examples; it does not establish the present two-power fractional-moment thresholds or complete defect spectral classification. Chavan–Stochel (2023, Proposition 4.3) concerns polynomial-moment \(m\)-isometries and related weak concavity, and Benhida–Curto–Exner (arXiv:2309.05888v2, Section 1 and main results) use geometrically regular weights with exponential-power dependence. Their stated cases and consequences do not yield this classification directly. Equivalent formulations by finite-difference sign changes and stronger divided-difference comparison theorems were searched; no statement covering the complete classification was identified. This is a best-knowledge comparison, **not a proof of priority**. A broad classical total-positivity/divided-difference theorem may implicitly subsume the threshold monotonicity, and uncatalogued literature could cover the exact family.

## Mathematical value — PASS

The one-parameter moment perturbation of a fractional-power shift is a natural controlled test for the higher-order concavity condition that triggers recent lifting results. Determining **exactly** which perturbations satisfy it, and how the entire sign spectrum changes beyond its boundary, is a meaningful classification rather than a binary sample calculation. The strict separated rank staircase, explicit asymptotic number of positive defect modes, and parameter-independent singular-value/Schatten tail jointly distinguish finite-dimensional leakage from invariant infinite-dimensional defect regularity. The exact family is intentionally restricted and does not pretend to classify all lifts or weighted shifts.

## Prior-work and residual limitations

Direct literature inspected: Suciu's full HTML preprint, including the definitions, Theorem 3.2 and weighted-shift examples; Chavan–Stochel's article including Proposition 4.3; Benhida–Curto–Exner's full HTML paper with its moment/contractivity and hyperexpansivity framework. The classical finite-difference identity and known lifting consequence are credited. No independence, external mathematical certification, or exhaustive bibliographic priority is asserted.

Self-review: passed. Independent audit: not yet performed.
