# Dihedral fixed loci and integral orientation modules of cycle coloring complexes

## Finding

Let \(n\ge3\), let \(C_n\) be the simple graph with vertices \(\mathbb Z/n\mathbb Z\) and edges between consecutive residues, and let \(X_n=\Delta(C_n)\) be the **ordinary Steingrímsson coloring complex**, realized as the union of graphical-arrangement hyperplanes in the sphere \(S^{n-2}\) of the coordinate-sum-zero space. The dihedral group \(D_n=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\).

Let \(\mathcal A_n\) be the set of acyclic orientations of \(C_n\), so \(|\mathcal A_n|=2^n-2\). Let \(\mathbf 1=\sum_{A\in\mathcal A_n}[A]\) in the integral permutation lattice, and let \(\varepsilon_n(g)\) be the sign of the permutation of the \(n\) vertex labels induced by \(g\). There is an **integral, \(D_n\)-equivariant isomorphism**
\[
\widetilde H_{n-3}(X_n;\mathbb Z)\ \cong\
\mathbb Z_{\varepsilon_n}\otimes_{\mathbb Z}
\bigl(\mathbb Z[\mathcal A_n]/\mathbb Z\mathbf1\bigr).
\]
All other reduced integral homology groups vanish. In particular, the only nonzero reduced Betti number is \(2^n-3\). This specifies the **quotient by the diagonal**, not the kernel of the augmentation map; those lattices need not be integrally isomorphic.

The complete rational character \(\chi_n(g)=\operatorname{tr}\bigl(g\mid\widetilde H_{n-3}(X_n;\mathbb Q)\bigr)\) is explicit. For \(0\le k<n\), put \(d=\gcd(n,k)\) (so \(d=n\) if \(k=0\)); then
\[
\chi_n(r^k)=(-1)^{n-d}(2^d-3).
\]
Writing every reflection uniquely as \(r^a s:i\mapsto a-i\), its trace is
\[
\chi_n(r^as)=
\begin{cases}
(-1)^{(n+1)/2},&n\text{ odd},\\
(-1)^{(n-2)/2}(2^{n/2}-1),&n\text{ even and }a\text{ even},\\
(-1)^{n/2+1},&n\text{ even and }a\text{ odd}.
\end{cases}
\]

The **actual geometric fixed-point spaces** are also classified. The rotation-fixed locus is empty when \(d\le2\), and is PL-homeomorphic to \(X_d\) when \(d\ge3\), so is homotopy equivalent to \(\bigvee^{2^d-3}S^{d-3}\). Every reflection for odd \(n\) fixes a sphere \(S^{(n-3)/2}\). For even \(n\), reflections with odd \(a\) (axes through opposite edges) fix \(S^{n/2-2}\); those with even \(a\) (axes through opposite vertices) fix the graphical coloring-arrangement link of the path on \(n/2+1\) vertices, hence a wedge of \(2^{n/2}-1\) spheres \(S^{n/2-2}\). The PL statement applies to the arrangement-link models; the wedge statements are homotopy classifications.

As a consequence, the ordinary quotient \(X_n/D_n\) has reduced rational homology only in degree \(n-3\), with rank
\[
 b_n=\frac{1}{2n}\left(\sum_{k=0}^{n-1}(-1)^{n-\gcd(n,k)}(2^{\gcd(n,k)}-3)+R_n\right),
\]
where \(R_n=n(-1)^{(n+1)/2}\) for odd \(n\) and
\[
R_n=\frac n2\left((-1)^{(n-2)/2}(2^{n/2}-1)+(-1)^{n/2+1}\right)
\]
for even \(n\). For \(n=8\), the ambient fifth reduced homology has rank \(253\), the quotient has rank \(13\), and the two reflection-axis types fix respectively a two-sphere and a wedge of fifteen two-spheres.

## Assumptions and scope

All groups are finite and all topological spaces are geometric realizations of simplicial complexes. The sphere is
\[
S_n=\{x\in\mathbb R^n: \textstyle\sum_{i=0}^{n-1}x_i=0,\ \sum_i x_i^2=1\}\cong S^{n-2},
\]
and the arrangement-link realization is
\[
X_n=S_n\cap\bigcup_{i=0}^{n-1}\{x:x_i=x_{i+1}\},
\]
with indices modulo \(n\). By the ordinary braid-arrangement subdivision of the link, this is precisely the usual coloring complex, not the differently defined *cyclic coloring complex*. The action on simplicial chains is induced by relabeling the coordinates. No claim about integral homology of \(X_n/D_n\), arbitrary subgroup fixed loci, or integral decomposition into rational irreducibles is asserted.

