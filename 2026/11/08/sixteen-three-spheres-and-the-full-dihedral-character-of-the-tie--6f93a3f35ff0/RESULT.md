# Sixteen three-spheres and the full dihedral character of the Tietze matching complex

## Finding
Let \(T\) be the twelve-vertex Tietze graph obtained by replacing one vertex of the Petersen graph by a triangle. Its **ordinary matching complex** \(\mathcal M(T)\) has a vertex for each graph edge, and its simplices are sets of pairwise vertex-disjoint graph edges. Then

\[
\mathcal M(T)\simeq\bigvee^{16}S^3.
\]

For the full graph automorphism group \(\operatorname{Aut}(T)\cong D_6=\langle r,s\mid r^6=s^2=1,\;srs=r^{-1}\rangle\) of order twelve, the rational third-homology character is

\[
\chi(r^a)=\begin{cases}16,&a\equiv0\pmod6,\\-2,&a\equiv2,4\pmod6,\\0,&a\equiv1,3,5\pmod6,\end{cases}
\qquad \chi(r^as)=0\quad(0\le a<6).
\]

In particular, if \(\lambda_{u,v}\) denotes the one-dimensional character with \(r\mapsto u\), \(s\mapsto v\), where \(u,v\in\{\pm1\}\), and \(\rho_1,\rho_2\) denote the two nonisomorphic two-dimensional rational irreducible representations, then

\[
\widetilde H_3(\mathcal M(T);\mathbb Q)
\cong\bigoplus_{u,v\in\{\pm1\}}\lambda_{u,v}
\oplus3\rho_1\oplus3\rho_2.
\]

Thus the full symmetry-invariant part is one-dimensional, and each reflection has \(+1\) and \(-1\) eigenspaces of dimension eight. The homotopy statement is **integral**; the irreducible representation statement is **rational**, not a classification of the integral \(\mathbb Z[D_6]\)-lattice.

## Assumptions and scope
The graph is simple and has vertices labeled \(1,2,\ldots,12\). The complete ordered edge list, with **zero-based indices** used by the certificate, is

```text
0:(1,2)   1:(1,6)   2:(1,10)  3:(2,3)   4:(2,7)   5:(3,4)
6:(3,8)   7:(4,9)   8:(4,11)  9:(5,7)  10:(5,8)  11:(5,12)
12:(6,8)  13:(6,9)  14:(7,9)  15:(10,11) 16:(10,12) 17:(11,12)
```

Each vertex has degree three; the unique graph triangle consists of vertices \(10,11,12\). Contracting that triangle gives the Petersen graph. Matchings include the empty face when forming the augmented face poset, but the ordinary simplicial complex and ordinary CW model do not include an empty cell.

## Proof
**Exact simplicial enumeration.** Represent a subset of edges by the eighteen-bit integer \(m\), with bit \(i\) corresponding to graph edge \(i\). It is a face if and only if every pair of its graph edges is disjoint. The exhaustive recurrence

```text
valid[0] = true
valid[m] = valid[m without its least set bit]
           AND (endpoints of that least-set-bit edge avoid the
                used endpoints in the smaller matching)
```

checks every integer from \(0\) to \(2^{18}-1\), and gives the face counts by simplex dimension \(0,1,2,3,4,5\):

\[
(18,117,335,408,165,8).
\]

There are therefore \(1051\) nonempty simplices and one empty face. A second, direct include/exclude recursion independently produces the identical set of \(1052\) faces.
There are \(15\) maximal three-simplices, \(117\) maximal four-simplices, and \(8\) maximal five-simplices, so the complex is nonpure even though its critical cells are all three-dimensional.

**Acyclic discrete-Morse matching.** Process the following zero-based edge indices in order:

```text
11, 9, 0, 16, 2, 15, 10, 3, 5, 17, 14, 6, 7, 8, 4, 1, 13, 12
```

At stage \(i\), for each as-yet-unpaired face \(m\), in increasing numerical order, whose bit \(i\) is absent, pair \(m\) with \(m\cup\{i\}\) whenever both are still unpaired faces. Process the empty face in the augmented construction. The augmented matching consists of \(518\) pairs, including \((\varnothing,\{11\})\), with precisely sixteen unpaired four-edge faces. Discard the empty face and its pair, keeping the singleton \(\{11\}\) as the sole critical zero-simplex. This leaves \(517\) disjoint ordinary pairs and sixteen critical three-simplices. No critical cells of any other dimension remain.

