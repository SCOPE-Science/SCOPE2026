# Finite-field Galois descent for idempotents of odd-order core-quandle algebras

## Finding

Let \(A\) be a finite abelian group of **odd order**, with invariant factors \(A\cong\prod_{i=1}^{r}C_{n_i}\) and exponent \(M\). Let \(q=p^e\) be a prime power such that \(p\nmid |A|\). Equip \(A\) with the core-quandle operation \(x*y=2y-x\), and let \(K[A,*]\) be its generally nonassociative quandle algebra over \(K=\mathbb F_q\): its basis elements satisfy \(e_xe_y=e_{2y-x}\).

For each divisor \(m>1\) of \(M\), define
\[
 d_m=\operatorname{ord}_m(2),\quad
 H_m=\langle 2,-1\rangle\leq (\mathbb Z/m\mathbb Z)^\times,\quad
 L_m=\langle 2,-1,q\rangle\leq (\mathbb Z/m\mathbb Z)^\times.
\]
The element \(q\) is invertible modulo \(m\), by the characteristic hypothesis. Put \(t_m=[L_m:H_m]\). Define
\[
 E_m=\begin{cases}
 2^{d_m/2}+1,&-1\in\langle2\rangle\pmod m,\\
 2^{d_m}-1,&-1\notin\langle2\rangle\pmod m.
 \end{cases}
\]
In the first case \(d_m\) is even. Choose any integer \(b_m=\varepsilon 2^j\), with \(\varepsilon\in\{1,-1\}\) and \(0\leq j<d_m\), such that \(b_m\equiv q^{t_m}\pmod m\). Set
\[
 g_m=\gcd\big(E_m,|q^{t_m}-b_m|\big),
 \qquad
 N_m=\sum_{h\mid m}\mu(m/h)\prod_{i=1}^{r}\gcd(h,n_i).
\]
The integer \(g_m\) is independent of the chosen signed power \(b_m\). The integer \(N_m\) counts characters of \(A\) having exact order \(m\), so \(|L_m|\mid N_m\).

For each idempotent \(u\), write its Fourier transform over an algebraic closure as \(\widehat u(\chi)=\sum_{x\in A}u_x\chi(x)\). Let \(s(u)\) be the number of **nontrivial** characters with \(\widehat u(\chi)\ne0\), and let \(\epsilon(u)=\sum_xu_x\in\{0,1\}\) be the augmentation. The complete bivariate enumerator is
\[
 \boxed{\ \sum_{u^2=u}X^{s(u)}Y^{\epsilon(u)}
 =(1+Y)\prod_{\substack{m\mid M\\m>1}}
 (1+g_mX^{|L_m|})^{N_m/|L_m|}.\ }
\]
In particular, the exact number of idempotents, **including zero**, is
\[
 \boxed{\ |\{u\in K[A,*]:u^2=u\}|
 =2\prod_{\substack{m\mid M\\m>1}}(1+g_m)^{N_m/|L_m|}.\ }
\]
The formula is valid for all odd-order finite abelian groups and all nonmodular finite coefficient fields, without a splitting-field assumption. It classifies the solutions by independently selecting zero or one of \(g_m\) nonzero field-descent-compatible values for each \(L_m\)-orbit of characters.

For \(A=C_{11}\), the count is \(68\) over \(\mathbb F_2\) and \(24\) over \(\mathbb F_3\). For \(A=C_{17}\), it is \(648\) over \(\mathbb F_2\) and \(36\) over \(\mathbb F_3\). These differences occur even though the underlying quandle is unchanged.

## Assumptions and scope

The algebra is defined by bilinear extension of the indicated basis multiplication; it is not assumed associative or commutative. Character order refers to the order of a homomorphism \(A\to\overline{\mathbb F_q}^{\times}\), which is well-defined because \(p\nmid|A|\). The nontrivial Fourier-support statistic is measured over a splitting field, but is invariant under Frobenius and hence intrinsic to each element of the finite-field algebra. The count includes both augmentation-zero and augmentation-one idempotents; the factors \(1\) and \(Y\) account for these two distinct choices.

The characteristic restriction is essential: if \(p\mid |A|\), the Fourier transform on \(A\) does not have the inverse used here. Odd order is also essential for the doubling permutation on the character group. No classification of even-order core quandles or modular coefficient algebras is claimed.

## Proof

