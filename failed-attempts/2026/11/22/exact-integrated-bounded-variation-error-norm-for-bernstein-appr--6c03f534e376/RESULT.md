# Exact integrated bounded-variation error norm for Bernstein approximation and its Gaussian localization

## Finding

For every integer \(n\ge1\), the classical degree-\(n\) Bernstein operator
\[
 (B_nf)(x)=\sum_{j=0}^{n}\binom nj x^j(1-x)^{n-j}f(j/n),\qquad 0\le x\le1,
\]
has the following exact sharp error norm on real pointwise Jordan-bounded-variation data:
\[
 C_n:=\sup_{\operatorname{Var}(f)>0}\frac{\int_0^1|B_nf(x)-f(x)|\,dx}{\operatorname{Var}(f)}
 =\max_{0\le k<n}\mathbb E\left|U_{n,k}-\frac{k}{n}\right|,
 \qquad U_{n,k}\sim\operatorname{Beta}(k+1,n-k).
\]
Every finite-degree maximum is attained by a single unit jump at an original grid point, with an appropriate one-sided value at that point. The formula is exactly evaluable using rational numbers. More explicitly, put
\[
 p_{n,k}=\binom nk\left(\frac{k}{n}\right)^k\left(1-\frac{k}{n}\right)^{n-k},\quad
 T_{n,k}=\sum_{j=k+1}^{n}\binom nj\left(\frac{k}{n}\right)^j\left(1-\frac{k}{n}\right)^{n-j}
\]
(with \(0^0=1\) at \(k=0\)). Then
\[
 C_n=\max_{0\le k<n}\frac{n-k}{n(n+1)}\left(1-2T_{n,k}+2kp_{n,k}\right).
\]
The sharp leading decay and localization are
\[
 \boxed{\lim_{n\to\infty}\sqrt n\,C_n=\frac1{\sqrt{2\pi}}},
 \qquad \frac{k_n}{n}\longrightarrow\frac12
\]
for **every** choice of maximizing index \(k_n\) in the finite formula. In particular, boundary jumps are asymptotically suboptimal, and every asymptotically worst jump location approaches the midpoint.

## Assumptions and scope

A real function \(f:[0,1]\to\mathbb R\) is arbitrary apart from finite pointwise Jordan total variation,
\[
 \operatorname{Var}(f)=\sup_{0=t_0<\cdots<t_m=1}\sum_{i=1}^m|f(t_i)-f(t_{i-1})|.
\]
This allows discontinuities, one-sided jumps and exceptional point values, which matter because \(B_n\) samples the grid. The integrated error uses Lebesgue measure; the norm is taken modulo constants since \(B_n\) reproduces constants. The beta random variable is continuous with parameters \(k+1\) and \(n-k\). No continuity of \(f\) is required.

## Proof

**1. Reduction to one-sided jumps.** Every real function of bounded Jordan variation admits a signed Jordan--Stieltjes representation by the two kinds of half-line indicators \(\mathbf1_{[s,1]}\) and \(\mathbf1_{(s,1]}\), plus a constant, with total coefficient-measure variation no larger than \(\operatorname{Var}(f)\). This follows by splitting its positive and negative variation functions and encoding both one-sided changes at each discontinuity; the two one-sided indicators also encode isolated point values. Both \(B_n-I\) and integration are linear, so Minkowski's inequality gives
\[
 \|B_nf-f\|_{L^1(0,1)}\le \operatorname{Var}(f)
 \sup_{s,\epsilon}\|(B_n-I)\mathbf1_{\text{half-line}(s,\epsilon)}\|_1.
\]
Conversely each such indicator has variation exactly one (when nonconstant), so this reduction is norm-sharp.

**2. A beta order-statistic identity.** Fix \(0\le k<n\). For a unit step whose sampling values vanish at \(j/n\) for \(j\le k\) and equal one for \(j\ge k+1\), the Bernstein output is
\[
 F_{n,k}(x)=\sum_{j=k+1}^{n}\binom nj x^j(1-x)^{n-j}
 =\Pr(U_{n,k}\le x),\quad U_{n,k}\sim\operatorname{Beta}(k+1,n-k).
\]
If the jump lies between \(k/n\) and \((k+1)/n\), at either endpoint with the sampling-compatible one-sided convention, the true step is \(\mathbf1_{[s,1]}\) almost everywhere. Layer-cake integration yields exactly
\[
 \int_0^1|F_{n,k}(x)-\mathbf1_{[s,1]}(x)|\,dx
 =\int_0^sF_{n,k}(x)\,dx+\int_s^1(1-F_{n,k}(x))\,dx
 =\mathbb E|U_{n,k}-s|.
\]
The rightmost expression is convex in \(s\). Its maximum on the closed grid gap is attained at \(k/n\) or \((k+1)/n\). Reflection \(1-U_{n,k}\overset d=U_{n,n-1-k}\) shows that the right-endpoint error equals the left-endpoint error for the reflected index. The asserted maximum over \(k/n\) follows. Each endpoint convention is realized by an actual single-jump Jordan function, so the finite norm is attained.

**3. Exact rational evaluation.** Let \(s=k/n\), \(a=k+1\), \(b=n-k\), \(\mu=a/(n+1)\), and \(F=F_{n,k}(s)=T_{n,k}\). Integration by parts in the incomplete beta integral gives
\[
 \mathbb E|U_{n,k}-s|=(\mu-s)(1-2F)
 +\frac{2s^{a}(1-s)^{b}}{(n+1)\operatorname{B}(a,b)}.
\]
Since \(\mu-s=(n-k)/(n(n+1))\) and \(1/\operatorname{B}(k+1,n-k)=(n-k)\binom nk\), this is exactly the finite rational expression in the finding. These identities include \(k=0\), giving \(1/(n+1)\). No numeric optimization or asymptotic approximation is used for the finite formula.

