# Neighboring-base repunit GCD growth and the exact twelve-digit spectrum

## Finding
For integers \(m\ge2\), \(h\ge1\), and \(b\ge2\), define the length-\(m\) repunit in base \(b\) and its cross-base greatest common divisor by
\[
R_m(b)=\sum_{j=0}^{m-1}b^j=\frac{b^m-1}{b-1},\qquad
G_{m,h}(b)=\gcd(R_m(b),R_m(b+h)).
\]
Define \(D_{m,h}(b)=b^2+b+1\) when \(h=1\) and \(6\mid m\), and \(D_{m,h}(b)=1\) otherwise. Then **for every fixed pair \((m,h)\)** there is a positive integer \(C_{m,h}\) such that
\[
E_{m,h}(b):=\frac{G_{m,h}(b)}{D_{m,h}(b)}\quad\text{is an integer dividing }C_{m,h}
\]
for all \(b\ge2\), and \(E_{m,h}(b)\) is periodic with period dividing \(C_{m,h}\). In particular, \(G_{m,h}(b)\) is unbounded as \(b\to\infty\) **if and only if** \(h=1\) and \(6\mid m\); in that case \(G_{m,1}(b)\asymp_m b^2\). Thus no shift of at least two bases produces an unbounded GCD.

At the first exceptional length \(m=6\), the precise formula is
\[
\frac{G_{6,1}(b)}{b^2+b+1}=
\begin{cases}
7,&b\equiv3,5\pmod7,\\
1,&\text{otherwise}.
\end{cases}
\]
At the next exceptional length \(m=12\), put
\[
T_5=\{2,3\},\quad T_7=\{3,5\},\quad
T_{13}=\{2,4,5,6,7,8,10,11\}.
\]
Then the full exact law, for every integer base \(b\ge2\), is
\[
\boxed{\frac{G_{12,1}(b)}{b^2+b+1}=
\prod_{p\in\{5,7,13\}}p^{\mathbf1_{\{b\bmod p\in T_p\}}}.}
\]
Its eight values are **exactly all divisors of \(455\)**, and its least positive period is **\(455\)**. Over one period, the respective multiplicities for values \(1,5,7,13,35,65,91,455\) are
\[
(75,50,30,120,20,80,48,32).
\]
Thus each divisor \(d\mid455\) has exact natural frequency
\[
\frac{1}{455}\prod_{p\in\{5,7,13\}}
\begin{cases}|T_p|,&p\mid d,\\p-|T_p|,&p\nmid d.\end{cases}
\]
The corresponding six-digit probabilities are \(5/7\) for multiplier \(1\) and \(2/7\) for multiplier \(7\).

## Assumptions and scope
The base \(b\) is an integer at least two, the shift \(h\) is a positive integer, and the length \(m\) is an integer at least two. The notation \(\asymp_m\) means bounds above and below by positive constants depending on the fixed length \(m\). The density assertion concerns uniformly sampled positive integer bases in long intervals. No assumption of primality of \(b\) or of the repunit values is made. The exact finite spectra are proved only for lengths six and twelve; the growth dichotomy and periodic bounded quotient hold for every length and shift.

## Proof
**1. The unique common cyclotomic factor.** Write \(P_m(X)=1+X+\cdots+X^{m-1}\). Its complex zeros are precisely the nonidentity \(m\)-th roots of unity, all simple. A common zero \(z\) of \(P_m(X)\) and \(P_m(X+h)\) must satisfy \(|z|=|z+h|=1\), whence \(\operatorname{Re}z=-h/2\). For integer \(h>2\) there is no solution; for \(h=2\), the sole possibility \(z=-1\) gives \(z+h=1\), which is not a zero of \(P_m\). For \(h=1\), the solutions are the two primitive cube roots \(z=(-1\pm i\sqrt3)/2\), and their translates \(z+1\) are primitive sixth roots. Both are roots of \(P_m\) exactly when \(6\mid m\). All these roots are simple; consequently
\[
\gcd_{\mathbb Q[X]}(P_m(X),P_m(X+h))=
\begin{cases}X^2+X+1,&h=1,\ 6\mid m,\\1,&\text{otherwise},\end{cases}
\]
where the GCD is monic. This also proves that the indicated quadratic divides **both** integer polynomials.

