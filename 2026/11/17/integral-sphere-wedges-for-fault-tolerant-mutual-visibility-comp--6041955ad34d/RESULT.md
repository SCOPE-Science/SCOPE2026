# Integral sphere wedges for fault-tolerant mutual-visibility complexes of complete bipartite graphs

## Finding

Let \(q\ge2\) and \(m,n\ge q+2\). For the simplicial complex \(\mathcal F_q(K_{m,n})\) of vertex sets supporting \(q\) internally vertex-disjoint, internally unobstructed shortest paths between every two selected nonadjacent vertices, put
\[
a=m-q,\quad b=n-q,\quad c_A=\binom{m-1}{q-1},\quad c_B=\binom{n-1}{q-1}.
\]
There is a **non-equivariant integral homotopy equivalence**
\[
|\mathcal F_q(K_{m,n})|\simeq
\bigvee^{c_Ac_B}S^{a+b-1}\;\vee\;
\bigvee^{(n-1)c_A}S^{a+1}\;\vee\;
\bigvee^{(m-1)c_B}S^{b+1}.
\]
When dimensions coincide, add their multiplicities. Thus all integral reduced homology is free, all groups outside these degrees vanish, and this describes the full homotopy type rather than only its Betti numbers.

The entire face polynomial, with the empty simplex contributing the constant term, is
\[
F_{m,n,q}(t)=
\left(\sum_{i=0}^{a}\binom mi t^i\right)
\left(\sum_{j=0}^{b}\binom nj t^j\right)
+(1+nt)\sum_{i=a+1}^{m}\binom mi t^i
+(1+mt)\sum_{j=b+1}^{n}\binom nj t^j.
\]
The inclusion of the rectangular skeleton-join core described below is split injective on reduced integral homology. Its relative homology is exactly the sum of the two extra sphere families. For instance, the redundancy-two complex on \(K_{4,4}\) is a wedge of \(27\) three-spheres, whereas for redundancy two on \(K_{5,6}\), it is a wedge of \(20\) four-spheres, \(20\) five-spheres, and \(20\) six-spheres.

## Assumptions and scope

The graph \(K_{m,n}\) is the finite undirected complete bipartite graph with disjoint vertex classes \(A\) and \(B\) of sizes \(m\) and \(n\). A set \(S\subseteq A\sqcup B\) is a face precisely when for each nonadjacent pair \(u,v\in S\) there are at least \(q\) shortest \(u,v\)-paths with pairwise disjoint interiors, none of whose interior vertices lie in \(S\). Adjacent pairs require no redundant paths; this is the \((q-1)\)-fault-tolerant mutual-visibility convention of Cicerone–Di Stefano–Klavžar–Zhang. The empty set and all singletons are faces.

The theorem assumes \(q\ge2\) and \(m,n\ge q+2\), so \(a,b\ge2\). The proof works also at \(q=1\), recovering a homotopy refinement of the previously characterized ordinary visibility family, but **the ordinary face classification is not a new contribution**. No statement is asserted for one class smaller than \(q+2\), for arbitrary multipartite graphs, or for equivariant homotopy splittings.

## Proof

**1. Exact face criterion.** Let \(i=|S\cap A|\) and \(j=|S\cap B|\). Distinct vertices in the same class are at graph distance two, and their shortest paths use precisely one vertex from the opposite class. For a selected pair in \(A\), the number of internally unobstructed, internally disjoint geodesics is exactly \(n-j\); for a selected pair in \(B\), it is \(m-i\). The condition is consequently
\[
(i\le1\ \text{or}\ j\le b)\quad\text{and}\quad
(j\le1\ \text{or}\ i\le a).
\]
Because \(a,b\ge2\), this is equivalent to
\[
(i\le a\text{ and }j\le b)\quad\text{or}\quad j\le1\quad\text{or}\quad i\le1.
\]
The three disjoint counting regions are the base rectangle and the two complementary bands \(i>a,\ j\le1\) and \(j>b,\ i\le1\). Their binomial enumeration yields the displayed polynomial.

**2. The simplicial decomposition.** Let \(\Delta_A,\Delta_B\) be full simplices; \(D_A,D_B\) the discrete complexes with exactly the indicated vertices; and let \(P_A=\operatorname{sk}_{a-1}\Delta_A\), \(P_B=\operatorname{sk}_{b-1}\Delta_B\), namely the complexes of subsets of size at most \(a\) and \(b\), respectively. The preceding criterion identifies the entire complex as
\[
K=K_0\cup C_A\cup C_B,
\quad K_0=P_A*P_B,
\quad C_A=\Delta_A*D_B,
\quad C_B=D_A*\Delta_B.
\]
Both \(C_A,C_B\) are contractible because each contains a full simplex as a join factor. Their intersections are
\[
K_0\cap C_A=L_A=P_A*D_B,\quad
K_0\cap C_B=L_B=D_A*P_B,
\quad C_A\cap C_B=D_A*D_B\subseteq K_0.
\]
In particular \((K_0\cup C_A)\cap C_B=L_B\). These are equalities of simplicial subcomplexes, so the unions are homotopy pushouts of cofibrations.