**1. Fourier polynomial identity.** Since \(p\nmid|A|\), character orthogonality and Fourier inversion work over a finite splitting extension of \(K\). For arbitrary algebra elements \(u=\sum_xu_xe_x\) and \(v=\sum_yv_ye_y\), directly substitute \(e_xe_y=e_{2y-x}\) to obtain
\[
 \widehat{uv}(\chi)=\sum_{x,y}u_xv_y\chi(2y-x)
 =\widehat u(\chi^{-1})\widehat v(\chi^2).
\]
Thus the idempotence equations are \(f(\chi)=f(\chi^{-1})f(\chi^2)\), where \(f=\widehat u\). At the trivial character, \(f(1)^2=f(1)\), yielding exactly two values \(0,1\).

**2. Every nonzero character orbit is completely supported and has one root parameter.** Let \(\chi\ne1\). If \(f(\chi)\ne0\), then \(f(\chi^{-1})\) and \(f(\chi^2)\) are nonzero. Applying the relation to \(\chi^{-1}\) proves the reverse inversion implication; applying it through the finite doubling cycle (doubling is invertible on odd-order characters) gives the same result in both directions. Hence each orbit under \(\langle2,-1\rangle\) is either entirely zero or entirely nonzero.

On a nonzero orbit, write \(h(\chi)=f(\chi)f(\chi^{-1})\). Multiplying the equations at \(\chi\) and \(\chi^{-1}\) and cancelling the nonzero left-hand product gives \(h(\chi^2)=1\). As doubling permutes this finite orbit, \(h(\chi)=1\) for all its members. Therefore
\[
 f(\chi^{-1})=f(\chi)^{-1},\qquad
 f(\chi^2)=f(\chi)^2.
\]
Writing \(a=f(\chi)\), the return after \(d_m\) doublings forces \(a^{2^{d_m}-1}=1\). If \(-1=2^{d_m/2}\pmod m\), compatibility with inversion forces \(a^{2^{d_m/2}+1}=1\). These constraints are sufficient as well: define \(f(\chi^{\varepsilon 2^j})=a^{\varepsilon 2^j}\); the relations \(2^{d_m}=1\) and, when applicable, \(2^{d_m/2}=-1\) modulo the appropriate root exponent make the definition unambiguous. Consequently an active \(H_m\)-orbit is equivalent to one choice of \(a\ne0\) with \(a^{E_m}=1\). No arbitrary independent Fourier values remain.

**3. Finite-field descent.** Fourier vectors correspond to elements with coefficients in \(\mathbb F_q\) precisely when
\[
 f(\chi^q)=f(\chi)^q
\]
for every character \(\chi\). This follows by applying Frobenius to the defining transform and, conversely, by inverse Fourier transformation and Frobenius-invariance. Since the Frobenius map \(\chi\mapsto\chi^q\) commutes with the signed-doubling action, an active orbit must be a whole \(L_m\)-orbit. The first power of Frobenius returning an \(H_m\)-orbit is \(q^{t_m}\), represented there by \(b_m=\pm2^j\); thus its root parameter additionally satisfies
\[
 a^{q^{t_m}}=a^{b_m}.
\]
Conversely, this single compatibility equation allows the parameter to propagate consistently along all the \(t_m\) Frobenius-translated \(H_m\)-orbits and enforces the descent relation everywhere. Therefore the allowed nonzero parameters are exactly the common roots of \(a^{E_m}=1\) and \(a^{q^{t_m}-b_m}=1\), namely the \(g_m\)-th roots of unity. In characteristic \(p\), this number equals \(g_m\): when \(p\ne2\), \(p\nmid b_m\) and hence \(p\nmid(q^{t_m}-b_m)\); when \(p=2\), \(E_m\) is odd. Thus \(p\nmid g_m\).

The choice of signed representative does not affect the count: the map \(\varepsilon2^j\mapsto\varepsilon2^j\pmod {E_m}\) factors through \(H_m\). Indeed \(2^{d_m}\equiv1\pmod{E_m}\), and if \(-1\in\langle2\rangle\pmod m\), then \(2^{d_m/2}\equiv-1\pmod{E_m}\). Any two representatives of the same element of \(H_m\) therefore agree modulo \(E_m\), giving the same gcd.

