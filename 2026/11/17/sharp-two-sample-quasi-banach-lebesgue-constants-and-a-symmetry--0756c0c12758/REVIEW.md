# Scientific review

## Correctness — PASS

The two-node inverse Gram matrix is explicit and invertible for every positive separation. On the inner segment the coefficient cost is a symmetric sum of two positive hyperbolic-sine powers; outside it is at most one. The strictly convex log-ratio argument proves that its stationary points have either one global midpoint maximum or exactly two symmetric off-center maxima, with the sharp threshold \(2\operatorname{arctanh}\sqrt{1-p}\). Taylor expansion at the degeneracy and direct large-gap asymptotics prove the nontrivial exponents and coefficients. The \(p=1/2\) stationary relation factors into midpoint versus the product-one branch. The included standard-library checker passed 16165 supplementary finite assertions. Its finite comparisons do not establish the universal statements; those follow from the analytic proof.

## Originality — PASS, with residual priority risk

The closest primary paper is Wang–Song–Zhang, arXiv:2611.08032 (initial posting 2026-11-05). Its Sections 3–4 were inspected for the generalized Lebesgue definition, sharp representer-penalty correspondence, exponential-kernel bounds and qualitative two-point example. The general factor and qualitative failure are **prior art**; the new result specifies the all-separation/all-exponent exact factor, all center maximizers, symmetry-breaking threshold, onset and large-gap asymptotics, and the full half-power branch. The ordinary cardinal Matérn results of Bejancu (arXiv:2009.00711) and published records about exponential Gram condition numbers or two-point circular-arc polynomial interpolation involve different invariants. Claim/alias, stronger-coverage, equivalent-form and exact-table searches did not establish an implication covering this result. Related summaries are not whole-paper exclusions. Older equivalent hyperbolic or quasi-Banach forms may still exist.

## Mathematical value — PASS

The motivating generalized Lebesgue factor controls the cost of insisting that nonconvex sparse kernel interpolation use only the sampled centers. A precise worst-center location is structurally important for this factor: at close spacing the midpoint is worst, whereas at wider spacing a pair of asymmetric maximizers appears and approaches the two sample sites. The result resolves a complete natural two-site model and its quantitative transition without asserting a general multi-site theorem.

## Scope and limitations

The sharp classification is confined to two sites of the one-dimensional exponential covariance kernel, with fixed \(0<p<1\). The original general representer criterion is credited to prior literature. The explicit limits are not uniform in the endpoint exponents. Some classical sources and published neighboring findings were not inspected in full, so unconditional publication priority is not asserted. Only supplementary finite diagnostics were executed; independent validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
