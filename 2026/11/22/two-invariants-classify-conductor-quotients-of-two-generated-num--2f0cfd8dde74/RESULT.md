# Two invariants classify conductor quotients of two-generated numerical semigroups

## Finding
Let \(2\le a<b\) be coprime integers and let \(S_{a,b}=\langle a,b\rangle\subseteq\mathbb Z_{\ge0}\). Put \(c=(a-1)(b-1)\), its conductor. Define the **conductor Rees quotient** \(Q_{a,b}\) to have underlying set
\[
 (S_{a,b}\cap\{1,\ldots,c-1\})\cup\{\infty\},
\]
with \(\infty\) absorbing and \(x\oplus y=x+y\) when \(x+y<c\), or \(\infty\) otherwise. It has no adjoined identity. Define the **nilpotency class** \(\nu(Q)\) as the least positive integer \(k\) for which every product of \(k\) elements of \(Q\) is \(\infty\).

**Classification theorem.** For all such coprime pairs:
\[
 |Q_{a,b}|=\frac{(a-1)(b-1)}2,\qquad
 \nu(Q_{a,b})=\left\lceil\frac{(a-1)(b-1)}a\right\rceil.
\]
The pair \((|Q_{a,b}|,\nu(Q_{a,b}))\) determines the ordered integers \((a,b)\) uniquely among all coprime \(2\le a<b\). Consequently,
\[
 Q_{a,b}\cong Q_{a',b'}\quad\Longleftrightarrow\quad(a,b)=(a',b').
\]
In addition, the complete automorphism group is
\[
 \operatorname{Aut}(Q_{a,b})\cong
 \begin{cases}
 C_2,&a\ge3\text{ and }b=a+1,\\
 1,&\text{otherwise}.
 \end{cases}
\]
This establishes the two-generated case of the conductor-quotient rigidity conjecture formulated by Delgado and Fernandes; it does **not** settle their conjecture for arbitrary symmetric numerical semigroups.

## Assumptions and scope
The numerical semigroup \(S_{a,b}\) contains zero, but the finite nonabsorbing part of \(Q_{a,b}\) consists **only of positive** elements strictly below the conductor. The quotient identifies every positive semigroup element at least \(c\) with \(\infty\). In particular, \(Q_{2,3}\) consists solely of \(\infty\), and its nilpotency class is one. Coprimality and \(a<b\) are required; no characteristic, field, or asymptotic assumption occurs.

