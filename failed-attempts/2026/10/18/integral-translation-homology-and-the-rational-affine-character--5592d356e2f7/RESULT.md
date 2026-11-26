# Integral translation homology and the rational affine character of the Paley-17 flag complex

## Finding
Let \(P_{17}\) be the Paley graph on \(\mathbb F_{17}\), with edges joining distinct \(u,v\) if \(v-u\) is a square. Set \(K=\operatorname{Cl}(P_{17})\), the flag (clique) complex. Let \(G=\mathbb F_{17}\rtimes Q\) be the affine group of maps \(x\mapsto ax+b\), where \(Q=(\mathbb F_{17}^{\times})^2\) consists of the eight nonzero squares. Let \(T\cong C_{17}\) denote the translation subgroup.

The complete reduced integral homology and its canonical integral translation module are
\[
\widetilde H_i(K;\mathbb Z)\cong\begin{cases}\mathbb Z^{16},&i=2,\\0,&i\ne 2,\end{cases}
\qquad
\widetilde H_2(K;\mathbb Z)|_T\cong \ker\bigl(\varepsilon:\mathbb Z[T]\to\mathbb Z\bigr).
\]
In the integral degree-two cycle lattice there is a class \(z\) whose first sixteen translates form a unimodular basis; its seventeenth translate is minus their sum.

The rational representation of the entire affine group is
\[
\widetilde H_2(K;\mathbb Q)\cong\ker\bigl(\varepsilon:\mathbb Q[\mathbb F_{17}]\to\mathbb Q\bigr),
\]
with character
\[
\chi(g)=\#\operatorname{Fix}_{\mathbb F_{17}}(g)-1
=\begin{cases}16,&g=1,\\-1,&g\in T\setminus\{1\},\\0,&g\in G\setminus T.\end{cases}
\]
It is irreducible as a rational \(G\)-module. Its complexification is the sum of the two nonisomorphic eight-dimensional irreducible representations induced from the two orbits of \(Q\) on the nontrivial characters of \(T\); those representations are Galois-conjugate (not complex-conjugate).

## Assumptions and scope
The vertex set is \(\{0,\ldots,16\}\), with all arithmetic modulo seventeen and \(Q=\{1,2,4,8,9,13,15,16\}\). A face is a clique. Each simplex is oriented by ascending vertex labels. Homology is simplicial homology of the finite flag complex with the indicated integral or rational coefficients. Only the explicit affine group action is classified; the theorem does not require a classification of every graph automorphism.

## Proof
**Integral homology.** Enumerating increasing cliques gives exactly \(17\) vertices, \(68\) edges, \(68\) triangles and no tetrahedra. The graph is connected, so its boundary \(\partial_1\) has rank \(16\) over \(\mathbb Z\). The integer \(68\times68\) triangle boundary \(B=\partial_2\) satisfies \(\partial_1B=0\), hence \(\operatorname{rank}(B)\le68-16=52\). The supplied verifier specifies an explicit \(52\times52\) submatrix of \(B\) by zero-indexed row and column positions in lexicographically sorted edges and triangles, and computes its exact determinant \(-1\) by fraction-free integer elimination. Therefore \(\operatorname{rank}(B)=52\), and its image is primitive in \(\mathbb Z^{68}\). As \(\ker\partial_1\) is primitive and has the same rank, \(\operatorname{im}\partial_2=\ker\partial_1\). Also \(\ker\partial_2\) is free of rank \(68-52=16\). There are no higher simplices, proving the integral homology assertion (including the absence of torsion).

**Integral cyclic module.** The verifier computes the integer kernel lattice of \(B\) using sixteen free triangle coordinates. Its explicit \(68\times16\) matrix \(J\) has integral entries and the identity as its free-coordinate submatrix, so its columns are a full integer basis: every integral cycle has integer free coordinates and equals the corresponding linear combination of columns of \(J\). Let \(z\) be the first basis column, and let \(S\in\operatorname{GL}_{16}(\mathbb Z)\) be the translation \(x\mapsto x+1\) on these homology coordinates. Direct exact matrix multiplication gives
\[
S^{17}=I,\qquad I+S+\cdots+S^{16}=0,
\qquad\det[z,Sz,\ldots,S^{15}z]=-1,
\]
where the determinant uses the integer basis \(J\). Thus the orbit has exactly one integral relation, the sum of seventeen translates is zero, and its first sixteen vectors form an integral basis. Consequently the cyclic module is \(\mathbb Z[T]/(1+t+\cdots+t^{16})\), which maps isomorphically onto the augmentation ideal of \(\mathbb Z[T]\) by multiplication by \(t-1\). The determinant and norm-operator identities are rechecked in `verify_integral_module.py`.

