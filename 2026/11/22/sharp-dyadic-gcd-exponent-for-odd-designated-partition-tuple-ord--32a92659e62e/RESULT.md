# Sharp dyadic gcd exponent for odd designated-partition tuple orders

## Finding
Let \(f_r(q)=\prod_{m\ge1}(1-q^{rm})\) and define
\[
F(q)=\frac{f_6(q)}{f_1(q)f_2(q)f_3(q)},\qquad
A_k(n)=[q^n]F(q)^k.
\]
Thus \(A_k(n)\) counts ordered \(k\)-tuples of partitions with designated summands having total size \(n\). For **every odd integer \(k\ge1\)**, put \(s=\nu_2(k+1)\). Then, for all \(n\ge0\),
\[
A_k(4n+3)\equiv0\pmod{2^{s-1}},\qquad
\nu_2(A_k(3))=s-1.
\]
In particular, the exact exponent of \(2\) in the greatest common divisor of all \(A_k(4n+3)\) is \(\nu_2(k+1)-1\). For example, the common dyadic modulus is sharp at \(4\), \(8\), and \(16\) for \(k=7,15,31\), respectively. This establishes the odd-\(k\) half of Conjecture 6.1 in Yaqubi--Mirzavaziri (2026).

## Assumptions and scope
All identities involving \(q\) are identities in \(\mathbb Z[[q]]\), or their indicated coefficientwise reductions. The valuation \(\nu_2(m)\) refers to a nonzero integer \(m\), and the gcd is taken over the infinite set of indices \(n\ge0\). The theorem makes no assertion about the exact odd part of this gcd or about even tuple orders.

## Proof
**1. Exact lacunarity of the reciprocal.** Write \(R(q)=F(q)^{-1}=f_1f_2f_3/f_6\). Since the sum of eta arguments in numerator and denominator is equal, the prefactor in the Dedekind-eta notation cancels:
\[
R(q)=\frac{\eta(z)\eta(2z)\eta(3z)}{\eta(6z)},\qquad q=e^{2\pi i z}.
\]
Theorem 1.1 of Kassel--Reutenauer (2017) expresses its coefficient \([q^m]R(q)\) as \((-1)^j r(m)\), \((-1)^{j+1}r(m)/4\), or \((-1)^{j+1}r(m)/2\), according as \(m=3j\), \(3j+1\), or \(3j+2\), respectively, where \(r(m)\) counts ordered signed representations \(m=x^2+y^2\). No integer congruent to \(3\pmod4\) is a sum of two squares, because each square is \(0\) or \(1\pmod4\). Hence
\[
[q^{4n+3}]R(q)=0\quad\text{for every }n\ge0.\tag{1}
\]
This is an exact identity over the integers, not merely a congruence.

**2. Integral Frobenius lifting.** For any \(H(q)\in\mathbb Z[[q]]\) and integer \(t\ge1\),
\[
H(q)^{2^t}\equiv H(q^2)^{2^{t-1}}\pmod{2^t}.\tag{2}
\]
Indeed \(H(q)^2\equiv H(q^2)\pmod2\). If \(U\equiv V\pmod{2^a}\) with \(a\ge1\), then \(U^2-V^2=(U-V)(U+V)\) is divisible by \(2^{a+1}\), since \(U+V\equiv 2V\equiv0\pmod2\). Repeated squaring proves (2).

Apply (2) first with \(H=F\), \(t=s\), and then with \(H(q)=F(q^2)\), \(t=s-1\). For \(s\ge2\), this yields
\[
F(q)^{2^s}\equiv F(q^4)^{2^{s-2}}\pmod{2^{s-1}}.\tag{3}
\]
The intermediate congruence in the first step even holds modulo \(2^s\), so no precision is lost beyond the second step. Writing \(k+1=2^s u\) with \(u\) odd and raising (3) to the positive integer power \(u\), we obtain
\[
F(q)^{k+1}\equiv F(q^4)^{2^{s-2}u}\pmod{2^{s-1}}.\tag{4}
\]
Multiply by the integral series \(R=F^{-1}\). Equation (1) and the fact that every term of \(F(q^4)^{2^{s-2}u}\) has degree divisible by \(4\) show that the coefficient of \(q^{4n+3}\) in the right-hand side of (4), after multiplication by \(R\), is zero. This proves \(2^{s-1}\mid A_k(4n+3)\) for \(s\ge2\). When \(s=1\) the claim is divisibility by \(1\), which is automatic.

**3. Sharpness at the first index.** The first four coefficients of \(F(q)\) are \(1,1,3,5\). A direct expansion of \(F(q)^k\) gives
\[
A_k(3)=5k+3k(k-1)+\binom{k}{3}=\frac{k(k+1)(k+14)}6.
\]
For odd positive \(k\), both \(k\) and \(k+14\) are odd, and \(\nu_2(6)=1\). Thus \(\nu_2(A_k(3))=\nu_2(k+1)-1=s-1\), certifying the exact universal exponent. \(\square\)

## Verification
The finite diagnostic program `verify_congruence.py` independently forms \(F\) through a logarithmic-derivative recurrence, checks the reciprocal through a separate Euler-product multiplication, and tests the claimed divisibility and sharpness for odd \(1\le k\le129\) and \(0\le n\le39\). It reports 2,600 coefficient divisibility checks, 65 sharpness checks, 40 reciprocal gap checks, and 81 independent reciprocal coefficient comparisons. The proof of the all-index result is Steps 1--3, not the finite checker.

## Relationship to prior work
Yaqubi--Mirzavaziri, *Partitions with designated summands: \(k\)-tuples and their congruences* (arXiv:2611.05623v1, first submitted 2026-11-03), Conjecture 6.1, predicts the exact highest common dyadic power for **all** tuple orders. Their Theorem 3.12 gives lower-order parity and other partial congruences, while Proposition 3.13 handles a separate even residue class. The present theorem resolves its entire odd-tuple subfamily, including arbitrarily deep powers of two, without addressing the remaining even orders.

Kassel--Reutenauer, *The Fourier expansion of \(\eta(z)\eta(2z)\eta(3z)/\eta(6z)\)* (2017), Theorem 1.1, already identifies the coefficients of the reciprocal eta quotient in terms of sums of two squares. Its exact lacunarity at the residue class \(3\pmod4\) is used here as a previously known premise; it is not claimed as new. The dyadic lifting and its implication for the open tuple-order valuation classification are the new argument.

## Limitations
No even-order cases of Conjecture 6.1 are settled. The result concerns only the exponent of \(2\) in the universal gcd; it does not classify odd prime divisors. The computer checks are bounded and are not evidence for infinite-index validity without the proved identities. An equivalent unindexed general theorem on high powers of reciprocal eta quotients would affect priority, despite the targeted literature and research-record comparisons reported separately.

## References
1. D. Yaqubi and M. Mirzavaziri, *Partitions with designated summands: \(k\)-tuples and their congruences*, arXiv:2611.05623v1, 2026-11-03, https://arxiv.org/abs/2611.05623, especially Theorem 3.12, Proposition 3.13 and Conjecture 6.1.
2. C. Kassel and C. Reutenauer, *The Fourier expansion of \(\eta(z)\eta(2z)\eta(3z)/\eta(6z)\)*, Archiv der Mathematik 108 (2017), DOI: 10.1007/s00013-017-1033-4; open author copy at https://reutenauer.math.uqam.ca/wp-content/uploads/2024/05/Fourier-expansion.pdf, especially Theorem 1.1.
