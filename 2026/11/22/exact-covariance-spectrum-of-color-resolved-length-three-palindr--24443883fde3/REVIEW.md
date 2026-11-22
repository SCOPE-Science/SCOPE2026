# Scientific review

## Correctness — PASS
The exact covariance is obtained from the only five potentially overlapping cyclic shifts of two length-three factors, with joint probabilities determined by matching ordered letters. The spectral proof exhausts the off-diagonal array space by a constant direction, two row/column-contrast sectors, and symmetric and skew-symmetric zero-row flow sectors; the dimensions sum to \(q(q-1)\). The discriminant inequalities prove strict ordering and positive definiteness. A bounded two-dependent multivariate central limit theorem applies for fixed \(q\); positive-definite whitening gives the asserted chi-square limit. Independent rational enumeration and mode checks are supplied in `checker.py`.

## Originality — PASS, qualified
A general overlap-matrix computation of contiguous-pattern covariance is already established by *A unified approach to word occurrence probabilities* (DOI:10.1016/S0166-218X(00)00195-5, particularly its Theorem 30), so neither the existence of the covariance formula nor individual-pattern moments are claimed as new. Rubinchik–Shur (arXiv:1505.08043) determine expected palindromic-factor counts and study distinct factors, not the complete ordered-color covariance eigenstructure. Even-Zohar–Lakrec–Tessler (arXiv:2012.00742) diagonalize *scattered-subsequence* word statistics, not contiguous cyclic motifs. The assessed claim is the explicit complete five-class spectrum, its finite-sample all-alphabet strict order and condition number, and resulting multivariate calibration. Historical priority remains uncertain: only indexed passages of the older general overlap paper were accessible, and no search proves absence of an earlier specialization.

## Value — PASS
The vector distinguishes each ordered outer/inner letter pair rather than collapsing to one palindrome total. Its covariance has natural exchangeable-color symmetry but is not scalar or multinomial; the exact diagonalization identifies the effective color-contrast and edge-circulation fluctuation modes. All nonconstant modes have positive variance even at finite circle size, making an invertible, explicitly conditioned covariance and a reproducible omnibus chi-square null calibration available without numerical covariance estimation. The near-isotropy formula \(\kappa=1+(3+\sqrt5)/q+O(q^{-2})\) also gives an interpretable alphabet-size stability law. This is a natural complete classification, not a parameter-only numerical coincidence.

## Limitations and closest literature
The general overlap covariance is prior knowledge; older unavailable full-text material leaves residual priority risk. No fixed-size exact chi-square law, nonuniform-alphabet theorem, jointly growing-alphabet CLT, or optimal testing-power statement is asserted. The finite checker verifies specified sizes, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
