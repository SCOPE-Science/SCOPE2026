# The orbit census of period-six derivations of the three-dimensional Heisenberg Lie algebra

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\ge5\), and let \(\mathfrak h=\mathfrak h_3(k)\) have basis \(x,y,z\) and sole nonzero basis bracket \([x,y]=z\). Let \(\mathscr D_6(k)\) be the set of \(k\)-linear derivations of \(\mathfrak h\) of **exact multiplicative order six** as endomorphisms (composition powers). Conjugacy is under the full Lie-algebra automorphism group \(\operatorname{Aut}_k(\mathfrak h)\).

The complete conjugacy census is:

| Field condition | Conjugacy classes and respective sizes | Total \(|\mathscr D_6(k)|\) |
|---|---|---|
| \(p\ne7,\ q\equiv1\pmod6\) | Six classes, size \(q^3(q+1)\) each | \(6q^3(q+1)\) |
| \(q\equiv5\pmod6\) | Two classes, size \(q^3(q-1)\) each | \(2q^3(q-1)\) |
| \(p=7\) | Twelve classes of size \(q^3(q+1)\) and three of size \(q^2\) | \(q^2(12q(q+1)+3)\) |

Every class is specified explicitly by its quotient matrix eigenvalues as follows. In the first row, the six unordered pairs of sixth roots of unity having ratio a primitive cube root give the six split classes. In the second row, the two Galois-conjugate unordered pairs \(\{\omega,\omega^2\}\) and \(\{\eta,\eta^{-1}\}\), where \(\omega\) is a primitive cube root and \(\eta\) a primitive sixth root, give the two nonsplit classes. In characteristic seven, the twelve unordered distinct pairs \(\{a,b\}\subset\mathbb F_7^\times\) with \(a+b\ne0\) give the regular split classes, and the three scalar blocks \(aI_2\) with \(a\in\{3,5,6\}\subset\mathbb F_7\) give the remaining classes. In characteristic seven there are additionally exactly three order-three derivation classes, of size \(q^2\) each, from the scalar blocks \(aI_2\), \(a\in\{1,2,4\}\). No order-one or order-two derivations exist under the stated hypotheses.

## Assumptions and scope
Here \(p\ge5\) is prime and \(q=p^e\) with \(e\ge1\). By the *order* of a derivation we mean its order in \(\operatorname{GL}_k(\mathfrak h)\), not the order of a Lie-algebra automorphism. A derivation need not be a Lie-algebra automorphism; it is conjugated by the latter group. A scalar class means that the induced operator on \(\mathfrak h/kz\) is scalar. The classification is for the nonabelian three-dimensional Heisenberg Lie algebra, not higher-dimensional Heisenberg algebras.

## Proof
**1. Derivations and automorphisms.** The derivation identity applied to \([x,y]=z\) shows that every derivation, and only a derivation, has the matrix
\[
D(A,v)=\begin{pmatrix} A&0\\v&\operatorname{tr}A\end{pmatrix},\qquad A\in M_2(k),\ v\in k^{1\times2}.
\]
All Lie automorphisms have matrices \(g(B,w)=\left(\begin{smallmatrix}B&0\\w&\det B\end{smallmatrix}\right)\) with \(B\in\operatorname{GL}_2(k)\) and \(w\in k^{1\times2}\). If \(D\) has finite nonzero order, \(A\) is invertible. For invertible \(A\), Cayley--Hamilton gives
\[
(\operatorname{tr}A)I_2-A=\operatorname{adj}(A),\qquad \det((\operatorname{tr}A)I_2-A)=\det A\ne0.
\]
Conjugation by \(g(I_2,w)\) changes \(v\) to \(v-w((\operatorname{tr}A)I_2-A)\), so a unique \(w\) removes \(v\). Conjugation by \(g(B,0)\) then acts on \(A\) by usual similarity. Thus the desired automorphism orbits are in bijection with ordinary similarity classes of admissible \(A\), and an orbit associated to \(A\) has size \(q^2|\operatorname{GL}_2(k)|/|C_{\operatorname{GL}_2(k)}(A)|\). All \(q^2\) central-row choices are conjugate.

**2. Sixth-root condition and the arithmetic exception.** For \(p\ge5\), the polynomial \(T^6-1\) is separable. The block diagonal reduction shows that \(D^6=I\) precisely when \(A^6=I_2\) and \((\operatorname{tr}A)^6=1\). Over an algebraic closure, let \(\alpha,\beta\) be the eigenvalues of \(A\); then they and \(\alpha+\beta\) are sixth roots of unity. Consequently \(r=\alpha/\beta\) satisfies
\[
r^6=1,\qquad (1+r)^6=1.
\]
The polynomial \(\Phi_3(T)=T^2+T+1\) divides both expressions \(T^6-1\) and \((T+1)^6-1\) over the integers. After division by \(\Phi_3\), the two monic degree-four integer polynomials are
\[
F(T)=T^4-T^3+T-1,\qquad G(T)=T^4+5T^3+9T^2+6T.
\]
Their integer resultant is \(-2^2\cdot3\cdot7^3\) (the sign is immaterial). Thus in characteristic \(p\ge5\), \(p\ne7\), the only common roots are the two roots of \(\Phi_3\): the ratio \(r\) must be a primitive cube root. In characteristic seven, the six sixth roots are exactly \(\mathbb F_7^\times\), and the condition on \(r\) becomes \(r\ne-1\), i.e. precisely that the two nonzero eigenvalues have nonzero sum. This conclusion applies over every extension \(\mathbb F_{7^e}\).

