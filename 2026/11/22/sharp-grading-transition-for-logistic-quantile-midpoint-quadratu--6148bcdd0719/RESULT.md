# Sharp grading transition for logistic-quantile midpoint quadrature in the homogeneous weighted Sobolev norm

## Finding

Let \(\rho(x)=e^{-x}/(1+e^{-x})^2\) be the logistic probability density and \(F(x)=(1+e^{-x})^{-1}\) its distribution function. For real \(p>0\) put
\[
\psi_p(t)=\frac{t^p}{t^p+(1-t)^p},\quad 0\le t\le1.
\]
For integer \(n\ge1\), set
\[
 a_j=\psi_p((j-1)/n),\qquad c_j=\psi_p((j-1/2)/n),\qquad b_j=\psi_p(j/n),
\]
\[
 x_j=F^{-1}(c_j)=p\log\frac{j-1/2}{n-j+1/2},\quad w_j=b_j-a_j,
 \qquad Q_{n,p}(f)=\sum_{j=1}^{n}w_j f(x_j).
\]
Every weight is positive, the weights total one, and \(p=1\) is the equal-probability midpoint rule. For the homogeneous weighted Sobolev error \(E_{n,p}\) defined below, the **exact finite-sample identity** is
\[
 E_{n,p}^{2}=\sum_{j=1}^{n}\left[\int_{a_j}^{c_j}\frac{(u-a_j)^2}{u^2(1-u)^2}\,du+\int_{c_j}^{b_j}\frac{(u-b_j)^2}{u^2(1-u)^2}\,du\right].\tag{1}
\]
For fixed \(p>0\) let
\[
 J_{j,p}=\int_{(j-1)^p}^{(j-1/2)^p}\frac{(v-(j-1)^p)^2}{v^2}\,dv
 +\int_{(j-1/2)^p}^{j^p}\frac{(v-j^p)^2}{v^2}\,dv,\quad C_p=\sum_{j=1}^{\infty}J_{j,p}.
\]
The series is positive and converges for \(0<p<2\). The complete trichotomy is
\[
 \lim_{n\to\infty}n^pE_{n,p}^2=2C_p \quad(0<p<2),\qquad
 \lim_{n\to\infty}\frac{n^2E_{n,2}^2}{\log n}=\frac43,
\]
\[
\lim_{n\to\infty}n^2E_{n,p}^2=
 \frac{p^2}{2}+\frac{2\pi p}{3\sin(\pi/p)}+\frac{\pi p}{3\sin(2\pi/p)}\quad(p>2).\tag{2}
\]
In particular \(C_1=\log2\), and \(\lim n^2E_{n,3}^2=9/2+2\sqrt3\pi\). The error rate is \(n^{-p/2}\) below the threshold, \(n^{-1}\sqrt{\log n}\) at the threshold, and \(n^{-1}\) above it. The latter is optimal in order among constant-exact quadratures using \(n\) point evaluations, for the stated seminorm.

## Assumptions and scope

