# One elliptic trace controls cyclotomic quadratic-sign triples and their sharp prime-power threshold

## Finding

Let \(q\) be an odd prime power, let \(\mathbb F_q\) be its finite field, and let \(\chi_q:\mathbb F_q\to\{-1,0,1\}\) be the quadratic character with \(\chi_q(0)=0\). For a sign triple \((a,b,c)\in\{-1,1\}^3\), put
\[
N_q(a,b,c)=\#\{x\in\mathbb F_q:\big(\chi_q(x),\chi_q(x+1),\chi_q(x^2+x+1)\big)=(a,b,c)\}.
\]
In characteristic different from \(3\), define
\[
U_q=\sum_{x\in\mathbb F_q}\chi_q(x^3+x^2+x),\qquad
r_q=\begin{cases}2,&q\equiv1\pmod3,\\0,&q\equiv2\pmod3.\end{cases}
\]
The *entire* eight-entry sign histogram is determined by the one elliptic trace \(U_q\), as follows.

If \(q\equiv1\pmod4\), then for each \(c\in\{-1,1\}\),
\[
\begin{aligned}
8N_q(1,1,c)&=q-5-6c-4r_q+3cU_q,\\
8N_q(1,-1,c)=8N_q(-1,1,c)=8N_q(-1,-1,c)&=q-1-2c-cU_q.
\end{aligned}
\]
If \(q\equiv3\pmod4\), then
\[
\begin{aligned}
8N_q(1,-1,c)&=q+1-4r_q+3cU_q,\\
8N_q(1,1,c)=8N_q(-1,1,c)=8N_q(-1,-1,c)&=q-3-4c-cU_q.
\end{aligned}
\]
For every odd prime power of characteristic at least \(5\), all eight triples occur if and only if
\[
q\notin\{5,7,11,13,17,19,23,25,29,31,37,49\}.
\]
Consequently the sharp universal prime-field cutoff is \(41\), and the sharp universal prime-power cutoff within characteristics at least \(5\) is \(53\). The field of order \(49\) misses exactly \((1,1,-1)\), although the prime fields of orders \(41\), \(43\), and \(47\) realize all eight triples. In characteristic \(3\), the third character is never \(-1\), so universality fails at every extension degree.

## Assumptions and scope

All counts concern \(x\in\mathbb F_q\), not integers restricted to an interval; a zero character is excluded from every displayed sign triple. The exact histogram holds for *every* odd prime power of characteristic at least \(5\), including extension fields. The classification of all-eight-pattern existence covers every odd prime power, with the separate characteristic-\(3\) obstruction. No assertion about characteristic \(2\) is made. The integer \(r_q\) counts the distinct roots of the third cyclotomic polynomial \(h(X)=X^2+X+1\) in \(\mathbb F_q\).

## Proof

**1. Two transformations collapse the higher-degree sums.** Write \(\chi=\chi_q\), \(h(x)=x^2+x+1\), and \(\delta=\chi(-1)\). Set
\[
V=\sum_x\chi((x+1)h(x)),\qquad W=\sum_x\chi(x(x+1)h(x)).
\]
The reflection \(x\mapsto-1-x\) fixes \(h(x)\) and transforms \(xh(x)\) into \(-(x+1)h(x)\), so \(V=\delta U_q\). The fractional linear transformation \(T(x)=-x/(x+1)\) permutes \(\mathbb F_q\setminus\{-1\}\) and satisfies
\[
h(T(x))=\frac{h(x)}{(x+1)^2},\qquad
\chi(T(x)h(T(x)))=\delta\chi(x(x+1)h(x)).
\]
The missing term in \(\sum_x\chi(xh(x))\) at \(x=-1\) equals \(\delta\); the missing term in \(W\) vanishes. Hence \(U_q-\delta=\delta W\), or
\[
\boxed{V=\delta U_q,\qquad W=\delta U_q-1.}
\]
This gives a genuinely one-trace formula rather than three independent character sums.

