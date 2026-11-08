# Scientific review

## Correctness — PASS
The law of total variance gives a sharp decomposition into within-arm and between-arm spread. The within-arm variance is maximized exactly by straight unit-slope paths; convexity of the between-arm functional then forces arm means to interval endpoints. Anchored Lipschitz polytopes have integral vertices, giving an exact finite maximization. Leading sign-imbalance gaps are at least \(1/n^2\), and integer covariance gaps are also at least \(1/n^2\); the explicit diameter inequalities prove eventual stabilization. The transport identity follows by finite Kantorovich duality. The strict sorted-gap argument proves unique path equality in the upper transport bound. Exact rational code checks the finite instances stated in VERIFICATION.md, not the universal theorem.

## Originality — PASS, with residual risk
Comparison of actual implications rather than titles: arXiv:0902.1156 discusses random graph spread, integral extrema, and random pendant forests but does not derive a deterministic uniform-tail variance reduction or the balanced transport slope. Sammer–Tetali's 2009 transportation treatment covers discrete tori and concentration, not these rooted products. Earlier exact mathematical claims concern double stars, lollipops, fans/wheels and related distinct families; none states the all-core construction or asymptotic path uniqueness. Targeted searches for pendant-path corona spread, balanced transport slopes and mathematical aliases returned no dominating equivalent claim. This is not a uniqueness proof over all published mathematics; Barthe–O'Connell was available only at abstract level and other unindexed results may exist.

## Mathematical value — PASS
The transformation is canonical (one path attached to every original vertex), the result is uniform over every connected core, and the eventual quadratic has an interpretable optimal-transport coefficient. The new sharp extremal characterization singles out paths among **all** connected cores of fixed order and provides a finite, if conservative, valid cutoff. It is not simply a fixed-size numerical table or an instance of Cartesian-product spread tensorization; an arbitrary graph of these rooted paths is not a Cartesian product.

## Limitations
No claims about unequal path lengths, weighted cores, or optimality of the stated cutoff. The classical existence of integral Lipschitz extrema and transport duality are explicitly acknowledged rather than presented as new.

Self-review: passed. Independent audit: not yet performed.
