# Independent mathematical audit

## correctness

PASS

Every diameter-three tree has a central adjacent pair, and all other vertices are leaves adjacent to one of the pair. Anchor the Gram matrix at the first hub. Leaf contrasts each have eigenvalue q/2. In coordinates consisting of the unanchored hub and the two leaf totals, the hub pivot is 1, its couplings are (2−q)/2 and q/2, and the leaf block has diagonal 1−q/2+q/(2m), q/2+q/(2n), and off-diagonal (1+q−q^s)/2. The hub Schur complement has diagonal q(2+2/m−q)/4, q(2+2/n−q)/4 and off-diagonal −(2q^s−2−q²)/4. For S=m+n>2 the latter numerator F increases on [2,3] since s>19/12>3^(5/12)>3^(2−s); q√(A_m A_n) strictly decreases on [2,2+2/max(m,n)), by the logarithmic derivative bound 1/2−S/4<0. They cross once before the first diagonal can vanish. Rank is one in the complement at the crossing; above it the determinant first becomes negative, and for q>2+2/max(m,n) a diagonal is negative. Strict nesting supplies all p<1, with p=0 elementary. The path exception embeds in a line at p=2, and no higher power can satisfy the snowflake triangle inequality along three successive vertices. At q_0=2+2/S, midpoint convexity at 2,3,4 gives F(q_0)<2/S, while q_0√(A_m A_n)=2q_0/S; every root lies above q_0. There A_m A_n=(q−2)^2+[4−2S(q−2)]/(mn) strictly increases with mn while the admissible q interval only widens as the larger leaf count decreases. This proves strict balancing. Substitution at m=n and differentiation in 1/m give the stated asymptotic. Frozen code and notes were inspected, not run. The separately written `python /workspace/branches/independent_reproduction.py 3` passed 72 independent shortest-path Gram instances (all unordered splits for 2≤m+n≤17), including endpoint nullity and sample fixed-sum monotonicity; the proof does not extrapolate the sample.

## originality

FAIL

The distinct indexed Gaussian distance-power result on 2026/11/1 explicitly treats the same conditional negative semidefiniteness condition on all double stars, with the same reduced two-by-two matrix up to a scalar, strict fixed-sum product ordering, degeneracies and endpoint rank, balanced equation and asymptotic. The assigned scalar equation and its root bracket are direct consequences of its eigenvalue criterion and its proof of strict negative diagonals at the root. The rephrasing in negative-type and Hilbert terms adds no distinct mathematical classification.

## value

PASS

As mathematics, the exact classification of all unweighted diameter-three trees and the strict fixed-order balancing law give a meaningful extremal statement and distinguish endpoint rank from the path exception. This is not additional scientific content relative to the equivalent indexed theorem; that decisive failure is recorded under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
