# Complete interior Narayana-row gcds at every index

## Finding

For every integer \(n\ge3\), let
\[
\mathcal N(n,k)=\frac1n\binom nk\binom n{k-1}\qquad(1\le k\le n)
\]
be the Narayana number that counts Dyck paths of semilength \(n\) with exactly \(k\) peaks. Its **interior-row content** is
\[
G(n)=\gcd\{\mathcal N(n,k):2\le k\le n-1\}.
\]
The following gives the entire prime-power factorization of \(G(n)\) for every index, prime or composite.

Call an integer \(m\ge2\) a *prime power* if \(m=p^a\) for a prime \(p\) and an integer \(a\ge1\). Define
\[
\alpha(n)=\begin{cases}p,&n=p^a\text{ is a prime power},\\1,&\text{otherwise},\end{cases}
\qquad
\beta(n)=\begin{cases}
q^{\min(2,b)-\mathbf1_{\{q=2,\ b\le2\}}},&n-1=q^b\text{ is a prime power},\\
1,&\text{otherwise}.
\end{cases}
\]
Then
\[
\boxed{G(n)=\alpha(n)\,\beta(n)\qquad(n\ge3).}
\]
In particular, no common prime factor can occur unless either \(n\) or \(n-1\) is a prime power. A prime-power index contributes its underlying prime to exponent exactly one; a prime-power predecessor contributes its underlying prime to exponent at most two. The only two exceptional binary predecessor exponents are \(n-1=2\), which contributes nothing, and \(n-1=4\), which contributes one factor of two rather than four.

For example,
\[
G(8)=14,\quad G(9)=12,\quad G(10)=9,\quad
G(17)=68,\quad G(28)=9,\quad G(33)=4,\quad G(50)=49.
\]
The published odd-prime-row Fermat-prime exception is the prime-index special case of this all-index formula.

## Assumptions and scope

The theorem applies to ordinary integers \(n\ge3\), including prime and composite indices. The gcd is of the \(n-2\) entries with strictly interior peak counts \(2\le k\le n-1\). The two endpoint entries equal one, so including endpoints would trivialize the gcd. A prime power includes prime exponent one. The indicator \(\mathbf1_E\) is one when \(E\) holds and zero otherwise. All divisibility and valuations refer to positive rational integers; no probabilistic or asymptotic assumptions are used.

