# Independent mathematical audit

## correctness

PASS

Commutation as partial maps makes the domain a union of full permutation cycles. Each active source cycle maps bijectively onto a cycle of the same length, with one of ell possible phases; different sources have different targets. A directed cycle of cycle labels prevents nilpotence regardless of its phases. A path on j labels vanishes at power j and contributes j−1 arrows, each of point rank ell. Including singleton paths, the j! linear orders on a j-set cancel the exponential generating-function denominator, giving exactly the stated factors. A forest on m labels with k paths of size at most h exists exactly for k ≤ m ≤ hk, proving the sharp support and including h=1. Unbounded ordered-block enumeration gives the stated Lah coefficients. A direct check on two 2-cycles gives 1+4T² at h=2; in the four-2-cycle example, the one-edge and two-disjoint-edge forests contribute 24T² and 48T⁴, and paths of three and four labels add 96T⁴ and 192T⁶ at their respective cutoffs. This recovers all stated sample strata. The frozen checker.py (lines 32–124, 127–170) supplies a separate executable replay specification; it was inspected, not executed. Finite checks do not substitute for the all-cycle-type proof.

## originality

FAIL

A distinct indexed result on nilpotent permutation centralizers gives exactly the joint rank/index law, exact-index subtraction, and unbounded rank counts on the same labeled objects, and goes on to prove a repeated-cycle reconstruction theorem. The submitted bounded-support display is not verbatim in its Finding, but is the immediate positive-coefficient support of that same law. This is demonstrated scientific overlap, not a determination of chronological priority.

## value

FAIL

An exact joint distribution for permutation centralizers is a natural statistic, in particular when mixed cycle lengths leave gaps in rank support. As submitted, that distribution is already available in equivalent indexed form, and the remaining cutoff-support display is just the feasible-size interval for the existing positive path decomposition followed by a weighted sum. The isolated numeric example and explicit extremum do not provide a separate research-level result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
