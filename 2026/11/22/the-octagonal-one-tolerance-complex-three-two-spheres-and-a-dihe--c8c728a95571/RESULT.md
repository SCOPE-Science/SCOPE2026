# The rational dihedral homology of the octagonal one-tolerance complex

## Finding

Let \(G=C_8^2\) be the graph on \(\mathbb Z/8\) with edges at cyclic distances one and two. Let \(K=\operatorname{Cl}(G)\) be its filled clique complex, and let \(X=\mathcal T_1(K)\) consist of the faces of \(K\) enlarged by at most one vertex. Let the order-sixteen dihedral group \(D_8=\langle r,s:r^8=s^2=1,\ srs=r^{-1}\rangle\) act on \(X\) by \(r(i)=i+1\) and \(s(i)=-i\).

The only nonzero reduced rational homology is in degree two, with
\[
\widetilde H_2(X;\mathbb Q)\cong\varepsilon_{-,-}\oplus\rho_2
\quad\text{as a rational }D_8\text{-module,}
\]
where \(\varepsilon_{-,-}(r)=\varepsilon_{-,-}(s)=-1\), and \(\rho_2\) has \(r\) a quarter turn and \(s\) a reflection. Thus the character values on \(r^a\) and \(r^as\), in order \(a=0,\ldots,7\), are
\[
(3,-1,-1,-1,3,-1,-1,-1),\qquad (-1,1,-1,1,-1,1,-1,1).
\]
The geometric quotients by all rotations and by \(D_8\) have zero reduced rational homology. The geometric quotient by the single reflection \(i\mapsto a-i\) has second rational Betti number one for even \(a\) and two for odd \(a\); its other reduced rational homology is zero.

## Assumptions and scope

The group acts on the geometric realization of the specified finite complex. The action and quotient claims are over \(\mathbb Q\). Neither deleting the filled triangles from the input nor replacing the tolerance rule by a robust-clique or a two-independence rule gives the same complex. The ordinary wedge of three two-spheres below is an input to the character computation, not a separate originality claim.

## Proof

**Faces and ordinary homology.** The four neighbors of each vertex induce a path on four vertices, so there is no four-clique. The graph's only three-cliques are the eight consecutive triples. There is no independent triple, since the three gaps between its cyclically ordered vertices would each be at least three. It follows that \(X\) has the full two-skeleton on eight vertices. Its tetrahedra are precisely the consecutive triples with one further vertex: there are \(8\cdot5-8=32\), because four consecutive vertices account for the eight double descriptions. No larger faces exist.

For context, the three-stage collapse in [1] specializes at eight even though its theorem is stated for nine and above. In the table below, all subscripts are modulo eight and each row is applied for every \(i\), in the indicated order of stages. A pair gives a tetrahedron and the triangle removed with it.

| Stage | Tetrahedron | Triangle |
|---|---|---|
| I | \(\{i,i+1,i+2,i+5\}\) | \(\{i,i+2,i+5\}\) |
| II | \(\{i-2,i,i+1,i+2\}\) | \(\{i-2,i+1,i+2\}\) |
| II | \(\{i,i+1,i+2,i+4\}\) | \(\{i,i+1,i+4\}\) |
| III | \(\{i,i+1,i+2,i+3\}\) | \(\{i,i+1,i+3\}\) |

In stage I the chosen face has only one graph edge, \(\{i,i+2\}\), and only \(i+1\) completes that edge to a consecutive triple. In stage II the first chosen face can complete its sole graph edge \(\{i+1,i+2\}\) with \(i\) or \(i+3\); the second can complete \(\{i,i+1\}\) with \(i+2\) or \(i-1\). The second alternative in each case gives a tetrahedron already removed in stage I. The only alternatives in stage III add \(i+2\) or \(i-1\); the latter is a stage II tetrahedron. The table accounts for all 32 distinct tetrahedra. The supplied collapse certificate gives another direct verification of reduction to dimension two. The complete two-skeleton makes \(X\) simply connected, and its Euler characteristic is \(8-28+56-32=4\). It therefore has free integral \(H_2\) of rank three and no other reduced integral homology. Representing a basis by spheres via Hurewicz and applying the homological Whitehead theorem gives the ordinary wedge of three 2-spheres. No equivariance of these collapses or of this wedge description is assumed.

