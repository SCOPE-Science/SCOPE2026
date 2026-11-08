# Scientific review: distinct Lyndon-factor distribution of three-marker binary words

## Correctness — PASS

The result uses the standard proper-suffix definition of a Lyndon word on the ordered binary alphabet. The independent factor classification distinguishes one-marker, two-marker and three-marker substrings and treats the indicator case where the initial zero run of a three-marker factor equals the first internal zero run but exceeds the second. Six disjoint order chambers give a rational generating function for the full count distribution; a correction handles the zero-free word. Normalized weak compositions converge to a uniform Dirichlet simplex, and the conditional order-chamber transformation proves the stated mixture and moments.

The proof's quantifiers cover every length with precisely three ones and no assumptions on the four zero gaps. The bundled verification independently enumerates all eligible words through length 21, cross-checks the generating function to length 70 and verifies moments with exact fractions. This is corroboration only, not an inference from finite cases to the infinite theorem.

## Originality — PASS (qualified)

K. Saari's *Lyndon Words and Fibonacci Numbers* (arXiv:1207.4233, first publicly posted July 17, 2012) studies lower bounds for Lyndon words, particularly Fibonacci Lyndon words, and the factor complexity of infinite sequences. Glen, Simpson and Smyth's *Counting Lyndon Factors* (arXiv:1701.00928, first publicly posted January 4, 2017) gives the unrestricted maximum and uniform-all-words expectations. Sections 2 and 4 were examined, not merely their titles or abstracts. Neither examined source states the fixed-three-one full multiplicity distribution or its Dirichlet limit law. The familiar ordered-block maximizer is already covered by the general maximum result and is not claimed as new.

Queries for fixed composition, three markers, full bivariate distributions, rational enumerators and equivalent terminology did not identify a covering result. This absence is a bounded priority assessment, not proof of global uniqueness. Unindexed or unpublished equivalent specializations remain a risk. No exact sequence lookup was treated as proof of novelty.

## Value — PASS

The full distribution addresses a natural conditioned version of Lyndon-factor complexity rather than merely recomputing an unrestricted maximum. At weight three, different internal zero-gap orders interact, including a genuine tie/strict-inequality correction that vanishes in continuous limits but affects exact integer counts. The rational bivariate series determines every finite-length probability mass without new factor enumeration; the six-component mixture explains nonconcentration of the normalized count and yields exact first two asymptotic moments. This is a complete classification of a naturally defined family, relevant to fixed-composition string models and distinct-substring complexity.

## Scope and residual risk

The result concerns distinct contiguous Lyndon factors, not all occurrences, not the Chen–Fox–Lyndon decomposition, and not other weights or alphabet orders. The inspected literature covers very general Lyndon-factor questions but might not exhaust specialized composition-conditioned work. The probability law is restricted to uniformly sampled weight-three words. A separate independent audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
