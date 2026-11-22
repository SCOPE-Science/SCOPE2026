# Scientific review

## Correctness — PASS

Direct differentiation gives \(E''=p(1-p)[1-\gamma Q_q(p)]\), with \(Q_q(p)=-3(p-(1+q)/3)^2+(1-q+q^2)/3\). Its vertex lies strictly inside \((0,1)\); the endpoint signs ensure the entire negative-curvature set is exactly one probability interval. On \(0<\gamma<4\), positivity of \(1-\gamma p(1-p)\) proves unique stationary/global minimization, and coercivity establishes attainment. The exact witness was checked symbolically. The standalone verifier passed its exact algebraic and numerical checks. The proof, not the finite tests, establishes all quantified claims.

## Originality — PASS, qualified

The classical envelope identity and sufficient convexity analyses are not claimed as new. The candidate's exact \(q\)-dependent **necessary and sufficient** convexity frontier, its complete negative-curvature interval, and the surviving unique-minimizer window were compared with the publicly accessible portions of the 2026 motivating paper, the 2018 envelope theory, the 2026 author's envelope exposition, and semantic mathematical-record searches. No covering statement was found. The motivating preprint's full theorem/appendix text could not be verified, leaving nonzero historical-priority risk. Search noncoverage alone is not proof of novelty.

## Value — PASS

The example provides a complete natural sharp classification for the canonical one-logit Bernoulli cross-entropy, rather than an arbitrary numerical slice. It separates global envelope convexity from exactness of stationary/global minimizers **strictly inside** the standard proximal-gradient stepsize range, thereby clarifying when envelope-based online convex-optimization arguments need extra conditions. The target-balance phase transition and exact negative-curvature locus give usable analytic benchmarks. No multidimensional or algorithmic acceleration inference is made.

## Closest literature and limits

- Zhang, Gao, Udell (2026), arXiv:2609.10732: online-scaled splitting and envelope sufficient smoothness/convexity theory; only public abstract and accessible introduction were available for direct inspection, not complete theorem text.
- Giselsson and Fält (2018), DOI 10.1007/s10957-018-1328-z: general envelope definitions and structural properties, with quadratic convexity discussion; not the soft-target logistic sharp formula in examined material.
- Zhang (2026-06-10): exact envelope definition and stepsize context, not the claimed sharp logistic parameter classification.

Scope is unregularized one-dimensional soft-target logistic loss with \(0<q<1\); finite computations are auxiliary, not proofs of all parameters or historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
