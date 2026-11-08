# Exact common divisors of interior Narayana counts in prime rows

## Finding

For integers \(n\ge1\) and \(1\le k\le n\), the Narayana number
\[
\mathcal N(n,k)=\frac1n\binom nk\binom n{k-1}
\]
counts Dyck paths of semilength \(n\) with exactly \(k\) peaks. For an **odd prime** \(p\), define the interior-row common divisor
\[
G(p)=\gcd\{\mathcal N(p,k):2\le k\le p-1\}.
\]
Then, for every odd prime \(p\),
\[
\boxed{
G(p)=
\begin{cases}
p,&p-1\text{ is not a power of }2,\\
p\,2^{\min(2,r-1)},&p=2^r+1\text{ with }r\ge1.
\end{cases}}
\]
In particular, \(G(3)=3\), \(G(5)=10\), and every Fermat prime \(p\ge17\) satisfies \(G(p)=4p\). Thus, among odd primes, \(G(p)>p\) holds exactly for Fermat primes other than \(3\). The statement does not assert that further Fermat primes exist.

## Assumptions and scope

The index \(p\) is a positive odd prime; the gcd is over all peak numbers strictly between the two extreme peak counts, \(2\le k\le p-1\). The endpoint Narayana numbers are both \(1\), so including them would make the gcd identically \(1\). All binomial coefficients and gcds are taken over the ordinary integers. A Fermat prime here means a prime of the form \(2^{2^m}+1\) for some integer \(m\ge0\). A prime of the form \(2^r+1\) must have \(r\) a power of two, by factoring \(a^b+1\) when \(r\) has an odd factor.

## Proof

**1. Prime divisor and candidate set.** For every \(1\le j\le p-1\),
\[
\nu_p\binom pj=1,
\]
since \(\binom pj=(p/j)\binom{p-1}{j-1}\), and \(\binom{p-1}{j-1}\not\equiv0\pmod p\) by Lucas's theorem (or the elementary factorial identity). Both \(j=k\) and \(j=k-1\) lie in this range for \(2\le k\le p-1\), so
\[
\nu_p\mathcal N(p,k)=1
\quad(2\le k\le p-1).
\]
Therefore \(p\) divides \(G(p)\) exactly once. The value at the first nontrivial peak count is
\[
\mathcal N(p,2)=\frac{p(p-1)}2.
\]
Every other prime divisor of \(G(p)\) must divide \(p-1\).

**2. Exclusion of odd primes other than \(p\).** Let \(\ell\ne p\) be an odd prime dividing \(p-1\), and write \(p-1=\ell^a u\) with \(a\ge1\) and \(\ell\nmid u\). The cofactor \(u\) is even, so \(u\ge2\). Set \(k=\ell^a+1\); then \(2\le k\le p-1\). The base-\(\ell\) expansion of \(p=1+u\ell^a\) has digit \(1\) in position zero and nonzero digit \(u\bmod\ell\) in position \(a\). Lucas's theorem therefore yields
\[
\binom p{\ell^a}\equiv u\not\equiv0\pmod\ell,
\qquad
\binom p{\ell^a+1}\equiv u\not\equiv0\pmod\ell.
\]
Because \(p\) is a unit modulo \(\ell\), \(\mathcal N(p,k)\not\equiv0\pmod\ell\). No such \(\ell\) divides the full interior-row gcd.

**3. The ordinary binary branch.** Write \(p-1=2^r u\) with \(r\ge1\) and \(u\) odd. If \(u>1\), then \(u\ge3\). Taking \(k=2^r+1\) gives an interior index. The binary digits of \(p=1+u2^r\) include a one in positions \(0\) and \(r\). Lucas's theorem makes both \(\binom p{2^r}\) and \(\binom p{2^r+1}\) odd. Since \(p\) is odd, \(\mathcal N(p,k)\) is odd. Consequently \(2\nmid G(p)\), and Steps 1–2 establish \(G(p)=p\) whenever \(u>1\).