**4. Independent orbit enumeration.** An exact-order-\(m\) character has a free orbit under multiplication by \(L_m\), because \(c\chi=\chi\) implies \(c\equiv1\pmod m\). The number \(N_m\) of exact-order-\(m\) characters follows by Möbius inversion from \(|\widehat A[h]|=\prod_i\gcd(h,n_i)\). There are \(N_m/|L_m|\) independent orbits, each permitting either no support or one of \(g_m\) active values. The trivial character independently permits augmentation \(0\) or \(1\). Multiplication of these finite choices proves the bivariate polynomial and total count. Character inversion yields an actual element of \(K[A,*]\) for every selection, so there is neither overcounting nor an omitted polynomial equation.

**5. Representative calculations.** For \(m=11\), \(d_m=10\), \(E_m=33\), and \(H_m=(\mathbb Z/11\mathbb Z)^\times\). At \(q=2\), \(q^{t_m}=2\) and \(g_m=\gcd(33,0)=33\); at \(q=3\), \(q^{t_m}=3\equiv-8\pmod{11}\) and \(g_m=\gcd(33,11)=11\). Since there is one nontrivial \(L_m\)-orbit, this yields \(2(1+33)=68\) and \(2(1+11)=24\).

For \(m=17\), \(d_m=8\), \(E_m=17\), and \(|H_m|=8\). At \(q=2\), \(|L_m|=8\) and there are two orbits with \(g_m=17\), giving \(2(1+17)^2=648\). At \(q=3\), \(|L_m|=16\) merges the two orbits and \(g_m=17\), giving \(2(1+17)=36\).

## Verification

Run `python3 verify.py` in the directory containing this file. The dependency-free program computes the predicted cyclic-group count from the number-theoretic formula **and independently** enumerates all coefficient vectors in actual small finite-field quandle algebras, squares each vector by literal basis multiplication, and compares counts and augmentation classes. It tests \(17\) cyclic cases: sizes \(3,5,7,9,11,15\) with several fields, including \(\mathbb F_4\) and \(\mathbb F_8\) (implemented with irreducible binary-polynomial arithmetic). It also verifies directly that all \(512\) elements of \(\mathbb F_2[T(C_3\times C_3)]\) are idempotent, and evaluates the two size-\(17\) arithmetic examples. The final marker is `VERIFY_OK`. Finite enumerations corroborate, but do not prove, the assertions for every group and field; the proof above is unrestricted within its stated scope.

## Relationship to prior work

Narayanan and Panja (2022, arXiv:2206.10386) analyze integral dihedral-quandle idempotents, especially the five-element case. Elhamdadi, Nunez, and Singh (2022, arXiv:2207.09257) motivate idempotent-derived link-coloring enhancements and report particular quandle-ring computations. Elhamdadi, Ta, and Virgin (2026, arXiv:2609.03799) establish a Fourier framework for Alexander-quandle algebras, including the character equation and integral-coefficient rigidity for Takasaki quandles. The Fourier identity, character theory, and the characteristic-zero orbit decomposition are **not** claimed as new.

The distinct result here is the full **non-splitting finite-field** product: Frobenius fuses signed-doubling character orbits into \(L_m\)-orbits and restricts their root parameters from \(E_m\) to \(g_m\). A previously described complex-field signed-doubling orbit decomposition alone does not specify these rational-point counts; for the same quandle \(C_{11}\), characteristic two and three already give different numbers. A related modular-characteristic calculation for the three-element dihedral quandle is outside the present nonmodular hypotheses. Accessible published records were searched for direct or stronger coverage; no such result was confirmed, but a complete priority determination is not asserted.

## Limitations

The coefficient characteristic must not divide \(|A|\); the group must have odd order. This counts individual embedded idempotent **elements**, not their automorphism orbits or the associated knot/link invariants. The Fourier-support statistic is not the original-basis support size. No assertion is made for arbitrary Alexander parameters, nonabelian core quandles, even-order groups, or modular characteristic. The derivation uses elementary finite-field descent from established Fourier equations; a more general existing theorem might subsume it, and publication priority requires further external verification. There is no independent mathematical audit.

## References

- P. Narayanan and S. Panja, *Idempotents in integral ring of dihedral quandle*, arXiv:2206.10386, originally posted 2022-06-17, https://arxiv.org/abs/2206.10386.
- M. Elhamdadi, B. Nunez, and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257, 2022, https://arxiv.org/abs/2207.09257.
- M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799, 2026, especially Sections 3–4, https://arxiv.org/abs/2609.03799.
- B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, 2026, https://arxiv.org/abs/2608.01550.
