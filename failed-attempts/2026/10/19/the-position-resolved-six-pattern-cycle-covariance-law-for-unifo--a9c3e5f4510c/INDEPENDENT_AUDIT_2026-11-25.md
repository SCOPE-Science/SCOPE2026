# Independent mathematical audit

## correctness

PASS

A prescribed injective partial mapping gives disjoint directed paths and closed cycles. Each prescribed edge reduces the number of path components by one, so in a three-position window there are n-3 paths, including isolated vertices. The remaining arrows match tails to heads uniformly; the completed cycle count has mean H_(n-3) plus the forced closed-cycle count, with H_0=0. There are (n)_3/6 equiprobable triples per pattern. A fixed point at x of rank r contributes binom(x-1,r-1) binom(n-x,3-r); a transposition fixes two ranks and leaves the last rank in the appropriate interval; 231 and 312 each contribute one three-cycle. Adding these counts with multiplicity and subtracting (n)_3(H_n-H_(n-3))=3n²-6n+2 after normalization yields the six claimed affine formulas. The constant nonzero 123 row and nonconstant 132 row give rank two when there are at least two positions; the single column at n=3 is nonzero. The two pooled pairs each have numerator -4. Independent disjoint-set counting of cycles and comparison-based ranks reproduced all 126 cells for n=3..8 with integer arithmetic.

## originality

FAIL

The earlier indexed Resultary finding 5a13f0bb8311 is an aggregate theorem in its headline, but its actual proof supplies the requisite stronger position-specific ingredients. It explicitly gives the conditional cycle mean for every fixed image triple at t, the fixed-point contribution by position and rank, every nonzero two-cycle contribution already as a function of t for each pair of positions and pattern, and the two exact three-cycle assignments. Keep t fixed instead of summing over it: the normalized local covariance is six times the sum of those supplied counts minus 3n²-6n+2. For example, 132 has the supplied fixed-point sum W1(t)+W3(t+1)+W2(t+2), transposition count t and no three-cycle; expansion gives 9n-14-12t. The same direct substitution works in all six cells and the rank assertion is elementary from those entries. This is coverage by the prior equations and case evaluation, not an inference from the aggregate vector alone or from title similarity. Two other indexed findings explicitly give the same positional table, but no priority or independent authorship is inferred from their catalogue dates.

## value

FAIL

The positional contrast is a natural statistic, but the exact invariant here is obtained by retaining the position in an existing explicit local calculation. The rank observation and pooled cancellations are direct algebra on those already computable entries, with no residual substantive gap in the frozen claim. The table can be convenient as exposition, not a separate worthwhile exact result under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
