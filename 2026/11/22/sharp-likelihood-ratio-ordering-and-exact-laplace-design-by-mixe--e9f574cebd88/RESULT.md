# Sharp likelihood-ratio ordering and exact Laplace design by mixed-phase resetting

## Finding

For a one-dimensional intermittent particle alternating Brownian diffusion and symmetric ballistic relocation, the stationary **absolute-position laws for every mixture of two complete-reset modes form one strict likelihood-ratio chain**, with a sharp reversal as the resetting rate varies. Moreover, **exactly one interior mixture of resetting into the diffusive or ballistic phase produces a pure Laplace stationary position law**, except on the previously known balance surface where every mixture is Laplace. The same classification gives one common spatial crossing of all nonidentical stationary densities and one boundary between opposite logarithmic curvatures.

Precisely, fix positive diffusion coefficient \(D\), ballistic speed \(v\), switching rates \(a\) (diffusive to ballistic) and \(b\) (ballistic to diffusive), and Poisson reset rate \(r\). At each reset, restart at the origin in an equally randomized ballistic direction with probability \(\theta\in[0,1]\) and in the diffusive phase with probability \(1-\theta\). Write \(p_\theta(x)\) for the stationary position density, \(\ell=r+b\), \(S=r+a+b\), and
\[
\Delta=v^2-D(r+b).
\]
For any \(0\le\theta_1<\theta_2\le1\) and every \(x>0\), the radial density ratio \(p_{\theta_1}(x)/p_{\theta_2}(x)\) is **strictly decreasing in \(x\)** if \(\Delta>0\), **strictly increasing** if \(\Delta<0\), and identically one if \(\Delta=0\). Thus the absolute-position distributions are strictly ordered in likelihood-ratio order, and hence in stochastic order, with the indicated direction. The order reverses at the single positive resetting rate \(r_*=v^2/D-b\) when \(v^2>Db\); if \(v^2\le Db\), the ballistic-start mixture is always the more concentrated one for \(r>0\).

Define \(0<\lambda_-<\lambda_+\) through the factorization
\[
Q(k)=(r+Dk^2)[(r+b)^2+v^2k^2]+a[r(r+b)+v^2k^2]
=Dv^2(k^2+\lambda_-^2)(k^2+\lambda_+^2).
\]
When \(\Delta\ne0\), there is **exactly one** \(\theta_*\in(0,1)\) for which the stationary law is a single exponential rather than a genuine two-exponential combination:
\[
\boxed{\displaystyle
\theta_* =\frac{v^2-\ell S/\lambda_+^2}{v^2-D\ell},\qquad
p_{\theta_*}(x)=\frac{\lambda_-}{2}e^{-\lambda_-|x|}.}
\]
For every \(x>0\), \((\log p_\theta)''(x)\) has the sign of \(\Delta(\theta_*-\theta)\); it vanishes exactly at \(\theta_*\). At \(\Delta=0\), all \(\theta\) yield the same known Laplace law with \(\lambda_-=\sqrt{r/D}\).

When \(\Delta\ne0\), **all** pairs of distinct \(p_\theta\) intersect at the same unique positive radius
\[
\boxed{\displaystyle x_*=\frac{\log(\lambda_+/\lambda_-)}{\lambda_+-\lambda_-}.}
\]
The exact difference in stationary radial tail probabilities, for \(x>0\), is
\[
\Pr_{\theta_1}(|X|>x)-\Pr_{\theta_2}(|X|>x)
=\frac{(\theta_2-\theta_1)r\Delta}{Dv^2(\lambda_+^2-\lambda_-^2)}
\big(e^{-\lambda_+ x}-e^{-\lambda_- x}\big).
\]
It therefore compares **every** nonconstant nondecreasing continuous loss of absolute displacement having finite expectation, not only its variance. The exact differences in all positive real moments follow by integration.

## Assumptions and scope

Let \((X_t,J_t)\) be a continuous-time process on \(\mathbb R\times\{0,+,-\}\). In state \(0\), \(dX_t=\sqrt{2D}\,dW_t\); in states \(+\) and \(-\), \(dX_t=\pm v\,dt\). Transitions \(0\to+\) and \(0\to-\) occur independently with rate \(a/2\) each; each ballistic state changes to \(0\) at rate \(b\). Independent Poisson events of rate \(r\) reset position to zero and redraw the phase as \(0\) with probability \(1-\theta\), or \(+\) and \(-\) with probability \(\theta/2\) each. All rates and \(D,v\) are strictly positive, and \(\theta\in[0,1]\). Each reset fully renews the position and motion phase. The position marginal at stationarity is symmetric and has a strictly positive continuous density. Its absolute-position density is \(2p_\theta(x)\) for \(x>0\). Likelihood-ratio order is used in that standard radial sense; it is not a claim of pathwise coupling, first-passage ordering, or process-level equivalence.

## Proof

