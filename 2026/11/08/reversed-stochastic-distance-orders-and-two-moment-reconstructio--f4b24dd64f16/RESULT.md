# Reversed stochastic distance orders and two-moment reconstruction for unit-edge bipartite metric graphs

## Finding

For positive integers \(p,q\), form the unit-edge **metric graph** \(G_{p,q}\) by replacing each edge of the complete bipartite graph \(K_{p,q}\) with a closed interval of length one, with the intrinsic shortest-path metric. Let \(D_{p,q}=d(X,Y)\) for independent points distributed according to normalized arclength on \(G_{p,q}\). Put \(n=p+q\), \(P=pq\), and \(F_{p,q}(r)=\Pr(D_{p,q}\le r)\). The complete distance law is

\[
F_{p,q}(r)=\begin{cases}
0,&r<0,\\
\dfrac{2r+(n-4)r^2/2}{P},&0\le r\le1,\\
1-\dfrac{(n-2)(2-r)^2/2+(P-n+1)\{2(2-r)-(2-r)^2\}}{P},&1\le r\le2,\\
1,&r\ge2.
\end{cases}
\]

In particular,
\[
\mu=\mathbb E D_{p,q}=\frac53-\frac{2n}{3P},\qquad
m_2=\mathbb E D_{p,q}^2=\frac{17}{6}-\frac{5n-2}{3P}.
\]
The two moments alone recover the isometry type in this family: with \(\Delta=6m_2+8-15\mu\),
\[
P=\frac4\Delta,\qquad n=\frac{2(5-3\mu)}\Delta,
\]
then \(\{p,q\}\) are the two roots, counted with multiplicity, of \(z^2-nz+P=0\). This includes the star cases and the single-edge graph.

For any fixed integer \(n\ge4\), as \(p\) increases from \(1\) through \(\lfloor n/2\rfloor\), the **arclength-uniform** distance becomes strictly larger in first-order stochastic order: \(F_{p,n-p}(r)\) strictly decreases at every \(0<r<2\) for each successive value of \(p\). Thus the star uniquely minimizes, and the balanced bipartition uniquely maximizes, every expectation \(\mathbb E\phi(D)\) with \(\phi\) strictly increasing and integrable. In contrast, when the two points are uniformly sampled from the **combinatorial vertices**, their distance becomes smaller in first-order stochastic order as the bipartition balances (strictly at thresholds \(1\le r<2\)). This is an exact sampling-measure reversal, not a change to the underlying shortest-path metric.

For \(0<\varepsilon<1\), the diameter tail has the exact expression
\[
\Pr(D_{p,q}>2-\varepsilon)=\frac{2(P-n+1)}P\varepsilon+
\frac{(n-2)/2-(P-n+1)}P\varepsilon^2.
\]
The linear term is positive precisely when both parts have at least two vertices. On a star \(K_{1,q}\) with \(q\ge2\), it vanishes and the tail is \(\frac{q-1}{2q}\varepsilon^2\). Thus the far-distance exponent distinguishes the presence of cycles in this family.

## Assumptions and scope

Every \(G_{p,q}\) has precisely \(P=pq\) unit edges and total length \(P\), and its sample law is arclength divided by \(P\). Distances are intrinsic, not ambient Euclidean distances. The two points are independent; graph vertices have arclength measure zero. Unless stated otherwise \(p,q\) are arbitrary positive integers, including \(p=q=1\); the strict fixed-order stochastic comparison requires \(n\ge4\). For sampled **vertices** the comparison uses independent uniform draws with replacement from the \(n\) original vertices. Equality of metric graphs means length-preserving isometry, not a chosen combinatorial labeling. For \(n=2\), the actual diameter is one; the upper part of the displayed CDF is nevertheless identically one.

## Proof

**Edge-pair trichotomy.** Two independent normalized-arclength points are obtained by independently choosing one of the \(P\) edges uniformly and then independent uniform positions on those edges. With probability \(1/P\) their edges coincide. With probability \((n-2)/P\) they are distinct and incident: for each edge, exactly \((p-1)+(q-1)=n-2\) other edges share one endpoint. The remaining probability is \((P-n+1)/P=(p-1)(q-1)/P\) and corresponds to disjoint edges. These are ordered-pair probabilities and exhaust all cases.

Write \(U,V\) for independent uniform variables on \([0,1]\). The intrinsic distances conditioned on these three events have laws
\[
D_{\rm same}\overset d=|U-V|,\qquad
D_{\rm incident}\overset d=U+V,\qquad
D_{\rm disjoint}\overset d=2-|U-V|.
\]
For incident edges the path through their shared endpoint is shortest; all alternative paths contain at least two extra unit-edge traversals. For disjoint edges, each of the two cross-part endpoint pairs is connected by a single edge, while the other two endpoint pairs require two edges. Minimizing the four endpoint-to-endpoint routes gives \(\min\{2+U-V,2-U+V\}=2-|U-V|\); this also holds for the four-cycle \(K_{2,2}\). For coincident edges, the segment within that edge is shortest. Degenerate endpoint coincidences are null events.