**4. Sharp Gaussian limit.** For any sequence of maximizing indices \(k_n\), compactness allows a subsequence with \(k_n/n\to p\in[0,1]\). The beta mean and variance satisfy
\[
 \mathbb EU_{n,k}=\frac{k+1}{n+1},\qquad
 \operatorname{Var}(U_{n,k})=\frac{(k+1)(n-k)}{(n+1)^2(n+2)},\qquad
 \left|\mathbb EU_{n,k}-\frac{k}{n}\right|\le\frac1{n+1}.
\]
If \(p\in(0,1)\), the order-statistic central limit theorem, or equivalently the binomial central limit theorem applied to \(\Pr(U_{n,k}\le x)=\Pr(\operatorname{Bin}(n,x)\ge k+1)\), gives
\[
 \sqrt n\left(U_{n,k_n}-\frac{k_n}{n}\right)
 \Longrightarrow N(0,p(1-p)).
\]
The displayed second-moment formula bounds second moments of these rescaled variables uniformly, hence their absolute first moments are uniformly integrable. It follows that
\[
 \sqrt n\,\mathbb E\left|U_{n,k_n}-\frac{k_n}{n}\right|
 \longrightarrow\sqrt{\frac{2p(1-p)}\pi}.
\]
At \(p=0\) or \(p=1\), Cauchy--Schwarz together with the same mean and variance formulas makes this limit zero. Choosing \(k_n=\lfloor n/2\rfloor\) supplies the lower bound \(1/\sqrt{2\pi}\). Along any maximizing subsequence the limit can be no larger than \(\max_{p\in[0,1]}\sqrt{2p(1-p)/\pi}=1/\sqrt{2\pi}\). This proves the sharp limit. Since the function \(p\mapsto p(1-p)\) has its unique maximum at \(1/2\), every maximizing sequence must satisfy \(k_n/n\to1/2\).

## Verification

`checker.py` is a standalone Python 3 checker. It derives Bernstein-tail polynomials independently by exact rational expansion, integrates each one-jump error exactly, verifies the beta/binomial formula and reflection for all degrees \(1\le n\le16\), and checks the exact values \(C_1=1/2\), \(C_2=1/3\), \(C_3=1/4\), \(C_4=1/5\). It also runs 1,200 seeded multijump numerical inequality tests and a numerical asymptotic consistency test. The finite tests are checks, not a substitute for the all-degree proof. Run: `python3 checker.py`.

## Relationship to prior work

Üster and İbikli (2015) establish pointwise convergence-rate bounds for Stancu-type Bernstein operators on bounded-variation data. Cheng (1983) and Bustamante, García-Muñoz and Quesada (2014) investigate Bernstein approximation of discontinuities, and Adell, Garrancho and Martínez-Sánchez (2025, published online; journal issue 2026) develop local pointwise bounds for positive operators. Czudek (2017) proves variation diminution. These frameworks supply context, but the accessible inspected statements do not imply the present **sharp integrated \(BV\to L^1\) error norm**, its finite beta-order-statistic maximization, and localization of every worst-case grid jump. Their pointwise error controls, variation-diminishing assertions, and the integrated operator norm are distinct assertions. A full-text priority comparison with Cheng (1983) and Bustamante et al. (2014) remains incomplete; historical equivalent formulations are a material residual risk.

## Limitations

The finite exact formula is an explicit maximum over \(n\) rational terms; a closed formula for its maximizing integer at every \(n\) is **not** established. The asymptotic location result does not assert a precise finite maximizing index or a higher-order asymptotic expansion. The result is for classical unmodified Bernstein sampling, real pointwise Jordan variation, one-dimensional Lebesgue-integrated error, and unrestricted endpoint values. No claims are made about Kantorovich, generalized Stancu, other norms, or higher dimensions. Independent external validation has not been performed.

## References

1. R. Üster and E. İbikli, *On the Rate of Convergence of the Stancu Type Bernstein Operators for Functions of Bounded Variation*, Mathematical Sciences and Applications E-Notes 3 (2015), 126–136, https://doi.org/10.36753/mathenot.421231; primary full text https://dergipark.org.tr/en/download/article-file/468245.
2. F. Cheng, *On the Rate of Convergence of Bernstein Polynomials of Functions of Bounded Variation*, J. Approx. Theory 39 (1983), 259–274, https://doi.org/10.1016/0021-9045(83)90098-9 (full text not obtained).
3. J. Bustamante, M. A. García-Muñoz and J. M. Quesada, *Bernstein Polynomials and Discontinuous Functions*, J. Math. Anal. Appl. 411 (2014), 829–837, https://doi.org/10.1016/j.jmaa.2013.10.024 (full text not obtained).
4. J. A. Adell, P. Garrancho and F. J. Martínez-Sánchez, *Approximation of Discontinuous Functions by Positive Linear Operators: A Probabilistic Approach*, first published November 25, 2025, https://doi.org/10.1002/mma.70341.
5. K. Czudek, *Bernstein and Kantorovich Polynomials Diminish the \(\Lambda\)-Variation*, J. Math. Anal. Appl. 452 (2017), 912–925, https://doi.org/10.1016/j.jmaa.2017.03.035.