## Proof

**1. Chamber lattice and integral exactness.** The graphical arrangement partitions \(S_n\) into open spherical chambers; fixing all strict edge-inequality signs produces a chamber exactly when those oriented inequalities form an acyclic directed graph. Indeed, a directed cycle contradicts increasing coordinates, and a topological ordering of any directed acyclic graph gives a point satisfying all strict inequalities. The chamber associated to any orientation is the intersection of open hemispheres, so it is spherically convex; its closure is a closed \((n-2)\)-ball. Hence the quotient space \(S_n/X_n\) is a wedge of \(|\mathcal A_n|\) spheres of dimension \(n-2\), one for each chamber, and
\[
H_{n-2}(S_n,X_n;\mathbb Z)\cong\mathbb Z[\mathcal A_n].
\]
Orient all chambers using the ambient orientation of the sphere. For any \(g\in D_n\), coordinate permutation has degree \(\varepsilon_n(g)\) on \(S_n\), because its restriction to the mean-zero hyperplane has the same determinant as on \(\mathbb R^n\). Thus the relative homology is the **orientation-sign-twisted** chamber permutation lattice. Under the long exact sequence of the pair, the ambient fundamental class maps to the signed-diagonal chamber sum \(\mathbf1\). All other relative groups vanish, so the cokernel is the claimed top reduced homology over \(\mathbb Z\); all other reduced homology groups vanish. This argument includes the reduced degree-zero case \(n=3\) and proves no torsion can occur.

**2. Dihedral action on chambers.** Encode orientations by bits \(b_i\in\{0,1\}\) on directed reference edges \((i,i+1)\). The two constant bit strings give the two directed cycles, so precisely \(2^n-2\) bit strings remain. Under \(r^k\), the \(n\) edge bits have \(d=\gcd(n,k)\) orbits and preserve their reference direction. There are therefore \(2^d-2\) fixed acyclic orientations. The sign of the vertex permutation is \((-1)^{n-d}\), giving the rotation formula after subtracting the diagonal line.

A reflection \(r^as\) sends edge \(i\) to edge \(a-i-1\) and **reverses its reference direction**. Any edge fixed setwise by a reflection prevents an invariant orientation. For odd \(n\), every reflection fixes one edge, so its invariant chamber count is zero. For even \(n\) and odd \(a\), two edges are fixed, so the count is again zero. For even \(n\) and even \(a\), the edges form \(n/2\) two-element orbits and each pair must have opposite reference bits, giving \(2^{n/2}\) fixed orientations; neither constant cyclic orientation is among them. The permutation sign is \((-1)^{(n-1)/2}\) for odd \(n\), \((-1)^{(n-2)/2}\) for even \(n\) with even \(a\), and \((-1)^{n/2}\) for even \(n\) with odd \(a\). Multiplying the fixed-chamber count minus one proves the reflection formula.

**3. Geometric fixed loci.** Fix an individual symmetry \(g\), and let its orbits on vertices be \(O_1,\ldots,O_m\). The fixed vectors in \(S_n\) are exactly the mean-zero sphere in the \(m\)-dimensional real space of coordinate functions constant on the orbits; this is \(S^{m-2}\) if \(m\ge2\) and empty otherwise. If any cycle edge has both ends in the same \(g\)-orbit, its equality hyperplane contains the whole fixed sphere. If no edge does, the fixed link is precisely the graphical-arrangement link for the graph on these \(m\) orbit vertices induced by edges between orbits (parallel edges do not alter the link). For \(r^k\), this quotient is \(C_d\) when \(d\ge3\), the edge \(K_2\) when \(d=2\), and has one orbit when \(d=1\). For odd reflections and for even edge-axis reflections, an edge lies within a vertex orbit, yielding the full fixed sphere. For even vertex-axis reflections no such edge exists, and the orbit graph is the path \(P_{n/2+1}\). The weighted coordinate-mean-zero subspace on the orbits is linearly isomorphic (modulo the all-ones direction) to the ordinary mean-zero space on the orbit labels, and translation along the all-ones direction preserves all pairwise coordinate equalities. Radial normalization therefore identifies their arrangements and associated PL triangulations. A tree with \(m\) vertices has \(2^{m-1}\) acyclic orientations. Applying Step 1 without the group action gives the asserted wedge multiplicities and dimensions.

