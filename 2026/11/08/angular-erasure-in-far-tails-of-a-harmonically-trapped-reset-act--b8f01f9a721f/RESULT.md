# Angular erasure in far tails of a harmonically trapped reset active Brownian particle

## Finding
Consider the two-dimensional active Brownian particle that is returned to its initial position and heading at each point of an independent Poisson process. Fix a harmonic relaxation rate \(\beta>0\), translational diffusivity \(D>0\), propulsion speed \(v>0\), reset rate \(r>0\), and rotational diffusivity \(d\geq0\). For the unique stationary position \(R\in\mathbb R^2\) and every unit vector \(u_\phi=(\cos\phi,\sin\phi)\), define \(H_\phi(x)=\Pr(u_\phi\cdot R>x)\). Then, as \(x\to+\infty\),

\[
\log H_\phi(x)=-\frac{\beta}{2D}\left(x-\frac v\beta h_d(\phi)\right)^2+o(x),\qquad
h_d(\phi)=\begin{cases}1,&d>0,\\ \cos\phi,&d=0.\end{cases}
\]

The remainder \(o(x)\) is uniform in \(\phi\in[0,2\pi]\) for each fixed parameter set. Equivalently, the coefficient of \(x\) after subtraction of the leading \(-\beta x^2/(2D)\) is \(v/D\) in **every direction** when \(d>0\), but is \((v/D)\cos\phi\) when \(d=0\). Thus every strictly positive rotational diffusivity erases the reset-heading anisotropy at the first subleading order of the extreme-displacement tail, even though finite-order stationary observables remain anisotropic. The limits \(d\downarrow0\) and \(x\to\infty\) do not commute at directions other than the reset heading.

Also, for \(d>0\), the stationary transverse marginal is not Gaussian for any positive \(\beta,D,v,r\). In particular, a vanishing radial fourth-order excess kurtosis does not imply an exactly Gaussian stationary position law. The conclusion excludes limits in which parameters themselves vary with \(x\).

## Assumptions and scope
Between complete resets, take \(R_0=0\), \(\theta_0=0\), and independent standard Brownian motions \(B^1,B^2,W\):

\[
\mathrm dR_t=-\beta R_t\,\mathrm dt+v(\cos\theta_t,\sin\theta_t)\,\mathrm dt+\sqrt{2D}\,\mathrm d(B^1_t,B^2_t),\qquad
\mathrm d\theta_t=\sqrt{2d}\,\mathrm dW_t.
\]

At Poisson resets with rate \(r\), both \(R\) and \(\theta\) are returned to \((0,0)\); noise increments and reset waiting times are independent. Angular positions are taken modulo \(2\pi\). Here \(x>0\) is the displacement threshold, not elapsed time. The theorem concerns projections of the stationary *position*, not increments, the stationary radial density, the time-integrated current, or the nontrapped \(\beta=0\) case. The boundary case \(d=0\) fixes the orientation forever between resets and is included solely to expose the singular angular limit. In particular, the asserted isotropization requires \(d>0\).

## Proof
**1. Stationary renewal mixture.** Complete Poisson resetting produces a unique regenerative invariant distribution. At a stationary observation instant, the age \(T\) of the last reset is exponential with rate \(r\), independent of the fresh Brownian motions. For fixed direction \(\phi\),

\[
X_\phi=u_\phi\cdot R=A_\phi(T)+\sqrt{V(T)}Z,
\quad A_\phi(t)=v\int_0^t e^{-\beta(t-s)}\cos(\theta_s-\phi)\,\mathrm ds,
\quad V(t)=\frac D\beta(1-e^{-2\beta t}),
\]

where \(Z\sim N(0,1)\) is independent of \(T\) and the angular Brownian path. Define \(c=v/\beta\), \(\sigma^2=D/\beta\). For every path, \(|A_\phi(t)|\le c(1-e^{-\beta t})\le c\) and \(V(t)\le\sigma^2\). For \(x>c\), monotonicity of a Gaussian upper tail in its mean and variance yields, uniformly in \(\phi\),

\[
H_\phi(x)\le\overline\Phi((x-c)/\sigma),\qquad
\log H_\phi(x)\le-\frac{(x-c)^2}{2\sigma^2}+O(\log x).
\]

**2. Strictly positive angular diffusion.** Fix \(d>0\), put \(\delta=x^{-1/4}\), \(t_x=2+(3/\beta)\log x\), and restrict to \(t_x\le T\le t_x+1\). Require \(\theta_1\) to be within angular distance \(\delta/2\) of \(\phi\), and the angular process to remain within distance \(\delta\) of \(\phi\) during \([1,T]\). The heat kernel of Brownian motion on the circle at time 1 has a strictly positive minimum. The Dirichlet heat kernel on an interval of width \(2\delta\) then gives a lower probability, uniform in \(\phi\), of the form

