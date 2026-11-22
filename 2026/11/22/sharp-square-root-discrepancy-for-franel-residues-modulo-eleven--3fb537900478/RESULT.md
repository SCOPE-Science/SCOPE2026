# Sharp square-root discrepancy for Franel residues modulo eleven

## Finding

For the Franel numbers
\[
f(n)=\sum_{j=0}^{n}\binom nj^3\qquad(n\ge0),
\]
write \(C_r(a)=\#\{0\le n<11^r:f(n)\equiv a\pmod {11}\}\), for an integer \(r\ge0\) and \(a\in\mathbb F_{11}\). Then \(C_r(0)=0\) for every \(r\), and all ten nonzero residues occur when \(r\ge2\). Define the exact centered variance
\[
V_r=\sum_{a\in\mathbb F_{11}^{\times}}\left(C_r(a)-\frac{11^r}{10}\right)^2.
\]
For every \(r\ge0\),
\[
\boxed{V_r=\frac{4\cdot11^r+2(6+\sqrt5)^r+2(6-\sqrt5)^r+1}{10}.}
\]
More strongly, for every integer \(N\ge1\) and every nonzero residue \(a\pmod {11}\),
\[
\boxed{\left|\#\{0\le n<N:f(n)\equiv a\pmod {11}\}-\frac N{10}\right|\le
\frac{9\sqrt{11}}{\sqrt{11}-1}\sqrt N.}
\]
This exponent \(1/2\) is optimal: for every \(r\ge0\), at least one nonzero residue \(a\) satisfies
\[
\left|C_r(a)-11^r/10\right|\ge\frac15\,11^{r/2}.
\]
In particular, the ten unit residues each have natural density \(1/10\), residue zero never occurs, and no bound of order \(O(N^{\theta})\), uniformly in the residue, can hold with \(\theta<1/2\). For a fixed residue, the lower bound holds along infinitely many powers of eleven for at least one residue by the pigeonhole principle.

## Assumptions and scope

The index \(n\) is a nonnegative integer; the target residue is taken modulo the **prime eleven**, not modulo its higher powers. A complete block has indices \(0\le n<11^r\), and a general cutoff is \(0\le n<N\). Congruences, frequencies, and lower bounds refer to these exact ranges. The prime eleven is the first of \(5,7,11\) whose eleven-digit Franel table has no zero residue: the digits \(2\) at prime five and \(3\) at prime seven already give zeros there. No general claim for every prime is made.

## Proof

**1. Digit product.** For base-eleven digits \(n=\sum_{i\ge0}d_i11^i\), Lucas's binomial congruence gives
\[
f(n)\equiv\prod_{i\ge0}f(d_i)\pmod {11}.
\]
Indeed, Lucas's theorem makes every summand with a forbidden digit of the summation index vanish, while the remaining binomial cubes factor digit by digit. Direct integer evaluation of the eleven one-digit sums gives
\[
(f(0),\ldots,f(10))\bmod 11=(1,2,10,1,5,8,4,9,6,8,1).
\]
Every entry is a unit, proving that eleven never divides a Franel number.

**2. Exact multiplicative-digit convolution.** Two generates \(\mathbb F_{11}^{\times}\), and the successive powers of two are
\[
(1,2,4,8,5,10,9,7,3,6).
\]
The multiplicities of those ten values in the one-digit Franel table are
\[
c=(3,1,1,2,1,1,1,0,0,1).
\]
Put \(P(X)=3+X+X^2+2X^3+X^4+X^5+X^6+X^9\). If \(a\equiv2^j\pmod {11}\), then \(C_r(a)\) is exactly the coefficient of \(X^j\) in \(P(X)^r\) reduced modulo \(X^{10}-1\). Equivalently, for \(\zeta=\exp(2\pi i/10)\),
\[
C_r(2^j)=\frac1{10}\sum_{h=0}^{9}\zeta^{-jh}P(\zeta^h)^r.
\]
This gives an explicit exact formula for **every** residue frequency, not only its variance. The cyclic square \(c*c\) equals
\[
(14,10,12,16,13,14,14,8,8,12),
\]
so all nonzero residues occur at depth two. Since \(c_0=3>0\), positivity persists at larger depths.

**3. Cyclotomic spectral cancellation.** Let \(Q(X)=P(X)P(X^{-1})\) in \(\mathbb Z[X]/(X^{10}-1)\). Its coefficient vector is
\[
(19,13,10,12,11,10,11,12,10,13).
\]
Exact monic polynomial division yields
\[
\begin{aligned}
Q(X)&\equiv121 &&\pmod{X-1},\\
Q(X)&\equiv1 &&\pmod{X+1},\\
Q(X)&\equiv5-2X^2-2X^3 &&\pmod{X^4+X^3+X^2+X+1},\\
Q(X)&\equiv11 &&\pmod{X^4-X^3+X^2-X+1}.
\end{aligned}
\]
It follows that, for \(h=1,\ldots,9\), the nine squared moduli \(|P(\zeta^h)|^2\), with multiplicity, are \(11\) four times, \(6+\sqrt5\) twice, \(6-\sqrt5\) twice, and \(1\) once. For the fifth roots, use \(\zeta^{2}+\zeta^{-2}=2\cos(2\pi/5)=(\sqrt5-1)/2\), and \(\zeta^{4}+\zeta^{-4}=2\cos(4\pi/5)=-(1+\sqrt5)/2\); the two values arise from the exponents \(2,8\) and \(4,6\) respectively. This is an exact identity in cyclotomic integer rings, not a numerical spectral estimate.

The discrete Fourier Parseval identity now gives
\[
\sum_{a\ne0}\left(C_r(a)-11^r/10\right)^2
=\frac1{10}\sum_{h=1}^9 |P(\zeta^h)|^{2r},
\]
which is the claimed closed formula, including \(r=0\).

**4. Global square-root bound.** The spectral calculation shows \(|P(\zeta^h)|\le\sqrt{11}\) whenever \(h\ne0\). Inverting the Fourier formula therefore gives
\[
|C_r(a)-11^r/10|\le(9/10)11^{r/2}.
\]
Any aligned block \([b11^r,(b+1)11^r)\) has a residue distribution obtained from \((C_r(a))\) by multiplying all output residues by \(f(b)\), because the fixed prefix and variable suffix separate into base-eleven digits. Thus the same deviation bound holds in every aligned block. For \(11^L\le N<11^{L+1}\), the base-eleven expansion partitions \([0,N)\) into at most ten aligned blocks of each length \(11^j\), \(0\le j\le L\). Adding the deviations gives
\[
|C_N(a)-N/10|\le9\sum_{j=0}^L11^{j/2}
\le\frac{9\sqrt{11}}{\sqrt{11}-1}\sqrt N.
\]
Here \(C_N(a)\) denotes the non-block frequency at cutoff \(N\), not \(C_r(a)\).

**5. Optimality.** The exact variance gives \(V_r\ge(2/5)11^r\). Among ten nonnegative squared deviations, one is at least \(V_r/10\ge 11^r/25\). Hence its absolute deviation is at least \(11^{r/2}/5\). This proves the sharp exponent; no numerical experiment is used in the infinite argument.

## Verification

The included standalone `check.py` uses only the Python standard library and can be executed with `python3 check.py`. It evaluates the first eleven Franel values exactly, checks Lucas digit products against direct binomial-cube sums for indices below \(160\), verifies the four exact cyclotomic polynomial remainders, and compares full integer convolution histograms and the variance formula through \(r=8\). Complete independent digit enumeration of the index range is also compared through \(r=4\). The checker is corroborating finite evidence; the proof above establishes every depth and every cutoff.

## Relationship to prior work

Franel's classical definition and recurrence go back to 1894. Zhi-Wei Sun's *Congruences for Franel numbers* (first preprint December 5, 2011) establishes finite sums and prime-square congruences for these same numbers, but its stated results are not frequency formulas for individual Franel values. Zhi-Hong Sun's *Congruences for sums involving Franel numbers* (published online July 31, 2017) treats weighted finite sums at primes rather than complete blocks of individual output residues. Henningsen–Straub's *Generalized Lucas congruences and linear p-schemes* (November 16, 2021) gives a general framework for digit-multiplicative congruences. The elementary Lucas product is the starting point here; the special cyclotomic cancellation, complete variance, and sharp arbitrary-cutoff exponent require the explicit eleven-digit Franel data and are not stated by that general framework. An earlier implicit derivation of the same special spectral identity may exist; no claim of independently verified publication priority is made.

## Limitations

This theorem concerns output values modulo eleven only; it does not classify values modulo \(11^k\) for \(k\ge2\). Its distribution statement is for the ten nonzero residues; zero never occurs. The sharpness argument forces a large discrepancy at some unit residue for each full block, and a single fixed residue along infinitely many full blocks, but does not identify that fixed residue or provide an asymptotic sign pattern. The literature comparison is not an exhaustive mathematical-priority certificate, and independent mathematical validation has not been performed.

## References

1. Z.-W. Sun, *Congruences for Franel numbers*, arXiv:1112.1034, initially posted December 5, 2011, https://arxiv.org/abs/1112.1034.
2. Z.-H. Sun, *Congruences for sums involving Franel numbers*, published online July 31, 2017, https://maths.hytc.edu.cn/__local/3/45/77/77F7497DDFD531E8688ED13C0D0_262306C8_24EB4.pdf.
3. J. A. Henningsen and A. Straub, *Generalized Lucas congruences and linear p-schemes*, arXiv:2111.08641, posted November 16, 2021, https://arxiv.org/abs/2111.08641.
4. OEIS, A000172, Franel numbers, https://oeis.org/A000172.
