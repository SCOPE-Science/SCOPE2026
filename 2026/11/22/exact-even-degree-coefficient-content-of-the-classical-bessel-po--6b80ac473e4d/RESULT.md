# Exact even-degree coefficient content of the classical Bessel polynomials

## Finding

Write the classical Bessel polynomial as
\[
y_n(X)=\sum_{k=0}^{n}a(n,k)X^k,\qquad
a(n,k)=\frac{(n+k)!}{2^k k!(n-k)!},
\]
with integral coefficients. For every integer \(n\ge2\), define the coefficient content of its nonconstant even part by
\[
H(n)=\gcd_{1\le j\le\lfloor n/2\rfloor}a(n,2j).
\]
Let \(P(n)=(n-1)n(n+1)(n+2)\), and let \(\operatorname{odd}(m)=m/2^{\nu_2(m)}\) for every positive integer \(m\). Then the exact all-index classification is
\[
\boxed{H(n)=\frac{\operatorname{odd}(P(n))}
{3^{\mathbf 1_{\{n\equiv1\pmod3\}}}}.}
\]
In particular, \(H(n)\) is odd. For every odd prime \(p\ne3\), its valuation is \(\nu_p(P(n))\); at \(p=3\), it is \(\nu_3(P(n))-\mathbf1_{\{n\equiv1\pmod3\}}\). The loss of one factor of three arises precisely when the four central consecutive factors contain two multiples of three.

## Assumptions and scope

The normalization is the standard integral Bessel polynomial with constant coefficient one, not the reversed polynomial. The positive even-degree indices are exactly \(k\in\{2,4,\ldots,2\lfloor n/2\rfloor\}\), and the theorem asserts the gcd of that nonempty set, for all integers \(n\ge2\). All primes and exponents in the proof are ordinary rational primes and nonnegative integer valuations.

## Proof

**1. Prime-adic lower bounds.** For every positive integer \(k\le n\), let \(I_{n,k}\) denote the \(2k\) consecutive integers from \(n-k+1\) through \(n+k\). For an odd prime \(p\) and every \(j\ge1\), write \(q=p^j\) and let \(M_q(n,k)\) be the number of multiples of \(q\) in \(I_{n,k}\). Legendre's factorial valuation formula yields the finite sum
\[
\nu_p(a(n,k))=\sum_{j\ge1}\left(M_{p^j}(n,k)-\left\lfloor\frac{k}{p^j}\right\rfloor\right).
\]
Every summand is nonnegative: an interval of \(2k\) consecutive integers contains at least \(\lfloor2k/q\rfloor\) multiples of \(q\), and \(\lfloor2k/q\rfloor\ge\lfloor k/q\rfloor\).

Suppose \(k\ge2\) is even and \(q=p^j\) divides at least one of the four central numbers \(n-1,n,n+1,n+2\). Those four numbers all belong to \(I_{n,k}\). If \(q>k\), then \(\lfloor k/q\rfloor=0\) and \(M_q(n,k)\ge1\). If \(q\le k\), then
\[
M_q(n,k)-\left\lfloor\frac{k}{q}\right\rfloor
\ge\left\lfloor\frac{2k}{q}\right\rfloor-\left\lfloor\frac{k}{q}\right\rfloor\ge1.
\]
Thus each odd-prime power dividing a central number contributes at least one to every even-degree coefficient's valuation.

If \(p\ge5\), the four consecutive central integers contain at most one multiple of each \(p^j\); the number of distinct powers \(p^j\) dividing any of them therefore equals \(\nu_p(P(n))\). If \(p=3\), the same holds for \(3^j\ge9\), while among the four central integers there are two multiples of three exactly when \(n\equiv1\pmod3\), and one otherwise. Consequently, for every allowed even \(k\),
\[
\nu_p(a(n,k))\ge
\begin{cases}
\nu_p(P(n)),&p\ge5,\\
\nu_3(P(n))-\mathbf1_{\{n\equiv1\pmod3\}},&p=3.
\end{cases}
\]

