# Scientific review

## Correctness — PASS

The precise deterministic Fourier-diagonalizable assumptions, invertible saddle system, and singular-vs-invertible preconditioning maps are defined in RESULT.md. Block multiplication yields the idempotent transformed matrix at zero leakage and a degree-two annihilating polynomial at positive leakage; a one-dimensional least-squares problem gives the all-order GMRES residual and frequencywise constrained least squares gives the flexible-update lower bound. The modewise conditioning formula follows from the trace and determinant of a two-by-two Gram matrix. The standalone `verify.py` reproduced the identities symbolically and across 160 complex Fourier instances, including 480 positive-leakage tests. No numerical test is used as a proof of any infinitely quantified statement.

## Originality — PASS (qualified)

The 2026 optical-preconditioning source provides the Type-2 Schur implementation and binary pupil but neither the exact hard-pupil idempotence/GMRES plateau nor the arbitrary fixed-mask flexible-search residual obstruction and zero-versus-positive-leakage characterization. Existing GMRES literature already establishes the general possibility of singular-preconditioner breakdown, and earlier saddle preconditioning theory exists. The contribution is the explicit and fully quantified application to this physically motivated Schur/Fourier structure, not the elementary principles in isolation. Direct source and related-paper statements were compared; the 2006 implicit-factorization article was available only at abstract level, so historical-priority risk remains.

## Value — PASS

A genuinely hard aperture can erase inverse-problem modes regardless of how small or large the positive Tikhonov regularization parameter is. The exact residual plateau and flexible geometric floor quantify what a rank-restricted preconditioning channel cannot repair, while the two-step leakage discontinuity explains the difference between exact solvability and numerical robustness. This is a source-motivated structural boundary relevant when interpreting idealized optical transfer simulations and safeguards for partial Fourier transmission; it does not claim failures of noisy physical implementations or universal practical algorithm performance.

## Closest literature and scope

- Drum et al., arXiv:2610.17275v1: motivating Type-2 optical Schur preconditioner and binary pupil.
- Gazzola et al., arXiv:1806.06599: low-rank GMRES preconditioning and known breakdown behavior; no identified Type-2 optical pupil formulas.
- di Serafino and Orban, arXiv:1910.02552: a different class of constraint-preconditioned saddle Krylov methods.
- Dollar et al., DOI 10.1137/05063427X: implicit-factorization saddle preconditioners, with full-text comparison unresolved.

Self-review: passed. Independent audit: not yet performed.
