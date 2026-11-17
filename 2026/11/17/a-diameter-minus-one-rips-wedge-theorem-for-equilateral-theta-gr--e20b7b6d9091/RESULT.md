# A diameter-minus-one Rips wedge theorem for equilateral theta graphs

## Finding

For integers \(m\ge2\) and \(L\ge2\), let \(\Theta_{m,L}\) be the finite simple graph consisting of \(m\) internally vertex-disjoint paths, each with exactly \(L\) edges, between the same two poles. Equip its \(2+m(L-1)\) vertices with the unit-edge shortest-path metric. Then the **inclusive graph-vertex Vietoris–Rips complex one unit below the diameter** has integral homotopy type

\[
\operatorname{VR}_{\le L-1}(\Theta_{m,L})\simeq
\bigvee^{(m-1)^{\lfloor L/2\rfloor}} S^{L-1}.
\]

This is an explicit exact simplicial-join decomposition, not merely a Betti-number computation. In particular the unique nonzero reduced integral homology group has degree \(L-1\), is free of rank \((m-1)^{\lfloor L/2\rfloor}\), and dies when the filtration reaches scale \(L\), at which point the complex is a full simplex. No claim is made about all intermediate filtration stages.

For the natural action of arm permutations \(\mathfrak S_m\) and simultaneous reversal of all arms \(C_2\), put
\(A_m=\ker(\mathbb Z^m\xrightarrow{\sum}\mathbb Z)\) and \(k=\lfloor L/2\rfloor\). The **integral** top-homology representation is

\[
\widetilde H_{L-1}(\operatorname{VR}_{\le L-1};\mathbb Z)
\cong A_m^{\otimes k}\boxtimes\varepsilon_L,
\quad
\varepsilon_L(\text{pole reversal})=
\begin{cases}(-1)^k,&L\text{ even},\\(-1)^{k+1},&L\text{ odd}.
\end{cases}
\]

The action exists for every \(m\ge2\); it is the full graph automorphism action when \(m\ge3\). Thus the new general regime \(L\ge5\) exhibits arbitrarily high sphere dimensions, exponential homology multiplicities, and a four-residue pole-reversal orientation pattern.

## Assumptions and scope

Name the poles \(p,q\) and the internal vertex on arm \(i\) at distance \(a\) from \(p\) by \(v_{i,a}\), with \(1\le i\le m\) and \(1\le a<L\). The edges are exactly those between successive vertices along these paths; no extra chords are allowed. Graph distances are measured **only between vertices** (not points in the continuous metric-graph realization). A finite subset is a Rips face precisely when all its pairwise distances are at most the stated threshold; there is no radius-doubling convention.

For a graph \(H\), denote its independence complex by \(\operatorname{Ind}(H)\). Let \(C_m=K_{m,m}\setminus M_m\) be the crown graph obtained by deleting one perfect matching from a complete bipartite graph, and let \(D_m=\operatorname{Ind}(C_m)\). Let \(E_m\) be a discrete set of \(m\) points.

## Proof

**1. Distances and the forbidden-pair graph.** The diameter is \(L\). The two poles have distance \(L\). On a common arm, two vertices \(v_{i,a},v_{i,b}\) are at distance \(|a-b|\), and from the poles the distances are \(a\) and \(L-a\). For vertices on distinct arms,

\[
d(v_{i,a},v_{j,b})=\min\{a+b,\ 2L-a-b\}\qquad(i\ne j).
\]

Every route between distinct arms passes through one of the poles; the displayed two routes attain the minimum. Consequently two vertices are at distance exactly \(L\) if and only if they are the two poles, or they are on distinct arms at complementary levels \(a+b=L\). The middle level \(a=b=L/2\), when integral, also gives all pairs of distinct arm labels at that level. No other pair is excluded from the threshold-\((L-1)\) graph.

**2. Exact factorization.** The graph of forbidden Rips edges (the distance-\(L\) graph) is a disjoint union of: one \(K_2\) on the poles; one crown graph \(C_m\) for each pair of distinct complementary levels \(a,L-a\); and, if \(L\) is even, one \(K_m\) on its middle level. A flag complex is the independence complex of the complement of its one-skeleton, and independence complexes turn disjoint unions into simplicial joins. Hence there are literal abstract-simplicial identities

\[
\operatorname{VR}_{\le L-1}(\Theta_{m,L})\cong
\begin{cases}
S^0*D_m^{*k},&L=2k+1,\\
S^0*D_m^{*(k-1)}*E_m,&L=2k.
\end{cases}
\]

Here \(D_m^{*0}\) is the unit for simplicial joins. This decomposition is valid even for the boundary \(m=2\), when the graph is a cycle.

**3. The crown factor.** The only independent vertex sets in \(C_m\) either lie wholly in one of its two shores or are the two matched vertices \(\{x_i,y_i\}\). Thus \(D_m\) is the union of two disjoint full \((m-1)\)-simplices and \(m\) bridging edges. Contracting each full simplex to a point is a homotopy equivalence of finite CW complexes, since each is a contractible cofibrant subcomplex. The quotient is a connected graph with two vertices and \(m\) parallel edges. Therefore \(D_m\simeq\bigvee^{m-1}S^1\), integrally, and \(E_m\simeq\bigvee^{m-1}S^0\). Applying the join–suspension identity and integral Künneth formula, with no torsion terms, to the exact decomposition proves the claimed sphere wedge and dimension for both parities of \(L\).