**2. Expand the eight indicators, correcting zeros.** Since the characteristic is at least \(5\), both \(h(x)\) and \(x(x+1)\) are separable monic quadratics, so
\[
\sum_x\chi(h(x))=\sum_x\chi(x(x+1))=-1,
\qquad \sum_x\chi(x)=\sum_x\chi(x+1)=0.
\]
For a fixed \((a,b,c)\), first sum the product \((1+a\chi(x))(1+b\chi(x+1))(1+c\chi(h(x)))\) over all \(x\). By the character-sum identities its value is
\[
q-ab-c-abc+c(a+\delta b+\delta ab)U_q.
\]
For an admissible \(x\) this product is \(8\) if its three signs match and \(0\) otherwise. At a zero of one of the three polynomials it need not be zero, so the extraneous total must be subtracted. The zeros \(x=0\) and \(x=-1\) contribute respectively \((1+b)(1+c)\) and \((1+a\delta)(1+c)\). Every root of \(h\) is a nontrivial cube root of unity; because \(q\) is odd, it is a square and its successor has quadratic character \(\delta\). There are \(r_q\) such roots, contributing \(r_q(1+a)(1+b\delta)\). Therefore
\[
\boxed{\begin{aligned}
8N_q(a,b,c)={}&q-ab-c-abc+c(a+\delta b+\delta ab)U_q\\
&-(1+b)(1+c)-(1+a\delta)(1+c)\\
&-r_q(1+a)(1+b\delta).
\end{aligned}}
\]
For \(\delta=1\), the coefficient \(a+b+ab\) equals \(3\) only for \((a,b)=(1,1)\), and equals \(-1\) on the other three pairs. For \(\delta=-1\), the coefficient \(a-b-ab\) equals \(3\) only for \((a,b)=(1,-1)\), and equals \(-1\) otherwise. Simplifying the displayed identity yields the claimed two threefold-equality formulas. Equivalently, the projective involutions \(x\mapsto1/x\) and \(x\mapsto-1-x\) act on the admissible sign pairs by \((a,b)\mapsto(a,ab)\) and \((a,b)\mapsto(\delta b,\delta a)\), giving one singleton orbit and one three-element orbit for each \(c\).

**3. Prove the infinite tail.** The smooth elliptic curve
\[
E:\quad y^2=x^3+x^2+x
\]
has \(q+1+U_q\) rational points over \(\mathbb F_q\). Its cubic has distinct roots because \(\operatorname{char}\mathbb F_q\ne3\); Hasse's inequality therefore gives \(|U_q|\le2\sqrt q\). When \(q\equiv1\pmod4\), the lowest possible singleton numerator is at least \(q-19-6\sqrt q\); when \(q\equiv3\pmod4\), it is at least \(q-7-6\sqrt q\). The threefold-orbit numerators are respectively bounded below by \(q-3-2\sqrt q\) and \(q-7-2\sqrt q\) for \(c=1\), and by \(q+1-2\sqrt q\) for \(c=-1\). Every one of these lower bounds is strictly positive when \(q\ge71\). Thus all eight signs occur at every prime-power order \(q\ge71\) of characteristic at least \(5\).

**4. Exhaust the finite remainder.** The only prime-power orders below \(71\) in characteristics at least \(5\) are the primes \(5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67\) and the extension-field orders \(25,49\). These nineteen cases are enumerated in `finite_cases.json` by the exact-arithmetic standard-library program `verify.py`. In each prime field the quadratic character is independently obtained by Euler's criterion and enumeration of nonzero squares; in both quadratic extension fields it is independently obtained from the norm character and the explicit square set. Each of the eight counts is independently checked against the theorem's formula. The twelve exceptional orders are precisely those stated in the Finding, and all other eligible orders below \(71\) realize every sign word. In particular \(49\) fails and \(53\) succeeds. The exceptional characteristic \(3\) follows directly from \(x^2+x+1=(x-1)^2\) there.

## Verification

Run `python3 verify.py` in the directory containing the packaged `verify.py` and `finite_cases.json`; it writes the finite-case certificate deterministically and checks all nineteen eligible fields below \(71\), plus \(\mathbb F_3\) as a separate boundary and seventy-six additional prime fields between \(71\) and \(499\). Its square-set versus Euler and norm comparisons independently test the finite characters, and its direct histogram versus trace-formula comparisons test every stated finite instance. The checker does not replace the infinite Hasse-bound argument in Step 3. The complete eight-count histograms, missing sign words, and traces of the small fields are in `finite_cases.json`.

## Relationship to prior work

Wang and Fang (2023) analyze arithmetic progressions of quadratic-residue signs, particularly three-term progressions with fixed steps and longer consecutive strings. Their full text does not treat the triple \((x,x+1,x^2+x+1)\), the associated fractional-linear symmetry, its one-elliptic-trace census, or the exact extension-field exceptions. McDonald, Sahay and Wyman (2022) give general asymptotic existence results for quadratic-residue shattering using Weil bounds, rather than an exact fixed cyclotomic triple histogram. General character-sum and elliptic-curve point-count estimates are established tools and are not asserted as new here. The new point of this classification is that the cyclotomic relation makes the apparent quartic trace equal to a cubic trace, reduces eight counts to two orbits per last sign, and yields the complete sharp finite-field exception list.

## Limitations

The displayed exact formulas apply only in odd characteristic at least \(5\). In characteristic \(3\) only the failure of eight-pattern universality is asserted, not a complete histogram. The priority comparison is based on accessible literature and mathematical-record searches, not on an exhaustive survey of every unpublished note or textbook exercise. In particular an equivalent character-sum formula in older elliptic-curve literature remains a residual possibility. No independent mathematical audit has been performed.

## References

1. X. Wang and H. Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, Journal of Mathematics, published online 2023-10-03, DOI: https://doi.org/10.1155/2023/5253261 (full article inspected).
2. B. McDonald, A. Sahay and E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, first public arXiv version 2022-10-07, https://arxiv.org/abs/2210.03789 (abstract and bibliographic material inspected; general background, not a same-object coverage claim).