**4. Rational quotient.** The transfer isomorphism for finite group actions and rational coefficients identifies the homology of the geometric quotient with the group-invariant rational homology. Averaging the characters from Step 2 over \(2n\) dihedral elements gives the stated formula for \(b_n\). The homological concentration in Step 1 rules out further positive-degree rational quotient homology. The same reduced-degree-zero statement holds for \(n=3\).

## Verification

The included `VERIFY.py` independently enumerates all \(2^n-2\) acyclic-orientation bit strings and all \(2n\) vertex permutations for every integer \(3\le n\le12\). It checks invariant chamber counts directly against the closed formulas, recomputes the signs as permutation inversion parities, and compares the resulting Lefschetz Euler characteristic \(1+(-1)^{n-3}\chi_n(g)\) with a separate computation of the geometric fixed arrangement using vertex-orbit graphs and acyclic-orientation enumeration. It also checks that the averaged invariant rank is a nonnegative integer. All \(150\) group elements tested pass. The recorded output is in `verification_output.txt`. This finite test is not the proof of the all-\(n\) theorem; the preceding exact relative-homology and orbit arguments are.

## Relationship to prior work

Steingrímsson introduced the coloring complex and related its combinatorics to graph colorings and acyclic orientations [1]. Jonsson established ordinary homotopy concentration for coloring complexes [2]. Hersh and Swartz identified this simplicial complex with the graphical-arrangement link and recovered the **nonequivariant** rank \(|\mathcal A(G)|-1\) [3]. These foundational facts and the ordinary rank are **not claimed as new**. The contribution isolated here is the explicit full integral action of polygon rotations and reflections, its complete character, the geometry of every element-fixed locus, and the resulting quotient homology for all cycle lengths; these are not given by the scalar rank alone.

Macauley and Mortveit's cyclic/dihedral equivalence of acyclic orientations [4] is generated by source-to-sink flips and global reversal of edge directions, **not** by the vertex-relabeling \(D_n\)-action used here. Braun and Crown Rundell's hyperoctahedral Hodge operators [5] act on chain slots of a different signed-graph construction; their stated results do not identify the integral cycle-label automorphism lattice. The similarly named *cyclic coloring complex* studied by Crown Rundell is a different simplicial construction and is not substituted for \(\Delta(C_n)\).

## Limitations

The integral lattice description is not an integral calculation of the quotient's homology; only rational quotient homology follows from transfer. Individual element-fixed loci are classified, not arbitrary subgroup fixed loci. The exact integral module may encode nonsplit extensions invisible in the rational character, but no specific extension classification is separately asserted beyond its explicit quotient-lattice presentation. The directly inspected literature did not show an identical equivariant statement; unindexed or inaccessible primary material (especially Jonsson's complete 2005 article and Hanlon's 2008 Hodge work) remains a publication-priority risk. No independent mathematical review has been performed.

## References

[1] E. Steingrímsson, *The Coloring Ideal and Coloring Complex of a Graph*, arXiv:math/0104063v1, first posted 2001-04-05; https://arxiv.org/abs/math/0104063 .

[2] J. Jonsson, *The Topology of the Coloring Complex*, Journal of Algebraic Combinatorics 21 (2005), 311–329, DOI:10.1007/s10801-005-6914-0 .

[3] P. Hersh and E. Swartz, *Coloring Complexes and Arrangements*, arXiv:0706.3657v1, first posted 2007-06-25; https://arxiv.org/abs/0706.3657 .

[4] M. Macauley and H. S. Mortveit, *Equivalences on Acyclic Orientations*, arXiv:0709.0291v1, first posted 2007-09-03; https://arxiv.org/abs/0709.0291 .

[5] B. Braun and S. Crown Rundell, *Hyperoctahedral Eulerian Idempotents, Hodge Decompositions, and Signed Graph Coloring Complexes*, arXiv:1307.7323v1, first posted 2013-07-28; https://arxiv.org/abs/1307.7323 .
