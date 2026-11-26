# Independent mathematical audit

## correctness

PASS

At depth t+max(a_i)+1 the present and absent all-marker subwords force the comparison word to contain exactly t ones and fix every zero gap, regardless of its presumed length or endpoint type. For the lower bound, a prefix ending with the i-th one is i-universal because it contains (01)^i, and appending zero first introduces 1^i0 at length i+1. The reverse suffix gives the corresponding t−i bound. The published repeated-letter and insertion identities therefore give sum of side distances t+a_i at a split of the i-th gap, including i=0 and t. The count follows by coefficient extraction from the positive bounded-composition polynomial; division by binom(n−t−1,t) and a fixed-t limit gives the simplex maximum law. Integrating the limiting tail yields the stated harmonic moments. An independent bounded replay checks 566 exact longest-gap insertion witnesses and 63 composition coefficients.

## originality

FAIL

The exact height expression is a direct specialization of the earlier explicit binary run reduction, not merely a quantity computable by a generic algorithm. Removing unit gaps by Lemma 5.4, then applying Lemma 5.5 to the remaining isolated markers and Lemma 5.3 to the resulting runs gives the stated maximum formula. The other two results amount to standard bounded composition enumeration and the longest-spacing distribution for that same maximum. No separate noncovered mathematical claim remains.

## value

FAIL

The positive-gap question is natural and the formula convenient, but the maximum-gap height is mechanically implied by the published exact run rules. The remaining fixed-length and asymptotic laws are routine maximum-part and longest-spacing identities without a further distinct height phenomenon. The result does not support a separate scientific contribution under this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
