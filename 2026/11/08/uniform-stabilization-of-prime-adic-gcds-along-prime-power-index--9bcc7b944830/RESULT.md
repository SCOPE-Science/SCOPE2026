# Uniform stabilization of prime-adic gcds along prime-power index towers

## Finding
For a positive integer \(m\), an integer \(n>1\), and a prime \(p\), set
\[
 g(m,n)=\gcd_{1\le k<n}\binom{mn}{mk},\qquad
 D_a(m,p)=\nu_p(g(m,p^a)),\quad a\ge1.
\]
Write \(m=p^t u\) with \(t\ge0\) and \(p\nmid u\), and let \(s_p(x)\) be the sum of the base-\(p\) digits of the nonnegative integer \(x\). Define
\[
 c=c_p(m)=\nu_p\binom{pu}{u}=\frac{s_p((p-1)u)}{p-1}\ge1,\qquad R=\max\{1,c-1\}.
\]
Then, for every integer \(a\ge1\),
\[
 \boxed{D_a(m,p)=D_{\min(a,R)}(m,p).}
\]
Thus the \(p\)-adic valuation of the restricted binomial gcd becomes constant after at most \(R\) prime-power steps, even when \(m\) is not a power of \(p\); the stabilization index and final value are computable using only the finitely many binomial coefficients with upper argument \(mp^R\). In particular the computation does not depend on the size of the exponent \(a\).

There is also an exact characterization of the valuation-one case, valid at **every** exponent. With \(s_p\) as above,
\[
 D_a(m,p)=1\quad\Longleftrightarrow\quad
 \min_{1\le j<p}\frac{s_p(uj)+s_p(u(p-j))-s_p(u)}{p-1}=1.
\]
For \(p=2\), this is equivalent to \(u=1\), or equivalently to \(m\) being a power of \(2\). For \(p>u\), the valuation is always \(1\).

## Assumptions and scope
All statements concern arbitrary positive integers \(m\), arbitrary primes \(p\), and every positive exponent \(a\). The gcd is taken over the full set of indices \(1\le k<p^a\), without any coprimality condition on the index. The assertion concerns only the exponent of the **chosen prime** \(p\) in that gcd; it neither factors the gcd fully nor bounds valuations at other primes. For \(p=2\), the argument covers arbitrary even or odd \(m\) after stripping its power of \(2\).

## Proof
**1. Prime-power scaling.** Legendre's formula gives, for every nonnegative integer \(N\),
\[
 \nu_p(N!)=\frac{N-s_p(N)}{p-1}.
\]
Multiplying all three arguments of a binomial coefficient by \(p^t\) leaves its \(p\)-adic valuation unchanged, because base-\(p\) digit sums are unchanged. Consequently
\[
 \nu_p\binom{mp^a}{mk}=\nu_p\binom{up^a}{uk}.
\]
It is enough to work with \(u\) coprime to \(p\).

**2. Mandatory low-digit carries.** For \(1\le k<p^a\), put \(r=\nu_p(k)\) and \(v=a-r\). We have \(0\le r<a\). The base-\(p\) sum
\[
 uk+u(p^a-k)=up^a
\]
has a carry at each of the digit positions \(r,r+1,\ldots,a-1\): the sum has zero digits below position \(a\), while \(uk\) first has a nonzero digit at position \(r\). The carry at position \(r\) is forced, and then the carries propagate through position \(a-1\). By Kummer's theorem,
\[
 \nu_p\binom{up^a}{uk}\ge a-r=v.
\]
Moreover \(k=p^rj\) with \(p\nmid j\) and \(1\le j<p^v\). Removing the common factor \(p^r\) in the binomial arguments shows
\[
 \nu_p\binom{up^a}{uk}=\nu_p\binom{up^v}{uj}.
\]
Define
\[
 E_v=\min_{\substack{1\le j<p^v\\p\nmid j}}\nu_p\binom{up^v}{uj}.
\]
The preceding observations give the **exact reduction**
\[
 D_a(m,p)=\min_{1\le v\le a}E_v,\qquad E_v\ge v.
\]