**Affine character.** Each \(x\mapsto ax+b\) preserves the quadratic-residue edge relation. For each of the \(136\) maps, count its setwise invariant oriented vertices, edges and triangles with permutation sign. The signed simplicial Lefschetz formula and homology concentration give
\[
\operatorname{tr}(g|\widetilde H_2(K;\mathbb Q))
=\operatorname{tr}(g|C_2)-\operatorname{tr}(g|C_1)+\operatorname{tr}(g|C_0)-1.
\]
The fully enumerated traces are \(16\) at identity, \(-1\) at each nontrivial translation, and \(0\) for each of the other \(119\) affine elements. Those are exactly the traces of the seventeen-point permutation augmentation, so semisimplicity of rational representations of finite groups yields the asserted isomorphism. Restricting to \(T\), the character is the rational cyclotomic representation \(\mathbb Q(\zeta_{17})\), which is irreducible over \(\mathbb Q\); hence the full \(G\)-representation is also rationally irreducible. Over \(\mathbb C\), the eight-square multiplier subgroup has exactly two orbits of size eight on the nontrivial additive characters. Clifford theory, or the explicit induced-character construction, gives the two distinct eight-dimensional complex irreducibles.

## Verification
Run `python3 verify_faces.py` with Python 3. It exhaustively reconstructs all cliques and signed boundaries, verifies the explicit unimodular minor and connectedness, and checks the Lefschetz formula for every affine group element. Install SymPy and run `python3 verify_integral_module.py` in the same directory to independently construct the full integer cycle basis and its translation/multiplier matrices, verify the cyclic norm relation and orbit determinant, and verify the affine conjugation relation. The latter does not assume Lefschetz traces.

## Relationship to prior work
The established nonequivariant topology of this seventeen-vertex flag complex is not claimed as a new homotopy classification. Romeo and Rinaldo (2018) identify the Paley-17 independence complex as vertex-decomposable; because Paley graphs are self-complementary, this is also pertinent to the clique complex. Aharoni, Berger and Meshulam (2003) study flag-complex homology and graph spectral criteria, but do not compute this affine homology representation. Boulet, Fieux and Jouve (2008) study simple-homotopy for flag complexes rather than the integral translation or rational affine module of this Paley example.

Among checked related indexed records, a Paley-17 *open-neighborhood* complex has different faces and integral torsion; a Paley-19 *tournament directed-flag* complex has a distinct vertex set, definition and homology. A cyclic equivariant result for Heawood independence homology is methodologically analogous, not an implication for Paley-17 clique homology. No inspected prior claim determines the integral sixteen-translate basis or the complete order-136 character.

## Limitations
The result is for this finite graph and its specific affine subgroup, not a theorem for all Paley graphs or an equivariant homotopy classification. The integral statement concerns restriction to the translation subgroup; **no integral isomorphism to the full affine permutation-augmentation lattice is asserted**. The ordinary nonequivariant homology rank is background, not presented as an independent novelty claim. A semantically equivalent computation might occur in unidentified literature; the literature comparison is not a proof of priority.

## References
1. R. Aharoni, E. Berger and R. Meshulam, *Eigenvalues and homology of flag complexes and vector representations of graphs*, arXiv:math/0312482, first public 2003-12-29, primary MSC 55U10. https://arxiv.org/abs/math/0312482
2. R. Boulet, E. Fieux and B. Jouve, *Simplicial simple-homotopy of flag complexes in terms of graphs*, arXiv:0809.1751, first public 2008-09-10. https://arxiv.org/abs/0809.1751
3. F. Romeo and G. Rinaldo, *2-dimensional vertex decomposable circulant graphs*, arXiv:1807.05755, first public 2018-07-16, especially the Paley-17 example. https://arxiv.org/abs/1807.05755
4. Published record, *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, repository published-finding corpus/2026, path `2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8` (different complex).
5. Published record, *Affine symmetry identifies the Paley-19 directed flag complex and its homology character*, repository published-finding corpus/2026, path `2026/10/11/SCOPE-affine-symmetry-identifies-the-paley-19-directed-flag-complex-an--9f50497a76ce` (different object).
