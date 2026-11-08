# Explicit automorphism-orbit bundles for smooth toric varieties of Picard number two

## Finding

Let \(s,r\ge 1\) and take integers \(0=b_0<b_1<\cdots<b_t\) and positive integers \(m_0,\ldots,m_t\) with \(\sum_{j=0}^t m_j=r+1\). Put
\[
B=\mathbb P^s_{\mathbb C},\qquad E=\bigoplus_{j=0}^t\mathcal O_B(b_j)^{\oplus m_j},\qquad X=\mathbb P_B(E),
\]
where \(\mathbb P(E)\) parametrizes **lines in** the fibres of \(E\). Define \(F_j=\bigoplus_{h\ge j}\mathcal O_B(b_h)^{\oplus m_h}\), with \(F_{t+1}=0\). Then the **entire orbit decomposition under the full algebraic automorphism group** is
\[
X=\bigsqcup_{j=0}^{t}U_j,\qquad U_j=\mathbb P(F_j)\setminus\mathbb P(F_{j+1}).
\]
More precisely, each \(U_j\) is canonically a vector-bundle total space over \(B\times\mathbb P^{m_j-1}\):
\[
U_j\cong\operatorname{Tot}\!\left(\bigoplus_{h>j}\left[\mathcal O_B(b_h-b_j)\boxtimes\mathcal O_{\mathbb P^{m_j-1}}(1)\right]^{\oplus m_h}\right).
\]
Its closure is \(\mathbb P(F_j)\) and has codimension \(c_j=\sum_{h<j}m_h\) in \(X\). If \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring of complex varieties, then
\[
[U_j]=[\mathbb P^s][\mathbb P^{m_j-1}]\mathbb L^{\sum_{h>j}m_h}.
\]
For \(t>0\), \(\operatorname{codim}_X(X\setminus U_0)=m_0\). Consequently the exact maximal codimension of homogeneity is dictated by the multiplicity of the least twist: for every integer \(k\ge1\), the complement to the open full automorphism orbit has codimension at least \(k+1\) if and only if \(m_0\ge k+1\). When \(t=0\), \(X\cong\mathbb P^s\times\mathbb P^r\) is homogeneous.

## Assumptions and scope

The base field is \(\mathbb C\). Every \(s,r\ge1\) and every nondecreasing integral splitting tuple are included after twisting all summands by the inverse of the smallest degree, so the minimum is zero. Distinct twist levels and their multiplicities, not the numerical gaps between degrees, determine the **orbit count and codimensions**. The gap sizes do affect the isomorphism classes of the vector bundles constituting the orbits. The input variety is projectivization of a split bundle over projective space, equivalently a smooth complete toric variety of Picard number two by Kleinschmidt's classification. No statement is made for singular toric varieties or higher Picard number.

## Proof

**1. Transitivity on each proposed stratum.** At a fixed point of \(B\), the evaluation of bundle automorphisms of \(E\) contains the full block upper-degree parabolic: a map from \(\mathcal O(b_i)\) to \(\mathcal O(b_h)\) exists only for \(b_h\ge b_i\), and for \(b_h\ge b_i\) its entries are evaluated global sections of \(\mathcal O(b_h-b_i)\). The evaluation map is surjective at each base point, including for degree zero. The invertible diagonal blocks and arbitrary degree-increasing off-diagonal blocks act transitively on the set of lines whose least nonzero twist component lies in level \(b_j\): first make that component a fixed basis vector, then remove all higher-degree components. Projective transformations of \(B\) lift, up to the harmless scalar choices in the standard linearizations of \(\mathcal O_B(b_j)\), and act transitively on \(B\). Thus each \(U_j\) is contained in a single orbit and indeed is an orbit of a subgroup of \(\operatorname{Aut}(X)\).

**2. No full automorphism can merge distinct strata.** If \(t=0\), there is one stratum. Assume \(t>0\), so \(b_t>0\). Let \(H\) be the pullback of the hyperplane class of \(B\) and \(\xi\) the relative hyperplane class for lines. Both \(H\) and \(D=\xi+b_t H\) are nef and globally generated. They generate the two extremal rays of the nef cone: on a line in a fibre of \(X\to B\), \(H\) has degree zero, and on a line lying in \(\mathbb P(\mathcal O_B(b_t))\cong B\), \(D\) has degree zero; moreover \(\operatorname{Pic}(X)\cong\mathbb Z^2\). The map associated with \(H\) is the fibration \(\pi:X\to B\), with positive-dimensional general fibre. The morphism associated with \(D\) is generically injective: on the dense locus where a degree-zero coordinate of the line is nonzero, the collection of sections associated with that coordinate includes all degree-\(b_t\) homogeneous forms in the base variables. Their ratios recover the base point via the Veronese embedding; then the remaining fibre coordinates are recovered from the globally generated summands. In particular the \(D\)-morphism is generically finite, whereas \(\pi\) is of fibre type. The dimensions of the generic fibres distinguish the two nef-ray contractions intrinsically. Thus every automorphism of \(X\) preserves \(\pi\) up to an automorphism of \(B\).