To prove acyclicity, orient every cover relation of the **ordinary**, nonempty face poset upward, except orient a matched relation downward. There are exactly \(3744\) cover relations. The attached verifier independently constructs all of them and checks that Kahn topological sorting removes all \(1051\) simplex-nodes. This is an exhaustive finite acyclicity proof, not a sample or an appeal to an unverified heuristic. Forman's discrete-Morse theorem now yields a CW complex with precisely one zero-cell and sixteen three-cells. Since every attaching map into a single point is constant, that CW complex is \(\bigvee^{16}S^3\).

**Full automorphism group.** On the ordered vertices \(1,\ldots,12\), two graph automorphisms are given by the image lists

```text
r = (5,7,2,1,4,8,9,3,6,12,10,11)
s = (1,2,7,5,4,6,3,9,8,10,12,11)
```

Their orders and the dihedral relation are checked directly. They generate twelve distinct permutations. Independently, exact graph-automorphism backtracking, checking adjacency and preserving the unique triangle, finds **exactly twelve** graph automorphisms. Hence these generators give all of \(\operatorname{Aut}(T)\).

**Character calculation.** Every automorphism permutes the eighteen simplicial vertices (graph edges). Its trace on a simplicial chain group is the sum over invariant simplices of the sign of the induced permutation of their ordered graph edges. Summing these chain traces with alternating dimension signs gives the ordinary Lefschetz number \(L(g)\). The established homotopy classification has \(H_0\cong\mathbb Q\), \(\widetilde H_3\cong\mathbb Q^{16}\), and zero homology in other positive degrees, so \(\chi(g)=1-L(g)\). Enumerating **all** invariant simplices for each of the twelve permutations yields the displayed class values. Inner products with the four one-dimensional and two two-dimensional dihedral characters give multiplicities \((1,1,1,1,3,3)\); these total \(4+12=16\) dimensions.

## Verification
Run `python3 verify_tietze.py` using Python's standard library only. The program reconstructs the specified graph, enumerates faces in two independent ways, repeats every staged matching step, checks all \(3744\) oriented Hasse edges for cycles, computes independent boundary-matrix ranks over \(\mathbb F_2\) and \(\mathbb F_3\), enumerates all graph automorphisms, and evaluates all twelve signed Lefschetz numbers. Boundary ranks in dimensions \(1\) through \(5\) are \((17,100,235,157,8)\) over both fields, consistent with the integral Morse proof; finite-field homology alone would not imply the integral claim. The exact recorded output is in `verification_output.txt`.

## Relationship to prior work
Marietti and Testa (arXiv:0705.1461, §4.4, Theorem 4.11) prove a wedge-of-spheres result for **forest** matching complexes; the Tietze graph contains cycles and is not a forest. Fouquet, Thuillier and Vanherpe (arXiv:1003.5459, §§1–2) analyze cubic flower-type constructions, triangular vertex inflation, and counts of **perfect matchings**; their statements do not determine the full ordinary matching complex, its homotopy type, or its symmetry action. Bayer, Jelić Milutinović and Vega (arXiv:2411.04601, Theorem 2) treat **outerplanar** graphs, whereas contraction of the distinguished triangle in the Tietze graph gives the nonplanar Petersen graph, so Tietze is not outerplanar. Their full-text introduction and conclusion discuss other graph families, but the inspected theorem does not classify this one. The ordinary matching complex equals the independence complex of the line graph, so searches under this equivalent formulation were also required and performed.

The Tietze graph and Petersen graph have closely related graph constructions, but an invariant of the Petersen graph's matching complex alone does **not** imply the present Tietze homotopy or the dihedral character: triangular vertex inflation changes both the simplicial vertex set and the matching constraints. No equivalence to a previously inspected matching-complex theorem was identified.

## Limitations
The result concerns this **specific** twelve-vertex graph and the **ordinary** matching complex, not the perfect-matching subcomplex, graph configuration spaces, a general flower-snark family, or all vertex-inflated cubic graphs. It does not claim an equivariant wedge decomposition or an integral irreducible-lattice splitting. Source searches do not prove global novelty: unindexed equivalent computations or broader theorems could exist. No independent mathematical audit has been performed.

## References
1. M. Marietti and D. Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461 (first submitted 2007-05-10), §4.4, Theorem 4.11. https://arxiv.org/abs/0705.1461
2. J.-L. Fouquet, H. Thuillier and J.-M. Vanherpe, *On a family of cubic graphs containing the flower snarks*, arXiv:1003.5459 (first submitted 2010-03-29), §§1–2. https://arxiv.org/abs/1003.5459
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching complexes of outerplanar graphs*, arXiv:2411.04601 (first submitted 2024-11-07), Theorem 2, §§1–3. https://arxiv.org/abs/2411.04601
4. E. W. Weisstein, *Tietze Graph*, MathWorld, graph description and bibliography. https://mathworld.wolfram.com/TietzeGraph.html
