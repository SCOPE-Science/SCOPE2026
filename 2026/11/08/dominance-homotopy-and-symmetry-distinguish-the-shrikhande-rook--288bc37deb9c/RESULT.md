# Dominance homotopy and symmetry distinguish the Shrikhande–rook twins

## Finding
Let \(S\) be the Shrikhande graph and \(R\) the \(4\times4\) rook graph, the two nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). For a finite graph \(G\), set
\[
\operatorname{Dom}(G)=\{F\subseteq V(G):V(G)\setminus F\text{ is dominating in }G\}.
\]
Then
\[
\boxed{\operatorname{Dom}(S)\simeq\bigvee^{11}S^9},
\qquad
\boxed{\widetilde H_k(\operatorname{Dom}(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=9,\\
\mathbb Z^2,&k=11,\\
0,&\text{otherwise}.
\end{cases}}
\]
The latter is an **integral homology** statement, not a claim about the rook complex's complete homotopy type. In particular, the two dominance complexes are not homotopy equivalent although their face counts agree in every dimension from zero through ten.

For the full \(192\)-element automorphism group \(A=\operatorname{Aut}(S)\), the rational representation on \(\widetilde H_9(\operatorname{Dom}(S);\mathbb Q)\) has a completely determined character \(\chi\): the orbit formula and all fourteen conjugacy-class values are given below and in `certificate.json`. Its invariants and character inner product satisfy
\[
\dim_{\mathbb Q}\widetilde H_9(\operatorname{Dom}(S);\mathbb Q)^A=0,
\qquad \langle\chi,\chi\rangle_A=3.
\]
Consequently its complexification is multiplicity-free with precisely three distinct irreducible constituents. The result does not identify the integral irreducible lattices.

## Assumptions and scope
Vertices of both graphs are \((x,y)\in(\mathbb Z/4\mathbb Z)^2\), labeled \(4x+y\), with coordinate representatives \(0,1,2,3\). In \(S\), adjacent vertices differ by one of
\[
D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
In \(R\), distinct vertices are adjacent precisely when a coordinate agrees. Graphs are simple and undirected. A set \(T\) dominates \(G\) when every vertex has a member of \(T\) in its closed neighborhood. The empty face is included in each abstract complex but not in the ordinary geometric realization or the nonempty face poset used for Morse matching.

Writing \(B_v=N_G[v]\), the face criterion is equivalent to
\[
F\in\operatorname{Dom}(G)\iff (\forall v\in V(G))\ B_v\not\subseteq F.
\]
Thus the minimal nonfaces come from closed neighborhoods; they are not the edges of the ordinary independence complex. The claim is restricted to these two sixteen-vertex graphs and the indicated full automorphism action.

## Proof
**1. Verify the graph presentations and face predicates.** The code checks all sixteen degrees and all unordered vertex pairs, obtaining valency six and exactly two common neighbors for each pair of distinct vertices in both graphs. The neighbors of a vertex induce a six-cycle in \(S\), but two triangles in \(R\). Exhaustively testing the stated forbidden-neighborhood predicate and, independently, coverage by the union of closed neighborhoods of the complement gives the same truth value for all \(2^{16}=65536\) masks per graph.

The full nonempty face counts are \(59818\) for \(S\) and \(59746\) for \(R\). In dimensions zero to ten the face counts coincide:
\[
(16,120,560,1820,4368,8008,11424,12726,10864,6712,2640).
\]
In dimension eleven there are \(528\) faces for \(S\) versus \(488\) for \(R\); in dimension twelve there are \(32\) for \(S\) versus none for \(R\). Their ordinary Euler characteristics are respectively \(-10\) and \(-2\).

**2. Construct and verify complete Morse reductions.** For each graph, enumerate all nonempty faces as ascending sixteen-bit masks. Starting with no paired faces, process pivot vertices \(0,1,\ldots,15\). At pivot \(v\), pair an as-yet-unpaired face \(F\) not containing \(v\) with \(F\cup\{v\}\) whenever the latter is a face and still unpaired. Every pair is a codimension-one cover relation, and no face participates twice. The resulting critical-cell counts, written as \((\text{dimension}:\text{count})\), are \((0:1,9:11)\) for \(S\) and \((0:1,9:1,11:2)\) for \(R\). The matching has respectively \(29903\) and \(29871\) pairs.

Orient each cover relation downward except the matched ones, which are oriented upward. The verifier forms all cover relations, \(461552\) for \(S\) and \(460656\) for \(R\), and Kahn-sorts the resulting directed graph. All faces are removed, proving that the two matchings are acyclic. Reverse-order pivot matchings give the same critical-cell counts and independently pass full acyclicity checks. (The exact covering counts and topological-sort totals are recorded in `certificate.json`.)

**3. Deduce homotopy and integral homology.** Forman's finite acyclic-matching theorem gives a CW model having one zero-cell and only the stated positive-dimensional cells. For \(S\), all eleven nine-cells attach to a point, giving the claimed wedge of nine-spheres, with no torsion. For \(R\), the only positive-dimensional cells have dimensions nine and eleven; hence every cellular boundary operator is zero, giving precisely the stated reduced integral homology. Higher attaching maps for the eleven-cells need not be null, so a sphere-wedge claim for \(R\) is intentionally not made.

**4. Determine the full symmetry group.** Every affine map \(z\mapsto Mz+t\) on \((\mathbb Z/4\mathbb Z)^2\) with \(MD=D\) preserves the graph. Exactly twelve admissible linear matrices are found exhaustively, giving \(16\cdot12=192\) affine automorphisms. Conversely, the six neighbors of any vertex induce a six-cycle, whose automorphism group has size twelve; each of the nine nonneighbors is uniquely identified by its pair of neighbors within that six-cycle. Hence a graph automorphism is completely determined by the image of one vertex and its six-cycle action. The automorphism group has at most \(16\cdot12=192\) elements and is exactly the displayed affine group.

**5. Recover the complete character by Lefschetz traces.** For \(g\in A\), let \(\mathcal O(g)\) denote its cycles on the sixteen vertices. If \(J\subseteq\mathcal O(g)\), write \(U_J\) for the union of the cycles in \(J\). The complete rational degree-nine character is
\[
\boxed{\chi(g)=\sum_{\substack{J\subseteq\mathcal O(g)\\U_J\in\operatorname{Dom}(S)}}(-1)^{|J|}.}
\]
Indeed a simplex fixed setwise by \(g\) is a union of vertex cycles. Its signed simplicial Lefschetz contribution is \((-1)^{|J|-1}\), since the orientation permutation on the simplex is the product of the cycle signs. The only nonzero reduced rational homology is in odd degree nine, so the ordinary Lefschetz trace equals \(1-\chi(g)\). The displayed orbit formula follows, including the empty cycle selection.

The verifier evaluates the signed simplicial Lefschetz sum directly on all nonempty faces for each of the \(192\) automorphisms. A distinct implementation independently evaluates the orbit-subset sum. All \(192\) values agree. Conjugation partitions the elements into fourteen classes; for each class the representative index, size, vertex-cycle type and trace are in `certificate.json` under `conjugacy_classes`. The sum of all traces is zero and the sum of their squares is \(576\). Character averaging gives invariant dimension zero and inner product three. Since that inner product is the sum of squares of complex irreducible multiplicities, the decomposition is multiplicity-free with three constituents.

## Verification
With Python 3 and only its standard library, run `python3 verify.py` followed by `python3 verify_orbits.py` in the directory containing the supplied artifacts. The first regenerates `certificate.json`, including complete adjacency masks, face vectors, two explicit matchings, exhaustively verified directed acyclicity, the full group-character array and conjugacy classes; the second computes the same character via independent orbit enumeration. The provided `verification_output.txt` is the captured successful output. The exact code and certificate in this package, not a prior-run log, support all finite counts and class values. The homotopy and rational-character deductions use the stated mathematical theorems in addition to these finite calculations.

## Relationship to prior work
The 2007 first public version of Marietti and Testa, *Cores of simplicial complexes*, proves sphere reductions for **forest** dominance complexes, not for these degree-six strongly regular graphs. The 2023 first public version of Matsushita and Wakatsuki proves the general equivalence between dominance complexes and the Alexander dual of the **open-neighborhood complex of the graph complement**, and computes selected product families, not either graph here. Matsushita's later *Closed neighborhood complexes of graphs* concerns sets **contained in** a closed neighborhood, whereas the present dominance faces **avoid containing** any closed neighborhood. These are distinct face conditions, and neither theorem computes the present group character.

Published comparisons of the same Shrikhande–rook pair determine their **ordinary independence complexes** and their **closed-neighborhood Čech nerves**. Their results concern different simplices: ordinary independence prohibits adjacent vertex pairs, and the Čech nerve consists of subsets contained in a closed neighborhood. Neither reported homotopy classification, nor the rook-only product formula for closed-neighborhood complexes, implies the present noncontainment-complex theorem. The graph-theoretic strongly regular classification and existence of these two twins are classical, not new claims.

## Limitations
The precise homotopy type of the rook dominance complex beyond its integral homology is not determined: possible high-dimensional attaching maps remain. The Shrikhande result does not classify its integral automorphism lattice or provide an equivariant homotopy splitting. There is no general classification of dominance complexes for all strongly regular graphs. The source comparisons cannot establish priority against unpublished, unindexed or inaccessible equivalent work; independent mathematical review has not been performed.

## References
1. M. Marietti and D. Testa, *Cores of simplicial complexes*, first public 2007-03-12, arXiv:math/0703351v1, https://arxiv.org/abs/math/0703351 (especially introduction and §8).
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, first public 2023-12-05, arXiv:2312.02639v1, https://arxiv.org/abs/2312.02639 (Theorem 1.1 and §§5–6).
3. T. Matsushita, *Closed neighborhood complexes of graphs*, first public 2025-11, arXiv:2511.12608, https://arxiv.org/abs/2511.12608 (Definitions 1.1 and 4.4, Theorem 1.4).
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, public mathematical record `41bf4d1d3187`, 2026-10-11.
5. *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, public mathematical record `5b6e4436155e`, 2026-10-11.
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
