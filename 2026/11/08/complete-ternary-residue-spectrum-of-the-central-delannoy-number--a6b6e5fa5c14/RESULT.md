# Complete ternary residue spectrum of the central Delannoy numbers

## Finding
For every integer \(k\ge1\), write
\[
D_n=\sum_{j=0}^{n}\binom{n}{j}^{2}2^j,\qquad
V_k=\{D_n\bmod 3^k:n\ge0\}.
\]
Then
\[
\boxed{V_k=\{r\in\mathbb Z/3^k\mathbb Z:r\equiv0\text{ or }1\pmod3\}.}
\]
Each member of \(V_k\) is attained by infinitely many different indices. Consequently \(\lvert V_k\rvert=2\cdot3^{k-1}\). The closure of the integer sequence in the ring of 3-adic integers is exactly \(3\mathbb Z_3\cup(1+3\mathbb Z_3)\), of normalized Haar measure \(2/3\).

## Assumptions and scope
The only variable is the nonnegative integer index \(n\). The modulus is an arbitrary positive power of three; no index restriction is imposed. The result concerns attainable **values**, not their frequencies in an index period. We use the standard 3-adic valuation \(\nu_3\), with \(\nu_3(0)=+\infty\), the ordinary Legendre polynomial \(P_n\), and the Laurent-polynomial constant-term operator \(\operatorname{CT}\).

## Proof
**1. Excluded residue modulo three.** Put
\[
F(X)=3+X+2X^{-1},\qquad D_n=\operatorname{CT}F(X)^n=P_n(3).
\]
The constant-term identity follows by expanding \(3+X+2/X\) or by comparing the generating series \((1-6t+t^2)^{-1/2}\). In the ring of Laurent polynomials over \(\mathbb F_3\), \(F(X)^3=F(X^3)\). For \(n=3m+a\), \(a\in\{0,1,2\}\), the exponents of \(F(X)^a\) lie between \(-a\) and \(a\), while those of \(F(X^3)^m\) are multiples of three. Consequently
\[
D_{3m+a}\equiv D_mD_a\pmod3,
\]
where \(D_0=1\), \(D_1=3\), \(D_2=13\). Iteration over base-three digits proves \(D_n\equiv0\) or \(1\pmod3\) for every \(n\). The residue \(1\) occurs precisely when the base-three representation of \(n\) uses only digits zero and two.

**2. Sparse-block multiplication.** For any Laurent polynomials \(A,B\) over \(\mathbb Z\), the congruence \(A\equiv B\pmod3\) implies \(A^{3^e}\equiv B^{3^e}\pmod{3^{e+1}}\) for all \(e\ge0\), by induction using the binomial theorem. Freshman's dream therefore gives, for \(r\ge k-1\) and \(L=3^{r-k+1}\),
\[
F(X)^{2\cdot3^r}\equiv F(X^L)^{2\cdot3^{k-1}}\pmod{3^k}.
\]
Take any \(0\le a<L\). Since the exponents of \(F(X)^a\) lie strictly between \(-L\) and \(L\), only the two constant terms can contribute to the constant term of the product modulo \(3^k\). Thus
\[
\boxed{D_{a+2\cdot3^r}\equiv D_a c_k\pmod{3^k},\qquad c_k=D_{2\cdot3^{k-1}}\bmod3^k.}\tag{1}
\]
For any fixed \(a\), any integer \(j\ge0\), and arbitrarily large choices of successive exponents \(r_1<\cdots<r_j\), each chosen so that the previous index is below \(3^{r_i-k+1}\), repeated application of (1) constructs distinct indices \(N\) with
\[
D_N\equiv D_a c_k^j\pmod{3^k}.\tag{2}
\]
(The case \(j=0\) uses \(N=a\).)

**3. The multiplier generates all principal units.** When \(k\ge2\), applying (1) with target modulus nine and starting index zero yields
\[
c_k\equiv D_6=8989\equiv7\pmod9.
\]
Hence \(c_k\equiv1\pmod3\) but \(c_k\not\equiv1\pmod9\). The elementary lifting-the-exponent identity gives \(\nu_3(c_k^{3^s}-1)=1+s\) for any positive integer representative \(c_k\) and all \(s\ge0\). Its order modulo \(3^k\) is therefore \(3^{k-1}\), exactly the size of the group \(1+3\mathbb Z/3^k\mathbb Z\). For \(k=1\) that group is trivial. Thus all residues of fixed 3-adic valuation and fixed nonzero first ternary unit digit can be produced from a single seed by (2).

**4. Two seeds for each positive valuation.** We prove for all \(a\ge1\) that
\[
D_{3^{a-1}}\equiv3^a\pmod{3^{a+1}},\qquad
D_{3^a+1}\equiv-3^a\pmod{3^{a+1}}.\tag{3}
\]
The proof uses exact coefficient domination, not a finite experiment. Let \(Q_n(T)=2^nP_n(T)\). The classical Legendre expansion is
\[
Q_n(T)=\sum_{h=0}^{\lfloor n/2\rfloor}
\frac{(-1)^h(2n-2h)!}{h!(n-h)!(n-2h)!}\,T^{n-2h}.
\]
For even \(n=2m\), the constant coefficient is \((-1)^m\binom{2m}{m}\); for odd \(n=2m+1\), the coefficient of \(T\) is \((-1)^m2(2m+1)\binom{2m}{m}\). The quotient of each higher even-degree coefficient by the constant coefficient is an integer divided by the factorial of its even degree. Similarly, the quotient of each higher odd-degree coefficient by the coefficient of \(T\) is an integer divided by the factorial of its odd degree. For completeness, the even quotient for degree \(2h>0\) equals
\[
(-1)^h\frac{2^h\,\prod_{j=1}^h(2m+2j-1)\prod_{j=0}^{h-1}(m-j)}{(2h)!},
\]
and the odd quotient for degree \(2h+1>1\) is \( (-1)^h2^h\prod_{j=1}^h(2m+2j+1)\prod_{j=0}^{h-1}(m-j)/(2h+1)!\), also an integer divided by a factorial, after cancellation of the appropriate even numerator factors. Because \(\nu_3(t!)<t/2\) for any positive integer \(t\), evaluating at \(T=3\) makes every term beyond the lowest degree divisible by at least one additional power of three relative to the lowest term: for even degrees \(t=2h\), \(t-\nu_3(t!)\ge1\); for odd degrees \(t=2h+1\), the excess is \((t-1)-\nu_3(t!)\ge1\) when \(t\ge3\). All denominators \(2^n\) are 3-adic units. Hence the 3-adic valuation and first nonzero ternary digit of \(P_n(3)\) come from its lowest-degree Legendre term.