**Traces from the fixed-face rule.** For a dihedral permutation \(g\), a setwise-fixed simplex is a union of vertex cycles. If it has \(k\) vertices and \(c\) cycles, its contribution to the alternating oriented-chain trace is \((-1)^{k-1}(-1)^{k-c}=(-1)^{c-1}\). We can therefore count simplices on the vertex cycles, admitting a collection exactly when its union is a face of \(X\). The resulting Euler characteristic is \(1+\operatorname{tr}(g\mid H_2(X;\mathbb Q))\).

- The identity has Euler characteristic four. An odd power of \(r\) has only an eight-cycle. The rotations \(r^2,r^6\) have two four-cycles, each using only one parity class, so neither gives an admitted tetrahedron. The half-turn \(r^4\) has four admitted antipodal pairs; a union of two pairs occupies only two residues modulo four and cannot contain a consecutive triple. Its cycle complex has four isolated vertices.
- For \(s\), the cycles are \(\{0\},\{4\},\{1,7\},\{2,6\},\{3,5\}\). The admitted pairs of cycles consist of the two singletons together and the six singleton-plus-pair collections; unions of two transpositions contain no consecutive triple. Exactly two triples of cycles are admitted, the two singletons together with \(\{1,7\}\) or \(\{3,5\}\). The Euler characteristic is \(5-7+2=0\).
- For \(rs\), the four cycles are \(\{0,1\},\{2,7\},\{3,6\},\{4,5\}\). The only admitted unions of two cycles are the first two together and the last two together. The Euler characteristic is \(4-2=2\). All even-parameter reflections are conjugate to \(s\), and all odd-parameter reflections to \(rs\).

These counts give the two character lists. They agree with the sum of the sign character and the two-dimensional character of the rational matrices
\[
r\longmapsto\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
s\longmapsto\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Characters determine the isomorphism class here: rational representations of this finite group are semisimple, and equality of characters after extending to \(\mathbb C\) implies isomorphism over \(\mathbb Q\).

**Geometric quotients.** In the barycentric subdivision a group element stabilizing a simplex fixes each vertex because those vertices have distinct original face cardinalities. The quotient chain complex over \(\mathbb Q\) is therefore the complex of coinvariants. Averaging identifies these with invariants, and is exact over \(\mathbb Q\). The average trace over the rotation subgroup is \((3+3-6)/8=0\), which also forces zero invariants under the full group. The invariant dimension under a reflection of trace \(\tau\) is \((3+\tau)/2\), giving the two asserted ranks. Connectedness and the disappearance of every other reduced homology degree follow from the same quotient argument.

## Reproducibility

The accompanying standard-library program `check.py` and `collapse_certificate.json` can be used as supplied. They verify the face oracle, a sequential free-face collapse to dimension two, all sixteen oriented face traces, and the quotient ranks. The fixed-cycle computation above independently explains the two reflection counts and requires no equivariant choices in the collapse.

## Relationship to prior work and limitations

The ordinary wedge is the eight-vertex specialization of the proof in [1]; the distinct conclusion here concerns the action and the two geometric reflection quotients. The same rational representation occurs for a different octagonal object, the independence complex of the chord-disjointness graph on 20 vertices in [2]. In that case the four-term rotation permutation module modulo its diagonal gives the same character, but its chord face rule and action on faces are not those of the eight-vertex tolerance complex. The octagonal two-independence complex has no consecutive triple as a face and in fact has a different full-dihedral quotient [3]. General Leray and chordal-graph tolerance bounds [4,5] do not compute the character; the even vertices of \(C_8^2\) induce a chordless four-cycle. No claim is made about homotopy types or integral homology of the geometric quotients, the integral representation lattice of \(X\), or characters at other cycle lengths.

## References

1. [Quadratic sphere wedges in one-tolerance complexes of squared cycles](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-quadratic-sphere-wedges-in-one-tolerance-complexes-of-squared-cy--8051329e5a96/RESULT.md), §§1–4 of the proof.
2. [The integral dihedral homology lattice of the first eight-point stable Kneser independence complex](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-the-integral-dihedral-homology-lattice-of-the-first-eight-point--75de5c5113c2/RESULT.md), Finding and assumptions.
3. [The full dihedral quotient of the octagonal two-independence complex is a homotopy three-sphere](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-full-dihedral-quotient-of-the-octagonal-two-independence-com--93294cc21c41/RESULT.md), Finding and assumptions.
4. M. Kim and A. Lew, *Leray numbers of tolerance complexes*, [arXiv:2109.03030](https://arxiv.org/abs/2109.03030).
5. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, [arXiv:2611.14384v1](https://arxiv.org/abs/2611.14384v1), Theorem 1.3.
