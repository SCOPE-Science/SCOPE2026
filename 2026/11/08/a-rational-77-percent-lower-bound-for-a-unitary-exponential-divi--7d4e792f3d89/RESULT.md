# A rational 77-percent lower bound for a unitary--exponential divisor-sum comparison density

## Finding
For positive integers \(n\), let \(\sigma^*(n)\) be the sum of unitary divisors and \(\sigma^{(e)}(n)\) the sum of exponential divisors. Let \(\delta\) be the natural density of the set \(\{n:\sigma^*(n)>\sigma^{(e)}(n)\}\), whose existence is established in prior literature. Set
\[
Q=28535726520270636024768604478765044285962240000000,
\quad
N=22146947537280283084803283684585457657160649113600.
\]
Then the following **rigorous rational bound** holds:
\[
\boxed{\delta\ge\frac{397N}{400Q}=0.770292125386622\ldots>\frac{77}{100}.}
\]
No claim is made that this lower bound is the true density. This is stronger than the previously published explicit bound \(0.753659844064288\ldots\), and much stronger than the square-free bound \(6/\pi^2\).

## Assumptions and scope
The unitary-divisor function is \(\sigma^*(n)=\sum_{d\mid n,\,\gcd(d,n/d)=1}d\). The exponential divisor sum is multiplicative, with \(\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\) for \(a\ge1\). Both functions take value one at \(n=1\). Thus for each prime \(p\), define
\[
\rho_p(0)=1,\qquad
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}\quad(a\ge1).
\]
The finite sieve uses precisely the ten primes
\[
P=(2,3,5,7,11,13,17,19,23,29)
\]
and their exponent caps
\[
E=(16,12,6,5,4,3,3,3,2,2).
\]
The remaining primes are constrained only to exponent zero or one. All density statements concern positive integers in natural order, not random sampled integers.

## Proof
**1. Exact finite cylinder mass.** For each vector \(\mathbf a=(a_p)_{p\in P}\), where \(0\le a_p\le E_p\), put \(R(\mathbf a)=\prod_{p\in P}\rho_p(a_p)\). Define
\[
Q=\prod_{p\in P}p^{E_p+1},\qquad
N=\sum_{\substack{0\le a_p\le E_p\;\forall p\in P\\R(\mathbf a)\ge1}}
\prod_{p\in P}(p-1)p^{E_p-a_p}.
\]
The standalone exact-integer verifier enumerates **all**
\[
\prod_{p\in P}(E_p+1)=26732160
\]
vectors. It checks every rational comparison by integer cross-multiplication, using the divisor-sum formula above, and computes the stated integers \(N,Q\). Consequently the natural density of integers whose exact \(p\)-adic valuations lie in an enumerated acceptable vector is exactly \(N/Q\). The enumeration is exhaustive by nested loops over the explicitly bounded Cartesian product; there is no statistical sampling.

**2. The prime tail.** Set \(\mathcal T=\{n:\nu_q(n)\le1\text{ for every prime }q>29\}\). Its natural density is the absolutely convergent Euler product
\[
\prod_{q>29}\left(1-\frac1{q^2}\right)
\ge1-\sum_{q>29}\frac1{q^2}.
\]
The last prime sum is **strictly smaller than** \(3/400\). To verify this without a numerical limit assumption, enumerate by trial division every prime \(31\le q\le997\), and check the finite exact-rational inequality
\[
\sum_{\substack{31\le q\le997\\q\text{ prime}}}\frac1{q^2}
+\frac1{2985}<\frac3{400}.
\]
There are exactly 158 primes in that interval. Every prime greater than \(997\) is congruent to \(1\) or \(-1\) modulo \(6\), and the remaining reciprocal-square tail is bounded by
\[
\sum_{j=167}^{\infty}\left(\frac1{(6j-1)^2}+\frac1{(6j+1)^2}\right)
\le2\sum_{j=167}^{\infty}\frac1{(6j-1)^2}
\le2\int_{166}^{\infty}\frac{dx}{(6x-1)^2}
=\frac1{2985}.
\]
The finite prime sum and the final comparison are checked exactly as fractions in the verifier.

**3. Product positivity.** If \(n\in\mathcal T\) has one of the acceptable finite exponent vectors, every prime \(q>29\) dividing \(n\) contributes \(\rho_q(1)=1+1/q>1\). Thus the product \(\sigma^*(n)/\sigma^{(e)}(n)\) is strictly larger than one unless the tail has no prime factors and \(R(\mathbf a)=1\). The integers supported entirely on the fixed finite set \(P\) have density zero (their count up to \(x\) is \(O((\log x)^{10})\)); excluding them does not affect the density. The finite-prime exact-valuation event and the tail square-freeness event have independent limiting densities by the Chinese remainder theorem and the convergent square-divisor sieve. Therefore
\[
\delta\ge\frac NQ\prod_{q>29}(1-q^{-2})
>\frac NQ\left(1-\frac3{400}\right)
=\frac{397N}{400Q}.
\]
The final exact integer inequality \(397N>308Q\) establishes \(397N/(400Q)>77/100\), completing the proof. The displayed non-strict bound follows immediately.

## Verification
Run `python3 verify_density.py` using only the Python standard library. It independently constructs all local prime-power factors, recursively visits every allowed vector, accumulates integer cylinder weights only when exact numerator-denominator comparison succeeds, and checks \(N\), \(Q\), \(397N>308Q\), the number of trial-division primes, and the exact finite rational reciprocal-square bound. The program terminates after the full finite census; its proof role is the exhaustive finite inequality, not the infinite Euler-product step. The program is included in full in the package.

## Relationship to prior work
Tim Trudgian posed the density question in 2013, proved existence of the relevant density via Erdős--Wintner, recorded the square-free lower bound \(6/\pi^2\), and reported an observed proportion near \(0.778307\) through \(10^9\). A later published result entitled *An explicit \(0.753659844\ldots\) lower bound for the unitary--exponential divisor-sum comparison density* gave the stronger earlier bound \(6097572635664749695003/(819750822146736480000\pi^2)\), using six primes through \(13\), exponent caps \(5\), and square-free tail. The present bound is a strict numerical strengthening, not a claim to the multiplicativity or cylinder-sieve mechanism. It differs in the ten-prime tailored valuation certificate, its elementary rational tail enclosure, and the resulting independently checkable rational threshold \(\delta>0.77\). OEIS A322446 records finite-range counts and an approximate limiting proportion, but those counts do not imply any rigorous bound above \(77\%\).

## Limitations
The bound is not an exact evaluation of the density. Its ten-prime exponent bounds are sufficient choices rather than claimed optimal. The computation is a finite exhaustive certificate whose validity depends on the inspectable standalone code and exact integer identities; the analytic tail and density argument is independent of that program. Searches did not establish historical priority exhaustively; a stronger unindexed published bound could exist. This result does not address whether there are infinitely many equality cases \(\sigma^*(n)=\sigma^{(e)}(n)\).

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, first posted 2013-12-17; Publ. Inst. Math. (Beograd) 97 (2015), 175--180.
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary--exponential divisor-sum comparison density*, published research result, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82 .
3. OEIS A322446, counts of \(\sigma^*(n)>\sigma^{(e)}(n)\) below powers of ten, https://oeis.org/A322446 .
