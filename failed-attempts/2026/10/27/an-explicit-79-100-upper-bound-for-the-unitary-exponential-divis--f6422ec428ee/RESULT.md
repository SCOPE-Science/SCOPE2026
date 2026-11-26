# An explicit \(79/100\) upper bound for the unitary–exponential divisor-sum comparison density

## Finding

Let \(\sigma^*(n)\) be the sum of unitary divisors of a positive integer, and let \(\sigma^{(e)}(n)\) be the sum of its exponential divisors. Write
\[
\delta=\lim_{X\to\infty}\frac{1}{X}\#\{1\le n\le X:\sigma^*(n)>\sigma^{(e)}(n)\}.
\]
The density exists by the distribution result cited in [1]. We prove the **strict explicit upper bound**
\[
\boxed{\delta<\frac{79}{100}.}
\]
More precisely, an exact finite-cylinder and moment certificate proves that the density of the complementary strict inequality \(\sigma^*(n)<\sigma^{(e)}(n)\) is at least
\[
L=\frac{13987674381253581924762057363332735566612039694216294400}{66269304071072984530235058557882269285612800000000000000}
  =0.2110732046657979\ldots>\frac{21}{100}.
\]
Thus the first displayed strict upper bound follows without relying on numerical sampling of integers.

## Assumptions and scope

For a prime \(p\), write \(v_p(n)\) for its exponent in \(n\). The two functions are positive and multiplicative; their prime-power factors satisfy
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d\quad(a\ge1),
\]
with both functions equal to \(1\) at \(p^0\). Define
\[
\rho_p(0)=1,\qquad \rho_p(a)=\frac{p^a+1}{\sum_{d\mid a}p^d}\quad(a\ge1).
\]
Then \(\sigma^*(n)/\sigma^{(e)}(n)=\prod_p\rho_p(v_p(n))\). For \(a=1\), \(\rho_p(1)=1+1/p\); for every \(a\ge2\), \(\rho_p(a)<1\) because the denominator contains \(p^a+p\), with \(p>1\).

The finite certificate fixes valuations at \(P_0=\{2,3,5,7,11,13,17,19\}\), using respective upper caps \((10,6,4,3,3,2,2,2)\). At \(P_1=\{23,29,31,37,41,43\}\), it records only whether the valuation equals \(1\), treating every other valuation conservatively as having ratio \(1\). Primes \(p\ge47\) form the unrestricted tail. The constants and finite choices are sufficient for the bound, not asserted optimal.

## Proof

**1. A finite multiplicative majorant.** For every prime in \(P_1\), define \(h_p(n)=1+1/p\) if \(v_p(n)=1\) and \(h_p(n)=1\) otherwise. Since \(\rho_p(a)\le1\) for \(a\ne1\), we have
\[
\prod_{p\in P_0\cup P_1}\rho_p(v_p(n))\le
R(n):=\prod_{p\in P_0}\rho_p(v_p(n))\prod_{p\in P_1}h_p(n).
\]
For an exponent vector \((a_p)_{p\in P_0}\) within the stated caps, its exact natural density is \(\prod_{p\in P_0}(p-1)/p^{a_p+1}\). Independently, at a prime \(p\in P_1\), the events \(v_p(n)=1\) and \(v_p(n)\ne1\) have respective densities \((p-1)/p^2\) and \((p^2-p+1)/p^2\). Every resulting finite pattern is an exact union of residue classes modulo a fixed integer, so multiplication of these densities is justified by the Chinese remainder theorem.

The attached program enumerates all \(\prod_{p\in P_0}(A_p+1)=166320\) permitted exponent vectors, sorts their exact rational factors, and combines them with the \(2^6=64\) exact statuses at \(P_1\). For increasing rational endpoints \(q_i\), the integers \(m_i\) computed by that program are the exact probability numerators for the disjoint events
\[
E_i=\{q_{i-1}<R(n)\le q_i\},
\]
restricted to the permitted \(P_0\)-exponents, with \(q_0=0\) and the denominators given by
\[
D=\prod_{p\in P_0}p^{A_p+1}\prod_{p\in P_1}p^2
=66269304071072984530235058557882269285612800000.
\]
Thus \(\operatorname{dens}(E_i)=m_i/D\), exactly. The smallest and largest endpoints are \(3/4\) and \(99/100\); the full list is encoded as exact rational pairs in `verify_upper_079.py`.