**2. Attainment for every odd prime.** The first retained coefficient equals
\[
a(n,2)=\frac{P(n)}8.
\]
Thus its valuation gives equality in the preceding lower bound for every \(p\ge5\), and also for \(p=3\) when \(n\not\equiv1\pmod3\). When \(n\equiv1\pmod3\) and \(n\ge2\), necessarily \(n\ge4\), so the coefficient \(a(n,4)\) is present. It obeys
\[
a(n,4)=\frac{P(n)(n-3)(n-2)(n+3)(n+4)}{2^4\,4!}.
\]
All four newly displayed factors are units modulo three, and \(\nu_3(4!)=1\). Therefore
\[
\nu_3(a(n,4))=\nu_3(P(n))-1.
\]
This supplies exact attainment of the lower bound for the remaining prime and congruence class.

**3. Absence of a factor of two.** For \(n\ge2\), let \(k\) be the largest power of two not exceeding \(n\). It is even. The exact coefficient factorization is
\[
a(n,k)=\binom{n+k}{2k}(2k-1)!!.
\]
Here \(0\le n-k<k\), and the two binary integers \(2k\) and \(n-k\) have disjoint nonzero bit positions. By Lucas's theorem (or the zero-carry case of Kummer's theorem), \(\binom{n+k}{2k}\) is odd. The odd double factorial \((2k-1)!!\) is odd too. Hence the gcd of the retained even-degree coefficients is odd. Combining all exact prime valuations proves the formula. \(\square\)

## Verification

The standalone script `CHECK.py` computes each coefficient independently from the Bessel recurrence \(y_n(X)=(2n-1)Xy_{n-1}(X)+y_{n-2}(X)\), as well as from the factorial/binomial identity. It checks all coefficients, the claimed gcd of positive even-degree entries, an explicit odd witness, and the exceptional three-adic drop for every \(2\le n\le256\). Running `python3 CHECK.py` produced `PASS: 34000 exact assertions; n=2..256, all coefficients via independent recurrence.` The calculations support, but are not substituted for, the preceding unrestricted proof.

For illustration, the contents for successive indices \(n=2,3,4,5,6,7,8,9\) are \(3,15,15,105,105,63,315,495\), respectively.

## Relationship to prior work

The standard Bessel coefficient formula and matching interpretation are given by Han and Seo (2004), whose investigated theorems concern inverse relations and log-concavity, rather than parity-restricted coefficient contents. The general Bessel-matrix and determinant representations of Yang and Zheng (2013) likewise do not state this gcd formula. OEIS A001498 records the coefficient triangle, from which finitely many cases can be tested, not an all-index parity-filtered gcd theorem.

A 2025 MathOverflow question and answer establish elementary whole-row divisibility by \(n+1\) when \(n\) is even and by \(n\) when \(n\) is odd. That divides all positive-degree coefficients, and does not determine the gcd of the *even-degree subrow*: for instance \(n=7\) has even-degree content \(63\), not merely the previously established common factor \(7\). The present proof's parity selection, four-factor lower bound, and unique three-adic correction are additional claims, not statements of the cited answer. A prior equivalent in older Bessel-polynomial literature cannot be ruled out conclusively.

## Limitations

Only the classical Bessel normalization, and only positive even degrees, are classified. The constant term is excluded because it is one. No classification is claimed for arbitrary generalized Bessel parameters, for finer coefficient subsets, or for an independent priority assessment. Sources with plausible background relevance, including older monographs and some early articles on Bessel polynomials, were not all available for full-text inspection. The computations have finite scope, while the theorem has an independent proof for every \(n\ge2\).

## References

- H. Han and S. Seo, *Combinatorial proofs of inverse relations and log-concavity for Bessel numbers*, initial public arXiv submission 2004-06-18, https://arxiv.org/abs/math/0406378 .
- S.-L. Yang and S.-N. Zheng, *A Determinant Expression for the Generalized Bessel Polynomials*, published online 2013-08-29, https://doi.org/10.1155/2013/242815 .
- *OEIS A001498: Coefficients of Bessel polynomials*, https://oeis.org/A001498 .
- A. Benmoussa, *Divisibility properties of Bessel numbers*, question and answer posted October–November 2025, https://mathoverflow.net/questions/503276/divisibility-properties-of-bessel-numbers-oeis-a001498 .
- NIST Digital Library of Mathematical Functions, §18.34, Bessel polynomials, https://dlmf.nist.gov/18.34 .
