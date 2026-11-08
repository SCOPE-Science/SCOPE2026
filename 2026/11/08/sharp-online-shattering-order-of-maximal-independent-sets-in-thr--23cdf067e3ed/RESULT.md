# Sharp online-shattering order of maximal independent sets in threshold graphs

## Finding

Let \(G\) be a nonempty finite threshold graph and let \(\mathcal M(G)\) be the concept class of its inclusion-maximal independent vertex sets, with a binary membership query at any vertex. For every integer \(h\ge1\), the smallest order of a threshold graph satisfying \(\operatorname{Ldim}(\mathcal M(G))\ge h\) is
\[
N_h=3\cdot 2^{h-1}-1.
\]
At this minimum order there is exactly one threshold graph up to isomorphism: its creation word, with the first vertex marked isolated, is
\[
0\,1\,(0\,11)^{2^{h-1}-1}.
\]
Every non-edgeless threshold graph satisfies \(\operatorname{VCdim}(\mathcal M(G))=1\), while an edgeless graph has both dimensions zero. Therefore the maximum Littlestone dimension among threshold graphs on \(n\ge2\) vertices is exactly
\[
1+\left\lfloor\log_2\!\left(\frac{n+1}{3}\right)\right\rfloor.
\]
An exact interval recurrence below computes the Littlestone dimension of every threshold graph with a creation word of length \(n\) in \(O(n^3)\) arithmetic operations.

## Assumptions and scope

Graphs are finite, simple, nonempty and undirected. A threshold creation word \(w=w_0\ldots w_{n-1}\) starts with \(w_0=0\); for \(i>0\), a zero adds a vertex adjacent to none of its predecessors, while a one adds a vertex adjacent to all predecessors. Such creation words represent exactly threshold graphs. The initial zero is a convention for the one-vertex base, not a restriction. Set \(d=|\{i:w_i=1\}|\); number the one-vertices \(u_1,\ldots,u_d\) by their creation order, and put \(u_0\) for the hypothesis consisting of all zero-vertices.

For \(j\ge1\), let \(M_j\) consist of \(u_j\) together with all zero-vertices created strictly after \(u_j\); let \(M_0\) consist of all zero-vertices. A hypothesis is the binary incidence vector of one of these sets. A support is VC-shattered when all its labelings are realized by hypotheses. Littlestone dimension is the largest depth of a complete adaptive binary mistake tree whose paths are realizable by hypotheses. When \(d=0\), the only hypothesis is the entire vertex set.

For a zero-vertex created after exactly \(j\) one-vertices, its membership query answers one on precisely \(M_0,\ldots,M_j\); a query at \(u_j\) answers one only on \(M_j\). Define the set of available proper prefix cuts
\[
Q=\{j+1: \text{some zero is created after exactly }j\text{ ones}\}\cap\{1,\ldots,d\}.
\]
In particular \(1\in Q\), induced by the initial zero. Write \(R(a,b)\) for the Littlestone rank of the subfamily \(\{M_a,\ldots,M_b\}\), where \(0\le a\le b\le d\).

## Proof

**1. Concept parametrization.** The one-vertices form a clique. An independent set contains at most one of them. If it contains \(u_j\), maximality forces the inclusion of every later zero, and forbids every earlier zero (which is adjacent to \(u_j\)). Without a one-vertex, maximality forces every zero, and any one-vertex is adjacent to the initial zero. Consequently the complete list of distinct maximal independent sets is \(M_0,\ldots,M_d\), exactly as defined. This classification agrees with, but is not claimed to improve, the established maximal-independent-set enumeration for threshold graphs.

**2. VC dimension.** Two one-vertices can never both be positive. The positive sets of two zero-vertex queries are nested initial intervals of the ordered hypotheses, so their two mixed patterns cannot both occur. For a one-vertex \(u_j\) and any zero-vertex \(v\), membership of \(v\) is fixed whenever membership of \(u_j\) is one; thus one of the joint labels is missing. No pair is shattered. If \(d\ge1\), membership in \(u_1\) is nonconstant, so the VC dimension is exactly one. If \(d=0\), it is zero.

**3. Exact online recurrence.** The initial value is \(R(a,a)=0\). For \(a<b\),
\[
R(a,b)=\max\!\left\{1,\ \max_{\substack{k\in Q\\a<k\le b}}
 \left(1+\min\{R(a,k-1),R(k,b)\}\right)\right\},
\]
where the inner maximum over an empty set is ignored. Indeed, any two distinct hypotheses in an interval are separated by some query at a one-vertex, so rank is at least one. A one-vertex query has at most one positive hypothesis and hence cannot be the root of a complete mistake tree of depth at least two. Every root giving rank at least two is therefore a zero-vertex query, whose two nonempty branches are precisely the consecutive subintervals cut at some \(k\in Q\). The standard rank recursion proves both the upper and lower directions. Enumerating all intervals in increasing size and scanning \(Q\) takes \(O(d^3)\) operations.

