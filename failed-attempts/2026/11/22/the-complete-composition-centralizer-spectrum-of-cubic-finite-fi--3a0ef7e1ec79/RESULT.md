# The complete composition-centralizer spectrum of cubic finite-field jets

## Finding
Let \(q=p^d\) be any prime power, \(k=\mathbb F_q\), and \(R=k[t]/(t^4)\). Let \(M=\operatorname{End}_{k\text{-alg}}(R)\), where endomorphisms preserve \(1\) and fix \(k\) pointwise. Denote by \(C_M(f)=\{g\in M:fg=gf\}\) the **composition** centralizer, and put
\[
Z_q(z)=\sum_{f\in M}z^{|C_M(f)|}.
\]
This is a complete multiplicity distribution, not merely a commuting probability.

**Theorem.** In characteristic \(2\),
\[
Z_q(z)=(q-2)q^2z^q+2(q^2-1)z^{2q^2}+2z^{q^3}.
\]
In odd characteristic,
\[
\begin{split}
Z_q(z)={}&(q-3)q^2z^q+(q^2-q)z^{3q}+qz^{q^2}\\
&+2q(q-1)z^{q^2+q}+2(q-1)z^{3q^2}+2z^{q^3}.
\end{split}
\]
Terms with equal exponents must be added, as happens for \(q=2\) or \(q=3\). In particular, the number \(\kappa_q\) of **ordered** commuting pairs is
\[
\boxed{\kappa_q=\begin{cases}5q^4-4q^2,&p=2,\\3q^4+9q^3-11q^2,&p\ne2.\end{cases}}
\]
The center \(Z(M)=\{f: C_M(f)=M\}\) has cardinality \(8\) when \(q=2\), \(6\) when \(q=3\), and \(2\) when \(q>3\). Therefore the commuting probability is \(\kappa_q/q^6\); it has leading constants \(5\) in characteristic two and \(3\) in odd characteristic as the field grows.

## Assumptions and scope
The assertion holds for all finite fields, including nonprime extension fields and characteristics \(2\) and \(3\). Endomorphisms are unital \(k\)-algebra homomorphisms, **not** arbitrary ring maps allowed to apply a Frobenius automorphism to coefficients. Composition is the semigroup multiplication, rather than multiplication of elements in the commutative ring \(R\). A map is specified uniquely by
\[
f(t)=at+bt^2+ct^3,\quad (a,b,c)\in k^3,
\]
because all nilpotent elements of \(R\) lie in \((t)\), and every such choice satisfies \(f(t)^4=0\). Hence \(|M|=q^3\). An endomorphism is invertible if and only if \(a\ne0\), but no invertibility condition is imposed in the count.

## Proof
**1. Composition equations.** Let \(f(t)=at+bt^2+ct^3\) and \(g(t)=ut+vt^2+wt^3\). We use \(f\circ g\) for formal composition of these substitution polynomials. This is opposite to the order of composition of their induced algebra endomorphisms, but the equation that the two maps commute is unchanged by reversing both sides. Directly expanding the substitution polynomials modulo \(t^4\) gives
\[
(f\circ g)(t)=au t+(av+bu^2)t^2+(aw+2buv+cu^3)t^3.
\]
Interchanging \(f\) and \(g\) shows \(fg=gf\) if and only if
\[
(a-a^2)v=(u-u^2)b,\tag{1}
\]
\[
(a-a^3)w-(u-u^3)c+2bv(u-a)=0.\tag{2}
\]
These are identities over \(k\); the coefficient \(2\) is reduced in the field.

**2. Odd characteristic.** First suppose \(a\notin\{0,1,-1\}\). Both \(a-a^2\) and \(a-a^3\) are nonzero. Given \(u\in k\), equation (1) determines \(v\) uniquely and then (2) determines \(w\) uniquely. Thus \(|C_M(f)|=q\), and the number of such \(f\) is \((q-3)q^2\).

For \(a=-1\), equation (1) forces \(v=-b(u-u^2)/2\). Equation (2) then becomes
\[
(u-u^3)(c+b^2)=0,\tag{3}
\]
and \(w\) is free. If \(c=-b^2\), all \(q\) values of \(u\) work, giving \(|C_M(f)|=q^2\), for exactly \(q\) such \(f\). Otherwise \(u\in\{0,1,-1\}\), giving \(|C_M(f)|=3q\), for exactly \(q(q-1)\) maps.

