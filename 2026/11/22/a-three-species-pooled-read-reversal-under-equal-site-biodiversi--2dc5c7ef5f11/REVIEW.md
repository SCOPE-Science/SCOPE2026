# Independent mathematical audit

## correctness

PASS

In the stated independent, error-free four-read model, the separate design observes A for sure and its joint success is 2bc. The pooled absence probability for B or C of first-site frequency u is (1-u/2)^4 > (1-u)^2; pooled absence of A is also positive. Independent inclusion–exclusion gives pooled joint success 12 times the product of its three label probabilities, or 3(1+a)bc/2. Thus the difference is bc(3a-1)/2, with the stated tie and strict signs on the open simplex. With at most two exhaustive labels and at least one read, joint detection is determined by the marginals, so the three-label example is minimal. The rarer of B and C gives the stated exponential lower bound on pooled failure, eventually exceeding the separate union bound. Conditional on the binomial site count, the pooled label multiset has the deterministic-allocation law, so pooling cannot beat the maximum over deterministic allocations; for three first-site reads plus one second-site read, joint completion is exactly 3bc(1+a). The supplied checker was inspected, not executed. The multinomial and inclusion–exclusion formulas can be replayed from RESULT.md, lines 28–72; the finite grid is not the basis of the continuum result.

## originality

PASS

The supported distinct claim is the sharp equal-depth reversal between per-label marginal dominance and complete inventory, including its threshold and minimal label count. Neither the inspected published sampling comparison nor the closest distinct catalogue comparison supplies this implication or a stronger comparison including it. This is a bounded assessment, not a priority certification.

## value

PASS

This gives a minimal, parameter-sharp counterexample to inferring the probability of a complete inventory from uniformly better single-taxon detection. That distinction matters when choosing between expected richness and complete coverage, and the four-read boundary makes a concrete test case for sampling-design reasoning. The result is not a laboratory recommendation: it needs equal effective mixture weights and idealized independent reads, and optimal deterministic allocation is not beaten.

The dated certificate retains the supplied scientific assessment, sources and limitations.
