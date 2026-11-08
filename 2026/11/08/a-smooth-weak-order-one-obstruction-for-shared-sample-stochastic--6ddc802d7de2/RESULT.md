# A smooth weak-order-one obstruction for shared-sample stochastic Heun

## Finding
The shared-sample stochastic-Heun scheme (equation (5) in Ayadi--Turinici, arXiv:2002.09304) cannot in general be weakly second-order relative to the authors' stochastic modified equation (6), even for globally smooth, globally Lipschitz sample losses. The following two-sample example has an exact global first-order bias:

\[
\lim_{n\to\infty} n\left(\mathbb E X_n-\mathbb E Z_1\right)=\frac{1}{2e}>0,
\qquad h=1/n.
\]

The observable is \(G(x)=x\); its polynomial growth is admissible for the cited weak-convergence statement.

## Assumptions and scope
Choose an even smooth function \(\chi\in C_c^\infty(\mathbb R)\) with \(0\le\chi\le1\), \(\chi=1\) on \([-2,2]\), and \(\chi=0\) outside \([-3,3]\). For an explicit reproducible choice let

\[
b(s)=\begin{cases}e^{-1/s}&s>0,\\0&s\le0,\end{cases}
\qquad H(s)=\frac{b(s)}{b(s)+b(1-s)},
\qquad \chi(x)=H(3-|x|).
\]

Here \(H(s)=0\) for \(s\le0\) and \(H(s)=1\) for \(s\ge1\). Although \(|x|\) is not differentiable at zero, \(\chi\) is identically one near zero and hence smooth. Set

\[
c(x)=\int_0^x\chi(u)\,du,\quad
 f_0(x)=0,\quad f_1(x)=2\int_0^xc(u)\,du.
\]

Both sample losses belong to \(C^\infty(\mathbb R)\), are globally Lipschitz, and have at most linear growth. Their gradients \(g_0=0\) and \(g_1=2c\) have all derivatives bounded. Their average gradient is \(\bar g=c\), and the sample-gradient variance is \(\mathcal V(x)=c(x)^2\). Crucially, \(c(x)=x\) on \([-2,2]\), \(|c(x)|\le3\), and \(xc(x)\ge0\) for all real \(x\).

Independently at each step select \(\gamma_k\in\{0,1}\) uniformly, and use **the same index in both stages**:

\[
\widetilde X_{k+1}=X_k-hg_{\gamma_k}(X_k),\quad
X_{k+1}=X_k-\frac h2\left[g_{\gamma_k}(X_k)+g_{\gamma_k}(\widetilde X_{k+1})\right].
\]

Initialize \(X_0=1\), take \(h=1/n\), integers \(n\ge2\), and compare at physical time \(t=1\) with the paper's stated noise-only modified equation

\[
dZ_t=-c(Z_t)\,dt+\sqrt h\,|c(Z_t)|\,dW_t,\qquad Z_0=1.
\]

## Proof
**1. Exact discrete mean.** For every \(n\ge2\), all steps and stage predictors lie in \([0,1]\): sample zero leaves the state unchanged, and sample one gives the multiplier \(1-2h+2h^2\in(0,1]\), with predictor multiplier \(1-2h\in[0,1]\). Therefore the cutoff never affects a numerical update and

\[
X_{k+1}=\begin{cases}X_k,&\gamma_k=0,\\ (1-2h+2h^2)X_k,&\gamma_k=1.\end{cases}
\]

Conditional independence across steps yields \(\mathbb E[X_{k+1}\mid X_k]=(1-h+h^2)X_k\), and hence

\[
\mathbb E X_n=(1-h+h^2)^n.
\]

Taking the logarithm gives \(n\log(1-1/n+1/n^2)=-1+1/(2n)+O(n^{-2})\), so

\[
\mathbb E X_n=e^{-1}\left(1+\frac1{2n}+O(n^{-2})\right).
\]

**2. Target diffusion mean.** Let \(G_t=\exp[-(1+h/2)t+\sqrt hW_t]\), the geometric Brownian solution of \(dG_t=-G_tdt+\sqrt hG_tdW_t\), \(G_0=1\). On \(\{\sup_{0\le s\le1}G_s<2}\), pathwise uniqueness for the globally Lipschitz coefficients implies \(Z_s=G_s\) throughout \([0,1]\), because \(c(x)=x\) and \(|c(x)|=x\) for \(0\le x\le2\). The reflection principle gives

