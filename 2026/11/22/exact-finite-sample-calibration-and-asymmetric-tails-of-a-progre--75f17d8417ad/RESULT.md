# Exact finite-sample calibration and asymmetric tails of a progressively censored exponentiality statistic

## Finding
Let \(0\le r<m\le n\), with \(d=m-r\ge2\), and observe the last \(d\) failures from a general progressively Type-II censored sample of \(n\) independent exponential lifetimes. The first \(r\) failures are unobserved, and, after failure \(i\in\{r+1,\ldots,m\}\), exactly \(R_i\ge0\) surviving units are withdrawn uniformly at random, with \(\sum_{i=r+1}^{m}R_i=n-m\). Consider the scale-free Qin–Yu–Gui spacing test statistic

\[
T=\frac{\sum_{i=r+1}^{m-1}(m-i)S_i}{(d-1)\sum_{i=r+1}^{m}S_i}.
\]

Define \(w_j=1-j/(d-1)\) for \(j=0,\ldots,d-1\) and \(c_\ell=(n-r)/(n-\ell)\) for \(\ell=0,\ldots,r\). For \(0<t<1\) away from the finite set \(\{w_1,\ldots,w_{d-1}\}\), put

\[
N_t=\{j\in\{1,\ldots,d-1\}:w_j<t\},\quad
P_t=\{j\in\{1,\ldots,d-1\}:w_j>t\},\quad
b_j=\frac1{t-w_j}\quad(j\in N_t).
\]

Then the **exact finite-sample null CDF** is the finite rational sum

\[
\boxed{\displaystyle
F_T(t)=\sum_{j\in N_t}
\left(\prod_{h\in N_t\setminus\{j\}}\frac{t-w_j}{w_h-w_j}\right)
\left(\prod_{\ell=0}^{r}\frac1{1+b_j(1-t)c_\ell}\right)
\left(\prod_{h\in P_t}\frac1{1+b_j(w_h-t)}\right).}
\]

An empty product equals one. At the finitely many knots, omit the zero-coefficient term and use continuity; \(F_T(t)=0\) for \(t\le0\) and \(F_T(t)=1\) for \(t\ge1\). The law depends only on \((n,m,r)\), not on the removal allocation \((R_i)\) or exponential scale.

The opposite extreme tails have **different exact powers**. Define the complete homogeneous symmetric polynomial \(h_j(c_0,\ldots,c_r)\) by \(\prod_{\ell=0}^r(1-c_\ell z)^{-1}=\sum_{j\ge0}h_jz^j\). Then

\[
\begin{aligned}
\Pr(T\le t)&\sim C_Lt^{m-1},&
C_L&=\frac{n!}{(n-r-1)!(n-r)^{r+1}}\frac{(d-1)^{d-2}}{(d-2)!},\\
\Pr(T>1-t)&\sim C_Rt^{d-1},&
C_R&=\frac{(d-1)^{d-1}}{(d-1)!}h_{d-1}(c_0,\ldots,c_r),
\end{aligned}\qquad t\downarrow0.
\]

For \(r\ge1\), the first missing failures force the left exponent \(m-1\) to exceed the right exponent \(m-r-1\). Moreover, the law strictly stochastically dominates the \(r=0\) benchmark with the same number \(d\) of observed failure spacings, whose statistic is the average of \(d-1\) independent \(\operatorname{Unif}(0,1)\) variables. Thus its null law is not symmetric about \(1/2\) when \(r>0\).

A minimal exact example is \((n,m,r)=(5,3,1)\), for which \(F_T(t)=5t^2/(4+t)\) throughout \(0<t<1\). For \((10,6,2)\), \(C_L=6.328125\) and \(C_R=32.60449382716049\ldots\).

## Assumptions and scope
The lifetimes are independent and identically distributed with exponential scale \(\sigma>0\). The first \(r\) failures have no observed times, and there is no removal before failure \(r+1\). At subsequent failures the removal counts are deterministic and the removed survivors are selected independently of their remaining lifetimes, uniformly at random. The observable ordered failure times are \(X_{r+1}<\cdots<X_m\), and the normalized spacings are