**CDF and density.** The three elementary CDFs, for \(0\le r\le1\), are \(A(r)=2r-r^2\), \(B(r)=r^2/2\), \(C(r)=0\). For \(1\le r\le2\) they are \(A(r)=1\), \(B(r)=1-(2-r)^2/2\), \(C(r)=(r-1)^2\). The mixture \(F_{p,q}=[A+(n-2)B+(P-n+1)C]/P\) yields the stated piecewise formula. Differentiation gives the density
\[
f_{p,q}(r)=\begin{cases}
\dfrac{2+(n-4)r}{P},&0<r<1,\\
\dfrac{(n-2)(2-r)+2(P-n+1)(r-1)}P,&1<r<2.
\end{cases}
\]
These pieces are nonnegative; integrating over the two unit intervals yields total probability one. Integrating \(rf_{p,q}(r)\) and \(r^2f_{p,q}(r)\) yields the displayed \(\mu\) and \(m_2\). Direct algebra gives \(6m_2+8-15\mu=4/P\), so the inverse formulas follow. Because the positive integers \(p,q\) are determined up to exchange by their sum and product, the distance moments identify precisely the unordered bipartition.

**Opposite stochastic orders.** For fixed \(n\), rearrange the mixture into
\[
F_{p,n-p}(r)=C(r)+\frac{A(r)+(n-2)B(r)-(n-1)C(r)}{p(n-p)}.
\]
For \(0<r<2\), the CDFs satisfy \(A(r)>C(r)\) and \(B(r)\ge C(r)\), so the numerator is strictly positive when \(n\ge2\). The product \(p(n-p)\) strictly increases over the integer range \(1\le p\le\lfloor n/2\rfloor\), proving the asserted strict first-order stochastic ordering and its unique extreme graphs up to swapping parts. For uniform independent combinatorial vertices, distance is zero on identical vertices, one on opposite-part vertices, and two on distinct same-part vertices. Hence for \(1\le r<2\) the vertex-distance CDF equals \((n+2P)/n^2\), strictly *increasing* with \(P\). For \(0\le r<1\) it equals \(1/n\) independently of \(P\). These opposite inequalities prove the measure-dependent reversal.

**Diameter tail.** Insert \(r=2-\varepsilon\) into the upper CDF branch. The linear coefficient \(2(P-n+1)/P\) vanishes iff \((p-1)(q-1)=0\). For a star, the remaining coefficient is \((n-2)/(2P)=(q-1)/(2q)\). This proves the exact tail and distinction.

## Verification

The standalone file `verify_bipartite_distances.py` samples actual continuous edge points and computes intrinsic distances using a Floyd–Warshall shortest-path calculation on the vertex graph, without reusing the case-mixture formula for the sampled distance. It checks the CDF at seven thresholds on eight different bipartitions, and the means. A symbolic integration component tests normalization, first and second moments and moment inversion on several bipartitions. Discrete algebraic checks also cover every integer order from 4 through 29 for strict CDF ordering and its reversal under vertex sampling. Execute `python verify_bipartite_distances.py` with Python 3 and SymPy installed (see `requirements.txt`). The executable tests do not replace the analytical proof above.

## Relationship to prior work

Sánchez (first posted August 2, 2011; primary MSC 51F99) explicitly calculates negative type for the **discrete vertex metric** of complete bipartite graphs, not normalized continuous edge-arclength distances. Lecci, Rinaldo and Wasserman (first posted May 6, 2013) investigate reconstruction of metric graphs from spatial data, rather than the exact arclength-uniform pair-distance law and the explicit order reversal for complete bipartite unit-edge spaces. Mémoli and Needham develop the general distance-distribution inverse-problem framework and limitations for metric-measure spaces, but the examined distance-density discussion does not supply this biclique formula or its two-moment inverse. Baptista, Kennedy and Mugnolo determine mean-distance properties of metric graphs, including an exact star case; the star mean is **not** claimed here as a new theorem. Shang treats average distances between *discrete vertices* of bipartite networks, corresponding to a different sampling measure and supporting the opposite vertex-order comparison. These are substantive comparisons, not an assertion that literature searching proves uniqueness.

## Limitations

The distribution and inverse characterization are confined to the family of intrinsically metrized complete bipartite graphs with **equal unit edge lengths** and normalized uniform arclength. They do not establish identifiability among all metric graphs or under arbitrary edge weights. The exact star expression is a consistency boundary already present in earlier mean-distance literature. Older or unindexed sources could contain equivalent biclique computations; independent priority validation has not been performed. Numerical results check finitely many configurations and samples only.

## References

1. M. Lecci, A. Rinaldo and L. Wasserman, *Statistical Analysis of Metric Graph Reconstruction*, arXiv:1305.1212 (first posted 2013-05-06). https://arxiv.org/abs/1305.1212 ; full text: https://www.jmlr.org/papers/volume15/lecci14a/lecci14a.pdf
2. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646 (2018). https://arxiv.org/abs/1810.09646
3. A. Baptista, J. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs* (2023 preprint; subsequent journal publication). https://arxiv.org/abs/2312.04952
5. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first posted 2011-08-02; primary MSC 51F99). https://arxiv.org/abs/1108.0451
4. Y. Shang, *Estimation of the Shortest Average Distance in Bipartite Networks with Given Density*, Journal of the Physical Society of Japan 80 (2011), DOI:10.1143/JPSJ.80.055001.
