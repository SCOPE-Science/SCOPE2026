# Three reciprocity cumulants recover graph order, degree, and triangles

## Finding

Let \(G\) be a finite simple undirected \(d\)-regular graph with \(n\) vertices, where \(d\ge1\); connectivity is not required. Independently, each vertex chooses one of its \(d\) neighbors uniformly. Let \(X\) be the number of edges whose endpoints choose one another, and let \(t(G)\) be the number of (unoriented) triangles in \(G\). Write \(\mu=\mathbb E X\), \(\sigma^2=\operatorname{Var}(X)\), and \(\kappa_3=\mathbb E[(X-\mu)^3]\). Then

\[
\mu=\frac{n}{2d},\qquad
\sigma^2=\frac{n(d-1)^2}{2d^3},\qquad
\kappa_3=\frac{n(d-1)^2(d-2)^2}{2d^5}-\frac{6t(G)}{d^6}.
\]

Consequently, the first three cumulants **uniquely determine** \(n\), \(d\), and \(t(G)\) among all finite positive-degree regular simple graphs. The explicit inverse is

\[
d=\frac1{1-\sqrt{\sigma^2/\mu}},\qquad
n=2d\mu,\qquad
t(G)=\frac{nd(d-1)^2(d-2)^2}{12}-\frac{d^6\kappa_3}{6}.
\]

In addition, \(\kappa_3=0\) at \(d=1\); at \(d=2\), it is nonpositive and is zero exactly when the graph is triangle-free; at \(d=3\), it is nonnegative and is zero exactly when every connected component is \(K_4\); at all \(d\ge4\), it is strictly positive.

For example, \(K_{3,3}\) and the triangular prism each have \(n=6\), \(d=3\), \(\mu=1\), and \(\sigma^2=4/9\), while their respective third cumulants are \(4/81\) and \(8/243\), distinguishing the graphs' triangle totals \(0\) and \(2\).

## Assumptions and scope

Each vertex chooses exactly one neighbor, independently of every other vertex. An edge is counted **once** if both choices point across it, not twice for its directed arcs. Graphs are labelled or unlabelled, possibly disconnected, but are finite, loopless, simple, and regular of positive degree. The statements concern the exact finite probability law; no asymptotic limit or sampling estimator is assumed.

## Proof

For each edge \(e=\{u,v\}\), let \(I_e\) be the indicator of the simultaneous events that \(u\) chooses \(v\) and \(v\) chooses \(u\). Since each vertex has only one outgoing choice, \(I_eI_f=0\) whenever edges \(e\) and \(f\) share a vertex. For pairwise vertex-disjoint edges, their indicators are independent and each has expectation \(d^{-2}\). Expanding the product \(z^X=\prod_{e\in E(G)}[1+(z-1)I_e]\), and denoting by \(M_r(G)\) the number of matchings of size \(r\), yields the exact probability-generating function

\[
\mathbb E[z^X]=\sum_{r=0}^{\lfloor n/2\rfloor}M_r(G)\left(\frac{z-1}{d^2}\right)^r.
\tag{1}
\]

Let \(m=nd/2\) denote the number of edges. There are \(h=n\binom d2=m(d-1)\) unordered pairs of incident distinct edges. The line graph \(L(G)\) has \(m\) vertices, is \(2(d-1)\)-regular, and has exactly \(n\binom d3+t(G)\) triangles: any three mutually incident edges of \(G\) either share one vertex or form a triangle. Inclusion-exclusion for independent vertex triples in \(L(G)\) gives

\[
\begin{aligned}
M_1(G)&=m,\\
M_2(G)&=\binom m2-h,\\
M_3(G)&=\binom m3-h(m-2)
+m\binom{2(d-1)}2-n\binom d3-t(G).
\end{aligned}
\tag{2}
\]

This also covers the boundary cases with \(m<3\): the binomial coefficients are ordinary combinatorial counts, and the displayed polynomial expression vanishes as required. Indeed, when counting independent triples in the line graph, start with all triples, subtract those containing each of its \(h\) edges, add triples containing each adjacent pair of line-graph edges (there are \(m\binom{2(d-1)}2\) such pairs), and subtract triples forming line-graph triangles.

