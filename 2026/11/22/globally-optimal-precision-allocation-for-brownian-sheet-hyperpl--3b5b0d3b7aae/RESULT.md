# Globally optimal precision allocation for Brownian-sheet hyperplane quadrature

## Finding

For each integer \(d\ge 2\) and total Gaussian measurement precision \(P>0\), consider standard \(d\)-parameter Brownian-sheet integration from one complete axis-orthogonal hyperplane integral in every coordinate direction. The independent errors may be allocated arbitrary precisions \(p_j\ge0\) summing to \(P\), while all slice locations \(x_j\in[0,1]\) are free. The unique globally Bayes-risk-minimizing design is

\[
p_1=\cdots=p_d=P/d,\qquad x_1=\cdots=x_d=r_d(P),
\]

where \(r_d(P)\in(2/3,1)\) is the unique solution of

\[
4d3^{d-1}(1-r)=Pr(3r-2).
\]

Writing \(c(r)=r-r^2/2\), the exact optimal conditional mean-square error is

\[
R_d^*(P)=3^{-d}\,\frac{3^{d-1}+(P/d)[r-3c(r)^2]}{3^{d-1}+(P/d)[r+3(d-1)c(r)^2]},\quad r=r_d(P).
\]

There is an exact dimension/precision crossover: \(r_d(P)\) depends on \(d,P\) only through \(\theta=P/(4d3^{d-1})\) and satisfies \(1-r=\theta r(3r-2)\). Consequently, it approaches \(1\) when \(\theta\to0\), approaches \(2/3\) when \(\theta\to\infty\), and converges to the unique interior solution for every positive finite limiting \(\theta\). In the noiseless limit \(P\to\infty\) at fixed dimension,

\[
\lim_{P\to\infty}R_d^*(P)=\frac{3^{-d}}{8d+1}.
\]

## Assumptions and scope

Let \(W_d:[0,1]^d\to\mathbb R\) be a centered, continuous version of the standard Brownian sheet with covariance

\[
\mathbb E[W_d(s)W_d(t)]=\prod_{k=1}^d\min(s_k,t_k).
\]

The scalar target is \(J_d=\int_{[0,1]^d}W_d(t)\,dt\). For each direction \(j=1,\ldots,d\), define the complete hyperplane-integral functional

\[
A_{j,x}=\int_{[0,1]^{d-1}}W_d(t_1,\ldots,t_{j-1},x,t_{j+1},\ldots,t_d)\,dt_{-j}.
\]

Exactly one such reading per direction is available: \(Y_j=A_{j,x_j}+\epsilon_j\). The independent centered Gaussian errors \(\epsilon_j\) are also independent of \(W_d\), with variance \(1/p_j\) when \(p_j>0\). A zero precision means that channel is absent. All locations are deterministic and selected before data collection. The estimator is the joint Gaussian conditional mean \(\mathbb E[J_d\mid Y_1,\ldots,Y_d]\), and risk is its unconditional mean-squared error, equal to posterior variance. The result does not optimize over arbitrary oblique cuts, curved paths, repeated cuts of one orientation, or cost functions other than the prescribed precision sum.

## Proof

**1. Covariance and conditional-independence identity.** Set \(c(x)=\int_0^1\min(x,t)\,dt=x-x^2/2\). Direct integration of the tensor-product covariance gives

\[
\operatorname{Var}(J_d)=3^{-d},\quad
\operatorname{Cov}(J_d,A_{j,x})=3^{-(d-1)}c(x),\quad
\operatorname{Var}(A_{j,x})=3^{-(d-1)}x.
\]

For distinct directions \(j\ne k\),

\[
\operatorname{Cov}(A_{j,x},A_{k,y})=3^{-(d-2)}c(x)c(y).
\]

Hence, after subtracting the conditional projection on \(J_d\),

\[
Z_{j,x}:=A_{j,x}-3c(x)J_d,
\quad
\operatorname{Var}(Z_{j,x})=3^{-(d-1)}[x-3c(x)^2],
\quad
\operatorname{Cov}(Z_{j,x},Z_{k,y})=0\quad(j\ne k).
\]

The \(Z_{j,x_j}\) are jointly Gaussian, mutually independent and independent of \(J_d\). The residual variance is positive at every \(x>0\), since \(3c(x)^2/x=3x(1-x/2)^2\le8/9<1\). Thus the full experiment is equivalent to independent scalar channels \(Y_j=3c(x_j)J_d+Z_{j,x_j}+\epsilon_j\), conditional on the common scalar signal \(J_d\). Its posterior precision is **exactly**

\[
R_d(x,p)^{-1}=3^d+\sum_{j:p_j>0}
\frac{9p_jc(x_j)^2}{1+p_j3^{-(d-1)}[x_j-3c(x_j)^2]}.
\tag{1}
\]

**2. Unique location for each positive channel precision.** Write \(u=p/3^{d-2}\), and set \(b(x)=x/3-c(x)^2\). Maximizing one summand of (1) is equivalent to maximizing

\[
H(u,x)=\frac{9u c(x)^2}{1+ub(x)},\qquad 0\le x\le1.
\]

The derivative has the sign of \(12(1-x)-ux(3x-2)\) for \(x>0\). This is positive through \(2/3\), strictly decreasing on \((2/3,1)\), and negative at \(1\), so there is exactly one global maximizing \(x(u)\in(2/3,1)\) satisfying

\[
12(1-x(u))=u x(u)(3x(u)-2).
\tag{2}
\]

