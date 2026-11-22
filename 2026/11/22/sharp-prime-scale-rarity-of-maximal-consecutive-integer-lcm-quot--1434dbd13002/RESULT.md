# Sharp prime-scale rarity of maximal consecutive-integer LCM quotients

## Finding
For integers \(k\ge2\), \(n\ge1\), put
\[
g_k(n)=\frac{\prod_{i=0}^{k}(n+i)}{\operatorname{lcm}(n,n+1,\ldots,n+k)}.
\]
The greatest possible value of \(g_k(n)\) is exactly \(k!\). Its natural-density frequency
\[
d_k=\lim_{X\to\infty}\frac1X\#\{1\le n\le X:g_k(n)=k!\}
\]
exists and is positive for every fixed \(k\). The following sharp prime-scale decay law holds as the window length tends to infinity:
\[
\boxed{\lim_{k\to\infty}\frac{\log k}{k}\log d_k=-\mathcal C,\qquad
\mathcal C=\sum_{j=1}^{\infty}\frac{\log(1+1/j)}{j}
=1.2577468869443696\ldots .}
\]
Equivalently, \(d_k=\exp\!(-(\mathcal C+o(1))k/\log k)\). The constant is universal. The finite-window frequency itself is already recoverable from a published all-value frequency law and is used here as an input; **the new assertion is its explicit sharp growing-window asymptotic**.

For completeness, a finite formula that supplies reproducible exact values is as follows. For each prime \(p\le k\), put \(e_p=\lfloor\log_p k\rfloor\), write the first \(e_p\) base-\(p\) digits of \(m=k+1\) as \(a_{p,0},\ldots,a_{p,e_p-1}\), and let \(t_p\) be the first index with \(a_{p,t_p}\ne0\), or \(e_p\) if there is none. Then
\[
d_k=\prod_{p\le k}\frac{H_p}{p^{e_p}},\qquad
H_p=\begin{cases}
p^{e_p},&t_p=e_p,\\
p^{t_p}a_{p,t_p}\displaystyle\prod_{i=t_p+1}^{e_p-1}(a_{p,i}+1),&t_p<e_p.
\end{cases}
\]
All factors are positive. This formula is a specialization of the finite prime-local value-frequency method, not a separately asserted novelty.

## Assumptions and scope
The variables \(k,n\) are positive integers with \(k\ge2\). The natural density is taken in \(n\) with \(k\) fixed; only after defining each \(d_k\) is \(k\to\infty\) considered. All logarithms are natural. Empty digit products equal one. A prime \(p\le k\) contributes exactly \(e_p\ge1\) digit positions. No assertion of uniform convergence in simultaneously growing \(n\) and \(k\) is made.

## Proof
**1. Maximum and local densities.** Fix \(k\), write \(m=k+1\), and let \(p\le k\) be prime with \(e=e_p\). Let \(N_j(n)\) be the number of the \(m\) integers \(n,\ldots,n+k\) divisible by \(p^j\). The valuation of their product minus that of their lcm gives
\[
\nu_p(g_k(n))=\sum_{j\ge1}(N_j(n)-1)_+
=\sum_{j=1}^e(N_j(n)-1).
\]
For \(j>e\), \(p^j>k\), so at most one of these integers is divisible by \(p^j\); for \(j\le e\), every such interval contains a multiple of \(p^j\). Put \(x=n-1\). The exact count is
\[
N_j(n)=\left\lfloor\frac{m}{p^j}\right\rfloor+c_j(x),\qquad
c_j(x)=\mathbf1_{(x\bmod p^j)+(m\bmod p^j)\ge p^j}.
\]
Thus \(c_j\) is the outgoing base-\(p\) carry at digit position \(j-1\) when adding \(m\) to \(x\). Because \(\lfloor k/p^j\rfloor=\lfloor m/p^j\rfloor-\mathbf1_{p^j\mid m}\), we obtain
\[
\nu_p(k!)-\nu_p(g_k(n))
=\sum_{j=1}^e\bigl(1-\mathbf1_{p^j\mid m}-c_j(x)\bigr)\ge0.
\]
Each summand is nonnegative: if \(p^j\mid m\), then \(c_j=0\); otherwise the term is \(1-c_j\). Consequently \(g_k(n)\le k!\) for all \(n\), and equality holds precisely when every carry at \(j>\min(\nu_p(m),e)\) is one, for every prime \(p\le k\).