**1. Stationarity and Fourier transforms.** Every reset starts an independent excursion, and the mean excursion length is \(1/r\), so the regenerative occupation law is the unique invariant probability. The finite-speed and Brownian pieces, together with exponentially distributed cycle length, ensure finite polynomial position moments. Let \(z=k^2\), \(\ell=r+b\), and \(S=r+a+b\). Solving the stationary Fourier balance equations for the three internal phases gives, for pure diffusive and pure ballistic resetting respectively,
\[
\Phi_D(k)=\frac{r(\ell S+v^2z)}{Q(k)},\qquad
\Phi_B(k)=\frac{r\ell(S+Dz)}{Q(k)}.
\]
The mixed resetting protocol has \(\Phi_\theta=(1-\theta)\Phi_D+\theta\Phi_B\), and consequently
\[
\Phi_\theta(k)=\frac{r(\ell S+A_\theta z)}{Q(k)},\qquad
A_\theta=(1-\theta)v^2+\theta D\ell.
\]
In particular,
\[
\Phi_D(k)-\Phi_B(k)=\frac{r\Delta k^2}{Q(k)}.
\]
This last identity and the special balance \(\Delta=0\) were already identified in earlier work (Reference 2); they are premises for the *new* order and inverse-design classification, not independent originality claims.

**2. Spectral roots and density coefficients.** With \(q(t)=Q(i\sqrt t)\),
\[
q(0)=r\ell S>0,\quad q(\ell^2/v^2)=-ab\ell<0,\quad q((r+a)/D)=-ab\ell<0.
\]
The quadratic \(q\) has leading coefficient \(Dv^2>0\), and hence precisely two distinct positive roots \(u<w\). Let \(\lambda_-=\sqrt u\) and \(\lambda_+=\sqrt w\). The two negative evaluations show \(u<\ell^2/v^2\) and \(u<(r+a)/D\). Put \(t_\theta=\ell S/A_\theta\) and \(c_\theta=rA_\theta/(Dv^2)\). Inverse Fourier transformation yields, for \(x\ge0\),
\[
p_\theta(x)=U_\theta e^{-\lambda_-x}+V_\theta e^{-\lambda_+x},
\]
\[
U_\theta=\frac{c_\theta(t_\theta-u)}{2\lambda_-(w-u)},\qquad
V_\theta=\frac{c_\theta(w-t_\theta)}{2\lambda_+(w-u)}.
\]
The bound \(u<\min(\ell^2/v^2,(r+a)/D)\), along with \(S>\ell\) and \(S>r+a\), ensures \(t_0=\ell S/v^2>u\) and \(t_1=S/D>u\); since \(t_\theta\) lies between these endpoints, **\(U_\theta>0\)** for all \(\theta\). The density is positive by the regenerative representation.

Direct substitution gives
\[
q(t_0)=-\frac{a\ell S\Delta}{v^2},\qquad
q(t_1)=\frac{bS\Delta}{D}.
\]
Since \(t_0,t_1>u\), these imply that \(V_0\) has the sign of \(\Delta\) and \(V_1\) has the opposite sign when \(\Delta\ne0\). The fast-mode coefficient is affine in \(\theta\):
\[
V_\theta=\frac{r(wA_\theta-\ell S)}{2Dv^2\lambda_+(w-u)}.
\]
It therefore has exactly one zero \(\theta_*\in(0,1)\), at the displayed expression. At that value, Fourier normalization forces \(p_{\theta_*}(x)=(\lambda_-/2)e^{-\lambda_-|x|}\). When \(\Delta=0\), \(Q(k)=\ell(r+Dk^2)(S+Dk^2)\) and every \(\Phi_\theta(k)=r/(r+Dk^2)\). Thus all mixtures are identical, and the purported uniqueness exception is essential.

**3. A sharp one-crossing formula and likelihood-ratio ordering.** Write \(H=\lambda_+\), \(L=\lambda_-\) for this step only, and set \(K=r\Delta/[2Dv^2(w-u)]\). Inverting the characteristic-function difference gives
\[
p_0(x)-p_1(x)=K(He^{-Hx}-Le^{-Lx}),\quad x\ge0.
\]
This has exactly one positive zero, \(x_*=\log(H/L)/(H-L)\), whenever \(K\ne0\). By linearity, \(p_{\theta_1}-p_{\theta_2}=(\theta_2-\theta_1)(p_0-p_1)\). Integrating over both tails gives the claimed tail-difference formula, with a strict sign at every radius \(x>0\).

For the stronger likelihood-ratio statement, write \(p_1(x)=A e^{-Lx}+B e^{-Hx}\) and \(y=e^{-(H-L)x}\). Then \(p_0(x)=(A-KL)e^{-Lx}+(B+KH)e^{-Hx}\), so
\[
\frac{d}{dx}\frac{p_0(x)}{p_1(x)}
=-\frac{(H-L)yK(HA+LB)}{(A+By)^2}.
\]
The quantity \(HA+LB\) is strictly positive: substituting the two coefficients from step 2 gives \(HA+LB=r\ell S/(2Dv^2LH)>0\). Both denominator factors are positive. For arbitrary \(\theta_1<\theta_2\), the numerator determinant of the two corresponding two-exponential mixtures is multiplied by \(\theta_2-\theta_1>0\); hence the derivative of \(p_{\theta_1}/p_{\theta_2}\) has precisely the sign of \(-\Delta\) for every \(x>0\). This proves the strict likelihood-ratio chain and its sharp reset-rate reversal. The tail formula also directly proves the stochastic and increasing-loss orders without relying on general order theory.

