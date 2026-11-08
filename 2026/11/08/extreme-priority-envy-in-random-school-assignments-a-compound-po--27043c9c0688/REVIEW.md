# Scientific review: extreme-priority envy cluster law

## Correctness

**PASS.** The event is defined at the exact rank threshold with strict inequalities, and all preferences, priorities, and the assignment mechanism are quantified. For each ordered pair, the exact event probability is the product of \(1/2\) and \(h(h-1)/(2n(n-1))\). A two-critical-school collision bound of \((h-1)^4/(2n)\) justifies coupling the correlated comparisons to independent school-specific binomial marks. Independent category counts converge to unit-rate Poisson counts, giving the complete generating function, the zero-event probability and the maximum-gap tail. The variance formula follows from binomial cluster moments and uniform exponential tails. The standalone finite verifier passed 93,328 exhaustive and 36,000 seeded comparisons. Remaining risk: the result only applies when priorities are independent across schools and the matching is exogenous.

## Originality

**PASS, with access risk.** The most closely related source is Hamdan (arXiv:2609.07682, 2026), whose available abstract introduces priority-gap severity, mechanisms, and simulations but does not state a compound-Poisson law for fixed exogenous matchings. The full text could not be accessed, so hidden equivalent material remains possible. Shen et al. (2023), inspected through their full accessible AAMAS PDF at the model and fairness definitions, instead investigate stochastic/likelihood envy with a single shared random priority. Ortega et al. (arXiv:2603.23385) analyze counts of unenvied agents for endogenous DA and RSD outcomes; their accessible abstract is not a stronger covering theorem. A targeted search of matching-market and compound-Poisson terms, published research records, and recoverable earlier in-scope claims yielded no direct implication. Search non-detection is not proof of absolute novelty.

## Value

**PASS.** Very justified envy is motivated by fairness restrictions on large matching markets. The theorem solves the baseline question of how many *extreme-severity* violations persist even when a fixed matching is independent of all preferences and priorities; it gives both the law of pair counts and the probability of a fully violation-free assignment. The non-Poisson cluster structure is substantive: at \(h=3\), the expected pair count is \(3/2\), but the probability of zero pairs approaches \(e^{-5/4}\), not the naive independent-event value \(e^{-3/2}\). The distribution of the largest rank advantage follows as an exact asymptotic tail. The result cannot be generalized to endogenous mechanisms without new work.

Self-review: passed. Independent audit: not yet performed.
