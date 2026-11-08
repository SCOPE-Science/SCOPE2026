# Complete three-prime classification of exponential-unitary perfect integers

## Finding
For an integer \(n=\prod_i p_i^{a_i}>1\), define its exponential-unitary divisor sum by
\[
\sigma^{(e)*}(n)=\prod_i\sum_{\substack{d\mid a_i\\\gcd(d,a_i/d)=1}}p_i^d.
\]
Call \(n\) *exponential-unitary perfect* when \(\sigma^{(e)*}(n)=2n\), and let \(\omega(n)\) denote the number of distinct prime divisors.

**Theorem.** For every integer \(n>1\) with \(\omega(n)\le3\),
\[
\sigma^{(e)*}(n)=2n
\quad\Longleftrightarrow\quad
n=36,\quad\text{or}\quad n=36q\ (q\ge5\text{ prime}),\quad\text{or}\quad n\in\{1800,2700\}.
\]
In particular, the only *squarefull* (all prime exponents at least two) exponential-unitary perfect integers with exactly three distinct prime factors are \(1800=2^3 3^2 5^2\) and \(2700=2^2 3^3 5^2\). Every exponential-unitary perfect integer with at most three distinct prime factors is also exponential-perfect (its ordinary exponential-divisor sum equals twice the integer). Any counterexample to the e-unitary/e-perfect equivalence question therefore has at least four distinct prime factors.

## Assumptions and scope
All primes are positive ordinary rational primes, all prime-power exponents are positive integers, and the local condition \(d\mid a\) includes \(d=a\). The convention for a prime appearing with exponent one is \(\sigma^{(e)*}(p)=p\). "Squarefull" means every positive prime exponent is at least two. No assertion is made for integers having four or more distinct prime factors, except the stated necessary condition on hypothetical counterexamples.

Write
\[
R_p(a)=p^{-a}\!\sum_{\substack{d\mid a\\\gcd(d,a/d)=1}}p^d.
\]
Then \(\sigma^{(e)*}(n)/n=\prod_{p^a\parallel n}R_p(a)\); in particular \(R_p(1)=1\).

## Proof
**1. Local upper bound.** If \(a\ge2\), the unitary divisors of \(a\) include \(a\) and \(1\). Every other proper unitary divisor is at most \(\lfloor a/2\rfloor\). Define
\[
S_p(a)=\sum_{d=1}^{\lfloor a/2\rfloor}p^{d-a}.
\]
For \(a\ge3\), \(R_p(a)\le1+S_p(a)\), and direct reindexing gives
\[
S_p(a+2)=p^{-1}S_p(a)+p^{-(a+1)}<S_p(a).
\]
The last inequality follows from \(S_p(a)\ge p^{1-a}\) and \((1-p^{-1})p^{1-a}>p^{-(a+1)}\) for every integer \(p\ge2\). Thus \(S_p(a)\) decreases along each parity progression. Its two initial values are \(S_p(3)=p^{-2}\) and \(S_p(4)=p^{-2}+p^{-3}<p^{-1}\). Hence
\[
1<R_p(a)\le1+\frac1p\qquad(a\ge2),
\]
with equality **only** at \(a=2\) (where the unitary divisors are \(1,2\)). For \(a\ge3\) the inequality is strict.

Two strengthened estimates will be used. For \(a=4\) and \(a=5\), the only unitary divisors are \(1,a\), so \(R_2(4)=9/8\) and \(R_2(5)=17/16\). For even \(a\ge6\), the envelope is at most \(1+S_2(6)=39/32\), while for odd \(a\ge7\) it is at most \(1+S_2(7)=71/64\). Consequently,
\[
R_2(a)\le\frac{39}{32}\quad(a\ge4).
\]
For \(b=3\), \(R_3(3)=10/9\); for \(b=4\), \(R_3(4)=28/27<10/9\). For odd \(b\ge5\), the envelope is at most \(1+S_3(5)=1+4/81\); for even \(b\ge6\) it is at most \(1+S_3(6)=1+13/243\). Therefore
\[
R_3(b)\le\frac{10}{9}\quad(b\ge3),
\]
with equality only when \(b=3\).

**2. Remove primes of exponent one.** Factor uniquely \(n=cm\), where \(c\) is the product of all prime-power factors occurring to exponent at least two, and \(m\) is the product of the remaining primes. Then \(m\) is squarefree and coprime to \(c\), and \(\sigma^{(e)*}(n)=m\sigma^{(e)*}(c)\). Hence \(n\) is exponential-unitary perfect if and only if \(c\) is. If \(c=1\) this is impossible, and if \(c\) is a prime power it is impossible by the strict local bound \(R_p(a)<2\). Thus the squarefull core \(c\) has at least two prime factors.

**3. Two-prime squarefull cores.** An odd squarefull core cannot be exponential-unitary perfect: each local sum has an even number of odd summands, hence is even, while \(2c\) has exactly one factor of two. Thus a two-prime core must be \(2^a q^b\), with odd prime \(q\) and \(a,b\ge2\). Its normalized divisor sum satisfies
\[
R_2(a)R_q(b)\le\frac32\left(1+\frac1q\right)\le\frac32\cdot\frac43=2.
\]
Equality requires \(q=3\) and \(a=b=2\). Directly, \(\sigma^{(e)*}(36)=6\cdot12=72\). Hence \(36\) is the unique two-prime squarefull core.