For proof it is convenient to put \(j=k-1\) and use
\[
\mathcal N(n,j+1)=\frac1n\binom nj\binom n{j+1},\qquad 1\le j\le n-2.
\]
The precise local assertion is, for each prime \(q\),
\[
\nu_q G(n)=\begin{cases}
1,&n=q^a\text{ for some }a\ge1,\\
\min(2,b)-\mathbf1_{\{q=2,\ b\le2\}},&n-1=q^b\text{ for some }b\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
The cases are disjoint because consecutive integers are coprime.

## Proof

**1. The local zero criterion when \(q\nmid n\).** Let \(q\) be prime, \(q\nmid n\), and let \(d\) be the last (units) base-\(q\) digit of \(n\). Lucas's theorem says that \(\binom nj\) is a unit modulo \(q\) precisely when every base-\(q\) digit of \(j\) is no greater than the corresponding digit of \(n\). Because the denominator \(n\) is a unit, one interior Narayana number is a unit if and only if a pair of consecutive interior binomial coefficients are both units.

If \(d\ge2\), take \(j=1\): the coefficients \(\binom n1\) and \(\binom n2\) are both units. If \(d=1\), write \(n-1=q^a u\), where \(a\ge1\) and \(q\nmid u\). When \(u>1\), take \(j=q^a\). Then \(1\le j\le n-2\), and both \(j\) and \(j+1\) have base-\(q\) digits bounded by those of \(n\): at position zero the digit is zero or one; at position \(a\) it is one and the corresponding digit of \(n\) is \(u\bmod q\ge1\). Consequently, \(q\nmid G(n)\) unless \(n-1=q^a\) is itself a prime power. The latter case is analyzed exactly in Step 3.

**2. The local zero criterion and exact valuation when \(q\mid n\).** Write \(n=q^a u\), where \(a\ge1\) and \(q\nmid u\). Suppose first that \(u>1\). If \(u\bmod q\ge2\), choose \(j=q^a\). If \(u\bmod q=1\), choose \(j=q^{a+t}\), where \(t\ge1\) is any position containing a nonzero base-\(q\) digit of \(u\) (such a position exists because \(u>1\)). In either case, \(1\le j\le n-2\), every digit of \(j\) is bounded by the corresponding digit of \(n\), and the digit of \(j\) in position \(a\) is strictly smaller than the corresponding digit of \(n\). Thus Lucas's theorem gives \(\nu_q\binom nj=0\), while \(\nu_q(n-j)=a\) and \(q\nmid(j+1)\). The identity
\[
\binom n{j+1}=\binom nj\frac{n-j}{j+1}
\]
gives \(\nu_q\binom n{j+1}=a\). Dividing the product by \(n\) gives \(\nu_q\mathcal N(n,j+1)=0\). Hence \(q\nmid G(n)\) if \(q\mid n\) but \(n\) is not a pure \(q\)-power.

Now suppose \(n=q^a\ge3\). For every \(1\le j\le n-1\), the coefficient \(\binom{q^a-1}{j-1}\) is a unit modulo \(q\), as the base-\(q\) digits of \(q^a-1\) are all \(q-1\). Therefore
\[
\nu_q\binom{q^a}{j}=a-\nu_q(j).
\]
For every interior index \(1\le j\le q^a-2\), the two consecutive integers \(j,j+1\) have at most one divisible by \(q\), and any such valuation is at most \(a-1\). It follows that
\[
\nu_q\mathcal N(q^a,j+1)=a-\nu_q(j)-\nu_q(j+1)\ge1.
\]
Equality occurs at \(j=q^{a-1}\) if \(a\ge2\), and at \(j=1\) if \(a=1\) (then \(q\ge3\) because \(n\ge3\)). Consequently \(\nu_qG(q^a)=1\).

**3. The exact local valuation for a prime-power predecessor.** Let \(n=q^b+1\), \(b\ge1\). Since \(q\nmid n\), Lucas's theorem shows that the only unit binomial coefficients in its row are those indexed by
\[
0,\quad1,\quad q^b,\quad q^b+1,
\]
with a harmless coincidence of consecutive unit positions when \(q^b=2\). The interior pairs are indexed by \(1\le j\le q^b-1\). If \((q,b)=(2,1)\), then \(n=3\) and the sole interior Narayana number is three, so the \(2\)-valuation is zero.

If \(b=1\) and \(q\) is odd, every interior pair contains a binomial coefficient divisible by \(q\), whereas at \(j=1\)
\[
\mathcal N(q+1,2)=\binom{q+1}{2}=\frac{q(q+1)}2
\]
has valuation one. If \((q,b)=(2,2)\), the same boundary value \(\mathcal N(5,2)=10\) has \(2\)-valuation one, and no interior pair consists of two units. These cases give the exponent one in the formula.

Finally assume \(b\ge2\) with \(q\) odd, or \(b\ge3\) with \(q=2\). At the two boundary interior indices \(j=1\) and \(j=q^b-1\), one binomial factor is a unit and the other has valuation
\[
\nu_q\binom{q^b+1}{2}=b-\nu_q(2)\ge2.
\]
For every strictly intermediate \(j\), both adjacent binomial factors are divisible by \(q\). Thus every interior Narayana number has \(q\)-valuation at least two. Equality is attained at \(j=q^{b-1}\). Indeed, the two coefficients \(\binom{q^b}{j}\) and \(\binom{q^b}{j+1}\) have valuations one and \(b\), respectively, by
\(\binom{q^b}{t}=\frac{q^b}{t}\binom{q^b-1}{t-1}\), since all binomials with upper entry \(q^b-1\) are units modulo \(q\). Also \(\binom{q^b}{j-1}\) has valuation \(b\). Thus Pascal's identity gives
\[
\nu_q\binom{q^b+1}{q^{b-1}}=
\nu_q\binom{q^b+1}{q^{b-1}+1}=1.
\]
The two terms in each Pascal sum have distinct valuations, so no cancellation can raise the smaller one. Hence the minimum is exactly two.

**4. Assembly.** Steps 1–3 prove, for each prime \(q\), the local formula in the scope section. A prime dividing \(n\) cannot divide \(n-1\), so the two possible prime-power contributions never overlap. Unique factorization gives \(G(n)=\alpha(n)\beta(n)\) for every \(n\ge3\), completing the proof.

## Verification

Execute `python3 verify.py` in the package directory. This standard-library-only checker computes the interior Narayana row directly from exact binomial coefficients and integer gcds, checking all \(598\) indices \(3\le n\le600\). Independently, it computes \(5210\) prime-adic minimum valuations using Legendre's factorial-valuation formula, with supported primes and unrelated test primes, for \(3\le n\le700\). It also checks \(21\) boundary and large prime-power examples, including \(n=3,5,9,17,28,33,128,256,344,512\). The expected line is `VERIFY_OK direct_rows=598 local_minima=5210 special_cases=21`. These tests are finite diagnostic checks; the proof of the universal claim is in Steps 1–4.

## Relationship to prior work

Bóna and Sagan (2005), particularly Theorem 1.2 and Corollary 2.2, give a criterion for divisibility of *individual* Narayana entries by a prime, and establish that all interior entries in rows of prime-power index are divisible by that prime. Their work does not give the all-index gcd or its exact prime-power exponents. A separately published theorem, *Exact common divisors of interior Narayana counts in prime rows* (2026), determines the gcd for odd-prime-indexed rows, including Fermat-prime exceptions. That theorem is a **strict special case** of the current statement; it does not treat any composite row indices, including the infinite families \(n=q^b+1\). An exact valuation-distribution theorem for rows \(n=mp^r\) gives strong local information at a prime dividing the row index but does not provide the combined cross-prime, prime-power-predecessor gcd classification. Published Narayana row-GCD tables list small values but no all-index theorem was recovered from the inspected material. These comparisons establish a concrete strengthening, not absolute priority.

## Limitations

The result concerns only the common divisor of strictly interior Narayana numbers, not the full row (whose gcd is one), not the full joint distribution of individual valuations, and not gcds over restricted peak sets. Its all-index classification is conditional only on ordinary integer primality/power detection and does not predict any new prime powers. Prior-art discovery is finite; an unlocated formula or an implicit corollary of more general theory remains a residual priority risk. The checker provides finite corroboration and is not an infinite proof.

## References

1. M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes*, first public version 18 May 2005, arXiv:math/0505382, https://arxiv.org/abs/math/0505382 ; full HTML https://arxiv.org/html/math/0505382v1 .
2. *Exact common divisors of interior Narayana counts in prime rows*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-common-divisors-of-interior-narayana-counts-in-prime-rows--6ee2efd0166c .
3. *Exact valuation polynomials and a geometric limit for dilated Narayana rows*, published 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-valuation-polynomials-and-a-geometric-limit-for-dilated-na--bde71f25e69e .
4. P. Luschny, *Narayana: IntegerTriangles*, row-GCD table, https://luschny.de/math/oeis/Narayana.html .
5. NIST Digital Library of Mathematical Functions, §26.6, Narayana-number table, https://dlmf.nist.gov/26.6 .
