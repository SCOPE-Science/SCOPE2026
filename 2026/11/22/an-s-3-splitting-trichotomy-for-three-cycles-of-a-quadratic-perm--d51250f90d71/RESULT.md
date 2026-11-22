# An \(S_3\) splitting trichotomy for three-cycles of a quadratic permutation

## Finding

Let \(p\) be an odd prime, \(m\geq1\), and \(K=\mathbb F_{p^m}\). Consider the polynomial permutation
\[
F(x,y)=\bigl((x+y)^2+x,\;(x+y)^2-y\bigr)
\]
of \(K^2\). Write \(N_3(p,m)\) for the number of *unoriented primitive cycles of least length three* in its functional graph.

The map has precisely one fixed point, \((0,0)\), and no primitive cycles of length two. For \(p=3\), \(N_3(3,m)=0\) for every \(m\geq1\). For every \(p\geq5\), let \(d_p\) denote the order of the Frobenius conjugacy class of \(p\) in the splitting field over \(\mathbb Q\) of
\[
J(Z)=Z^3-3Z+6.
\]
That splitting field is Galois of degree six, with group \(S_3\); its only ramified primes are among two and three. The exact count is
\[
\boxed{N_3(p,m)=2\,\mathbf 1_{d_p\mid m},\qquad d_p\in\{1,2,3\}.}
\]
Moreover the sets of primes with \(d_p=1,2,3\) have respective natural densities \(1/6,1/2,1/3\). Consequently exactly a density \(1/6\) of primes support three-cycles over the prime field; every \(p\geq5\) supports exactly two such cycles over \(\mathbb F_{p^6}\).

There is a base-field criterion requiring only a quadratic character and a cubic root test:
\[
N_3(p,1)=2\iff \left(\frac{-6}{p}\right)=1\quad\text{and}\quad
\exists z\in\mathbb F_p:\ z^3-3z+6=0.
\]

## Assumptions and scope

All fields in the theorem have odd characteristic; only \(p\geq5\) is covered by the unramified splitting criterion. The arithmetic density is a natural density **among rational primes**, not a density of points in a fixed finite field. Two distinct three-cycles mean six distinct points. No claim is made about primitive cycles of length four or greater, or about the full cycle decomposition of \(F\).

## Proof

**1. Polynomial conjugacy.** In odd characteristic the invertible linear coordinate change
\[
(u,v)=\bigl(2(x+y),2(x-y)\bigr)
\]
conjugates \(F\) to the quadratic Hénon permutation
\[
H(u,v)=(u^2+v,u),\qquad H^{-1}(a,b)=(b,a-b^2).
\]
Directly, a fixed point obeys \(v=u\) and \(u^2=0\), so only the origin is fixed. If \(H^2(u,v)=(u,v)\), its second coordinate gives \(u^2+v=v\), hence \(u=0\); its first coordinate then gives \(v^2=0\). Thus there are no nontrivial two-cycles.

**2. Exact third-iterate elimination.** Put \(t=u^2+v\). Then
\[
H^2(u,v)=(t^2+u,t),\qquad H^3(u,v)=((t^2+u)^2+t,t^2+u).
\]
The period-dividing-three condition is equivalent to the pair
\[
A=t^2-t+u^2+u=0,\quad B=(t-u^2)^2+t-u=0.
\]
Indeed the second coordinate gives \(t^2+u=v=t-u^2\), after which the first coordinate can be rewritten using \(v=t-u^2\). Subtraction gives
\[
B-A=2(1-u^2)t+u^4-u^2-2u.
\]
When \(u^2=1\) this difference is \(-2u\ne0\), so such an element cannot be periodic of period dividing three. Otherwise the unique possible value of \(t\) is
\[
t=\frac{-u^4+u^2+2u}{2(1-u^2)}.
\]
Substitution into **both** equations yields the identical expression
\[
A=B=\frac{u^2(u^6-3u^2+6)}{4(1-u^2)^2}.
\]
Therefore, over every odd-characteristic field, the points fixed by \(H^3\) are in bijection with \(u=0\) and the *distinct nonzero* roots of
\[
g(U)=U^6-3U^2+6.
\]
For each \(u\), the corresponding second coordinate is uniquely \(v=t-u^2\). At \(u=0\) this is the fixed point \((0,0)\). In characteristic three the polynomial reduces to \(U^6\), giving no other fixed points of \(H^3\). For \(p\geq5\), \(g(0)=6\ne0\), \(g(\pm1)=4\ne0\), and
\[
\operatorname{disc}(g)=-2^{17}3^7,
\]
so its six roots are simple. Every nonzero root corresponds to a point of *exact* period three.

**3. Splitting field and the regular action.** Both \(g(U)\) and \(J(Z)\) are Eisenstein at three. The discriminant of \(J\) is \(-864=-6\cdot12^2\). Hence its splitting field \(E\) has Galois group \(S_3\) and degree six over \(\mathbb Q\).