## Proof
**1. The two numerical invariants.** The two-generator Frobenius and symmetry formulas (Sylvester's theorem) give \(c=(a-1)(b-1)\) and exactly \(c/2\) elements of \(S_{a,b}\) in \(\{0,\ldots,c-1\}\). On deleting the additive identity \(0\) and inserting the absorbing element \(\infty\), the cardinality remains \(c/2\).

The smallest positive element of \(S_{a,b}\) is \(a\). Thus every sum of \(k\) positive elements is at least \(ka\), whereas \(k\) copies of \(a\) have sum exactly \(ka\). Therefore all length-\(k\) products in \(Q_{a,b}\) equal \(\infty\) if and only if \(ka\ge c\), giving \(\nu(Q_{a,b})=\lceil c/a\rceil\), including \((a,b)=(2,3)\).

**2. Strict reconstruction of the smaller generator.** Fix a possible conductor \(c\). Suppose there are two admissible smaller generators \(a<a'\) with larger companions \(b>a\) and \(b'>a'\), respectively, and with the same conductor. Since \(b'\ge a'+1\),
\[
 c=(a'-1)(b'-1)\ge a'(a'-1)\ge aa'.
\]
Hence
\[
 \frac ca-\frac c{a'}
 =\frac{c(a'-a)}{aa'}\ge a'-a\ge1.
\]
Taking ceilings yields \(\lceil c/a\rceil>\lceil c/a'\rceil\). Thus two different admissible smaller generators cannot produce the same nilpotency class at fixed conductor. Since \(c=2|Q|\), the pair of semigroup invariants uniquely recovers \(a\); then \(b=1+c/(a-1)\) is uniquely recovered. This proves the complete isomorphism classification.

**3. Indecomposables and automorphisms.** In any nilpotent semigroup, an isomorphism permutes its indecomposable nonzero elements; such elements are precisely its minimal generators. If \(a=2\), then \(c=b-1\le b\), so \(b\) is absent from the quotient and only powers of \(a\) survive; this quotient is monogenic (or the singleton \(Q_{2,3}\)) and is automorphism-rigid.

Now let \(a\ge3\). Then both \(a\) and \(b\) are below \(c\), and they are exactly the two indecomposables. Their individual nilpotency exponents are
\[
 \rho(b)=\left\lceil\frac cb\right\rceil=a-1,
 \qquad \rho(a)=\left\lceil\frac ca\right\rceil.
\]
If \(b\ge a+2\), then \(c=(a-1)(b-1)>a(a-1)\) and \(\rho(a)\ge a>\rho(b)\); hence an automorphism cannot exchange the generators. Fixing both generators fixes the entire quotient, so the automorphism group is trivial.

If \(b=a+1\), then \(c=a(a-1)\). Every positive word of total degree \(d\le a-2\) in \(a,b\) has integer sum at most \((a-2)(a+1)=c-2<c\), while every word of degree \(d\ge a-1\) has sum at least \((a-1)a=c\). Distinct monomials of degree at most \(a-2\) have distinct sums: any nontrivial integer relation between \(a\) and \(a+1\) would require at least \(a\) copies of one of them. Therefore the quotient is precisely the free commutative nilpotent semigroup on two generators, cut off at total degree \(a-1\). Generator interchange is an automorphism, and no other automorphisms are possible because all automorphisms permute the two indecomposables. This yields \(C_2\).

## Verification
The standalone Python 3 checker `verify.py` has no external dependencies. Run `python3 verify.py` in the directory containing that file. It independently constructs finite conductor quotients and their indecomposables, tests the cardinality and nilpotency formulas for 919 coprime pairs, detects any collision of the size/class invariants, and checks generator-swapping as an actual semigroup automorphism for 114 small pairs. It also tests the strict-ceiling inequality over all admissible smaller generators for conductors through 2000. `verification_output.txt` records the checked execution. These finite experiments only corroborate the separate infinite proof.

## Relationship to prior work
Delgado and Fernandes, *Rees quotients of numerical semigroups* (arXiv:1210.2910, first posted 9 October 2012), introduce these quotients; Remark 2.3 already gives the general conductor nilpotency class, while Theorem 4.9 and Corollary 4.10 give an algorithmic generator-permutation criterion for isomorphisms and automorphisms. Section 6.3 observes small-conductor coincidences by cardinality and nilpotency class and formulates Conjecture 6.2 on distinct symmetric numerical semigroups. The formulas for conductor, genus, and nilpotency used here are **prior results**, not new claims. The result asserted here is the uniform strict-reconstruction argument and exact two-generator classification, together with the explicit exceptional automorphism family.

An indexed result titled *Rigidity and a forbidden near-maximal type for two-generator numerical-semigroup quotients* treats the different construction \(\{n:pn\in\langle a,b\rangle\}\) and its pseudo-Frobenius type, not a conductor Rees quotient; its complete public `RESULT.md` was inspected to exclude an ambiguity in the word *quotient*. García-García and Moreno-Frías (2012) study algorithms for morphisms of finitely generated commutative monoids; only their abstract was accessible, and it remains a limited-access historical risk.

## Limitations
Only conductor-cutoff quotients of **two-generated** coprime numerical semigroups are covered. Other cutting points, general numerical semigroups, and the full symmetric-semigroup conjecture are not addressed. The automorphism classification concerns semigroup automorphisms, not endomorphisms or automorphisms of the numerical semigroup itself. Search and accessible full-text comparison cannot establish absolute historical priority; no independent mathematical audit has been performed.

## References
1. M. Delgado and V. H. Fernandes, *Rees quotients of numerical semigroups*, arXiv:1210.2910v1 (9 October 2012), subsequently *Portugaliae Mathematica* **70** (2013), 93–112, DOI:10.4171/PM/1927. Especially Remark 2.3, Theorem 4.9, Corollary 4.10, and Conjecture 6.2. https://arxiv.org/abs/1210.2910
2. J. I. García-García and M. Á. Moreno-Frías, *On morphisms of commutative monoids*, *Semigroup Forum* **84** (2012), 333–341, DOI:10.1007/s00233-011-9349-z. Only abstract accessible. https://rodin.uca.es/xmlui/handle/10498/35537
3. *Rigidity and a forbidden near-maximal type for two-generator numerical-semigroup quotients* (2026), published `RESULT.md`: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-rigidity-and-a-forbidden-near-maximal-type-for-two-generator-num--e5140886fb31/RESULT.md
