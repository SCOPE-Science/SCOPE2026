# An integral autotopism presentation for Latin-square clique homology

## Finding

Let \(M:R\times C\to S\) be **any** Latin square of order \(n\ge5\), with three disjoint label sets of size \(n\). Its Latin-square graph has one vertex for every cell \((r,c)\), and joins two distinct cells when they share a row, a column, or a symbol. Write \(X=\operatorname{Cl}(G(M))\) for its full simplicial clique complex. Let \(T\) be the autotopism group of \(M\), consisting of triples of permutations of \(R,C,S\) preserving \(M\). Define the integral augmentation lattices

\[
A_R=\ker(\mathbb Z[R]\xrightarrow{\sum}\mathbb Z),\quad A_C=\ker(\mathbb Z[C]\xrightarrow{\sum}\mathbb Z),\quad A_S=\ker(\mathbb Z[S]\xrightarrow{\sum}\mathbb Z).
\]

Let \(\mathcal I(M)\) be the set of *intercalates*: unordered pairs of rows and columns whose four entries form a Latin subsquare of order two. There is an explicit \(T\)-equivariant short exact sequence of **integral** lattices

\[
\boxed{\ 0\longrightarrow\mathbb Z[\mathcal I(M)]
\xrightarrow{\ \Phi\ }A_R\otimes A_C\otimes A_S
\longrightarrow\widetilde H_2(X;\mathbb Z)\longrightarrow0.\ }
\]

For an intercalate with rows \(r_0,r_1\), columns \(c_0,c_1\), and two symbols \(s_0,s_1\), the image of its oriented generator is, up to a coherent choice of sign,

\[
\Phi(I)=(e_{r_0}-e_{r_1})\otimes(e_{c_0}-e_{c_1})\otimes(e_{s_0}-e_{s_1}).
\]

The sublattice \(\operatorname{im}\Phi\) is **primitive**. In particular, the quotient has no integral torsion, its rank is \((n-1)^3-|\mathcal I(M)|\), and all other reduced integral homology groups vanish. For every autotopism \(g=(\rho,\kappa,\sigma)\in T\), the complete rational homology character is

\[
\boxed{\ \operatorname{tr}\bigl(g\mid\widetilde H_2(X;\mathbb Q)\bigr)
=(|\operatorname{Fix}(\rho)|-1)(|\operatorname{Fix}(\kappa)|-1)(|\operatorname{Fix}(\sigma)|-1)
-|\operatorname{Fix}_{\mathcal I(M)}(g)|.\ }
\]

The theorem holds for nongroup Latin squares, all even and odd orders at least five, and the entire color-preserving autotopism group, not only translations of a group table. The integral presentation is stronger than the rational character formula.

## Assumptions and scope

Every row, column, and symbol of \(M\) occurs exactly once in each appropriate line. The three label sets are treated as **distinct** even if numerically identified in an example. Autotopisms preserve each of the three line *types*; exchanges of the line types (paratopisms) are not asserted. All homology is reduced simplicial homology with integer coefficients unless indicated; \(\mathbb Z[\mathcal I(M)]\) is the ordinary permutation lattice on the set of intercalates. The symbol ordering in the displayed generator is selected compatibly with the tetrahedron's orientation; independent changes of this ordering adjust the sign, without changing the sublattice or the sequence.

The restriction \(n\ge5\) allows the standard classification of maximal cliques: besides simplices on a single line, the only mixed maximal cliques are rainbow triangles and intercalate tetrahedra. All operations are with the *full* clique complex, not its two-skeleton. The sequence need not split as a \(\mathbb Z[T]\)-module; only a split injection of underlying abelian groups is proved.

## Proof

