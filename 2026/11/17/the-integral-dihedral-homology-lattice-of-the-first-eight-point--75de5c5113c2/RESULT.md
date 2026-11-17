# The integral dihedral homology lattice of the first eight-point stable Kneser independence complex

## Finding

Let \(G=\operatorname{SG}_{2,4}\) be the stable Kneser graph whose vertices are the 20 chords of a regular octagon, excluding its sides, with edges between disjoint chords. Put \(K=\operatorname{Ind}(G)\). The octagon's dihedral symmetry \(D_8=\langle r,s\mid r^8=s^2=1,\;srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\) on the eight polygon vertices modulo eight.

**The integral representation**, not just its rational character or rank, is
\[
\boxed{\widetilde H_2(K;\mathbb Z)\cong
\mathbb Z\langle u_0,u_1,u_2,u_3\rangle/
\mathbb Z(u_0+u_1+u_2+u_3),\quad
r u_j=u_{j+1},\quad s u_j=u_{1-j},}
\]
where subscripts of the \(u_j\) are modulo four. All other reduced integral homology groups vanish, as is already implied by the known nonequivariant homotopy classification.

Thus the eightfold rotation acts on this rank-three lattice with order four, and its integral coinvariants are
\[
\boxed{\widetilde H_2(K;\mathbb Z)_{\langle r\rangle}\cong\mathbb Z/4\mathbb Z.}
\]
Although the rational rotation module is a sign line plus the two-dimensional quarter-turn representation, **these summands do not split as integral rotation modules**. Over \(\mathbb F_2\), the operator \(r-1\) has one nilpotent Jordan block of size three.

## Assumptions and scope

All simplicial complexes here are abstract, finite, and include the empty face; geometric realization and reduced integral simplicial homology use their standard definitions. A chord is an unordered pair of distinct residues modulo eight that are not consecutive. An admissible triple consists of three pairwise nonconsecutive octagon vertices. The action on oriented chains includes the sign of the induced permutation of each simplex's vertices. The statement concerns this specific 20-vertex complex and its specified order-sixteen dihedral symmetry; it does not assert a classification for all stable Kneser parameters.

## Proof

**1. Reduce to a graph plus sixteen triangles.** The faces of \(K\) are pairwise-intersecting families of octagon chords. Every such family is either a subset of the star of a common polygon vertex, or is exactly the three chords of an admissible polygon triple. To see this, choose two intersecting distinct chords \(\{a,b\}\) and \(\{a,c\}\): a chord meeting both either contains \(a\) or equals \(\{b,c\}\). If the latter occurs, no fourth distinct chord can meet all three. Let \(U\) be the union of the eight full star simplices. The exceptions are sixteen two-simplices, attached along edges in \(U\).

The nerve of the star cover is the graph \(H=\overline{C_8}\) on the original eight polygon vertices: a star-intersection is nonempty exactly when the corresponding two polygon vertices form a chord, and no three distinct star intersections meet. The cover consists of simplices with contractible nonempty intersections. Equivalently, the explicit face-poset closure maps described in the cited equivariant character calculation identify \(U\) with \(H\) equivariantly. Hence \(H_2(U;\mathbb Z)=0\), and the long exact sequence for \((K,U)\) identifies \(H_2(K;\mathbb Z)\) with the kernel of the relative attaching map. Under the canonical chain identification this is the kernel of the ordinary signed boundary
\[
D:\mathbb Z^{16}\longrightarrow\mathbb Z^{20},\qquad
[a,b,c]\longmapsto[b,c]-[a,c]+[a,b],\quad a<b<c,
\]
where the columns are indexed by admissible triples and the rows by chords in lexicographic order. Because \(H\) is a graph, its first integral cycles are literally the kernel of the graph's one-boundary; there is no omitted integral quotient or normalization in this identification.

**2. Exact integer kernel.** Order the sixteen admissible triples lexicographically as follows:

```text
(0,2,4) (0,2,5) (0,2,6) (0,3,5)
(0,3,6) (0,4,6) (1,3,5) (1,3,6)
(1,3,7) (1,4,6) (1,4,7) (1,5,7)
(2,4,6) (2,4,7) (2,5,7) (3,5,7)
```

For the 16 coordinates in that order, define three integer vectors:

```text
b0 = (-1, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)
b1 = ( 1,-1, 0, 1,-1, 1,-1, 1, 0,-1, 1,-1, 0,-1, 1, 0)
b2 = ( 0, 0, 0, 0, 0, 0,-1, 0, 1, 0, 0,-1, 0, 0, 0, 1)
```

Direct signed boundary cancellation gives \(Db_0=Db_1=Db_2=0\). A \(13\times13\) submatrix of \(D\), with zero-based row indices \((0,1,2,3,5,6,7,8,10,11,12,14,15)\) and column indices \((0,1,2,3,4,5,6,7,8,9,10,11,13)\), has determinant \(1\). Thus \(\operatorname{rank}_{\mathbb Q}D\ge13\); the three independent kernel vectors force equality. At the zero-based coordinates \(12,14,15\), the three vectors form the identity matrix. Therefore every *integral* kernel vector is uniquely the integral linear combination of these three vectors with coefficients equal to those three coordinates. Hence they constitute an actual integral basis for \(H_2(K;\mathbb Z)\), not merely a rational basis or a finite-index sublattice.

