# Self-review

## Correctness — PASS

The Gram matrix for the origin and its signed coordinate orbits reduces rigorously to two linear equations with Schur complement \((1-s^2)^2>0\). The resulting outer weight is positive for the entire exact parameter domain; the central sign is controlled by \(dF_u(s)\). Strict monotonicity is proved analytically by comparing \(\beta/(1-e^{-\beta x})\) with \(2\coth x\). Correct endpoint behavior proves a unique crossing and exact boundary. Small-\(s\) expansion proves the dimension limit, and a separate flat-kernel expansion reproduces polynomial moment weights. The included independent full-matrix numerical solver and formula checks pass 3,774 assertions. NumPy checks are illustrative, not an infinite-domain proof.

## Originality — PASS (qualified)

The closest prior, Karvonen--Särkkä (2018), explicitly analyzes this exact symmetric node set with Gaussian kernel and standard Gaussian measure, provides a general two-orbit linear solve, and observes negative central weight in large dimension. Those facts are explicitly conceded. The present specific mathematical advance is a necessary-and-sufficient nonnegative-weight radius for all \(d,\ell,\tau\), unique sign transition without reentry, and dimension-asymptotic constant. The prior paper does not state or prove this explicit sharp phase diagram or asymptotic. Särkkä et al. (2015) treat related sigma-point rules and kernel quadrature without this sign cutoff; Karvonen et al. (2019) focus principally on one-dimensional positivity. Search of related abstracted research records returned a one-dimensional three-node uniform-target Gaussian-kernel result, not the multivariate Gaussian-target orbit result. The prior general matrix-inversion framework makes the weight formulas an accessible specialization; this narrows the novelty and remains a risk. Unindexed equivalent derivations could further limit priority.

## Value — PASS

The all-parameter classification resolves the exact design-scale needed to avoid a sign instability explicitly recognized in prior literature. The \(\sqrt{\log d}\) law supplies a quantitative high-dimensional design guideline, and the sharp zero boundary distinguishes truly nonnegative quadrature from negative-weight extrapolation. This is a natural complete positivity classification for an established sparse sigma-point architecture, not an arbitrary numeric slice. It does not assert optimal accuracy or improved conditioning.

## Scientific limits and related work

The conclusion assumes isotropic Gaussian measure and kernel, identical axis radius, no nugget and exact arithmetic. The strongest coverage risk is section 4.3 of the 2018 work, whose general orbit reduction directly supplies an implicit weight solve; the new claims are the rigorously unique positivity frontier and its asymptotic rather than first disclosure of the setup or negative weights. There is no independent validation and bibliographic priority remains subject to specialized external review.

Self-review: passed. Independent audit: not yet performed.
