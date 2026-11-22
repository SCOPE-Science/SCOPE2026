# Power-saving Möbius GCD-kernel asymptotics for every real exponent above one

## Finding
For a real \(s>1\) and an integer \(N\ge1\), define
\[
T_s(N)=\sum_{1\le m,n\le N}\frac{\mu(m)\mu(n)\gcd(m,n)^s}{mn},\qquad \beta=s-1.
\]
Here \(\mu\) is the classical Möbius function. Set
\[
C_s=\prod_p(1-p^{-1})(1+p^{-1}-p^{-s-1}),\quad
R_s(r)=\prod_{p\mid r}(1+p^{-1}-p^{-s-1})^{-1},
\]
\[
A_{q,s}=\sum_{1\le k,l\le q}\frac{\mu(k)\mu(l)R_s(kl)}{kl},\qquad
c_s=\frac{C_s}{\beta}\sum_{q\ge1}A_{q,s}\big(q^{-\beta}-(q+1)^{-\beta}\big).
\]
The products converge, \(C_s>0\), \(A_{q,s}\ge0\), and \(c_s>0\); the last series converges absolutely. For each \(\varepsilon>0\),
\[
\boxed{T_s(N)=c_sN^\beta+O_{s,\varepsilon}(N^{\theta_s+\varepsilon}),}\qquad
\theta_s=\begin{cases}
\beta/(\beta+1),&0<\beta\le1/2,\\
2\beta/3,&1/2\le\beta\le3/2,\\
\beta-1/2,&\beta\ge3/2.
\end{cases}
\]
In all three ranges \(\theta_s<\beta\). There is also an absolutely convergent double-series representation
\[
c_s=\frac{C_s}{\beta}\sum_{k,l\ge1}
\frac{\mu(k)\mu(l)R_s(kl)}{kl\max(k,l)^\beta},
\]
and the large-kernel-exponent limit is
\[
\boxed{c_s=\frac{1}{\zeta(2)(s-1)}\left(1+O(2^{-(s-1)})\right)}\qquad(s\to+\infty).
\]

## Assumptions and scope
All asymptotics in \(N\) fix the real parameter \(s>1\). The implied constants in the power-saving bound may depend on \(s\) and \(\varepsilon\), and no uniformity as \(s\downarrow1\) is asserted. The large-\(s\) expansion concerns the leading constant, not a joint \(N,s\) limit. The real Jordan convolution is \(J_s(d)=\sum_{e\mid d}\mu(e)(d/e)^s=d^s\prod_{p\mid d}(1-p^{-s})>0\).

## Proof
**1. Positive square decomposition.** The convolution identity \(\sum_{d\mid n}J_s(d)=n^s\) yields, for every integer \(N\ge1\),
\[
T_s(N)=\sum_{d\le N}\frac{J_s(d)}{d^2}
\left(\sum_{k\le N/d}\frac{\mu(dk)}k\right)^2.
\tag{1}
\]
Only squarefree \(d\) contribute. For an integer \(r\ge1\), introduce the nonnegative multiplicative function
\[
f_{r,s}(d)=\mu(d)^2\prod_{p\mid d}(1-p^{-s})\,\mathbf1_{\gcd(d,r)=1}.
\]
Then \(\mu(dk)\mu(dl)=\mu(d)^2\mu(k)\mu(l)\mathbf1_{\gcd(d,kl)=1}\).

