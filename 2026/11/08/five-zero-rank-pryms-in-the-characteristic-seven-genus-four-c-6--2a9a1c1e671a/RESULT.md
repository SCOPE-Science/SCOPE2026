# Five zero-rank Pryms in the characteristic-seven genus-four \(C_6\) family

## Finding
Let \(k=\overline{\mathbb F}_7\). For \((a,b)\in k^2\), put
\[
F_{a,b}(x)=x^{10}+x^7+a x^4+b x,\quad
\Delta=a^2+3a^3+3b+b^2+4ab,
\]
\[
u=a^3+6ab+3b^2,\qquad v=3a^2+3a+6b,\qquad
R(a)=2a^3+(a+1)^5.
\]
Assume \(b\Delta\ne0\). Then \(H_{a,b}:y^2=F_{a,b}(x)\) is a smooth genus-four hyperelliptic curve with an order-three automorphism, genus-one quotient \(E_{a,b}\), and three-dimensional Prym \(P_{a,b}\).

The geometric Jacobian \(7\)-rank \(f_7\) and Cartier \(a\)-number are exactly

| Parameter condition (always \(b\Delta\ne0\)) | \(f_7(J(H_{a,b}))\) | \(a(J(H_{a,b}))\) | \(f_7(P_{a,b})\) |
| --- | ---: | ---: | ---: |
| \(uv\ne0\) | 4 | 0 | 3 |
| \(u=0\), \(v\ne0\) | 3 | 1 | 3 |
| \(v=0\), \(R(a)\ne0\) | 2 | 2 | 1 |
| \(v=0\), \(R(a)=0\) | 1 | 2 | 0 |

All four rows occur over \(\mathbb F_7\), respectively at \((a,b)=(1,1),(3,4),(1,6),(2,4)\).

On the smooth parameter surface, \(v=0\) is the reduced graph \(b=3a(a+1)\), with \(a\notin\{0,-1,-2\}\). Exactly **five distinct geometric coefficient pairs** on that graph have zero-rank Prym; they are the roots of the separable quintic
\[
R(a)=(a-2)(a-3)(a^3+3a^2-1)\quad\text{over }\mathbb F_7,
\qquad b=3a(a+1).
\]
Two have rational \(a\)-coordinates \(2,3\), and the remaining three form one cubic Galois orbit. There is no Prym \(7\)-rank two, and no Jacobian \(7\)-rank zero in this family.

The Cartier Hasse determinant for the displayed differential basis is
\[
3b^2 u v^2.
\]
The scheme of Cartier rank at most two is the **reduced** divisor \(v=0\) on the smooth parameter surface, even though the Hasse divisor has multiplicity two along it. The \(u=0\) Hasse component has multiplicity one.

## Assumptions and scope
All statements are over the algebraically closed field \(k\) of characteristic seven. A curve means the smooth projective model of the displayed equation, which is well defined exactly for \(b\Delta\ne0\). A \(7\)-rank is the dimension of the geometric \(7\)-torsion \(\mathbb F_7\)-vector space of an abelian variety, equivalently the stable rank of Cartier on regular one-forms. The Cartier \(a\)-number is the dimension of the kernel of Cartier. The Prym is the connected kernel of the norm to the genus-one quotient; the associated Jacobian-to-product isogeny has degree prime to seven. Counts refer to normalized coefficient pairs, **not** to geometric isomorphism classes.

## Proof

**1. Smoothness and quotient.** Factor \(F_{a,b}(x)=x g(x^3)\), where \(g(z)=z^3+z^2+az+b\). As \(\operatorname{char}k=7\), the map \(x\mapsto x^3\) is separable away from zero. Hence \(F\) is separable if and only if \(b\ne0\) and \(g\) has three distinct roots. The cubic discriminant of \(g\) reduces to \(\Delta=a^2+3a^3+3b+b^2+4ab\). With \(\deg F=10\), a separable hyperelliptic model has genus four.

Let \(\zeta\) be a primitive cube root of unity. The automorphism \((x,y)\mapsto(\zeta x,\zeta^2y)\) has order three. Its invariant coordinates \(X=x^3\), \(Y=xy\) satisfy
\[
E_{a,b}:Y^2=X(X^3+X^2+aX+b).
\]
The quotient is a smooth elliptic curve because \(Xg(X)\) is separable. Since three is invertible in \(k\), the quotient and connected Prym give a prime-to-seven isogeny \(J(H_{a,b})\sim E_{a,b}\times P_{a,b}\). Thus their geometric \(7\)-ranks add.

**2. Cartier coefficients.** On \(H_{a,b}\) take the basis \(\omega_j=x^{j-1}dx/y\), \(1\le j\le4\). For \(F^3=\sum c_i x^i\), the standard Cartier formula is \(\mathcal C(\omega_j)=\sum_{i=1}^4 c_{7i-j}^{1/7}\omega_i\). Direct multinomial expansion over \(\mathbb F_7[a,b]\) gives the coefficient matrix
\[
M=\begin{pmatrix}
3ab^2&0&0&b^3\\
0&u&0&0\\
0&0&v&0\\
3&0&0&3(a+1)
\end{pmatrix}.
\]
The elliptic quotient Hasse coefficient (the coefficient of \(X^6\) in \([X(X^3+X^2+aX+b)]^3\)) equals \(u\), so the elliptic quotient is ordinary exactly when \(u\ne0\).