\[
S_{r+1}=(n-r)X_{r+1},\qquad
S_i=\left(n-i+1-\sum_{\ell=r+1}^{i-1}R_\ell\right)(X_i-X_{i-1}),\quad i=r+2,\ldots,m.
\]

All statements are exact for fixed integer \(n,m,r\) in the indicated range; the limits \(t\downarrow0\) are endpoint limits at fixed sample sizes, not asymptotics in \(n\).

## Proof
**1. Independent spacing representation.** By exponential order-statistic spacings before the first observed failure and the lack-of-memory property at subsequent uniformly randomized removals, there exist independent rate-one exponentials \(E_0,\ldots,E_r,G_1,\ldots,G_{d-1}\) such that jointly

\[
(S_{r+1},S_{r+2},\ldots,S_m)/\sigma
\stackrel{\mathrm d}=\left(\sum_{\ell=0}^{r}c_\ell E_\ell,G_1,\ldots,G_{d-1}\right).
\]

Indeed the \((\ell+1)\)-st ordinary exponential order-statistic increment has rate \((n-\ell)/\sigma\), and multiplication by \((n-r)\) produces the coefficient \(c_\ell\). Subsequent risk-set-weighted increments have independent \(\operatorname{Exp}(1)\) laws, independently of the first observed event. This also proves removal-allocation and scale invariance.

**2. CDF decomposition.** Since \(T=(\sum_{j=0}^{d-1}w_jS_{r+1+j})/(\sum S_{r+1+j})\), the event \(T\le t\), apart from probability-zero ties, is \(A_t\le B_t\), where

\[
A_t=(1-t)\sum_{\ell=0}^rc_\ell E_\ell+\sum_{h\in P_t}(w_h-t)G_h,
\qquad B_t=\sum_{j\in N_t}(t-w_j)G_j.
\]

The two sums are independent; every term in \(B_t\) is exponential of distinct rate \(b_j=1/(t-w_j)\). Its survival function is

\[
\Pr(B_t>x)=\sum_{j\in N_t}
\left(\prod_{h\in N_t\setminus\{j\}}\frac{b_h}{b_h-b_j}\right)e^{-b_jx},\quad x\ge0.
\]

This follows by factoring the Laplace transform \(\prod_{j\in N_t}b_j/(b_j+s)\) into simple fractions. Conditioning on \(A_t\), evaluating \(\mathbb E e^{-b_jA_t}\), and using \(b_h/(b_h-b_j)=(t-w_j)/(w_h-w_j)\) gives the displayed CDF. Strict positivity and continuity of the original density handle all knots.

**3. Left tail.** When \(0<t<1/(d-1)\), \(N_t=\{d-1\}\), \(b_{d-1}=1/t\). The CDF therefore simplifies exactly to

\[
F_T(t)=\prod_{\ell=0}^{r}
\frac{(n-\ell)t}{(n-\ell)t+(n-r)(1-t)}
\prod_{j=1}^{d-2}\frac{t}{w_j}.
\]

Taking \(t\downarrow0\) produces \(r+1+d-2=m-1\) powers of \(t\) and the explicit \(C_L\).

**4. Right tail.** Write \(\varepsilon=1-t\). For \(0<\varepsilon<1/(d-1)\), the event \(T>1-\varepsilon\) equals

\[
\sum_{j=1}^{d-1}\left(\frac{j}{d-1}-\varepsilon\right)G_j
<\varepsilon\sum_{\ell=0}^{r}c_\ell E_\ell.
\]

