# Marked Poisson law for closed reciprocal triangles in symmetric two-nearest-neighbor networks

## Finding
Let \(K_n\) have independent identically distributed continuous edge weights. Each vertex points to its two neighbors of smallest incident weight. A *closed reciprocal triangle* is a three-vertex set whose every vertex chooses its two partners, producing all six directed arcs and no outgoing arcs from that triple (incoming arcs are permitted). Write \(T_n\) for its count. The exact expectation is
\[
\mathbb ET_n=\frac{n(n-1)(n-2)}{(2n-5)(3n-7)(3n-6)},\qquad n\ge3.
\]

Let \(F\) be the continuous common edge-weight cumulative distribution function. Sort the three internal values of \(nF(W_e)\) for each closed triangle as \(a\le b\le c\). The counting measure of these triples converges in distribution to a **finite Poisson point process** on \(S=\{0\le a\le b\le c<\infty\}\), with intensity
\[
\mu(da\,db\,dc)={\bf1}_{\{a\le b\le c\}}e^{-b-2c}\,da\,db\,dc.
\]
In particular, \(T_n\Rightarrow\operatorname{Pois}(1/18)\), and the number of closed triangles whose maximum internal transformed edge is at most \(t\ge0\) converges to \(\operatorname{Pois}(\Lambda(t))\), where
\[
\Lambda(t)=\frac1{18}-\frac12e^{-2t}+(\tfrac t3+\tfrac49)e^{-3t}.
\]
Disjoint edge-mark regions of continuity have asymptotically independent Poisson counts.

## Assumptions and scope
The graph is the complete graph on \(n\ge3\) labeled vertices, and unordered edge weights are independent with a common atomless continuous distribution. Direction matters: each vertex has exactly two outgoing arcs. A closed triangle has no outgoing arcs, but may receive arcs from outside. It is *not necessarily* an isolated component of the undirected graph obtained by forgetting directions. Transforming weights by \(F\) yields independent \(\operatorname{Unif}[0,1]\) edge values and does not change the directed network. All limits are for \(n\to\infty\), with fixed mark regions and \(t\).

## Proof
**1. One triple and an exact integral.** For a specified triple, sort its three independent transformed internal edges as \(0\le a\le b\le c\le1\). The three vertex-specific internal maximum weights are \(b,c,c\): each of the other \(n-3\) edge weights incident to these vertices must exceed its maximum. By independence the conditional event probability is \((1-b)^{n-3}(1-c)^{2n-6}\). The internal order statistics have joint density \(6\), whence
\[
\begin{aligned}
\Pr(\text{specified triple closed})
&=6\int_0^1\!\int_0^c\!\int_0^b
 (1-b)^{n-3}(1-c)^{2n-6}\,da\,db\,dc\\
&=\frac6{2n-5}\int_0^1b(1-b)^{3n-8}\,db\\
&=\frac6{(2n-5)(3n-7)(3n-6)}.
\end{aligned}
\]
Multiplication by \(\binom n3\) proves the finite expectation.

**2. Disjointness and joint event probabilities.** Distinct closed triangles cannot share vertices: a shared vertex would have to choose two different two-element neighbor sets. Fix \(m\) ordered, vertex-disjoint prospective triangles and condition on their internal values. Put \(\alpha_v\) equal to the larger of the two internal values incident to vertex \(v\). Every edge from a selected vertex to one of the \(n-3m\) unselected vertices must exceed \(\alpha_v\). Every edge joining two different selected triangles must exceed both endpoint thresholds. Consequently the exact conditional joint probability is
\[
\prod_{v\in V_*}(1-\alpha_v)^{n-3m}
\prod_{\substack{u,v\in V_*\\u,v\text{ in distinct triangles}}}
 (1-\max\{\alpha_u,\alpha_v\}),
\]
where the second product runs over unordered cross-triangle pairs. There are no other constraints; in particular, edges incident to outside vertices are not subject to their own choices.

