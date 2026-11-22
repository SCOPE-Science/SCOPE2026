# Exact Fourier calibration and null variance of the circularized Anderson–Darling score

## Finding

Let \(n\geq1\), set \(m=n+1\), and let \(U_{(1)}<\cdots<U_{(n)}\) be the order statistics of \(n\) independent observations from \(\mathrm{Uniform}(0,1)\). With \(U_{(0)}=0\) and \(U_{(m)}=1\), form the \(m\) spacings \(D_j=U_{(j)}-U_{(j-1)}\), extended periodically in the index. For \(c\in\{0,\ldots,m-1\}\) and \(i\in\{1,\ldots,m-1\}\), put
\[
P_{c,i}=\sum_{j=1}^{i}D_{c+j},\quad p_i=i/m,
\quad h(p,u)=-2\left[p\log\frac{u}{p}+(1-p)\log\frac{1-u}{1-p}\right].
\]
The *actual, nonlinear* average-circularized modified Anderson–Darling score of Liu [1, Eq. (4.8)] is
\[
T_n=\frac1m\sum_{c=0}^{m-1}\sum_{i=1}^{m-1}h(p_i,P_{c,i}).
\]
As \(n\to\infty\), without further scaling,
\[
\boxed{T_n\ \Longrightarrow\ T_\infty=\sum_{k=1}^{\infty}a_k(Z_{k,1}^2+Z_{k,2}^2),}
\]
where the \(Z_{k,j}\) are independent standard real normals and
\[
\boxed{a_k=\frac{\gamma+\log(2\pi k)-\operatorname{Ci}(2\pi k)}{\pi^2k^2}
=\frac1{\pi^2k^2}\int_0^{2\pi k}\frac{1-\cos t}{t}\,dt,\qquad k\geq1.}
\]
Here \(\gamma\) denotes Euler's constant and \(\operatorname{Ci}(x)=-\int_x^\infty\cos(t)/t\,dt\) for \(x>0\). The coefficients are strictly positive and strictly decreasing. The law is non-Gaussian, has mean \(1\), and has **exact variance**
\[
\boxed{\operatorname{Var}(T_\infty)=\frac{42-4\pi^2}{9}=0.280175821738062836\ldots.}
\]
Thus circular pooling yields an explicit limiting calibration whose variance is \((42-4\pi^2)/(6\pi^2-54)=0.483281515227\ldots\) times the classical unpooled Anderson–Darling limiting variance \(2\pi^2/3-6\), using the classical eigenvalues \(1/[k(k+1)]\). The statement concerns the specified modified logarithmic score and a fully specified continuous null; it does not assert a finite-sample pivotal law under fitted parameters.

There is a quantitative spectral cutoff. Write \(T_{\infty,K}=\sum_{k=1}^{K}a_k(Z_{k,1}^2+Z_{k,2}^2)\) and \(R_K=T_\infty-T_{\infty,K}\geq0\). Then
\[
\begin{aligned}
\mathbb E R_K&=\frac{2}{\pi^2K}\bigl(\log(2\pi K)+\gamma+1\bigr)
+O\!\left(\frac{\log K}{K^2}\right),\\
\operatorname{Var}(R_K)&=\frac{4}{3\pi^4}\frac{\log^2 K}{K^3}\,(1+o(1)),
\end{aligned}
\]
so \(\mathbb P(R_K>\varepsilon)\leq\mathbb ER_K/\varepsilon\) for every \(\varepsilon>0\). These statements quantify the truncation error when computing upper-tail null probabilities from finitely many independent chi-squares.

## Assumptions and scope

The sample observations are independent and identically distributed from a *fully specified, continuous* distribution \(F_0\). Applying \(F_0\) yields independent uniforms and the above statistic. There is no estimation of \(F_0\) or nuisance parameters. The circularization uses exactly the \(n+1\) spacings, including the two boundary spacings, and averages all \(n+1\) starts. The score uses \(p_i=i/(n+1)\), not the alternate \((i-1/2)/n\) convention. All limits take \(n\to\infty\) through integers. Normal variables in the limit are mutually independent.

## Proof

**1. Brownian bridge from normalized exponential spacings.** The exact null spacings have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Represent them as \(D_j=E_j/S_m\), where \(E_j\) are independent \(\operatorname{Exp}(1)\) variables and \(S_m=\sum_j E_j\). Let \(B_m\) be the polygonal interpolation of
\[
B_m(r/m)=\sqrt m\left(\sum_{j=1}^{r}D_j-r/m\right),\qquad 0\leq r\leq m.
\]
The functional central limit theorem and \(S_m/m\to1\) give \(B_m\Rightarrow B\) in \(C[0,1]\), where \(B(t)=W(t)-tW(1)\) is a standard Brownian bridge. Both the polygonal functions and their limit agree at the two endpoints; extend them periodically. At the grid locations \(s=c/m,t=i/m\), the *exact identity*
\[
\sqrt m(P_{c,i}-p_i)=B_m((s+t)\bmod1)-B_m(s)
\]
holds, including wrapped indices.

