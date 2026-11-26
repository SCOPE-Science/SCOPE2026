# Independent mathematical audit

## correctness

PASS

A right factor from the full rank-(n−2) class has a single uniform top hook. In the middle row of the stack, only this edge can link distinct endpoints that propagate from the left diagram. Both of its endpoints must be among the r through endpoints for a loss of two; if an endpoint is in a bottom hook, tracing that hook either exits toward the bottom or stays internal, and no two through endpoints are joined. Thus the conditional loss probability is binom(r,2)/binom(n,2), including zero at minimum rank. Permuting the outer rows independently acts transitively on every rank stratum and preserves the convolution powers of the bi-invariant input measure. Consequently the mass of any prescribed diagram is its total rank mass divided by the stratum size, and multiplying by the number of ordered tuples produces the exact integer fibers. The stay-and-drop recurrence yields the displayed generating function with exponent k−1 because X1 is already present. At each successive rank above the minimum, the holding time is geometric on {1,2,…}, independent of previous holding times by the rank chain and the strong Markov property. Summing 1/[r(r−1)] by parity gives the harmonic difference for each parity; the empty n=3 sum is zero. At any fixed admissible ranks the scaled geometric vector converges to independent exponentials, and the remaining scaled expectation is bounded by the summable reciprocal-product tail, uniformly in n. Each limiting law has a finite mean and a positive finite variance, and their different means separate the two laws. Their CDFs are continuous and strictly increasing on the positive axis: any remainder can be small with positive probability by finite truncation and a mean bound, and an independent first exponential supplies positive mass on every intervening interval. Rank-uniformity at the absorbing rank gives the exact TV identity; the nondegenerate strictly varying survival profiles on each parity exclude cutoff. Independent replay: python3 /workspace/checks/frozen_math_checks.py 2 enumerates matchings and stacks them using union–find, validating every prescribed target including the unattainable top rank for n=3,4,5 up to lengths 3,4,2 respectively.

## originality

PASS

Credit the Brauer rank classes and class sizes to the structural literature, the two-sided invariance to the usual symmetry argument, and the exponential pair-merger rates to coalescent theory. The inspected sources do not give the same full-stratum random product transition and its consequent all-length prescribed-output and absorption laws. Related exact convolution results concern different monoids whose multiplication changes the transition probabilities or even the rank-uniformity conclusion.

## value

PASS

The first singular rank class is a natural generating stratum, and the count into an individual diagram is finer information than either stratum sizes or generation of lower ideals. The exact TV identity and the distinct even/odd quadratic profiles describe how the random product reaches its minimal ideal; they are more informative than a generic time bound or a small-degree calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
