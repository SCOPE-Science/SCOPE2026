# Scientific review

## Correctness — PASS

The exact proof reduces any fixed-factor nonnegative matrix to its nonnegative velocity marginal and uses the spatial constant vector for converse realization. In degree one it computes the feasible interval from endpoint inequalities. In degree two it exhausts all extreme rays of the three-dimensional polyhedral sample cone, evaluates their two moments exactly, and proves the full finite-size formula. The strict rank hierarchy, continuum limits, and arbitrarily-close infeasible full-grid targets follow from explicit constructions. The dimension assumptions, nonnegative versus strict positivity, equal weights, and small-grid exception have been checked. Running the actual packaged checker yields 1,800 counted exact-rational cases, checked with explicit assertions for grid sizes 3 through 50; the unlimited-size result is analytical rather than experimental.

## Originality — PASS, with residual risk

The 2026 Kormann–Nazarov–Wen study introduces the mass/momentum/positivity core-matrix quadratic program and explicitly leaves feasibility under rank restrictions unresolved. The older robust conservative and LoMaC papers preserve kinetic moments through fixed or adapted basis modes but do not supply this nodewise-positive polynomial-factor feasibility classification. Searches for exact finite-grid degree-one and degree-two moment cones, adjacent-zero extreme rays, and the asymptotic \(1/3\) and \(1/\sqrt3\) limits did not identify a statement implying this combination. Basic convex-cone machinery is known, and unindexed equivalent elementary calculations remain possible. No general novelty of the extreme-ray method is asserted.

## Value — PASS

The sharp **if and only if** condition is a practical feasibility precheck for a natural fixed-velocity-factor specialization of a recently proposed correction algorithm, where a failed QP cannot be repaired by merely improving the optimizer. The explicit rank-two-to-rank-three attainable-momentum jump, fixed-grid values, and construction showing failure despite arbitrarily small approximation error explain why conservation-mode inclusion alone does not guarantee positivity. The statement is a complete natural classification with a concrete rank-enrichment diagnostic; no claim about global convergence or broad algorithmic speedup is needed.

## Literature and limitations

Closest source: Kormann–Nazarov–Wen (2026), section 4 equations (4.1)–(4.5) and conclusion. Supporting comparison: Einkemmer–Ostermann–Scalone (2022/2023) and Guo–Qiu (2024). The theorem is for equispaced one-dimensional velocity samples and low-degree fixed polynomial factors, not arbitrary Vlasov time integrators, arbitrary nonpolynomial bases, or a general feasibility algorithm. Scientific priority may require further specialist assessment.

Self-review: passed. Independent audit: not yet performed.
