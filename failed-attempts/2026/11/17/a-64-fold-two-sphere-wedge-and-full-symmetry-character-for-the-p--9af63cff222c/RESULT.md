# A \(64\)-fold two-sphere wedge and full symmetry character for the Paley graph of order \(25\)

## Finding

Let \(P_{25}\) be the Paley graph on \(\mathbb F_{25}\), with an edge between distinct elements precisely when their difference is a nonzero square. Let \(K=\operatorname{Cl}(P_{25})\) denote its ordinary flag (clique) complex. Then
\[
K\simeq\bigvee^{64}S^2.
\]
Moreover, the natural action of its full graph automorphism group
\[
G=\{x\mapsto a x^{5^e}+b:\ a\in(\mathbb F_{25}^{\times})^2,\ b\in\mathbb F_{25},\ e\in\{0,1\}\},\qquad |G|=600,
\]
on \(\widetilde H_2(K;\mathbb Q)\) has the complete sixteen-class character in `character_table.csv`. Equivalently, if \(R_g\) is the graph whose vertices are cycles of \(g\) that individually induce cliques of \(P_{25}\), and whose edges join two such cycles when their union induces a clique, then
\[
\chi(g)=-\sum_{C\in\operatorname{Cl}(R_g)}(-1)^{|C|},
\]
where the empty clique is included. The character takes the values \(64,4,0,-1,-16\) with respective element multiplicities \(1,62,450,72,15\).

For the translation subgroup \(T\cong(\mathbb Z/5)^2\), the complex representation of \(\widetilde H_2(K;\mathbb C)\) has additive-character multiplicities \(4\) for the trivial character, \(2\) for each of the twelve nontrivial square-frequency characters, and \(3\) for each of the twelve nonsquare-frequency characters, using the trace pairing on \(\mathbb F_{25}\). Consequently,
\[
\dim\widetilde H_2(K;\mathbb Q)^T=4,\qquad
\dim\widetilde H_2(K;\mathbb Q)^G=0.
\]
Thus the ordinary quotient \(|K|/T\) has four-dimensional reduced rational second homology, whereas \(|K|/G\) is rationally acyclic. For the subgroup fixing the zero field element, the invariant dimension is one.

The rational Betti number \(64\), by itself, is covered by the general Latin-square-graph homology theorem of Cioabă and Mim (2026) and is **not** claimed as new. The claims here are the explicit homotopy upgrade and the complete action on homology, including the Fourier decomposition and quotient consequences.

## Assumptions and scope

Use \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\), represented by integers \(5a+b\) for \(a,b\in\{0,1,2,3,4\}\), meaning \(a+bt\). Its nonzero-square subgroup has twelve elements, and the graph has vertex set the twenty-five field elements and degree twelve. A simplex is a nonempty set of pairwise adjacent vertices, together with the usual empty face. The invariant quotients are geometric realizations of ordinary orbit spaces, with rational coefficients and not homotopy-orbit constructions. No equivariant homotopy equivalence is asserted.

The full character formula uses the ordinary signed simplicial action on ordered oriented faces; no preferred choice of homology basis is needed. In the Fourier description, a frequency \(u\) labels the additive character \(t\mapsto\exp(2\pi i\operatorname{Tr}_{\mathbb F_{25}/\mathbb F_5}(ut)/5)\).

## Proof

**The graph and its automorphisms.** The twelve nonzero squares split into three one-dimensional \(\mathbb F_5\)-subspaces with their origins removed. A linear coordinate change identifies the corresponding three directions with horizontal, vertical, and constant-sum directions. Thus adjacency is exactly the Latin-square-graph relation: two points share a row, a column, or a sum-coordinate. Any four-clique lies in one of these lines. Indeed, normalize a noncollinear triangle to \((0,0),(a,0),(0,a)\); a fourth vertex on any of the three directions through \((0,0)\) cannot be adjacent to both other points unless \(2a=0\), which is impossible for nonzero \(a\) in characteristic five. Hence all maximal five-cliques are the fifteen five-point lines, in three disjoint parallel classes of five. A graph automorphism permutes those three classes. The kernel is an autotopism of the addition Latin square: if coordinate permutations \(f,g,h\) satisfy \(f(x)+g(y)=h(x+y)\), then subtracting the values at zero shows that \(h-h(0)\) is additive, hence multiplication by an element of \(\mathbb F_5^\times\). The kernel has exactly \(25\cdot4=100\) elements. The displayed semilinear affine group has \(25\cdot12\cdot2=600\) distinct adjacency-preserving permutations; its multiplier and Frobenius actions generate all permutations of the three directions. Hence it is the full automorphism group.