**2. Interior Taylor expansion and boundary removal.** For any fixed \(\delta\in(0,1/2)\) restrict to \(\delta\leq i/m\leq1-\delta\). Uniformly on this interior region, \(\sup_{c,i}|P_{c,i}-p_i|=O_{\mathbb P}(m^{-1/2})\), and a uniform third-order Taylor bound gives
\[
h(p_i,P_{c,i})=
\frac{(P_{c,i}-p_i)^2}{p_i(1-p_i)}+O_{\mathbb P}(m^{-3/2}).
\]
The average of the \(O(m^2)\) errors, divided by \(m\), is \(O_{\mathbb P}(m^{-1/2})\). The continuous mapping theorem and two-dimensional Riemann sums therefore give the truncated weak limit
\[
T_{n,\delta}\Rightarrow\int_0^1\int_{\delta}^{1-\delta}
\frac{[B((s+t)\bmod1)-B(s)]^2}{t(1-t)}\,dt\,ds.
\]
To remove the endpoints **without assuming unproved uniform relative errors**, use the exact beta marginals \(P_{c,i}\sim\operatorname{Beta}(i,m-i)\). Writing \(d(j)=\log j-\psi(j)\), where \(\psi\) is the digamma function, beta log expectations give
\[
\mathbb Eh(p_i,P_{c,i})=
2\left[\frac{i}{m}d(i)+\frac{m-i}{m}d(m-i)-d(m)\right].
\]
The elementary harmonic-number inequalities \(0<d(j)\leq1/j\) yield \(0\leq\mathbb Eh(p_i,P_{c,i})\leq4/m\), uniformly in all \(m,i,c\). Since the omitted end ranks number at most \(2\delta m+2\), their nonnegative contribution to \(\mathbb ET_n\) is at most \(8\delta+8/m\). For the Gaussian limiting integral, the bridge increment variance is \(t(1-t)\), so the corresponding endpoint expectation is exactly \(2\delta\). Markov's inequality and the converging-together theorem thus prove
\[
T_n\Rightarrow T_\infty=\int_0^1\int_0^1
\frac{[B((s+t)\bmod1)-B(s)]^2}{t(1-t)}\,dt\,ds.
\]
This argument supplies the endpoint justification needed to pass from the exact log score to its quadratic Brownian functional.

**3. Complete independent Fourier decomposition.** For each nonzero integer \(k\), let \(\widehat B_k=\int_0^1B(s)e^{-2\pi i k s}\,ds\). For the distributional derivative of the bridge, all nonconstant Fourier coefficients are orthogonal white-noise coefficients. Thus for positive \(k\), \(\widehat B_k=\xi_k/(2\pi i k)\), where \(\xi_k=(Z_{k,1}+iZ_{k,2})/\sqrt2\), with all displayed real Gaussian coordinates independent. Parseval gives
\[
\int_0^1[B(s+t)-B(s)]^2\,ds
=\sum_{k\ne0}|\widehat B_k|^2\,2(1-\cos(2\pi kt)).
\]
The integrands are nonnegative, so Tonelli permits exchanging the sum and the \(t\) integral. By symmetry,
\[
\int_0^1\frac{1-\cos(2\pi kt)}{t(1-t)}\,dt
=2\int_0^{2\pi k}\frac{1-\cos x}{x}\,dx.
\]
Combining the positive and negative frequencies yields the stated independent \(\chi_2^2\) mixture with
\(a_k=4\int_0^{2\pi k}(1-\cos x)/x\,dx/(2\pi k)^2\). The standard definition of \(\operatorname{Ci}\) yields the explicit special-function formula.

**4. Strict positivity, mode ordering, exact moments.** Put \(G(x)=\int_0^x(1-\cos u)/u\,du\). Then \(G(x)>0\), is nondecreasing and satisfies \(G(2\pi)>1\) because
\(G(2\pi)>\pi^{-1}\int_0^\pi(1-\cos u)\,du=1\).
For all \(x\geq2\pi\),
\[
\frac{d}{dx}\frac{G(x)}{x^2}
=\frac{1-\cos x-2G(x)}{x^3}<0.
\]
Consequently \(a_k> a_{k+1}>0\). Define the even periodic function
\[
K(t)=1+2[t\log t+(1-t)\log(1-t)],\quad0<t<1,
\]
with \(K(0)=K(1)=1\). Direct integration by parts shows its nonzero complex Fourier coefficient is exactly \(a_k\), while \(\int_0^1K(t)dt=0\). Because \(a_k=O((\log k)/k^2)\) and \(K\) is continuous, the Fourier series converges absolutely and uniformly, so evaluating at zero gives \(2\sum_{k\ge1}a_k=1\). The squared coefficients obey Parseval:
\(\int_0^1K(t)^2dt=2\sum_{k\ge1}a_k^2\).
Now
\[
\int_0^1K(t)^2dt
=\frac73-\frac{2\pi^2}{9},
\]
as follows by expanding the square and applying
\(\int_0^1 t^2\log^2t\,dt=2/27\) and
\(\int_0^1t(1-t)\log t\log(1-t)dt=37/108-\pi^2/36\), the latter obtained by differentiating the beta integral at \((2,2)\). Hence
\[
\mathbb E T_\infty=2\sum a_k=1,\qquad
\operatorname{Var}(T_\infty)=4\sum a_k^2
=2\int_0^1K^2=\frac{42-4\pi^2}{9}.
\]
The third cumulant is \(16\sum_{k\ge1}a_k^3>0\), proving the limit is non-Gaussian.