**2. Uniform local mean.** If \(g_{r,s}=f_{r,s}*\mu\), the nonzero local values of \(g\) are, for \(p\nmid r\), \(g(p)=-p^{-s}\), \(g(p^2)=-(1-p^{-s})\), and, for \(p\mid r\), \(g(p)=-1\), \(g(p^2)=0\). Higher prime powers vanish. Fix \(1/2<\sigma<1\). Since \(s>1\),
\[
\sum_{e\ge1}\frac{|g_{r,s}(e)|}{e^\sigma}
\le K_{s,\sigma}\prod_{p\mid r}(1+p^{-\sigma})
\le K_{s,\sigma}\tau(r),
\]
where convergence of the unrestricted Euler product follows from \(2\sigma>1\) and \(s+\sigma>1\). Thus \(f_{r,s}=\mathbf1*g_{r,s}\) and the floor-sum decomposition give, uniformly in positive integers \(r\) and real \(X\ge1\),
\[
\sum_{d\le X}f_{r,s}(d)=C_sR_s(r)X
+O_{s,\sigma}(\tau(r)X^\sigma).
\tag{2}
\]
Indeed the constant is the absolutely convergent Euler product \(\prod_p(1-p^{-1})(1+f_{r,s}(p)/p)\). Partial summation of (2) gives
\[
\sum_{d\le X}d^{\beta-1}f_{r,s}(d)
=\frac{C_sR_s(r)}\beta X^\beta
+O_{s,\sigma}\left(\tau(r)[1+X^{(\beta-1+\sigma)_+}\log(2X)]\right).
\tag{3}
\]
When \(\beta-1+\sigma<0\), the error is \(O_{s,\sigma}(\tau(r))\), with no logarithm required. These bounds follow by integrating the error term \(O(\tau(r)t^\sigma)\) against \((\beta-1)t^{\beta-2}\), including the logarithmic boundary case.

**3. Positivity of the coefficient series.** For a fixed positive integer \(q\), apply (2) to the expansion of
\[
\sum_{d\le X}\mu(d)^2\prod_{p\mid d}(1-p^{-s})
\left(\sum_{k\le q}\frac{\mu(k)\mathbf1_{\gcd(k,d)=1}}k\right)^2.
\]
It equals \(C_sA_{q,s}X+O_{s,q,\sigma}(X^\sigma)\). The summand is nonnegative, so \(A_{q,s}\ge0\). Since \(0<R_s(r)\le1\), the triangle bound is \(A_{q,s}\le H_q^2\), where \(H_q=\sum_{k\le q}1/k\). Also \(A_{1,s}=1\). The identity
\[
\sum_{q\ge j}(q^{-\beta}-(q+1)^{-\beta})=j^{-\beta}
\]
and the bound \(\sum_{k,l\ge1}(kl\max(k,l)^\beta)^{-1}\le2\sum_{j\ge1}H_jj^{-1-\beta}<\infty\) prove absolute convergence of both formulas and \(c_s\ge(C_s/\beta)(1-2^{-\beta})>0\).

**4. Quotient blocks and uniform error.** In (1), group divisors with \(\lfloor N/d\rfloor=q\). For each \(q\le Q<N\), expand the square, apply (3) at \(N/q\) and \(N/(q+1)\), and sum over \(1\le k,l\le q\). Since \(\tau(kl)\le\tau(k)\tau(l)\) and \(\sum_{k\le q}\tau(k)/k\le H_q^2\), these blocks contribute
\[
\frac{C_sN^\beta}{\beta}\sum_{q\le Q}A_{q,s}(q^{-\beta}-(q+1)^{-\beta})
+O_{s,\sigma}\left(\sum_{q\le Q}H_q^4\left[1+(N/q)^{(\beta-1+\sigma)_+}\log(2N)\right]\right).
\tag{4}
\]
For the omitted blocks, \(d\le N/(Q+1)\). The bounds \(0<J_s(d)/d^2\le d^{\beta-1}\) and \(\left|\sum_{k\le N/d}\mu(dk)/k\right|\le1+\log(N/d)\) imply, by dyadic summation (or integral comparison with an endpoint correction),
\[
0\le T_{s,>Q}(N)\ll_s N^\beta Q^{-\beta}(1+\log Q)^2+(1+\log N)^2.
\tag{5}
\]
The omitted tail of the main coefficient has the same first bound, by \(A_{q,s}\le H_q^2\) and summation by parts. If \(0<\beta<1/2\), choose \(\sigma\) with \(1/2<\sigma<1-\beta\); (4) is \(O_s(Q(1+\log Q)^4)\), and \(Q=\lfloor N^{\beta/(\beta+1)}\rfloor\) yields \(N^{\beta/(\beta+1)+\varepsilon}\). If \(1/2\le\beta\le3/2\), set \(\sigma=1/2+\delta\) with small positive \(\delta\); taking \(Q=\lfloor N^{1/3}\rfloor\) gives error \(O_{s,\varepsilon}(N^{2\beta/3+\varepsilon})\). For \(\beta>3/2\), the \(q\)-sum of \(q^{-(\beta-1/2+\delta)}\) converges and the same \(Q\) gives \(O_{s,\varepsilon}(N^{\beta-1/2+\varepsilon})\). At the boundary values, any logarithm is absorbed by \(N^\varepsilon\). This establishes the theorem, including the ranges and quantifiers.

