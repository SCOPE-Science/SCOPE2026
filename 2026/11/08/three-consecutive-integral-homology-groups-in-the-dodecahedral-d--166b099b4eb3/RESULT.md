# Three consecutive integral homology groups in the dodecahedral dominance complex

## Finding
Let \(D\) be the standard twenty-vertex dodecahedral graph and let \(K=\operatorname{Dom}(D)\) be the complex of vertex subsets whose complements are dominating sets. Its complete reduced integral homology is
\[
\widetilde H_k(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{12},&k=9,\\
\mathbb Z,&k=10,\\
\mathbb Z^{10},&k=11,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is exactly eight-connected, has dimension thirteen, and contains no integral homology torsion. **No sphere-wedge homotopy decomposition is asserted.**

## Assumptions and scope
The graph is the simple cubic graph \(\operatorname{GP}(10,2)\), with two kinds of vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) and thirty edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). The standalone verifier uses an isomorphic labeling on integers zero through nineteen. Its full edge set, in that labeling, is

```
(0,1) (0,10) (0,19) (1,2) (1,8) (2,3) (2,6) (3,4)
(3,19) (4,5) (4,17) (5,6) (5,15) (6,7) (7,8) (7,14)
(8,9) (9,10) (9,13) (10,11) (11,12) (11,18) (12,13)
(12,16) (13,14) (14,15) (15,16) (16,17) (17,18) (18,19)
```

An explicit vertex permutation in the program identifies the two graph presentations. Write \(N_D[v]=\{v\}\cup\{w:\{v,w\}\in E(D)\}\) for a closed neighborhood. A subset \(\sigma\) is a face of \(K\) exactly when \(N_D[v]\not\subseteq\sigma\) for every vertex \(v\); equivalently, \(V(D)\setminus\sigma\) dominates the graph. The empty face is included, as in standard simplicial homology conventions. The calculation uses integer coefficients and ordinary (nonequivariant) reduced homology.

## Proof
**Finite face enumeration.** Encode a nonempty vertex subset by its twenty-bit indicator mask. Test every one of the \(2^{20}-1\) such masks against all twenty four-vertex closed neighborhoods. There are exactly 425,028 nonempty faces. The numbers of faces in dimensions zero through thirteen are
\[
(20,190,1140,4825,15184,36390,66800,93060,95900,
69644,32680,8405,780,10).
\]
The verifier independently checks the equivalent complementary dominating-set condition for every mask. In particular the maximum face dimension is thirteen. The reduced Euler characteristic computed directly from the faces is \(-21\), consistent with the claimed groups.

**Acyclic matching.** Consider the Hasse poset of **nonempty** simplices. Starting with everything unpaired, traverse the graph vertices in order \(19,18,\ldots,0\). At vertex \(v\), pair each still-unpaired simplex \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is a face and is still unpaired. This selects exactly 212,500 disjoint codimension-one pairs. Reverse these pairs in the downward-oriented face-poset Hasse graph. An exact topological sort examines all 425,028 vertices and all 3,559,600 Hasse covering relations and exhausts the directed graph, proving that the matching is acyclic. Forman's discrete-Morse theorem therefore gives a homotopy-equivalent cellular model with exactly one critical zero-cell, fourteen critical nine-cells, three critical ten-cells, and ten critical eleven-cells.

**Exact integral Morse boundaries.** Orient each simplex by increasing vertex label. For a matched covering \(s\subset t=s\cup\{v\}\), the signed incidence \([t:s]\) is \((-1)^j\), with \(j\) the number of labels in \(s\) smaller than \(v\). Algebraically eliminate each matched pair: the reduced projection of its lower face is minus the signed sum of the reduced projections of the other codimension-one faces of its upper partner, divided by the unit incidence \([t:s]\). The acyclic matching makes this recursion terminate. Applying it to the boundaries of the critical simplices gives the **exact integral** Morse differential \(\partial_{11}=0\) (three rows by ten columns) and \(\partial_{10}\) (fourteen rows by three columns) with the following only nonzero rows, indexed starting from zero in increasing order of critical nine-simplex masks:

| Row | First column | Second column | Third column |
| ---: | ---: | ---: | ---: |
| 5 | \(-1\) | \(-1\) | \(0\) |
| 9 | \(-1\) | \(0\) | \(1\) |
| 10 | \(1\) | \(0\) | \(-1\) |
| 12 | \(-1\) | \(-1\) | \(0\) |
| 13 | \(1\) | \(0\) | \(-1\) |

