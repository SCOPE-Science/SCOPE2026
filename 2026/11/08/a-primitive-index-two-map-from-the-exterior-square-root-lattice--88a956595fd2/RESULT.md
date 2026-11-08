# A primitive index-two map from the exterior-square root lattice to the Petersen generalized-Jacobian lattice

## Finding
Let \(k\) be any finite field, \(X/k\) any smooth del Pezzo surface of degree five, and \(D\subset X\) the reduced union of its ten geometric \((-1)\)-curves. The geometric dual graph \(P\) of \(D\) is the Petersen graph, with the natural action of \(S_5\). Let
\[
A_4=\{(a_0,\ldots,a_4)\in\mathbb Z^5:\sum_{i=0}^4a_i=0\},\qquad B=\bigwedge^2 A_4,
\]
where \(S_5\) permutes the five coordinates, and let \(H=H_1(P,\mathbb Z)\), including its signed edge-orientation action.

**Integral statement.** There exists an \(S_5\)-equivariant injection \(\iota:B\hookrightarrow H\) with cokernel \(\mathbb Z/2\mathbb Z\). Furthermore
\[
\operatorname{Hom}_{\mathbb Z[S_5]}(B,H)=\mathbb Z\,\iota.
\]
Thus \(B\otimes\mathbb Q\cong H\otimes\mathbb Q\) as \(S_5\)-modules but \(B\not\cong H\) as integral \(S_5\)-modules. In particular, **every** nonzero equivariant integral map from \(B\) to \(H\) has index \(2|m|^6\) for a nonzero integer \(m\), and none is unimodular.

**Geometric consequence.** The connected generalized Jacobian \(J_D=\operatorname{Pic}^{0}_{D/k}\) is a six-dimensional \(k\)-torus with geometric character lattice \(H\). Let \(T_B\) be the \(k\)-torus obtained from \(B\) using the same Galois action through \(S_5\). The primitive map, unique up to sign, descends to a degree-two isogeny
\[
1\longrightarrow\mu_2\longrightarrow J_D\longrightarrow T_B\longrightarrow1.
\]
Its order-two kernel is independent of the sign choice; in characteristic two it is **nonreduced**. This is an equivariant integral distinction, not a claim that each individual twist is nonisomorphic as an abstract torus (the split twists, for example, are isomorphic).

## Assumptions and scope
The degree-five del Pezzo surface is smooth and geometrically integral over the finite field \(k\). The divisor is **all ten geometric exceptional curves as a reduced \(k\)-divisor**, not a selected pentagon, and all intersections are geometric ordinary nodes. Over an algebraic closure its ten components are projective lines with fifteen nodes; equivalently the graph has ten vertices and fifteen edges. The Galois action on the ten components factors through \(S_5\), whether or not the individual curves are defined over \(k\). The lattice assertion itself is characteristic-free and concerns the full abstract \(S_5\)-action, not merely one cyclic Frobenius subgroup.

## Proof
**1. The character lattice.** The normalization \(\widetilde D\) consists geometrically of ten copies of \(\mathbb P^1\), whose connected Picard varieties vanish. For an ordinary nodal curve the normalization gluing exact sequence presents \(\operatorname{Pic}^0(D)\) as the quotient of one \(\mathbb G_m\) factor per node by the component-rescaling torus. Taking geometric characters gives
\[
X^*(J_D\otimes_k\bar k)=\ker\bigl(\partial:\mathbb Z^{E(P)}\to\mathbb Z^{V(P)}\bigr)=H_1(P,\mathbb Z).
\]
The boundary matrix has rank nine because \(P\) is connected; the rank of \(H\) is \(15-10+1=6\). All these constructions commute with graph automorphisms and hence Galois descent.

**2. Integral bases and the map.** Label graph vertices by the lexicographically ordered two-element subsets of \(\{0,1,2,3,4\}\), and join two vertices exactly when the subsets are disjoint. Orient each of its fifteen edges from the smaller to the larger vertex index and order the edges lexicographically. Let \(N\) be the six-column integer cycle basis obtained by taking the standard free-chord basis of the nullspace of the resulting \(10\times15\) signed incidence matrix, with free coordinates ordered as in the executable verifier. For \(A_4\), use \(e_i-e_4\) (\(0\le i\le3\)); for \(B\), use their six lexicographically ordered exterior products. In these specified bases put
\[
U=\begin{pmatrix}
 1&0&0&0&-1&0\\
 0&0&0&-1&0&1\\
 0&0&0&1&1&0\\
 -1&-1&0&0&0&0\\
 -1&0&-1&0&0&0\\
 0&1&1&0&0&0
\end{pmatrix}.
\]
The map \(\iota\) is represented by \(U:B\to H\). In the verifier, \(N\) is computed directly as the integer nullspace basis of the incidence matrix; no geometric choices beyond the stated labels and orientations enter.

For a permutation \(g\in S_5\), let \(A(g)\) denote the signed permutation of graph edges restricted to the cycle lattice, and \(C(g)\) the \(4\times4\) integral standard-root action. Set \(W(g)=\bigwedge^2 C(g)\). The finite exact identities
\[
A(g)U=UW(g)\qquad (g\in S_5)
\]
are checked for all 120 permutations by the standalone verifier. This exhaustive calculation is a proof of equivariance for the finite group, not an extrapolation from sample permutations.