For any algebraic root \(a\) of \(g\), the identity
\[
g(U)=(U^3-3U)^2+6(1-U^2)^2
\]
and \(g(\pm1)\ne0\) show that
\[
w=\frac{a^3-3a}{a^2-1}\in\mathbb Q(a),\qquad w^2=-6.
\]
Over \(\mathbb Q(w)\), the sextic factors as
\[
g(U)=(U^3-wU^2-3U+w)(U^3+wU^2-3U-w).
\]
The first cubic has discriminant \(36\), and is irreducible over \(\mathbb Q(w)\) because \([\mathbb Q(a):\mathbb Q]=6\) and \([\mathbb Q(w):\mathbb Q]=2\). An irreducible cubic with square discriminant has cyclic Galois group, so all three roots of the first factor belong to \(\mathbb Q(a)\). The roots of the second factor are their negatives. Therefore \(L=\mathbb Q(a)\) is the full splitting field of \(g\), of degree six. Squaring its six roots gives all three roots of \(J\), so \(E\subseteq L\). Since both fields have degree six, \(E=L\).

Thus the six roots of \(g\) form a *regular* \(S_3\)-set: irreducibility makes the action transitive, and six equals the group order, so every point stabilizer is trivial.

**4. Finite-field orbit count and prime densities.** For every \(p\geq5\), the polynomial \(g\) has separable reduction and is unramified. The conjugacy class of Frobenius on its roots is the regular permutation action of an element of \(S_3\). No nonidentity element fixes a root. Consequently \(g\) has either six or zero roots in \(\mathbb F_{p^m}\), according as \(\operatorname{Frob}_p^m\) is the identity or not. By Step 2, six roots give exactly two three-cycles, proving the formula.

The conjugacy classes of \(S_3\) comprise the identity (one element), transpositions (three), and three-cycles (two), of orders one, two, three. Chebotarev's density theorem gives the displayed densities. Finally, the cubic \(J\) splits over \(\mathbb F_p\) exactly when its Frobenius is the identity. Since \(\operatorname{disc}(J)=-6\cdot12^2\), a cubic root together with the quadratic character \(\left(\frac{-6}{p}\right)=1\) forces complete splitting; conversely complete splitting implies both conditions.

## Verification

The supplied `verify.py` requires only Python 3's standard library. Run `python3 verify.py` from the extracted package. It independently checks the two integral polynomial-elimination identities, the sextic square decomposition, direct conjugacy on small prime fields, direct third-iterate and fixed-point counts over all prime fields through \(139\), and extension-root counts through degrees six using polynomial arithmetic modulo the sextic. It checks \(194081\) prime-field points and the three Frobenius patterns; no symbolic-computation package is required. These finite computations supplement the algebraic proof and do not certify the infinitude or natural densities.

## Relationship to prior work

Ruikai Chen, *Permutation polynomials from quadratic and linear forms*, arXiv:2611.09629v1 (submitted November 6, 2026), Example 7, supplies the underlying quadratic permutation and tests bijectivity, but does not state the cycle census or a Frobenius splitting law. The conjugacy identifies this example with the classical quadratic Hénon family; this identification is not claimed as the original contribution. Patrick Ingram's *Canonical heights for Hénon maps* develops arithmetic height and rational-period questions for the Hénon family, not this explicit finite-field three-cycle profile. The 2024 multi-author Hénon open-problems survey likewise discusses arithmetic periodic points over number fields without the displayed prime-density classification. Related exact small-cycle counts for other polynomial permutations do not imply the sextic splitting law for this particular example.

## Limitations

The result is only a least-period-three classification (with fixed and period-two exclusions), not a classification of longer cycles. Chebotarev supplies an asymptotic density, not an effective least prime with a specified Frobenius class or a uniform finite interval error term. The characteristic-three case is exceptional and was handled directly rather than by unramified Frobenius. The algebraic calculation is elementary, but an unnoticed equivalent treatment of this specific Hénon parameter in earlier dynamical literature remains a possible priority risk; the cited source inspections do not establish absolute novelty.

## References

1. Ruikai Chen, *Permutation polynomials from quadratic and linear forms*, arXiv:2611.09629v1, November 6, 2026, Example 7. https://arxiv.org/abs/2611.09629
2. Patrick Ingram, *Canonical heights for Hénon maps*, arXiv:1111.3609, first submitted November 15, 2011; *Proceedings of the London Mathematical Society* 108 (2014), 780–808. https://arxiv.org/abs/1111.3609
3. J. Xénelkis de Hénon and contributors, *Hénon maps: a list of open problems*, *Arnold Mathematical Journal*, August 13, 2024, especially Section 11. https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html
4. A. Endler and J. A. C. Gallas, *Arithmetical signatures of the dynamics of the Hénon map*, *Physical Review E* 65 (2002), 036231 (period-four orbit parametrization). https://doi.org/10.1103/PhysRevE.65.036231
5. Classical results: Eisenstein's irreducibility criterion; discriminant criterion for cubic splitting groups; Dedekind–Frobenius splitting theory; Chebotarev's prime-density theorem.
