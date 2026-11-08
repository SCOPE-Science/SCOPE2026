# Sharp seven- and ten-vertex shape thresholds for random cactus spanning-tree leaf counts

## Finding

**Theorem (weighted cycle factorization and sharp shape thresholds).** Let \(G\) be a finite connected simple cactus graph with \(N\ge3\) vertices, with a strictly positive conductance \(w_e\) on every edge. Choose a spanning tree \(T\) with probability proportional to \(\prod_{e\in T}w_e\), and let \(L\) be the number of degree-one vertices of \(T\). Write \(b_1\) for the number of vertices of degree one in \(G\). For each simple cycle \(C\) and \(j\in\{0,1,2\}\), define
\[
R_{C,j}=\sum_{e=uv\in E(C):\,\mathbf1_{\{d_G(u)=2\}}+\mathbf1_{\{d_G(v)=2\}}=j}\frac1{w_e}.
\]
Empty sums are zero. Then the complete probability generating function is
\[
\boxed{\mathbb E[z^L]=z^{b_1}\prod_C\frac{R_{C,0}+R_{C,1}z+R_{C,2}z^2}{R_{C,0}+R_{C,1}+R_{C,2}}.}\tag{1}
\]
In particular, it has only real zeros **if and only if**
\[
\boxed{R_{C,1}^{\,2}\ge4R_{C,0}R_{C,2}\quad\text{for every cycle }C.}\tag{2}
\]
For **unweighted** cactus graphs, the leaf-count probabilities are log-concave for every \(N\le9\); the first possible failure of log-concavity occurs at exactly \(N=10\). The first possible failure of real-rootedness occurs at exactly \(N=7\). Both lower bounds are attained by explicit connected cactus graphs.

Here log-concavity means \(\Pr(L=j)^2\ge\Pr(L=j-1)\Pr(L=j+1)\) at every integer \(j\); the probability sequence has no internal zeros. Real-rootedness includes possible zeros at the origin.

## Assumptions and scope

A *cactus* is a finite connected simple graph in which each edge belongs to at most one simple cycle; equivalently every biconnected block is a bridge or a cycle. Graphs on two vertices are excluded so that the standard degree-one definition of a tree leaf entails no degenerate exceptions. The weights in the first two conclusions are **strictly positive**; the seven- and ten-vertex cutoff assertions concern **unit weights**. The thresholds refer to minimum graph order among all such connected unweighted cacti, not to a particular cycle length or a restricted enumeration.

For every cycle \(C\), let \(E_C\) denote the unique edge removed from \(C\) to obtain \(T\). Every bridge belongs to \(T\). The variables \(E_C\) are independent, and
\[
\Pr(E_C=e)=\frac{w_e^{-1}}{\sum_{f\in E(C)}w_f^{-1}}.\tag{3}
\]
The original degree of a vertex, not its random tree degree, is used in the definition of \(R_{C,j}\).

## Proof

**1. Independent cycle deletions.** Every spanning tree of a cactus is obtained by deleting exactly one edge from each simple cycle and retaining all bridges. Indeed, deleting fewer would leave a cycle, while deleting more disconnects a cycle block because there is no alternate connection between its different vertices outside that block. The product of all edge conductances of a candidate tree equals the product of all conductances in \(G\) divided by \(\prod_C w_{E_C}\). Normalizing this weight over the Cartesian product of the cycle choices gives independence and (3).

**2. Which vertices can become leaves.** A vertex incident to \(c\) cycle blocks and \(h\) bridge blocks has original degree \(2c+h\). Removing one edge from each incident cycle can decrease its degree by at most \(c\), hence its tree degree is at least \(c+h\). If \(c+h\ge2\), the vertex cannot become a leaf. If \(c+h=1\), there are just two possibilities: an original degree-one vertex (\(c=0,h=1\)) is always a leaf, while an original degree-two vertex on one cycle (\(c=1,h=0\)) becomes a leaf exactly when \(E_C\) is incident to it. Original degree-two vertices on two bridge blocks remain of degree two. Consequently,
\[
L=b_1+\sum_C \left(\mathbf1_{\{d_G(u_C)=2\}}+\mathbf1_{\{d_G(v_C)=2\}}\right),
\quad E_C=u_Cv_C.
\]
The independent choices (3) prove (1) and show that each cycle contributes a random variable supported on \(\{0,1,2\}\).

**3. Real-rootedness.** A factor in (1), up to a positive scalar, is the quadratic \(R_{C,0}+R_{C,1}z+R_{C,2}z^2\). Because its coefficients are nonnegative, it has only real zeros precisely when its discriminant \(R_{C,1}^{\,2}-4R_{C,0}R_{C,2}\) is nonnegative. This also includes constant, linear, and monomial cases. All zeros of a polynomial product come from its factors, so (2) is both necessary and sufficient.

**4. A graph-order bound for cycle patterns.** Restrict now to unit weights. Call a cycle vertex *active* when its degree in \(G\) is two; all other cycle vertices are *inactive*. Let \(a,b,c\) be the numbers of cycle edges with respectively two, one, and zero active endpoints. If both vertex types occur, let \(r\ge1\) be the number of maximal active runs around the cycle, equivalently the number of maximal inactive runs. Then
\[
b=2r,\qquad |V(C)|=a+2r+c,\qquad \#\{\text{inactive vertices on }C\}=c+r.\tag{4}
\]
Each inactive cycle vertex has an incident edge outside \(C\), and different inactive cycle vertices require different outside vertices: a connected component outside a cactus cycle cannot attach to two vertices of that cycle without forming a second cycle sharing at least two vertices with it. Hence
\[
\boxed{N\ge a+2c+3r.}\tag{5}
\]
When only one type of cycle vertex occurs, the factor is a monomial; no root or log-concavity issue arises.