**1. A line-cover nerve.** Let \(Y\subseteq X\) be the union of the full simplices supported on each of the \(n\) row-lines, \(n\) column-lines, and \(n\) symbol-lines. Every nonempty intersection of any collection of these simplices is either a singleton cell or a simplex, hence contractible. The simplicial nerve \(N\) has vertices \(R\sqcup C\sqcup S\). Every pair of vertices of different colors gives an edge; the colored triple \(\{r,c,s\}\) gives a triangle precisely when \(M(r,c)=s\). No four distinct lines have common intersection. The nerve theorem, via the common equivariant barycentric refinement of the cover, gives a \(T\)-equivariant homotopy equivalence \(Y\simeq N\). Equivariance here is valid because the cover is permuted by \(T\) and its nonempty intersections are simplices, with contractible fixed subspaces under their stabilizers.

**2. Filling missing triples.** Put \(Z\subseteq X\) equal to \(Y\) together with all triangles whose three edges have the three distinct adjacency types. Such a *rainbow* triangle is canonically indexed by a nonincident colored triple \((r,c,s)\) with \(s\ne M(r,c)\): its three vertices are the unique cells at the pairwise intersections \(R_r\cap C_c\), \(R_r\cap S_s\), and \(C_c\cap S_s\). Their three edges lie respectively on those three lines. Conversely each missing colored triple gives exactly this rainbow triangle. In the cover-nerve equivalence, the attaching loop of the rainbow triangle represents the boundary of the corresponding missing two-simplex \([r,c,s]\), with compatible orientation. This correspondence is natural under color-preserving autotopisms. Attaching all these triangles, using the homotopy pushout form of the nerve construction, yields an equivariant homotopy equivalence

\[
Z\simeq_T J:=R*C*S,
\]

where each of \(R,C,S\) is a discrete \(n\)-point complex and \(*\) denotes simplicial join. Indeed \(N\) contains every cross-color edge and exactly the incident colored triangles, so adjoining the missing ones gives the whole join. The join chain formula gives the *integral equivariant* identification

\[
\widetilde H_2(Z;\mathbb Z)\cong_T
\widetilde H_0(R;\mathbb Z)\otimes\widetilde H_0(C;\mathbb Z)\otimes\widetilde H_0(S;\mathbb Z)
=A_R\otimes A_C\otimes A_S,
\]

and all other reduced homology of \(Z\) vanishes. No tensor product is being inferred merely from rational characters: it comes from the integral simplicial join.

**3. The intercalate attaching map.** The classification of mixed cliques (see Reference 1, Section 3) says that \(X\) is obtained from \(Z\) by adjoining exactly one tetrahedron for every intercalate. All other higher simplices already lie in a line simplex inside \(Y\). Thus \(C_3(X,Z;\mathbb Z)\) is free on intercalates, and every other relative chain group vanishes. The four triangular faces of an intercalate tetrahedron are rainbow triangles. Under the equivalence of Step 2 their boundaries, together with the four incidence triangles from \(N\), form the eight oriented triangles of the octahedral sphere

\[
\{r_0,r_1\}*\{c_0,c_1\}*\{s_0,s_1\}.
\]

The class of this sphere under the join Künneth map is exactly the product of the three signed zero-cycles displayed in the Finding. This identifies the connecting homomorphism \(H_3(X,Z;\mathbb Z)\to H_2(Z;\mathbb Z)\) with \(\Phi\). An autotopism stabilizing an intercalate may exchange its two rows or two columns. Either exchange acts as two disjoint transpositions of its four cells, hence is even. Therefore the oriented relative tetrahedra carry the **untwisted** permutation action of \(T\) on \(\mathcal I(M)\); no orientation-character correction is needed. Their boundary map is equivariant.

**4. Primitivity, without rationalization.** Every rainbow triangle belongs to at most one intercalate tetrahedron: its three cells uniquely determine the potential fourth cell, if it exists. For every intercalate choose one of its four rainbow faces. The coefficient on this chosen triangle is an integer-valued function of a two-cycle of \(Z\), well defined on its homology class because all three-simplices in \(Z\) lie on a single row, column, or symbol line, so their boundaries have zero coefficients on rainbow triangles. On the boundaries of the intercalate tetrahedra, these coefficient maps form a diagonal matrix with diagonal entries \(\pm1\). Consequently the boundary map \(\mathbb Z[\mathcal I(M)]\to H_2(Z;\mathbb Z)\) has an abelian-group left inverse. In particular it is injective and its image primitive, although this chosen left inverse need not be equivariant.

