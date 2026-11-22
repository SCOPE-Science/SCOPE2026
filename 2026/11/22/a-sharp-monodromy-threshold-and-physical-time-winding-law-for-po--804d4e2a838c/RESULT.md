# A sharp monodromy threshold and physical-time winding law for polynomial angular bottlenecks

## Finding

For every integer \(k\geq1\) and all constants \(a,b,c>0\), let \(R=x^2+y^2\) and consider the real polynomial vector field

\[
\begin{aligned}
\dot x&=-aR^kx-(by^2+cR^2)y,\\
\dot y&=-aR^ky+(by^2+cR^2)x.
\end{aligned}
\tag{1}
\]

Its origin is globally asymptotically attracting and its angular velocity is strictly positive at every nonzero point. Nevertheless, **there is a sharp change in monodromy at \(k=2\)**: for \(k=1\) every nonstationary trajectory has finite total angular displacement and approaches one of the two directions of the horizontal axis; for every \(k\geq2\) every nonstationary trajectory winds around the origin infinitely often and the origin is monodromic.

More precisely, let \(\theta(t)\) be any continuous lift of the polar angle of a nonzero solution, and put \(N(t)=(\theta(t)-\theta(0))/(2\pi)\). Then, for \(k\geq2\),

\[
\lim_{t\to\infty}\frac{N(t)}{(2kat)^{(2k-3)/(2k)}}
=\frac{\sqrt{bc}}{2\pi a(2k-3)}.
\tag{2}
\]

For the normalized quintic example \(k=2\), \(a=b=c=1\), this specializes to \(N(t)\sim t^{1/4}/(\pi\sqrt2)\); the physical time of the \(n\)-th completed revolution is asymptotic to \(4\pi^4n^4\). These results distinguish infinite winding and finite winding even though both regimes have global radial attraction and no nontrivial curve of zero angular speed.

## Assumptions and scope

The parameters \(a,b,c\) are arbitrary strictly positive real numbers, and \(k\) is an integer at least one. The system is studied on the entire plane; a trajectory with nonzero initial point remains nonzero at every finite positive time. Angular speed means the ordinary polar derivative \(\dot\theta\) off the origin. Monodromic means every sufficiently close nontrivial orbit winds arbitrarily often about the singularity, equivalently there are no approaching characteristic trajectories with a limiting polar direction in this explicit flow. Winding count \(N(t)\) is a real number; changing the initial angle lift by an integer multiple of \(2\pi\) does not change it. The positive parameter assumptions are needed for the uniform sign and for the specific asymptotic constants.

## Proof

**1. Exact polar reduction and radial attraction.** Put \(x=r\cos\theta\), \(y=r\sin\theta\). From (1), direct multiplication gives

\[
x\dot x+y\dot y=-aR^{k+1},\qquad
x\dot y-y\dot x=R(by^2+cR^2).
\]

Consequently, for \(r>0\),

\[
\dot r=-ar^{2k+1},\qquad
\dot\theta=br^2\sin^2\theta+cr^4>0,\qquad
r(t)=\bigl(r_0^{-2k}+2kat\bigr)^{-1/(2k)}.
\tag{3}
\]

This explicit radial solution is positive for all finite \(t\geq0\), tends to zero, and bounds the orbit. The polynomial vector field is locally Lipschitz and no finite forward blow-up occurs. Thus the origin is the unique equilibrium and attracts every solution. The strict angular inequality proves that there is no nontrivial curve of zero ordinary angular velocity in the punctured plane.

**2. Finite winding at \(k=1\).** Set \(s=\log(r^{-2})\). By (3), \(ds/dt=2ar^2>0\) and \(s\to\infty\). With \(A=b/(2a)\), \(B=c/(2a)\), the angular equation becomes

\[
\frac{d\theta}{ds}=A\sin^2\theta+Be^{-s}.
\tag{4}
\]

We show that only finitely many levels \(n\pi\) can be crossed. Fix \(L=(2A)^{-1}\), choose \(D>\max\{1,L/\pi\}\), and put \(K_D=\sup_{u\geq D}u^2e^{-(u-D)}<\infty\). Take \(S\) sufficiently large that \(Be^{-S}K_D<L/2\). Suppose the increasing solution first or subsequently reaches a level \(n\pi\) at \(s_0\geq S\). Define, for \(s\geq s_0\) and \(u=s-s_0+D\), the strict upper barrier

\[
q(s)=(n+1)\pi-\frac{L}{u}.
\]