For \(a\in\{0,1\}\), equation (1) is \((u-u^2)b=0\). If \(b\ne0\), then \(u\in\{0,1\}\). At \(u=a\), equation (2) imposes no condition on \(v\), and \(v,w\) vary freely, producing \(q^2\) maps. At the other root, equation (2) reduces to \(2b(u-a)v=0\), so \(v=0\) and \(w\) is free, producing \(q\). Thus \(|C_M(f)|=q^2+q\) for \(2q(q-1)\) choices of \(f\). If \(b=0,c\ne0\), equation (2) requires \(u^3=u\), whose three roots are \(0,1,-1\); both \(v,w\) are arbitrary, so \(|C_M(f)|=3q^2\), for \(2(q-1)\) maps. If \(b=c=0\), both equations vanish for every \((u,v,w)\), so \(|C_M(f)|=q^3\), for two maps. These are all \(q^3\) elements and give the odd-characteristic polynomial.

**3. Characteristic two.** When \(a\notin\{0,1\}\), again \(a-a^2\) and \(a-a^3\) are nonzero (\(a^3=a\) only at \(a=0,1\)), yielding one \((v,w)\) for each \(u\), so \(|C_M(f)|=q\) for \((q-2)q^2\) maps. For \(a\in\{0,1\}\), equations (1),(2) simplify to
\[
(u-u^2)b=0,\qquad(u-u^3)c=0.
\]
When \((b,c)\ne(0,0)\), their common solutions are exactly \(u=0,1\); the coefficients \(v,w\) are arbitrary and \(|C_M(f)|=2q^2\) for \(2(q^2-1)\) maps. When \(b=c=0\), all \(q^3\) maps commute with \(f\), accounting for two more elements.

**4. Aggregate and center.** Summing each histogram's centralizer cardinalities (equivalently differentiating \(Z_q(z)\) at \(z=1\)) gives the displayed \(\kappa_q\). Since \(|M|=q^3\), the central elements are precisely the coefficients of \(z^{q^3}\) after merging coincident exponents. In characteristic two, \(2q^2=q^3\) exactly when \(q=2\), so the center then has \(2(q^2-1)+2=8\) elements, otherwise two. In odd characteristic, \(3q^2=q^3\) exactly when \(q=3\), giving \(2(q-1)+2=6\) central maps; all other odd prime powers have center of order two. This proves all assertions.

## Verification
The attached `verification/jet4_check.py` computes finite-field operations directly, including polynomial-basis extension fields, and checks every ordered pair of the \(q^3\) endomorphisms. The complete centralizer histograms and pair counts agree with the theorem for \(q=2,3,4,5,7,8,9\). The checks exercise the small-field exponent collisions and both prime and extension fields; they are **finite corroboration**, not a substitute for the preceding field-uniform proof. Reproduce with `python verification/jet4_check.py` (Python 3 standard library only). The record `verification/finite_checks.json` contains the exact expected counts and tested fields.

## Relationship to prior work
Finite chain rings form the general algebraic setting of Alkhamees and Alhajouj (2022), who study matrix presentations of such rings rather than composition centralizers. Alabiad and Alkhamees (2021) study automorphism **groups** of finite chain rings; invertible maps alone form only a proper subset of the endomorphism monoid. A published result entitled *Conjugacy and centralizer spectra of finite fourth-order substitution groups* concerns the invertible substitution group of the **longer** quotient \(k[t]/(t^5)\) in characteristic at least five. That group result does not, as stated, determine centralizers taken in the **full endomorphism monoid** of \(k[t]/(t^4)\), especially the singular substitutions and small characteristics. Published truncated-polynomial derivation-centralizer results instead concern the Lie bracket of derivations, not composition of unital algebra endomorphisms. These distinctions justify the specific comparison; they do **not** establish historical uniqueness.

## Limitations
The theorem concerns precisely truncation length four, fixed coefficient fields, and ordered commuting pairs. It does not establish an all-truncation enumeration, simultaneous commutation of triples, or full conjugacy classification. Published-source overlap is assessed from accessible original full text and bibliographic descriptions of directly related results; the full text of a plausible substitution-group predecessor was not accessible during this review. Consequently earlier broader monoid work may still imply this statement. Independent validation has not been performed.

## References
1. Y. Alkhamees and B. Alhajouj, *Structure of a chain ring as a ring of matrices over a Galois ring*, AIMS Mathematics **7** (2022), 15824–15833. Published 2022-06-27; primary MSC 16L30. DOI: `10.3934/math.2022866`. https://www.aimspress.com/aimspress-data/math/2022/9/PDF/math-07-09-866.pdf
2. S. Alabiad and Y. Alkhamees, *On Automorphism Groups of Finite Chain Rings*, Symmetry **13** (2021), article 681, published 2021-04-14. https://doi.org/10.3390/sym13040681
3. *Conjugacy and centralizer spectra of finite fourth-order substitution groups*, published mathematical record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-conjugacy-and-centralizer-spectra-of-finite-fourth-order-substit--21c11f1dc6ee
4. *Adjoint-centralizer spectra and a characteristic-two parity isomorphism for truncated polynomial derivations*, published mathematical record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-adjoint-centralizer-spectra-and-a-characteristic-two-parity-isom--a51032612a86
