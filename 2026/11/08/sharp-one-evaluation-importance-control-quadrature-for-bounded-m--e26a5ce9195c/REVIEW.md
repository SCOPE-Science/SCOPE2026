# Self-review

## Correctness — PASS
The estimator uses a normalized positive density and centered deterministic control, so it is unbiased for every integrable integrand. For all monotone bounded test functions the squared centered error is controlled by step functions; the formula for a unit step gives the constant variance \(V_*=(\coth(1)-1)/4\). A specifically constructed step prior makes a sharp universal lower bound: completing the square and applying Cauchy--Schwarz shows no competitor in the stated importance-control family can improve the constant, and equality uniquely determines the optimal density and control. The independent `check.py` exercised 79 finite numerical identities/checks, not substituted for proof.

## Originality — PASS, with limits
The closest primary full-text source, Basak--Bect--Vazquez, arXiv:2203.00423, proves \(1/12\) worst-case variance for uniform one-point control-variate sampling and studies stratification; it does not give a nonuniform-density minimax saddle. The new constant is strictly smaller. Comparisons also included Novak's arXiv:2307.06787 introduction/lower-bound discussion and nearby published-result searches. Broader publication precedence cannot be ruled out absolutely. The research makes no claim of minimax optimality among arbitrary single-evaluation algorithms.

## Value — PASS
This resolves a natural, explicitly defined one-evaluation estimator-design problem and improves a published benchmark by approximately 6.09%. It supplies both an implementable density and an exact least-favorable distribution of monotone step inputs. The restricted class matters: no practical gain is claimed when sampling cost, nonlinear estimators, or multiple evaluations change the comparison.

## Sources and residual limitations
Basak, Bect, Vazquez (2022), arXiv:2203.00423, Sections 3--5; Novak (2023), arXiv:2307.06787, inspected general discussion. Exact proof and reproducibility are provided in `RESULT.md` and `check.py`. Specialist precedence and unrestricted minimax optimality remain open outside the claim.

Self-review: passed. Independent audit: not yet performed.
