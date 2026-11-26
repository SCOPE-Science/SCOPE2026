# Independent mathematical audit

## correctness

PASS

For any integer q≥2 the generalized binomial is a single integer power of q, so integrality is equivalent to a nonnegative exponent. At width m the exponent at zero-based position j is G(m)-d(m,j), with d(m,j) the number of gaps in (j,j+m]. Binomidness requires the initial length-L sum of d to be at least every shifted length-L sum. The Frobenius bound follows by reflecting nongaps in [0,F] into gaps; checking candidate gaps through 5 by rejecting any sum of two positive nongaps gives exactly the eight lists. When m≥F the sequence d(m,j) decreases; when L≥F the initial block contains the full nonnegative support; and when s≥F the shifted sum is zero. I independently checked the other 172 inequalities by updating the sliding gap-window sums. All pass, including the noninterlaced <3,4> case. Shapiro's Definition 4 and Proposition 9/Corollary 10 support the all-level and pyramid interpretation. In the finding, 'fails closure under adding two' means precisely failure of positive-index closure n∈S implies n+2∈S for n≥1, as required by the divisibility criterion; it is not a claim of closure of the finite gap set or a condition at n=0. Replay recipe: /workspace/branches/independent-math.md, section 3.

## originality

PASS

Seven genus-at-most-three indicator families fall under the earlier two-step theorem. Credit that overlap. The main distinct content is the all-width proof for <3,4>, the first exception to that theorem's positive-index hypothesis, and thus the completed initial-genus boundary. Neither the inspected ComboSum results nor the all-level examples for a different recurrence supply this case.

## value

PASS

The genus filtration gives a natural boundary in an existing all-level integrality question. The smallest semigroup outside the two-interlaced criterion is an actual positive instance at every width and index. The conductor reduction turns this bounded family into a result on infinitely many pyramid entries, rather than an empirical small-index extension or an exercise reproducing the seven covered cases. No claim about larger genus or the general ComboSum question is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
