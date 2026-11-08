# A two-term mean for the divisor ratio on square-completed integers

## Finding

For every real \(X\ge 3\), let \(s(n)\) be the least nonnegative integer such that \(n+s(n)\) is a square, let \(\tau\) count positive divisors, and let \(\omega\) count distinct prime factors, with \(\omega(1)=0\). Define
\[
D(m)=\frac{\tau(m)}{2^{\omega(m)}},\qquad
S(X)=\sum_{1\le n\le X}D(n+s(n)).
\]
The following unconditional two-term asymptotic holds as \(X\to\infty\):
\[
\boxed{S(X)=K_0X\sqrt{\log X}+K_1\frac{X}{\sqrt{\log X}}+O\left(\frac{X}{(\log X)^{3/2}}\right).}
\]
Let \(\gamma\) denote Euler's constant, and, with the square root chosen positive at real \(s>1\), define the absolutely convergent Euler product
\[
H(s)=\prod_{p\ \mathrm{prime}}
\frac{1-\tfrac12p^{-s}+\tfrac12p^{-2s}}{(1-p^{-s})^{1/2}},\qquad \Re s>\tfrac12.
\]
The exact constants are
\[
\boxed{K_0=\sqrt{\frac2\pi}\,H(1)>0,\qquad
K_1=\sqrt{\frac2\pi}\left(H'(1)+\frac{3\gamma-1}{2}H(1)\right).}
\]
In particular, \(S(X)\sim K_0X\sqrt{\log X}\), and the first correction is strictly negative: \(K_1<0\). Truncated Euler products give approximately \(K_0\approx1.1436\) and \(K_1\approx-0.5284\); these decimal figures are illustrative, not certified enclosures.

## Assumptions and scope

All sums are over positive integers and \(X\) is real. No hypothesis such as the Riemann hypothesis is used. The implied constant in the error term is absolute. All logarithms are natural. The analytic input is the classical two-term Selberg--Delange theorem for Dirichlet series \(\zeta(s)^zH(s)\), with the analytic and growth conditions checked below. The result gives two asymptotic terms, not a power-saving remainder after a finite polynomial in \(\log X\).

## Proof

**1. Local factors.** Put \(f(m)=D(m^2)\). Multiplicativity and \(D(p^{2a})=(2a+1)/2\) for each integer \(a\ge1\) give, for \(|u|<1\),
\[
\sum_{a\ge0}f(p^a)u^a
=1+\sum_{a\ge1}\left(a+\tfrac12\right)u^a
=\frac{1-\tfrac12u+\tfrac12u^2}{(1-u)^2}.
\]
Thus, absolutely for \(\Re s>1\),
\[
\mathcal F(s):=\sum_{m\ge1}\frac{f(m)}{m^s}
=\zeta(s)^2\prod_p(1-\tfrac12p^{-s}+\tfrac12p^{-2s})
=\zeta(s)^{3/2}H(s).
\]
The local factor of \(H(s)\) is \(1+\tfrac58p^{-2s}+O(p^{-3\Re s})\), uniformly in vertical strips with \(\Re s\) bounded below by any fixed number strictly greater than \(1/2\). Consequently its product is locally uniformly and absolutely convergent, and holomorphic for \(\Re s>1/2\), with locally absolutely convergent derivatives. At real \(s=1\), every local factor is positive, so \(0<H(1)<\infty\). The holomorphic Euler product is bounded in a fixed half-plane \(\Re s\ge1-\delta>1/2\), providing the regularity needed by Selberg--Delange. Standard zero-free regions for \(\zeta\) handle the \(\zeta(s)^{3/2}\) factor. Also \(0\le f(m)\le\tau(m)\), because each prime-power factor \(a+1/2\) is at most \(a+1\); thus the standard \(\zeta(s)^2\) majorant required by the classical Selberg--Delange hypotheses is available.

**2. Two-term mean on squares.** The classical Selberg--Delange expansion at exponent \(z=3/2\) applies to the nonnegative coefficients \(f\). Indeed the Taylor function determining its coefficients is
\[
\frac{t^{3/2}\mathcal F(1+t)}{1+t}
=H(1)+\big(H'(1)+(\tfrac32\gamma-1)H(1)\big)t+O(t^2),
\]
because \(t\zeta(1+t)=1+\gamma t+O(t^2)\). Therefore, setting
\[
A=\frac{H(1)}{\Gamma(3/2)},\qquad
B=\frac{H'(1)+(\tfrac32\gamma-1)H(1)}{\Gamma(1/2)},
\]
we obtain
\[
F(T):=\sum_{m\le T}f(m)
=T\left(A(\log T)^{1/2}+B(\log T)^{-1/2}\right)
+O\left(T(\log T)^{-3/2}\right)
\]
for real \(T\ge3\). This is precisely the two-coefficient case of Selberg--Delange, with the series coefficient at the first derivative divided by \(\Gamma(1/2)\).

**3. Exact square blocks and partial summation.** The condition \((m-1)^2<n\le m^2\) is equivalent to \(n+s(n)=m^2\). Each full block therefore contributes exactly \((2m-1)f(m)\). For every integer \(T\ge1\),
\[
S(T^2)=\sum_{m=1}^{T}(2m-1)f(m)=2TF(T)-2\int_1^T F(t)\,dt-F(T).
\]
Using, for each fixed real \(\beta\),
\[
\int_2^T t(\log t)^\beta\,dt
=\frac{T^2}{2}\left((\log T)^\beta-\frac{\beta}{2}(\log T)^{\beta-1}
+O((\log T)^{\beta-2})\right),
\]
we deduce
\[
S(T^2)=T^2\left(A(\log T)^{1/2}
+\left(B+\tfrac14A\right)(\log T)^{-1/2}\right)
+O\left(T^2(\log T)^{-3/2}\right).
\]
The omitted \(F(T)\) term is smaller than the displayed error.

**4. Arbitrary cutoffs.** Let \(T=\lfloor\sqrt X\rfloor\). The incomplete next block is
\[
S(X)-S(T^2)=(\lfloor X\rfloor-T^2)f(T+1).
\]
For any fixed \(\varepsilon>0\), the standard divisor bound \(f(m)\le\tau(m^2)\ll_\varepsilon m^\varepsilon\) makes this \(O_\varepsilon(X^{1/2+\varepsilon})\). Replacing \(T^2\) by \(X\) and \(\log T\) by \(\frac12\log X\) similarly adds less than the stated error. Since \(\Gamma(1/2)=\sqrt\pi\) and \(\Gamma(3/2)=\sqrt\pi/2\), elementary simplification yields precisely \(K_0\) and \(K_1\) in the finding.

**5. Strict negativity of the second coefficient.** Writing \(z=1/p\) and \(N(z)=1-z/2+z^2/2\), direct differentiation of the convergent product shows
\[
-\frac{H'(1)}{H(1)}=
\sum_p (\log p)\frac{z^2(5-3z)}{4N(z)(1-z)}
>\frac12\log2+\frac3{16}\log3.
\]
The elementary bounds \(\log2>2/3\) and \(\log3>1\) give a lower bound \(25/48>1/2\). Also \(\gamma<2/3\): indeed \(\gamma<H_6-\log6\), \(H_6=49/20\), and the first five positive terms of
\[
\log6=2\sum_{j\ge0}\frac{(5/7)^{2j+1}}{2j+1}
\]
already exceed \(107/60\). Therefore \((3\gamma-1)/2<1/2<-H'(1)/H(1)\), proving \(K_1<0\). This proves the claim. \(\square\)

## Verification

Run `python verify.py` using Python 3 standard library. It checks the local power series through degree \(40\), independently computes \(D(m^2)\) by ordinary prime-factor exponent products and by divisor counts for \(1\le m\le360\), and verifies exact direct-versus-block sums for every cutoff \(1\le X\le15000\). It also prints finite-prime approximations to \(H(1)\), \(H'(1)/H(1)\), and the two coefficients alongside finite-cutoff diagnostics. Exact arithmetic uses `fractions.Fraction`. No finite check proves the asymptotic expansion; the proof invokes Selberg--Delange with explicitly verified Euler factors.

## Relationship to prior work

Mihoub Bouderbala's February 2026 preprint considers exactly \(S(X)\) and gives a different asserted logarithmic-order expansion in its Theorem 2.1. Its displayed Euler product contains the prime-local linear term \(-1/(2p^s)\), so that product is not absolutely convergent at \(s=1\). Reorganizing the *same exact* Dirichlet series instead as \(\zeta(s)^{3/2}H(s)\) reveals the positive main term and enables the second-order coefficient above. The present claim is not the paper's asserted formula, and it does not assume that the latter is valid.

The Selberg--Delange method itself is classical and is not claimed as new. Related published results on mean values of \(D(n)\) without square completion and on unweighted \(\tau(n^2)\) do not state the two constants for this exact square-completion average. Novelty is a claim about this explicit arithmetic asymptotic and its correction of the order of growth, not about the general analytic technique.

## Limitations

The proof is analytic and relies on the established Selberg--Delange theorem, not a self-contained reproof of that theorem. The remainder is logarithmic rather than a power-saving estimate. A claim that the constant has rigorously certified decimal digits is not made. Search-based originality comparisons cannot exclude an equivalent unindexed older treatment. There has been no independent mathematical audit.

## References

1. M. Bouderbala, *On the Asymptotic Behavior of a Multiplicative Arithmetic Function Related to the Divisor Function Over Perfect Squares Integers Generated by Shifting*, arXiv:2602.20808, initial public version 2026-02-24, Theorem 2.1 and equations (9)--(11). https://arxiv.org/abs/2602.20808
2. R. de la Bretèche and G. Tenenbaum, *Remarks on the Selberg--Delange method*, arXiv:2010.12929, initial public version 2020-10-24. https://arxiv.org/abs/2010.12929
3. M. Bouderbala, *On a sum of a multiplicative function linked to the divisor function over the set of integers B-multiple of 5*, Communications in Mathematics 31 (2023), 369--374; arXiv:2212.05549. https://arxiv.org/abs/2212.05549
4. OEIS A307869, asymptotic mean of the unshifted divisor/unitary-divisor ratio. https://oeis.org/A307869
5. K. Venkatasubbareddy and A. Sankaranarayanan, *On the distribution of the sequence of integers d(n²)*, Czechoslovak Mathematical Journal 76 (2026), 515--524, DOI 10.21136/CMJ.2026.0310-25 (different, unnormalized summatory function).
