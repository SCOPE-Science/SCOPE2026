# Binary-translation fixed spaces of bipartite graph complexes are affine-semiflat sphere bouquets

## Finding
For every integer \(r\ge2\), let \(V=\mathbb F_2^r\) and let \(\mathcal B_{2^r}\) denote the simplicial complex of simple bipartite graphs on the fixed vertex set \(V\). A simplex is an edge set giving a bipartite graph; an empty edge set is allowed. The regular translation group \(T=V\) acts on the underlying graph vertices and therefore on its edge-set complex.

The geometric fixed-point space \(|\mathcal B_{2^r}|^T\) is naturally PL-homeomorphic, compatibly with the quotient normalizer \(\operatorname{GL}(r,2)\), to the simplicial complex \(\mathcal K_r\) whose vertices are nonzero vectors of \(V\), and whose faces are exactly the sets contained in a binary affine hyperplane not through the origin:
\[
\mathcal K_r=\bigcup_{0\ne\ell\in V^*}2^{\{v\in V:\ell(v)=1\}}.
\]
Moreover, for every \(r\ge2\),
\[
|\mathcal B_{2^r}|^T\simeq\bigvee^{b_r}S^{r-1},
\]
where the sphere multiplicity \(b_r\) is given by the explicit recurrence below. Thus the only nonzero reduced integral homology group is free of rank \(b_r\) in degree \(r-1\). Examples are \(b_2=1\), \(b_3=6\), \(b_4=91\), \(b_5=2820\), and \(b_6=177661\).

## Assumptions and scope
All graphs are finite, simple and undirected, with isolated vertices allowed. The space \(|\mathcal B_{2^r}|^T\) consists of points in a geometric realization fixed by *all* translations, not merely faces fixed pointwise or setwise. No claim is made about general permutation subgroups or equivariant wedge splittings. The exact PL model is natural for the group \(\operatorname{GL}(r,2)\), while the asserted sphere decomposition is only an ordinary homotopy equivalence.

For \(0\le k\le r\), let the binary Gaussian coefficient be
\[
{r\brack k}_2=\prod_{i=0}^{k-1}\frac{2^{r-i}-1}{2^{k-i}-1},\qquad {r\brack 0}_2=1.
\]
Define the integers
\[
\mu_0=1,\qquad
\mu_k=-1-\sum_{j=1}^{k-1}\left({k\brack j}_2-{k-1\brack j}_2\right)\mu_j
\quad(k\ge1).
\]
Then the nonnegative sphere multiplicity is
\[
b_r=(-1)^r\left[1+\sum_{k=1}^r{r\brack k}_2(2^k-1)\mu_k\right].
\]

## Proof
**1. Geometric fixed points are edge-orbit simplices.** For any simplicial complex with a group action permuting its vertices, a point of its realization is fixed exactly when its barycentric coefficients are constant along each group orbit. Thus its fixed locus is naturally triangulated by the barycenters of vertex orbits whose unions are faces. Translation on the edges of the complete graph on \(V\) has precisely one orbit \(E_d=\{\{x,x+d\}:x\in V\}\) for each nonzero \(d\in V\). Each orbit is a perfect matching, with \(2^{r-1}\) edges. Different differences cannot lie in the same orbit. This gives a simplicial model on the vertex set \(V\setminus\{0\}\): a set \(S\) is a face if and only if the undirected Cayley graph \(\operatorname{Cay}(V,S)\) is bipartite. The linear group permutes these difference orbits, making the identification equivariant.

**2. Bipartiteness is affine-hyperplane containment.** Write \(H=\langle S\rangle\le V\). Each connected component of \(\operatorname{Cay}(V,S)\) is a coset of \(H\). A bipartite coloring of the component containing zero assigns to \(h\in H\) the parity of a word in the generators \(S\). This parity is well-defined exactly if there is no odd-length relation among the generators, equivalently if the Cayley graph has no odd closed walk. Consequently a bipartite coloring exists exactly when the map on generators \(d\mapsto1\) extends to a linear functional \(\ell_H:H\to\mathbb F_2\), which can then be extended to \(V\). Conversely any \(\ell\in V^*\) with \(\ell(d)=1\) for every \(d\in S\) gives a coloring on every coset. For nonempty \(S\), this \(\ell\) is automatically nonzero. The empty face is contained in every hyperplane facet. Therefore the fixed simplicial complex is precisely \(\mathcal K_r\) as displayed.

**3. Intersection poset and its shellability.** Cover \(\mathcal K_r\) by the \(2^r-1\) full simplices indexed by nonzero linear functionals \(\ell\); these simplices have the vertex sets \(H_\ell=\{v:\ell(v)=1\}\). An intersection of such simplices is empty or a full simplex on an affine subspace avoiding the origin, and hence contractible when nonempty. Every nonempty affine subspace \(A=a+W\subset V\) avoiding zero arises as such an intersection: \(a\notin W\), and the functionals vanishing on \(W\) and taking value one on \(a\) span \(W^\perp\); intersecting their affine hyperplanes gives \(a+W\). The cover's intersection-poset lemma (a form of the nerve lemma) identifies the homotopy type of \(\mathcal K_r\) with the order complex of the poset \(P_r\) of **nonempty affine subspaces of \(V\) not containing zero**, ordered by reverse inclusion.