**3. Finite-field descent and class sizes.** If \(p\ne7\) and \(q\equiv1\pmod6\), all sixth roots lie in \(k\). There are six unordered distinct root pairs with primitive-cube-root ratio. Each produces one split regular semisimple similarity class, with centralizer size \((q-1)^2\) in \(\operatorname{GL}_2(k)\), hence derivation orbit size \(q^2 q(q+1)=q^3(q+1)\). If \(q\equiv5\pmod6\), Frobenius inverts sixth roots. Exactly two eligible unordered pairs are Frobenius stable: those of the two primitive cube roots, and of the two primitive sixth roots. Their matrices are nonsplit regular semisimple; each has centralizer size \(q^2-1\), hence orbit size \(q^3(q-1)\).

If \(p=7\), all sixth roots lie in the prime subfield and there are \(\binom{6}{2}-3=12\) unordered distinct non-opposite pairs. These yield regular split classes. The other admissible semisimple blocks are the six scalar matrices \(aI_2\), \(a\in\mathbb F_7^\times\). For a scalar block, its orbit has size \(q^2\), since all of \(\operatorname{GL}_2(k)\) centralizes it.

**4. Exact orders.** In characteristic not seven, an order-three derivation would require \(\alpha^3=\beta^3=(\alpha+\beta)^3=1\). But the established ratio \(r\) is a primitive cube root, so \((1+r)^3=-1\) and hence \((\alpha+\beta)^3=\beta^3(1+r)^3=-1\ne1\), a contradiction. An order-two derivation would have \(\alpha,\beta\in\{1,-1\}\) and \(\alpha+\beta\in\{0,2,-2\}\), none of which equals \(1\) or \(-1\) in characteristic at least five. Therefore every admissible derivation in these fields has exact order six. In characteristic seven, the unique subgroup of \(\mathbb F_7^\times\) of order three is \(\{1,2,4\}\). The sum of any two distinct elements of this subgroup lies outside it, so all twelve regular classes have exact order six. A scalar block \(aI_2\) yields eigenvalues \(a,a,2a\), and multiplication by \(2\) preserves the order-three subgroup; hence exactly \(a\in\{1,2,4\}\) give order three, while the remaining \(a\in\{3,5,6\}\) give order six. Orders one and two are impossible for nonabelian \(\mathfrak h\) when \(p\ge5\). This completes the classification and yields the totals in the table.

## Verification
The standalone script `verify.py` enumerates all \(2\times2\) matrices over prime fields of orders \(5,7,11,13,19\). It tests powers \(1,2,3,6\) exactly, groups eligible matrices by characteristic polynomial (equivalent to similarity for the semisimple matrices present), and checks both the class count and the predicted multiplicities. Its successful terminal line is `PERIODIC_DERIVATIONS_OK`. The general finite-field and extension-field assertions follow from the proof, not from the finite tests.

## Relationship to prior work
Burde and Moens (2011; published 2012), especially their Example 2.9 and Proposition 2.5, demonstrate periodic derivations of the three-dimensional Heisenberg algebra and the distinguished role of order six in characteristic zero. Their result supplies explicit examples and structural existence statements rather than an enumeration of finite-field conjugacy classes and orbit sizes. Burde and Moens (2020) study arbitrary-characteristic derivations satisfying polynomial identities and explicitly tabulate the characteristic-seven obstruction in the resultant for sixth roots; their resultant mechanism anticipates why characteristic seven is exceptional. The present finite-field conjugacy census is a separate quantitative statement obtained by combining this root phenomenon with a direct orbit computation. It does not claim to discover the characteristic-seven exceptional prime or the existence of periodic Heisenberg derivations.

## Limitations
The statement excludes characteristics two and three, excludes other periods, and does not classify higher-dimensional Heisenberg algebras. The full generality is proved algebraically; finite numerical checks alone would not establish it. Published-work comparison was bounded, and an unlocated classical or later explicit orbit enumeration could overlap this exact count. Independent external validation has not been performed.

## References
1. D. Burde and W. A. Moens, *Periodic derivations and prederivations of Lie algebras*, arXiv:1108.3548v1, first public version 2011-08-17; *J. Algebra* **357** (2012), 208–221. https://arxiv.org/abs/1108.3548
2. D. Burde and W. A. Moens, *The structure of Lie algebras with a derivation satisfying a polynomial identity*, arXiv:2009.05434, first public version 2020-09-11. https://arxiv.org/abs/2009.05434
