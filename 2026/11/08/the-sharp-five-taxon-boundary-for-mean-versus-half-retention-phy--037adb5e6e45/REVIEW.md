# Scientific review: sharp mean-versus-half-retention phylogenetic risk

## Correctness — PASS

The argument is an exact probability-generating-function identity, not an inference from sampled outcomes. Direct enumeration of all sixteen four-leaf survivor configurations yields the base polynomial; common-root grafting multiplies the **difference** of distribution polynomials by \(qz+(1-q)z^2\) because both input trees share the same all-extinct probability. The coefficient sum at retention level \(n-1\) factors into the stated crossover law, and differentiating at one gives the expectation gap. The only two rooted full-binary shapes through four leaves have concordant half-retention and expectation rankings, while the five-leaf pair disagrees for \(0<q<1/3\). Exact finite enumeration for leaf counts four through eleven independently confirms the formulas. The proof applies to every integer \(n\ge4\); finite tests are supplementary.

## Originality — PASS, with historical-priority limits

Faller, Pardi and Steel's *Distribution of phylogenetic diversity under random extinction* (arXiv:0708.0425; 2008) is the essential primary precedent. It explicitly defines the distribution and critical-loss tail risk and provides a general exact computation algorithm; the ability to compute tail probabilities and the qualitative risk-versus-mean distinction are already known. Steel, Mimoto and Mooers (2007) provides a related expected-contribution formulation. The inspected literature does not state the sharp five-taxon half-retention exception or the exact infinite-family crossover formula. Earlier comparisons of the same four-leaf local tree rotation address mean and variance, not this event probability. The 2015 Faith paper was checked at abstract level only. Historical priority is provisional; no independent audit has occurred.

## Value — PASS

A half-retention target is an interpretable biodiversity risk criterion. The theorem shows exactly when expectation-based and threshold-based tree comparisons first disagree in a constrained homogeneous model. The \((n-4)/(n-2)\) crossover is a structural rule for arbitrarily large tree families and changes systematically with tree size, rather than an isolated numerical curiosity. The result responds to the published mean-versus-tail-risk question without asserting ecological field applicability beyond its explicit assumptions.

## Scope and residual risk

All lengths are unit **edge counts**, not equal root-to-tip temporal lengths. Extinction events are independent and identical; both trees have the same leaf count and initial rooted diversity; the result compares a particular family rather than classifying all possible trees. The underlying distribution algorithm and much of the motivation predate this result. Priority assessment is limited to inspected accessible evidence. Future independent literature and mathematical review is warranted.

Self-review: passed. Independent audit: not yet performed.