If \(t=\min(\nu_p(m),e)=e\), all \(p^e\) residues are admitted. Otherwise the initial \(t\) digits of \(x\) are free, the next digit must lie among \(a_{p,t}\) possibilities forcing the first carry, and each later digit among \(a_{p,i}+1\) possibilities preserving it. Hence exactly \(H_p\) residues modulo \(p^e\) attain the maximal local valuation. Since these conditions involve distinct prime-power moduli, the Chinese remainder theorem proves the displayed finite formula, its positivity and the existence of \(d_k\) (all congruence classes recur periodically). The congruence conditions can be met simultaneously, so \(k!\) is indeed attained.

**2. Remove small primes.** We prove the claimed asymptotic with \(m=k+1\). For large \(m\) set \(J=\lfloor(\log m)^3\rfloor\). Each local factor satisfies \(p^{-e_p}\le H_p/p^{e_p}\le1\), and \(p^{e_p}\le k<m\). Thus, without needing a prime-counting estimate,
\[
\sum_{p\le m/J}\log(H_p/p^{e_p})
=O\!\left(\frac{m\log m}{J}\right)
=o(m/\log m).
\]
Every prime \(p>m/J\) satisfies \(p^2>k\) for large \(m\). Therefore \(e_p=1\), and its factor equals \(1\) when \(p\mid m\), or equals
\(\rho_p=\{m/p\}=(m\bmod p)/p\) when \(p\nmid m\), where braces denote fractional part. Among these primes there is at most one divisor of \(m\), and it contributes zero to \(\log d_k\). Hence, with this convention,
\[
\log d_k=\sum_{m/J<p\le m-1}\log\rho_p+o(m/\log m).
\]

**3. Control the logarithmic singularities.** Put \(\eta=(\log m)^{-2}\). For primes not dividing \(m\), replace \(\log\{m/p\}\) by the bounded \(\log\max\{\{m/p\},\eta\}\), assigning value zero when \(p\mid m\). We show that the total difference is \(o(m/\log m)\). In the interval \(m/(j+1)<p<m/j\), write \(u=m/p-j\), with \(1\le j\le J\). The set \(0<u<\eta\) splits into dyadic shells \(\eta2^{-\ell-1}\le u<\eta2^{-\ell}\). Such a shell is an interval of ordinary integers of length \(O(\eta2^{-\ell}m/j^2)\), and the logarithmic loss on it is \(O(\ell+1)\). For shells of length at least \(m^{2/3}\), the standard Brun–Titchmarsh upper bound for primes in intervals gives \(O(\eta2^{-\ell}m/(j^2\log m))\) primes per shell. Summing the weighted geometric series over \(j,\ell\) costs \(O(\eta m/\log m)\). For the shorter shells, their union for each fixed \(j\) lies in a single interval of length \(O(m^{2/3})\); counting integers instead of primes gives \(O(Jm^{2/3}\log m)=o(m/\log m)\), since each individual nonzero remainder has \(u\ge1/p\ge1/m\). This proves the truncation estimate. The at-most-one prime divisor of \(m\) changes the truncated sum by at most \(O(\log\log m)\).

