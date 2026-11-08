# A reduced superspecial locus for a genus-four cyclic trigonal deformation in every characteristic \(p\equiv5\pmod6\)

## Finding
Let \(p\) be any rational prime with \(p\equiv5\pmod6\), let \(k=\overline{\mathbb F}_p\), and let \(t\in k\) satisfy \(t^2\ne4\). Let \(C_t\) be the smooth projective model of
\[
y^3=x^6+t x^3+1.
\]
Put \(q=(p-2)/3\) (an odd positive integer) and define the monic degree-\(q\) polynomial
\[
H_q(T)=[z^q](1+Tz+z^2)^q
=\sum_{j=0}^{\lfloor q/2\rfloor}\binom{q}{2j}\binom{2j}{j}T^{q-2j}\in\mathbb F_p[T].
\]
Then \(C_t\) has genus four, and its Jacobian has exactly the following two arithmetic possibilities:
\[
\begin{array}{c|cc}
&\text{Jacobian }p\text{-rank}&\text{Cartier }a\text{-number}\\\hline
H_q(t)=0&0&4\\
H_q(t)\ne0&2&2.
\end{array}
\]
The scheme \(V(H_q)\subset\mathbb A^1_k\) has **exactly \(q=(p-2)/3\) distinct reduced geometric points**, all in the smooth parameter locus. Every one is superspecial; there are no other superspecial members. In particular no smooth family member has \(p\)-rank one, three, or four, or \(a\)-number zero, one, or three. This counts coefficient parameters, not geometric isomorphism classes.

