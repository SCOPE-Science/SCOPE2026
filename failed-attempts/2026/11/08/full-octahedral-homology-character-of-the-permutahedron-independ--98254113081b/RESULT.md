# Full octahedral homology character of the permutahedron independence complex

## Finding
Let \(T\) be the edge graph of the three-dimensional permutahedron, also called the truncated-octahedral graph. Write \(X=\operatorname{Ind}(T)\) for its ordinary independence complex, with the empty simplex included in the augmented chain complex. The only nonzero reduced integral homology is
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}\mathbb Z^4,&j=5,\\0,&j\ne5.\end{cases}
\]
Its full graph-automorphism group is \(B_3=(C_2)^3\rtimes S_3\), of order \(48\). Denote an element by \(g=(\pi,\varepsilon)\), acting on geometric coordinates as \(g(x)_i=\varepsilon_i x_{\pi(i)}\), where \(\pi\in S_3\) and \(\varepsilon_i\in\{-1,1\}\). Then its complete fifth-homology character is
\[
\boxed{\chi_5(g)=\prod_{i=1}^{3}\varepsilon_i+
\operatorname{sgn}(\pi)\sum_{\{i:\pi(i)=i\}}\varepsilon_i.}
\]
Equivalently, as rational representations of \(B_3\),
\[
\widetilde H_5(X;\mathbb Q)\cong
\mathbb Q_{\mathrm{flip}}\oplus
(\operatorname{sgn}_{S_3}\otimes\mathbb Q^3_{\mathrm{nat}}),
\]
where \(\mathbb Q_{\mathrm{flip}}\) has character \(\prod_i\varepsilon_i\) and \(\mathbb Q^3_{\mathrm{nat}}\) is the signed coordinate module with matrix entries \(M_{ij}=\varepsilon_i\mathbf 1_{j=\pi(i)}\). The latter summand is irreducible over \(\mathbb Q\). Central inversion acts as \(-I_4\), and the full invariant subspace has dimension zero.

## Assumptions and scope
The underlying graph has the 24 distinct signed permutations of \((0,1,2)\) as vertices. Two are adjacent if and only if their squared Euclidean distance is \(2\). Its 36 edges form the standard three-dimensional permutahedral one-skeleton, equivalent to the adjacent-transposition Cayley graph on four letters. Only this fixed graph is considered. The graph automorphism action permutes the vertices of the *ordinary* independence complex, not a matching, neighborhood, Vietoris–Rips, or equivariant replacement.

The ten conjugacy classes of \(B_3\) are indexed by signed cycle type \((\lambda_+,\lambda_-)\): the lengths of coordinate-permutation cycles whose accumulated coordinate sign is respectively positive and negative. The complete class-size and character table is:

| Positive cycles | Negative cycles | Class size | Fifth-homology trace |
|---|---|---:|---:|
| \(()\) | \((1,1,1)\) | 1 | -4 |
| \(()\) | \((2,1)\) | 6 | 2 |
| \(()\) | \((3)\) | 8 | -1 |
| \((1)\) | \((1,1)\) | 3 | 0 |
| \((1)\) | \((2)\) | 6 | -2 |
| \((1,1)\) | \((1)\) | 3 | 0 |
| \((1,1,1)\) | \(()\) | 1 | 4 |
| \((2)\) | \((1)\) | 6 | 0 |
| \((2,1)\) | \(()\) | 6 | 0 |
| \((3)\) | \(()\) | 8 | 1 |

## Proof
**1. Topological concentration by a complete finite matching.** Generate all independent faces as 24-bit masks using backtracking; there are 37,076 including the empty face. Their numbers by cardinalities \(0,1,\ldots,12\) are
\[
(1,24,240,1304,4218,8400,10356,7824,3555,960,168,24,2).
\]
Pair as-yet-unmatched faces \(\sigma\) and \(\sigma\cup\{v\}\) while iterating vertices \(v\) in the fixed lexicographic coordinate order. This yields exactly 18,536 disjoint augmented matching pairs and four unmatched faces, all of cardinality six. The executable certificate reconstructs all 219,240 augmented Hasse covers, reverses the matched covers and performs a complete topological sort of the resulting directed graph, visiting all 37,076 faces. This proves acyclicity of the specified matching, rather than merely reporting a rank computation.

The empty face participates in a matching pair. Removing it therefore leaves one additional critical vertex, along with the four critical 5-cells. Forman's discrete-Morse theorem gives a CW model with one 0-cell and four 5-cells, so \(X\simeq\bigvee^4 S^5\). The preceding statement is only the nonequivariant homotopy calculation; its sphere rank was already recorded in prior work and is not claimed as a new discovery.