**3. Both attaching maps are null.** Since \(a,b\ge2\), the one-skeleta of \(P_A\) and \(P_B\) are complete graphs, so both skeletons are path connected. The inclusion \(D_B\hookrightarrow P_B\) is homotopic to a constant map: choose a path from each of the finitely many discrete vertices to one fixed vertex. Thus \(P_A*D_B\to P_A*P_B\) is homotopic to a map into the cone \(P_A*\{b_0\}\) and hence nullhomotopic. Symmetrically \(D_A*P_B\to P_A*P_B\) is nullhomotopic. Its composite inclusion into \(K_0\cup C_A\) is null as well. Since \(C_A,C_B\) are contractible, the two cofibration pushouts yield an inclusion-compatible homotopy splitting
\[
K\simeq K_0\vee\Sigma L_A\vee\Sigma L_B.
\]
All relevant base spaces are connected; their simplicial realizations are CW complexes. This splitting also shows that \(\widetilde H_*(K_0;\mathbb Z)\to\widetilde H_*(K;\mathbb Z)\) is split injective and identifies the relative summands.

**4. Evaluate the skeleton joins.** The rank-\(a\) uniform-matroid complex \(P_A\) is homotopy equivalent to \(\bigvee^{\binom{m-1}{a}}S^{a-1}\). One proof pairs every face not using a fixed pivot vertex with its pivot extension whenever that extension still has at most \(a\) vertices; the unpaired top faces are exactly the \(\binom{m-1}{a}\) size-\(a\) subsets avoiding the pivot. This is an acyclic matching, giving the stated wedge (with a distinguished vertex). Likewise \(P_B\simeq\bigvee^{\binom{n-1}{b}}S^{b-1}\). Since \(\binom{m-1}{a}=c_A\) and \(\binom{n-1}{b}=c_B\), joins distribute over wedges up to homotopy, while \(D_A\simeq\bigvee^{m-1}S^0\) and \(D_B\simeq\bigvee^{n-1}S^0\). Therefore
\[
K_0\simeq\bigvee^{c_Ac_B}S^{a+b-1},\qquad
\Sigma L_A\simeq\bigvee^{(n-1)c_A}S^{a+1},\qquad
\Sigma L_B\simeq\bigvee^{(m-1)c_B}S^{b+1},
\]
proving the claim for every specified integer triple.

## Verification

`VERIFY.py` computes the graph adjacencies and shortest paths directly, packs pairwise interior-disjoint geodesics by backtracking, and checks every nonempty vertex subset. It then independently builds the full simplicial boundary matrices over \(\mathbb F_2\), checks their ranks, and compares the resulting Betti numbers with the integral wedge prediction. `VERIFY_OUTPUT.txt` gives the exact recorded output for seven parameter triples, covering \(6149\) nonempty faces. The output includes the redundant-path count boundary \(q=1\) as a check but it does not enlarge the new claim. The infinite-family proof is structural and is not inferred from the finite enumeration.

## Relationship to prior work

Bujtás–Klavžar–Tian (arXiv:2412.03066, first public 2024-12-04), Proposition 3.2, gives the ordinary mutual-visibility face classification and visibility polynomial for balanced complete bipartite graphs. The ordinary \(q=1\) face condition is therefore **known** and is used solely as a consistency boundary. It does not imply the robustness-level \(q\ge2\) face complexes or their integral homotopy types.

Cicerone–Di Stefano–Klavžar–Zhang (arXiv:2512.01978, first public 2025-12-01), Definition 3.1, introduces the fault-tolerant version. Its Section 7 proves extremal cardinalities for Hamming and direct-product graph families, not a classification of complete bipartite fault-tolerant face complexes. The latter is a complete bipartite graph, not the categorical product of two complete graphs. Thus the present theorem has different objects and stronger topological conclusions. Relevant recorded work on total visibility and induced-degree complexes studies stronger/different face restrictions; these do not imply the present homotopy formula.

## Limitations

The theorem excludes sparse-shore cases \(m\le q+1\) or \(n\le q+1\), where the skeletons need not be path connected and the attachment argument changes. The homotopy equivalence is nonequivariant; no integral automorphism-module decomposition, persistence theorem, or arbitrary-graph classification is established. Mod-two calculations corroborate finite cases but do not independently prove the integral theorem. Bibliographic searches cannot exclude all unindexed or differently formulated prior derivations, especially those treating arbitrary joins or fault-tolerance complexes without visibility terminology.

## References

1. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (first public 2024-12-04), https://arxiv.org/abs/2412.03066; full article https://link.springer.com/article/10.1007/s00010-025-01197-y, Proposition 3.2.
2. S. Cicerone, G. Di Stefano, S. Klavžar, G. Zhang, *Fault-tolerant mutual-visibility: complexity and solutions for grid-like networks*, arXiv:2512.01978 (first public 2025-12-01), https://arxiv.org/html/2512.01978, Definition 3.1 and Section 7.