The test space consists of real, locally absolutely continuous functions \(f\) on \(\mathbb R\) with finite derivative energy
\[\|f\|_{\dot H^1(\rho)}^2:=\int_{\mathbb R}|f'(x)|^2\rho(x)\,dx<\infty.\]
We quotient by additive constants. Because \(\rho\) has exponential tails, the Cauchy–Schwarz inequality on \([0,x]\) gives at most \(O(e^{|x|/2})\) growth for a representative of bounded derivative energy; this is integrable against \(\rho\). Each point evaluation and the integral therefore exist. Since \(Q_{n,p}(1)=1\), the integration error is well-defined on the quotient. Define its worst-case norm by
\[
 E_{n,p}=\sup_{\|f\|_{\dot H^1(\rho)}\le1}\left|\int_{\mathbb R}f(x)\rho(x)\,dx-Q_{n,p}(f)\right|.
\]
This is **not** the inhomogeneous \(W^{1,2}_\rho\)-norm \(\int(|f|^2+|f'|^2)\rho\), used in the motivating literature, and constants in this theorem should not be transferred without proof. The parameter \(p\) is fixed as \(n\to\infty\); uniform estimates for varying \(p\) are not asserted.

## Proof

**1. Exact Riesz error formula.** Let \(G\) be the cumulative distribution function of the discrete measure \(\sum_jw_j\delta_{x_j}\). Both probability measures have total mass one. Integration by parts gives for every \(f\) in the test class
\[
 \int f\rho-Q_{n,p}f=\int_{\mathbb R}(G(x)-F(x))f'(x)\,dx.\tag{3}
\]
There are no boundary terms: the cumulative difference is bounded by the logistic tail at either end, while the weighted Cauchy–Schwarz estimate bounds \(|f(x)-f(0)|\) by a multiple of \(e^{|x|/2}\). Cauchy–Schwarz in \(L^2(\rho)\) and the extremizing derivative \(f'=(G-F)/\rho\) show that
\[
 E_{n,p}^2=\int_{\mathbb R}\frac{(G-F)^2}{\rho}\,dx.
\]
Indeed this extremizing derivative has finite energy by the displayed integral, and the resulting primitive is admissible. Under \(u=F(x)\), \(du=\rho(x)\,dx\), \(\rho(F^{-1}(u))=u(1-u)\), so \(dx/\rho(x)=du/[u^2(1-u)^2]\). On \([a_j,c_j)\) the discrete cumulative distribution equals \(a_j\); on \([c_j,b_j)\) it equals \(b_j\). This proves (1), including the two endpoint cells.

**2. Uniform cell estimate and the endpoint model.** Write \(t_j=(j-1/2)/n\), \(d_j=b_j-a_j\). For an interior cell with \(t_j\to t\in(0,1)\), Taylor expansion of the smooth map \(\psi_p\) gives
\[
 n^3 e_{j,n}\to H_p(t):=\frac{\psi_p'(t)^3}{12\psi_p(t)^2[1-\psi_p(t)]^2}
 =\frac{p^3}{12}\frac{t^{p-3}(1-t)^{p-3}}{[t^p+(1-t)^p]^2},\tag{4}
\]
where \(e_{j,n}\) denotes the \(j\)-th summand of (1). To check the coefficient \(1/12\), the two half-cell integrals have local numerator equal to squared distance from the relevant endpoint; each contributes \((d_j/2)^3/3\), giving \(d_j^3/12\).

For \(1\le j\le n/2\), the estimates \(\psi_p(t)\asymp_p t^p\), \(\psi_p'(t)\asymp_p t^{p-1}\), and \(\psi_p(t)\le1/2\) give the **uniform bound**
\[
 0<e_{j,n}\le K_p n^{-p}j^{p-3}\quad(j\ge2),\qquad e_{1,n}\le K_pn^{-p}.\tag{5}
\]
For completeness, on \([a_j,b_j]\) with \(j\ge2\) the denominator \(u^2(1-u)^2\) is bounded above by a constant times \((j/n)^{-2p}\); the two numerator integrals sum to at most \((b_j-a_j)^3/3\), while \(b_j-a_j\le K_pj^{p-1}n^{-p}\). The first cell is controlled by substituting \(u=n^{-p}v\), since its endpoint is zero and the integrand remains bounded. The right-half estimates follow by symmetry.

Fix \(j\) and let \(n\to\infty\). Since \(n^p\psi_p(s/n)\to s^p\), substitution \(v=n^pu\) in (1) yields
\[
 n^pe_{j,n}\to J_{j,p}.\tag{6}
\]
When \(0<p<2\), the majorant \(j^{p-3}\) in (5) is summable. Symmetry, dominated convergence for the first finitely many cells, and a uniform tail bound for the remaining ones yield \(n^pE_{n,p}^2\to2\sum_{j\ge1}J_{j,p}\). Equation (5) also proves absolute convergence of the positive series.

**3. The logarithmic threshold.** At \(p=2\), (4) has \(H_2(t)\sim(2/3)t^{-1}\) as \(t\downarrow0\), and the same asymptotic at one. More directly, for \(1\ll j\ll n\), the cell expansion obtained from (1) gives \(n^2e_{j,n}=(2/3)j^{-1}(1+o(1))\), uniformly when \(j\to\infty\) and \(j/n\to0\). One verifies this uniformly by expanding \(\psi_2(t)=t^2(1+O(t))\) and its first three derivatives on an entire cell. Sum over \(J\le j\le\varepsilon n\); the first \(J\) cells contribute \(O_J(n^{-2})\), the middle compact range contributes \(O_\varepsilon(n^{-2})\), and (5) bounds the omitted endpoint segments by \(O(n^{-2}\log J)\). First send \(n\to\infty\), then \(J\to\infty\) and \(\varepsilon\to0\). Each endpoint contributes \((2/3)n^{-2}\log n\); hence the total coefficient is \(4/3\).

**4. Integrable bulk and closed form for \(p>2\).** For \(p>2\), the endpoint bound (5) shows that, after multiplication by \(n^2\), the total contribution of cells with \(j\le\varepsilon n\) is \(O_p(\varepsilon^{p-2})+o(1)\), and likewise at the right end. Therefore the interior Riemann sum (4) converges to
\[
 \lim_{n\to\infty}n^2E_{n,p}^2=\frac{p^3}{12}\int_0^1\frac{t^{p-3}(1-t)^{p-3}}{[t^p+(1-t)^p]^2}\,dt.\tag{7}
\]
With \(r=t/(1-t)\), this becomes
\[
 \frac{p^3}{12}\int_0^\infty\frac{r^{p-3}(1+r)^4}{(1+r^p)^2}\,dr
 =\frac{p^2}{12}\sum_{k=0}^4 {4\choose k}
 \Gamma\!\left(1+\frac{k-2}{p}\right)\Gamma\!\left(1-\frac{k-2}{p}\right).
\]
All beta integrals are convergent exactly in this regime. The gamma reflection identity \(\Gamma(1+z)\Gamma(1-z)=\pi z/\sin(\pi z)\), with the continuous value one at \(z=0\), evaluates the sum to the third formula in (2). Substituting \(p=3\) gives \(9/2+2\sqrt3\pi\).

**5. The equal-quantile constant.** For \(p=1\), adjoining the two half-cells around each positive integer gives the one-sided limit as \(1/2\) plus all integrals \(\int_{j-1/2}^{j+1/2}(v-j)^2/v^2\,dv\), \(j\ge1\). Its partial sum through \(j=N\) is exactly
\[
 S_N=2N+1-\frac1{4(N+1/2)}-2N\log(N+1/2)
 +2\log\Gamma(N+1/2)-2\log\Gamma(1/2).
\]
Stirling's formula gives \(S_N\to\log2\). This proves \(C_1=\log2\), and by symmetry the full coefficient is \(2\log2\).

**6. No \(n\)-point method can beat the power \(n^{-1}\).** For any constant-exact linear quadrature using at most \(n\) real nodes, let \(G\) be its discrete cumulative weight function. The error representation (3) remains valid, including possibly signed weights. On \(u\in[1/4,3/4]\), the weight \(1/[u^2(1-u)^2]\) is at least 16. The step function \(G\) is constant on at most \(n+1\) intervals of lengths \(\ell_i\) totaling \(1/2\). For each interval, minimizing \(\int(u-c)^2du\) over constants \(c\) gives \(\ell_i^3/12\). Convexity of the cube gives \(\sum\ell_i^3\ge (1/2)^3/(n+1)^2\). Therefore
\[
 E_n^2\ge16\frac{(1/2)^3}{12(n+1)^2}=\frac1{6(n+1)^2}.
\]
Non-constant-exact quadratures have infinite operator norm on the quotient. Thus the rate \(n^{-1}\) for \(p>2\) is sharp in order; this argument makes no claim about minimization of the leading constant.

## Verification

The accompanying standalone `verify_logistic.py` evaluates formula (1) at 75-digit working precision using an explicit antiderivative, checks positivity and consistency across multiple integers \(n\) and exponents \(p\), and compares scaled values to the proven constants. It prints `VERIFY_OK 35`. This finite checker is supplementary to, not a replacement for, Steps 1–6. The exact endpoint and beta-integral derivations above establish the infinite assertions.

## Relationship to prior work

Suzuki (2026), arXiv:2611.11545, studies the suboptimality of **Gaussian nodes** for logistic-weight integration in the full weighted Sobolev norm, and describes the previously known Möbius-transformed trapezoidal rule with optimal \(n^{-1}\) order at smoothness one. Suzuki, Hyvönen and Karvonen (2024), arXiv:2407.13650 (subsequently published), prove optimal-order bounds for a **different transformed trapezoidal rule**. These results already establish that optimal order is possible: the new claim is not that observation. The present finding instead determines the exact worst-case error and the full \(p\)-dependent endpoint-grading phase transition for the explicit **mass-exact power-logit quantile-midpoint family**, in the homogeneous derivative-energy norm, including the \(2\log2\) ungraded constant and the exact \(p>2\) leading constants. In the inspected articles' algorithm descriptions, statements, and logistic examples, this parameterized family and these constants do not appear. Related graded randomized quadrature investigations concern independent stratum samples of algebraically singular functions rather than this deterministic logistic Sobolev operator norm. A literature search is not a proof of historical uniqueness.

## Limitations

The norm is homogeneous and quotiented by constants, not the full \(W^{1,2}_\rho\) norm from the parent paper. Fixed \(p\) is essential to the asymptotic proof. The formula handles logistic density in one dimension, not arbitrary exponential-tailed measures, finite-precision effects, higher smoothness, optimal leading constants across all quadratures, or randomized sampling. Exact mathematical validity and historical priority should be independently checked before treating it as a published theorem.

## References

- Yuya Suzuki, *Suboptimality of Gaussian quadrature for Freud and logistic weights in weighted Sobolev spaces*, arXiv:2611.11545v1, first publicly posted 2026-11-08, https://arxiv.org/abs/2611.11545 .
- Yuya Suzuki, Nuutti Hyvönen and Toni Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650, first posted 2024-07-18, https://arxiv.org/abs/2407.13650 .
