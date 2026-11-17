# The full vertex-symmetry quotient of the five-vertex forest complex is a homotopy three-sphere

## Finding

Let \(K_5\) be the complete graph with five labeled vertices, and let \(\mathcal F(K_5)\) be its graphic-matroid independence complex: a simplex is a set of graph edges containing no cycle. The symmetric group \(S_5\) permutes the graph vertices and hence the simplices. For the *ordinary geometric orbit space* \(Y=|\mathcal F(K_5)|/S_5\),

\[
\boxed{Y\simeq S^3.}
\]

In particular, \(\pi_1(Y)=1\), \(H_0(Y;\mathbb Z)=H_3(Y;\mathbb Z)=\mathbb Z\), and all its other reduced integral homology vanishes.

## Assumptions and scope

All graphs are simple and undirected. Edges of \(K_5\) are the ten unordered vertex pairs from \(\{0,1,2,3,4\}\). The complex contains exactly the edge subsets whose spanning graph is a forest. Its maximal faces have four edges, so its geometric realization is three-dimensional. The finite group \(S_5\) acts by vertex relabeling and is *not* assumed free. The quotient is the ordinary topological orbit space, not the homotopy orbit space or the complex of unlabeled forest isomorphism classes with an artificially chosen incidence relation.

## Proof

**1. Genuine quotient cell structure.** Write \(P\) for the poset of all nonempty forests, ordered by strict inclusion, and \(\mathrm{sd}\,\mathcal F(K_5)=\Delta(P)\) for the barycentric subdivision. A simplex of this subdivision is a strict chain \(A_0\subsetneq\cdots\subsetneq A_d\). Every relabeling preserves the rank \(|A_i|\), so a group element that preserves a simplex setwise fixes every chain vertex: there are no inversions. Therefore \(\Delta(P)/S_5\) is an honest finite \(\Delta\)-complex presenting the ordinary geometric quotient. Each \(d\)-cell is exactly an orbit of strict chains with \(d+1\) terms. Orient a chain by its increasing-inclusion order. Its cellular boundary is the alternating sum of the orbits of its faces, with no unverified stabilizer factors.

**2. Exhaustive orbit counts and integral chains.** Exhaustively inspect all \(2^{10}-1\) nonempty edge subsets with a disjoint-set cycle test. The numbers of forests with one, two, three and four edges are \((10,45,110,125)\), respectively. Enumerate every strict nonempty forest chain and canonicalize it under all \(120\) permutations. The quotient cell numbers are

\[
(c_0,c_1,c_2,c_3)=(9,33,49,25).
\]

Let \(D_d:\mathbb Z^{c_d}\to\mathbb Z^{c_{d-1}}\) be the signed deletion matrix on chain orbits. Exact integer computation verifies \(D_1D_2=D_2D_3=0\) and gives the complete nonzero Smith diagonals

\[
D_1:\ 1^{\times8},\qquad D_2:\ 1^{\times25},\qquad D_3:\ 1^{\times24}.
\]

For clarity, the displayed notation means respectively eight, twenty-five and twenty-four entries equal to one, with all other Smith entries zero. The calculation uses arbitrary-precision integers, not numerical rank approximations. The images of the three differentials are primitive, and the ranks give

\[
H_0(Y;\mathbb Z)=\mathbb Z,\quad H_1(Y;\mathbb Z)=0,\quad
H_2(Y;\mathbb Z)=0,\quad H_3(Y;\mathbb Z)=\mathbb Z.
\]

**3. Fundamental group.** Choose a spanning tree of eight of the thirty-three quotient one-cells. Contracting that tree leaves twenty-five free generators. For each of the forty-nine two-cells attached along a chain \((A,B,C)\), use the edge word \(e_{AB}e_{BC}e_{AC}^{-1}\) with tree edges suppressed. The attached `k5_forest_verify.py` constructs these words from the quotient, freely reduces them, and performs exactly twenty-five elementary Tietze eliminations. At each elimination a generator occurs once with exponent \(+1\) or \(-1\) in one relator; that relator uniquely expresses it as a word in the others, and the code substitutes the expression in every remaining relator. After all eliminations there are no generators and all twenty-four remaining relators reduce to the identity. Every operation preserves the presented group, so \(\pi_1(Y)=1\).

**4. Homotopy identification.** By simple connectivity and \(H_2=0\), the Hurewicz theorem gives \(\pi_2(Y)=0\), and the next Hurewicz map \(\pi_3(Y)\to H_3(Y;\mathbb Z)\cong\mathbb Z\) is an isomorphism. Represent a primitive third-homology generator by a based map \(S^3\to Y\). It induces an isomorphism on all integral homology groups. Both spaces are simply connected CW complexes; the homology version of Whitehead's theorem makes the map a homotopy equivalence. This establishes the boxed statement.

## Verification

Run `python k5_forest_verify.py` using Python 3.10 or later with SymPy installed (`requirements.txt`). The verification is self-contained: it reconstructs all forest chains, all relabeling orbits and all boundary matrices; computes exact integral Smith diagonals; checks both boundary compositions; and constructs and eliminates the fundamental-group presentation. `CHECKS.txt` records its output. The finite enumeration is exhaustive because all possibilities lie among the \(2^{10}\) edge subsets and the \(120\) vertex permutations. The step from the computed invariants to a homotopy equivalence is the theorem-based argument in the proof, not an inference from numerical testing alone.

As a nonequivariant contrast, the labeled complex has \((10,45,110,125)\) nonempty face counts and is a shellable rank-four matroid complex. Its reduced homology is a free group of rank fifty-one in degree three, whereas the ordinary full-symmetry quotient has one generator in that degree.

## Relationship to prior work

The matroid-independence-complex shellability theorem, for example Ardila–Castillo–Samper, *The topology of the external activity complex of a matroid* (first posted October 14, 2014), identifies the nonequivariant wedge-of-spheres framework and treats a different external-activity construction. Its statements do not determine the homotopy type or fundamental group of the ordinary \(S_5\)-orbit space. Klee–Samper discuss lexicographic shellings and face enumerators, not orbit-space attaching maps. Moci–Pezzoli study automorphism-group representations on the *dual* matroid independence complex, including the complete-graph case; those complex-representation results do not imply an integral simply-connected quotient for the primal forest complex. Published related calculations for the Petersen graphic-matroid forest complex and the complete bipartite graph \(K_{2,n}\) involve different graphs and groups, and their homology-module information does not imply this orbit homotopy type.

## Limitations

The theorem concerns only the five-vertex complete graph and the full vertex-permutation group. It does not assert an equivariant equivalence of the original forest complex to a sphere, nor does it classify other group subquotients or general \(K_n\). A finite calculation gives the exact cell boundaries and presentation for this case, and standard topological theorems supply the infinite homotopy-theoretic conclusion. An unindexed or differently described earlier calculation of the same quotient cannot be excluded by literature searches alone.

## References

1. F. Ardila, F. Castillo and J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (initial public posting 2014-10-14), https://arxiv.org/html/1410.3870v2.
2. S. Klee and J. A. Samper, *Lexicographic shellability, matroids and pure order ideals*, arXiv:1406.1951 (initial public posting 2014-06-08), https://arxiv.org/html/1406.1951v1.
3. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (initial public posting 2020-01-11), https://arxiv.org/abs/2001.03760.
