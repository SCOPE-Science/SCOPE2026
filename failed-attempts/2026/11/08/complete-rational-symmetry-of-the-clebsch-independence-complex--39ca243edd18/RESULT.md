# Complete rational symmetry of the Clebsch independence complex

## Finding
Let \(C\) be the five-regular, sixteen-vertex Clebsch graph, realized as the Cayley graph of \(V=\mathbb F_2^5/\langle(1,1,1,1,1)\rangle\) with generating directions \(d_i=[e_i]\), \(0\le i\le4\). Its full graph-automorphism group is \(G=V\rtimes S_5\), where \(S_5\) permutes the five generators. Let \(K=\operatorname{Ind}(C)\) be its ordinary independence complex: the simplices are the subsets of vertices containing no graph edge.

Define the four-dimensional rational \(S_5\)-representation \(U=\{(z_0,\ldots,z_4)\in\mathbb Q^5:\sum_i z_i=0\}\). Let \(W\) be a rational vector space with basis \(f_0,\ldots,f_4\), on which \((a,\sigma)\in G\) acts by
\[
(a,\sigma)f_i=(-1)^{\ell_{\sigma(i)}(a)}f_{\sigma(i)},\qquad
\ell_i([a_0,\ldots,a_4])=\sum_{j\ne i}a_j\pmod2.
\]
The function \(\ell_i\) is well defined on the quotient because replacing every coordinate by its complement changes the sum of the other four entries by zero modulo two. Write \(\varepsilon(a,\sigma)=\operatorname{sgn}(\sigma)\) for the inflated sign character.