**5. The sharp real-root cutoff.** If \(N\le6\) and \(ac>0\), (5) forces \(r=1\), \(a=c=1\), and \(N=6\). The cycle factor is then proportional to \(1+2z+z^2\), whose discriminant is zero. If \(ac=0\), the factor is automatically real-rooted. Thus every unweighted cactus on at most six vertices has a real-rooted leaf generating polynomial. Conversely, take a five-cycle and add a pendant edge at each of two adjacent cycle vertices. Its three remaining cycle vertices are active and its two new pendant vertices are deterministic leaves. Equation (1) gives
\[
\mathbb E[z^L]=\frac{z^2}{5}(1+2z+2z^2).
\]
The quadratic discriminant is \(4-8=-4\), showing that seven vertices are necessary and sufficient for non-real-rootedness.

**6. The sharp log-concavity cutoff.** A nonnegative triple \((c,b,a)\) is log-concave exactly when \(b^2\ge ac\); factors with missing terms remain trivially log-concave. Suppose \(N\le9\). When \(r=1\), (5) yields \(a+2c\le6\), and direct integer bounds give \(ac\le4=b^2\). When \(r\ge2\), (5) yields \(a+2c\le9-3r\le3\), so \(ac\le1<4r^2=b^2\). Therefore every individual cycle factor has a nonnegative log-concave coefficient sequence with no internal zeros. Convolution preserves this property: for example, the Toeplitz matrix of such a sequence has all two-by-two minors nonnegative, and Toeplitz-matrix multiplication realizes convolution; Cauchy–Binet preserves nonnegative two-by-two minors. By (1), the full leaf-count distribution is log-concave.

For sharpness, take an eight-cycle and add a pendant edge at each of two adjacent cycle vertices. The cycle has \((c,b,a)=(1,2,5)\), so
\[
\boxed{\mathbb E[z^L]=\frac{z^2}{8}(1+2z+5z^2).}
\]
Its three nonzero consecutive probabilities are \(1/8,2/8,5/8\), and \(2^2<1\cdot5\). Hence it is not log-concave, establishing the first possible order \(N=10\).

This proves all assertions. The proof of the infinite graph-family cutoff uses (5), not a finite graph census.

## Verification

Run `python verify.py` with `networkx` as specified by `requirements.txt`. The checker reconstructs every connected cactus graph isomorphism type appearing in the NetworkX graph atlas on orders three through seven. For each, it independently enumerates every cycle-deletion spanning tree and compares the resulting exact rational leaf-count distribution against (1), first with unit weights and then with nonconstant positive rational weights. It also recomputes every pairwise leaf covariance from the same enumeration as a cross-check of the underlying cycle mechanism. It scans all binary active/inactive cycle patterns through length thirteen and reports first non-real-rooted and non-log-concave orders seven and ten. Finally, it recomputes the two explicit witness distributions using exact fractions.

Successful standalone output reports 101 connected cactus graph types, 78 with cycles, 101 weighted repetitions, and `PASS`. These finite checks are independent corroboration only: the all-order proof is the block-decomposition and inequality argument above.

## Relationship to prior work

Hladký, Nachmias, and Tran (2017) study local limits and leaf densities of uniform spanning trees on dense graph sequences. Their assumptions and conclusions concern a different regime; they do not give an exact finite weighted-cactus leaf polynomial or either first-failure threshold. Bahrani and Lumbroso (2017) give a combinatorial enumeration and random-generation framework for cactus graphs themselves, not this distribution of spanning-tree leaves. Noguchi and Zamfirescu (2023) prove that the **support** of possible spanning-tree leaf numbers is an interval for every connected graph. That theorem does not bound ratios of **probabilities** or determine real-rootedness. Aldous (1990) provides foundational random spanning-tree methods and leaf statistics but no explicit cactus cutoff is identified in the material consulted. The standard closure of log-concavity under convolution is used, not claimed as new.

The new mathematical assertion is the exact shape criterion and the universal, sharp seven- and ten-vertex boundaries for this natural random spanning-tree statistic, with (1) furnishing the structural proof and weighted extension. A formula for arbitrary graphs based only on matrix-tree determinants would not by itself imply the sharp threshold classifications.

## Limitations

The cutoff assertions are for simple connected cacti with **unweighted** edges; arbitrary positive conductances need not preserve those order cutoffs. The full law (1) and root criterion (2) do allow arbitrary positive conductances. The result concerns the count of leaves, not every joint event of leaf indicators or arbitrary graph classes. The current originality assessment is a targeted literature comparison rather than an independent or exhaustive historical-priority certification. Computational verification through seven vertices does not prove the nine-vertex universal result; that follows from (5) and convolution closure.

## References

1. J. Hladký, A. Nachmias, and T. Tran, *The local limit of the uniform spanning tree on dense graphs*, first public version 2017-11-27, https://arxiv.org/abs/1711.09788.
2. M. Bahrani and J. Lumbroso, *Split-Decomposition Trees with Prime Nodes: Enumeration and Random Generation of Cactus Graphs*, first public version 2017-11-29, https://arxiv.org/abs/1711.10647.
3. K. Noguchi and C. T. Zamfirescu, *Spanning trees for many different numbers of leaves*, first public version 2023-12-21, https://arxiv.org/abs/2312.13674, https://doi.org/10.46298/dmtcs.13116.
4. D. J. Aldous, *The random walk construction of uniform spanning trees and uniform labelled trees*, SIAM Journal on Discrete Mathematics 3 (1990), 450–465, https://doi.org/10.1137/0403039.
5. F. Brenti, *Unimodal, log-concave and Pólya frequency sequences in combinatorics*, Memoirs of the American Mathematical Society 81 (1989), no. 413.
