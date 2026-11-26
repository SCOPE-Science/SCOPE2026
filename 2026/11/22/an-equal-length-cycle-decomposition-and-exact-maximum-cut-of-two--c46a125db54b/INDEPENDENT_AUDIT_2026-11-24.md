# Independent mathematical audit

## correctness

PASS

Remove the closing base edge, leaving n-2 wrap lifts w_j=(0,j)--(j,n-1) outside the path token graph. The path Q_j first decreases the smaller coordinate from j to j-1 on column n-1, then decreases the larger from n-1 to j on row j-1, then decreases the smaller to zero on column j. These runs meet only at consecutive endpoints and have 1+(n-1-j)+(j-1)=n-1 edges. Every larger-coordinate edge in row a belongs to Q_{a+1}; each smaller-coordinate edge in column b<n-1 belongs to Q_b; in column n-1 the edge between smaller coordinates a,a+1 starts Q_{a+1}. All indicated indices are legal and the three classes cover path-token edges exactly once. Appending w_j closes each path into a simple n-cycle; for n=3 the construction is just the token triangle. Each n-cycle costs at least one uncut edge when n is odd. The even-index token parity colors exactly the path-edge lifts bichromatically, plus the wrap lifts precisely when n is even. Each base edge contributes n-2 lifts, with no duplicate because the symmetric difference determines the base edge. The cut reaches the cycle upper bound, and deleting the complement of a maximum cut is equivalent to optimal edge bipartization. The standalone verify.py is the replay path for finite checks through n=150 and cut exhaustion through n=7; inspected, not executed and not needed for this proof.

## originality

PASS

The parity-lift lower bound and its exactness for bipartite bases already cover the even case and predict the odd value only from below. The edge-disjoint simple-cycle partition and the resulting sharp odd upper bound are the surviving distinct claims under the comparisons made.

## value

PASS

The cycle is a basic nonbipartite test of whether the natural token parity lift is sharp. The explicit partition answers the missing odd upper bound by providing the exact transversal cost, and gives more structural information than the cut number alone: each cycle uses exactly one lift of every base edge. Thus the result has a concrete use independent of the already known even case and lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