**5. Sharp truncation scale.** Integration by parts in \(\operatorname{Ci}\) at integer-period endpoints gives \(\operatorname{Ci}(2\pi k)=O(k^{-2})\). Thus
\[
a_k=\frac{\log(2\pi k)+\gamma}{\pi^2k^2}+O(k^{-4}).
\]
Integral comparison or Euler summation yields the displayed expectation expansion for \(R_K\). Likewise, since independent \(\chi_2^2\) terms have variance \(4\),
\(\operatorname{Var}(R_K)=4\sum_{k>K}a_k^2\sim4\log^2K/(3\pi^4K^3)\). Nonnegativity yields the stated rigorous probability cutoff. All assertions are infinite-sequence statements proved by analytic integration and standard limit theorems, not inferred from finite numerical experiments.

## Verification

Run `python verify.py` from this directory after installing the freely available `mpmath` package. It checks the closed variance by an independent numerical integral, the Fourier coefficients against direct quadrature, positivity and initial mode ordering, convergence of 250 spectral variance terms, exact finite-\(m\) beta/digamma mean identities, and an exponential-spacings Monte Carlo sanity check. In the recorded execution all **39 assertions passed**. The exact mean of the finite statistic is not claimed as new: its formula is used only to cross-check the endpoint bound, and it is separately present in the existing literature/record of this statistic. The full proof above, not numerical assertions, supports the continuum weak limit and variance formula.

## Relationship to prior work

Liu [1, §§4 and 6, especially Eqs. (4.8) and (6.11), Theorems 6–7] introduces the exact circularly pooled statistic and the *continuum Gaussian kernel* and its circulant-matrix approximations. The author explicitly states in §6.1 that weak convergence of the circularized versions requires further rigorous study, and the subsequent kernel analysis is presented as a Gaussian approximation. The theorem here proves the weak convergence for the **nonlinear finite-sample score itself**, controls the endpoint ranks, and identifies each spectral weight analytically, together with the closed null variance and sharp truncation decay. Neither the Fourier coefficients nor the closed variance formula nor the endpoint-converging argument appears in the inspected main text and appendix of [1].

The parallel 2022 preprint [2] announces a weighted-chi-square asymptotic distribution and a circulant kernel; its accessible abstract does not provide enough detail to rule out stronger coverage in its unavailable body. The journal version [3] was dated May 2023, after the first September 2022 preprint, and the accessible abstract does not disclose this explicit coefficient/variance theorem. The distributional representation, not the generic use of Fourier analysis or the existence of a Gaussian quadratic approximation, is the claim of interest. Classical beta-spacing, functional CLT, Fourier and Parseval tools are used without any claim to their invention.

## Limitations

The weak convergence is under a specified continuous null and for the average-pooled *modified* logarithmic Anderson–Darling score, not the maximum-pooled score, fitted-parameter test, general weights, or the classical unmodified Anderson–Darling statistic. The coefficients are special-function values; no finite elementary expression for every null quantile is claimed. The variance comparison to the unpooled classical AD law concerns asymptotic null variance, not comparative statistical power. An inaccessible parallel preprint body and the journal full text leave a residual historical-priority risk; no independently performed mathematical audit is claimed.

## References

1. Chuanhai Liu, *Reweighted and Circularized Anderson-Darling Tests of Goodness-of-Fit*, arXiv:2209.08050, earliest public version 16 September 2022, https://arxiv.org/abs/2209.08050. The available HTML provides full mathematical main text and appendix.
2. Chuanhai Liu, *Circularly Symmetric Tests of Goodness-of-Fit*, arXiv:2209.08150, earliest public version 16 September 2022, https://arxiv.org/abs/2209.08150. Only the abstract could be read in this comparison.
3. Chuanhai Liu, *Reweighted and circularised Anderson-Darling tests of goodness-of-fit*, *Journal of Nonparametric Statistics* **35** (2023), 869–904, https://doi.org/10.1080/10485252.2023.2213782. Public abstract and bibliographic data examined.
4. M. Csörgő and L. Horváth, *On the distributions of \(L_p\)-norms of weighted uniform empirical and quantile processes*, *Annals of Probability* **16** (1988), 142–161. General weighted-process context, cited and discussed in [1].