**2. Uniform control of all larger primes.** For any positive integer \(k\), put
\[
Z(n)=\prod_{p\ge47}\max\{1,\rho_p(v_p(n))\}
=\prod_{\substack{p\ge47\\v_p(n)=1}}\left(1+\frac1p\right).
\]
For a finite set of such primes, independence of exact prime-exponent statuses in natural density gives
\[
\mathbb E Z(n)^k
=\prod_p\left(1+\frac{p-1}{p^2}\left[\left(1+\frac1p\right)^k-1\right]\right)
\le\exp(S_k),
\]
where
\[
S_k=\sum_{p\ge47}\frac{(1+1/p)^k-1}{p}.
\]
The sum is finite for every fixed \(k\). For primes \(47\le p\le1000\), the certificate sums the rational terms explicitly; for the remaining primes it uses only
\[
\sum_{p>1000}\frac{(1+1/p)^k-1}{p}
\le\sum_{j=1}^{k}\binom kj\sum_{m>1000}m^{-j-1}
\le\sum_{j=1}^{k}\frac{\binom kj}{j\,1000^j}.
\]
The finite-prime expectations converge to the corresponding infinite-prime model because the expected sum of positive logarithmic contributions from primes \(p>Y\) is at most \(\sum_{m>Y}m^{-2}\), which tends to zero. This also allows finite-sieve estimates to pass to lower natural densities of strict negative-comparison events. By Markov's inequality, for \(0<q<1\),
\[
\Pr\{Z\ge q^{-1}\}\le q^k\exp(S_k).
\]
The attached integer-only verifier bounds \(S_k\) from above by rounding each rational summand upward at scale \(10^{12}\). It bounds its exponential by an upward-rounded Taylor expansion to degree \(80\), with a separately proved tail smaller than \(10^{-12}\) for the encountered \(S_k<9\). It then rounds \(q^k\exp(S_k)\) **upward** to multiples of \(10^{-9}\). This produces verified integer bounds \(b_i\) on \(10^9\Pr\{Z\ge q_i^{-1}\}\); no floating-point comparison enters the certificate.

**3. Combining disjoint certificates.** If \(E_i\) holds and \(Z(n)<q_i^{-1}\), then the full prime-factor ratio is bounded strictly by \(R(n)Z(n)<1\). Events for disjoint \(i\) remain disjoint. The limiting proportion of integers satisfying the strict reverse inequality is therefore at least
\[
\sum_i \frac{m_i}{D}\left(1-\frac{b_i}{10^9}\right)
=\frac{13987674381253581924762057363332735566612039694216294400}{66269304071072984530235058557882269285612800000000000000}.
\]
The independent integer comparison carried out in the certificate is
\[
100\cdot13987674381253581924762057363332735566612039694216294400
-21\cdot66269304071072984530235058557882269285612800000000000000
=7112052632825517341269506617745901663335169421629440000>0.
\]
Hence the strict negative-comparison density is greater than \(21/100\). The positive-comparison density \(\delta\) is at most one minus that density, establishing \(\delta<79/100\). \(\square\)

## Verification

Run `python3 verify_upper_079.py` with Python 3.9 or later. The program uses only `itertools`, `math`, `fractions`, and `bisect`; no external packages, files, or network services are needed. It prints all \(26\) exact bin masses and conservative failure bounds, the two exact integer sides of the final strict inequality, and `VERIFY_OK` if the certificate passes. The recorded output is also embedded in `certificate_output.txt`; direct replay yielded a certified negative-density lower bound \(0.2110732046657979\ldots\). Finite exact arithmetic certifies the explicit constants, while the analytic prime-tail argument (not finite enumeration) covers infinitely many integers and all remaining primes.

## Relationship to prior work

Trudgian [1, Section 4] asks for the density \(\delta\), proves the squarefree lower bound \(6/\pi^2\), and reports a finite-range proportion about \(0.778307\). A subsequent published finite-cylinder argument [2] supplies the substantially stronger **lower** bound \(\delta\ge0.753659844\ldots\), which does not imply an upper bound. The present theorem controls the opposite inequality using a complementary mix of exact prime-power cylinders and rigorous moments of the unrestricted prime tail. It improves an earlier checked upper estimate \(\delta\le0.7979594789\ldots\) by more than \(0.0079\) at the level of the stated constant. It does not determine \(\delta\) exactly.

## Limitations

This is an explicit, nonoptimal upper bound, not an evaluation of the density or a proof of its decimal expansion. All computational claims refer to exact integer calculations replayed from the accompanying script. The explicit comparison against accessible prior work is bounded; unindexed literature remains a residual originality risk. The proof does not use the empirical proportion as evidence for its inequality.

## References

[1] T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (first public 2013-12-17); *Publ. Inst. Math. (Beograd)* 97 (2015), 175–180; DOI 10.2298/PIM140617001T. Sections 1.2 and 4.

[2] *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, publicly accessible mathematical research result (2026-10-04), complete `RESULT.md` (read in full); available publicly under the quoted title.

[3] OEIS A322446, enumeration of strict unitary-divisor-sum dominance through powers of ten (used only as numerical context, not in the proof).
