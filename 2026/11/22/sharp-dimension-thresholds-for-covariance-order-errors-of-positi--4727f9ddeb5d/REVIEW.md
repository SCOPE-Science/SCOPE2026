# Scientific assessment

## Correctness — PASS

The exact variation-of-constants covariance is a polynomial moment matrix on the controllable nilpotent chain. The signed error's entries are exactly the scalar quadrature errors of monomials divided by factorials. The first nonzero moment therefore appears only at the bottom-right entry in dimension \(m+1\), and the next dimension has an explicit strictly negative two-by-two principal minor. The published IF-SSPRK2/3 stage combinations reduce exactly to composite trapezoidal/Simpson quadrature when the source is constant. The resulting error magnitudes and Vandermonde rank identities have been checked with rational arithmetic in `verify.py` (56 dimension/panel cases); infinite quantifiers follow from the written proof, not from tests.

## Originality — PASS, with historical-priority qualifications

Comparison was by implication, not shared keywords. The original 2026 integrating-factor method establishes positive semidefiniteness and a norm estimate, not a finite-time first-missing-moment matrix-order classification. The published planar-rotation study establishes aliasing and rank recovery in dimension two, not nilpotent polynomial-moment Loewner-sign thresholds. A previously published mathematical finding establishes a stationary indefinite-error theorem for distinct positive decay rates and general positive quadratures, but does not imply exact one-sided rank-one errors and all-step indefinite phase boundaries for finite-time nilpotent chains. The separate universal trapezoid Loewner-order frontier concerns all-source one-step upper bounds for a fixed drift, not this dimension-sharp finite-horizon chain classification. Classical moment theory may contain an equivalent formulation not identified in the checked sources; no exhaustive priority certificate is claimed.

## Value — PASS

The theorem gives a natural **complete classification** of when positivity-preserving quadratures can also provide one-sided covariance error on a controllable chain. It distinguishes three practically different properties — positive semidefinite numerical output, positive definite numerical output, and sign-definite approximation error — with exact, dimension-dependent thresholds. The second-to-third order transition postpones loss of a one-sided matrix-error interpretation by one entire state dimension, and the finite-time failure persists at arbitrarily small steps. Such distinctions matter when covariance bounds, uncertainty enclosures and invertibility are required, rather than norm convergence alone.

## Sources and limitations

Primary source: Zhang, Lan and Jing, arXiv:2606.15703v1, Sections 2–3, especially the IF-SSPRK2/3 formulas and the positivity result. Related prior scientific records: “Exact covariance aliasing and a sharp ellipticity crossover for integrating-factor Lyapunov integrators”; “Exact Loewner-order frontier for covariance trapezoids in Lyapunov flows”; “Inertia of high-order positive quadrature stationary covariance errors” (distinct-rate stationary setting). Background: Trefethen (2022) on polynomial quadrature exactness; Berg–Szwarc (2014) on moment Hankel matrices. The general theorem assumes exact polynomial moments, and the named integrator conclusions assume a rank-one constant source on a nilpotent chain.

Self-review: passed. Independent audit: not yet performed.
