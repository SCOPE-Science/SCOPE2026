# Scientific review

## Correctness — PASS

The result uses normalized Haar \(L^2\), the complex weighted Fourier \(\ell^1\) ball, and arbitrary positive anisotropic smoothness exponents. Finite-subgroup character orthogonality turns zero samples into one zero-sum condition per frequency alias class. The proof gives the exact inequality \(\|b\|_2\le\sqrt2\sum_kw_k|b_k|/(u+v)\) for each class, with all equality cases, and shows an extremizer must live in one class. Product weights reduce the global minimizing pair to one coordinate axis. Discrete convexity/concavity proves the smoothness-one transition; the explicit two-tone witnesses give attainment. Separate convexity and triangle-inequality arguments establish the maximum same-data diameter and nonlinear reconstruction obstruction. The comparison to optimized sampling uses a stated published theorem, not an experimental estimate.

The standalone script `verify_alias_wiener.py` passed 9,029 finite assertions, including direct frequency-pair minimizations, exact-on-grid witnesses, multiblock tests, and selected 2D enumerations. These supplement rather than replace the analytic infinite-dimensional reasoning.

## Originality — PASS, qualified

Relevant published primary materials were inspected: Moeller (2026) Sections 1–3, 6–7; Moeller–Stasyuk–Ullrich (2026) Section 6 and theorem statements; Kolomoitsev–Lomako–Tikhonov (2023) Sections 1, 5, 6 and examples. The first two quantify optimal sampling widths rather than fixed-grid nullspace radii. The 2023 grid study proves asymptotic errors of specified interpolation and quasi-interpolation operators, not the exact extremal zero-sample two-mode theorem. Searches of published mathematical records for the exact alias-pair invariant, smoothness-one phase transition, and Fourier \(\ell^1\) nullspace bounds returned related Fourier sampling spectra and bandlimited sampling-distortion records but not a statement implying this one. The inspected published sources and mathematical research records provided no duplicate of the exact fixed-grid statement. Standard Fourier aliasing and weighted convexity are acknowledged ingredients, and hidden equivalent statements in earlier literature remain a risk. No independent originality certification is claimed.

## Mathematical value — PASS

This gives a sharp all-grid-size, all-positive-smoothness formula for a canonical radius of information, complete extremizer rigidity, a critical change of the minimizing alias geometry at smoothness one, and an exact tensor-product reduction in all finite dimensions. It immediately yields the maximum diameter of observationally indistinguishable unit-ball functions. Combined with the explicitly cited optimized-width theorem, it proves a polynomial inefficiency of equally spaced sampling that persists even if nonlinear recovery is allowed. These consequences motivate the finite invariant beyond mere code reproducibility or a routine normalization check.

## Limits and closest literature

The claim applies to complex Fourier \(\ell^1\) coefficient balls and exact fixed subgroup-grid point observations; it does not determine full grid minimax radii for nonzero observations or real-valued function subclasses. The prior optimized sampling rate is external; no new proof of it is asserted. Classical or unindexed aliases remain a bibliographic uncertainty. No independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