**4. Logarithmic curvature.** For \(p(x)=Ue^{-Lx}+Ve^{-Hx}>0\),
\[
(\log p)''(x)=\frac{UV(H-L)^2e^{-(H+L)x}}{p(x)^2},\qquad x>0.
\]
Since \(U_\theta>0\) and \(V_\theta\) has the sign of \(\Delta(\theta_*-\theta)\), this gives the asserted sharp curvature classification. It is a half-line assertion and does not assert global log-convexity across the cusp at the reset origin.

## Verification

A standalone Python checker `CHECK.py` symbolically rederives the Fourier denominator, two protocol transforms, their difference, two spectral interlacing inequalities, the balance factorization, and the stationary variance contrast. It independently solves the complex three-by-three stationary Fourier-generator equations on both sides of the threshold and at equality. For additional positive parameter grids, it checks normalization, positivity, exact density/tail differences, the one-crossing radius, likelihood-ratio signs, logarithmic curvature, the unique interior Laplace mixing probability, and arbitrary positive real moment differences. Running `python CHECK.py` with NumPy and SymPy passes 5,910 assertions. This finite testing supplements the four-step all-parameter proof.

For example, with \(r=a=b=D=1\) and \(v=2\), one has \(\Delta=2>0\),
\[
\lambda_-^2=\frac{3-\sqrt3}{2},\qquad
\lambda_+^2=\frac{3+\sqrt3}{2},\qquad
\theta_*=\sqrt3-1.
\]
Thus restarting ballistically with probability \(\sqrt3-1\) yields **exactly** the Laplace density of scale \(1/\lambda_-\), even though neither pure reset protocol yields a Laplace law.

## Relationship to prior work

Flaquer-Galmés, Campos, and Méndez (Reference 1) introduce precisely the alternating diffusion/ballistic model and give the two pure-start stationary distributions, the search-time laws, and an equal-weight mixture in Appendix A. They do **not** give the full mixture likelihood-ratio chain, the all-cost reversal, the universal spatial crossing, the unique inverse-designed pure Laplace weight, or the logarithmic-curvature boundary. The new theorem derives these from the existing propagator framework.

The published *Exact spatial aliasing and strict temporal separation in intermittent resetting transport* (Reference 2) already proves the stationary-distribution equality at \(v^2=D(r+b)\) and strict temporal-covariance distinctions. That equality is explicitly **not** claimed as new here. Its all-time covariance conclusions do not imply the off-balance likelihood-ratio/stochastic ordering or the unique Laplace design for \(\Delta\ne0\); the present claim is restricted to the latter static mixture classification.

Santra, Olsen, and Gupta (Reference 3) study general switching-process propagators and non-reset intermittent active motion, including spatial cumulants, but not the specific complete-reset mixture and the present ordering and inverse-design classification. The generic fact that ratios of two-exponential mixtures can be monotone is not itself an originality claim; the finding is the sharp *physical parameter-domain* and *mixed-reset* classification, with genuine probability constraints and an observable risk reversal. Other broader switching or two-exponential total-positivity results could make the algebraic mechanism familiar; no independent publication-priority certification is asserted.

## Limitations

All conclusions require positive diffusion, speed, switching and reset rates; symmetric independently redrawn ballistic directions; complete instantaneous Poisson resetting of both position and internal phase; one spatial dimension; and observation of stationary **position**, not joint phase, paths, first-arrival times, or nonequilibrium dissipation. The mixed-reset parameter \(\theta\) is an independently sampled Bernoulli choice at *each* reset. Equal one-point densities at balance or at the tuned Laplace mixture do not imply equality of dynamical laws. The logarithmic curvature statement applies for positive radii, not across the cusp at the origin. Exact ordering or priority is not asserted for different reset mechanisms or unexamined broader classes.

## References

1. R. Flaquer-Galmés, D. Campos, and V. Méndez, *Intermittent random walks under stochastic resetting*, Physical Review E **109**, 034103 (2024); arXiv:2401.16849, first public 2024-01-30, https://arxiv.org/abs/2401.16849, doi:10.1103/PhysRevE.109.034103. Sections II–III and Appendix A.
2. *Exact spatial aliasing and strict temporal separation in intermittent resetting transport*, publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-exact-spatial-aliasing-and-strict-temporal-separation-in-intermi--a1ab52a1b12f/RESULT.md.
3. I. Santra, K. S. Olsen, and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, Soft Matter **20**, 9360–9372 (2024); arXiv:2408.16643, first public 2024-08-29, https://arxiv.org/abs/2408.16643, doi:10.1039/D4SM01054J.