**5. Large exponent.** Factor the Euler product as
\[
C_s=\zeta(2)^{-1}\prod_p\left(1-\frac{p^{-s}}{p+1}\right)
=\zeta(2)^{-1}(1+O(2^{-s})).
\]
For \(\beta=s-1\ge2\), the \(q=1\) summand of \(\beta c_s/C_s\) is \(1-2^{-\beta}\), while the nonnegative tail is at most \(\sum_{q\ge2}H_q^2q^{-\beta}=O(2^{-\beta})\). Hence the displayed large-\(s\) expansion follows.

## Verification
The accompanying `verify.py` checks the defining double sum against the exact Jordan-square decomposition using rational arithmetic for integer exponents \(s=2,3,4\), at every cutoff \(1\le N\le35\). It also computes the local products, finite coefficient series and independent normalized finite sums for real exponents \(s=1.25,1.5,2,2.5,3,4\), with two cutoff values in each case. The resulting output ends in `MOBIUS_GCD_POWER_DIAGNOSTICS_OK 105 12`. These calculations are finite diagnostics; equations (2)--(5) are the infinite proof.

## Relationship to prior work
Azimifard, arXiv:2611.00525v1 (31 October 2026), proves exactly the \(s=2\) case, with \(N\)-error \(O_\varepsilon(N^{2/3+\varepsilon})\), using the Jordan-square identity and uniform coprimality mean. The present theorem extends the fixed denominator \(mn\) to every real GCD exponent \(s>1\), establishes its changed normalization \(N^{s-1}\), supplies a parameter-dependent error exponent, and determines the large-exponent constant. The general GCD-matrix literature of Aistleitner--Berkes--Seip--Weber (arXiv:1407.5403v2) addresses spectral bounds for \(\gcd(m,n)^{2\alpha}/(mn)^\alpha\) and unspecified coefficient vectors, not this fixed Möbius vector with denominator \(mn\). Ehm (arXiv:2405.06349v2) studies Nyman--Beurling Gram kernels; the kernels and main asymptotic are different. The general Jordan identities and convolution methods are standard and are credited rather than asserted to be new.

## Limitations
No endpoint theorem for \(s\le1\), no uniform error estimate as \(s\downarrow1\), and no claim that \(\theta_s\) is the optimal error exponent. Although relevant indexed sources and the motivating full text were compared, an unindexed general GCD-kernel result could cover the parameter theorem. The numerical checker cannot establish asymptotics or historical uniqueness.

## References
1. A. Azimifard, *A power-saving asymptotic for a Möbius-weighted GCD quadratic form*, arXiv:2611.00525v1, submitted 31 October 2026, https://arxiv.org/html/2611.00525v1.
2. C. Aistleitner, I. Berkes, K. Seip, M. Weber, *Convergence of series of dilated functions and spectral norms of GCD matrices*, arXiv:1407.5403v2, https://arxiv.org/html/1407.5403v2.
3. W. Ehm, *On certain Gram matrices and their associated series*, arXiv:2405.06349v2, https://arxiv.org/html/2405.06349v2.