\[
\Pr(\text{angular event},\ T\in[t_x,t_x+1])
\ge C\delta e^{-r(t_x+1)}
\exp\!\left(-C' d(t_x+1)\delta^{-2}\right).
\]

The constants depend on the fixed physical parameters, not on \(x\) or \(\phi\). This follows, for example, by retaining the positive first Dirichlet eigenfunction in an interior subinterval and using the Markov property. Its logarithm is \(-O(\sqrt x\log x)=o(x)\).

On this event, the contribution of \([0,1]\) to the active integral is bounded below by \(-c e^{-\beta(T-1)}\), while the contribution of \([1,T]\) is at least \(c\cos\delta(1-e^{-\beta(T-1)})\). Consequently,

\[
A_\phi(T)\ge c-O(x^{-1/2}),\qquad
V(T)\ge \sigma^2(1-O(x^{-6})),
\]

uniformly in \(\phi\). Taking the Gaussian right tail conditional on this event and applying the standard Mills expansion gives

\[
\log H_\phi(x)\ge-\frac{(x-c)^2}{2\sigma^2}
-O(\sqrt x\log x).
\]

Combined with the universal upper bound, this proves the uniform expansion for every \(d>0\). The asymptotically dominating trajectories are old enough for the harmonic thermal variance to saturate and keep the propulsion nearly aligned with the chosen observation direction during its significant recent memory window. Their probability penalty is sublinear on the \(x\) scale.

**3. Frozen-heading boundary.** If \(d=0\), \(\theta_s=0\), and \(A_\phi(t)=c_\phi(1-e^{-\beta t})\), where \(c_\phi=(v/\beta)\cos\phi\), possibly negative. For \(q>0\), integrating the conditional Gaussian moment generating function over the exponential age and changing variables \(y=qe^{-\beta t}\) gives the *exact* formula

\[
\mathbb E[e^{qX_\phi}]
=\frac r\beta e^{Dq^2/(2\beta)+c_\phi q}q^{-r/\beta}
\int_0^q y^{r/\beta-1}
\exp\!\left(-\frac{D}{2\beta}y^2-c_\phi y\right)\,\mathrm dy.
\]

The integral converges to a finite, strictly positive constant as \(q\to\infty\), uniformly over \(|c_\phi|\le c\). Hence

\[
\log\mathbb E[e^{qX_\phi}]
=\frac{Dq^2}{2\beta}+c_\phi q-\frac r\beta\log q+O(1).
\]

Chernoff's inequality with \(q=\beta(x-c_\phi)/D\) gives the required upper bound, with an \(O(\log x)\) correction. For the lower bound, restrict \(T\) again to \([t_x,t_x+1]\); its probability is polynomially small in \(x\), while its conditional mean differs from \(c_\phi\) by \(O(x^{-3})\) and its thermal variance differs from \(\sigma^2\) by \(O(x^{-6})\). Gaussian Mills estimates give the matching lower bound. Both bounds are uniform in \(\phi\), proving the frozen-heading expansion.

**4. Non-Gaussianity at the fourth-kurtosis zero set.** For \(d>0\), reflection symmetry implies \(\mathbb E[Y]=0\), with \(Y=(0,1)\cdot R\). The proven transverse upper-tail expansion has coefficients \(-\beta x^2/(2D)+(v/D)x+O(1)+o(x)\). A nondegenerate centered Gaussian has no linear term in its logarithmic right-tail expansion. Its quadratic coefficient would also force variance \(D/\beta\), so the positive linear coefficient is a contradiction. Thus \(Y\), and hence the joint stationary position, is never exactly Gaussian. A vanishing radial kurtosis can therefore identify a fourth-moment crossover but cannot certify a Gaussian law. This does not contradict the source's explicitly defined kurtosis-based regimes.

## Verification
The standalone `checker.py` re-evaluates the conditional Gaussian variance and the exact frozen-heading moment generating function by independent quadrature; checks the logarithmic moment-generating-function correction at three angles and multiple tilt parameters; evaluates both mean identities, including the active angular-renewal mean; and tests the analytic inequalities entering the lower-bound construction on parameter grids. The verification is diagnostic and finite; the proof above is responsible for the limits and all-parameter assertions. Run from the directory containing this file and `checker.py` with `python checker.py` (Python standard library only).

## Relationship to prior work
Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap* (arXiv:2409.06920, first posted September 11, 2024), defines this complete-reset model, obtains finite-order moment and radial-kurtosis formulas, and describes its zero-kurtosis surface. It does not establish the angularly uniform far-tail expansion or the singular distinction between \(d>0\) and \(d=0\). Chaudhuri and Dhar (arXiv:2005.14234) treat moment and kurtosis behavior in a harmonic trap without resetting; their model is not the regenerative full-reset stationary mixture. Kumar, Sadekar and Basu (arXiv:2008.03294) analyze marginal stationary tails under complete resetting *without* harmonic confinement; their exponential or compressed-exponential laws are for a different regime and do not cover the Gaussian-plus-linear tail here. The new limit is consistent with known Gaussian-convolution bounds but adds a matching angular small-ball lower bound and a discontinuous zero-rotation comparison.

## Limitations
This result is a fixed-parameter, large-position expansion for \(D,\beta,v,r>0\); it is not uniform as \(d\downarrow0\), nor does it determine the lower-order \(o(x)\) term, probability-density prefactors, higher-dimensional analogues, or the \(D=0\) compact-support boundary. As always, the absence of a located covering result is not proof of publication priority; a general theorem about bounded active drift and Gaussian variance mixtures could subsume the statement. The result makes no claim of independent verification.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920 (first public version 2024-09-11), https://arxiv.org/abs/2409.06920.
2. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234 (2020), https://arxiv.org/abs/2005.14234.
3. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020), https://arxiv.org/html/2008.03294v1.
4. A. N. Borodin and P. Salminen, *Handbook of Brownian Motion: Facts and Formulae*, 2nd ed. (2002), standard Brownian interval-survival bounds and Gaussian tail estimates.