A projective-bundle automorphism over a base automorphism \(g\) gives \(E\simeq g^*E\otimes L\) for some line bundle \(L\) on \(B\). Since \(g^*\mathcal O_B(1)\simeq\mathcal O_B(1)\), comparison of splitting degrees yields \(L\simeq\mathcal O_B\): a finite nonempty multiset of integers cannot equal a nonzero translate of itself. All such bundle isomorphisms preserve the canonical filtration by summands of degree at least \(b_j\), since \(H^0(B,\mathcal O_B(b_i-b_h))=0\) when \(b_i<b_h\). Therefore every \(\mathbb P(F_j)\), and hence every difference \(U_j\), is invariant under the full automorphism group. Step 1 proves the asserted orbits are exactly the \(U_j\).

**3. Geometry and codimensions.** Projection of a line with least nonzero component in \(\mathcal O_B(b_j)^{\oplus m_j}\) onto that component defines a map \(U_j\to B\times\mathbb P^{m_j-1}\). If \(\ell\) is the tautological line in the degree-\(b_j\) block, higher-degree components of the original line are exactly homomorphisms from \(\ell\) into the sum of higher-degree blocks. Since \(\ell=\mathcal O_B(b_j)\boxtimes\mathcal O_{\mathbb P^{m_j-1}}(-1)\), this is the displayed vector bundle. The closure is \(\mathbb P(F_j)\), because its complement in that projective bundle is a proper projective subbundle. The codimension is the difference between \(r+1\) and \(\operatorname{rank}F_j\), which is \(\sum_{h<j}m_h\). The motivic formula is the standard multiplicative formula for vector bundles. The open boundary is \(\mathbb P(F_1)\), giving codimension \(m_0\) when \(t>0\).

## Verification

The accompanying standalone script `toric_orbit_check.py` independently enumerates fibre projective points over the prime fields of orders \(2,3,5\), with all sorted splitting tuples of length two through five and entries between zero and three. It checks the exact number of points at every lowest-active-degree level against the predicted product of projective-space and affine-space counts. It verifies 207 parameter/field combinations. This finite census corroborates only the fibre-stratum combinatorics; it is **not** a proof of the all-dimensional algebraic automorphism assertion, which is supplied above.

The cases \(s=1,r=1\) reproduce the two orbits on nontrivial Hirzebruch surfaces. The case \(s=1,r=2,m_0=2,m_1=1\) reproduces the two orbits (open complement and a curve) in the threefold example of Arzhantsev–Shakhmatov. When all twists agree, the statement reduces to homogeneity of a product of projective spaces.

## Relationship to prior work

The standard classification of smooth complete toric varieties of Picard number two as split projective bundles is due to Kleinschmidt. Bazhov's 2011 preprint (published 2013) gives a general criterion for equivalence of torus orbits under the full automorphism group of **any** complete toric variety, in terms of monoids of divisor classes. Thus the abstract group-orbit problem is previously solved; the present contribution is the **explicit all-dimensional vector-bundle geometry, exact strata, motivic classes and multiplicity-only codimension formula for this natural Picard-two family**, which require specializations and further geometric arguments not stated there. In 2026 Arzhantsev and Shakhmatov classified complete toric varieties homogeneous in codimension one in dimensions at most three and explicitly asked for the smooth complete classification in arbitrary dimension. Their example of \(\mathbb P_{\mathbb P^1}(\mathcal O^{\oplus2}\oplus\mathcal O(b))\) is recovered. The result here answers the Picard-number-two portion of that question, not the general open problem.

## Limitations

This is a natural subclass classification, not a solution of the unrestricted higher-Picard-number problem. Generic orbit data were already accessible algorithmically from Bazhov's theorem; no priority is claimed for the algorithm, the Kleinschmidt family, or any low-dimensional known examples. Whether the explicit vector-bundle form has appeared elsewhere is an outstanding historical-priority risk. The finite-field checker does not independently establish the full automorphism theorem.

## References

1. I. Arzhantsev and K. Shakhmatov, *Automorphisms of toric varieties and Gale duality*, arXiv:2609.09051 (first version 8 September 2026), especially Problem 1 and Example 2.
2. I. Bazhov, *On orbits of the automorphism group on a complete toric variety*, arXiv:1110.4275 (first version 19 October 2011), especially Theorems 1, 3.6 and 3.7.
3. P. Kleinschmidt, *A classification of toric varieties with few generators*, Aequationes Math. 35 (1988), 254–266.
