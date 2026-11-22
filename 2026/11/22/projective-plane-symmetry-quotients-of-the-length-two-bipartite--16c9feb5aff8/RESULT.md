# Projective-plane symmetry quotients of the length-two bipartite enriched nerve

## Finding
Let \(a,b\ge1\), let \(X=V(K_{a,b})\) have the shortest-path metric, and let \(N_2(X)\) be the **inclusive ordered length nerve**: an \(n\)-simplex is a tuple \((x_0,\ldots,x_n)\) with \(\sum_{i=0}^{n-1}d(x_i,x_{i+1})\le2\). Its degenerate simplices are those with an adjacent repetition. Write \(H=S_a\times S_b\) for the independent within-part vertex permutations. Then

\[
|N_2(X)|\simeq\bigvee^{ab(a+b)-(a+b-1)^2}S^2,\qquad |N_2(X)|/H\simeq S^2.
\]

When \(a=b\), the full graph-automorphism group is \(H\rtimes C_2\), including exchange of the two parts, and

\[
|N_2(X)|/(H\rtimes C_2)\simeq \mathbb{RP}^2,
\quad H_1(|N_2(X)|/(H\rtimes C_2);\mathbb Z)\cong\mathbb Z/2.
\]

More precisely, if \(g\in H\) has \(f_A\) fixed points in the first part and \(f_B\) in the second, then
\[
\operatorname{tr}(g_*\mid H_2(|N_2(X)|;\mathbb Q))
=f_Af_B(f_A+f_B)-(f_A+f_B-1)^2.
\]
In the balanced case, every element exchanging the two parts has trace \(-1\) on rational second homology.

## Assumptions and scope
Distances between distinct vertices in opposite parts are \(1\); within one part they are \(2\). The length nerve here is an **ordered simplicial set**, not an unordered symmetrized length–Rips simplicial complex or the usual diameter-based Vietoris–Rips complex. We use genuine geometric orbit spaces of its realization, not chainwise invariants, homotopy quotients or quotient graphs. All statements hold for every pair of positive integers, including a part of size one. The wedge multiplicity is positive. A realization of a simplicial set is a CW complex, and its nondegenerate ordered simplices supply the open cells.

## Proof
**1. Cells and integral homology.** No nondegenerate simplex can have dimension greater than two, since each consecutive change costs at least one. Let \(n=a+b\). There are \(n\) zero-cells, \(n(n-1)\) directed one-cells, and \(a^2b+ab^2=abn\) two-cells, precisely the alternating ordered triples \((x,y,z)\) with \(x,z\) in one part and \(y\) in the other. Repetition of the first and last vertices is allowed and is **not** a degeneracy. Their cellular boundaries are
\[
\partial(x,y,z)=(y,z)-(x,z)+(x,y),
\]
where the middle edge \((x,z)\) is zero when \(x=z\), because the resulting one-simplex is degenerate. The one-cell differential is \(\partial(x,y)=y-x\).

The two-cells \((x,y,x)\) identify the directed edge \((y,x)\) with the inverse of \((x,y)\) in the fundamental group. The cells \((x,y,z)\) with \(x\ne z\) identify the same-part edge \((x,z)\) with the two-edge path through \(y\) in the opposite part. Thus the one-skeleton reduces, with its attaching relations, to the undirected complete bipartite graph. For each pair \(x,z\) in one part and \(y,y'\) in the other, the two routes from \(x\) to \(z\) through \(y\) and \(y'\) are identified. These are the four-cycle relations. Every cycle in a complete bipartite graph is a product of four-cycles (and the graph is a tree if a part has one vertex). Therefore \(\pi_1(|N_2(X)|)=1\).

Its Euler characteristic is \(n-n(n-1)+abn\), so its second Betti number equals
\[
R_{a,b}=n-n(n-1)+abn-1=abn-(n-1)^2.
\]
Because its cellular two-chains form a free abelian group and no three-cells exist, second homology is free of rank \(R_{a,b}\). A simply connected finite two-dimensional CW complex with free homology only in degree two is homotopy equivalent to a wedge of that many two-spheres: choose maps representing an integral basis by Hurewicz and apply Whitehead's homology theorem. This proves the first assertion, integrally, including \(a=b=1\).

**2. Within-part orbit-space CW model.** The action of \(H\) sends each open cell to a different cell unless it fixes the entire ordered tuple. Consequently the geometric quotient has open cells indexed by orbits of ordered nondegenerate tuples, with the same signed attaching boundaries. It has two vertex orbits, \(A,B\); directed cross-edges \(s:A\to B\) and \(t:B\to A\); and, when \(a\ge2\) or \(b\ge2\), respectively, same-part edge loops \(u:A\to A\) or \(v:B\to B\). Its two-cells are \(p=(A,B,A)\), \(q=(B,A,B)\), and optionally \(p'=(A,B,A')\) and \(q'=(B,A,B')\) with distinct endpoint vertices. The boundaries are
\[
\partial p=s+t,\quad\partial q=t+s,
\quad\partial p'=s+t-u,\quad\partial q'=t+s-v.
\]
Here the boundary equations give the actual characteristic-map circuits, including the cancellation pairs. Each optional edge \(u\) occurs on the boundary of exactly one two-cell orbit \(p'\), and likewise \(v\) for \(q'\). Elementary CW collapses remove these free pairs. The remaining complex consists of two vertices and two oppositely directed edges making a circle, with two discs \(p,q\) attached by degree-one maps along that circle. It is a two-sphere. Thus \(|N_2(X)|/H\simeq S^2\).

