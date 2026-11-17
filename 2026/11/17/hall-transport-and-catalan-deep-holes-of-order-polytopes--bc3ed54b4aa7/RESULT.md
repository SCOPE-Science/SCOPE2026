# Hall transport and Catalan deep holes of order polytopes

## Finding
For a finite poset \(P\) with \(n\ge2\) elements, let its standard order polytope be
\[
\mathcal O(P)=\{y\in[0,1]^n:y_i\le y_j\text{ whenever }i<_P j\}.
\]
Write \(H(P)=d_H([0,1]^n,\mathcal O(P))\) for the ambient Euclidean Hausdorff distance, which is directed from the cube because \(\mathcal O(P)\subseteq[0,1]^n\). Then
\[
H(P)^2\le \frac{\lfloor n^2/4\rfloor}{n}.
\]
Equality holds exactly when there is a binary vector \(b\) with \(k=\sum_i b_i\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) satisfying the following **weighted Hall criterion**. Put \(U=\{i:b_i=1\}\), \(W=\{j:b_j=0\}\), and for \(S\subseteq U\) put \(N_P^+(S)=\{j\in W:\exists i\in S\text{ with }i<_P j\}\). The criterion is
\[
(n-k)|S|\le k|N_P^+(S)|\qquad\text{for every }S\subseteq U.
\]
Moreover, **all** maximizers of the distance to \(\mathcal O(P)\) are precisely those binary vectors, and each has the unique nearest order-polytope point \((k/n)\mathbf1\). For even \(n\), universal-bound equality is equivalent to the (undirected) comparability graph of \(P\) having a perfect matching.

For the total chain \(C_n\), the bound is attained and the number of deepest cube corners equals
\[
B_n=\begin{cases}\displaystyle \frac{1}{m+1}\binom{2m}{m},&n=2m,\\[4pt]
\displaystyle\frac2{2m+1}\binom{2m+1}{m},&n=2m+1.
\end{cases}
\]
For the alternating fence \(F_n\) with successive cover relations \(1<2>3<4>\cdots\), the same sharp squared distance is attained, but **exactly one** cube corner is deepest: its coordinates are \(1\) at all minimal elements and \(0\) at all maximal elements. Both posets have the same underlying undirected Hasse path, yet their deepest-corner multiplicities are dramatically different.

## Assumptions and scope
All distances are ordinary Euclidean distances in the explicitly given \(n\)-coordinate embedding; no normalization of edges or directions is imposed. Posets have at least two labeled elements. A comparability arrow \(i<_P j\) points from the smaller to the larger element. The two path examples have \(n\ge2\). The theorem concerns distance from the **entire** unit cube to an order polytope and classifies only corners that attain the universal sharp bound; for a general poset not satisfying the Hall criterion, it does not claim a formula for the smaller value of \(H(P)\).

## Proof
**1. A universal sharp variance bound and extremal corners.** For every \(x\in[0,1]^n\), its constant mean \(\bar x\mathbf1\) belongs to every \(\mathcal O(P)\). Thus
\[
\operatorname{dist}(x,\mathcal O(P))^2\le \sum_i(x_i-\bar x)^2=:V(x).
\]
The quadratic form of \(V\) is \(I-\mathbf1\mathbf1^T/n\). Holding the other coordinates fixed, \(V\) is a *strictly convex* quadratic in any one coordinate, with coefficient \(1-1/n>0\). Its cube maximum is therefore attained only at binary corners. For a binary corner with \(k\) ones, \(V(b)=k(n-k)/n\le \lfloor n^2/4\rfloor/n\), with equality exactly at the two specified balanced values of \(k\). Consequently any point achieving the universal distance bound must be such a binary corner and must have the constant vector \(c=(k/n)\mathbf1\) as its Euclidean projection onto the closed convex set \(\mathcal O(P)\).

**2. Projection, finite flow, and weighted Hall.** The vector \(c\) lies strictly inside all coordinate constraints and on all order-comparability supporting hyperplanes. Its outward normal cone is
\[
N_{\mathcal O(P)}(c)=\operatorname{cone}\{e_i-e_j:i<_P j\}.
\]
The Euclidean projection criterion says that \(c=\Pi_{\mathcal O(P)}(b)\) if and only if \(b-c\in N_{\mathcal O(P)}(c)\). The vector \(b-c\) supplies \((n-k)/n\) units at every element of \(U\) and demands \(k/n\) units at every element of \(W\); its total supply and demand agree. A nonnegative directed comparability flow with this divergence is equivalent, by flow decomposition along increasing poset paths and by direct comparability of each path's endpoints, to transportation from \(U\) to \(W\) using only arcs \(i<_P j\). The finite bipartite max-flow/min-cut theorem states that these supplies and demands admit such a transportation precisely when \((n-k)|S|\le k|N_P^+(S)|\) for every subset \(S\subseteq U\). This proves the criterion and the exhaustive deep-hole classification. The Euclidean projection is unique by strict convexity of squared distance.

For even \(n\), both sides have equal cardinality and every positive and negative mass equals \(1/2\). The criterion is the ordinary Hall marriage condition on the comparability edges between \(U\) and \(W\), hence equivalent to a perfect matching there. Conversely, any perfect matching in the undirected comparability graph can be oriented from each matched smaller element to its matched larger element; declaring the smaller endpoints \(U\) and the larger endpoints \(W\) provides a balanced deep corner. Thus even-order saturation is equivalent to a comparability-graph perfect matching.

