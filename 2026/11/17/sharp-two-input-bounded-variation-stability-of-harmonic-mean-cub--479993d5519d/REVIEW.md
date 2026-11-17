# Scientific review: harmonic-mean Hermite variation sensitivity

## Correctness — PASS
The sharp statement is for all real bi-infinite finite-variation sample sequences on the uniform grid. The signed harmonic selector is locally absolutely continuous in each increment and has coordinate derivatives in the sharp interval \([0,2]\). The one-edge directional perturbation has exactly three nonconstant Hermite cells, with variations \(8u/27\), \(1\), and \(8v/27\). The middle cell remains monotone for every \(u,v\in[0,2]\) by checking four quadratic derivative polynomials. Telescoping finite changes and using lower semicontinuity extends the bound to all summable increment differences. The near-plateau example gives the exact rational ratio \(1+32/(27(1+\varepsilon))\), hence the sharp supremum \(59/27\). The code checks symbolic identities and rational witnesses, with numerical tests only as corroboration.

## Originality — PASS, with historical-priority risk
Fritsch–Butland (1984), fully inspected at pages 300–304, supplies the harmonic-mean slope construction and one-input monotonicity, not an explicit variation modulus between two interpolated datasets. Edelman–Micchelli (1987), inspected at pages 441, 443, 448, treats admissible slope geometry and cannot by itself imply this specific two-input norm. Aràndiga–Yáñez (2019), inspected in its introduction, formula definitions and main monotonicity theorems, treats accuracy and shape preservation of related means, rather than the stated sharp perturbation factor. Public mathematical searches and prior-claim comparisons found no direct covering result. This is not a proof of global historical uniqueness; unindexed results and uninspected sections of the secondary papers remain risks.

## Mathematical value — PASS
The harmonic-mean cubic is a classical shape-preserving interpolant. Its individual total-variation equality might suggest robustness, whereas the sharp two-input gain \(59/27>2\) establishes a concrete counterintuitive stability separation. The result applies to the whole infinite uniform grid, identifies the local three-cell mechanism and the extremizing near-plateau geometry, and requires no arbitrary finite-size cutoff. It is relevant to data perturbations in shape-preserving reconstruction, not merely to evaluating known interpolation coefficients.

## Closest sources and limits
- Fritsch and Butland, 1984, DOI 10.1137/0905021, fully inspected; interior formulas (2), (5), pages 300–301, and numerical examples through page 304.
- Edelman and Micchelli, 1987, *Admissible Slopes for Monotone and Convex Interpolation*, selected pages inspected.
- Aràndiga and Yáñez, 2019, DOI 10.1016/j.aml.2019.02.012, discussion of harmonic means and interpolation accuracy inspected.

This proof does not cover finite boundary PCHIP derivative formulas, irregular grid spacing or other nonlinear slope limiters. The 1984 paper's printed issue gives June 1984 without a specific day; its explicitly verified first online-release day is July 14, 2006, which is the dated online source evidence here. Historical priority and the exact first print-release day have not been independently established.

Self-review: passed. Independent audit: not yet performed.
