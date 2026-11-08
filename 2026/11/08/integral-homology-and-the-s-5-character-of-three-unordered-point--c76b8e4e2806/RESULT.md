# Integral homology and the \(S_5\)-character of three unordered points on \(K_5\)

## Finding
For the geometric complete graph \(K_5\), let \(B_3(K_5)\) be the space of unordered subsets of exactly three distinct points. Its complete integral homology is
\[
H_i(B_3(K_5);\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^6\oplus\mathbb Z/2,&i=1,\\
\mathbb Z^{30},&i=2,\\
0,&i\ge3.
\end{cases}
\]
The vertex-permutation group \(S_5\) acts on rational homology. With \(S^\lambda\) denoting the irreducible rational Specht module of partition \(\lambda\vdash5\),
\[
H_1(B_3(K_5);\mathbb Q)\cong S^{(3,1,1)},\qquad
H_2(B_3(K_5);\mathbb Q)\cong S^{(4,1)}\oplus S^{(3,2)}\oplus 2S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}.
\]
The second-homology trace equals \(30\) on the identity, \(-2\) on elements of cycle type \((2,2,1)\), and zero on all other elements. In particular \(H_2(B_3(K_5);\mathbb Q)^{S_5}=0\).

## Assumptions and scope
The underlying graph is the geometric realization of the simple complete graph on vertices \(0,1,2,3,4\); particles are unordered and may move continuously on edges, but may never coincide. The group \(S_5\) acts by permuting the original graph vertices (and hence the points along its edges). No particle-number variation or equivariant homotopy splitting is asserted.

Each original graph edge is subdivided once, yielding a graph with fifteen vertices and twenty edges. Distinct original vertices have graph distance two in this subdivision, and every simple noncontractible cycle has length at least six. For three particles these satisfy the Prue–Scrimshaw sufficient-subdivision inequalities: essential-to-essential paths of length at least two and essential cycles of length at least four. The resulting unordered Abrams cubical complex is included \(S_5\)-equivariantly and is a homotopy model for the configuration space. An equivariant inclusion that induces an ordinary homology isomorphism also induces an isomorphism of \(S_5\)-modules.

A cubical \(k\)-cell is an unordered selection of three pairwise closure-disjoint vertex and open-edge cells, exactly \(k\) of which are edges. Orient a cube by sorting its moving edges by the index of their oriented edge in a fixed global list; each graph edge is oriented from its lesser to its greater numbered endpoint. Boundary signs are the usual alternating product-cube signs.

## Proof
**Integral chain calculation.** Complete enumeration gives cubical chain ranks \((455,1560,1650,520)\) in degrees \(0,1,2,3\). Both compositions \(d_1d_2\) and \(d_2d_3\) vanish coefficientwise over the integers. The one-skeleton is connected and \(d_1\) is an ordinary oriented incidence map, so its Smith factors are \(454\) copies of \(1\).

For \(d_2\), integer-preserving unit-pivot elimination splits off \(1098\) independent unit factors, leaving a \(23\)-row, \(37\)-column integer residual matrix. Direct Smith normal form of that actual residual has nonzero factors \((1,2)\). Thus the complete nonzero Smith factors of \(d_2\) are \(1099\) copies of \(1\) and one \(2\); its rank is \(1100\).

For \(d_3\), unit-pivot elimination produces \(520\) unit pivots and no residual. Hence \(d_3\) is injective and its image is a primitive (direct-summand) sublattice of \(C_2\). It follows that \(H_2=\ker d_2/\operatorname{im}d_3\) is torsion-free, because it injects into the free abelian group \(C_2/\operatorname{im}d_3\). Rank computations then give \(b_1=1560-454-1100=6\) and \(b_2=1650-1100-520=30\). The torsion of \(H_1\) is exactly the torsion of \(C_1/\operatorname{im}d_2\), since the quotient by \(H_1\) is the free group \(\operatorname{im}d_1\). Therefore it is \(\mathbb Z/2\). There are no cells above degree three, and \(d_3\) is injective.

**First-homology symmetry.** Summing the paths traveled by all three particles gives a natural \(S_5\)-equivariant morphism from the first homology of the configuration space to the first homology of the underlying graph. For each original triangle, park two particles on its two complementary original vertices and let the remaining particle travel once around the triangle. The ten resulting loops map onto the triangle cycle classes, which span \(H_1(K_5;\mathbb Q)\). Both spaces have first rational homology of dimension six, so the map is an equivariant isomorphism. The graph cycle representation is \(\ker(\mathbb Q^{10}\rightarrow\mathbb Q^5)\), equivalently \(S^{(3,1,1)}\).

