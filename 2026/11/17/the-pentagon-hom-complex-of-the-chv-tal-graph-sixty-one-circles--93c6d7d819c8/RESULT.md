# The pentagon Hom complex of the Chvátal graph: sixty-one circles and a dihedral character

## Finding

Let \(H\) be the standard twelve-vertex Chvátal graph, specified by the 24 edges below, and let \(C_5\) be the loopless cycle on five ordered vertices. The ordinary polyhedral graph-Hom complex satisfies
\[
\boxed{\operatorname{Hom}(C_5,H)\simeq\bigvee^{61} S^1.}
\]
More precisely, **280 elementary collapses of regular CW cells** remove all the two- and three-dimensional cells, leaving a connected graph with 440 vertices and 500 edges. Thus \(\pi_1\) is free of rank 61, \(H_1(-;\mathbb Z)\cong\mathbb Z^{61}\), and all integral higher homology vanishes.

The full graph automorphism group is a dihedral group of order eight. Writing \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), the induced rational first-homology character has values
\[
\begin{array}{c|ccccc}
\text{class}&1&r^2&\{r,r^3\}&\{s,r^2s\}&\{rs,r^3s\}\\\hline
\operatorname{tr}_{H_1}&61&1&1&-9&1.
\end{array}
\]
Equivalently,
\[
H_1(\operatorname{Hom}(C_5,H);\mathbb Q)
\cong6A_1\oplus10A_2\oplus5B_1\oplus10B_2\oplus15E,
\]
where the one-dimensional characters \(A_1,A_2,B_1,B_2\) give \((r,s)=(+,+),(+,-),(-,+),(-,-)\), respectively, and \(E\) is the standard two-dimensional rational representation of \(D_4\). This decomposition is over \(\mathbb Q\), not a claimed splitting of integral lattices.

## Assumptions and scope

The target is the simple undirected loopless graph \(H\) on vertices \(0,\ldots,11\) with the following **complete** edge list; the order of each edge is immaterial:

```text
01 04 06 09 12 15 17 23 26 28 34 37
39 45 48 5-10 5-11 6-10 6-11 78 7-11 8-10 9-10 9-11
```

It is triangle-free and 4-regular, but contains the four-cycle \(5,10,6,11,5\). This non-square-free boundary case is essential to the motivation.

A \(q\)-cell of \(\operatorname{Hom}(C_5,H)\) is an ordered five-tuple of nonempty target-color subsets \(\eta=(A_0,\ldots,A_4)\) with each pair \(A_i,A_{i+1}\) completely adjacent in \(H\), cyclically. Its closure is the product \(\prod_i\Delta(A_i)\), of dimension \(q=\sum_i(|A_i|-1)\). Cellular faces replace exactly one \(A_i\) by a nonempty subset. A codimension-one facet removes one element of a nonsingleton \(A_i\). A graph-Hom vertex is an ordinary graph homomorphism.

For the explicit dihedral generators, give images of vertices \(0,\ldots,11\) in that order:

```text
r = (1,5,11,6,0,4,7,10,9,2,3,8)
s = (0,4,3,2,1,5,9,8,7,6,11,10)
```

## Proof

**1. Complete enumeration, with two independently formulated methods.** One implementation lists every length-five closed walk in \(H\), regarded as singleton-valued Hom cells, and repeatedly inserts each individually admissible target color in any one coordinate. All cells are obtained this way: for any valid cell, select one color from each coordinate and add the remaining colors one at a time; every intermediate choice is a face of that cell. A second independent enumeration starts with the 110 distinct nonempty subsets of four-vertex neighborhoods, constructs the complete-adjacency transition relation, and counts every closed sequence of five such subsets directly. Both produce the **same explicit set of 1,500 cells**, with cell counts
\[
(f_0,f_1,f_2,f_3)=(440,760,280,20).
\]
No higher-dimensional cells exist; in particular the cell Euler characteristic is \(440-760+280-20=-60\).

**2. Full elementary-collapse certificate.** The companion file `artifacts/collapse_pairs.json` records 280 ordered pairs of cells, each as two five-tuples of integer subset masks. For every pair \((\sigma,\tau)\), the standalone checker reconstructs the entire cell poset from the edge list, establishes that \(\sigma\) is a codimension-one facet of \(\tau\), that \(\tau\) is its **unique** remaining containing cell of the next dimension, and that \(\tau\) has no higher-dimensional remaining coface. It then removes these two cells. Exactly 20 pairs consist of a 2-cell and a 3-cell; the remaining 260 pairs consist of a 1-cell and a 2-cell. These are genuine elementary collapses of a finite regular CW complex; a permitted elementary collapse preserves its homotopy type.

The resulting one-dimensional CW complex has 440 vertices and 500 edges. The checker independently performs graph traversal to show that all 440 vertices are in one connected component. A finite connected graph is homotopy equivalent to a wedge of as many circles as its edge count minus its vertex count plus one; here that number is \(500-440+1=61\). This proves the integral homotopy type, not just rational Betti numbers or an Euler-characteristic identity.