Adjoin \(V\) as a least element. This augmented intersection poset is a geometric semilattice associated to the pointed rank-\(r+1\) matroid of the homogenized affine hyperplane arrangement. In characteristic two the equations \(\ell(x)=1\) homogenize to \(\ell(x)+t=0\), with the hyperplane at infinity \(t=0\) distinguished; standard pointed-matroid shellability applies without a characteristic restriction. Ziegler's EL-shelling theorem for geometric semilattices (1992, Theorem 2.2), building on Wachs--Walker, makes the order complex of its proper affine-intersection part shellable. Its maximal chains have ranks one through \(r\), so the order complex is pure of dimension \(r-1\). Consequently, for \(r\ge2\), it is homotopy equivalent to a wedge of spheres in that dimension; integral reduced homology is free and concentrated there. This use of the geometric-semilattice theorem is a previously established tool, not claimed as a new shellability theorem.

**4. An explicit Möbius calculation.** In the augmented intersection poset, the number of codimension-\(k\) nonempty affine subspaces not through zero equals \({r\brack k}_2(2^k-1)\): choose their direction subspace of codimension \(k\), then a nonzero coset in the quotient of order \(2^k\). Fix such an affine subspace \(A=a+W\) of codimension \(k\). The super-affine subspaces of codimension \(j\) that contain \(A\) and avoid zero correspond to \((k-j)\)-dimensional subspaces of \(V/W\) not containing \(a+W\). Their number is \({k\brack j}_2-{k-1\brack j}_2\) for \(1\le j<k\). Möbius inversion on the interval from the adjoined bottom \(V\) to \(A\) therefore gives \(\mu_0=1\) and the asserted recurrence for \(\mu_k\).

Adjoin an artificial top to the augmented intersection poset. The Möbius invariant of the entire bounded poset equals the reduced Euler characteristic of the order complex of \(P_r\), namely
\[
\widetilde\chi(|P_r|)=-\left[1+\sum_{k=1}^r {r\brack k}_2(2^k-1)\mu_k\right].
\]
Since the only homotopy spheres have dimension \(r-1\), equating this value to \((-1)^{r-1}b_r\) proves the formula. Evaluating the integer recurrence gives the listed multiplicities.

## Verification
The standalone `check_binary_bipartite.py` enumerates all edge-orbit selections for \(1\le r\le4\), constructs their Cayley graphs directly and tests bipartiteness by breadth-first two-coloring; independently it generates the affine-hyperplane facets. All masks agree, including \(32768\) cases for \(r=4\). It also calculates every mod-two reduced boundary rank through \(r=4\), and confirms the predicted Betti number and dimension, with \(r=1\) treated only as a boundary check. Integer Gaussian-binomial and Möbius recurrences check all stated multiplicities through \(r=6\). The finite tests corroborate, but do not replace, the complete argument above. Run `python3 check_binary_bipartite.py` with standard Python, no third-party dependencies.

## Relationship to prior work
The simplicial complex of bipartite graphs and its ordinary nonequivariant sphere-wedge homotopy type were studied by Chari and by Linusson--Shareshian; Jonsson's 2007 monograph, Chapter 14.1, gives a detailed independent treatment and precise general statements. In contrast, nonequivariant wedge dimensions or Euler series do not determine geometric fixed-point homotopy types under translations. The original part here is the family-wide fixed-space identification with the binary affine-hyperplane cover, including the normalizer-natural model and explicit integral sphere multiplicities. Ziegler's 1992 geometric-semilattice shellability result supplies a general theorem used in the proof; it does not concern fixed loci of bipartite graph complexes or their parameter-specific multiplicity formula.

## Limitations
This theorem identifies a specified regular elementary-abelian translation subgroup only; the higher symmetry group may act nontrivially on the resulting homology, which is not computed here. The ordinary homotopy equivalence to a sphere bouquet need not respect the linear-group action. A complete full-text inspection of the Linusson--Shareshian journal article was not possible; mathematical priority remains subject to wider literature review, especially under pointed-matroid terminology. No claim is made of independent external verification.

## References
1. G. M. Ziegler, *Matroid Shellability, β-Systems and Affine Hyperplane Arrangements*, preprint dated February 29, 1992, revised June 14, 1992; *J. Algebraic Combinatorics* 1 (1992), 283–300. https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/030PREPRINT.pdf
2. S. Linusson and J. Shareshian, *Topology of Colors (Extended Abstract)*, Formal Power Series and Algebraic Combinatorics (2000), pp. 268–275. https://doi.org/10.1007/978-3-662-04166-6_24
3. S. Linusson and J. Shareshian, *Complexes of t-Colorable Graphs*, *SIAM J. Discrete Math.* 16 (2003), 371–389. https://doi.org/10.1137/S0895480100366968
4. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer (2007), Chapter 14. https://doi.org/10.1007/978-3-540-75859-4