For the odd seed, set \(n=3^{a-1}\) and \(m=(n-1)/2\). Its lowest term is
\[
D_n\equiv (-1)^m2^{1-n}\,3n\binom{n-1}{m}\pmod{3^{a+1}}.
\]
Lucas' congruence gives \(\binom{3^{a-1}-1}{m}\equiv(-1)^m\pmod3\). Because \(n\) is odd, \(2^{1-n}\equiv1\pmod3\), giving the positive congruence in (3).

For the even seed take \(n=3^a+1=2m\) and \(j=m-1=(3^a-1)/2\). The lowest term is \((-1)^m2^{-n}\binom nm\). Since
\[
\frac1{3^a}\binom nm=\frac{3^a+1}{mj}\binom{3^a-1}{j-1},
\]
and \(j\equiv1\), \(m\equiv2\pmod3\), Lucas' congruence yields \(3^{-a}\binom nm\equiv(-1)^a\pmod3\). As \((-1)^m=(-1)^{a+1}\) and \(2^{-n}\equiv1\pmod3\), this gives the negative congruence in (3). In particular both seeds have exactly valuation \(a\).

**5. Exhaustion and infinite attainment.** Fix \(k\ge1\). For the unit classes (necessarily congruent to one modulo three), the seed \(D_0=1\) together with powers of the generator \(c_k\) supplies every such class. For each \(1\le a<k\), the two seeds from (3), multiplied by powers of \(c_k\) using (2), supply every class of exact valuation \(a\), with both possible first unit digits. A seed of valuation at least \(k\), for instance \(D_{3^{k-1}}\), supplies zero modulo \(3^k\). This exhausts exactly the classes congruent to zero or one modulo three. Replacing any exponent of \(c_k\) by that exponent plus an arbitrary positive multiple of its order, and choosing widely separated new blocks each time, gives infinitely many different indices for every target class. Compatibility across all \(k\) implies the asserted 3-adic closure, whose Haar measure is \(1/3+1/3=2/3\). \(\square\)

## Verification
Running the embedded standalone Python verifier confirms exact recurrence values through index 30000, comparison with the defining binomial sum for indices up to 100, full residue images modulo the first five powers of three, 201 separated-block congruences, the two normalized seed congruences through \(a=8\), generator checks through \(k=6\), and constructed image exhaustions through \(k=6\). A finite computation does **not** prove the statements for unrestricted \(k\); Steps 1–5 do.

## Relationship to prior work
Deutsch and Sagan [1], Theorem 5.15, determine the ternary base-digit pattern giving the residue modulo three. Sun [2] studies Delannoy congruences and sums, rather than this full higher-power value image. Krattenthaler and Müller [3], Section 13, give general algorithms and concrete \(3^k\)-congruences for Delannoy generating functions, but their inspected discussion does not explicitly give the uniform all-exponent value-image theorem above. Alekseyev, Amdeberhan, Shallit, and Vukusic [4] determine valuations of Legendre polynomials at primes. The OEIS records A088917 and A358360 capture the mod-three digit criterion and 3-adic valuations, respectively, but not the higher-power unit-image classification. The new ingredient here is the separated-block principal-unit generator and the two opposite-sign seeds, yielding exact surjectivity within every allowed 3-adic residue ball. Full historical priority is not certified.

## Limitations
This theorem concerns central Delannoy values at the prime three only. It does not determine frequency of residues within index intervals or periods, nor does it claim corresponding complete images for other primes or other Delannoy parameters. The 2010 Sun paper was available for its metadata and abstract but not inspected fully; an unlocated equivalent statement remains a residual priority risk. The analytic and coefficient arguments are self-contained above; the 2025 valuation paper is cited as related work rather than used as an unproved oracle.

## References
[1] E. Deutsch and B. Sagan, “Congruences for Catalan and Motzkin numbers and related sequences,” arXiv:math/0407326 (first public 2004-07-19), especially Theorems 5.9 and 5.15. https://arxiv.org/abs/math/0407326

[2] Z.-W. Sun, “On Delannoy numbers and Schröder numbers,” arXiv:1009.2486 (first public 2010-09-13); Journal of Number Theory 131 (2011), 2387–2397. https://arxiv.org/abs/1009.2486

[3] C. Krattenthaler and T. W. Müller, “A method for determining the mod-\(3^k\) behaviour of recursive sequences,” arXiv:1308.2856 (first public 2013-08-13), Section 13. https://arxiv.org/abs/1308.2856

[4] M. Alekseyev, T. Amdeberhan, J. Shallit, and I. Vukusic, “On the p-adic valuations of values of Legendre polynomials,” arXiv:2505.08935 (first public 2025-05-13). https://arxiv.org/abs/2505.08935