**4. Sharp vertex lower bound.** Suppose the full concept class has an adaptive complete mistake tree of depth \(h\). Its \(2^h\) leaves require distinct hypotheses, so \(d+1\ge2^h\), i.e. at least \(2^h-1\) one-vertices. Consider the first \(h-1\) levels of the tree. Every query there has two positive-depth children and thus cannot query a one-vertex. Every such query is a proper prefix cut of the ordered hypotheses. The \(2^{h-1}-1\) corresponding cut positions are all distinct: distinct internal nodes at the same or preceding levels partition disjoint consecutive intervals, and the same cut cannot separate two distinct such intervals. Moreover, none is the initial cut \(k=1\): within any interval, that cut is constant or isolates only \(M_0\), leaving a branch of rank zero, which is impossible above the final level. Therefore at least \(2^{h-1}-1\) **noninitial** zero-vertices exist. Including the initial vertex gives
\[
n\ge (2^h-1)+(2^{h-1}-1)+1=3\cdot2^{h-1}-1.
\]
For \(h=1\) the same statement simply says a nontrivial concept family requires at least one one-vertex besides the initial vertex.

**5. Construction and uniqueness.** Let \(m=2^{h-1}\) and take the word \(01(011)^{m-1}\). It has \(2m-1=2^h-1\) ones, \(m\) zeros and hence \(2m=2^h\) distinct hypotheses. The noninitial zero-vertices supply exactly the cuts after hypothesis indices \(2,4,\ldots,2m-2\) (using zero-based interval boundaries). These cuts recursively bisect the ordered \(2^h\) hypotheses down to consecutive pairs. At each pair, a one-vertex query separates its two hypotheses. This builds a complete tree of depth \(h\), matching the lower bound.

If equality holds in the vertex bound, the full mistake tree uses exactly \(2^h\) hypotheses. Its subfamilies at level \(h-1\) are exactly \(m\) disjoint consecutive pairs; therefore its distinct high-level prefix cuts must be precisely the boundaries after \(2,4,\ldots,2m-2\) hypotheses. Equality permits exactly those \(m-1\) noninitial zeros, and exactly \(2m-1\) ones. Hence the creation word is uniquely \(01(011)^{m-1}\). Every extremal threshold graph has some creation word in the first-zero convention, and the equality argument forces this same word for any such representation. Hence all extremal graphs are isomorphic to the displayed construction.

**6. All orders.** For any \(n\ge N_h\), append \(n-N_h\) zero-vertices after the last one-vertex. These vertices belong to every maximal independent set and hence do not change either dimension. The lower bound and this padding construction give the stated maximum dimension formula for every \(n\ge2\).

## Verification

Run `python3 verify_threshold.py` with Python 3; the program has no external dependencies. It enumerates all \(2^{n-1}\) threshold creation words on \(1\le n\le11\) vertices (2,047 words overall), checks their concept lists directly against maximal independent sets enumerated from edges for \(n\le8\), independently computes Littlestone dimension from its defining recursion, and compares it to the interval recurrence and the asserted VC dimension. The first ranks two and three are attained on 5 and 11 vertices, respectively. Expected final output ends in `THRESHOLD_ONLINE_PASS 2047 minimum_ranks [(0, 1), (1, 2), (2, 5), (3, 11)]`. These finite checks corroborate the unrestricted proof but do not establish it for all orders.

## Relationship to prior work

Gurski and Rehs (first public source 2017-10-24, arXiv:1710.08953) classify and enumerate maximal independent sets of threshold graphs (notably their Observation 8 and Theorem 25). We use that standard description; enumerability is not claimed new. Alon, Livni, Malliaris and Moran (2018, arXiv:1806.00949) discuss Littlestone dimension, threshold concept classes and finite-versus-infinite online rank, but not the graph-specific minimum vertex order or creation-word characterization. The new focus here is the all-order exact rank recurrence and sharp unique order-minimizing threshold graph for each online dimension. The general finite-class cardinality upper bound \(\operatorname{Ldim}\le\lfloor\log_2|\mathcal M(G)|\rfloor\) does not determine the minimum graph order: distinct prefix tests require additional graph vertices beyond those identifying the hypotheses.

## Limitations

The uniqueness assertion is only among threshold graphs (not arbitrary graphs or all cographs). The creation word must be understood under the stated first-zero convention. No claimed consequence pertains to arbitrary graph maximal independent sets, randomized online learning, or private learning. Historical priority under alternative terminology for nested one-hot/prefix concept classes may remain unrecognized. Independent expert review has not been performed.

## References

1. Frank Gurski and Carolin Rehs, *Counting and Enumerating Independent Sets with Applications to Knapsack Problems*, arXiv:1710.08953, initially public 2017-10-24. https://arxiv.org/abs/1710.08953 .
2. Noga Alon, Roi Livni, Maryanthe Malliaris and Shay Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949, initially public 2018-06-04. https://arxiv.org/abs/1806.00949 .
