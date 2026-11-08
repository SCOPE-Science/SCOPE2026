# Exact stationary noise laws for one-delay accelerated momentum and delayed gradient descent

## Finding

The deterministic accelerated tuning of the one-delay generalized momentum method in Gürbüzbalaban et al., Proposition 3.19, has a precisely quantifiable steady-state noise penalty. For independent additive gradient noise of common coordinate variance \(\sigma^2>0\) on the two-dimensional diagonal quadratic with eigenvalues \(\mu=L/\kappa\) and \(L\), its stationary mean-square iterate error satisfies, with fixed \(L>0\),

\[
\lim_{\kappa\to\infty}\frac{8L^2}{\sigma^2\kappa^{3/2}}\lim_{k\to\infty}\mathbb E\|x_k\|_2^2=1.
\]

The slow and fast spectral modes separately satisfy

\[
\mathbb E|x_{\infty,\mu}|^2\sim\frac{\sigma^2}{8L^2}\kappa^{3/2},\qquad
\mathbb E|x_{\infty,L}|^2\sim\frac{\sigma^2}{7L^2}\sqrt\kappa.
\]

By contrast, one-step delayed gradient descent with its **own optimal worst-case deterministic spectral-radius stepsize** has stationary squared error \(5\sigma^2\kappa/(6L^2)\) asymptotically. Thus the exact asymptotic ratio of the stationary total errors is

\[
\boxed{\displaystyle\frac{\mathbb E\|x_{\infty}^{\rm GMM}\|_2^2}{\mathbb E\|x_{\infty}^{\rm DGD}\|_2^2}\sim\frac{3}{20}\sqrt\kappa.}
\]

The accelerated method has worst-case deterministic spectral factor \(1-1/(2\sqrt\kappa)\), while optimally tuned delayed gradient descent has factor \(\kappa/(\kappa+1)\). This is a comparison of *these particular rate-tuned constant-parameter methods*, not a general lower bound for all stochastic acceleration schemes.

## Assumptions and scope

Fix real \(L>0\), \(\sigma^2>0\), \(\kappa>1\), and let \(q=\kappa^{-1/2}\in(0,1)\), \(\mu=Lq^2\), \(A=\operatorname{diag}(\mu,L)\), and \(f(x)=\frac12 x^\top Ax\) on \(\mathbb R^2\). The unique minimizer is zero. At each iteration, let \(\xi_k\in\mathbb R^2\) be independent across \(k\), independent of the initial history, centered, with \(\mathbb E(\xi_k\xi_k^\top)=\sigma^2 I_2\). No Gaussian assumption is needed. Initial histories have finite second moments.

For one-step delayed generalized momentum, define

\[
 y_k=x_k+\nu(x_k-x_{k-1}),\qquad
 x_{k+1}=x_k+\beta(x_k-x_{k-1})-\alpha(Ay_{k-1}+\xi_k),
\]

with the *published* deterministic accelerated choice

\[
 \alpha=\frac{2-q^2}{8L},\quad
 \beta=1-q+\frac{q^2}{2},\quad
 \nu=\frac{4-4q+q^2}{2-q^2}.
\]

For the delayed-gradient comparator, define

\[
 z_{k+1}=z_k-h(Az_{k-1}+\xi_k),\qquad
 h=h_*=\frac{\kappa^2}{L(\kappa+1)^2}.
\]

The symbol \(x_{\infty}\) means a stationary second-moment limit, not a sample-path almost-sure pointwise limit. Both fixed-parameter recurrences have stable companion matrices in this scope.

## Proof

**1. Cubic modal dynamics.** Fix an eigenvalue \(\lambda=tL\) with \(t\in\{q^2,1\}\). Define \(d=\alpha L=(2-q^2)/8\) and \(e=d\nu=(4-4q+q^2)/8\). Writing \(u_k\) for its coordinate and suppressing the coordinate of the centered noise, direct substitution gives

\[
 u_{k+1}=a u_k+b_tu_{k-1}+c_tu_{k-2}-\alpha\xi_k,
 \quad a=1+\beta,\quad b_t=-\beta-t(d+e),\quad c_t=te.
\]

Its characteristic polynomial \(z^3-az^2-b_tz-c_t\) equals equation (81) of Gürbüzbalaban et al. The latter's Proposition 3.19 proves, by a Schur--Cohn argument on the full spectral interval, that its roots have modulus at most \(\rho=1-q/2<1\). Therefore a unique stationary covariance exists, and the effect of any finite-second-moment initialization vanishes.

**2. Exact cubic stationary variance.** For an arbitrary real Schur-stable recurrence \(U_{k+1}=aU_k+bU_{k-1}+cU_{k-2}+\varepsilon_k\) with innovation variance \(w>0\), set \(r_j=\mathbb E(U_kU_{k-j})\) at stationarity. Independence gives the Yule--Walker identities

\[
 r_1=ar_0+br_1+cr_2,\quad
 r_2=(a+c)r_1+br_0,\quad
 r_3=ar_2+br_1+cr_0,
\]
\[
 r_0=ar_1+br_2+cr_3+w.
\]

Eliminate \(r_1,r_2,r_3\) to obtain the exact rational expression

\[
 \boxed{\displaystyle\frac{r_0}{w}=\mathcal R(a,b,c)=
 \frac{1-b-c^2-ac}{(1+a-b+c)(1-a-b-c)(1+b-c^2+ac)}.}
\]

Each denominator is nonzero for a Schur-stable companion matrix (equivalently a positive definite stationary covariance). In the delayed GMM modal recurrence \(w=\alpha^2\sigma^2\), so the exact finite-\(\kappa\) formula is