**4. Three-prime squarefull cores.** Again the parity argument forces a prime \(2\); write \(c=2^a q^b r^e\), where \(3\le q<r\) are odd primes and \(a,b,e\ge2\). If \(a\ge4\), then the strengthened bound gives
\[
\frac{\sigma^{(e)*}(c)}c
\le\frac{39}{32}\cdot\frac43\cdot\frac65
=\frac{39}{20}<2,
\]
which is impossible. Thus \(a=2\) or \(3\).

If \(a=2\), the factor \(\sigma^{(e)*}(2^2)=6\) divides \(\sigma^{(e)*}(c)=2c\), so \(3\mid c\) and \(q=3\). The choice \(b=2\) gives \(R_2(2)R_3(2)=2\) already, contradicting \(R_r(e)>1\). Therefore \(b\ge3\), and
\[
2=R_2(2)R_3(b)R_r(e)
\le\frac32\cdot\frac{10}{9}\cdot\frac65=2.
\]
Equality throughout forces \(b=3\), \(r=5\), \(e=2\), giving \(c=2700\).

If \(a=3\), the factor \(\sigma^{(e)*}(2^3)=10\) forces \(5\mid c\). If the third prime is at least \(7\) rather than \(3\), then
\[
R_2(3)R_5(e)R_q(b)
\le\frac54\cdot\frac65\cdot\frac87
=\frac{12}{7}<2,
\]
which is impossible. Hence the odd primes are exactly \(3,5\). Now
\[
2=R_2(3)R_3(b)R_5(e)
\le\frac54\cdot\frac43\cdot\frac65=2,
\]
so equality forces \(b=e=2\), giving \(c=1800\). The two candidates actually work: the local sums are \(10\cdot12\cdot30=3600=2(1800)\) and \(6\cdot30\cdot30=5400=2(2700)\).

**5. Reinsert singleton primes.** If \(\omega(n)\le3\), the core analysis leaves either \(c=36\) or a three-prime core \(c\in\{1800,2700\}\). In the first case the coprime squarefree factor \(m\) can contain at most one prime, giving \(n=36\) or \(36q\) with prime \(q\ge5\). In the second case, \(m=1\). Conversely, each listed integer is exponential-unitary perfect by multiplicativity and the displayed checks. Every listed prime exponent belongs to \(\{1,2,3\}\), a squarefree exponent, so every exponential divisor is also exponential-unitary and the same integers are exponential-perfect. This completes the proof.

## Verification
The accompanying standard-library Python script `artifacts/verify.py` evaluates each local divisor sum using exact integer arithmetic. It checks the local upper bound for primes through \(31\) and exponents \(2\) through \(30\); tests \(184320\) squarefull three-prime parameter triples with \(2\) as smallest prime, other primes through \(31\), and exponents \(2\) through \(17\); and independently factors every integer from \(2\) through \(350000\) to compare the full three-prime classification. The recorded output was:

`VERIFY_OK local_bound=319 squarefull_triples=184320 exact_solutions=[(2, 2, 3, 3, 5, 2), (2, 3, 3, 2, 5, 2)] direct_interval=2..350000 ternary_count=1199 core_36=PASS`

The finite tests are corroboration, not the proof for unrestricted prime and exponent ranges. Run with `python3 artifacts/verify.py` from the containing directory.

## Relationship to prior work
Minculete and Tóth's original 2009 preprint (published in 2011) defined the exponential-unitary divisor sum, identified known examples including \(36,1800,2700\), proved the odd-number obstruction, and asked whether an exponential-unitary perfect integer could fail to be exponential-perfect. The construction \(36q\) follows already from their squarefree-multiplication property. The novelty asserted here is not these individual examples but the **exhaustive three-prime classification**, which excludes every other set of exponents and primes and sharpens the necessary support size in their open problem.

A published two-prime classification establishes \(36\) as the only two-prime exponential-unitary perfect integer; that statement is prior work and is also reconstructed here. An asymptotic theorem for fixed prime-support layers of *ordinary exponential-perfect integers* does not classify their three-prime powerful cores, nor does it establish the stronger exponential-unitary exclusion. OEIS A391281 lists the three displayed powerful examples among known terms, but a list does not establish uniqueness at three-prime support. The classic 1978 article *On e-perfect numbers* was identified bibliographically; its complete primary text could not be inspected. Later handbook accounts were consulted; the 1978 paper concerns ordinary exponential-perfectness and is therefore not assumed to settle the exponential-unitary statement.

## Limitations
The result does not determine any exponential-unitary perfect integer with four or more distinct prime factors and does not solve the global question of whether all such integers are exponential-perfect. The literature comparison is not a proof of absolute historical priority. A more obscure treatment of three-prime cases, especially under older exponential-divisor terminology, could exist. No independent mathematical audit has been performed.

## References
1. L. Tóth and N. Minculete, *Exponential unitary divisors*, arXiv:0910.2798, originally released 2009-10-15; *Annales Univ. Sci. Budapest.*, Sect. Comp. **35** (2011), 205–216. https://arxiv.org/abs/0910.2798 ; https://ac.inf.elte.hu/Vol_035_2011/doi/205_35.pdf .
2. OEIS A391281, *Primitive e-unitary perfect numbers*. https://oeis.org/A391281 .
3. OEIS A322858, *e-perfect numbers that are not e-unitary perfect*. https://oeis.org/A322858 .
4. J. Hanumanthachari, V. V. Subrahmanya Sastri and V. Srinivasan, *On e-perfect numbers*, *Math. Student* **46** (1978), 71–80; bibliographic record at https://schoolbooksarchive.azimpremjiuniversity.edu.in/handle/20.500.12497/11737 .
5. J. Sándor and B. Crstici, *Handbook of Number Theory II*, Kluwer/Springer, 2004, Chapter 1, pp. 51–53.
