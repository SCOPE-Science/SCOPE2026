# Arithmetic classification of derivations of odd dihedral quandle algebras

## Finding
Let \(n\ge3\) be odd, let \(K\) be any field whose characteristic does not divide \(n\), and let \(A_n(K)\) have basis \(\{e_i:i\in\mathbb Z/n\mathbb Z\}\) and bilinear product \(e_i e_j=e_{2j-i}\). Every derivation of \(A_n(K)\) is **translation invariant** and the derivation Lie algebra is abelian. More precisely, all derivations, with no repetitions, are
\[
D_c(e_i)=\sum_{u\in\mathbb Z/n\mathbb Z}c_u e_{i+u},\qquad
c_u=c_{-u}+c_{u/2}.
\]
The subscript \(u/2\) means multiplication by the inverse of \(2\) modulo \(n\); the displayed recurrence automatically forces \(c_0=0\).

In characteristic zero or two the derivation algebra is zero. In odd characteristic \(p\) not dividing \(n\), its dimension is completely arithmetic. For each divisor \(m>1\) of \(n\), define
\[
d_m=\operatorname{ord}_m(2),\qquad H_m=\langle2,-1\rangle\le(\mathbb Z/m\mathbb Z)^\times.
\]
Define the positive integer
\[
\Delta_m=\begin{cases}
2^{d_m/2}+1,&-1\in\langle2\rangle\pmod m,\\
2^{d_m}-1,&-1\notin\langle2\rangle\pmod m.
\end{cases}
\]
The first case necessarily has even \(d_m\). Then
\[
\boxed{\dim_K\operatorname{Der}(A_n(K))=
\sum_{\substack{m\mid n\\m>1}}\frac{\varphi(m)}{|H_m|}\,\mathbf1_{\{p\mid\Delta_m\}}.}
\]
In particular, for \(n=11\) over a field of characteristic \(3\), and for \(n=13\) over a field of characteristic \(5\), the derivation Lie algebra is one-dimensional, even though the coefficient characteristic does not divide the quandle order.

## Assumptions and scope
A derivation means a \(K\)-linear map \(D:A_n(K)\to A_n(K)\) satisfying \(D(xy)=D(x)y+xD(y)\) for all \(x,y\). The algebra is generally neither associative nor unital. The field may be infinite or finite. The hypotheses are that \(n\) is odd and \(\operatorname{char}K\nmid n\); no assertion is made for even \(n\) or for the excluded modular characteristic.

## Proof
**1. Translation-weight rigidity.** For \(a\in\mathbb Z/n\mathbb Z\), the translation \(T_a(e_i)=e_{i+a}\) is an algebra automorphism, since \(2(j+a)-(i+a)=2j-i+a\). Hence conjugation by \(T_1\) preserves the vector space of derivations. Extend scalars to a splitting field \(L\) containing all \(n\)-th roots of unity. Since \(\operatorname{char}K\nmid n\), the finite-order conjugation operator is diagonalizable over \(L\). It suffices to analyze its eigencomponents.

Let \(\zeta\) be a primitive \(n\)-th root in \(L\). A component of translation weight \(t\in\mathbb Z/n\mathbb Z\) has the form
\[
D_t(e_i)=\zeta^{ti}\sum_u c_u e_{i+u}.
\]
For each \(i,j,u\), comparing the coefficient of \(e_{2j-i+u}\) in the Leibniz identity gives
\[
\zeta^{2t(j-i)}c_u=c_{-u}+\zeta^{t(j-i)}c_{u/2}.
\]
For fixed \(u\), the quadratic polynomial \(c_uZ^2-c_{u/2}Z-c_{-u}\) therefore vanishes on all powers of \(\zeta^t\). If \(t\ne0\), this root of unity has order at least three, since \(n\) is odd. A polynomial of degree at most two cannot have three distinct roots unless it vanishes identically. Hence every \(c_u\) vanishes, and the entire weight component is zero. All derivations therefore have only weight zero: they commute with \(T_1\), so their matrix entries are constant along cyclic diagonals. Descent back to \(K\) gives the asserted circulant form.

**2. Coefficient condition.** For a circulant map, the same coefficient identity with \(t=0\) is exactly \(c_u=c_{-u}+c_{u/2}\), independent of \(i,j\). It is therefore both necessary and sufficient for the Leibniz identity on every basis pair, and hence on all elements by bilinearity. Setting \(u=0\) gives \(c_0=0\). Applying the recurrence at \(u\) and at \(-u\) and adding yields \(c_v+c_{-v}=0\) for every \(v\), since multiplication by two permutes the indices. Thus
\[
c_{-u}=-c_u,\qquad c_{u/2}=2c_u.
\]
If \(\operatorname{char}K=2\), these equalities combined with the original recurrence give \(c_{u/2}=0\) for all \(u\), and the derivation is zero. Otherwise they are equivalent to \(c_{-u}=-c_u\) and \(c_{2u}=c_u/2\), together with \(c_0=0\).