**4. Prime number theorem and the constant.** Define the bounded, piecewise-smooth function
\[
F_{J,\eta}(t)=\log\max\!\left(\{1/t\},\eta\right),
\qquad 1/J\le t\le1,
\]
with arbitrary values at the finitely many jump points \(t=1/j\). It has supremum norm \(O(\log(1/\eta))\) and total variation \(O(J\log(1/\eta))\). Partial summation and the classical prime number theorem with error \(\pi(y)=\operatorname{Li}(y)+O(ye^{-c\sqrt{\log y}})\) uniformly for \(m/J\le y\le m\) imply
\[
\sum_{m/J<p\le m}F_{J,\eta}(p/m)
=\frac m{\log m}\int_{1/J}^{1}F_{J,\eta}(t)\,dt+o(m/\log m).
\]
Indeed the exponential PNT error absorbs the polylogarithmic variation, while replacing \(1/\log(mt)\) by \(1/\log m\) costs \(o(m/\log m)\). The point \(p=m\), if prime, is immaterial. The integral converges to \(\int_0^1\log\{1/t\}\,dt\): the part \(0<t<1/J\) is bounded absolutely by \(O(1/J)\), and truncation at \(\eta\) incurs \(O(\eta)\) in the integral (sum the same geometric-endpoint estimates). Break the interval at \(t=1/j\) and set \(u=1/t-j\). Then
\[
\int_0^1\log\{1/t\}\,dt
=\sum_{j=1}^{\infty}\int_0^1\frac{\log u}{(j+u)^2}\,du
=-\sum_{j=1}^{\infty}\frac{\log(1+1/j)}{j}
=-\mathcal C.
\]
The last equality follows by integration by parts, with the boundary at zero handled after subtracting the harmless constant \(1/j\) from the antiderivative. The series converges absolutely by comparison with \(\sum j^{-2}\). Together, the four steps prove \(\log d_k=-(\mathcal C+o(1))k/\log k\), and hence the theorem.

## Verification
The accompanying standalone `artifacts/verify.py` uses exact integers to compare the displayed local count with direct prime-power valuation tests for every \(2\le k<300\) and every prime \(p\le k\); it also compares complete-period counts of \(g_k(n)=k!\) for \(2\le k\le12\) with the product formula. Those finite tests verify the normalization, carries, and equality characterization but are not a substitute for the prime-number-theorem argument. A separate deterministic prime sieve evaluates \(-\log(d_k)\log k/k\) for \(k=10^3,10^4,10^5,10^6\), giving respectively approximately \(1.48104,1.41751,1.37196,1.34512\), consistent with the slower convergence to \(\mathcal C\).

## Relationship to prior work
Huang and Yang (arXiv:2611.15379v1, first public 2026-11-11) determine least periods of multiplicative consecutive-LCM quotients and explicitly recover the earlier classical \(g_k\) period. That source motivates the growing-window question but contains no sharp frequency-decay theorem. Hong and Qian (arXiv:0903.0530) provide the crucial finite local valuation framework, and Farhi and Kane (arXiv:0808.1507) resolve the least-period problem. A published exact value-frequency result for arithmetic-progressions contains all finite \(d_k\) values as special cases, so the finite formula above is **covered by prior work**. The present claim is only the analytic \(k\to\infty\) rate with its explicit constant, which does not follow as a stated asymptotic from that fixed-window exact formula. A related published result studies the density of equality in Farhi's different *lcm-binomial triangle*, with a nonsharp upper exponential estimate; it concerns a different observable and does not cover this asymptotic.

## Limitations
No effective error term in \(k\), no local limit theorem for nonmaximal quotient values, and no simultaneous \(n,k\) scaling are proved. The finite count relies on known valuation arithmetic; only the sharp new prime-scale asymptotic is asserted as a contribution. An unindexed analytic treatment of the same extremal density may exist. The demonstration uses classical PNT and short-interval Brun–Titchmarsh estimates without reproving these standard theorems. Independent validation and exhaustive priority verification have not occurred.

## References
- W.-J. Huang and Q.-H. Yang, *On least periods of a class of arithmetic functions*, arXiv:2611.15379v1 (first submitted 2026-11-11), https://arxiv.org/abs/2611.15379.
- S. Hong and G. Qian, *The least common multiple of consecutive arithmetic progression terms*, arXiv:0903.0530 (2009), especially the prime-adic count, https://arxiv.org/abs/0903.0530.
- B. Farhi and D. Kane, *New results on the least common multiple of consecutive integers*, arXiv:0808.1507 (2008), https://arxiv.org/abs/0808.1507.
- *Exact value-frequency law for consecutive arithmetic-progression LCM quotients*, published scientific record, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-value-frequency-law-for-consecutive-arithmetic-progression--8e35eb7b4fbc/RESULT.md.
- *Digitwise classification and least equality period in the lcm-binomial triangle*, published scientific record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-digitwise-classification-and-least-equality-period-in-the-lcm-bi--7061eaf7542e/RESULT.md.
