# Scientific review

## Correctness — PASS

The exact difference and second-difference recurrences are derived algebraically from the classical four-point insertion formula. Their \(\ell^1\) coefficient bound \(q=1/2+4\omega<1\) establishes uniform convergence and an explicit geometric error bound. Interpolatory retained knots and lower semicontinuity prove that total variation of the continuous limit equals the limit of polygonal variations; translation invariance and absolutely convergent jump superposition establish the *sharp* operator norm and an attaining jump. The level-22 certificate contains exact integer sums, checked against independent low-level rational computations. No finite experiment is used as an infinite proof.

## Originality — PASS, qualified

The original 1987 article defines the four-point scheme and is available through its metadata but not the full paper. The October 1988 author report was materially inspected (rule, fundamental solution, convergence and difference machinery); it does not state the present sharp \(BV\) norm or numerical enclosure. The full 2008 arXiv paper of Amat–Dadourian–Liandrat studies stability in the supremum norm for nonlinear subdivision perturbations, rather than the present scalar total variation of the infinite limit. Closest indexed other research concerns spline orthoprojectors and finite/local refinement, which neither mathematically implies nor numerically determines the four-point subdivision limit coefficient. A hidden earlier BV analysis remains a historical-priority risk.

## Value — PASS

The cubic-reproducing four-point scheme is a classical interpolatory subdivision method. Its complete infinite-refinement total variation gain is a natural stability invariant relevant to ringing and response to step data; first-refinement measurements are not the correct limiting constant. The result supplies a sharp jump extremizer, a general-range computable tail certificate, and a rigorous sub-micro-unit enclosure of the classical cubic-tension value. It is intentionally narrower than a complete symbolic closed form but is a substantive quantitative endpoint stability result, not an arbitrary finite table entry.

## Limitations

Original 1987 paper full-text priority remains unresolved. The exact constant is characterized as a certified monotone limit, not by an elementary closed form. The bound is proved for real bi-infinite inputs and \(0\le\omega<1/8\), not for all tension parameters, arbitrary nonuniform grids, or nonlinear subdivision rules.

Self-review: passed. Independent audit: not yet performed.
