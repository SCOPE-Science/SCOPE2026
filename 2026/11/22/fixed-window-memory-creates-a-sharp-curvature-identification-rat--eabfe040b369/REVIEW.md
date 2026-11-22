# Scientific review

## Correctness — PASS

The algorithm is exactly the estimator defined in equation (3) of Hu–Pollock–Xue–Zhu on the specified invariant lower-eigenmode starting ray, including the short-window startup. Every multiplier is positive and stays in a proved invariant interval. A geometric-mean min/max estimate gives blockwise global contraction to the unique fixed point. Explicit differentiation yields an \(\ell\)-lag companion matrix, whose determinant and \(\ell\)-step sup-norm bound squeeze the spectral radius; complex-conjugate roots give the exact two-window crossover. The embedded checker separately exercises finite examples and does not purport to certify an infinite argument.

## Originality — PASS, historically qualified

The source gives a general optimization-error guarantee and a one-window rate analysis, while presenting several other windows as empirical choices. It does not derive the fixed-\(\ell\) feedback companion, the \(a=1/2\) reversal or the \(\ell\to\infty\) local spectral limit. The closest published mathematical record [2] analyzes a one-window recurrence rather than any fixed history length beyond one. Multiple searches using window length, memory, geometric residual ratios, companion spectral roots, and aliases found no implication covering the final claim. The published record [2] was only available in summary, and classical delay-recurrence sources can contain related methods, so priority is not independently established.

## Value — PASS

Finite smoothing-window length is a genuine design parameter of the published method. The same optimizer and asymptotic iterate rate conceal a sharp change in feedback stabilization, including a one-to-two-window phase reversal and arbitrarily slow *local parameter identification* as a fixed memory length grows. This distinguishes optimization accuracy from parameter-calibration responsiveness and gives a reproducible test case for adaptive-window choices; it is not presented as a general failure of the optimizer.

## Scope and evidence

Primary source: Hu, Pollock, Xue and Zhu, arXiv:2602.13620v1, Sections 2.1 and 3.1 (algorithm, geometric estimator, general convergence and numerical comparisons). Closest published comparison: *Exact alternating identification on two endpoint spectra* (2026-10-04), publicly indexed summary. Residual risks: invariant-ray restriction; generic delayed-recursion literature not exhaustively searchable; full text of closest published comparison inaccessible. Independent validation remains open.

Self-review: passed. Independent audit: not yet performed.
