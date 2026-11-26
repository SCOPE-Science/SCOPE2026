# The sharp five-prime-support bound for the totient of Dedekind's function

## Finding

**Theorem.** Let \(\varphi\) denote Euler's totient and \(\psi\) Dedekind's arithmetic function. For every integer \(n\ge3\) with at most five distinct prime factors,
\[
\frac{\varphi(\psi(n))}{n}\le\frac{384}{385}.
\]
Equality holds **exactly** for
\[
n=2^a3^b\cdot5\cdot7\cdot11\quad(a,b\ge1\text{ integers}).
\]
Thus \(\varphi(\psi(n))<n\) holds for every \(n>2\) with \(\omega(n)\le5\). This threshold is sharp: \(39270=2\cdot3\cdot5\cdot7\cdot11\cdot17\) has six distinct prime factors and \(\varphi(\psi(39270))=41472>39270\). For the excluded boundary \(n=2\), equality \(\varphi(\psi(2))=2\) holds.

## Assumptions and scope

For every positive integer \(n\), define
\[
\psi(n)=n\prod_{p\mid n}\left(1+\frac1p\right),\qquad
\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right).
\]
The products run over **distinct** prime divisors, and \(\omega(n)\) counts those primes. There is no bound on prime exponents, on the size of \(n\), or on the number of digits in \(n\). The conclusion is a uniform upper bound for \(n\ge3\) with \(\omega(n)\le5\); it does not concern arbitrary numbers with six or more distinct prime factors.

## Proof

For every positive \(m\), the exact totient formula gives
\[
2\mid m\Longrightarrow\frac{\varphi(m)}m\le\frac12,\qquad
6\mid m\Longrightarrow\frac{\varphi(m)}m\le\frac13.
\]
In the second implication, equality occurs precisely when every prime factor of \(m\) is in \(\{2,3\}\). Each factor \((1+1/p)\) strictly decreases with \(p\), so for a fixed bound on \(\omega(n)\) the largest \(\psi(n)/n\) is obtained by choosing the smallest permitted distinct prime factors.

**Case 1: \(n\) is even with at least two distinct prime factors.** A factor \(2^a\Vert n\) contributes \(\psi(2^a)=3\cdot2^{a-1}\), divisible by \(3\); any odd prime-power factor \(p^b\Vert n\) contributes \(p^{b-1}(p+1)\), divisible by \(2\). Multiplicativity therefore implies \(6\mid\psi(n)\). Because \(\omega(n)\le5\),
\[
\frac{\psi(n)}n
=\prod_{p\mid n}\left(1+\frac1p\right)
\le\frac32\frac43\frac65\frac87\frac{12}{11}
=\frac{1152}{385}.
\]
Consequently
\[
\frac{\varphi(\psi(n))}{n}
=\frac{\varphi(\psi(n))}{\psi(n)}\frac{\psi(n)}n
\le\frac13\frac{1152}{385}=\frac{384}{385}.
\]
Equality in the product bound requires exactly the prime support \(\{2,3,5,7,11\}\), because each factor strictly decreases with its prime. Equality in the totient bound additionally requires that \(\psi(n)\) have no prime divisor other than \(2\) or \(3\). If one of the exponents on \(5,7,11\) were at least \(2\), then that prime would divide \(\psi(n)\), so all three exponents must be \(1\). Conversely, for arbitrary positive \(a,b\),
\[
\psi(2^a3^b\cdot5\cdot7\cdot11)
=(3\cdot2^{a-1})(4\cdot3^{b-1})(6)(8)(12)
=2^{a+7}3^{b+2}.
\]
It follows that
\[
\frac{\varphi(\psi(2^a3^b\cdot5\cdot7\cdot11))}{2^a3^b\cdot5\cdot7\cdot11}
=\frac{2^{a+7}3^{b+1}}{2^a3^b\cdot385}=\frac{384}{385}.
\]
This proves both the upper bound and its exact equality class in this case.

**Case 2: \(n\) is an even prime power.** Write \(n=2^a\); since \(n\ge3\), \(a\ge2\). Then \(\psi(n)=3\cdot2^{a-1}\) and \(\varphi(\psi(n))/n=1/2<384/385\).