**2. Uniform boundedness of the quotient.** Let \(D_{m,h}(X)\) be that monic common factor (or \(1\)), and set \(A_{m,h}(X)=P_m(X)/D_{m,h}(X)\), \(B_{m,h}(X)=P_m(X+h)/D_{m,h}(X)\). These are monic integral polynomials without a common complex zero. Their integer Sylvester resultant \(C_{m,h}=|\operatorname{Res}(A_{m,h},B_{m,h})|\) is positive. The integer resultant Bézout identity implies that \(\gcd(A_{m,h}(b),B_{m,h}(b))\) divides \(C_{m,h}\). Since \(G_{m,h}(b)=D_{m,h}(b)\gcd(A_{m,h}(b),B_{m,h}(b))\), this proves the divisor bound. Both evaluations are unchanged modulo \(C_{m,h}\) when \(b\) increases by that modulus, and their GCD divides it; therefore the quotient is periodic. If the quadratic factor is absent the GCD is bounded, while if it is present it is between \(b^2+b+1\) and \(C_{m,1}(b^2+b+1)\). This proves the full growth classification.

**3. Length six.** Direct factorization after removing \(X^2+X+1\) gives
\[
A_{6,1}(X)=X^3+1,\qquad
B_{6,1}(X)=(X+2)(X^2+3X+3).
\]
An explicit integral Bézout identity is
\[
(-4X^2-15X-16)A_{6,1}(X)+(4X^2-5X+5)B_{6,1}(X)=14.
\]
The two evaluations have opposite parity: when \(b\) is even, \(A_{6,1}(b)\) is odd; when \(b\) is odd, \(B_{6,1}(b)\) is odd. Thus their GCD divides seven. Direct reduction modulo seven shows the two common zeros are exactly \(b\equiv3,5\pmod7\). This proves the six-digit formula without relying on any finite sampling.

**4. Length twelve and the exact local certificate.** The quotient polynomials factor over \(\mathbb Z[X]\) as
\[
\begin{aligned}
A_{12,1}(X)&=(X+1)(X^2+1)(X^2-X+1)(X^4-X^2+1),\\
B_{12,1}(X)&=(X+2)(X^2+3X+3)(X^2+2X+2)\\
&\qquad\cdot(X^4+4X^3+5X^2+2X+1).
\end{aligned}
\]
An exact Sylvester determinant computation yields
\[
|\operatorname{Res}(A_{12,1},B_{12,1})|
=2^{10}5^2 7^2 13^8=1023252616422400.
\]
Hence a common prime divisor of the quotient evaluations must be among \(2,5,7,13\). Reduction of the displayed factorizations modulo these primes gives no common root modulo two and precisely the sets \(T_5,T_7,T_{13}\) above at the three odd primes.

It remains essential to exclude *simultaneous* divisibility by the squares of those primes; the exponents in the resultant alone do not accomplish this. For each listed root \(r\pmod p\), both derivatives \(A'_{12,1}(r)\) and \(B'_{12,1}(r)\) are nonzero modulo \(p\). The unique lift \(r+pt_A\) satisfying \(A_{12,1}(r+pt_A)\equiv0\pmod{p^2}\) and the analogous lift \(r+pt_B\) for \(B_{12,1}\) have the following \((t_A,t_B)\) pairs, in order of the stated root sets:

| Prime | Roots in increasing order | Lift digits \((t_A,t_B)\), in that order |
|---|---|---|
| \(5\) | \(2,3\) | \((1,3),(3,4)\) |
| \(7\) | \(3,5\) | \((4,2),(2,6)\) |
| \(13\) | \(2,4,5,6,7,8,10,11\) | \((6,11),(11,5),(5,1),(1,11),(11,7),(7,1),(1,6),(6,12)\) |

