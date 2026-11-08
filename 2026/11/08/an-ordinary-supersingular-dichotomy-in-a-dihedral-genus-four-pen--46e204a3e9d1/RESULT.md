# An ordinary–supersingular dichotomy in a dihedral genus-four pencil

## Finding
Let \(k=\overline{\mathbb F}_p\), where \(p\) is an odd prime with \(p\equiv2,3\pmod5\). For every \(a\in k\) with \(a^2\ne4\), consider
\[
 C_a:\quad y^2=x^{10}+ax^5+1.
\]
Then \(C_a\) is a smooth hyperelliptic curve of genus four, and
\[
 J(C_a)\sim J(D_a)^2,\qquad D_a:\ v^2=(u+2)(u^5-5u^3+5u+a).
\]
Here \(D_a\) is smooth of genus two and \(\sim\) denotes isogeny over \(k\). The Newton polygon of \(J(C_a)\) is **either ordinary or entirely slope one-half**. In particular, its geometric \(p\)-rank is always either \(4\) or \(0\).

For \(p=7\), the arithmetic classification is exact:
\[
 (f_7(J(C_a)),a(J(C_a)))=\begin{cases}
 (0,2),&a=0\ \text{or}\ a^2=-1,\\
 (4,0),&a(a^2+1)\ne0.
 \end{cases}
\]
Here \(a(J)\) is the Cartier \(a\)-number, not the coefficient parameter. Therefore **exactly three** smooth geometric coefficient parameters in this pencil give supersingular but non-superspecial genus-four Jacobians. The parameters \(a\) and \(-a\) may define isomorphic curves; this is not an isomorphism-class census.

## Assumptions and scope
The ground field is algebraically closed and of odd characteristic different from five; for the Newton-polygon statement, its characteristic is \(2\) or \(3\) modulo five. The curve is the smooth projective model of the displayed affine equation, with \(a^2\ne4\). Ordinary means \(p\)-rank equals dimension; supersingular means all Newton slopes equal \(1/2\). The group action and isogeny statements are geometric, not assertions that the quotient maps descend to a specified finite base field without adjoining fifth roots of unity.

## Proof
**1. Smoothness and symmetry.** Put \(F_a(x)=x^{10}+ax^5+1\). Since \(p\ne2,5\), its repeated roots satisfy \(x^5=-a/2\) and \(F_a(x)=1-a^2/4\). Thus \(F_a\) is squarefree exactly when \(a^2\ne4\). It has degree ten and gives genus \(4\). Choose a primitive fifth root of unity \(\zeta\in k\). The maps
\[
 \sigma(x,y)=(\zeta x,y),\qquad \tau(x,y)=(x^{-1},y/x^5)
\]
act as automorphisms. They satisfy \(\sigma^5=\tau^2=1\) and \(\tau\sigma\tau=\sigma^{-1}\), hence generate a dihedral group of order ten.

**2. Two genus-two quotients and the square decomposition.** The invariant functions for \(\tau\) are
\[
 u=x+x^{-1},\qquad v=y(x+1)x^{-3}.
\]
The Laurent identity \(x^5+x^{-5}=u^5-5u^3+5u\) gives
\[
 v^2=(u+2)(u^5-5u^3+5u+a).
\]
The five roots of \(u^5-5u^3+5u+a\) correspond to reciprocal pairs of roots of \(x^{10}+ax^5+1\), and are distinct for \(a^2\ne4\). The extra root \(u=-2\) is different, because the quintic takes the value \(a-2\) there. Thus the sextic is squarefree and \(D_a=C_a/\langle\tau\rangle\) has genus two. Every reflection \(\sigma^j\tau\) is conjugate to \(\tau\), and its quotient is a genus-two curve isomorphic to \(D_a\).

A basis of regular differentials on \(C_a\) is \(\omega_i=x^{i-1}dx/y\), for \(1\le i\le4\). On these,
\[
 \sigma^*\omega_i=\zeta^i\omega_i,\qquad \tau^*\omega_i=-\omega_{5-i}.
\]
The pullback of the differential space of each reflection quotient is the two-dimensional \(+1\)-eigenspace of that reflection. The \(+1\)-eigenspaces for \(\tau\) and \(\sigma\tau\) intersect trivially: a common vector would be fixed by their product \(\sigma\), which has no eigenvalue \(1\) on the four-dimensional differential space. Hence these two pullback spaces sum to all four differentials. Pullback on Jacobians from the two genus-two quotients consequently defines a separable isogeny
\[
 J(D_a)\times J(D_a)\longrightarrow J(C_a).
\]

