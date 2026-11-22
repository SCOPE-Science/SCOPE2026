# Exact comparison-dependence geometry and independent interval families in randomized Quicksort

## Finding

For a uniformly randomized-pivot Quicksort execution on \(n\ge2\) distinct totally ordered keys, let \(I_{a,b}\) indicate whether keys of ranks \(a<b\) are ever directly compared. Write \(A=[a,b]\), \(B=[c,d]\), \(u=b-a+1\), \(v=d-c+1\), \(w=|A\cap B|\), and \(t=|A\cup B|\). The exact two-indicator covariance for **distinct** rank intervals is

\[
\operatorname{Cov}(I_A,I_B)=
\begin{cases}
0,&\text{disjoint or strictly contained, with no common endpoint},\\
\dfrac{s-2}{s\ell},&\text{one is contained in the other and they share exactly one endpoint},\\
\dfrac{(u-2)(v-2)}{uv(u+v-1)},&\text{they meet at one endpoint, but otherwise do not overlap},\\
-\dfrac{2(u+v-2w)}{uvt},&\text{their endpoints strictly interleave},
\end{cases}
\]
where \(s=\min(u,v)\) and \(\ell=\max(u,v)\). On the diagonal, \(\operatorname{Var}(I_A)=2(u-2)/u^2\). Thus all strictly interleaving pairs are negatively correlated; shared-endpoint pairs are positively correlated whenever both intervals have at least three ranks; and disjoint or strictly contained pairs are independent.

The higher-order assertion is a **complete classification of independent subfamilies**: for any finite collection \(\mathcal F\) of distinct rank intervals of lengths at least three, its entire family of comparison indicators is mutually independent **if and only if** every two intervals are disjoint or strictly nested with four distinct endpoints. In that case, for all real \(z_A\),

\[
\mathbb E\prod_{A\in\mathcal F}z_A^{I_A}
=\prod_{A\in\mathcal F}\left(1-\frac2{|A|}+\frac{2z_A}{|A|}\right).
\]

## Assumptions and scope

Uniformly randomized-pivot Quicksort picks a pivot uniformly from each active subarray, compares it once with every other key in that subarray, and recursively processes the smaller and larger keys. All input keys are distinct; the results depend only on their sorted ranks. Equivalently, draw independent identically distributed continuous priorities \(U_1,\ldots,U_n\) and pivot first on the smallest-priority key in every current rank interval. The statements apply for every integer \(n\ge2\) and all specified pair/family choices. An interval \([a,b]\) is the *closed set of consecutive ranks* \(\{a,a+1,\ldots,b\}\). Strict nesting means \(a<c<d<b\), or the reverse: the smaller interval does not share an endpoint with the larger.

When adjacent ranks are compared, the indicator is deterministic one. The mutual-independence characterization excludes these degenerate length-two intervals because they can be added to any collection without affecting independence.

## Proof

**Priority reduction.** Until the first pivot chosen among ranks \(a,\ldots,b\), the two endpoint keys remain in the same recursive subarray. That first pivot compares the endpoints exactly when it is one of them; an interior pivot separates them permanently. Hence
\[
I_{a,b}=\mathbf 1\{\operatorname{argmin}_{a\le j\le b} U_j\in\{a,b\}\},\qquad
\Pr(I_{a,b}=1)=\frac2{b-a+1}.
\]
Ties have probability zero. By conditioning on the location of the least priority in an interval, all formulas below use finite equiprobable choices.

**Joint probabilities, by endpoint order.** Let \(p_{A,B}=\Pr(I_A=I_B=1)\). If \(A\) and \(B\) are disjoint, their events concern disjoint independent priorities, so \(p_{A,B}=4/(uv)\). If \(A\) is strictly nested in \(B\) (or conversely), the larger interval has its minimum at one of its two outside endpoints with probability \(2/\ell\); conditionally, the relative priority ordering in the smaller interval remains uniform, giving \(p_{A,B}=4/(uv)\).

Suppose the two intervals share their left endpoint, with smaller length \(s\) and larger length \(\ell\). The minimum in the larger interval must occur at their common left endpoint (probability \(1/\ell\)), or its right endpoint (probability \(1/\ell\)) together with a successful smaller-interval event (conditional probability \(2/s\)). Thus \(p_{A,B}=(s+2)/(s\ell)\). Right-endpoint sharing is symmetric. Subtracting \(4/(s\ell)\) gives \((s-2)/(s\ell)\).

If the intervals touch at one endpoint but have disjoint interiors, write them in order \([a,b]\), \([b,d]\). The minimum over their union must lie at \(a\), \(b\), or \(d\); the conditional success probabilities for the other interval are \(2/v\), \(1\), or \(2/u\), respectively. Therefore
\[
p_{A,B}=\frac{1+2/u+2/v}{u+v-1},\qquad
p_{A,B}-\frac4{uv}=\frac{(u-2)(v-2)}{uv(u+v-1)}.
\]