**3. Orbit arithmetic.** Fix a nonzero \(u\) of additive order \(m\mid n\). Its coefficient is determined along the doubling orbit by
\[
c_{2^j u}=2^{-j}c_u,\qquad c_{-2^j u}=-2^{-j}c_u.
\]
If \(-1\notin\langle2\rangle\pmod m\), the signed orbit has size \(2d_m\), and the only consistency condition on a nonzero parameter is \(2^{d_m}=1\) in \(K\), equivalently \(p\mid2^{d_m}-1\). If \(-1\in\langle2\rangle\pmod m\), then \(2^{d_m/2}\equiv-1\pmod m\), the signed orbit has size \(d_m\), and consistency is \(2^{d_m/2}=-1\) in \(K\), equivalently \(p\mid2^{d_m/2}+1\). This also enforces the full doubling-cycle relation. In characteristic zero, neither positive integer condition can hold, so all coefficients vanish.

Exactly \(\varphi(m)\) indices have additive order \(m\). Multiplication by the subgroup \(H_m\) acts freely on them: if \(h u=u\), then \(h\equiv1\pmod m\). There are therefore \(\varphi(m)/|H_m|\) signed orbits. Each contributes one freely chosen coefficient precisely when the stated congruence holds, and contributes none otherwise. The coefficients constructed on distinct orbits have disjoint supports and are independent. Summing over divisors proves the dimension formula and supplies an explicit basis. Finally, any two circulant matrices commute, so the derivation Lie algebra is abelian.

**4. Boundary examples.** For \(m=11\), the doubling order is \(10\), \(2^5\equiv-1\pmod{11}\), and \(\Delta_{11}=33\). Hence characteristic \(3\) gives exactly one derivation on \(A_{11}\). For \(m=13\), doubling has order \(12\) with \(2^6\equiv-1\pmod{13}\), giving \(\Delta_{13}=65\) and dimension one in characteristic \(5\). These characteristics are coprime to the respective quandle orders.

## Verification
Run `python checker.py` with Python 3 and NumPy. The checker independently builds all \(n^3\) Leibniz linear equations in \(n^2\) unconstrained matrix entries and computes their rank over finite prime fields, without assuming circulant form. It compares the resulting dimensions to the orbit formula for thirty coprime pairs with \(n\in\{3,5,7,9,11,13\}\), and directly checks the Leibniz equations for every constructed orbit-basis derivation. Further direct tests include the cross-characteristic cases \((n,p)=(11,3),(13,5),(23,89)\) and the vanishing case \((15,7)\). The recorded output is `VERIFY_OK rank_cases=30 orbit_examples=4`. The proof above, not the finite tests, establishes the theorem for arbitrary admissible \(n\) and fields.

## Relationship to prior work
Elhamdadi–Makhlouf–Silvestrov–Zappala (2021, Theorem 3.9) classify derivations of dihedral quandle algebras in **characteristic zero**; their Section 4.2 gives positive-characteristic matrices for orders three through six. This paper's zero-derivation conclusion for odd orders is therefore not new. Sangare–Ta (2026, primary MSC 17D99) investigate idempotents, algebra automorphism groups and commutator widths of the same dihedral-quandle algebra family; their Proposition 4.6 classifies automorphisms of the **integral** odd-dihedral quandle algebra, not derivations over fields. Bardakov–Elhamdadi (2026) revisit quandle-ring algebraic properties and explicitly reference the characteristic-zero derivation theory. Elhamdadi–Ta–Virgin (2026) introduce Fourier methods for quandle algebras, particularly odd dihedral/Takasaki quandles, in their idempotent work. The present finding uses translation-weight decomposition to classify **all derivations in arbitrary cross-characteristic**, including nonzero examples not covered by the earlier characteristic-zero theorem or low-order tables. It does not claim a new characterization of derivations for all quandles.

## Limitations
The odd-order and coefficient-characteristic-coprime hypotheses are essential to this proof, which uses separability of the cyclic translation action. No result for even order or for characteristic dividing \(n\) is inferred. The recent Fourier paper's full text was unavailable during comparison; only its publicly available abstract and bibliographic record were inspected. A hidden equivalent observation or a more general historical theorem remains a priority risk. Computations in the verification script establish only finite cases.

## References
1. M. Elhamdadi, A. Makhlouf, S. Silvestrov, E. Zappala, *The derivation problem for quandle algebras*, arXiv:2106.08289v1 (2021), Theorem 3.9 and Section 4.2. https://arxiv.org/abs/2106.08289
2. V. Bardakov, M. Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057v1 (2026). https://arxiv.org/abs/2601.07057
3. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026). https://arxiv.org/abs/2609.03799

4. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1 (first submitted 2026-08-03), primary MSC2020 17D99. https://arxiv.org/abs/2608.01550