**3. Index and uniqueness.** Integer determinant and Smith-form calculations give
\[
\det U=-2,\qquad\operatorname{SNF}(U)=\operatorname{diag}(1,1,1,1,1,2).
\]
In particular \(U\) is injective, its cokernel is cyclic of order two, and it is primitive (it has entries equal to one). To establish uniqueness, impose \(A(g)Z=ZW(g)\) for \(g=(0\,1)\) and \(g=(0\,1\,2\,3\,4)\); these two permutations generate \(S_5\). With 36 unknown entries in \(Z\), the resulting \(72\times36\) integer coefficient matrix has rank **35 modulo 101**, by full exact Gaussian elimination. Consequently its rational rank is at least 35. The exhibited nonzero solution \(U\) makes the rational rank at most 35. The rational space of intertwiners is therefore exactly \(\mathbb Q U\). As \(U_{11}=1\), every intertwiner with integer entries must be an integer multiple \(mU\), proving the displayed \(\mathbb Z[S_5]\)-Hom identity and the absence of an equivariant integral isomorphism. For \(m\ne0\), \(|\det(mU)|=2|m|^6\).

**4. Descent and isogeny.** Since \(U\) is \(S_5\)-equivariant, restricting its action to the Galois image yields an injection of character lattices \(X^*(T_B)=B\hookrightarrow X^*(J_D)=H\), with quotient the trivial Galois module \(\mathbb Z/2\). Contravariant equivalence between algebraic tori and Galois lattices gives the claimed exact sequence with kernel the diagonalizable group scheme \(D(\mathbb Z/2)=\mu_2\). This group scheme has length two in every characteristic and is not étale in characteristic two. Replacing \(U\) by \(-U\) composes the isogeny with inversion on a torus; the kernel remains unchanged.

## Verification
Execute `python verification/verify_petersen_lattice.py` with Python 3.9 or later and SymPy. The program constructs the graph, incidence and cycle basis; checks equivariance for every permutation of five labels; computes the determinant and Smith invariants; and performs the \(72\times36\) elimination over \(\mathbb F_{101}\). Its packaged output ends with `ALL_CHECKS_PASSED`. The proof is not based on bounded finite-field point enumerations. The exhaustive finite group check and finite integer-matrix certificates are sufficient for the nonstandard integral-lattice part of the theorem.

## Relationship to prior work
Roulleau (arXiv:1001.5111; first made public January 28, 2010) discusses the degree-five del Pezzo surface and its ten exceptional curves. González-Sánchez, Harrison, Polo-Blanco, and Schicho (arXiv:1009.4044) classify degree-five del Pezzo twists using their \(S_5\)-line configurations. Dolgachev, Farb, and Looijenga (2018) explicitly identify the full ten-line Wiman–Edge boundary as the Petersen graph with its \(S_5\)-action; Farb and Looijenga (2019/2020) develop its degeneration geometry. The general normalization and graph description of nodal Picard varieties is classical, with related modern compactified-Jacobian treatment by Casalaina-Martin, Kass, and Viviani (arXiv:1107.4166).

These known results account for the graph, its symmetry, and the torus description via nodal gluing. The statement assessed here concerns an additional **integral** comparison: the primitive index-two embedding of \(\bigwedge^2 A_4\) in the graph-cycle lattice, the uniqueness of this equivariant embedding, and the resulting \(\mu_2\)-isogeny. Complex/rational representation equivalence alone does not determine an integral index or a characteristic-two kernel. The comparison does not claim the Petersen graph itself, its six-dimensional rational character, or any point-count formula as new.

## Limitations
This is an exact structural statement for one natural boundary on all smooth degree-five del Pezzo surfaces, not a classification of Jacobians for other divisors, nor a claim of a novel point-count table. A primitive equivariant index-two map does not prohibit an abstract isomorphism between the two split tori. Specialist historical sources may contain an equivalent integral lattice calculation; publication priority requires external review. No independent mathematical audit has been performed.

## References
1. X. Roulleau, *The Fano surface of the Fermat cubic threefold, the del Pezzo surface of degree 5 and a ball quotient*, arXiv:1001.5111, first posted 2010-01-28. https://arxiv.org/abs/1001.5111
2. J. González-Sánchez, M. Harrison, I. Polo-Blanco, J. Schicho, *Algorithms for Del Pezzo Surfaces of Degree 5*, arXiv:1009.4044, first posted 2010-09-21. https://arxiv.org/abs/1009.4044
3. I. Dolgachev, B. Farb, E. Looijenga, *Geometry of the Wiman–Edge pencil, I*, European J. Math. 4 (2018), 879–930, DOI 10.1007/s40879-018-0231-3. https://link.springer.com/article/10.1007/s40879-018-0231-3
4. B. Farb, E. Looijenga, *Geometry of the Wiman–Edge pencil and the Wiman curve*, arXiv:1912.12280, first posted 2019-12-27. https://arxiv.org/abs/1912.12280
5. S. Casalaina-Martin, J. L. Kass, F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166, first posted 2011-07-21. https://arxiv.org/abs/1107.4166
6. Q. Ren, K. Shaw, B. Sturmfels, *Tropicalization of Del Pezzo Surfaces*, arXiv:1402.5651, first posted 2014-02-23. https://arxiv.org/abs/1402.5651
