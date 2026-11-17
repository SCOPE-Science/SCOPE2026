# Facet-graph diameter and nine rigid antipodes in chains of ideal right-angled \(24\)-cells

## Finding
For every integer \(m\ge2\), let \(\mathcal C_m\) be a hyperbolic four-polytope formed by chaining \(m\) regular ideal right-angled \(24\)-cells across octahedral facets, with the two cuts of every intermediate cell opposite. Such chains occur in the classification of Kolpakov [1]. The *facet graph* \(\Gamma_m\) has one vertex per three-dimensional facet of \(\mathcal C_m\); two vertices are adjacent when their facets meet along a two-dimensional ridge. Then
\[
 |V(\Gamma_m)|=14m+10,\qquad \operatorname{diam}(\Gamma_m)=m+2,
\]
and **exactly nine unordered pairs of distinct facets attain this graph distance**, independently of \(m\).

These nine pairs have explicit root labels. Fix \(r=(1,1,0,0)\), and label the facet normals of each original cell by
\[
 \mathcal R=\{\pm e_i\pm e_j:1\le i<j\le4\}.
\]
Number cells from \(0\) to \(m-1\), and label the right cut of a nonterminal cell by \(r\) and the left cut of a noninitial cell by \(-r\). The unique long-distance pair is \((-r,r)\), together with eight pairs \((x,y)\), one for each \(x\in\mathcal R\) satisfying \(r\cdot x=-1\), where
\[
 y=\begin{cases} -x,&m\text{ odd},\\ x+r,&m\text{ even}.\end{cases}
\]
The first component belongs to the first terminal cell, and the second to the last. Each is a genuine unmerged terminal facet.

For the unique reflection-double case \(m=2\), the facet graph has \(38\) vertices and \(164\) edges; the numbers of unordered pairs at distances \(1,2,3,4\) are respectively \(164,374,156,9\).

## Assumptions and scope
The ambient hyperbolic polytopes and the chain realization are those of the classification in [1]. The root-system description is combinatorial: the original \(24\)-cell facet adjacency graph has vertices \(\mathcal R\), with two root labels adjacent precisely when their Euclidean dot product is \(1\). Reflecting across a cut and choosing the next cell's labels by central inversion makes each seam identify the eight root labels \(a\) satisfying \(r\cdot a=1\) with the eight labels \(-a\) on the next cell, without creating new facet identifications beyond this seam. The cut facets themselves are discarded as exterior facets. All graph distances are unweighted discrete distances, not intrinsic hyperbolic distances, and every two-dimensional ridge is counted once.

The known count \(14m+10\) is included to specify the graph's size; it is not presented as a new face-enumeration result. The new result is the exact unbounded-family graph diameter and its complete nine-pair equality classification.

## Proof
**1. Finite local graphs.** Write \(G\) for the graph on \(\mathcal R\) with edges at dot product \(1\). Put \(A=\{a:r\cdot a=1\}\), \(B=-A\). Both are eight-element sets. Let \(L=G-\{r\}\), \(I=G-\{r,-r\}\), and \(H=G-\{-r\}\). The first cell contributes a copy of \(L\), the last a copy of \(H\), and the intermediate cells copies of \(I\). The seam glues \(a\in A\) in one block to \(-a\in B\) in the next block. Ordinary root enumeration establishes that the subgraphs induced by \(A\) and \(B\) are three-cubes, and that each is *isometric* within every block in which it occurs. In particular, a path that leaves a block and later returns to the same seam can be replaced, without increasing length, by a path within the seam. Consequently a shortest path joining nonadjacent cells may be taken monotonically through their intervening seams.

These claims require only the finite \(24\)-root graph and are reproduced independently by the supplied standard-library exact verifier. The verifier constructs all \(24\) roots and all \(96\) root adjacency edges, computes full breadth-first distances within \(L,I,H\), and checks all \(8\times8\) seam-to-seam distances (rather than extrapolating from a sample of chain lengths).

**2. An exact min-plus transfer.** Define the involution \(\sigma(a)=r-a\) on \(A\), and the auxiliary metric
\[
 \phi(a,b)=\begin{cases}0&a=b,\\2&b=\sigma(a),\\1&\text{otherwise}.\end{cases}
\]
This is the graph metric of the complete eight-vertex graph with the four \(\sigma\)-opposite edges removed. It is *not* the seam's cube metric. Exact distances through one internal block are
\[
 d_I(-a,b)=1+\phi(a,\sigma(b)),\qquad a,b\in A.
\]
Write \(T(a,b)\) for this transfer distance. Min-plus matrix multiplication is \((U\otimes V)(a,b)=\min_c[U(a,c)+V(c,b)]\). Since \(\phi\) obeys the triangle inequality, \(\phi\otimes\phi=\phi\) (take \(c=a\)); since \(\sigma\) is an isometry of \(\phi\), induction yields
\[
 T^{\otimes p}(a,b)=p+\phi(a,\sigma^p(b))\quad(p\ge1),
\]
with the ordinary identity kernel for \(p=0\). This closed transfer formula is the infinite-parameter step: it establishes the passage across arbitrarily many internal cells.