**3. Part exchange.** In the balanced case the involution \(\tau\) induced on the \(H\)-quotient exchanges \(A\leftrightarrow B\), \(s\leftrightarrow t\), \(p\leftrightarrow q\), and the optional free pairs \((u,p')\leftrightarrow(v,q')\). The collapses in the previous paragraph can be performed simultaneously on the exchanged free pairs and hence equivariantly. On the remaining two-sphere CW model, \(\tau\) exchanges every open cell with a distinct open cell, hence acts freely. A free involution on \(S^2\) has quotient homeomorphic to \(\mathbb{RP}^2\) (e.g. by the classification of connected two-fold coverings of surfaces). The equivariant collapse descends to a homotopy equivalence of geometric quotients. It follows that \(|N_2(X)|/(H\rtimes C_2)\simeq\mathbb{RP}^2\), with \(H_1\cong\mathbb Z/2\).

**4. Rational character.** An element \(g\in H\) fixes exactly \(f=f_A+f_B\) vertices, \(f(f-1)\) directed nondegenerate edges, and \(f_Af_B(f_A+f_B)\) alternating two-cells. The cellular Lefschetz number is therefore \(f-f(f-1)+f_Af_Bf\). Since ordinary rational homology is nonzero only in degrees zero and two, the trace on second homology is this number minus one, equal to the displayed character. An element interchanging parts fixes no nondegenerate ordered cell in any dimension, so its Lefschetz number is zero and its second-homology trace is \(-1\).

## Verification
The accompanying Python program `verify_enriched_bipartite.py` enumerates all nondegenerate ordered tuples of total length at most two, constructs the signed normalized boundary matrices, and tests \(\partial_1\partial_2=0\). For \((a,b)=(1,1),(1,2),(2,2),(2,3),(3,3),(3,4)\), it checks degree-zero, -one and -two Betti numbers over \(\mathbb F_{101}\) and \(\mathbb F_2\) for the original realization and the within-part geometric orbit spaces. For balanced sizes \(1,2,3\), it also computes the full shore-exchanging quotient; its rational homology is \((1,0,0)\) and mod-two homology is \((1,1,1)\), as required for \(\mathbb{RP}^2\). The run prints `ALL CHECKS PASSED`. This finite computation is a check, not a substitute for the all-parameter proof.

## Relationship to prior work
Melodia, *Persistent Magnitude Homology for Quantitative Equational Theories* (first public 21 August 2026, arXiv:2608.21479), shows that the length-filtered nerve produces persistent magnitude homology, including exact-sequence and stability comparisons. Ivanov and Xu, *On \(\ell_p\)-Vietoris-Rips complexes*, Section 2.3, explicitly distinguish the ordered \(\ell_1\) simplicial set defining blurred magnitude homology from the symmetric finite-subset simplicial complex; the former is our object. These papers do not identify the present complete-bipartite two-stage homotopy types or the effect of part-exchange geometric quotients.

The published classification *Complete integral length–Rips persistence of complete bipartite graph metrics* studies the **unordered symmetrized finite-subset** complex and explicitly excludes the ordered blurred-magnitude simplicial set. In particular its length-two stage for \(K_{1,1}\) is contractible, while the present ordered nerve is \(S^2\); its conclusions therefore do not imply our theorem. Livernet–Roff–Whitehouse, *Homotopy theories via the magnitude-path spectral sequence*, supplies broader magnitude/path machinery but not this geometric orbit classification. Searches of accessible mathematical records and primary literature did not identify a statement implying the present coupled family of homotopy and equivariant quotient results. The absence of a search hit is not a guarantee of global originality.

## Limitations
Only the **inclusive scale-two ordered** length nerve of the unit-edge complete bipartite shortest-path metric is classified. The theorem does not give the complete persistence barcode, arbitrary bipartite graph classifications, integral decomposition of the full permutation representation, or arbitrary subgroup orbit spaces. The quotient description uses ordinary geometric orbit spaces, not Borel homotopy quotients. Classification of other natural group actions is open. Publication-priority searches are necessarily incomplete, and no independent mathematical audit has been performed.

## References
1. Luciano Melodia, *Persistent Magnitude Homology for Quantitative Equational Theories*, arXiv:2608.21479, first public 2026-08-21, https://arxiv.org/abs/2608.21479.
2. Sergei O. Ivanov and Xiaomeng Xu, *On \(\ell_p\)-Vietoris-Rips complexes*, arXiv:2411.01857, https://arxiv.org/abs/2411.01857; Journal of Applied and Computational Topology, https://doi.org/10.1007/s41468-026-00247-x, especially Section 2.3.
3. Muriel Livernet, Emily Roff and Sarah Whitehouse, *Homotopy theories via the magnitude-path spectral sequence*, arXiv:2606.09747, first public 2026-06-08, https://arxiv.org/abs/2606.09747.
4. *Complete integral length–Rips persistence of complete bipartite graph metrics*, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-complete-integral-length-rips-persistence-of-complete-bipartite--78d3fc3f10bf/RESULT.md.