**3. Factorial moment measures.** For each triple write its sorted internal \(F\)-transformed edge values as \((a,b,c)/n\). With these scaled variables fixed, the probability in Step 2 tends to
\(\prod_{j=1}^m e^{-b_j-2c_j}\).
The number of ordered disjoint triangle families is \((n)_{3m}/6^m\). The \(m\) sorted internal triples contribute the density factor \(6^m n^{-3m}\). The product of these combinatorial and density factors tends to one. Thus, for arbitrary bounded continuous nonnegative test functions \(f_1,\ldots,f_m\) on \(S\),
\[
\mathbb E\sum_{\substack{T_1,\dots,T_m\text{ distinct}\\T_j\text{ closed}}}\prod_{j=1}^m f_j(\mathrm{mark}(T_j))
\longrightarrow \prod_{j=1}^m\int_S f_j(a,b,c)e^{-b-2c}\,da\,db\,dc.
\]
The same conclusion holds for bounded continuity regions. To justify passage under the integral even for unbounded mark sets, use the upper bound \(e^{-\frac12\sum_j(b_j+2c_j)}\) whenever \(n\ge6m\), since \(1-x\le e^{-x}\). The bound is integrable over \(S^m\). Every fixed mixed factorial-moment measure therefore converges to that of the claimed finite Poisson point process. Its Poisson moment sequences determine the joint laws and control total mass, establishing the point-process convergence.

**4. The mark intensity.** The total mass is
\[
\mu(S)=\int_0^\infty\!\int_0^c\!\int_0^b
 e^{-b-2c}\,da\,db\,dc
=\frac12\int_0^\infty b e^{-3b}\,db=\frac1{18}.
\]
Restricting to \(c\le t\) and integrating first in \(a\), then \(b\), gives
\(\Lambda(t)=\int_0^t e^{-2c}[1-(c+1)e^{-c}]\,dc\), equal to the displayed closed form. This completes all claims.

## Verification
The standalone standard-library script `CHECKER.py` exhaustively checks all \(6!=720\) edge orderings on four vertices, reproducing \(\mathbb ET_4=4/15\), and checks the mark-CDF derivative and finite expectation boundary values. Its output is `PASS`. These finite checks are independent sanity checks, not substitutes for the factorial-moment proof.

## Relationship to prior work
Cooper and Frieze (1995) study the same independent symmetric-weight complete-graph model and derive Poisson laws for **isolated components** of its undirected two-nearest-neighbor graph. Their isolated triangle intensity is approximately \(0.00415239\); an isolated triangle must be closed, but a closed triangle can have incoming arcs and thus need not be an isolated component. Their statement does not determine the count of all closed directed sink triples or their complete edge-mark intensity. Ball (2014) studies reciprocal geometric nearest-neighbor graphs built from spatial point distances and connectivity thresholds, not independent symmetric edge weights or this fixed-size marked motif. Previously published exact laws for mutual **one-nearest-neighbor pairs** concern a different outdegree and cannot imply the three-vertex two-nearest-neighbor result. The proof here instead records the directed absorbing three-node motifs and their entire edge-weight profile.

## Limitations
The limit concerns a fixed outdegree of two and vertex triples, not all strongly connected components or isolated undirected components. The formula for edge marks is in distribution-function quantile units \(nF(W_e)\), not untransformed physical distances. No explicit convergence-rate bound is claimed. Historical priority remains subject to unlocated general theorems on rare directed motifs; no independent audit has been conducted.

## References
1. C. Cooper and A. Frieze, *On the connectivity of random k-th nearest neighbour graphs*, Combinatorics, Probability and Computing 4 (1995), 343–362. https://doi.org/10.1017/S0963548300001711 ; publicly accessible preprint https://www.math.cmu.edu/~af1p/Texfiles/ok.pdf (manuscript dated June 15, 1995).
2. N. Ball, *A strict undirected model for the k-nearest neighbour graph*, first arXiv version June 3, 2014. https://arxiv.org/abs/1406.0716