Conditional on the finite value \(s=\sum c_\ell E_\ell\), the left side has small-ball probability asymptotic to \((\varepsilon s)^{d-1}(d-1)^{d-1}/((d-1)!)^2\): integrate the product exponential density, tending to one at zero, over the corresponding simplex. For \(\varepsilon<1/[2(d-1)]\), the same density bounded by one supplies a uniform upper bound proportional to \(\varepsilon^{d-1}s^{d-1}\). The conditioning variable has every finite moment, so dominated convergence applies. Finally \(\mathbb E(\sum c_\ell E_\ell)^{d-1}=(d-1)!h_{d-1}(c_0,\ldots,c_r)\). This proves \(C_R\).

**5. Strict stochastic shift.** For \(r>0\), couple the first spacing to \(E_r\) as \(\sum_{\ell=0}^{r}c_\ell E_\ell>E_r\) almost surely. Holding the remaining spacings fixed, the function of the first spacing in \(T\) is strictly increasing because all other weights are below one. Replacing that spacing by \(E_r\) yields the \(r=0\) statistic with \(d\) spacings. Its Dirichlet-normalized exponential gaps give the average of \(d-1\) independent uniforms. Both distributions have positive density on \((0,1)\); the coupling yields strict CDF inequality at every interior threshold. For \(r>0\), the different endpoint powers also preclude symmetry about the only possible center, \(1/2\).

## Verification
The standalone Python 3 standard-library program `check_exact.py` evaluates the rational CDF exactly, verifies the uncensored Irwin–Hall specialization, the one-knot left-tail formula, the exact rational \((5,3,1)\) example and both sharp tail coefficients. It also directly simulates individual exponential lifetimes with randomized survivor removals under two different schemes for \((n,m,r)=(10,6,2)\). The actual replay passed 413 assertions/comparisons. Finite checks support but do not replace the proof. The rational partial-fraction sum can suffer cancellation under ordinary floating-point evaluation at extreme tail levels; rational or high-precision arithmetic is preferable.

## Relationship to prior work
Qin, Yu and Gui (2020) introduce this statistic, prove its independent-spacing representation and approximate its null law by normal methods; their Section 4 explicitly describes exact null calibration as difficult under initial missing failures. Huffer and Lin (2001) already give a **general exact algorithm** for probabilities of rational linear combinations of independent exponential variables. This work does **not** claim to invent exact computability or that general algorithm: the contribution is the direct finite rational CDF formula for this specific statistic, the complete asymmetric endpoint constants/exponents and the strict stochastic shift. The later exact-inference work of Balakrishnan, Lin and collaborators treats scale/location inference and prediction pivots, not these fixed-statistic tail powers. The `Gofpt2` documentation available in 2026 lists normal and simulation calibration methods, not this rational form.

## Limitations
Only a fully exponential null, independent lifetimes, noninformative randomized removals and the specified initial-missing-failure scheme are covered. No finite-sample power under nonexponential alternatives, no general right-censoring mechanism, no high-dimensional or growing-sample asymptotic and no numerical stability guarantee for naive floating-point partial fractions are claimed. The general Huffer–Lin machinery is strong prior coverage for computability, and priority of the particular explicit formula and tail asymmetry still merits independent literature review.

## References
1. Qin, X., Yu, J., and Gui, W. (2020, first online publication September 18). *Goodness-of-fit test for exponentiality based on spacings for general progressive Type-II censored data*. Journal of Applied Statistics 49 (2022), 599–620. https://doi.org/10.1080/02664763.2020.1821613 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9041613/ .
2. Huffer, F. W., and Lin, C.-T. (2001). *Computing the joint distribution of general linear combinations of spacings or exponential variates*. Statistica Sinica 11, 1141–1157. https://www3.stat.sinica.edu.tw/statistica/oldpdf/A11n411.pdf .
3. *Exact Inference and Prediction for Exponential Models Under General Progressive Censoring with Application to Tire Wear Data* (2025). Mathematics 13, 3627. https://doi.org/10.3390/math13223627 .
4. `Gofpt2` documentation, *Generalized Goodness-of-Fit Test for Progressive Type-II Censored Data*, 2026: https://rdrr.io/cran/Gofpt2/man/gof_test_censored.html .