The first column equals the second **minus** the third, so \(\operatorname{rank}\partial_{10}\leq 2\). Rows five and nine and columns zero and one form an integral minor of determinant \(-1\), proving rank two and primitivity of the image in \(\mathbb Z^{14}\). Thus
\[
\widetilde H_9(K;\mathbb Z)=\mathbb Z^{14}/\operatorname{im}\partial_{10}
\cong\mathbb Z^{12},\qquad
\widetilde H_{10}(K;\mathbb Z)=\ker\partial_{10}\cong\mathbb Z,\qquad
\widetilde H_{11}(K;\mathbb Z)=\mathbb Z^{10}.
\]
All other reduced groups vanish because there are no other positive-dimensional critical cells. The CW model has cells only in dimensions zero, nine, ten, and eleven, hence it is eight-connected. Nonzero ninth homology makes its connectivity exactly eight.

## Verification
Run `python3 dodecahedral_dominance_verify.py` with standard Python, requiring no third-party packages. The script enumerates **every** vertex subset and uses the independent complementary domination condition, checks the exact face vector, validates the displayed isomorphism to \(\operatorname{GP}(10,2)\), constructs both a reverse-order and a forward-order discrete-Morse matching, and proves each matching acyclic by a complete topological sort of **all** Hasse covers. It then evaluates the oriented integral Morse differentials by recursive exact integer arithmetic, checks \(\partial_{10}\partial_{11}=0\), and finds maximal minors of determinant \(\pm1\). The forward-order matching independently leaves cell counts \((1,15,6,12)\) in dimensions \((0,9,10,11)\), with boundary ranks three and two and unit maximal minors in both degrees. It produces the same integral homology groups, including torsion-freeness. The companion file `dodecahedral_dominance_output.txt` records the successful output. Only a **finite exact computation** is claimed; the code explicitly exhausts this finite graph rather than extrapolating to larger graphs.

## Relationship to prior work
Marietti and Testa study dominance complexes of forests and their sphere homotopy types, first in the publicly posted 2007 work *Cores of simplicial complexes*, Theorem 8.1, and subsequently in *A simple uniform approach to complexes arising from forests*, Proposition 4.10. Taylan's Theorem 5.4 extends a sphere result to chordal graphs. The dodecahedral graph contains induced five-cycles and is neither a forest nor chordal, so those conclusions do not cover it.

Matsushita and Wakatsuki prove the general Alexander-dual identity \(\operatorname{Dom}(G)^{\vee}=\mathcal N(\overline G)\). For this graph, evaluating the theorem requires the ordinary neighborhood complex of its **graph complement**, not the known ordinary neighborhood complex of the dodecahedral graph itself. No inspected theorem or table determined those dual homology ranks for this case. Previously indexed exact dodecahedral independence- and matching-complex computations have different simplices: independent vertex sets and vertex-disjoint **edge** sets, respectively. They do not imply the displayed dominance groups. A targeted comparison also considered indexed dodecahedral graph Čech and neighborhood-complex results, but neither has the same face criterion.

## Limitations
This is an exact finite integral homology and connectivity result for the twenty-vertex dodecahedral graph, not a classification of all polyhedral graphs. The calculation does not determine whether the eleven-cells have nontrivial higher attaching maps or whether the complex is a wedge of spheres, and it asserts no automorphism representation, equivariant homotopy splitting, persistence module, or infinite-family theorem. Mathematical priority may be affected by equivalently formulated but unindexed work. Independent mathematical review has not been performed.

## References
1. Mario Marietti and Damiano Testa, *Cores of simplicial complexes*, arXiv:math/0703351v1, first publicly submitted 12 March 2007, Section 8, https://arxiv.org/abs/math/0703351.
2. Mario Marietti and Damiano Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461v1, first publicly submitted 10 May 2007, Section 4.3, https://arxiv.org/abs/0705.1461.
3. Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly submitted 27 January 2015, Theorem 5.4, https://arxiv.org/abs/1501.06754.
4. Takahiro Matsushita and Shun Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1, first publicly submitted 5 December 2023, Theorem 1.1, https://arxiv.org/abs/2312.02639.
5. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI 10.1006/aima.1997.1650.
6. Publicly indexed studies titled *The dodecahedral independence complex is a wedge of four 5-spheres*, *The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres*, and *The complete rational dodecahedral neighborhood-homology character*. The mathematical statements are distinct from the dominance-complex invariant computed here.
