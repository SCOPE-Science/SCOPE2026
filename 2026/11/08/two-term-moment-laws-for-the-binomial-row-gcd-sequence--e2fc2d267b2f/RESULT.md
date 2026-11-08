# Two-term moment laws for the binomial row GCD sequence

## Finding
For integers \(k\ge2\) define
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
Then for every fixed real \(s>0\), with \(X\to\infty\),
\[
\boxed{\sum_{2\le k\le X}D(k)^s
=\frac{X^{s+1}}{(s+1)\log X}\left(\zeta(s+1)+\frac{\zeta(s+1)/(s+1)-\zeta'(s+1)}{\log X}+O_s((\log X)^{-2})\right).}
\]
The implied constant may depend on the fixed exponent \(s\). For \(s=1\), the first two nonzero terms are
\[
\frac{\pi^2X^2}{12\log X}
+\frac{X^2}{2(\log X)^2}\left(\frac{\zeta(2)}2-\zeta'(2)\right).
\]

## Assumptions and scope
The argument is unconditional and uses the prime number theorem and the 2026 prime-power criterion for the binomial GCD. A sum over integer indices \(k\) with \(2\le k\le X\) is understood for real \(X\ge2\). Only fixed positive real moments are asserted; the estimate is not uniform as \(s\downarrow0\). Write \(p^a\parallel n\) for the maximal exact prime-power component of \(n\) supported on the prime \(p\).

## Proof
**Divisibility lemma.** For every \(k\ge2\), \(D(k)\mid k+1\). Set \(F(x)=\binom{kx}{k}\), a degree-\(k\) polynomial with integer values at nonnegative integer arguments. Its forward differences are integer valued there. Modulo \(D(k)\), we have \(F(1)=1\) and \(F(2)=\cdots=F(k+1)=0\). Therefore \(\Delta^jF(1)\equiv(-1)^j\pmod{D(k)}\) for each \(0\le j\le k\). Newton's finite interpolation formula at \(x=0\) yields
\[
0=F(0)=\sum_{j=0}^{k}\binom{-1}{j}\Delta^jF(1)
\equiv k+1\pmod{D(k)}.
\]
This strengthens the prime-support observation in the motivating source; it is proved here to control prime-power errors independently of any exact valuation formula.

**Dominant rows.** The prime-primary criterion of Guo, Qiu, Cao, Feng and Gao [1, Theorem 1 and primary criterion] says that, for \(n=k+1=p^a b\), with \(p\nmid b\),
\[
p\mid D(k)\quad\Longleftrightarrow\quad b\le p^a.
\]
Because \(\gcd(b,p)=1\), equality is impossible. Thus the condition is \((p^a)^2>n\), and at most one exact prime-power component meets it. If this component has exponent one, \(n=pm\) with \(p\) prime and \(p>m\); the divisibility lemma forces \(D(n-1)=p\). Otherwise \(D(n-1)=1\) or the sole positive component has exponent at least two, and then \(1<D(n-1)\le p^a\).

**Exceptional prime powers.** For \(Y\ge2\), the number of prime powers \(t=p^a\le Y\) with \(a\ge2\) is \(O(\sqrt{Y}\log Y)\): count possibilities separately for each exponent \(a\ge2\). Fix \(s>0\), and let \(E_s(X)\) be the total \(s\)-th moment contributed by integers \(n\le X\) possessing a component \(t=p^a\) with \(a\ge2\) and \(t^2>n\). Since \(n=tb\), \(1\le b<t\), and \(D(n-1)^s\le t^s\),
\[
E_s(X)\le\sum_{\substack{t=p^a\le X\\ a\ge2}}t^s\min(t,X/t)
=O_s\left(X^{s+1-\delta_s}\log X\right),
\qquad \delta_s=\tfrac12\min(s,1)>0.
\]
Indeed, the subsum for \(t\le\sqrt X\) is \(O_s(X^{s/2+3/4}\log X)\); for \(t>\sqrt X\) it is \(O_s(X^{1+s/2}\log X)\) when \(s<1\), or \(O_s(X^{s+1/2}\log X)\) when \(s\ge1\). The remaining unit-valued rows contribute at most \(X\), which is also negligible on every required logarithmic scale.

**Prime-weighted moment.** It therefore suffices to compute
\[
T_s(X)=\sum_{m\le\sqrt X}\ \sum_{m<p\le X/m}p^s.
\]
The weighted prime number theorem, by partial summation, gives for every fixed \(s>0\), as \(Y\to\infty\),
\[
\sum_{p\le Y}p^s
=\frac{Y^{s+1}}{(s+1)\log Y}
\left(1+\frac1{(s+1)\log Y}+O_s((\log Y)^{-2})\right).
\]
The subtraction \(\sum_{m\le\sqrt X}\sum_{p\le m}p^s\) is \(O_s(X^{(s+2)/2})\). The portion with \(m>X^{1/4}\) contributes \(O_s(X^{s+1-s/4}/\log X)\), using the uniform upper bound for weighted prime sums and \(m\le\sqrt X\). Hence restrict to \(m\le X^{1/4}\), put \(L=\log X\) and \(u=\log m\), and expand
\[
\frac1{L-u}=\frac1L+\frac{u}{L^2}+O\left(\frac{u^2}{L^3}\right),\qquad
\frac1{(L-u)^2}=\frac1{L^2}+O\left(\frac{u}{L^3}\right).
\]
The sums \(\sum_{m\ge1}m^{-s-1}\), \(\sum_{m\ge1}(\log m)m^{-s-1}\), and \(\sum_{m\ge1}(\log m)^2m^{-s-1}\) converge. Their first two values are \(\zeta(s+1)\) and \(-\zeta'(s+1)\). Summing the expansions gives the asserted two-term moment law, with error \(O_s(X^{s+1}/(\log X)^3)\). Replacing \(X\) by \(X+1\) to restore \(n=k+1\), and omitting the isolated row \(n=2\), changes the sum by a smaller term. This completes the proof.

## Verification
The included `verify.py` uses exact integer arithmetic. It compares direct binomial GCDs for \(2\le k\le40\) against a separate digit-length valuation computation; it also enumerates all rows through one million and checks the large-prime and repeated-prime-power decomposition exactly. `verify_output.txt` is the output of running that program with Python 3. Its measured first-moment ratios decrease from about \(1.212\) at \(X=1000\) to about \(1.092\) at \(X=10^6\), consistent with slow logarithmic convergence; no finite numerical check is used to prove the asymptotic.

## Relationship to prior work
Guo, Qiu, Cao, Feng and Gao [1] prove the exact prime-support criterion for this same binomial-GCD family; they do not state its positive-moment distribution. The novelty claimed here is the complete positive-real moment family with the explicit first logarithmic correction, not the underlying GCD criterion or standard weighted prime number theorem. Hong [2] treats a different GCD in which the upper binomial index is fixed and the lower indices vary over a coprimality-restricted range. No priority is claimed for classical prime-summation tools.

## Limitations
This does not give uniform control as the moment exponent approaches zero, pointwise bounds on the GCD beyond those already implicit in the known criterion, or an independently reviewed proof. The second-order coefficient is conditional only on standard unconditional analytic number-theory estimates, not on conjectures. Earlier unindexed moment computations cannot be ruled out.

## References
[1] D. Guo, R. Qiu, Y. Cao, R. Feng, X.-S. Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997, first posted 2026-06-22, https://arxiv.org/abs/2606.22997 ; accessible full text https://www.researchgate.net/publication/407506744_A_Greatest_Common_Divisor_Criterion_of_Certain_Binomial_Coefficients .

[2] S. Hong, *The greatest common divisor of certain binomial coefficients*, C. R. Math. 354 (2016), 756–761, https://doi.org/10.1016/j.crma.2016.06.001 .
