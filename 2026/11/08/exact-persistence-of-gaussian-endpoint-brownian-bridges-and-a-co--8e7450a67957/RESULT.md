# Exact persistence of Gaussian-endpoint Brownian bridges and a covariance-rank crossover

## Finding
Let \(B\) be a standard Brownian bridge on \([0,1]\), and let \(Y=(Y_0,Y_1)\sim N(0,C)\) be an independent centered Gaussian vector with any fixed positive-semidefinite \(2\times2\) covariance \(C\). For each \(r>0\), define the continuous Gaussian process
\[
X_r(s)=B(s)+\sqrt r\,[(1-s)Y_0+sY_1],\qquad 0\le s\le1,
\]
and its persistence probability \(S_C(r)=\Pr\{X_r(s)\ge0\text{ for all }s\in[0,1]\}\).

**Positive-definite case.** Write
\[
C=\begin{pmatrix}v&c\\c&w\end{pmatrix},\quad v,w>0,\quad \Delta=vw-c^2>0,\quad \rho=c/\sqrt{vw},\quad \tau_r=\rho-2r\Delta/\sqrt{vw}.
\]
Define the elementary function, for every \(t<1\),
\[
J(t)=\int_0^\infty\frac{du}{u^2-2tu+1}
=\begin{cases}
\dfrac{\frac\pi2+\arcsin t}{\sqrt{1-t^2}},&-1<t<1,\\[2pt]
1,&t=-1,\\[2pt]
\dfrac{\operatorname{arcosh}(-t)}{\sqrt{t^2-1}},&t<-1.
\end{cases}
\]
Then, **for every \(r>0\)**,
\[
\boxed{S_C(r)=\frac14+\frac{\arcsin\rho}{2\pi}-\frac{\sqrt\Delta}{2\pi\sqrt{vw}}J(\tau_r).}
\]
In particular, for fixed \(C\succ0\),
\[
\boxed{S_C(\infty)-S_C(r)\sim\frac{\log r}{4\pi r\sqrt{\det C}},\qquad S_C(\infty)=\frac14+\frac{\arcsin\rho}{2\pi}.}
\]

**Rank-one and zero cases.** If \(C=aa^{\mathsf T}\), with \(a=(a_0,a_1)\in\mathbb R^2\), then
\[
\boxed{S_C(r)=\begin{cases}
\frac12\bigl(1-(1+4r a_0a_1)^{-1/2}\bigr),&a_0a_1>0,\\
0,&a_0a_1\le0.
\end{cases}}
\]
When \(a_0a_1>0\), the limiting persistence probability is \(1/2\), but its deficit is of a different order:
\[
\boxed{\tfrac12-S_C(r)\sim\frac1{4\sqrt{r a_0a_1}}.}
\]
For the zero covariance \(C=0\), persistence is zero. Thus full-rank Gaussian endpoints have a \((\log r)/r\) persistence deficit, while positively aligned rank-one endpoints have an \(r^{-1/2}\) deficit; anticorrelated rank-one endpoints have zero persistence at every scale.

## Assumptions and scope
The bridge has variance \(\operatorname{Var}(B(s))=s(1-s)\) and is independent of \(Y\). All probabilities concern the **entire continuous path**, including its two endpoints, not a finite observation grid. The scale \(r\) multiplies the endpoint covariance; the original covariance \(C\) is held fixed when \(r\to\infty\). The rank-one parameterization \(C=aa^{\mathsf T}\) includes both positive and negatively aligned endpoint vectors and the possibility of a zero coordinate. The event \(X_r\ge0\) has the same probability as \(X_r>0\) in the interior when both endpoint values are strictly positive; when either endpoint is zero, the Brownian-bridge survival probability is zero.

## Proof
**1. Brownian reflection.** Condition on the endpoint pair \(\sqrt rY=(u,v)\). Its interpolated bridge is a standard Brownian bridge from \(u\) to \(v\). With \(p_1(z)=(2\pi)^{-1/2}e^{-z^2/2}\), reflection at the origin gives the killed heat kernel \(p_1(v-u)-p_1(v+u)\) for \(u,v>0\). Dividing by the unconditional bridge transition density yields
\[
\Pr\bigl(\min_{0\le s\le1}X_r(s)\ge0\mid \sqrt rY=(u,v)\bigr)
=\mathbf1_{\{u>0,v>0\}}(1-e^{-2uv}).
\]
Endpoints at zero have conditional probability zero by immediate Brownian oscillation. Consequently,
\[
S_C(r)=\Pr(Y_0>0,Y_1>0)-D_C(r),\quad
D_C(r)=\mathbb E[e^{-2rY_0Y_1}\mathbf1_{\{Y_0>0,Y_1>0\}}].
\]
This identity holds even for singular Gaussian covariances.