**3. Full dihedral action and a primitive orbit.** Apply the polygon symmetries to each oriented triple, including its orientation sign. Relative to the basis \((b_0,b_1,b_2)\), the resulting exact integer matrices are
\[
R=\begin{pmatrix}0&-1&-1\\0&-1&0\\1&0&0\end{pmatrix},\qquad
S=\begin{pmatrix}-1&0&0\\0&-1&0\\0&1&1\end{pmatrix}.
\]
The identities \(R^4=I\), \(S^2=I\), and \(SRS=R^{-1}\) hold. Consider \(v=-b_0-b_1\). Its four successive rotation images have basis-coordinate columns
\[
\begin{pmatrix}-1\\-1\\0\end{pmatrix},\quad
\begin{pmatrix}1\\1\\-1\end{pmatrix},\quad
\begin{pmatrix}0\\-1\\1\end{pmatrix},\quad
\begin{pmatrix}0\\1\\0\end{pmatrix}.
\]
Their sum is zero; any three have determinant of absolute value one. In particular the first three are an integral basis, so the single relation is their complete relation lattice. Moreover \(Sv=Rv\), and \(SR^jv=R^{1-j}v\). The map \(u_j\mapsto R^jv\) is therefore the asserted integral \(D_8\)-equivariant isomorphism.

**4. Arithmetic consequence.** The Smith invariants of \(R-I\) are \((1,1,4)\): the gcd of its entries is one, the gcd of its \(2\times2\) minors is one, and its determinant has absolute value four. Consequently its coinvariants are exactly \(\mathbb Z/4\mathbb Z\). The characteristic polynomial of \(R\) is \((t+1)(t^2+1)\). The two rational summands would have separate integral rotation coinvariants \(\mathbb Z/2\mathbb Z\) and \(\mathbb Z/2\mathbb Z\) were they integrally split; the actual cyclic order-four quotient rules this out. Finally the successive ranks of \((R-I)\), \((R-I)^2\), and \((R-I)^3\) modulo two are \(2,1,0\), proving the stated single length-three Jordan block.

## Verification

The accompanying dependency-free script `verify_sg24.py` reconstructs the 20 chords and 16 admissible triples; exhaustively enumerates all 244 nonempty simplices of \(K\); checks the eight-star/triangle classification; constructs all integer entries of \(D\); verifies the unimodular rank-thirteen minor and the three primitive kernel vectors; and calculates both signed dihedral generator matrices from polygon permutations. It then checks the four-element primitive orbit, the dihedral relations, exact Smith invariants, mod-two Jordan ranks, and the signed Lefschetz traces of all sixteen symmetries **directly from the original 244 simplices**. Running `python3 verify_sg24.py` prints `STABLE_KNESER_2_4_INTEGRAL_DIHEDRAL_LATTICE_PASS` after all assertions succeed. The accompanying `verification_output.txt` contains the full recorded output. These are exhaustive finite checks for the specific eight-point complex; the preceding integral kernel argument supplies the mathematical proof.

## Relationship to prior work

Braun's arXiv preprint *Independence Complexes of Stable Kneser Graphs* (2009) proves the nonequivariant wedge-of-two-spheres theorem and supplies the classical polygonal star/triangle structure. It determines that the present second integral homology has rank three but not its integral dihedral module. Schultz's 2010 paper concerns the dihedral topology of graph \(\operatorname{Hom}(K_2,G)\), a different complex. The published *Dihedral character of stable Kneser independence-complex homology* determines the **rational** dihedral character for all polygon sizes using a signed relative-cell model; it explicitly does not classify integral modules. In the eight-point case its character agrees with the matrices above, but rational character agreement does not determine the integral coinvariant group or rule out the two distinct rank-three lattices. None of those statements implies the cyclic order-four coinvariants, primitive orbit presentation or integral nonsplitting established here.

## Limitations

Only the canonical eight-point parameter is classified integrally. The homotopy equivalence to a wedge of three two-spheres was known before this calculation and is not claimed as new. The new lattice result does not establish an equivariant wedge decomposition, the integral homology of geometric symmetry quotients, or analogous lattices for all larger stable Kneser graphs. Unindexed equivalent calculations remain a publication-priority risk. Independent mathematical audit has not been performed.

## References

1. Benjamin Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (first public 2009-12-03), Theorem 1.4 and Section 3. https://arxiv.org/abs/0912.0720 ; journal full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p118/pdf/ .
2. Carsten Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1 (first public 2010-03-29), Sections 4–5. https://arxiv.org/abs/1003.5688 .
3. *The dihedral character of stable Kneser independence-complex homology* (published research record, 2026-10-11): https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-dihedral-character-of-stable-kneser-independence-complex-hom--8af1ffc8127a .
