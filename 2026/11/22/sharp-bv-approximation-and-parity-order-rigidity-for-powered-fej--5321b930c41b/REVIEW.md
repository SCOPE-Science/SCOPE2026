# Scientific review

## Correctness — PASS

The normalized Laurent polynomial identity gives the exact finite Fourier constant. The circle BV translation inequality proves the upper bound; the exact symmetric arc-leakage formula gives semicircle attainment, and BV coarea plus nested superlevel sets proves that all equality inputs are exactly two-level semicircle functions. Taylor expansion of the kernel at its antipode proves the parity orders and constants. Dominated convergence and the classical logarithmic integral establish the Jackson-square asymptotic. The included standard-library checker passed 968 exact coefficient and parity tests, positive quadrature and arc tests, plus large-degree asymptotic sanity checks. No finite test is used for an infinite quantifier.

## Originality — PASS, with historical priority risk

The 2010/2013 Nielsen treatment concerns matrix-weighted Lp convergence of Jackson summation, while the 2013 Babenko–Kryakin–Staszak article concerns continuous-function modulus inequalities and Jackson–Stechkin bounds. The 2024 Catala–Hockmann–Kunis–Wageringel paper uses the same squared-Fejér Jackson kernel to bound the first moment in Wasserstein measure approximation, so the kernel and its first-moment bound are prior art, but its inspected §§3.3–3.4 do not imply the exact BV-to-L1 norm, classification of all extremizers or the general powered parity-order law. An earlier published ordinary-Fejér q=1 BV claim establishes only the lower power case; it does not imply the explicit all-q finite constants or 2q+2 vanishing orders. Closest published-finding corpus hits concerning powered Fejér–Jackson kernels measure bounded-input-to-Lipschitz gain, a different norm. Unindexed older literature may contain equivalent formulas and cannot be excluded by these searches.

## Value — PASS

Sharp error calibration on discontinuous periodic signals for the classical Jackson kernel and all integer-powered positive summation families is a natural approximation question. The exact finite-degree coefficient, full extremizer classification and parity-dependent high-order flatness provide information not supplied by known O(1/n) bounds; in particular raising power changes local robustness to displacement at even degrees from quartic to order 2q+2. q=2 asymptotic 6 log(2)/pi ties the natural Jackson rate to its sharp BV worst case. The isolated integral and elementary kernel identities are acknowledged as known and are not claimed as new.

## Material primary comparisons and limits

The 2010 research report is dated by year alone; the earliest selected precisely day-dated public research lead is the March 20, 2013 journal version. This date is not asserted to be the first public appearance of all underlying ideas. Nielsen's §3 and Theorem 12, Babenko–Kryakin–Staszak's principal theorems, and Catala–Hockmann–Kunis–Wageringel's §3.3/Remark 3.4 were read at the accessible HTML level. The latter source already gives Jackson normalization and a first-moment bound; no claim of priority for those items is made. Independent literature review has not been conducted.

Self-review: passed. Independent audit: not yet performed.
