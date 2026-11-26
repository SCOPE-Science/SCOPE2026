# Integral Picard-torus descent at the characteristic-two Fermat cubic boundary

## Finding
Let \(k=\mathbb F_q\), \(q=2^m\) with \(m\ge1\). Consider the smooth cubic surface
\[
S:\quad X_0^3+X_1^3+X_2^3+X_3^3=0\subset\mathbb P^3_k,
\]
and let \(D\subset S\) be the *reduced* union of all \(27\) geometric lines. Write \(J=\operatorname{Pic}^0_{D/k}\) and let \(T\) be its maximal torus quotient. Then \(D\) is geometrically connected, has \(45\) ordinary triple points and no other singularities, and has arithmetic genus \(109\). The smooth connected affine algebraic group \(J\) has \(45\)-dimensional vector-group unipotent radical \(U\cong\mathbb G_a^{45}\), no abelian quotient, and rank-\(64\) torus quotient. **Integrally**, not merely up to isogeny,
\[
T\cong\begin{cases}
\mathbb G_m^{64},&m\text{ even},\\
(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m)^{32},&m\text{ odd}.
\end{cases}
\]
Consequently, with \(C_n\) denoting a cyclic group of order \(n\), there are abstract finite-abelian-group isomorphisms
\[
J(k)\cong\begin{cases}
(k,+)^{45}\times C_{q-1}^{64},&m\text{ even},\\
(k,+)^{45}\times C_{q^2-1}^{32},&m\text{ odd}.
\end{cases}
\]
The new arithmetic assertion is the integral structure of Frobenius on the \(64\)-dimensional torus lattice, together with its precise contrast to the rank-\(91\) line-divisor torus in odd characteristics. The \(27\) lines, \(45\) Eckardt points and rational Frobenius eigenmultiplicities were known and are not claimed as discoveries.

## Assumptions and scope
All finite fields in this statement have characteristic two; \(D\) is the reduced union of *all* geometric contained lines, with its canonical descent to \(k\). The divisor is not a smooth curve, and \(\operatorname{Pic}^0(D)\) is not the Picard group of the ambient cubic surface nor that of its open complement. For odd \(m\), the notation \(\operatorname{Res}_{\mathbb F_{q^2}/k}\mathbb G_m\) means the two-dimensional induced torus, whose character lattice is the integral permutation module \(\mathbb Z[C_2]\). A rational Frobenius character does not determine this integral lattice.

## Proof
**The singular curve and its normalization.** Let \(\omega\in\mathbb F_4\) satisfy \(\omega^2+\omega+1=0\). For each of the three unordered coordinate-pair partitions and every \((a,b)\in\{1,\omega,\omega^2\}^2\), impose equations \(X_j=aX_i\), \(X_l=bX_h\) on the two ordered pairs. Each defines a contained line, since \(a^3=b^3=1\), and the \(27\) lines are distinct. A smooth cubic surface has exactly \(27\) geometric lines, so this is the complete list. All are defined over \(\mathbb F_4\). Any intersection between two distinct such lines is \(\mathbb F_4\)-rational (intersection of \(\mathbb F_4\)-linear subspaces). The projective \(\mathbb F_4\)-point census given in the standalone verifier proves, by exhaustive exact field arithmetic, that their union consists of exactly \(45\) points, and precisely three distinct lines pass through each one. At every point the three line directions are distinct tangent directions on the *smooth* surface; thus the singularities of the reduced curve are ordinary planar triple crossings. No other geometric singularity is possible. The local delta invariant is \(3\) for each, and normalization is \(27\) disjoint copies of \(\mathbb P^1\). Since the incidence graph is connected,
\[
p_a(D)=45\binom32-27+1=109.
\]
This also agrees with adjunction: \(D\sim9H\) on the cubic with \(K_S=-H\), \(H^2=3\).

**The connected Picard group.** The normalization exact sequence for unit sheaves on a reduced connected curve with ordinary multiple points yields a connected linear Picard group (all normalized components are rational). Define the bipartite graph \(\Gamma\) with \(27\) component vertices, \(45\) singular-point vertices and one edge for each local normalization branch. Each triple point has three branches, so \(\Gamma\) is connected with \(72\) vertices and \(135\) edges; hence
\[
H_1(\Gamma,\mathbb Z)\cong\mathbb Z^{135-72+1}=\mathbb Z^{64}.
\]
The integral character lattice of the torus quotient \(T\) is this graph cycle lattice, or its integral dual under the opposite conventional normalization; the resulting involution types are the same because each occurring indecomposable is self-dual. At a planar ordinary triple the normalization-unit quotient has torus rank \(3-1=2\), and its remaining \(\delta-(3-1)=1\) dimension is a vector group. To see the group law explicitly even in characteristic two, compare linear jets on its three smooth branches: after fixing common constant terms, the one-dimensional failure of linear-jet compatibility is additive, since products of \(1+at\) and \(1+bt\) agree with \(1+(a+b)t\) modulo \(t^2\). At the \(45\) triple points these line-jet defects descend as a rank-\(45\) vector space over \(k\). Hence \(U\cong\mathbb G_a^{45}\) and the torus quotient has dimension \(64\).