**3. Cutoff.** Taking \(j=1\) in \(E_1\) yields
\[
 E_1\le\nu_p\binom{pu}{u}=c.
\]
For every \(v\ge c\), the bound \(E_v\ge v\) gives \(E_v\ge c\ge E_1\). Such levels cannot improve the running minimum. If \(c\ge2\), the minimum is therefore attained among \(1\le v\le\min(a,c-1)\); if \(c=1\), it is attained at \(v=1\). This proves the formula with \(R=\max\{1,c-1\}\). The digit-sum expression for \(c\) is Legendre's formula applied to \(\binom{pu}{u}\).

**4. Valuation-one classification.** Since \(E_v\ge v\), any value \(D_a=1\) must already occur at \(v=1\). Conversely \(E_1=1\) persists at all later exponents. Legendre's formula gives
\[
 \nu_p\binom{pu}{uj}=\frac{s_p(uj)+s_p(u(p-j))-s_p(u)}{p-1},\qquad 1\le j<p.
\]
This establishes the stated finite digit-sum criterion. When \(p=2\), the only \(j\) is \(1\), and \(E_1=s_2(u)\), which is \(1\) precisely for \(u=1\) because \(u\) is odd. If \(p>u\), then \((p-1)u=(u-1)p+(p-u)\) has base-\(p\) digit sum \(p-1\), so \(c=1\) and \(D_a=1\). This completes the proof.

## Verification
A standalone Python 3 verifier (`verify.py`, using only the standard library) independently computes (i) complete binomial gcds through `math.comb` and `math.gcd`, (ii) their valuations through Legendre factorial sums, and (iii) Kummer carry counts by direct base-\(p\) addition. It checks the cutoff for many \((m,p,a)\), and confirms nontrivial strict drops: \(D_1(11,2)=3\) but \(D_2(11,2)=2\); similarly \(D_1(39,2)=D_2(39,2)=4\), while \(D_3(39,2)=3\). The expected stdout is in `verification_output.txt`. All finite checks are corroboration only; the proof of the assertion for arbitrarily large \(a\) is the carry argument above.

## Relationship to prior work
Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* (arXiv:2606.20940, first posted June 18, 2026), studies exactly the restricted gcd \(g(m,n)\). Its Theorem 1 determines the \(p\)-valuation when \(m\) itself is a power of \(p\); its Theorem 2 gives the full gcd under special restrictions on prime factors. Neither theorem gives the uniform exponent cutoff and valuation-one digit criterion for arbitrary \(m\) proved here. The special case \(m=p^t\) agrees with Wu's valuation-one theorem.

Siao Hong (2016) obtains a gcd for **different** index restrictions, namely indices coprime to \(m\) instead of multiples of \(m\). Chung, Yang, and Zhou (2025) study a distinct restricted family based on digit sums and primes dividing the upper argument minus one. The classical Kummer theorem is a premise, not a claim of novelty. OEIS A265388 tabulates the full gcd only for \(m=2\). Searches did not identify a published statement implying the arbitrary-\(m\) stabilization theorem. Earlier literature on restricted binomial gcds is extensive, so priority is not asserted unconditionally.

## Limitations
The cutoff \(R\) is a proven uniform upper bound, not claimed to be the least stabilization exponent for every \(m,p\). Different primes dividing the full gcd may behave differently. No general formula for the entire integer \(g(m,p^a)\) is claimed. The historical comparison with the 1985 Joris--Oestreicher--Steinig paper could not be completed from its full text; a possible unindexed stronger theorem is an originality risk. Self-review and finite verification do not constitute independent mathematical audit.

## References
1. C. W. Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* (2026), arXiv:2606.20940, https://arxiv.org/abs/2606.20940 (first posted 2026-06-18).
2. S. Hong, *The greatest common divisor of certain binomial coefficients*, Comptes Rendus Mathématique 354 (2016), 756–761, https://doi.org/10.1016/j.crma.2016.06.001.
3. C.-L. Chung, T.-C. Yang and K. Zhou, *The Greatest Common Divisor of Sets of Binomial Coefficients with Restrictions*, Contemporary Mathematics 6 (2025), 971–985, https://doi.org/10.37256/cm.6120255017.
4. H. Joris, C. Oestreicher and J. Steinig, *The greatest common divisor of certain sets of binomial coefficients*, Journal of Number Theory 21 (1985), 101–119, https://doi.org/10.1016/0022-314X(85)90013-7 (full text unavailable in this review).
5. OEIS A265388, https://oeis.org/A265388 (special case \(m=2\)).
6. E. E. Kummer, classical prime-adic carry theorem for binomial coefficients (1852).