**4. Integral equivariance.** Orient the \(m\) bridges of \(D_m\) from the first shore to the second. Every integer one-cycle has bridge coefficients summing to zero; conversely every integer vector with sum zero occurs as bridge coefficients after completing paths inside the contractible shores. Hence \(H_1(D_m;\mathbb Z)\cong A_m\), with arm permutations permuting coordinates and shore interchange acting by minus one. Similarly \(\widetilde H_0(E_m;\mathbb Z)\cong A_m\). The poles give \(\widetilde H_0(S^0;\mathbb Z)\cong\mathbb Z\), on which pole reversal acts by minus one. Reversing all arms swaps the two shores within **each** crown factor and fixes the even-length middle factor. Thus pole reversal contributes \((-1)^{k+1}\) for odd \(L\), and \((-1)^k\) for even \(L\). Arm permutations act diagonally on the \(k\) augmentation factors. Natural reduced-join Künneth isomorphisms yield the stated integral tensor-power module. For \(m\ge3\), precisely the poles have degree \(m\), so the full automorphism group is \(\mathfrak S_m\times C_2\).

**5. Exact enumerative consequence.** Writing \(F(t)=\sum_{\sigma}t^{|\sigma|}\), with the empty face included, put \(Q_m(t)=2(1+t)^m-1+mt^2\). Since face polynomials multiply under joins, the whole Rips complex has exact face polynomial

\[
F(t)=\begin{cases}
(1+2t)Q_m(t)^k,&L=2k+1,\\
(1+2t)(1+mt)Q_m(t)^{k-1},&L=2k.
\end{cases}
\]

In particular the total number of faces **including the empty face** is \(3(2^{m+1}-1+m)^k\) for odd \(L\), and \(3(m+1)(2^{m+1}-1+m)^{k-1}\) for even \(L\). For \((m,L)=(3,5)\) and \((4,5)\), these counts are \(972\) and \(3675\). The dimension, homology rank, and symmetry conclusion do not rely on these finite counts.

## Verification

The accompanying standard-library checker `theta_last_radius_verify.py` independently rebuilds shortest-path metrics and verifies all maximal-distance pairs and their crown/discrete block structure for every \(2\le m\le5\), \(2\le L\le9\): 32 parameter pairs. For 24 cases with at most 23 graph vertices, it independently enumerates all Rips faces and checks the full face-count formula, covering 160155 face instances. A separate signed simplicial Lefschetz computation verifies 90 natural arm-permutation/pole-reversal character values, including both length parities. The literal verification output is in `verification_output.txt`. These are finite corroborations; the all-parameter proof is Steps 1–5.

## Relationship to prior work

Adams, Adetowubo, Barriga-Acosta, Feng, and Sterling [1] study graph-vertex Vietoris–Rips complexes of finite torus grids, including high-dimensional sphere phenomena at their last nontrivial radius; their underlying graphs are Cartesian products of cycles, not parallel-path theta graphs. Adamaszek [2] proves graph-power collapse for girth at least \(3r+1\) and studies cycle powers. Here the girth is \(2L\), which **does not satisfy** his stability hypothesis at \(r=L-1\) when \(L\ge3\); his cycle-power results include the two-arm boundary only.

Previously published technical results classify the equal-arm length-three and length-four theta cases [3,4]. The length-four result gives the \((m-1)^2\) three-sphere wedge and tensor-square homology, but assumes exactly four edges per arm. The new theorem treats **all** integer arm lengths, adds a general \(k\)-fold augmentation tensor lattice and proves the parity-dependent orientation character. A distinct mixed three-/five-edge theta result [5] assumes at least two length-three arms and is not an implication for the all-equal length-five graph (its diameter and last active radius differ). Literature and indexed-record comparisons cannot exclude an unindexed equivalent general result.

## Limitations

Only equal-length, unit-edge, internally disjoint theta paths and vertex shortest-path metrics are covered. The theorem classifies the penultimate integer radius, not the entire persistence filtration or metric-graph realizations. The full automorphism-group assertion requires \(m\ge3\); for \(m=2\) the natural subgroup action is still covered. The equivalence is ordinary integral homotopy equivalence, not an equivariant homotopy equivalence. No independent mathematical validation has been performed.

## References

[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (first public 2025-02-10). https://arxiv.org/abs/2502.07134

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), especially Proposition 2.2 and Section 6. https://arxiv.org/html/1104.0433v3

[3] *Complete Vietoris–Rips persistence and symmetry of three-edge theta graphs*, public technical record dated 2026-10-11, identifier c282838fbdca.

[4] *Square-growth third homology and full symmetry of four-edge theta Rips filtrations*, public technical record dated 2026-11-08, identifier 5f57307aa768.

[5] *Four consecutive Rips barcode dimensions for mixed three- and five-edge theta graphs*, public technical record; the mixed-arm assumptions and claim were compared directly.