**The principal result is the full rational automorphism-module decomposition**
\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong(\varepsilon\otimes U)\oplus(\varepsilon\otimes W)}.
\]
These summands are irreducible over \(\mathbb Q\) of dimensions four and five. In particular, the full symmetry group has no invariant nonzero third-homology class. For \(g=(a,\sigma)\), its complete character is
\[
\boxed{\chi_3(g)=\operatorname{sgn}(\sigma)\left(\#\operatorname{Fix}(\sigma)-1+\sum_{\sigma(i)=i}(-1)^{\ell_i(a)}\right).}
\]
Over all \(1920\) group elements, the character values and respective multiplicities are \(-5:20\), \(-3:60\), \(-1:884\), \(1:865\), \(3:80\), \(5:10\), and \(9:1\).

The underlying nonequivariant homotopy type \(K\simeq\bigvee^9 S^3\) is already known and is **not** claimed as a new theorem. It is reconstructed here solely to justify that the signed Lefschetz numbers determine the unique nonzero reduced rational homology character.

## Assumptions and scope
The graph is the five-regular Clebsch graph, not its ten-regular complement. A concrete binary encoding uses vertex labels \(0,\ldots,15\) and edges \(\{x,x\oplus d\}\) for \(d\in\{1,2,4,8,15\}\), with bitwise XOR \(\oplus\). This is the quotient of the five-dimensional binary cube by antipodal identification. Every statement concerns the ordinary, unsigned independence complex with integral simplicial orientations and the rational homology action of *all* graph automorphisms, not just a coordinate subgroup.

## Proof
**1. The full group.** Every translation of \(V\) and every permutation of the five directions preserves adjacency, producing \(16\cdot120=1920\) distinct automorphisms. An automorphism fixing \(0\) can permute only its five neighbors. The remaining ten vertices are precisely the pairwise sums \(d_i+d_j\) for \(i<j\), each uniquely characterized by its two common neighbors with \(0\). Thus an automorphism fixing \(0\) and those five neighbors fixes all vertices; its stabilizer embeds in \(S_5\). Consequently \(G\) is the full automorphism group.

**2. Homotopy concentration, checked integrally.** Enumerating all nonempty independent subsets gives \(392\) faces with face vector \((16,80,160,120,16)\). For each pivot \(v=0,\ldots,15\), in increasing integer-face-mask order, pair each available independent face not containing \(v\) with the face obtained by adding \(v\), whenever both remain. This produces \(190\) pairs. Reversing their \(190\) directed Hasse covers and orienting all other covers downward produces an acyclic orientation of all \(1200\) covers: its topological sort visits all \(392\) faces. The critical faces comprise one vertex, one \(2\)-simplex (mask \(1048\)), and ten \(3\)-simplices (masks \(1680,2400,10370,18564,24720,26880,33320,33864,36960,38400\)).

The explicit integral algebraic-Morse differential from the ten \(3\)-cells to the single \(2\)-cell is the row
\[
(1,1,0,0,-1,-1,0,0,-1,-1).
\]
Its entries have gcd one. A unimodular change of the ten three-cell generators makes this map a single unit, so one three-cell cancels the two-cell and the resulting CW complex is a wedge of nine three-spheres. Therefore \(\widetilde H_i(K;\mathbb Z)=0\) for \(i\ne3\) and \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^9\). This independent reconstruction uses no assumption about the already established sphere-wedge conclusion.

**3. Exact character formula.** For any graph automorphism \(g\), the simplicial Lefschetz number is
\[
L(g)=\sum_{\substack{\varnothing\ne F\in K\\gF=F}}(-1)^{|F|-1}\operatorname{sgn}(g|_F),
\]
where the permutation sign is taken on the ordered vertices of each fixed simplex. Homology concentration gives \(L(g)=1-\chi_3(g)\). Exhaustively enumerate all \(1920\) affine-direction permutations and all \(392\) independent faces, evaluating this signed fixed-face formula. For each affine element the result agrees exactly with the displayed closed formula. It follows, for every \(g=(a,\sigma)\), that the third-homology character is the sum of the traces of \(\varepsilon\otimes U\) and \(\varepsilon\otimes W\): the first trace equals \(\operatorname{sgn}(\sigma)(\#\operatorname{Fix}(\sigma)-1)\), and only \(\sigma\)-fixed basis vectors contribute to the second trace. Semisimplicity of rational representations of finite groups and equality of all complex characters yield the stated rational \(G\)-module isomorphism.

**4. Irreducibility and invariants.** The standard augmentation representation \(U\) of \(S_5\) is irreducible over \(\mathbb Q\), so its inflation and sign twist remain irreducible. Each \(f_i\) in \(W\) affords a distinct nontrivial rational character \(\ell_i\) of the normal translation group \(V\). Since \(S_5\) permutes these five weight spaces transitively, every \(G\)-stable subspace of \(W\) is either zero or all of \(W\). Hence the five-dimensional summand is also irreducible. The translation group has no invariants on \(W\), and \(S_5\) has no invariants in its sign-twisted standard representation; therefore the full nine-dimensional module has no invariant vector.

## Verification
Execute `python3 verify.py` with Python 3 and its standard library. The verifier independently enumerates the graph, its \(392\) nonempty independence faces, all \(190\) specified Morse pairs and \(1200\) covers, verifies acyclicity, computes the exact integral Morse degree vector and checks simplicial boundary ranks over \(\mathbb F_2\). It then enumerates all \(1920\) distinct automorphisms, checks adjacency preservation, calculates signed fixed-simplex Lefschetz traces, and compares each with the algebraic character formula. The group-wide character sum is zero, confirming the absence of invariants. Run output is included as `verification_output.txt`; the reproducible algorithms rather than that output alone are the finite certificate.

## Relationship to prior work
Greenwood and Gleason's original sixteen-vertex cubic-residue construction proves the classical three-color Ramsey bound and identifies the canonical graph; it does not study simplicial homology representations. Engström's archived work gives general independence-complex definitions and gluing methods, without this group's character. Adamaszek's classification concerns chordal graphs, whereas the triangle-free Clebsch graph has induced four-cycles and is not chordal. Published tables of Clebsch independent-set counts and previously established nonequivariant wedge classifications supply face numbers and homology dimensions, not a complete nine-dimensional \(G\)-character. Results for the Clebsch *open-neighborhood complex* concern a different simplicial construction, with \(31\)-dimensional second homology rather than this \(9\)-dimensional third homology; those character results do not imply the current decomposition. Analogous character decompositions for other graph complexes likewise do not cover this object.

## Limitations
This is an exact finite, rational equivariant homology classification of the specified graph's ordinary independence complex. It does not claim an integral \(\mathbb Z[G]\)-lattice isomorphism, an equivariant wedge decomposition, an infinite folded-cube family, or a new nonequivariant sphere-wedge classification. An indexed-literature and mathematical-record search cannot rule out an equivalent unpublished or poorly indexed calculation; independent mathematical validation has not been performed.

## References
1. R. E. Greenwood and A. M. Gleason, “Combinatorial Relations and Chromatic Graphs,” *Canadian Journal of Mathematics* **7** (1955), 1–7, DOI: 10.4153/CJM-1955-001-4. Original graph construction; full accessible PDF: https://doi.org/10.4153/CJM-1955-001-4.
2. A. Engström, “Complexes of Directed Trees and Independence Complexes,” arXiv:math/0508148v1, first public August 8, 2005; *Discrete Mathematics* **309** (2009), 3299–3309. Full text: https://arxiv.org/html/math/0508148v1.
3. M. Adamaszek, “A note on independence complexes of chordal graphs and dismantling,” arXiv:1508.02426, first public August 10, 2015. Full text: https://arxiv.org/abs/1508.02426.
4. R. Forman, “Morse Theory for Cell Complexes,” *Advances in Mathematics* **134** (1998), 90–145, DOI: 10.1006/aima.1997.1650.
