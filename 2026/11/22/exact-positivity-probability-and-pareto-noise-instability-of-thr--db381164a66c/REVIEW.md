# Self-review

## Correctness — PASS

The exact natural cubic spline area identity follows by integrating each cubic and using its two zero-end second derivatives. Differentiating this identity with respect to the three ordinates gives the explicit weights; the central weight is strictly positive and the outer sign boundaries are two disjoint algebraic intervals. The ordered-uniform three-point density gives a uniform normalized middle-gap coordinate. Solving the resulting one-dimensional weight-norm inequality yields the full survival function, not merely an asymptotic bound. The positive leading singularity of the weight-square sum and Tonelli's theorem prove both divergent Gaussian-noise moments. The standalone symbolic and exact-rational checks confirm the algebra and normalizations. No computational experiment is substituted for the continuum proof.

## Originality — PASS (subject to historical priority review)

The nearest related published studies establish positivity criteria for polynomial-exact and Bayesian-kernel quadrature weights (van den Bos–Sanderse 2019; Karvonen–Kanagawa–Särkkä 2018), cubic Hermite shape preservation (Aràndiga–Baeza–Yáñez 2021), and Gaussian rules for a different \(C^1\) cubic-spline space (Ait-Haddou–Bartoň–Calo 2014). None of the inspected relevant text provides the same **three-knot natural cubic cardinal-integral rule**, its exact \(4-\sqrt{13}\) positivity probability, or the survival law. Related published findings on pointwise natural-spline overshoot and heavy tails of random polynomial or affine-exact quadrature were also compared at the level of their functionals and sampling models. Pointwise overshoot does not settle the integrated weight signs; polynomial or affine-exact weights are not the natural-spline coefficients. Targeted searches did not reveal an exact prior theorem, but search coverage cannot establish uniqueness. Residual historical risk remains for older spline-integration literature or unpublished equivalent analyses.

## Value — PASS

The theorem identifies the **first nontrivial natural-spline knot count** where nodal integral weights can turn negative: the two-knot natural spline is affine and yields weights \(1/2,1/2\). For the next count, it determines not merely a counterexample but the exact probability of positivity, full distribution of worst-case bounded nodal-error amplification, and an infinite unconditional absolute-noise risk for random unstratified knots. This gives a motivated, precise warning about using random unconstrained knot positions for numerical integration and distinguishes positivity of a spline curve from positivity of its integrated sample coefficients. The exact one-dimensional law is valuable independently of any unproved extension to more knots.

## Limits and closest literature

The integral is averaged over the random hull, not over a fixed integration interval. Gaussian-noise divergence concerns measurement error and does not describe noiseless smooth-function approximation error. The result depends on independent uniform knots, the three-knot natural boundary condition, and normalization by the observed span. The 2014 Gaussian spline-quadrature work concerns a different spline space and optimized quadrature nodes; the 2018 Bayesian and 2019 polynomial interpolatory constructions have different defining equations. The targeted comparison does not replace independent priority research.

Self-review: passed. Independent audit: not yet performed.