Write \(F_r=\mathbb E[(X)_r]\) for falling-factorial moments. Differentiating (1) at \(z=1\) gives \(F_r=r!M_r(G)/d^{2r}\). Ordinary moments satisfy \(\mathbb E[X^2]=F_2+F_1\) and \(\mathbb E[X^3]=F_3+3F_2+F_1\). Hence

\[
\mu=F_1,\qquad
\sigma^2=F_2+F_1-F_1^2,
\]
\[
\kappa_3=F_3+3F_2+F_1-3F_1(F_2+F_1)+2F_1^3.
\tag{3}
\]

Substitute (2) into (3), using \(m=nd/2\) and \(h=m(d-1)\); collecting terms yields precisely the three cumulant formulas in the finding. In particular, the only host-dependent contribution to \(\kappa_3\), when \(n,d\) are fixed, is \(-6t(G)/d^6\).

Since \(\mu>0\), the ratio \(\sigma^2/\mu=(1-1/d)^2\) lies in \([0,1)\) and is strictly increasing in positive integer \(d\). Taking the nonnegative square root uniquely recovers \(d\); the formulas for \(n\) and \(t(G)\) then follow algebraically, including \(d=1\).

For the sign classification, when \(d=1\) the graph is a disjoint union of edges, so \(t=0\) and \(\kappa_3=0\). When \(d=2\), \(\kappa_3=-3t/32\). When \(d=3\), \(\kappa_3=2(n-t)/243\), and \(t\le n\) because each vertex lies in at most three triangles; equality means that every neighborhood is a triangle, forcing each component to be \(K_4\). Finally, for all \(d\ge4\), each vertex lies in at most \(\binom d2\) triangles, so \(t\le n d(d-1)/6\) and

\[
\kappa_3\ge\frac{n(d-1)}{2d^5}\bigl((d-1)(d-2)^2-2\bigr)>0.
\]

## Verification

The standalone standard-library script `verify.py` computes the law in two independent ways: direct exhaustive enumeration of every vertex's neighbor choices and exact coefficient extraction from the matching expansion (1). For sixteen graphs, including cycles, complete graphs, bicliques, the Petersen graph, the cube, the triangular prism, and disconnected regular graphs, it checks all probability masses, moments, inverse formulas, and sign claims using rational arithmetic. Running `python3 verify.py` produced `VERIFY_OK 301 exact rational assertions`. These finite checks corroborate the algebraic identities; the preceding proof establishes them for all finite admissible graphs.

## Relationship to prior work

Leckey and Wormald (2018) study random functional digraphs with prescribed indegree profiles and their orbit lengths. Wang and Resnick (2021) analyze reciprocity in a growing preferential-attachment digraph. Neither model has independent uniform outgoing neighbor choices restricted to an arbitrary fixed regular graph, and neither paper reports the cumulant-based inverse recovery of degree and triangle count.

Davies, Jenssen, and Perkins (2020 preprint; revised 2021) study matching polynomials of regular graphs, and explicitly use third-order matching-cluster terms involving triangles. That established matching enumerative framework is closely related to (1), and its third-order terms anticipate the combinatorial mechanism underlying the new formulas. The contribution here is the exact probabilistic identification and sign classification for reciprocal one-neighbor selections, **not** a new matching-enumeration theorem. The simple matching-polynomial reduction also leaves a historical-priority risk from other work on random mappings.

## Limitations

The three cumulants recover \(n,d,t(G)\), not the graph's isomorphism type or its higher subgraph counts. They are theoretical population cumulants: no robustness or estimation error bound from finitely many independent samples is asserted. Dependence between vertices' choices, irregular degrees, loops, or multiple edges are outside the stated theorem. The identity may be derivable from older matching-polynomial or random-mapping literature; a full historical-priority determination and independent proof review have not been performed.

## References

- K. Leckey and N. Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence*, arXiv:1803.02667, first posted 2018-03-07. https://arxiv.org/abs/1803.02667
- E. Davies, M. Jenssen, and W. Perkins, *A proof of the Upper Matching Conjecture for large graphs*, arXiv:2004.06695, first posted 2020-04-14. https://arxiv.org/abs/2004.06695
- T. Wang and S. I. Resnick, *Measuring Reciprocity in a Directed Preferential Attachment Network*, arXiv:2103.07424, first posted 2021-03-12. https://arxiv.org/abs/2103.07424
