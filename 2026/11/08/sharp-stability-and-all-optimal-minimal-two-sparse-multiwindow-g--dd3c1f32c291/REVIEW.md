# Scientific review

## Correctness — PASS
The claim concerns full complex-Hermitian linear intensity lifting from exactly \(m=\lfloor N/2\rfloor\) unit two-sparse Gabor windows. The Weyl conjugation characters diagonalize the frame operator, giving \(N\sum_r|\langle g_r,M_vT_ug_r\rangle|^2\). A minimal injective family must assign exactly one support-difference class to each of the \(m\) unoriented nonzero differences. At a non-antipodal lag, only its assigned window contributes, giving \(Np(1-p)\le N/4\); the fixed identity eigenvalue is \(Nm\). This proves the sharp lower condition bound. Direct finite character sums give the complete spectra for odd and even \(N\); they establish that all non-antipodal windows must be balanced and that the even-order antipodal window obeys the exact displayed two-phase inequality. The equality constructions attain the bound for all \(N\ge3\). A standalone original-projector matrix computation checks the entire spectra for 32 configurations through \(N=10\). Numerical testing is not treated as an infinite proof. The source's general single-window Weyl Gram identity is credited, and each nonstandard optimizer reduction is explicitly proved in the result.

## Originality — PASS (provisional historical priority)
The general one-window Gabor projector spectral identity of Goldberger, Kang and Okoudjou is prior art. The published two-sparse multiwindow capacity finding already proves the qualitative minimum number \(\lfloor N/2\rfloor\), so that threshold is not claimed new. Neither published item determines the sharp condition number *over all minimal-window injective designs*, nor the full equality set including nonbalanced antipodal optimizers. The complete local Jacobian theorem for two-tap spectrograms has a different real signal-space derivative and cannot imply a sharp Hermitian operator-lifting design. Bartusel and Salanevich deal with signal phase retrieval; they do not determine this Hermitian stability optimization. The Han--Hu--Liu--Wang article is closest on multiwindow tomography and mentions a quantitative stability metric, but its full text was inaccessible after open-access attempts and an authorized institutional access attempt; this remains a genuine priority risk. The surviving new theorem is a precise sharp maximin classification, not the old general spectrum or old rank threshold. An equivalent differently phrased prior result remains possible.

## Mathematical value — PASS
Minimal support and minimum-window budget impose a natural, tight instrument-design problem: make an informationally complete set of the smallest possible number of two-sparse Gabor masks *as numerically stable as possible*. The theorem supplies a sharp full-matrix condition number in every dimension and classifies every optimizer, revealing an even-dimensional Nyquist phase/amplitude flexibility that is invisible to rank-only completeness criteria. The explicit results provide exact reproducible baselines for all-Hermitian tomography under homogeneous measurement noise. They do not assert optimality for arbitrary dense windows, nonlinear pure-state reconstruction, or shot-noise statistics.

## Closest literature and limits
[1] A. Goldberger, S. Kang, K. A. Okoudjou, arXiv:2106.01509v1, Theorem 2 (general one-window Gabor spectrum); inspected full text.

[2] D. Han, Q. Hu, R. Liu, H. Wang, DOI 10.1007/s43034-022-00208-2 (multiwindow quantum injectivity and a stability metric); abstract available, full text inaccessible.

[3] D. Bartusel, arXiv:2206.06729v1, Sections 4.2–4.3 (cyclic phase retrieval); inspected full text.

[4] P. Salanevich, arXiv:2307.00834v1, Introduction and Section II (pure-state Gabor phase retrieval); inspected full text.

[5] *Sharp operator-span capacity of two-sparse multi-window Gabor systems*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-operator-span-capacity-of-two-sparse-multi-window-gabor-sy--b553eeb756ed ; complete result and proof read, qualitative capacity only.

[6] *Exact local conditioning and optimal weighting for two-tap cyclic spectrograms*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-conditioning-and-optimal-weighting-for-two-tap-cycli--52be44b25eaa ; complete result and proof read, distinct local Jacobian problem.

The formulas depend on the specified normalizations, full labelled orbits, exactly two nonzero coordinates per unit window, and minimal cardinality. The finite checker is corroborative rather than exhaustive. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