Indeed \(t_A\equiv -(A_{12,1}(r)/p)(A'_{12,1}(r))^{-1}\pmod p\), and similarly for \(t_B\). Every displayed pair has unequal entries. Hence no integer \(b\) gives a common root modulo \(p^2\), for any \(p\in\{5,7,13\}\). The GCD of the quotient evaluations is therefore squarefree with exactly the asserted prime-divisibility criteria, establishing the twelve-digit formula.

**5. Sharp period and frequencies.** The Chinese remainder theorem gives, independently for each \(p\in\{5,7,13\}\), \(|T_p|\) residue choices for presence of \(p\) and \(p-|T_p|\) for its absence. This gives all eight divisors, the exact counts and their densities. A period of the quotient must also be a period of each indicator \(\mathbf1_{\{b\bmod p\in T_p\}}\), because the factors are distinct primes. A nonempty proper subset of the cyclic group \(\mathbb Z/p\mathbb Z\) has least period \(p\) for prime \(p\). Thus any period is divisible by all three primes. The exhibited period \(455\) is therefore minimal.

## Verification
The accompanying `checker.py` uses only the Python standard library. It reconstructs the displayed quotient polynomials by multiplication, checks the resultant by exact fraction-free elimination on the Sylvester matrix, enumerates every residue modulo \(2\), \(5^2\), \(7^2\), and \(13^2\), checks all 455 base residue classes, and independently compares direct repunit GCDs for 4,000 consecutive positive bases at each of the two exceptional lengths. These computations validate the finite modular certificate and arithmetic; the all-length root-of-unity and resultant argument above, not sampling, proves the infinite statement. Run with `python3 checker.py`.

## Relationship to prior work
Komatsu (first preprint September 2022, primary MSC 11D07) treats shifted geometric sequences and discusses repunits in the context of Frobenius representation questions, motivating an independent multiplicative question: the shared divisors of a fixed repunit length across differing bases. Its hypotheses and conclusions concern additive representations, not neighboring-base GCDs. Bodin, Dèbes and Najib (first preprint 2020) and Bodin and Dèbes (first preprint 2021) prove general periodicity and finiteness for the GCD of values of *coprime* integral polynomials. Frenkel and Pelikán (first preprint 2016) establish the resultant divisibility and analyze the special case of squarefree resultants. Those general results underlie step 2; the periodicity principle itself is **not claimed as new**. The present specific contributions are the *unique-shift and length* classification of polynomial common factors for repunit pairs, and the exact, non-squarefree-resultant twelve-digit spectrum and sharp period, including all finite prime-power obstructions. Ruiz (2025) discusses base-change congruences of repunits, but the inspected Section 6 does not formulate this cross-base GCD spectrum. See the references for provenance.

## Limitations
The explicit complete normalized GCD spectra are determined only at the first two exceptional lengths, six and twelve. For other lengths divisible by six, the resultant procedure yields an effective finite bound and period but not a closed smallest period or full frequency table. The searches and primary texts inspected do not establish an equivalent statement, but unindexed number-theory literature could contain one; mathematical publication priority is not independently certified. This is an elementary exact theorem, with no claim about primality of the repunit values.

## References
1. T. Komatsu, *The Frobenius number for shifted geometric sequences associated with the number of solutions*, first public preprint 27 September 2022 (primary MSC 11D07), https://arxiv.org/abs/2209.13118 .
2. A. Bodin, P. Dèbes and S. Najib, *Prime and coprime values of polynomials*, first public preprint 6 February 2020, https://arxiv.org/abs/2002.02292 .
3. A. Bodin and P. Dèbes, *Coprime values of polynomials in several variables*, first public preprint 28 May 2021, https://arxiv.org/abs/2105.13883 .
4. P. E. Frenkel and J. Pelikán, *On the greatest common divisor of the value of two polynomials*, first public preprint 29 August 2016, https://arxiv.org/abs/1608.07936 .
5. D. E. Ruiz, *An introduction to generalized repunit numbers*, public version March 2025, https://www.researchgate.net/publication/389438226_AN_INTRODUCTION_TO_GENERALIZED_REPUNIT_NUMBERS .