**4. The Fermat-prime branch.** It remains to assume \(p=2^r+1\), where \(r\ge1\). Put \(A=2^r\). For every integer \(1\le j<A\), the binomial coefficient \(\binom{A-1}{j-1}\) is odd, hence
\[
\nu_2\binom Aj=r-\nu_2(j).
\]
For \(2\le k\le A\), using \(\binom{A+1}{k}=\frac{A+1}{k}\binom A{k-1}\), this gives
\[
\nu_2\binom{A+1}k=r-\nu_2(k)-\nu_2(k-1).
\]
At \(k=2\), the other factor \(\binom{A+1}1=A+1\) is odd, so
\[
\nu_2\mathcal N(A+1,2)=r-1.
\]
For each \(3\le k\le A\), applying the same identity to both binomial factors yields
\[
\nu_2\mathcal N(A+1,k)
=2r-\nu_2(k)-2\nu_2(k-1)-\nu_2(k-2).
\]
When \(k\) is odd, both \(k\) and \(k-2\) are odd and \(\nu_2(k-1)\le r-1\), so this valuation is at least \(2\). For \(r\ge2\), equality is attained at \(k=2^{r-1}+1\). When \(k\) is even and \(k\ge4\), the integer \(k-1\) is odd; exactly one of \(k\) and \(k-2\) has valuation \(1\), while the other has valuation at most \(r\). Therefore the displayed valuation is at least \(r-1\). Including \(k=2\), the minimum binary valuation across the row is exactly
\[
\min\{r-1,2\}
\]
for \(r\ge2\), and zero for \(r=1\). Steps 1–2 exclude any extra odd prime divisor. Thus \(G(p)=p2^{\min(2,r-1)}\), completing the proof.

## Verification

Run the standalone standard-library checker in the same package with `python3 verify.py`. It reconstructs every Narayana entry and its exact gcd for all odd primes up to \(257\); verifies \(828\) Lucas nonvanishing-witness cases for primes up to \(2000\); and checks the critical Fermat-branch binary-valuation witnesses for exponents \(1,2,4,8,16\) (the largest by symbolic valuation, not enumeration of its huge row). Expected terminal line begins with `VERIFY_OK`. Finite checks support, but do not substitute for, the proof for arbitrary odd primes.

## Relationship to prior work

Bóna and Sagan (2005) proved a necessary-and-sufficient criterion for **prime** divisibility of individual Narayana numbers. Their Corollary 2.2 states that all nonendpoint entries in a row indexed by a prime power are divisible by that prime. The present result determines the **entire gcd** when that row index is an odd prime, proves there are no other common odd prime factors, and determines the exact residual \(2\)-adic exponent, including its Fermat-prime exception. Their article comments on the added complexity of higher valuations, but does not state this exact row gcd. Eu, Liu and Yeh (2006) address Lucas-type congruences for several combinatorial sequences; no complete corresponding prime-row Narayana gcd was located in the accessible description. Published sequence tables of Narayana values or numbers of odd entries do not, without further analysis, furnish the gcd theorem.

## Limitations

The theorem concerns only odd-prime-indexed rows. It does not classify the gcd for composite row indices, make claims about the existence of unknown Fermat primes, or provide a combinatorial group action explaining the exact powers of two. The archival priority comparison is based on inspected available material and targeted searches; no universal novelty certification is asserted.

## References

1. M. Bóna and B. E. Sagan, *On Divisibility of Narayana Numbers by Primes*, first posted 18 May 2005, arXiv:math/0505382, https://arxiv.org/abs/math/0505382 .
2. S.-P. Eu, S.-C. Liu and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers*, *Studies in Applied Mathematics* 116 (2006), 135–144, DOI:10.1111/j.1467-9590.2006.00337.x .
3. OEIS A001263, Narayana's triangle, https://oeis.org/A001263 .
4. OEIS A335965, number of odd entries in a Narayana row, https://oeis.org/A335965 .
5. É. Lucas, classical congruence theorem for binomial coefficients (1878); see the statement cited in Bóna and Sagan, reference 1.