\[
\mathbb P\left(\sup_{s\le1}G_s\ge2\right)
\le\mathbb P\left(\sup_{s\le1}W_s\ge\frac{\log2}{\sqrt h}\right)
\le2\exp\left[-\frac{(\log2)^2}{2h}\right].
\]

The product \(xc(x)\ge0\) and bound \(|c|\le3\) give, by Itô's formula,

\[
\mathbb E Z_1^2\le1+9h,\qquad \mathbb E G_1^2=e^{-2+h}.
\]

The two variables agree outside the exponentially rare exit event. Cauchy--Schwarz therefore implies

\[
|\mathbb E Z_1-\mathbb E G_1|\le C\exp\left[-\frac{(\log2)^2}{4h}\right],
\]

with \(C\) uniform for \(0<h\le1/2\). As \(\mathbb E G_1=e^{-1}\), we obtain the stated exponential mean bound for \(Z_1\). Combining with step 1 proves the boxed first-order limit.

**3. General local obstruction.** For any sufficiently smooth sample gradients, writing \(g_\gamma=f'_\gamma\), the same-sample step has first moment

\[
\mathbb E[X_1-x]=-h\bar g(x)+\frac{h^2}{2}\,\mathbb E[g'_\gamma(x)g_\gamma(x)]+O(h^3).
\]

The target SDE with drift \(-\bar g\) has

\[
\mathbb E[Z_h-x]=-h\bar g(x)+\frac{h^2}{2}\bar g'(x)\bar g(x)+O(h^3).
\]

The difference is \(\tfrac{h^2}{2}\operatorname{Cov}(g'_\gamma(x),g_\gamma(x))+O(h^3)\), which is generally nonzero. In the example, at \(x=1\) the covariance equals \(1\). Averaging the two independent stages would cancel this first-moment term but would change the sampling protocol and does not by itself establish full weak order two.

## Verification
A standalone pure-Python script `verify.py` checks the exact two-stage multipliers with rational arithmetic for \(n=2,\ldots,250\), independently computes all four two-stage index pairings, and verifies the scaled first-moment limit at six high-precision mesh sizes. Its recorded output is `verification_output.txt`. These checks are supplementary: exact proofs of the infinite-order and diffusion statements are above.

## Relationship to prior work
Ayadi and Turinici, arXiv:2002.09304, Section 3.1, equation (5), explicitly specify same-sample stages; Theorem 1 asserts weak order two relative to equations (6)--(7), with proof comparing first increment moments in equations (16) and (19). The local covariance contribution present in the scheme is missing from that comparison. The present claim is a direct counterexample to the theorem as stated, not a claim that stochastic Heun has no order-two properties relative to other modified equations.

Li, Tai, and E, arXiv:1811.01558, develop the weak stochastic-modified-equation framework for stochastic gradient algorithms; their different methods do not imply this counterexample or salvage the claimed order. Stillfjord and Williamson, arXiv:2201.12782, study stochastic Runge--Kutta optimization with common-stage sampling and different convergence guarantees, not this fixed-time weak-order-two assertion.

## Limitations
The result applies to the auxiliary fixed-step shared-sample stochastic-Heun integrator and the specific uncorrected diffusion (6). It does not disprove convergence of the separate adaptive SGD-G2 algorithm, rule out an order-two *drift-corrected* stochastic modified equation, or measure the performance of practical learning-rate adaptation. A first-moment correction alone is not a proof of full weak order two. The smooth cutoff provides globally Lipschitz data; the exact recursion takes place inside its linear region.

## References
- I. Ayadi and G. Turinici, *Stochastic Runge-Kutta methods and adaptive SGD-G2 stochastic gradient descent*, arXiv:2002.09304v1 (first publicly submitted 2020-02-20), https://arxiv.org/html/2002.09304v1, Section 3.1, equations (5)--(7), (16), (19)--(21), Theorem 1.
- Q. Li, C. Tai, and W. E, *Stochastic Modified Equations and Dynamics of Stochastic Gradient Algorithms I: Mathematical Foundations*, arXiv:1811.01558v1 (2018), https://arxiv.org/html/1811.01558v1.
- T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge--Kutta method for stochastic optimization*, arXiv:2201.12782v1 (2022), https://arxiv.org/html/2201.12782v1.