**2. The automorphism group.** Every signed coordinate permutation preserves squared Euclidean distance and hence graph adjacency, giving a faithful subgroup of order 48. Independently, the checker constructs all graph automorphisms by assigning images in breadth-first vertex order, checking every edge and nonedge against all previously assigned images. Exactly 48 assignments extend to automorphisms, proving the subgroup is the full group.

**3. Signed fixed-face Lefschetz formula.** For any graph automorphism \(g\), the alternating trace on the augmented simplicial chain complex equals minus the alternating sum over all independent faces of \((-1)^{|\sigma|}\) times the sign of the vertex permutation restricted to a setwise-fixed face. Since reduced homology is concentrated in odd degree five, the two minus signs cancel:
\[
\chi_5(g)=\sum_{\substack{\sigma\in X\\g\sigma=\sigma}}
(-1)^{|\sigma|}\operatorname{sgn}(g|_\sigma).
\]
If a fixed face is the union of \(k\) vertex orbits of \(g\), then the summand is \((-1)^k\). Equivalently, \(\chi_5(g)\) is the independence polynomial at \(-1\) of the conflict graph formed from those vertex orbits that contain no internal graph edge. These two formulas give **independent** trace calculations in the attached program.

**4. Complete character and decomposition.** For each of the 48 signed coordinate permutations the two trace algorithms agree. The ten class values are those displayed above; direct substitution into the boxed formula gives exactly the same values for every element. Over characteristic zero, representations of a finite group are determined by their characters, establishing the direct-sum description. The natural three-dimensional signed coordinate representation is irreducible: its diagonal sign-change subgroup forces an invariant subspace to be a sum of coordinate axes, while coordinate permutations act transitively on those axes. Tensoring by a one-dimensional character preserves irreducibility. The two constituents are inequivalent (dimensions 1 and 3). Character averaging gives zero fixed vectors, and the central inversion has trace \(-4\) on a four-dimensional involutive representation, hence acts by \(-I_4\).

## Verification
Run `python3 verification/verify_character.py` under Python 3 with no third-party dependencies. The program rebuilds the graph, the complete augmented independence face poset, the matching, the directed Hasse acyclicity test, the exhaustive full automorphism group, all group-character values, and two separately implemented fixed-face formulas. It asserts the complete class table, the zero invariant multiplicity, and the character inner product equal to two. The saved output in `verification/verify_character.out` was reproduced by executing this exact script. Finite exhaustive checks prove the finite statement; no extrapolation to other graphs is used.

## Relationship to prior work
Araujo-Pardo, Del Río-Francos, López-Dudet, Oliveros and Schulte identify the graph of the three-dimensional permutahedron with the adjacent-transposition Cayley graph of the four-letter symmetric group; their article concerns graphicahedra and their symmetries, not independence homology. Barmak develops star-cluster techniques and general graph independence-complex topology; his theorems do not determine the homology representation of this graph.

The prior work *Vertex-uniform independence-complex splitting for the truncated octahedron* (2026, public record `4c0894f5e0e3`) establishes \(X\simeq\bigvee^4 S^5\), together with vertex deletion and link homotopy types. That result is acknowledged in full. It makes no claim identifying the action of all 48 automorphisms on the four-dimensional homology. The present claim is the **complete character and irreducible decomposition**; the previously known nonequivariant sphere-wedge statement is used as context and independently checked, not resubmitted as novelty. Related indexed work on Vietoris–Rips complexes uses a different simplicial construction on the same vertex set, and results on the truncated *cube* concern a different graph.

## Limitations
The representation is classified over \(\mathbb Q\); no claim is made about the integral \(\mathbb Z[B_3]\)-lattice structure, a canonical equivariant wedge decomposition, or higher-dimensional permutahedra. The exhaustive matching is a finite computer-assisted proof, with a standalone complete checker; a short symbolic, family-wide proof has not been established. An equivalent calculation in unindexed literature remains a priority risk, and no independent mathematical audit has been performed.

## References
1. G. Araujo-Pardo, M. Del Río-Francos, M. López-Dudet, D. Oliveros and E. Schulte, *The Graphicahedron*, arXiv:0910.3908v1, first public 2009-10-20; especially Lemma 3.3 and the permutahedral graph discussion.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02; general independence-complex topology and related methods.
3. *Vertex-uniform independence-complex splitting for the truncated octahedron* (2026), publicly indexed manuscript, record `4c0894f5e0e3`; full mathematical statement inspected for direct implication comparison.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for the discrete-Morse acyclic-matching theorem.