**A complete Morse reduction.** Lexicographically enumerate cliques of each cardinality by intersecting common neighbor sets; their numbers in dimensions \(0,1,2,3,4\) are exactly \((25,150,250,75,15)\), with no larger faces. On the nonempty face poset, for each pivot vertex \(v=0,1,\ldots,24\), in order, pair every still-unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) whenever both are still unmatched. Use sorted face iteration to make the construction deterministic. The resulting matching has exactly \(225\) face pairs. Explicitly orient each cover of the face poset downward, except paired covers, which are oriented upward. Kahn's topological-sort algorithm visits all \(515\) faces, giving a full acyclicity certificate rather than an inference from Betti numbers. Exactly one critical vertex and exactly \(64\) critical two-faces remain, with no critical faces in any other dimension. Forman's discrete Morse theorem therefore gives a CW complex with one zero-cell and sixty-four two-cells and no one-cells; every attaching map of a two-cell to that zero-cell is null. This establishes the claimed integral homotopy type.

**The complete character.** For any automorphism \(g\), the reduced Lefschetz number is \(-1\) plus the alternating signed trace on all nonempty simplices. Because the above Morse reduction proves all reduced rational homology is concentrated in even degree two, this is exactly \(\chi(g)\). A \(g\)-invariant simplex is a union of cycles of the vertex permutation; a union of \(r\) cycles has oriented-sign contribution \((-1)^{r-1}\) to the simplicial Lefschetz sum. This yields the displayed orbit-clique formula, which is independently checked against direct signed fixed-face counting for each of the \(600\) automorphisms. Direct group-conjugation enumeration gives sixteen conjugacy classes with the sizes and traces provided in the accompanying table.

**Fourier multiplicities and quotients.** A nonidentity translation has five vertex cycles of length five. If its displacement is a nonzero square, those cycles are precisely five affine lines and \(\chi=4\); if the displacement is a nonsquare, none is a clique and \(\chi=-1\). Therefore \(\chi|_T\) equals \(64\) at identity, \(4\) on twelve nonzero squares, and \(-1\) on twelve nonsquares. Taking the discrete Fourier transform under the field trace pairing yields the stated \(4,2,3\) multiplicities. Summing the complete class character yields zero full-group invariants, and averaging the translations yields four. Averaging the order-twenty-four subgroup fixing zero yields one. Rational transfer after barycentric subdivision identifies homology of each ordinary finite-group quotient with the invariants, proving the quotient statements.

## Verification

Run `python3 verify.py` with standard-library Python. The verifier independently reconstructs all faces, checks the entire directed Hasse graph for cycles, recomputes reduced boundary ranks modulo three distinct primes, tests the \(600\) graph permutations, and obtains character values by two distinct formulas. It also checks conjugacy-class constancy, all sixteen class sizes, exact Fourier coefficients in the fifth-cyclotomic integer ring, and subgroup averages. `verification_output.txt` records the completed execution. `character_table.csv` is a human-readable representation of the verified sixteen-class character. The modular computations provide cross-checks; the integral homotopy claim rests on the finite acyclic matching, not on modular ranks.

## Relationship to prior work

Lim and Praeger (arXiv:math/0605252, first public May 10, 2006) study generalized Paley graphs and automorphism groups, supplying the historical graph-theoretic setting. Costa, Farber, and Horak (2015) develop homotopical questions for clique complexes. Cioabă, Guo, Ji, and Mim (2025/2026) analyze clique-complex Laplacians and first cohomology of strongly regular graphs, including Paley examples. Most directly, Cioabă and Mim (arXiv:2606.27328, June 25, 2026), Theorem 3.12, already prove that the Latin-square-graph clique homology is concentrated in degree two and has rank \((n-1)^3-I(M)\). At order five with the addition Latin square, \(I(M)=0\), so that theorem subsumes the homology-rank statement here. Its relevant sections give field-homology and Laplacian results, not a simplicial Morse wedge equivalence or the full \(600\)-element homology character. Those are the differences claimed. No priority claim is made against unindexed or undiscovered results.

## Limitations

This is an exact finite theorem for the order-twenty-five Paley graph. It does not establish an analogous wedge or character decomposition for larger Paley graphs, integral group-module normal forms, integral quotient torsion, or equivariant homotopy types. The non-equivariant Morse matching is not asserted to be group-invariant. The full published-priority question remains subject to independent literature review. No independent mathematical audit has been performed.

## References

- T. K. Lim and C. E. Praeger, *On generalised Paley graphs and their automorphism groups*, arXiv:math/0605252 (first public 2006-05-10), https://arxiv.org/abs/math/0605252.
- A. Costa, M. Farber, and D. Horak, *Fundamental groups of clique complexes of random graphs*, Transactions of the London Mathematical Society 2 (2015), 1–32, https://doi.org/10.1112/tlms/tlv001.
- S. M. Cioabă, K. Guo, C. Ji, and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, Linear Algebra and its Applications 730 (2026), 152–197, online 2025-10-20, https://doi.org/10.1016/j.laa.2025.10.013.
- S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (first public 2026-06-25), especially Theorem 3.12, https://arxiv.org/abs/2606.27328.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