Its inverse \(u(x)=12(1-x)/[x(3x-2)]\) decreases strictly from infinity to zero as \(x\) increases from \(2/3\) to \(1\).

**3. Strict concavity of optimized scalar information.** Let \(G(u)=H(u,x(u))\), extended by \(G(0)=0\). The envelope theorem and (2) give

\[
G'(u)=\frac{9c(x(u))^2}{[1+ub(x(u))]^2}
=\frac{9x^2(3x-2)^2}{4[3x^3-9x^2+6x-1]^2},\qquad x=x(u).
\]

Define \(A(x)=3x^3-9x^2+6x-1\) and \(Q(x)=9x^4-12x^3+6x-2\). On \([2/3,1]\), \(A(2/3)=-1/9\) and \(A'(x)=9(x-1)^2-3<0\), so \(A<0\). Also \(Q(2/3)=2/9\) and \(Q'(x)=6(6x^3-6x^2+1)>0\), because the parenthesized polynomial is increasing there and equals \(1/9\) at \(2/3\). Direct differentiation therefore yields

\[
\frac{d}{dx}\frac{x^2(3x-2)^2}{4A(x)^2}
=-\frac{x(3x-2)Q(x)}{2A(x)^3}>0\quad(2/3<x<1).
\]

But \(u'(x)=12[3x^2-6x+2]/[x^2(3x-2)^2]<0\) on this interval. Therefore \(G'(u)\) is strictly decreasing: \(G\) is strictly concave for \(u>0\), continuously and strictly concave up to \(u=0\).

**4. Global budget allocation and explicit risk.** By step 2, optimizing (1) over all locations for a given allocation gives

\[
R_d^{-1}=3^d+3^{d-2}\sum_{j=1}^d G(p_j/3^{d-2}).
\]

Strict Jensen concavity and \(\sum_jp_j=P\) show that the **unique** maximizing allocation is \(p_j=P/d\) for every \(j\), including exclusion of zero-precision boundary allocations. Equation (2) then forces \(x_j=r_d(P)\) and gives the stated unique root. Substituting into (1) gives the displayed optimal risk formula. All boundary positions and allocations are included in the global comparison.

**5. Dimension scaling and noiseless endpoint.** With \(\theta=P/(4d3^{d-1})\), equation (2) is exactly \(1-r=\theta r(3r-2)\); monotonicity of the two sides proves the three asserted asymptotic regimes. For fixed dimension and \(P\to\infty\), \(r\to2/3\) and \(c(2/3)=4/9\). Taking the limit in the risk formula gives \(3^{-d}/(8d+1)\). In particular, for fixed \(P>0\), \(r_d(P)\to1\) as \(d\to\infty\); the large-dimension and high-precision limits of the optimal location do not commute.

## Verification

`verify.py` (Python standard library only) recomputes the **full** Gaussian conditional covariance risk with rational matrix inversion, independently of the scalar residual formula. It checks exact agreement on 125 rational examples in dimensions 2 through 6, including the conditional residual-covariance cancellation. It also checks the unique-root equation, the risk expression in 99 parameter cases, 4,950 supplemental random competing designs, and noiseless limits. Execute with `python3 verify.py`. The proof above, not finite randomized checks, establishes optimality, uniqueness, and the all-dimensional limits.

## Relationship to prior work

Longi et al. (UAI 2020) study the use and placement of **integral-observation sensors** in spatial Gaussian-process inference, with generic Gaussian covariance formulas, sensor-placement algorithms and applications to tomography and ultrasound. Their full paper does not state the present Brownian-sheet, one-per-axis hyperplane experiment; it neither supplies the conditional-independence decomposition nor the unique precision-allocation law or dimension scaling. Karvonen's 2019 Bayesian-integration thesis and general kernel quadrature research provide the framework for GP integration posterior uncertainty, but do not by themselves optimize this tensor-slice layout. Earlier optimal **point** observation designs are not logically covering because here each datum is a complete \((d-1)\)-dimensional integral with different covariance and signal-to-noise behavior. These comparisons establish the distinction from inspected sources, not a universal publication-priority guarantee.

## Limitations

The classification assumes an exactly specified Brownian-sheet prior, a complete hyperplane integral in every coordinate direction, independent Gaussian instrument errors, a linear precision budget and Bayes mean-square loss for the **single volume integral**. It does not cover non-Gaussian or correlated errors, arbitrary geometries, partial hyperplane paths, repeated orientations, sequential/adaptive designs, other priors, or reconstruction of the whole field. Publication priority beyond the inspected full text and targeted records is not independently certified.

## References

1. J. N. Hendriks, C. Jidling, A. Wills and T. B. Schön, *Evaluating the squared-exponential covariance function in Gaussian processes with integral observations*, first public arXiv version 18 December 2018, https://arxiv.org/abs/1812.07319.
2. K. Longi, C. Rajani, T. Sillanpää, J. Mäkinen, T. Rauhala, A. Salmi, E. Haeggström and A. Klami, *Sensor Placement for Spatial Gaussian Processes with Integral Observations*, Proceedings of UAI 2020, PMLR 124, pp. 1009–1018 (public conference dates 3–6 August 2020). https://proceedings.mlr.press/v124/longi20a.html
3. T. Karvonen, *Kernel-Based and Bayesian Methods for Numerical Integration*, Aalto University doctoral thesis (2019). https://urn.fi/URN:ISBN:978-952-60-8704-7
4. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, Statistics and Computing 29 (2019), pp. 1317–1333. https://doi.org/10.1007/s11222-019-09901-0