Initially \(\theta(s_0)=n\pi<q(s_0)\). Moreover \(q'=L/u^2\), while

\[
A\sin^2q+Be^{-s}
\leq\frac{AL^2}{u^2}+Be^{-s_0}e^{-(u-D)}
<\frac{L}{2u^2}+\frac{L}{2u^2}=q'.
\]

Here \(AL^2=L/2\) and the inequality \(\sin^2(L/u)\leq(L/u)^2\) were used. The scalar comparison theorem now yields \(\theta(s)<q(s)<(n+1)\pi\) for every \(s\geq s_0\). Therefore **at most one integer-multiple-of-\(\pi\) crossing occurs after \(S\)**, so \(\theta\) is bounded above. Because it is increasing, it has a finite limit. Equation (4) shows that this limit must satisfy \(\sin^2\theta_\infty=0\); otherwise its derivative stays bounded away from zero. Hence \(\theta_\infty\in\pi\mathbb Z\), and the trajectory approaches a horizontal limiting ray. The angular displacement before \(S\) is finite by smoothness. This proves the nonmonodromic statement for \(k=1\).

**3. Infinite winding and cycle time at \(k\geq2\).** For these integers, (3) gives \(\dot\theta\geq cr^4\), and

\[
\int_0^\infty r(t)^4\,dt=\infty
\qquad\text{because}\quad r(t)^4\asymp t^{-2/k}.
\]

Thus \(\theta(t)\to+\infty\), establishing monodromy. Define \(p=2k-3>0\) and the inverse-power radial coordinate \(U=r^{-p}\). Equation (3) gives the exact derivative

\[
\dot U=p a r^3.
\tag{5}
\]

For any *frozen* radius \(\rho>0\), the time needed for one full turn under angular velocity \(b\rho^2\sin^2\theta+c\rho^4\) is independent of the initial angle and equals

\[
T_{\mathrm{fr}}(\rho)
=\int_0^{2\pi}\frac{d\theta}{b\rho^2\sin^2\theta+c\rho^4}
=\frac{2\pi}{\rho^3\sqrt{c(b+c\rho^2)}}
\sim\frac{2\pi}{\sqrt{bc}\,\rho^3}.
\tag{6}
\]

The integral uses the elementary identity \(\int_0^{2\pi}(A+B\sin^2\theta)^{-1}d\theta=2\pi/\sqrt{A(A+B)}\) for \(A>0\), \(A+B>0\).

Let \(t_n\) be successive crossings of any fixed lifted phase modulo \(2\pi\), with \(\rho_n=r(t_n)\to0\). We claim

\[
t_{n+1}-t_n\sim T_{\mathrm{fr}}(\rho_n).
\tag{7}
\]

Indeed, let \(M=4\pi/\sqrt{bc}\). By the exact radial law (3), uniformly for \(0\leq\tau\leq M\rho_n^{-3}\),

\[
\frac{r(t_n+\tau)}{\rho_n}
=\bigl(1+2ka\rho_n^{2k}\tau\bigr)^{-1/(2k)}
=1+O(\rho_n^{2k-3})=1+o(1).
\]

At each angular position, the angular velocity is increasing as a function of the radius. Comparison with the frozen angular flows at radii \(\rho_n\) and \(r(t_n+M\rho_n^{-3})\), whose full-turn durations are given by (6), shows first that the next turn is completed before \(M\rho_n^{-3}\), and then squeezes its duration between two quantities asymptotic to the same right side of (7). This also justifies applying the uniform radial estimate throughout an entire turn.

Combining (5), (7), and the uniform relative change of \(r\) during a turn gives

\[
U(t_{n+1})-U(t_n)
=p a\int_{t_n}^{t_{n+1}}r(t)^3\,dt
\longrightarrow \frac{2\pi p a}{\sqrt{bc}}.
\tag{8}
\]

By Cesàro averaging, \(U(t_n)/n\to2\pi p a/\sqrt{bc}\). Between successive turn times, the increase of \(U\) is bounded and tends to the constant in (8), while \(U\to\infty\). Therefore for arbitrary \(t\to\infty\),

\[
\frac{N(t)}{U(t)}\longrightarrow\frac{\sqrt{bc}}{2\pi p a}.
\]

Using \(U(t)=\bigl(r_0^{-2k}+2kat\bigr)^{p/(2k)}\) proves (2). In the special case \(k=2\), \(a=b=c=1\), inverting the formula gives the stated quartic time law. Every comparison and limit applies to arbitrary fixed nonzero initial data, completing the proof. \(\square\)

## Verification

The accompanying standalone `verify.py` independently checks the Cartesian-to-polar identities by exact symbolic algebra for the first four integer orders. It integrates the angle-parametrized inverse-radius equation for four choices of \(k,a,b,c\), comparing 30-turn averages with the proved limiting coefficient; all four relative errors were below 5%. It additionally integrates eight positive-angle examples for \(k=1\) out to \(s=140\), observing approach to a finite integer multiple of \(\pi\). The exact test output is reproducible with Python, SymPy and SciPy. This is a finite computation supplement only: the proof of each all-time and all-parameter assertion is analytic and does not rely on the numerical tolerances.

## Relationship to prior work

García and Giné's November 11, 2026 work analyzes coefficients of Poincaré maps under monodromy and angular-speed conditions in analytic planar systems. Its hypotheses motivate distinguishing strict positive angular velocity from actual monodromy, but its reported results concern first-return coefficients, not physical-time winding counts. Their 2024 preprint on inverse integrating factors likewise concerns expansions and analyticity of Poincaré maps. The 2025 article on monodromic singularities without zero-angular-speed curves treats analytic return maps. These are relevant conceptual precedents, not claims of priority for the present polynomial family. Literature and indexed-result searches did not establish an equivalent full statement; absence of a search hit is not a proof of priority. See the accompanying review for detailed comparisons and limitations.

## Limitations

The classification is exact for the polynomial family (1), not a characterization of all analytic planar singularities with positive angular speed. The coefficient in (2) depends on the specific quadratic angular bottleneck and quartic regularization, and the integer-order threshold need not survive unrelated perturbations. The theorem does not assert that the origin has an analytic Poincaré return map or classify perturbation cyclicity. The numerical checker samples finite angle intervals and cannot independently establish infinite-time asymptotics. Independent mathematical audit has not been performed.

## References

1. I. A. García and J. Giné, *Stability of analytic monodromic singularities without curves of zero angular speed*, arXiv:2611.15233v1 (first public 11 November 2026), https://arxiv.org/abs/2611.15233.
2. I. A. García and J. Giné, *Principal Bautin ideal of monodromic singularities with inverse integrating factors*, arXiv:2412.09205v1 (12 December 2024), https://arxiv.org/abs/2412.09205.
3. I. A. García and J. Giné, *Monodromic singularities without curves of zero angular speed*, AIMS Mathematics 10 (2025), 1488–1500, https://doi.org/10.3934/math.2025069.