**5. The exact sequence and character.** The long exact sequence for \((X,Z)\), Steps 2–4, and the vanishing of the other relative groups give the asserted integral short exact sequence, with \(H_3(X;\mathbb Z)=0\) and no other nonzero reduced homology. Tensoring with \(\mathbb Q\) makes a short exact sequence of finite-dimensional representations. Each augmentation permutation lattice \(A_R\) has trace \(|\operatorname{Fix}(\rho)|-1\), and similarly for the other colors. The permutation lattice on intercalates has trace \(|\operatorname{Fix}_{\mathcal I(M)}(g)|\). Additivity of traces in exact sequences gives the stated formula. The integral ranks follow from the sequence, not from an assumption of freeness of homology.

## Verification

The attached `verify.py` uses only the Python standard library. It enumerates every clique of four independently constructed group-table Latin squares (cyclic orders four, five, six and the Klein four-group) plus a nongroup order-five Latin square, identifies every intercalate, checks disjointness of the intercalate rainbow faces, and calculates **signed** fixed-face Lefschetz numbers for each tested autotopism. It checks the predicted character against the independent signed simplicial trace, not merely ordinary ranks. Exact observations are recorded in `verify_output.txt`. The tests cover the small orders four, five, and six, including the two inequivalent Latin group tables of order four and a nongroup example of order five with four intercalates. The latter also has directly computed mod-two second Betti number sixty, as predicted; the all-order proof applies from order five onward. Small-order four is a supplementary structural test, not an extension of the theorem's domain. The infinite statement is proved by the nerve, join, and relative boundary arguments rather than these finite computations.

## Relationship to prior work

Cioabă and Mim [1, Section 3; Theorem 3.12] establish that the Latin-square graph clique complex has field-independent second Betti number \((n-1)^3-I(M)\), with other positive-degree field homology vanishing. Their result does not specify the integral representation of the autotopism group. A previously established all-Latin-square nonequivariant sphere-wedge classification [2] also does not imply an integral group-module identification.

Earlier published symmetry results [3] compute rational translation characters for **odd-order abelian** Latin group tables. The stronger even-order comparison [4] establishes an integral permutation-module exact sequence for the intercalate boundaries and identifies the larger module only **rationally** for even-order abelian group tables; it explicitly does not assert an integral augmentation-tensor lattice isomorphism. The new finding uses the line-cover nerve to identify that larger lattice **integrally**, establishes the primitive inclusion for arbitrary Latin squares, and gives the full color-preserving autotopism action (not just translation subgroup actions). These statements are not logical corollaries of the rational characters or nonequivariant homotopy ranks alone.

## Limitations

This is a presentation, not a classification of the Smith form of every individual autotopism's integral action. The exact sequence is not claimed to split as a group-module sequence. Actions that exchange the three line types are not covered. Its correctness uses the standard mixed-clique classification for Latin-square graphs; the independent small examples do not replace the all-order topological proof. Unindexed equivalent results may exist, and an independent mathematical audit has not been performed.

## References

1. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1 (first public 2026-06-25), especially Section 3 and Theorem 3.12, https://arxiv.org/abs/2606.27328.
2. *Every Latin-square clique complex is a wedge of two-spheres*, prior published result (2026-11-08 onward): https://github.com/published-finding corpus/2026.
3. *Translation characters of odd-order Latin-square clique homology*, 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-translation-characters-of-odd-order-latin-square-clique-homology--e7cda2f0fcdd/RESULT.md.
4. *Intercalate correction modules in even-order Latin-square clique homology*, 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-intercalate-correction-modules-in-even-order-latin-square-clique--f1a50eb000f9/RESULT.md.
