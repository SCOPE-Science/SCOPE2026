# Scientific review

## Correctness — PASS

The claim concerns exact completed matrix nonnegativity on finite pure-birth generators with arbitrary strictly positive transition rates. A direct, independent matrix-power checker verifies the analytic coefficient expansion at exact rational rates and steps. The proof gives necessary and sufficient local positivity conditions, a nonreentrant interval, a two-case universal comparison, an attained five-state lower extremizer, a limiting upper family, and a proof excluding inversion at smaller sizes. Its infinite statements are derived by algebra and inequalities, not the finite checks. The near-zero-rate upper family is an approximation, not an attained case.

## Originality — PASS (priority provisional)

The highest-overlap published mathematical result is the heterogeneous directed-cycle RK4 theorem (published-finding corpus, 2026-11-08), whose pair-cubic and four-rate-sum formulas closely match the present RK4 local ingredients. A homogeneous pure-birth RK4 state-count classification (published-finding corpus, 2026-10-12) covers the equal-rate subfamily. A separate RK3-versus-RK2 cycle result is also related. None of their inspected claims establishes the new sharp heterogeneous **RK4/RK3** two-sided ratio, the attained four-rate extremizer, the opposite sharp limiting family, or the minimum number of pure-birth states for an RK4 disadvantage. An exact componentwise root formula by itself does not settle this rate-uniform optimization. The stronger possibility that the comparison has appeared elsewhere under a different stability or positivity terminology has not been excluded by exhaustive library coverage.

## Value — PASS

The sharp universal constant proves that higher formal order can reduce admissible probability-preserving steps by almost 13% in a natural serial transport/decay chain, while another rate architecture can yield almost a 75% gain. Five-state minimality and the explicit optimal rate architecture distinguish a structural interaction of long-path jumps with departure-rate heterogeneity. The comparison informs selection of positivity-constrained time steppers; it is not an accuracy or efficiency comparison, and the local formulas are not separately valued as new.

## Limits and closest literature

The result concerns completed RK3/RK4 matrices only, with fixed positive rates and one absorbing end. The 2014 invariance-threshold literature gives general polynomial-root methodology, not this cross-order extremum. The 2021 graph-Laplacian positivity literature motivates the problem but studies modified positivity-preserving schemes. A heterogeneous directed-cycle RK4 classification covers essentially the same local polynomial ingredients; priority of the cross-method extremal comparison remains provisional. See `RESULT.md` and `AUDIT.json` for exact implications and evidence.

Self-review: passed. Independent audit: not yet performed.
