# Scientific review

## Correctness
PASS. The exact conditional probability that all prescribed positions in a subset are fixed is the product of their target multiplicities divided by the falling factorial of the number of positions. This yields the complete probability-generating function, including zero multiplicities. A two-coordinate balancing step changes only the pair-product term of every elementary symmetric polynomial, giving a positive multiple of the second difference of a genuine auxiliary fixed-match distribution. This proves every convex-test inequality at every order, strictness for strictly convex tests, and the moment/extremal formulas. Exact enumeration and rational checks in `check.py` passed for all degree vectors of sizes two through six.

## Originality
PASS (provisional, with stated priority risk). The 2007 Hansen–Jaworski full article defines the exact conditional sampling model but analyzes cyclic-point, component-count and component-size distributions, not a fixed-point convex-order comparison under degree balancing. The 2008 local-properties paper concerns other local random-mapping variables. Stark (2026) studies a different repeated-reference-position match statistic, with nonconstant mean, and therefore does not imply the invariant-mean comparison here. A published Bernoulli balancing transport law has a similar second-difference pattern but uses independent Bernoulli indicators with replacement; our falling-factorial law differs and is not a Poisson-binomial special case. No searched record stated the all-degree convex-order classification or the exact stop-loss transfer for the random-mapping fixed-point statistic. Older multiset matching material could implicitly contain it; the result is not certified as historically first.

## Value
PASS. Fixed-point fluctuations in a directed functional graph with given indegrees are a natural structural probability question: heterogeneous target loads control the uncertainty of self-loops even though their conditional mean is unchanged. The result completely orders all indegree profiles by majorization for every convex loss, exhibits sharp minimal and maximal laws, and quantifies each unit smoothing operation. The statement is stronger than variance monotonicity or a single formula and can be used for finite degree-constrained random mapping comparisons without an asymptotic regime.

## Scope and limitations
The theorem requires uniform sampling conditional on the full degree vector and only concerns the number of self-loops, not the total cyclic population. An inaccessible or unindexed historical treatment of equivalent generalized rencontre laws remains a residual originality risk. Finite checks are not infinite proof; the accompanying all-order argument is the proof. No independent validation or external priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
