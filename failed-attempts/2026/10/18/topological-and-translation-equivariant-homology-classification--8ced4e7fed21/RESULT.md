# Topological and translation-equivariant homology classification of the \(25\)-vertex Paley clique complex

## Finding
Let \(P_{25}\) be the Paley graph whose vertex set is \(\mathbb F_{25}\), with two distinct vertices joined when their difference is a nonzero square. Its ordinary flag, or clique, complex \(X=\operatorname{Cl}(P_{25})\) has integral homotopy type
\[
\boxed{X\simeq\bigvee^{64}S^2.}
\]
In particular, \(\pi_1(X)=1\), \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{64}\), and every other reduced integral homology group vanishes. Together with the homotopy classification, the theorem determines the **entire natural additive-translation representation** on second rational homology. For the translation \(\tau_v:x\mapsto x+v\),
\[
\operatorname{tr}(\tau_v\mid H_2(X;\mathbb Q))=
\begin{cases}
64,&v=0,\\
4,&v\ne0\text{ is a square},\\
-1,&v\text{ is a nonsquare}.
\end{cases}
\]
For an additive character \(\psi:\mathbb F_{25}\to\mathbb C^\times\), define \(s_\psi=\sum_{u\in S}\psi(u)\), where \(S\) denotes the twelve nonzero squares. Then the multiplicity of \(\psi\) in \(H_2(X;\mathbb C)\) is exactly \(4\) for the trivial character, \(3\) for the twelve nontrivial characters satisfying \(s_\psi=2\), and \(2\) for the twelve satisfying \(s_\psi=-3\). Thus the translation-invariant subspace has dimension \(4\).

The numerical homology rank is already covered by a published general Latin-square-graph theorem and is **not** claimed as new. The explicit nonabelian simple-connectivity certificate and the full equivariant character are the additional structural information.

## Assumptions and scope
Identify \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\), whose elements have unique forms \(a+bt\) with \(a,b\in\{0,1,2,3,4\}\). The polynomial is irreducible because \(2\) is nonsquare in \(\mathbb F_5\). Represent \(a+bt\) by \((a,b)\) in lexicographic order. The nonzero quadratic residues are exactly
\[
\{(a,0),(a,a),(a,-a):a\in\mathbb F_5^\times\}.
\]
Thus two vertices are adjacent precisely when their difference lies in one of the three displayed affine directions. This is the order-five cyclic Latin-square graph up to a linear change of coordinates. All homotopy and homology are of the geometric realization of the *ordinary* simplicial clique complex, not of the neighborhood, independence, or graph braid complex. Integer coefficients are used for the homotopy corollaries; no equivariant splitting is asserted.

## Proof
**1. Face structure.** The explicit residue description yields \(25\) vertices and \(150\) edges. Enumeration of pairwise adjacent subsets (or the line-and-transversal classification) gives the complete face vector, counting nonempty simplices by dimensions zero through four,
\[
(f_0,f_1,f_2,f_3,f_4)=(25,150,250,75,15).
\]
All \(15\) four-dimensional simplices are the five-point affine lines in the three square directions. Every three-dimensional simplex belongs to exactly one such line. The complete enumeration and uniqueness conditions are asserted in the independent-from-input deterministic construction in `verify.py`, not inferred from experimental sampling.

**2. An integral homotopy-preserving reduction to dimension two.** For each five-point affine line \(L\), let \(p\) be its least vertex. First remove the pair \((L\setminus\{p\},L)\), where the four-point face is free. Each of the remaining four four-point faces \(T\subset L\), all containing \(p\), can then be paired with its three-point face \(T\setminus\{p\}\). The latter is free because different full lines intersect in at most one vertex, and the other surviving four-point faces of \(L\) all contain \(p\). This gives exactly \(15+4\cdot15=75\) elementary free-face collapse pairs. The remaining connected simplicial complex \(Y\) has \(25\) vertices, \(150\) edges, and \(190\) triangles, and \(X\searrow Y\). In particular, \(X\) and \(Y\) have the same homotopy type.

**3. Nonabelian fundamental-group certificate.** Choose the lexicographically ordered Kruskal spanning tree of the \(150\)-edge one-skeleton. Its \(24\) tree edges are contracted in the cellular presentation of \(\pi_1\); the other \(126\) undirected edges are oriented by increasing vertex index and give free generators. For every oriented triangle \((a,b,c)\), with \(a<b<c\), write the relator \(e_{ab}e_{bc}e_{ca}\), dropping the tree-edge letters. There are \(250\) triangles before collapsing, and elementary collapses preserve the group. The verifier forms these exact \(250\) triangular relations, cyclically freely reduces words, then repeatedly chooses a relation containing some remaining generator exactly once. Cyclically rotate that relator to \(xuv=1\), substitute \(x=(uv)^{-1}\) (or its inverse when the unique letter is inverse-oriented), delete that relator, and freely reduce all other substituted relators. These are valid Tietze transformations, not merely linear row operations. The deterministic sequence eliminates *all \(126\) generators*, leaving neither generators nor nontrivial relators. Hence \(\pi_1(Y)=1\). The generator-selection order and every word substitution are reproduced from first principles in `verify.py` without a database, external graph package, random seed, or proprietary calculation.

