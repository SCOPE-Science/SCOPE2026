# Self-review

## Correctness — PASS

The random updates are exactly two nilpotent-shear exponentials. Explicit expansion yields an isotropic averaged Gram matrix and a scaled-rotation mean matrix. Conditional expectation proves the exact \(n\)-step second moment; independence proves the mean formula. The phase boundary is a single-minimum elementary function, with strict convexity of the derivative sign function proving uniqueness of the interior minimum, two transverse roots above it, and all boundary cases. `check.py` independently enumerates small exact-rational products and checks the real numerical thresholds; finite checks are supportive rather than an infinite proof. The statement is only mean/mean-square, not pathwise.

## Originality — PASS with precedence risk

The closest application source, Veldman–Zuazua (arXiv:2109.13798, Example 1 and Remark 9), gives the identical per-cell selection rule but discusses fixed-final-time refinement and general exponential error bounds when sampled dissipativity fails; it does not report this exact fixed-step, all-horizon phase portrait. Sturman–Thiffeault (doi:10.1007/s00332-018-9497-3, §§2–4) analyze the underlying negative-shear products and generalized moments, but their inspected theorems give exponent bounds rather than the exact damped mean/mean-square threshold pair. Gog et al. (doi:10.1098/rspa.1999.0498, §§2–3) explicitly report nonnormal-shear instability windows under different switching, preventing any claim of first discovery of reentrant shear instability. The distinguishing statement is the sharp \(k/a\) interval where mean decay holds for every step but mean-square blowup occurs for some steps, with exact two-sided endpoints. General random-product second-moment methods may imply it indirectly; this is a residual publication-precedence risk, not evidence of novelty by failed search alone.

## Value — PASS

A strictly dissipative target and individually Hurwitz subgenerators appear innocuous, yet the unbiased independent one-choice-per-step method has a precisely characterized long-time mean-square failure invisible to the mean trajectory. The exact dimensionless thresholds locate the tuning regime where increasing the step size first destroys and later restores mean-square contraction, a meaningful stability-design boundary for non-dissipative randomized time splitting. It is limited to a planar balanced shear pair and exact subflows; no general-method stability assertion is made.

## Limitations and independent validation

All-time claims rely on exact matrix identities and calculus, not finite experiment. The general moment-radius equivalence and full historical priority need independent specialist checking. None is claimed here.

Self-review: passed. Independent audit: not yet performed.
