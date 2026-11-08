# Review of the power-productivity Shapley fairness law

## Correctness

**PASS.** All variables, allocation feasibility constraints and the cooperative max-game Shapley benchmark are defined. An explicit optimizer proves the minimum ratio is the sum of Shapley-to-productivity ratios, rather than merely bounding it. The known max-game Shapley decomposition is reconstructed directly; finite summation by parts gives the rank-ratio formula, beta-moment conditioning gives the finite-population mean, and exact finite telescoping supplies the three displayed special cases. The limiting curve follows from deterministic quantile-grid integration with both endpoint tails bounded; an empirical-CDF inequality and Borel--Cantelli transfer the limit to random uniforms, with expectation control giving convergence in mean. The standalone checker executed with 1,137 successful checks. Its finite tests support but do not prove the asymptotic theorem.

## Originality

**PASS, with residual publication-priority risk.** The closest source is Bei, Lu, Wu and Zhou (2026), which already contains fixed-profile Shapley formulas, the no-transfer approximation factor, and logarithmic worst-case guarantees. Those are used as premises, not represented as new results. The 2014 cooperative max-games paper independently covers fixed-weight Shapley computations. A comparison of the relevant full primary text, published index results and order-statistic/average-case searches found no equivalent statement for the iid power-family mean, the uniform second-order harmonic specialization, the pathwise power stochastic ordering or the digamma almost-sure limit. Some potentially relevant earlier stochastic max-game work may be unindexed; these searches do not establish absolute uniqueness.

## Mathematical value

**PASS.** A central practical question left unanswered by worst-case bounds is whether heterogeneous random productivity typically incurs a growing feasibility loss. The exact finite-n identity \(\mathbb E A_{n,1}=\sum_{j=1}^n j^{-2}\) and its almost-sure limit \(\pi^2/6\) show a bounded typical loss, while a complete power-family law quantifies systematic heterogeneity. Finite-n exact formulas for other powers and stochastic monotonicity make the result a useful calibration target in contribution-based resource allocation. It remains deliberately restricted to a single uncapped resource.

## Sources and limitations

Primary comparisons: https://arxiv.org/abs/2606.16743 (initial posting June 15, 2026), and https://ifmas.csc.liv.ac.uk/Proceedings/aamas2014/aamas/p29.pdf (AAMAS 2014). The exact statistics concern iid values from a specified distribution; unrelated fair-division guarantees cannot be inferred. No multigood or varying-exponent extension is claimed. Independent novelty and mathematical audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