**3. The terminal comparison.** For left endpoint \(x\) in a block \(X\in\{L,I\}\), and right endpoint \(y\) in a block \(Y\in\{I,H\}\), separated by \(k\ge1\) seams, set \(p=k-1\). By the isometric-seam property, the exact distance is
\[
 \min_{a,b\in A}\bigl[d_X(x,a)+T^{\otimes p}(a,b)+d_Y(-b,y)\bigr].
\]
For \(p=0\), the transfer is the identity, forcing \(a=b\). For \(p\ge1\), subtracting \(p\) leaves a finite expression over at most \(23\times23\times8\times8\) elementary integer comparisons. The complete endpoint table, derived directly from the explicit dot-product graph, is:

| Endpoint block types | Maximum transfer-adjusted distance | Number of ordered endpoint pairs achieving it |
|:---|---:|---:|
| \(L,H\) | \(4\) | \(9\) |
| \(L,I\) | \(4\) | \(8\) |
| \(I,H\) | \(4\) | \(8\) |
| \(I,I\) | \(4\) | \(8\) |

The table holds both for \(p=0\) and for each of the two parities of positive \(p\). The explicit self-contained `verification/verify_chain.py` reconstructs the finite base graph, enumerates every entry in this table, and checks all equalities exactly. In the \((L,H)\) row, the nine equality cases are precisely \((-r,r)\) and the eight pairs \((x,-x)\) for odd \(p\), or \((x,x+r)\) for even \(p\), with \(r\cdot x=-1\); here for \(p=0\) the latter even rule applies. Because \(p=m-2\) for the terminal-to-terminal comparison, this is exactly the parity statement in the theorem.

**4. Global maximum and multiplicity.** Each individual block has graph diameter \(3\). Endpoints in blocks separated by \(k\) seams have distance at most \((k-1)+4=k+3\). In an \(m\)-cell chain, the only pair of blocks at separation \(m-1\) is the pair of terminal blocks, giving the bound \(m+2\) and exactly nine equality cases. All shorter separations give at most \(m+1\) when \(m\ge3\); the case \(m=2\) is immediate. The nine terminal endpoint labels lie outside every seam identification, so they are nine distinct *unordered* facet pairs. This proves the diameter and its complete equality classification.

Finally, direct construction of \(\Gamma_2\) from the stated root-label quotient, followed by exact breadth-first distances for all \(\binom{38}{2}\) facet pairs, produces the announced four-entry distance histogram. This finite histogram is supplementary to, not the basis for, the proof for all \(m\).

## Verification
The independent-in-code (not independent-in-review) standard-library Python program `verification/verify_chain.py` reconstructs \(\mathcal R\), every local graph, the isometric-seam and transfer identities, the exact finite endpoint table and all terminal equality pairs. It also builds and exhaustively tests the full glued graph for each \(2\le m\le8\). Running `python verification/verify_chain.py` produced `PASS` with \(32{,}161\) counted exact assertions, including the \(38\)-vertex distance histogram. The general statement for arbitrarily large \(m\) follows algebraically from the min-plus identity and the exhaustive finite endpoint table; the bounded direct tests alone are not used as an infinite proof.

## Relationship to prior work
Kolpakov's October 2026 classification [1], inspected in full-text HTML, supplies the structural fact that the relevant hyperbolic four-polytopes decompose into oppositely cut chains of regular ideal right-angled \(24\)-cells. It also supplies the known facet count and identifies the doubled case as the unique second-minimal-volume realization. Kolpakov's 2012 minimality theorem [2] provides the earlier single-cell context. Neither establishes this facet–ridge adjacency graph's exact diameter or the constant nine antipodal pairs. Unlike metric estimates based on ambient hyperbolic distance or Euclidean vertex distances of a regular \(24\)-cell, the invariant here is the graph metric among *facets of a glued chain*. No equivalence is inferred merely from a search failure; historical priority remains provisional.

## Limitations
The theorem concerns these specific regular-cell chains and their facet graphs, not arbitrary entirely ideal right-angled hyperbolic four-polytopes. It does not compute hyperbolic geodesic distances, spectral gaps, or all distance distributions for \(m>2\). Finite local enumeration is a rigorous bounded component of the proof, but the self-contained script is not a separately conducted formal or human independent audit. Other historical terminology may conceal an equivalent facet-graph theorem; independent mathematical review has not been performed.

## References
[1] A. Kolpakov, *On the second smallest ideal right-angled hyperbolic four-polytope*, arXiv:2611.00118 (first public preprint date: 2026-10-28), https://arxiv.org/abs/2611.00118.

[2] A. Kolpakov, *On the optimality of the ideal right-angled 24-cell*, Algebraic & Geometric Topology 12 (2012), 1941–1949, arXiv:1211.2944, https://arxiv.org/abs/1211.2944.