**3. Total chains and Catalan enumeration.** In the total chain, the normal generators may be restricted to adjacent differences \(e_i-e_{i+1}\). Writing \(t=k/n\), the unique coefficients expressing the sum-zero vector \(b-t\mathbf1\) as a combination of these generators are its prefix sums, so the condition is
\[
\sum_{j=1}^{r}(b_j-t)\ge0\qquad(1\le r<n).
\]
For \(n=2m\), balanced strings have \(m\) ones and this is the ordinary Dyck-prefix condition, counted by the Catalan number \(\binom{2m}{m}/(m+1)\). For \(n=2m+1\), either \(k=m\) or \(k=m+1\), and \(\gcd(k,n)=1\). Multiplying the prefix increments by \(n\), a one contributes \(n-k\) and a zero contributes \(-k\). Because each partial sum at length \(r\) is congruent to \(-kr\pmod n\), the \(n\) partial sums before the final return are distinct modulo \(n\). Hence exactly one cyclic rotation of each balanced binary word has all partial sums nonnegative (start at the unique minimum); no balanced word has a nontrivial rotational period. Exactly \(\binom nk/n\) of the strings with each fixed \(k\) qualify, giving twice that count because the two allowed \(k\)'s have the same binomial coefficient.

**4. Alternating fences and uniqueness.** Every odd-indexed element of \(F_n\) is minimal and every even-indexed element is maximal. A deep corner cannot put a positive supply at a maximal element, because that element has no outgoing comparability arc; nor can it put a negative demand at a minimal element, because it has no incoming arc. Accordingly any deep corner must be \(b=(1,0,1,0,\ldots)\). For this corner, set \(k=\lceil n/2\rceil\) and define the signed prefix residual \(s_r=\sum_{j=1}^{r}(b_j-k/n)\), \(1\le r<n\). The directed flow on the Hasse edge between positions \(r\) and \(r+1\), oriented from its odd to its even endpoint, has nonnegative magnitude \(|s_r|\), since \(s_r\ge0\) for odd \(r\) and \(s_r\le0\) for even \(r\). For even \(n\) these values alternate between \(1/2\) and \(0\); for odd \(n=2m+1\), they are \((m+1-j)/n\) on \(r=2j-1\) and \(-j/n\) on \(r=2j\), with \(1\le j\le m\) where the edge exists. Their net divergence is precisely \(b-(k/n)\mathbf1\). Hence the normal-cone criterion holds and this sole corner is deepest.

## Verification
The exact-arithmetic script `check_deep_holes.py` enumerates all binary corners of chains of order \(2\) through \(12\), uses the pool-adjacent-violators projection to measure the actual Euclidean distances, and checks both the Hall rule and the exact Catalan/odd-binomial counts. It checks all balanced corners for alternating fences through order \(12\) and verifies a nonnegative rational covering-edge flow. The independent exact script `independent_exact.py` enumerates all partitions of coordinates to obtain the least-squares isotonic projection for four families of small posets through order \(7\), testing the Hall condition against the sharp distance. Both scripts use only the Python standard library; run `python3 check_deep_holes.py` and `python3 independent_exact.py` in the directory containing the extracted files. Every tested arithmetic assertion is rational and exact. These finite checks are corroborative; the preceding argument proves the infinite-domain statements.

## Relationship to prior work
Stanley's original order-polytope framework supplies the inequalities, and standard isotonic projection and finite max-flow theorems supply key proof ingredients. The 2021 study of generalized snake-poset order polytopes concerns triangulations, circuit and volume structure rather than Euclidean cube-to-polytope deep holes. An isotonic-regression algorithmic treatment concerns efficient fits rather than this global Hausdorff bound and weighted Hall equality criterion. A recent order/chain-polytope edge theorem concerns combinatorial edges, not cube-corner Euclidean nearest points. Closest identified work on directed Hausdorff distances measures the separation between **order and chain polytopes**, not between an order polytope and its containing cube. The exact link between a sharp Euclidean gap, comparability matching, and the Catalan-versus-unique orientation contrast is the claim under assessment; it is not inferred from shared terminology.

## Limitations
The equality criterion requires a finite test for an arbitrary poset and does not yield its nonsaturating exact distance. The Catalan and uniqueness enumerations are only for the two specified path Hasse orientations. Historical priority is provisional; equivalences expressed as worst-case isotonic regression or distance-to-isotone-cone inequalities could have appeared under different names. No independent mathematical audit is represented by the included self-review.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf.
2. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (first public February 22, 2021), https://arxiv.org/abs/2102.11306.
3. A. Henzi, A. Mösching, and L. Dümbgen, *Accelerating the pool-adjacent-violators algorithm for isotonic distributional regression*, arXiv:2006.05527 (2020), https://arxiv.org/abs/2006.05527.
4. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413 (2026), https://arxiv.org/abs/2610.07413.
5. P. Hall, *On representatives of subsets*, Journal of the London Mathematical Society (1935), for the marriage criterion; the weighted finite flow version follows from max-flow/min-cut.
