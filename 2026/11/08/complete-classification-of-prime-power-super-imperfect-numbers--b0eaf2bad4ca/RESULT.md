# Complete classification of prime-power super-imperfect numbers

## Finding
Let \(\beta\) be the multiplicative alternating sum-of-divisors function determined by \(\beta(1)=1\) and
\[
\beta(p^e)=p^e-p^{e-1}+\cdots+(-1)^e
=\frac{p^{e+1}+(-1)^e}{p+1}
\]
for primes \(p\) and integers \(e\ge1\). A positive integer \(n\) is *super-imperfect* if \(2\beta(\beta(n))=n\).

**Theorem.** For every prime \(p\) and every integer \(a\ge1\), the prime power \(p^a\) is super-imperfect if and only if
\[
p^a\in\{2,4,8,128,32768,2147483648\}.
\]
Equivalently, among prime powers the only solutions are \(2^a\) with \(a=2\) or \(a=2^t-1\) for \(1\le t\le5\). This exhausts the prime-power subfamily, **not** the arbitrary-composite super-imperfect problem.

## Assumptions and scope
All arguments take place in the ordinary integers. Prime powers have positive exponents; \(1\) is not included and also does not solve the equation. Write \(F_j=2^{2^j}+1\), \(j\ge0\), for Fermat numbers. We use only the classical facts that \(F_0,F_1,F_2,F_3,F_4\) are prime and \(F_5=641\cdot6700417\) is composite, both checked by exact trial division in the supplementary verifier. No hypothesis about future Fermat primes is needed.

## Proof
**Step 1: classify odd arguments whose \(\beta\)-value is a power of two.** For every odd integer \(m\ge1\),
\[
\beta(m)\text{ is a power of }2
\quad\Longleftrightarrow\quad
m\text{ is a squarefree product of Fermat primes}.
\tag{1}
\]
The empty product is allowed. By multiplicativity, it suffices to consider an odd prime power \(q^e\). If \(e\) is positive and even, \(\beta(q^e)\) is odd and greater than one. If \(e=2u-1\) is odd, factor
\[
\beta(q^{2u-1})=(q-1)\bigl(1+q^2+\cdots+q^{2(u-1)}\bigr).
\]
For odd \(u>1\), the parenthesized number is an odd integer greater than one. For even \(u\), it is divisible by \(q^2+1\), which is congruent to \(2\pmod8\) and exceeds \(2\); therefore it has an odd prime divisor. Thus only \(u=1\), or \(e=1\), can yield a power of two. In that case \(\beta(q)=q-1\), so \(q=2^b+1\) for some \(b\ge1\). If \(b\) had an odd divisor greater than one, \(2^b+1\) would have a proper factor of the form \(2^c+1\). Hence \(b=2^j\) and \(q=F_j\) is prime. Conversely a product of distinct Fermat primes has \(\beta\)-value a power of two. This proves (1).

**Step 2: reduce prime powers to powers of two.** If \(2\beta(\beta(p^a))=p^a\), then \(p^a\) is even, so \(p=2\). Put \(m=\beta(2^a)\). The number \(m\) is odd, and the equation becomes \(\beta(m)=2^{a-1}\). By (1), \(m\) is a squarefree product of Fermat primes.

**Step 3: exclude all even exponents except two.** If \(a\ge2\) is even, write \(d=a+1\), which is odd. Then
\[
m=\frac{2^d+1}{3}.
\]
For any prime Fermat number \(F_j\), the multiplicative order of \(2\) modulo \(F_j\) is exactly \(2^{j+1}\), because \(2^{2^j}\equiv-1\pmod{F_j}\). For \(j\ge1\), the congruence \(2^d\equiv-1\pmod{F_j}\) would force \(d\equiv2^j\pmod{2^{j+1}}\), impossible for odd \(d\). Therefore the only permitted prime factor of \(m\) is \(F_0=3\). By squarefreeness, \(m=1\) or \(3\); since \(a\ge2\), \(m\ge3\), and \(m=3\) forces \(d=3\), namely \(a=2\). This exponent indeed works: \(\beta(4)=3\), \(\beta(3)=2\).

**Step 4: force every odd exponent into the Fermat family.** Suppose \(a\) is odd, and write \(d=a+1=2^t v\) with \(t\ge1\) and \(v\) odd. Now
\[
m=\frac{2^d-1}{3}.
\]
If a prime Fermat number \(F_j\) divides \(m\), its multiplicative-order condition \(2^{j+1}\mid d\) gives \(j<t\). Since \(m\) is a product of *distinct* Fermat primes,
\[
m\mid\prod_{j=0}^{t-1}F_j=2^{2^t}-1.
\tag{2}
\]
If \(v\ge3\), however, \((2^{2^t v}-1)/3>2^{2^t}-1\), contradicting (2). Therefore \(v=1\), whence \(a=2^t-1\) and
\[
m=\frac{2^{2^t}-1}{3}=\prod_{j=1}^{t-1}F_j.
\]
The Fermat numbers are pairwise coprime, as follows from \(\prod_{j=0}^{s-1}F_j=F_s-2\). Because \(m\) is a product of distinct Fermat *primes*, every factor \(F_1,\ldots,F_{t-1}\) must be prime. The composite number \(F_5\) forces \(t\le5\). For each \(1\le t\le5\), all these factors are prime and
\[
\beta(m)=\prod_{j=1}^{t-1}(F_j-1)
=2^{\sum_{j=1}^{t-1}2^j}=2^{2^t-2}=2^{a-1},
\]
so every listed odd exponent works. Together with \(a=2\), this proves the theorem.

## Verification
Run `python3 verify.py` (Python standard library only). The script independently factors the inputs for every exponent \(1\le a\le24\), verifies the exponent \(31\) witness by its exact factorization, tests the odd-prime-power structural criterion on 510 prime/exponent pairs, confirms primality of \(F_0,\ldots,F_4\) by trial division, and checks the explicit factorization of \(F_5\). Its expected final line begins `VERIFY_OK`. The infinite classification is proved in the preceding argument; finite checks are not substituted for that proof.

## Relationship to prior work
Tóth's 2011 preprint, *A survey of the alternating sum-of-divisors function*, introduces super-imperfect numbers, formulates the open question whether any others exist (Section 7, Problem 1), and proves that **within the already chosen family** \(2^{2^t-1}\), precisely the indices \(1\le t\le5\) work (Section 7 Proposition and its proof in Section 8). The present classification adds the converse reduction: *any* prime-power solution has this form, apart from \(4\). Thus it gives a complete answer for the natural prime-power subfamily, not a new proof of Tóth's known restricted-family statement. OEIS A200758 lists the same six examples and the earlier restricted-family proposition; listing them does not imply their exhaustiveness among all prime powers.

## Limitations
The theorem does not exclude solutions with two or more distinct prime divisors. It does not assert that the full super-imperfect problem is solved. The local Fermat-prime criterion is an elementary intermediate lemma, not an independent claim of a novel broad classification. Literature searches have not ruled out every unindexed previous proof; historical priority requires external review. No independent mathematical audit has been performed.

## References
1. L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842, first posted 2011-11-21; especially Sections 1, 7, and 8. https://arxiv.org/abs/1111.4842
2. OEIS Foundation, A200758, *Superimperfect numbers*: https://oeis.org/A200758
3. Classical Fermat-number factorization \(F_5=641\cdot6700417\); checked directly by `verify.py`.