**Integral Frobenius action.** If \(m\) is even, \(\omega\in k\), all vertices and branches of \(\Gamma\) are rational, and Frobenius acts trivially. This gives \(T\cong\mathbb G_m^{64}\). If \(m\) is odd, Frobenius acts by \(\omega\mapsto\omega^2\), an involution of the graph. The exact enumerated permutation fixes \(3\) of the \(27\) line vertices, \(7\) of the \(45\) triple-point vertices, and \(9\) of the \(135\) oriented component-to-point edges. The alternating trace formula for the graph chain complex gives
\[
\operatorname{tr}(F\mid H_1(\Gamma,\mathbb Q))=9-(3+7)+1=0.
\]
But this rational trace alone would allow nonisomorphic integral tori. For an integral involution lattice, the three indecomposable summands are \(\mathbb Z_+\), \(\mathbb Z_-\), and \(\mathbb Z[C_2]\). Write their multiplicities as \(a,b,c\). Reduction modulo two shows \(c=\operatorname{rank}_{\mathbb F_2}(F-I)\), because each regular summand contributes rank one and the two rank-one summands contribute zero. The exact certificate constructs *two different integral fundamental-cycle bases*, acts on each chord basis by the edge permutation, and obtains \(\operatorname{rank}_{\mathbb F_2}(F-I)=32\) in both, with trace zero. Therefore
\[
a+b+2c=64,\quad a-b=0,\quad c=32,
\]
so \(a=b=0\). Thus \(H_1(\Gamma,\mathbb Z)\cong\mathbb Z[C_2]^{32}\), and the asserted **integral** induced torus isomorphism follows.

**Rational-point groups.** For every finite field, Lang's theorem gives \(H^1(k,U)=0\), so the sequence \(U(k)\to J(k)\to T(k)\) is surjective with kernel \(U(k)\). It is a sequence of finite abelian groups. The group \(U(k)\cong(k,+)^{45}\) has 2-power order and exponent two; the group \(T(k)\) has odd order, since it is a product of groups \(k^\times\) or \(\mathbb F_{q^2}^\times\). Primary decomposition of finite abelian groups splits the sequence abstractly. These two multiplicative groups are cyclic, giving the stated isomorphisms. No canonical splitting of the algebraic-group extension is asserted.

## Verification
Run `python3 verify_char2_fermat_picard.py` from this package using Python 3 with the standard library. It computes in the four-element field \(\mathbb F_2[t]/(t^2+t+1)\); enumerates all projective points and all \(27\) line point sets; proves their singular-incidence multiplicity profile \(3^{45}\) and completeness of all line intersections; constructs the entire 72-vertex/135-branch normalization graph and the full Frobenius permutation; and independently builds two spanning-tree fundamental-cycle bases of rank \(64\). For each, integral cycle-coordinate action is reduced modulo two and has \(F-I\) rank \(32\), with trace zero. The recorded exact success marker is `CHAR2_FERMAT_CUBIC_INTEGRAL_PICARD_TORUS_OK`. The symbolic normalization and involution-lattice arguments turn these exhaustive finite incidence checks into the stated all-extension theorem; no finite-field sample alone is used to infer an infinite assertion.

## Relationship to prior work
The classical cubic-surface 27-line equations, and their appearance in the family of Fermat surfaces, are described by Schütt, Shioda and van Luijk (arXiv:0812.2377, first posted 2008-12-12). The characteristic-two Hermitian surface's complete 45-point triple incidence is established in the literature; in particular Dolgachev–Duncan (arXiv:1712.01167, 2017) treats its automorphisms and the full exceptional-line configuration. A published analysis titled *The factorial complement of all 27 lines on the binary Fermat cubic* computes exactly the same boundary's geometry and the rational eigenvalues \(+1\) and \(-1\), each of multiplicity \(32\), on its graph cohomology. It does **not** classify the associated graph cycle lattice integrally or the complete Picard-torus isomorphism type. An earlier calculation of \(\operatorname{Pic}^0\) for prime-degree Fermat line divisors assumes odd prime degree at least five and characteristic exceeding that degree, and therefore does not cover this characteristic-two cubic special fiber. Similarly, the rank-\(217\) arithmetic Picard-torus calculation for the Fermat quartic concerns a different degree, different singularities and different Frobenius action. This distinction is between an integral group structure and a rational character, not between titles or notations.

## Limitations
The exact torus isomorphism concerns the reduced 27-line divisor on this cubic in characteristic two only, not the Picard group of the surface or arbitrary cubic surfaces. The known ordinary triple-point and rational Frobenius eigenvalue counts are inputs rather than independent novelty claims. Historic priority of the stronger integral lattice calculation has not been externally certified: unindexed finite-geometry and generalized-Jacobian literature could contain equivalent group decompositions. The proof and certificate establish arithmetic groups without asserting a canonical algebraic splitting of the additive-by-torus extension. The \(2017\) reference is background only; the selected archive source was already public in \(2008\).

## References
- M. Schütt, T. Shioda, and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377v1 (2008-12-12), https://arxiv.org/abs/0812.2377.
- M. Homma and S. J. Kim, *Numbers of points of surfaces in the projective 3-space over finite fields*, arXiv:1409.5842v1 (2014-09-20), https://arxiv.org/abs/1409.5842.
- I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167v1 (2017-12-04), https://arxiv.org/abs/1712.01167 (later context, not an archival anchor).
- *The factorial complement of all 27 lines on the binary Fermat cubic* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-factorial-complement-of-all-27-lines-on-the-binary-fermat-cu--3fc752675013.
- *Degree-one generation of the rational cohomology of the 27-line complement on the Fermat cubic* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-degree-one-generation-of-the-rational-cohomology-of-the-27-line--861ceab139a4.