**Case 3: \(n\) is odd and \(3\mid\psi(n)\).** Because each odd prime-power contribution to \(\psi(n)\) is even, \(6\mid\psi(n)\). The five smallest possible odd prime divisors are \(3,5,7,11,13\), so
\[
\frac{\varphi(\psi(n))}n
\le\frac13\frac43\frac65\frac87\frac{12}{11}\frac{14}{13}
=\frac{512}{715}<\frac{384}{385}.
\]

**Case 4: \(n\) is odd and \(3\nmid\psi(n)\).** No prime \(p\equiv2\pmod3\) divides \(n\), since \(3\mid p+1\mid\psi(n)\) would follow. Thus every prime divisor of \(n\) is \(3\) or congruent to \(1\) modulo \(3\). The five smallest eligible primes are \(3,7,13,19,31\). Because \(\psi(n)\) is even,
\[
\frac{\varphi(\psi(n))}{n}
\le\frac12\frac43\frac87\frac{14}{13}\frac{20}{19}\frac{32}{31}
=\frac{20480}{22971}<\frac{384}{385}.
\]
All integers in the stated domain fall into one of these four cases. Finally, direct multiplicativity gives \(\psi(39270)=124416=2^9 3^5\) and \(\varphi(124416)=41472>39270\), establishing sharpness of the five-prime-support restriction. This completes the proof.

## Verification

A standalone, dependency-free Python program, `verify_sandor_support.py`, implements exact sieves for the smallest prime factor, Dedekind's function, Euler's totient and distinct-prime-factor count. It verifies the scaled integer inequality \(385\varphi(\psi(n))\le384n\) and the complete prescribed equality pattern for every \(3\le n\le300000\) with \(\omega(n)\le5\). It separately finds the least positive violation of \(\varphi(\psi(n))\le n\) through this limit and checks the explicit values at \(n=2,2310,39270\). All arithmetic is integral: no floating-point comparisons occur. The bound-free result rests on the four-case proof above, not on the finite search.

## Relationship to prior work

Sándor's 2005 paper formulated the inequality \(\varphi(\psi(n))\le n\) and, in Remark 3.10, showed it for even integers with at most two distinct prime factors and odd integers with at most four. Its Theorem 3.9 uses the sufficient hypothesis \(\psi(n)\le2n\). This hypothesis does not handle the present extremal family: at \(2310\), \(\psi(n)/n=1152/385>2\). Remark 3.26 lists \(39270\) among counterexamples, but does not prove that six is the least possible number of distinct prime factors among counterexamples or give the sharp five-prime-support ratio and equality classification. The 2012-12-21-dated OEIS A196200 records numerical counterexamples and the same seed equation, not the claimed infinite classification. Sándor's 2016 note concerns other multiplicative inequalities for \(\psi\), and its theorems do not bound \(\varphi(\psi(n))/n\) for fixed prime support. No assertion of global literature completeness is made.

## Limitations

This theorem controls at most five distinct prime factors; it gives no bound of this strength on six-prime-support integers. In particular it does not settle which larger integers violate the original Sándor inequality, nor their infinitude or density. The program checks only a finite interval, and cannot by itself certify an infinite theorem. Earlier literature not indexed or accessible in the inspected corpus could contain equivalent arguments. For historical dating, the 2005 paper predates the day-stamped 2012 OEIS record, but its exact first day of public availability was not established; the dated source attribution must not be interpreted as claiming first discovery of the subject in 2012.

## References

1. J. Sándor, “On the Composition of Some Arithmetic Functions, II,” *Journal of Inequalities in Pure and Applied Mathematics* **6** (2005), no. 3, Article 73, especially Theorem 3.9, Remark 3.10, Theorem 3.23, Remark 3.26. Full text: https://www.maths.tcd.ie/EMIS/journals/JIPAM/images/146_05_JIPAM/146_05.pdf
2. OEIS Foundation, A196200, “Numbers k such that Euler phi(Dedekind psi(k)) > k,” initial dated record 2012-12-21: https://oeis.org/A196200
3. J. Sándor, “A note on Dedekind's arithmetical function,” *Notes on Number Theory and Discrete Mathematics* **22** (2016), no. 1, 5–7: https://nntdm.net/papers/nntdm-22/NNTDM-22-1-05-07.pdf
