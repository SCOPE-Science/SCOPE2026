# Independent mathematical audit

## correctness

PASS

For a uniform labelled GL_n matrix at fixed q, multiplying an ideal vector by e_i puts e_i^2 in the ideal whenever its i-coordinate is nonzero. The squares are independent, so the ideal equals the coordinate span of its union of supports. The zero-cut block count is |GL_r||GL_(n-r)| q^{r(n-r)}. For r=1 or n-1 the exact probability is (q-1)/(q^n-1). Two of the 2n row/column cut events impose at least 2n-3 distinct zeros. Conditioning an independent uniform matrix on invertibility costs at most the reciprocal of the positive infinite product of (1-q^{-j}). Bonferroni gives the stated singleton-union error. In the middle-cut sum the successive term ratio tends uniformly to zero up to n/3; beyond n/3 through n/2 the sum is bounded by 2^n q^{-2n^2/9+O(n)}. The r=2 term dominates this error bound by symmetry. Row-only and column-only masses are each asymptotic to n(q-1)/(q^n-1); the intersection is negligible, not identically empty. Reviewer replay `python3 /workspace/review-evidence/1.py` verified every fixed cut at q=2, n=2,3,4 and the nonsimple counts 3, 88, 8502 by independent enumeration of ordered row bases. It tests neither all ideals as subspaces nor the asymptotic; those follow from the proof. The ensemble is not uniform over isomorphism classes.

## originality

FAIL

A distinct checked catalogue result covers the headline law with a stronger uniform estimate and structural witness. Its coefficient and cut formula are identical, and its unique one-vertex mechanism logically implies the stated equal directional weights by transpose symmetry. This is an equivalent-coverage decision, not a historical priority determination or a finding of impropriety. The elementary ideal dictionary is not a separately substantial surviving claim.

## value

PASS

As mathematics, the conditioning-dependent coefficient and concentration on one-vertex ideal mechanisms give a useful exact benchmark for random labelled perfect algebras that independent-edge heuristics miss. The isolated ideal dictionary or a replay of small labelled counts would not independently justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
