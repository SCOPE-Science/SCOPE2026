# Unique antithetic stage pairing and a Hessian-only Gaussian error law for randomized Runge–Kutta integration

## Finding

Let \(d\ge1\), \(T>0\), and \(f:\mathbb R^d\to\mathbb R^d\) be a globally Lipschitz, four-times continuously differentiable autonomous vector field with bounded derivatives of orders one through four. Write \(y'(t)=f(y(t))\), \(y(0)=y_0\). The one-step randomized explicit two-stage Runge–Kutta map is

\[
R_{h,u}(x)=x+h f(x+hu f(x)),\qquad u\in[0,1].
\]

Use \(2n\) steps of length \(h=T/(2n)\), grouped into independent pairs. In pair \(k\), use \(U_k\) for the first stage and \(1-U_k\) for the second, where the \(U_k\) are independent uniform random variables on \([0,1]\). Thus

\[
X_0=y_0,\qquad X_{k+1}=R_{h,1-U_k}(R_{h,U_k}(X_k)),\qquad 0\le k<n.
\]

For the fundamental matrix \(\Phi(t,s)\) solving \(\partial_t\Phi(t,s)=Df(y(t))\Phi(t,s)\), \(\Phi(s,s)=I_d\), define the vector fields

\[
A(x)=Df(x)^2 f(x),\qquad H(x)=D^2f(x)[f(x),f(x)],
\]

and the bias vector and covariance matrix

\[
B_T=-\frac16\int_0^T\Phi(T,s)A(y(s))\,ds,
\quad
\Sigma_T=\frac{2}{45}\int_0^T g(s)g(s)^\mathsf T\,ds,
\quad g(s)=\Phi(T,s)H(y(s)).
\]

Then \(\max_{0\le k\le n}\|X_k-y(2kh)\|=O(h^2)\) deterministically, uniformly in all stage realizations, and

\[
\boxed{h^{-5/2}\bigl(X_n-y(T)-h^2B_T\bigr)\ \Longrightarrow\ \mathcal N_d(0,\Sigma_T).}
\]

Here the Gaussian law is allowed to be degenerate if \(g(s)\) vanishes. For \(f(x)=\sin x\), \(d=1\), \(y_0=1\), \(T=1/2\), it is nondegenerate and its asymptotic variance is approximately \(0.016876976071422\).

There is a sharp uniqueness statement. Keep each stage uniform on \([0,1]\), and allow any fixed joint law \((U,V)\) for a pair, independently repeated across pairs. If \(U+V\ne1\) with positive probability, then on the admissible linear equation \(y'=y\) with \(y_0\ne0\),

\[
\boxed{h^{-3/2}(X_n-e^T y_0)\ \Longrightarrow\ \mathcal N\!\left(0,\frac T2 e^{2T}y_0^2\operatorname{Var}(U+V)\right).}
\]

Thus **complementary antithetic stages are the only uniform-marginal pair coupling** eliminating the generic \(h^{3/2}\)-scale trajectory error and achieving deterministic-order \(O(h^2)\) accuracy across every smooth autonomous vector field in this class. The pairing does not increase the number of evaluations of \(f\).

## Assumptions and scope

All limits are along integers \(n\to\infty\) with exactly \(2n\) randomized RK2 steps and \(h=T/(2n)\). Within-pair dependence is permitted but different pairs are independent and identically distributed. All stage values have uniform marginals, and the vector field is autonomous, exact and noiseless. The strong \(O(h^2)\) bound is at *pair endpoints* \(2kh\), not necessarily at each odd half-pair iterate. The limit theorem is a fixed-final-time asymptotic, not a large-time stability claim. The comparison law for noncomplementary couplings is established using the nonzero initial value scalar linear test \(f(x)=x\), which satisfies all derivative assumptions although the field itself is unbounded.

## Proof

**1. Pair expansion.** Fix \(x\) in a bounded set and denote \(F=f(x)\), \(J=Df(x)\), \(K=D^2f(x)\). Taylor expansion with a remainder uniform for \(u,v\in[0,1]\) gives

\[
R_{h,u}(x)=x+hF+h^2uJF+\frac{h^3u^2}{2}K[F,F]+O(h^4)
\]

and, composing without exchanging the stages,

\[
\begin{aligned}
R_{h,v}(R_{h,u}(x))={}&x+2hF+h^2(1+u+v)JF\\
&+h^3\left[(u+v)J^2F+
\left(\frac12+v+\frac{u^2+v^2}{2}\right)K[F,F]\right]+O(h^4).
\end{aligned}
\]

For \(v=1-u\), the second-order coefficient is the exact value \(2JF\). The exact flow of duration \(2h\) has third-order coefficient \(\tfrac43(J^2F+K[F,F])\). Consequently, with \(\xi(u)=(1-u)^2-1/3\),

\[
\boxed{R_{h,1-u}(R_{h,u}(x))-\operatorname{Flow}_{2h}(x)
=h^3\left[-\frac13 A(x)+\xi(u)H(x)\right]+O(h^4).}
\]

The constants in the remainder are uniform on the compact trajectory neighborhood because derivatives through order four are continuous and bounded there. The stage law has

\[
\mathbb E\xi(U)=0,\qquad
\mathbb E\xi(U)^2=\frac15-\frac19=\frac4{45}.
\]

**2. Global strong error.** Global Lipschitz continuity makes the two-step numerical map locally Lipschitz in \(x\) with factor at most \(1+Ch\) for small \(h\), uniformly in the stage values. The local defect from step 1 is at most \(Ch^3\). Starting from the exact initial condition, discrete Gronwall proves \(\max_{k\le n}\|X_k-y(2kh)\|\le C_T h^2\), pathwise. This also keeps all numerical states in one fixed compact region for small \(h\).

**3. Propagating the local defects.** Set \(t_k=2kh\), \(e_k=X_k-y(t_k)\). Linearize the exact flow and the pair defect around \(y(t_k)\); the pathwise strong bound gives

\[
e_{k+1}=(I_d+2hDf(y(t_k)))e_k
+h^3\left[-\frac13 A(y(t_k))+\xi(U_k)H(y(t_k))\right]+r_k,
\]

where the total propagated effect of all remainders satisfies \(\left\|\sum_{k<n}\text{propagated }r_k\right\|\le C_T h^3\). Indeed the local Taylor error is \(O(h^4)\), the defect's dependence on \(e_k\) contributes \(O(h^3\|e_k\|)\), and the nonlinear flow linearization contributes \(O(h\|e_k\|^2)\). The discrete fundamental matrices differ by \(O(h)\) from the continuous \(\Phi\) on fixed horizons. Variation of constants and a first-order Riemann-sum estimate therefore give

\[
e_n=h^2 B_T+h^3\sum_{k=0}^{n-1}\Phi(T,t_k)H(y(t_k))\xi(U_k)+O(h^3),
\]

with the final remainder uniform in all stage realizations. The deterministic bias follows because each term in the sum represents a \(2h\)-wide time interval, so \(-h^3\sum A/3=-h^2\int A/6+O(h^3)\) after propagation.

**4. Multivariate Gaussian limit.** The variables \(\xi(U_k)\) are bounded, independent, identically distributed, centered, and have variance \(4/45\). For each fixed direction \(q\in\mathbb R^d\), the Cramér–Wold projection of the scaled random sum is

\[
q^\mathsf T h^{1/2}\sum_{k<n}g(t_k)\xi(U_k),
\qquad g(s)=\Phi(T,s)H(y(s)).
\]

Its Lindeberg condition holds automatically because the summands are uniformly \(O(\sqrt h)\). Its variance converges to

\[
\frac4{45}\lim_{h\to0} h\sum_{k<n}(q^\mathsf Tg(t_k))^2
=\frac2{45}\int_0^T(q^\mathsf Tg(s))^2\,ds.
\]

The scalar triangular-array central limit theorem in each direction and Cramér–Wold give \(\mathcal N_d(0,\Sigma_T)\). The propagated remainder is \(O(h^3)=o(h^{5/2})\), completing the first limit.

**5. Necessity and uniqueness.** For the scalar linear test \(f(x)=x\), a generic paired step has exact multiplier

\[
Q_h(U,V)=(1+h+h^2U)(1+h+h^2V)
=1+2h+h^2(1+U+V)+h^3(U+V)+h^4UV.
\]

Since each stage is uniform, \(\mathbb E(U+V)=1\). Taylor expansion uniformly in \((U,V)\) gives \(\log Q_h(U,V)=2h+h^2(U+V-1)+O(h^3)\). Summing \(n=T/(2h)\) independent pair logarithms, the remainder is \(O(h^2)=o(h^{3/2})\), while the centered leading sum obeys a scalar central limit theorem with variance \(T\operatorname{Var}(U+V)/2\) after normalization by \(h^{3/2}\). Exponentiation and the delta method supply the stated limit, including the factor \(e^{2T}y_0^2\). If \(\operatorname{Var}(U+V)=0\), uniform marginals force \(U+V=1\) almost surely; conversely this antithetic law has the global \(O(h^2)\) bound of step 2. Thus it is the unique uniform-marginal coupling with universal second-order strong accuracy.

## Verification

Run `python3 verify.py` using Python's standard library. The checker verifies exact rational coefficients for the two-stage composition on quadratic and linear scalar vector fields, moments of the uniform stage law, and a high-accuracy quadrature of the sine benchmark. Its reproducible Monte Carlo experiment is only an illustration; the infinite-dimensional quantifiers over all admissible vector fields, the asymptotic Gaussian law, and the uniqueness conclusion follow from the analytical proof above rather than finitely many tests.

The sine benchmark uses \(f(x)=\sin x\), \(y_0=1\), \(T=1/2\). Its exact trajectory is \(y(t)=2\arctan(e^t\tan(1/2))\), and its scalar fundamental matrix is \(\Phi(T,s)=\sin(y(T))/\sin(y(s))\). Direct substitution gives \(B_T\approx-0.010592106848791\) and \(\Sigma_T\approx0.016876976071422\).

## Relationship to prior work

The explicit uniform-stage RK2 algorithm is given by Bochacik, Goćwin, Morkisz and Przybyłowicz [1]. Their analysis studies inexact information, approximation rates and fixed-step stability for independent stages, not complementary dependence between adjacent stages or a bias-corrected Gaussian fluctuation coefficient. Kruse and Wu [2] investigate randomized explicit RK schemes for time-irregular coefficient functions, emphasizing moment and almost-sure error rates rather than the antithetic pairing limit. Bochacik and Przybyłowicz [3] study *implicit* randomized RK2 variants, whose stage equations and stability questions differ. The earlier quasi-randomized RK method of Coulibaly and Lécot [4] uses low-discrepancy-type randomization and needs separate scrutiny for any possible equivalent coupling statement. Classical antithetic variance reduction and deterministic modified-equation analysis explain the underlying mechanisms, but neither by its name alone establishes the stated combined uniqueness and propagated-Hessian covariance law.

## Limitations

The theorem is for autonomous, smooth, globally Lipschitz ODEs with exact function evaluations, independent pairs and uniform stage marginals. It does not extend automatically to nonautonomous or rough coefficients, noisy data, correlated different pairs, odd half-pair endpoints, long-time invariant measures, or stochastic differential equations. The Gaussian limit can be degenerate for a linear vector field because its Hessian vanishes, and the non-antithetic necessity statement means **failure of universal** \(O(h^2)\) accuracy, not a failure on every individual ODE. The theorem is not a claim of independent peer review or exhaustive historical precedence.

## References

1. T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge-Kutta method—stability and convergence under inexact information*, first public 2020-06-22, https://arxiv.org/abs/2006.12131.
2. R. Kruse and Y. Wu, *Error analysis of randomized Runge-Kutta methods for differential equations with time-irregular coefficients*, first public 2017-01-12, https://arxiv.org/abs/1701.03444.
3. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge-Kutta schemes*, first public 2024-04-29, https://arxiv.org/abs/2404.19059.
4. I. Coulibaly and C. Lécot, *A quasi-randomized Runge-Kutta method*, *Mathematics of Computation* (1999), https://doi.org/10.1090/S0025-5718-99-01056-X (only accessible summary inspected for this comparison).