**3. Cartier monomial cycle.** The standard coefficient formula for the Cartier–Manin matrix on a hyperelliptic curve is
\[
 M_{ij}=[x^{pi-j}]F_a(x)^{(p-1)/2},\qquad 1\le i,j\le4.
\]
Every power of \(x\) in the expansion of \(F_a^{(p-1)/2}\) is divisible by five. Therefore \(M_{ij}\) can be nonzero only when \(j\equiv pi\pmod5\). For \(p\equiv2,3\pmod5\), multiplication by \(p\) permutes \(\{1,2,3,4\}\) in a **single four-cycle**. If all four permitted entries are nonzero, \(M\) is invertible and the Jacobian is ordinary. If any permitted entry is zero, the fourth Frobenius-twisted product \(M M^{(p)}M^{(p^2)}M^{(p^3)}\) vanishes (up to the harmless convention-dependent reversal of the twisted order), because every cycle traverses that zero edge. Thus the stable Frobenius rank and the geometric \(p\)-rank are zero. There is no intermediate rank.

**4. Why the rank-zero case is supersingular.** By step 2, \(J(C_a)\) is isogenous to \(J(D_a)^2\), so its \(p\)-rank equals twice that of the genus-two Jacobian \(J(D_a)\). If the rank of \(J(C_a)\) is zero then \(J(D_a)\) has \(p\)-rank zero. A principally polarized abelian surface of \(p\)-rank zero is supersingular: denominator divisibility for Newton slopes in height four and slope symmetry leave only four copies of slope \(1/2\). Therefore \(J(C_a)\) is supersingular. This argument gives the asserted Newton-polygon dichotomy, not merely a dichotomy of ranks.

**5. The exact characteristic-seven locus.** For \(p=7\), coefficient extraction from \(F_a(x)^3\) gives
\[
 M(a)=\begin{pmatrix}
 0&3a&0&0\\
 0&0&0&3(a^2+1)\\
 3(a^2+1)&0&0&0\\
 0&0&3a&0
 \end{pmatrix}.
\]
Its permitted entries are nonzero exactly when \(a(a^2+1)\ne0\), and its rank falls from four to two exactly at \(a=0\) and the two distinct roots of \(a^2+1\). These are all smooth, since none satisfies \(a^2=4\) in characteristic seven. By the Cartier-kernel formula \(a(J(C_a))=4-\operatorname{rank}M(a)\), their \(a\)-number is \(2\), while the ordinary locus has \(a\)-number \(0\). This proves the stated classification.

## Verification
The standalone programs `verify_cartier.py` and `verify_quotient.py` use exact integer/polynomial arithmetic. The first reconstructs the characteristic-seven Cartier matrix from expansion and checks monomial support for sample primes congruent to two or three modulo five; it checks all three exceptional parameters over \(\mathbb F_{49}\). The second verifies the involution-quotient Laurent identity and computes an independent genus-two Cartier determinant \(2a(a^2+1)\) in characteristic seven. Both scripts terminate with `PASS` under Python 3. Their finite checks corroborate, but do not replace, the characteristic-uniform proof in steps 1–4.

## Relationship to prior work
Kudo, Nakagawa and Takagi develop Cartier-matrix algorithms and arithmetic searches for genus-four hyperelliptic curves carrying an order-three symmetry; those normal forms and computations differ from this order-five dihedral pencil. Bruin and Kulkarni classify geometrically hyperelliptic genus-four Jacobians that split as the square of a genus-two Jacobian; that general geometric framework is acknowledged and is not claimed as novel. Li, Mantovan, Pries and Tang describe Newton polygons in distinguished cyclic-cover families; their listed fivefold-cover families have different branch data from the cover here (the latter has exponents \((1,1,4,4)\)). The specific inert-prime Newton dichotomy and the exact three-parameter characteristic-seven degeneration are the contributions asserted here.

## Limitations
The proof does not classify characteristics congruent to one or four modulo five or characteristic five. It does not give an explicit supersingular parameter polynomial for every inert characteristic, an isomorphism-class count, a full Ekedahl–Oort stratification, or a superspecial Jacobian. Classical dihedral decompositions and general cyclic-cover techniques may yield some implications without the present wording; an equivalent older arithmetic specialization remains a priority risk.

## References
- M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing \(C_6\)*, arXiv:2210.14822, first public 2022-10-26, https://arxiv.org/abs/2210.14822.
- N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959, first public 2023-09-05, https://arxiv.org/abs/2309.01959.
- W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, arXiv:1805.06914, first public 2018-05-17, https://arxiv.org/abs/1805.06914.
- M. Kudo, S. Harashita and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095, first public 2019-03-19, https://arxiv.org/abs/1903.08095.