If the endpoints interleave strictly, say \(a<c<b<d\), the minimum over their union must be at \(a\) or \(d\): an interior minimum makes at least one event fail. If it is at \(a\), the second interval succeeds conditionally with probability \(2/v\); if it is at \(d\), the first succeeds with probability \(2/u\). The union has \(t=u+v-w\) elements, so
\[
p_{A,B}=\frac2t\left(\frac1u+\frac1v\right),\qquad
p_{A,B}-\frac4{uv}=\frac{2(u+v-2t)}{uvt}=-\frac{2(u+v-2w)}{uvt}.
\]
As the two non-overlapping wings are nonempty, \(u+v-2w>0\), proving strict negativity. These cases exhaust all endpoint-order patterns. The variance expression follows directly from the Bernoulli marginal.

**Mutual independence.** Suppose \(\mathcal F\) has pairwise disjoint or strictly nested rank intervals. Pick an inclusion-minimal interval \(J\) in the family. Every other interval is disjoint from \(J\) or strictly contains it, so the other indicator events depend on priorities inside \(J\) only through the minimum numerical priority \(M_J\). For a containing interval, its two endpoints are outside \(J\), and knowing \(M_J\) and all priorities outside \(J\) is sufficient to decide whether its minimum lies at a containing endpoint. However, the indicator \(I_J\) depends only on which labelled point in \(J\) achieves that minimum, and its identity is uniform on \(J\), independent of \(M_J\) and all priorities outside \(J\). Hence \(I_J\) is independent of the joint vector of all remaining indicators. Remove \(J\), apply the same argument inductively, and obtain mutual independence and the displayed product generating function.

For the converse, take two nondegenerate intervals not disjoint and not strictly nested. They share an endpoint or strictly interleave. The covariance formulas are then respectively strictly positive or strictly negative. Mutual independence would force all such covariances to vanish, a contradiction. This proves the characterization.

## Verification

The standalone standard-library Python program `verify.py` enumerates all \(n!\) relative priority orders for every \(2\le n\le8\) and evaluates the actual comparison events directly from minimum-priority endpoints. It checks every individual probability, every entry in the exact covariance matrix (including diagonals and both signs), and the equivalence of zero covariance with strict-nesting/disjointness for nondegenerate distinct intervals. It also enumerates every eligible three-interval strictly nested/disjoint family at those sizes and checks its exact triple product probability. Its replay reports **935 exact-rational assertions**, including **11 nondegenerate three-event product tests**. These finite checks are independent of the above all-size proof and do not themselves establish the infinite family result.

Run with `python3 verify.py` from the directory containing the files. There are no external Python dependencies.

## Relationship to prior work

The basic comparison indicator and its marginal \(2/(b-a+1)\) are standard in algorithm analysis and are **not claimed as new**. Iliopoulos and Penman (2010) give a self-contained proof of the previously known variance of the *total* randomized-Quicksort comparison count, using a total-cost recurrence and generating functions. Alonso and collaborators (2003) analyze inversions in outputs of Quicksort with unreliable comparisons. These treatments address different observables and do not state the full interval-resolved pair covariance kernel together with the all-order independence classification. The exact variance of ordinary total comparisons is an established result, not a claim of this work.

The structural point of the present finding is that the nontrivial indicator field has a sign-complete geometric dependence law, and that pairwise zero covariances in the strict-laminar regime strengthen to exact *joint* independence for arbitrarily many events. Consequently, one can evaluate joint generating functions and weighted-count variances on precisely delineated collections of key pairs.

## Limitations

This result concerns uniformly randomized pivots, distinct keys, and comparisons made directly between a pivot and keys in its subproblem; it does not describe median-of-sample Quicksort, imperfect comparisons, or comparisons introduced by a separate partitioning implementation. The field outside strict-laminar families is generally dependent; the formulas do not yield an arbitrary joint law for all comparison indicators. Literature priority has not been independently audited: a logically equivalent statement in other random search-tree, Cartesian-tree, or treap terminology cannot be excluded. No claim is made concerning a new total-comparison variance formula or a new Quicksort limit distribution.

## References

- L. Alonso, P. Chassaing, F. Gillet, S. Janson, E. M. Reingold, R. Schott, *Quicksort with unreliable comparisons: a probabilistic analysis*, arXiv:math/0312437 (first posted 2003-12-24), https://arxiv.org/abs/math/0312437.
- V. Iliopoulos and D. Penman, *Variance of the number of Comparisons of Randomized Quicksort*, arXiv:1006.4063 (first posted 2010-06-21), https://arxiv.org/abs/1006.4063.
- *Randomized Quicksort*, University of Michigan EECS 376 lecture notes, https://eecs376.github.io/notes/randomness.html (standard individual comparison probability).