## Assumptions and scope
Characteristic is \(p>3\) with \(p\equiv2\pmod3\); all curve-theoretic invariants are geometric over \(k\). The cubic cover \(x:C_t\to\mathbb P^1\) is tamely ramified at the six simple zeros of \(f(x)=x^6+tx^3+1\), and unramified at the three points above infinity. Indeed \(f'(x)=3x^2(2x^3+t)\), so repeated roots occur precisely when \(t^2=4\). Riemann--Hurwitz gives \(2g-2=-6+6\cdot2=6\) and \(g=4\).

The four holomorphic differentials
\[
\omega_0=dx/y,\quad\omega_1=dx/y^2,\quad\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2
\]
form a basis. Regularity at the finite branch points follows by taking \(y\) as a parameter; at infinity, \(x\) has pole order one, \(y\) pole order two and \(dx\) pole order two. The four independent regular forms exhaust \(H^0(C_t,\Omega^1)\).

## Proof
The Cartier map \(\mathcal C\) is inverse-Frobenius semilinear and obeys \(\mathcal C(h^p\eta)=h\mathcal C(\eta)\). For any polynomial \(P(x)\), \(\mathcal C(P(x)dx)\) is obtained by taking the \(p\)-th roots of the coefficients of \(x^{p-1+pi}\) and replacing those monomials by \(x^i dx\).

Since \(p=3q+2\), put \(m=2q+1=(2p-1)/3\), and write \(F(z)=1+tz+z^2\). Then \(f(x)=F(x^3)\),
\[
\frac{dx}{y}=\left(\frac1{y^2}\right)^p f(x)^m dx,
\qquad
\frac{x^i dx}{y^2}=\left(\frac1y\right)^p x^i f(x)^q dx.
\]
In the first formula only the exponent \(2p-1\) can be both \(-1\) modulo \(p\) and divisible by three within the available degree range; in the second, only \(x^{p-1}\) is possible, and then only for \(i=1\). Consequently
\[
\mathcal C(\omega_0)=H_m(t)^{1/p}\omega_2,\quad
\mathcal C(\omega_2)=H_q(t)^{1/p}\omega_0,\quad
\mathcal C(\omega_1)=\mathcal C(\omega_3)=0,
\]
where \(H_n(T)=[z^n](1+Tz+z^2)^n\). It remains to compare the two coefficients without making any assumption about \(t\in\mathbb F_p\).

**Polynomial identity.** For every nonnegative integer \(n\), the monic polynomial \(H_n(T)\) satisfies
\[
(T^2-4)H_n''+(1-2n)T H_n'+n^2H_n=0.\tag{1}
\]
Indeed, the coefficient of \(T^{n-2j}\) is \(a_j=n!/((j!)^2(n-2j)!)\) and satisfies \(j^2a_j=(n-2j+2)(n-2j+1)a_{j-1}\). Put \(\Delta=T^2-4\) and \(r=(q+1)/2\). Since \(m=q+2r\) and \(m+q+1=p\), differentiating \(G=\Delta^r H_q\) and using (1) for \(H_q\) shows
\[
\Delta G''+(1-2m)TG'+m^2G=0\quad\text{in }\mathbb F_p[T].
\]
For a monic polynomial solution of degree \(m<p\) with parity \(m\), equation (1) determines all coefficients uniquely by the displayed recurrence: every denominator \(j^2\), for \(1\le j\le\lfloor m/2\rfloor\), is invertible modulo \(p\). Both \(G\) and \(H_m\) are such solutions. Hence the exact polynomial identity in \(\mathbb F_p[T]\) is
\[
\boxed{H_{2q+1}(T)=(T^2-4)^{(q+1)/2}H_q(T).}\tag{2}
\]
On \(t^2\ne4\), the two arrows of the Cartier operator therefore vanish simultaneously. If \(H_q(t)=0\), the Cartier operator is zero and the Jacobian is superspecial; its \(a\)-number equals four and \(p\)-rank zero. Otherwise it has an invertible semilinear two-cycle on \(\langle\omega_0,\omega_2\rangle\) and kills \(\omega_1,\omega_3\). The Cartier rank and its stable rank are both two; hence \(a=2\) and \(p\)-rank two.

**Reducedness and exact count.** The degree-\(q\) polynomial \(H_q\) is monic. At \(T=\pm2\) we have \(H_q(2)=\binom{2q}q\) and \(H_q(-2)=(-1)^q\binom{2q}q\), both nonzero since \(2q<p\). Suppose some root \(\alpha\) has multiplicity at least two. Since \(\alpha^2-4\ne0\), equation (1) first implies \(H_q''(\alpha)=0\), and repeated differentiation gives all derivatives through order \(q\) zero. This contradicts \(H_q^{(q)}(\alpha)=q!\ne0\), since \(q<p\). Thus \(H_q\) is squarefree and has exactly \(q\) distinct geometric roots, disjoint from the singular fibers. This completes the proof.

## Verification
Run `python3 verify_hasse_family.py` using the Python standard library. It computes the two relevant Cartier coefficients by two independent polynomial-expansion methods, verifies the exact factorization (2) and squarefreeness for every prime \(p\equiv5\pmod6\) up to 149, and independently checks the complete four-basis Cartier extraction for \(p=5,11,17\). These **finite checks corroborate** the characteristic-independent proof; they do not replace it. For instance, when \(p=5\), \(H_q(T)=T\), giving one superspecial parameter; when \(p=11\), \(H_q(T)=T^3+6T\), giving three distinct superspecial parameters.

## Relationship to prior work
Borges and Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987 (first public 2022-12-07), determine \(p\)-ranks of the fixed Fermat-type equations \(y^m=x^n+1\) and of additional fixed curves. Their Theorem 1.1 covers the special central fiber \(t=0\), but not the complete deformation parameter or its reduced exceptional locus. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4*, arXiv:1804.09063, proves superspeciality of a specific genus-four complete intersection for \(p\equiv2\pmod3\). This is prior evidence for the distinguished superspecial central case, not for the present moving-locus classification. Montanucci and Speziali, *The a-numbers of Fermat and Hurwitz curves*, arXiv:1603.03604, investigate fixed Fermat/Hurwitz curves by Cartier operators; no result for this nontrivial one-parameter deformation is claimed here as theirs. The coefficient-extraction method is standard; the claim of novelty is the full deformation stratification and \((p-2)/3\) reduced-parameter enumeration, not the underlying Cartier theory or the central Fermat example.

## Limitations
The count concerns parameter values in the displayed normalized coefficient family, not isomorphism classes of smooth curves. Some parameters may become isomorphic after coordinate changes. Only primes \(p\equiv5\pmod6\) are classified; the behavior at other primes is not claimed. The theorem supplies \(p\)-rank and \(a\)-number, not full Newton polygons of nonsuperspecial members. Even after targeted comparison, a historical-priority risk remains from any unindexed general theorem on Kummer covers or genus-four curves with a \((\mathbb Z/3)^2\)-action; no independent priority certification has been performed.

## References
- H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, v1 submitted 2022-12-07; full text: https://arxiv.org/html/2212.03987v3.
- M. Kudo, *On the existence of superspecial nonhyperelliptic curves of genus 4*, arXiv:1804.09063 (2018), https://arxiv.org/abs/1804.09063.
- M. Montanucci and P. Speziali, *The a-numbers of Fermat and Hurwitz curves*, arXiv:1603.03604 (2016), https://arxiv.org/abs/1603.03604.