\[
 V_t=\lim_{k\to\infty}\mathbb E|u_k|^2=
 \frac{\sigma^2(2-q^2)^2}{64L^2}\,\mathcal R(a,b_t,c_t),\quad t\in\{q^2,1\}.
\]

**3. Exact endpoint asymptotics.** In the four factors of \(\mathcal R\), denote the numerator by \(N\) and denominator factors in their displayed order by \(D_1,D_2,D_3\). Direct polynomial substitution and expansion give

\[
 \begin{array}{c|cccc}
 t & N & D_1&D_2&D_3\\\hline
 q^2 &2+O(q)&4+O(q)&q^2/4+O(q^4)&q+O(q^2)\\
 1&3/2+O(q)&21/4+O(q)&1/4+O(q^2)&q/2+O(q^2)
 \end{array}
\]

as \(q\downarrow0\). Consequently \(\mathcal R(a,b_{q^2},c_{q^2})\sim2q^{-3}\) and \(\mathcal R(a,b_1,c_1)\sim16/(7q)\). Since \(\alpha^2\to1/(16L^2)\), this proves the two modal limits and the total limit in the Finding.

**4. Exact optimal comparator and its stationary variance.** A delayed-gradient modal recurrence is \(z_{k+1}=z_k-u z_{k-1}-h\xi_k\) with \(u=h\lambda\). For \(0<u<1\), the roots of \(z^2-z+u\) have largest modulus

\[
 \varrho(u)=\begin{cases}(1+\sqrt{1-4u})/2,&0<u\le1/4,\\\sqrt u,&1/4\le u<1.\end{cases}
\]

This function first strictly decreases and then strictly increases. Over \(\lambda\in[\mu,L]\), the maximum is thus at one of the endpoints. Minimizing this maximum over stable \(0<h<1/L\) forces their equality. The unique solution is \(h=h_*\) above and \(\max\varrho(h_*\lambda)=\kappa/(\kappa+1)\). A two-lag Yule--Walker calculation gives for any mode

\[
 W_\lambda(h)=\lim_{k\to\infty}\mathbb E|z_{k,\lambda}|^2=
 \frac{h\sigma^2(1+h\lambda)}{\lambda(1-h\lambda)(2+h\lambda)}.
\]

At \(h=h_*\), the slow mode has \(h_*\mu=\kappa/(\kappa+1)^2\to0\), so \(W_\mu\sim\sigma^2\kappa/(2L^2)\). The fast mode has \(h_*L\to1\) with \(1-h_*L\sim2/\kappa\), hence \(W_L\sim\sigma^2\kappa/(3L^2)\). Sum these to obtain \(5\sigma^2\kappa/(6L^2)\), and divide the two methods' totals to obtain \((3/20)\sqrt\kappa\). This concludes the proof.

## Verification

The standalone script `checks/check.py` recomputes stationary variances from independent discrete Lyapunov equations over a range of spectral points, checks exact-rational Yule--Walker systems, tests sample trajectories and the root-radius and asymptotic comparisons. Running `python3 checks/check.py` using NumPy, SciPy and SymPy produces 459 supplementary checks (450 numerical/simulation and 9 exact-rational). The algebraic proof above, not finite diagnostics, establishes the limit for every \(\kappa>1\).

## Relationship to prior work

Gürbüzbalaban et al. (2026), Proposition 3.19 and equation (81), supply the deterministic one-delay parameters and their exact spectral factor; both are credited and not claimed as new. Their conclusion explicitly identifies stochastic gradients as an open direction, while their analysis contains no stationary variance law for this tuning. Mohammadi, Razaviyayn and Jovanović (2022/2024) already establish broad deterministic-rate versus noise-amplification tradeoffs, including a \(\sqrt\kappa\)-relative penalty for classical *two-state, no-delay* HB/NAG; the scaling phenomenon by itself is not new. The present finding isolates the higher-order **one-delay cubic** dynamics and derives its particular two-mode exact rational variance and sharp constants against a **rate-optimized one-delay** comparator. Stich and Karimireddy (2020) prove broader nonasymptotic stochastic delayed-GD rates under differing stepsize/accuracy regimes rather than the present constant-gain stationary DREAM law.

## Limitations

This is a two-dimensional diagonal quadratic, fixed unit delay, exact arithmetic, white additive gradient noise, and a specified published deterministic tuning. It does not show that stochastic DREAM cannot be improved by a different tuning, diminishing steps, averaging, noise compensation, or a different performance criterion. It neither establishes a universal information-theoretic noise lower bound nor extends the formulas to time-varying delays or nonlinear objectives. Existence of stationary *second moments* is proved; a full distributional description needs assumptions on the noise law. There has been no independent audit.

## References

1. M. Gürbüzbalaban, M. H. Rafi, N. S. Aybat, W. U. Bajwa, *DREAM: Delay-Resistant Acceleration with Momentum*, arXiv:2610.37444v1 (first publicly released 2026-10-27), Proposition 3.19 and equations (81)--(83). https://arxiv.org/html/2610.37444v1
2. H. Mohammadi, M. Razaviyayn, M. R. Jovanović, *Tradeoffs between convergence rate and noise amplification for momentum-based accelerated optimization algorithms*, arXiv:2209.11920 (initial release 2022-09-24; later IEEE Transactions on Automatic Control 70 (2025), 889--904). https://arxiv.org/pdf/2209.11920
3. S. U. Stich, S. P. Karimireddy, *The Error-Feedback Framework: Better Rates for SGD with Delayed Gradients and Compressed Updates*, Journal of Machine Learning Research 21 (2020). https://jmlr.csail.mit.edu/papers/volume21/19-748/19-748.pdf