**4. Homotopy conclusion.** The Euler characteristic is
\[
\chi(X)=25-150+250-75+15=65.
\]
As \(Y\) is a connected, simply connected two-dimensional finite CW complex, its cellular homology has \(H_1=0\) and \(H_2\cong\mathbb Z^{64}\). In dimension two, \(H_2\) is a subgroup of a free abelian cellular chain group, so it is free. The Hurewicz isomorphism supplies maps of \(64\) two-spheres representing a basis of \(H_2\); their wedge induces an isomorphism on integral homology. The homological Whitehead theorem for simply connected CW complexes makes that wedge map a homotopy equivalence. Therefore \(X\simeq Y\simeq\bigvee^{64}S^2\).

**5. Exact translation character.** For a nonzero translation \(\tau_v\), all vertex orbits have size \(5\). A setwise fixed simplex must therefore have exactly five vertices; there are no invariant simplices of smaller size. Such a simplex is an affine line parallel to \(v\), which is a clique precisely when \(v\) belongs to the square set \(S\). If \(v\in S\), exactly five affine lines are fixed, each with orientation sign \(+1\) because its vertices are permuted in a five-cycle. If \(v\notin S\), no positive-dimensional or zero-dimensional simplex is fixed. Thus the ordinary Lefschetz number is \(5\) for nonzero square translations and \(0\) for nonsquare translations. Since \(H_0\) is one trivial line and only \(H_2\) survives in positive degrees, the character values are \(4\) and \(-1\), respectively, with identity trace \(64\).

For an additive character \(\psi\ne1\), Fourier inversion yields
\[
m_\psi=\frac{1}{25}\left(64+4\sum_{v\in S}\overline{\psi(v)}-\sum_{v\notin S\cup\{0\}}\overline{\psi(v)}\right)
=\frac{13+s_\psi}{5}.
\]
The adjacency matrix of \(P_{25}\) has parameters \((25,12,5,6)\), checked directly, and obeys \(A^2+A=6I+6J\). Hence its eigenvalues on nontrivial additive characters are the two roots of \(z^2+z-6=0\), namely \(2\) and \(-3\). The trace of \(A\) gives multiplicity \(12\) for each. Substituting into the inversion formula proves multiplicities \(3\) and \(2\); the trivial character has multiplicity \((64+12\cdot4-12)/25=4\). These sum to \(4+12\cdot3+12\cdot2=64\), providing a dimension check. This is an equivariant classification, not merely an ordinary Betti-number calculation.

## Verification
Run `python3 verify.py` with Python \(3\) and only its standard library. The program builds \(\mathbb F_{25}\), enumerates all cliques, explicitly verifies every one of the \(75\) free-face collapses against all remaining cofaces, constructs the \(126\)-generator presentation, and performs \(126\) mathematically justified Tietze eliminations. It also enumerates exact simplex-fixed-point Lefschetz traces for all \(25\) translations and checks the strongly regular adjacency parameters used in Fourier inversion. A successful run prints `PI1_TRIVIAL; WEDGE_64_S2; VERIFY_OK`. The face-vector and Euler-characteristic identities are asserted independently of any published homology table. The enumeration is exhaustive on a defined set of \(25\) vertices; no generalization to larger Paley graphs is extrapolated.

## Relationship to prior work
Cioabă and Mim, *On the homology groups of clique complexes of strongly regular graphs* (arXiv:2606.27328, first submitted 2026-06-25), Theorem 3.12, determine the homology of the clique complex of every order-at-least-five Latin-square graph **over every field**. For the cyclic order-five Latin square there are no \(2\times2\) intercalates, and their theorem implies second Betti number \((5-1)^3=64\), with all other positive-degree field homologies zero. That stronger general homological calculation **covers** the numerical Betti formula in this finding. Their paper's Introduction, Sections 3.2–3.5, and integral Smith-invariant Proposition 3.13 address homology and Laplacians, not simple connectivity, nonabelian Tietze elimination, or an integral wedge-of-spheres homotopy type. Those homotopy-strengthening and translation-character statements are the distinct contribution here, independently proved above. The general homology theorem does not prescribe the action of translations on those classes.

Kahle, *Topology of random clique complexes* (arXiv:math/0605536, initially submitted 2006-05-19), is an early source for clique-complex topology and for the conceptual distinction between homology concentration and sphere-wedge homotopy. Its random-graph setting does not contain a deterministic Paley-graph homotopy computation. Earlier work on cliques in square-order Paley graphs addresses extremal and maximal clique geometry, not the homotopy type of this clique complex. An unpublished or unindexed equivalent Paley-specific fundamental-group reduction remains a bibliographic possibility; absence from searches is not a uniqueness proof.

## Limitations
The claim concerns one specific \(25\)-vertex Paley graph. The complete integral homology ranks were already inferable from the general Latin-square-graph theorem, and their coincidence is explicitly acknowledged; the homotopy strengthening is not claimed as a theorem for every Latin square or every square-order Paley graph. The fundamental-group calculation is a finite but exhaustive, deterministic group-presentation proof. Its reliability depends on the validity of the explicit elementary collapse and Tietze steps, each checked by the included executable. Unindexed equivalent homotopy or translation-module calculations may exist.

## References
- M. Kahle, *Topology of random clique complexes*, arXiv:math/0605536, first submitted 2006-05-19; https://arxiv.org/abs/math/0605536.
- S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, first submitted 2026-06-25; Theorems 3.6, 3.8, 3.12 and Proposition 3.13; https://pdfs.assets.alphaxiv.org/2606.27328v1.pdf.
- R. D. Baker, G. L. Ebert, J. Hemmeter, and A. J. Woldar, *Maximal cliques in the Paley graph of square order*, Journal of Statistical Planning and Inference 56 (1996), 33–38; https://doi.org/10.1016/S0378-3758(96)00006-7. Cited solely for the earlier clique-geometry context, not for the topological conclusion.