**Second-homology symmetry.** For each of the 120 vertex permutations, the program counts its fixed cubical generators with orientation signs. A fixed cube contributes the sign of the permutation of its moving edge factors multiplied by the signs of any reversed oriented edges. Let \(L(g)=\sum_{k=0}^3(-1)^k\operatorname{tr}(g\mid C_k)\). Since the only rational homology is in degrees zero, one and two, the equivariant Euler–Poincaré identity gives
\[
\operatorname{tr}(g\mid H_2)=L(g)-1+\operatorname{tr}(g\mid H_1(K_5;\mathbb Q)).
\]
The latter trace is the oriented-edge trace minus the vertex-permutation trace plus one. In the standard conjugacy-class order, the following table gives the exact values:

| Cycle type | Class size | Trace on \(H_1\) | Trace on \(H_2\) |
|:---|---:|---:|---:|
| \((1,1,1,1,1)\) | 1 | 6 | 30 |
| \((2,1,1,1)\) | 10 | 0 | 0 |
| \((2,2,1)\) | 15 | -2 | -2 |
| \((3,1,1)\) | 20 | 0 | 0 |
| \((3,2)\) | 20 | 0 | 0 |
| \((4,1)\) | 30 | 0 | 0 |
| \((5)\) | 24 | 1 | 0 |

The Murnaghan–Nakayama character rule and character orthogonality now give the displayed Specht decomposition. All seven multiplicities are nonnegative integers; their weighted dimensions sum to thirty. The trivial-representation multiplicity is zero.

## Verification
The standalone `k5_three_point_verify.py` (Python 3.10+ and SymPy) constructs all cubical cells, all signed integer boundary matrices, validates the chain identities, performs the integral unit-pivot reductions, and takes the Smith form only of the actual residual \(23\)-by-\(37\) matrix. It also verifies ten explicit triangle cycles and commutation of differential and action for a generating set of adjacent transpositions, computes all 120 signed equivariant Euler traces, and independently reconstructs the seven irreducible characters using rim-hook removal. Executing the included program reproduces `k5_three_point_verify.out`, whose success marker is `K5_UNORDERED_THREE_POINT_INTEGRAL_AND_S5_CHARACTER_PASS`. No numerical tolerance or extrapolation from finite fields is used.

## Relationship to prior work
Farley–Sabalka (2004 preprint; 2005 paper) and Prue–Scrimshaw (2009 preprint) provide the cubical model and subdivision framework, without this specific second-homology symmetry calculation. Ko–Park (2011 preprint) establish a general first-homology formula for graph braid groups: the first integral homology is not claimed as new here. Maciążek–Sawicki (2019, full open-access article, especially Sections 5.1, 5.3, 5.5 and 5.6) give universal cycles and relations for wheel graphs, \(K_{3,3}\), and \(K_{2,p}\), but not this classification of \(B_3(K_5)\).

Ramos–Yun, *Computing stable homology representations of graph configuration spaces* (June 11, 2026 preprint), is particularly close. Its Table 8 gives the \(S_5\)-representation of **ordered** three-point configuration homology of \(K_5\), while its Theorem 4.4 concerns certain stable multiplicities of the ordered problem. Their ordered \(S_5\)-module by itself does not determine the \(S_5\)-module of the unordered quotient: that requires the commuting particle-permutation action and its invariant subspace, not supplied by their Table 8. The present calculation independently evaluates the unordered cubical chain action and additionally proves the integral Smith form. Thus the two results have overlapping objects and methods but distinct stated representations and integral conclusions.

## Limitations
This is an exact finite case, not a uniform calculation for all complete graphs or all particle counts. The rational \(S_5\)-representation is determined, but integral \(\mathbb Z[S_5]\)-module extension data and an equivariant homotopy type are not. Published and indexed literature was checked, including closely related 2026 ordered-space work, but an unidentified equivalent treatment or derivation from a stronger uninspected result remains possible. No independent mathematical audit has been performed.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first public 25 October 2004; Algebraic & Geometric Topology 5 (2005), 1075–1109.
2. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first public 30 September 2009.
3. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first public 13 January 2011; Discrete & Computational Geometry 48 (2012), 915–963.
4. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, DOI:10.1007/s00220-019-03583-5.
5. E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1, 11 June 2026, especially Section 4 and Table 8.