**2. The exact two-dimensional integral.** If \(C\succ0\), its bivariate normal density is
\[
(2\pi\sqrt\Delta)^{-1}\exp\!\left[-\frac{w u^2+v z^2-2cuz}{2\Delta}\right].
\]
Substitute \(x=u\sqrt{w/\Delta}\) and \(y=z\sqrt{v/\Delta}\), obtaining
\[
D_C(r)=\frac{\sqrt\Delta}{2\pi\sqrt{vw}}
\int_{x,y>0}\exp\!\left[-\tfrac12(x^2+y^2)+\tau_rxy\right]dx\,dy.
\]
For \(\tau_r<1\), polar coordinates \(x=s\cos\theta\), \(y=s\sin\theta\) and integration of \(s\exp[-s^2(1-\tau_r\sin 2\theta)/2]\) give
\[
\int_0^{\pi/2}\frac{d\theta}{1-\tau_r\sin2\theta}
=\int_0^\infty\frac{dt}{t^2-2\tau_rt+1}=J(\tau_r).
\]
Completing the square in the last integral gives each of the displayed elementary branches for \(J\). The centered bivariate-normal orthant identity gives \(\Pr(Y_0>0,Y_1>0)=1/4+\arcsin(\rho)/(2\pi)\). Substitution proves the exact formula.

**3. Full-rank high-scale limit.** As \(s\to+\infty\),
\[
J(-s)=\frac{\operatorname{arcosh}s}{\sqrt{s^2-1}}=\frac{\log(2s)+O(s^{-2}\log s)}s.
\]
Here \(-\tau_r=2r\Delta/\sqrt{vw}-\rho\sim2r\Delta/\sqrt{vw}\). The prefactor in step 2 therefore gives
\[
D_C(r)=\frac{\log r+O_C(1)}{4\pi r\sqrt\Delta},
\]
which proves both the positive-definite limit and its sharp logarithmic leading constant. In particular, the constant cannot be obtained by merely inserting a finite endpoint probability into the reflection formula without analyzing the singular quadrant integral.

**4. Singular covariances.** If \(C=aa^{\mathsf T}\), write \(Y=aZ\), where \(Z\sim N(0,1)\). When \(a_0a_1\le0\), both endpoints cannot be strictly positive and the persistence probability is zero. When \(a_0a_1>0\), the event of both positive endpoints is precisely one half-line of \(Z\). Evenness of the Gaussian density and the reflection identity yield
\[
S_C(r)=\tfrac12\bigl(1-\mathbb E e^{-2ra_0a_1Z^2}\bigr)
=\tfrac12\bigl(1-(1+4ra_0a_1)^{-1/2}\bigr).
\]
The \(r^{-1/2}\) deficit follows by direct expansion. For \(a=0\), the process is the standard pinned bridge, which is nonnegative throughout with probability zero.

## Verification
Run `python verify_persistence.py` with Python 3 and SciPy. The checker compares the displayed closed form with **independent direct bivariate Gaussian quadrature** over the positive quadrant across a range of covariance correlations and scales, checks the singular rank-one formula against one-dimensional quadrature, and diagnoses both high-scale laws. It reports 37 passing numerical assertions. The exact integral transformations, reflection argument, and asymptotic expansions above, not numerical tests, prove the continuum and infinite-scale statements.

## Relationship to prior work
Raket's 2026 endpoint classification provides the covariance parameterization and independent bridge-plus-Gaussian-endpoint representation used here. The companion bestiary documents related Brownian boundary processes. Those sources are credited for the process representation; the new claim is the **exact persistence functional for all endpoint covariances** and the **different high-scale rates at full versus singular rank**. The reflection formula for a Brownian bridge with deterministic positive endpoints, and the Gaussian orthant probability, are classical inputs. The persistence law does not follow from the covariance classification without integrating a nontrivial quadrant kernel and resolving its large-scale boundary layer. Earlier Gaussian-bridge maximum work exists, and historical priority of every equivalent integrated formula has not been established.

## Limitations
These formulas concern a driftless, unit-duration Brownian bridge with centered Gaussian endpoints and a common scalar covariance multiplier. They do not establish persistence for arbitrary Gaussian processes, time-dependent boundaries, non-Gaussian endpoints, or rates uniform as a positive-definite covariance approaches rank one. The high-scale limits hold **for each fixed covariance**; the limits in \(r\) and \(\det C\downarrow0\) are not interchangeable without extra analysis. No claim of independent external validation or complete historical priority is made.

## References
- L. L. Raket, *Brownian covariances on an interval: a complete endpoint classification*, arXiv:2610.36762v1, first posted 27 October 2026, https://arxiv.org/abs/2610.36762.
- L. L. Raket, *A Bestiary of Brownian Processes: A Field Guide to Boundary Conditions and Conditioning*, arXiv:2610.33747v1, first posted 24 October 2026, https://arxiv.org/abs/2610.33747.
- M. Abundo, *Asymptotic of the running maximum distribution of a Gaussian Bridge*, Stochastic Analysis and Applications 41 (2023), online 2022, https://doi.org/10.1080/07362994.2022.2123344 (related but potentially broader prior maximum-distribution literature).