**3. Full dihedral action.** The two displayed vertex permutations preserve all 24 target edges and satisfy \(r^4=s^2=1\), \(srs=r^{-1}\). They generate eight distinct automorphisms. Exhaustive adjacency-and-nonadjacency-preserving backtracking finds exactly eight graph automorphisms, so they form the full automorphism group.

The automorphism action on each product-of-simplices cell is cellular. Orient the simplex on each color subset by the increasing color order, and take the ordered product orientation. For any automorphism \(g\), the cellular chain trace in dimension \(j\) is the sum, over setwise fixed \(j\)-cells, of the sign of the induced coordinatewise color permutation. This calculates the Lefschetz number
\[
L(g)=\sum_{j=0}^3(-1)^j\operatorname{tr}(g\mid C_j).
\]
The proved homotopy type yields \(H_0\cong\mathbb Q\), with trivial group action, and only \(H_1\) in positive degrees. By the cellular Lefschetz trace identity, \(\operatorname{tr}(g\mid H_1)=1-L(g)\). The exhaustive fixed-cell computation gives the character table in the Finding. Inner products with the five rational irreducible dihedral characters give multiplicities \((6,10,5,10,15)\), completing the equivariant homological statement.

## Verification

Run `python3 artifacts/verify_chvatal_hom.py` using Python 3.9 or later and the adjacent `artifacts/collapse_pairs.json`. Only the Python standard library is needed; there is no network dependency. The checker independently generates all Hom cells by direct five-state closed walks and by single-color expansions, compares their **complete cell sets**, regenerates every codimension-one facet, checks all 280 successive elementary collapses, verifies connectedness and the graph cycle rank, enumerates the full eight-element graph automorphism group, and checks cellular orientation signs, character values, and irreducible multiplicities.

The actual run produced `artifacts/verification_output.json` with `status: PASS`, 440 Hom vertices, 760 one-cells, 280 two-cells, 20 three-cells, 280 valid collapse pairs, and a connected 440-vertex/500-edge graph. These finite exhaustive checks prove the **specific finite assertion** because they cover every cell of the explicit complex. They do not certify unrelated target graphs or source cycle lengths.

## Relationship to prior work

The December 26, 2024 preprints of Fujii–Kimura–Nozaki and Matsushita establish major structure theorems for graph-Hom complexes with **square-free codomains**. Their hypotheses fail here: \(H\) contains the indicated four-cycle. Neither theorem implies a graph-Hom classification for this target; the relevant theorems, definitions and sections of their available full texts were inspected. This result instead supplies a direct regular-CW collapse proof and a dihedral character at a canonical non-square-free four-chromatic target.

Previously recorded computations of \(\operatorname{Hom}(C_5,\mu(C_5))\), and of \(\operatorname{Hom}(C_5,P)\) for the Petersen graph \(P\), treat different target graphs; their rank and component statements do not determine the Chvátal case. The previously published prism-to-pentagon result reverses the target role and also does not imply it. The complete-graph target theorem for \(\operatorname{Hom}(C_5,K_m)\) cannot be transferred to this noncomplete induced subtarget by an equivalence theorem. Exact-pair, alias, general-theorem and database searches yielded no identified covering result. This does not prove global bibliographic uniqueness; an unindexed or differently formulated prior computation remains possible.

## Limitations

The theorem is for the specifically defined standard Chvátal graph and source \(C_5\); it makes no all-source-length or all-triangle-free-target assertion. The elementary collapse is not asserted equivariant, although the rational homology representation is computed from the original cellular action. The rational representation decomposition is not an integral-lattice classification. The originality judgment is based on inspected accessible sources and actual record searches, not on a proof that unindexed work does not exist. The computation has not undergone independent external mathematical validation.

## References

1. S. Fujii, K. Kimura and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039, first released 2024-12-26; Theorems 1.1–1.2, Section 2.2, and Appendix A. https://arxiv.org/abs/2412.19039
2. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144, first released 2024-12-26; Theorem 1.2 and Theorem 5.8. https://arxiv.org/abs/2412.19144
3. *Chvátal Graph*, Wolfram MathWorld, reference for the standard twelve-vertex quartic graph and its girth-four status. https://mathworld.wolfram.com/ChvatalGraph.html
4. *Stiefel manifolds and coloring the pentagon*, Journal of Combinatorial Theory Series A (2014), a complete-target Hom-complex classification, not a theorem for the Chvátal target. https://doi.org/10.1016/J.JCTA.2013.09.006
5. *Odd-cycle graph-Hom complexes into the Petersen graph: twenty-four circles and rigid nine-cycles*, published-finding corpus research record (2026), compared as a separate square-free codomain case. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-odd-cycle-graph-hom-complexes-into-the-petersen-graph-twenty-fou--ce6537190eb4