Write \(B=\bigl(\begin{smallmatrix}3ab^2&b^3\\3&3(a+1)\end{smallmatrix}\bigr)\) for the block indexed by \(1,4\). It has determinant \(3b^2 v\). Consequently \(\det M=3b^2uv^2\). On the smooth locus \(b\ne0\), if \(v\ne0\) then \(B\) is invertible; the rank of Cartier is four if \(u\ne0\) and three if \(u=0\). If \(v=0\), then \(b=3a(a+1)\). Substitution yields
\[
\Delta\big|_{v=0}=2a(a+2)^3,\qquad
u\big|_{v=0}=-a^2(a+2)^2.
\]
The smoothness condition also requires \(a+1\ne0\). Hence \(a\notin\{0,-1,-2\}\), and \(u\ne0\). Since the lower left entry of \(B\) equals \(3\), this block has rank one and Cartier has rank two. The displayed \(a\)-numbers follow.

**3. Stable Cartier rank and the five points.** For \(v\ne0\), the block \(B\) and the scalar \(v\) are invertible under all Frobenius twists, while the scalar \(u\) contributes a stable rank one exactly if \(u\ne0\). Thus the total \(7\)-rank is four or three as stated.

For \(v=0\), factor \(B=z w^{\mathsf T}\) with
\[
z=(ab^2,1)^{\mathsf T},\qquad w=(3,3(a+1))^{\mathsf T}.
\]
The Cartier operator uses seventh roots of entries; its second iterate on this block has rank zero precisely when \(w^{(7)\mathsf T}z=0\). Indeed, for the coefficient matrix \(M\), the second iterate is represented up to entrywise seventh roots by \(M^{(7)}M\). The relevant scalar reduces on \(v=0\) to
\[
w^{(7)\mathsf T}z=3(ab^2+(a+1)^7)=3(a+1)^2\bigl(2a^3+(a+1)^5\bigr).
\]
Because \(a+1\ne0\), this vanishes precisely when \(R(a)=0\). If it vanishes, all further Cartier iterates have zero rank on \(B\); otherwise every iterate has rank one on that block. The remaining scalar \(u\) is nonzero on \(v=0\), and \(v=0\) contributes no rank. Hence the Jacobian's stable ranks are one and two, respectively; subtracting the ordinary elliptic quotient's rank one gives Prym rank zero or one.

The polynomial \(R(a)=2a^3+(a+1)^5\) has degree five and factors as stated. Its formal derivative is \(6a^2+5(a+1)^4\). If \(R=R'=0\), multiplying \(R'\) by \(a(a+1)\) and using \(R=0\) implies \(a=5=-2\), but \(R(-2)=4\ne0\). Thus \(R\) is squarefree. Direct substitution gives \(R(0)=1\), \(R(-1)=5\), and \(R(-2)=4\); all five roots occur in the smooth graph. The cubic factor has no root in \(\mathbb F_7\), so the stated field-of-definition pattern follows.

**4. Divisor structure.** With \(b\Delta\) inverted, the loci \(u=0\) and \(v=0\) are disjoint by the restriction \(u|_{v=0}=-a^2(a+2)^2\), whose zeros violate smoothness. The \(3\times3\) minors of \(M\) generate \((v)\) on this smooth locus: all have a factor \(v\), and one is \(3b^2uv\); near \(v=0\) the factor \(3b^2u\) is a unit. The resulting rank-at-most-two subscheme is the reduced graph \(v=0\). The polynomial \(u\) defines a reduced curve there as well: a common zero of \(u,u_a,u_b\) forces \((a,b)=(0,0)\), excluded by smoothness. Therefore the Hasse determinant \(3b^2uv^2\) has multiplicity one on \(u=0\) and two on \(v=0\), as asserted.

## Verification
Run `python verify_cartier.py` for a standard-library multinomial reconstruction of the full characteristic-seven Cartier coefficient matrix and independent elliptic Hasse coefficient. Run `python verify_strata.py` (SymPy required) for polynomial identities, squarefreeness, divisor factorizations, and a complete prime-field sample of smooth coefficient pairs with Cartier and stable-rank checks. The symbolic rank proof above applies over \(\overline{\mathbb F}_7\), while finite-field samples and executions are corroboration only.

## Relationship to prior work
Kudo, Nakagawa and Takagi (first publicly posted 26 October 2022) introduce precisely this \(C_6\)-automorphism genus-four family, prove the general coefficient-position formula for its Cartier matrix (Lemma 3.1.1), and enumerate superspecial members over finite fields primarily in characteristics at least seventeen. Their construction and general Cartier formula are prerequisites here, not claimed as new. The new statement resolves the complete characteristic-seven geometric \(7\)-rank and Cartier \(a\)-number stratification, including five non-superspecial zero-rank Pryms, a missing rank-two Prym stratum, and the divisor multiplicities. Li, Mantovan, Pries and Tang analyze Newton polygons for Moonen's twenty *special* families of cyclic covers; their printed sextic monodromy types do not give the particular \((6;1,2,3,3,3)\) coefficient-level result or its five-point locus. An older unindexed equivalent calculation or a consequence of broader cyclic-cover machinery remains a priority risk.

## Limitations
This theorem is confined to a normalized two-parameter family in characteristic seven. It does not classify isomorphism classes of its curves or Pryms, full Newton polygons, or all hyperelliptic genus-four curves with \(C_6\) automorphisms in other characteristics. The five-point count is for distinct geometric coefficient pairs. No independent mathematical audit has been performed, and the priority comparison is limited to accessible literature and targeted searches.

## References
1. M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing \(\mathbb Z_6\)*, arXiv:2210.14822 (first posted 2022-10-26), especially Section 2.2 and Section 3.1, https://arxiv.org/abs/2210.14822.
2. W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, arXiv:1805.06914, especially the tables of monodromy data, https://arxiv.org/abs/1805.06914.
3. N. Yui, *On the Jacobian varieties of hyperelliptic curves over fields of characteristic \(p>2\)*, Journal of Algebra 52 (1978), 378–410 (standard Cartier coefficient formula, as cited in Reference 1).
