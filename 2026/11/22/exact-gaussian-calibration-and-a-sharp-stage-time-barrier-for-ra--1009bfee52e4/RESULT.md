# Exact Gaussian calibration and a sharp stage-time barrier for randomized midpoint Langevin sampling

## Finding

Consider the overdamped Langevin equation with symmetric positive-definite precision matrix \(A\),
\[
  dX_t=-AX_t\,dt+\sqrt{2}\,dW_t,
  \qquad \pi=\mathcal N(0,A^{-1}).
\]
At each numerical step of length \(h>0\), choose a stage fraction \(U\in[0,1]\), independently of the current state and Brownian path, and apply the shared-increment predictor/corrector
\[
  Y=X-hUA X+\sqrt2\,W_{Uh},\qquad
  X'=X-hAY+\sqrt2\,W_h.
\]
Here \(W\) is a fresh \(d\)-dimensional standard Brownian motion during each step, and the same random \(U\)-law is used independently at subsequent steps. This is the variable-stage family of the explicit randomized-midpoint Langevin rule; the customary uniform stage law is one member.

**Sharp classification.** There is a unique finite-variance stationary distribution with covariance exactly \(A^{-1}\) if and only if \(A=\lambda I\), \(0<h\lambda<1\), and the stage law satisfies
\[
  \mathbb E[1-2U+(h\lambda)^2U^2]=0.
\]
For isotropic \(A\) and \(0<t=h\lambda<1\), all such laws are automatically contracting. Among them the **only** stage law preserving the full Gaussian target \(\pi\) is the deterministic choice
\[
 U=\alpha_t:=\frac1{1+\sqrt{1-t^2}}\quad\hbox{almost surely}.
\]
For every nonconstant covariance-calibrated stage law the stationary marginal is non-Gaussian: writing \(R_t(u)=1-t+t^2u\), its fourth cumulant (in each scalar coordinate) is strictly positive and equals
\[
 \operatorname{cum}_4(X_i)=
 \frac{3h^4\lambda^2\operatorname{Var}(1-2U+t^2U^2)}
 {1-\mathbb E R_t(U)^4}>0.
\]
Among all exactly Gaussian-calibrated members of this family, the unique fastest contraction per numerical step occurs at
\[
 h\lambda=\frac1{\sqrt2},\qquad
 \inf |R_t(\alpha_t)|=2-\sqrt2.
\]
At the excluded boundary \(t=1\), \(U=1\) produces the identity chain: it preserves every input distribution but has **no unique stationary distribution**. For \(t>1\), even exact stationary target variance is impossible for every stage law on \([0,1]\). For nonisotropic \(A\), exact target covariance is impossible for every common stage law and every positive step size, whether the numerical chain is stable or not.

## Assumptions and scope

The dimension \(d\) is any positive integer; \(A\) is a fixed real symmetric positive-definite matrix, \(h>0\), and \(U\) is an arbitrary Borel probability law on \([0,1]\), independent of all current and past states and of each step's fresh Brownian motion. The law is *shared across eigendirections within a step* and independently resampled between steps. The stage noise \(W_{Uh}\) and final noise \(W_h\) are Brownian increments on the same step, **not independent noise draws**. The fixed-time target is the exact equilibrium of the stated OU diffusion. No centring hypothesis is imposed on a candidate stationary distribution. Preserving a single law does not constitute uniqueness of stationarity.

Define \(m_1=\mathbb E U\) and \(m_2=\mathbb E U^2\). All results are exact finite-step statements, not asymptotic order conditions. The optimal contraction refers to the exact Gaussian-preserving deterministic subfamily and to convergence measured per numerical step, not per unit simulated physical time, gradient-evaluation cost, or general nonlinear-target error.

## Proof

**1. Conditional affine step and covariance defect.** Eliminating the predictor gives
\[
 X'=P(U)X+\xi_U,\quad
 P(u)=I-hA+uh^2A^2,\quad
 \xi_U=\sqrt2(W_h-hAW_{uh}).
\]
By \(\operatorname{Cov}(W_h,W_{uh}\mid U=u)=uhI\),
\[
 Q(u):=\operatorname{Cov}(\xi_U\mid U=u)
 =2h(I-2uhA+uh^2A^2).
\]
If the current covariance is \(A^{-1}\) and the mean is \(\mu\), the law of total covariance gives
\[
  \operatorname{Cov}(X')-A^{-1}
  =h^2 A\left[(1-2m_1)I+h^2m_2A^2\right]
    +\operatorname{Cov}(P(U)\mu).\tag{1}
\]
Indeed, conditional on \(U=u\) the covariance is \(P(u)A^{-1}P(u)+Q(u)\) and the mean is \(P(u)\mu\). Expanding the conditional covariance cancels its terms of orders \(h\) and \(h^3\); the remaining terms give the first summand in (1). The second summand is positive semidefinite and may be nonzero for an uncentred input.

**2. Necessity, sharp scalar threshold, and existence.** Write \(t_j=h\lambda_j\) in an orthonormal eigenbasis. The first term of (1) on eigenmode \(j\) is \(h^2\lambda_j\mathbb E q_{t_j}(U)\), with
\[
  q_t(u)=1-2u+t^2u^2=(1-u)^2+(t^2-1)u^2.
\]
If any \(t_j>1\), that mode has strictly positive covariance defect even before the nonnegative mean contribution is added, ruling out stationary target covariance. If any \(t_j=1\), stationarity of its target variance forces \(\mathbb E(1-U)^2=0\), so \(U=1\) almost surely. Now the mean contribution vanishes, and (1) forces \(q_{t_i}(1)=t_i^2-1=0\) for every mode \(i\). Thus all \(t_i=1\), where \(P=I\), \(Q=0\), and the chain is the identity with no unique stationary distribution.

It remains to consider \(0<t_j<1\) for every \(j\). Then \(0<1-t_j\le R_{t_j}(U)\le1-t_j+t_j^2<1\). A stationary finite mean satisfies \(\mu=\mathbb E[P(U)]\mu\) and is therefore zero. Now (1) requires
\[
  1-2m_1+(h\lambda_j)^2m_2=0\quad\text{for every }j.\tag{2}
\]
If two eigenvalues differ, subtracting their equations forces \(m_2=0\), hence \(U=0\) almost surely and \(m_1=0\), contradicting (2). Therefore \(A=\lambda I\), and with \(t=h\lambda\) the condition is \(\mathbb E q_t(U)=0\). For \(0<t<1\), the polynomial decreases strictly on \([0,1]\) and has a unique root
\[
 \alpha_t=(1-\sqrt{1-t^2})/t^2
 =1/(1+\sqrt{1-t^2})\in(1/2,1).
\]
Both the deterministic law at this root and nonconstant laws are feasible; for example \(\Pr(U=1)=1/(2-t^2)\), \(\Pr(U=0)=1-1/(2-t^2)\), gives zero expected \(q_t\).

For \(0<t<1\), each scalar multiplier obeys
\[
 0<1-t\le R_t(u)\le1-t+t^2<1.
\]
The random affine chain is thus uniformly contractive, and its series of past innovations converges in all finite moments because the Gaussian innovations have uniformly bounded moments. It has a unique stationary distribution and zero mean; the scalar variance recursion is
\[
 V_{k+1}=\mathbb E R_t(U)^2\,V_k
       +\mathbb E[2h(1-2tU+t^2U)].
\]
The difference between the right-hand side evaluated at \(V=\lambda^{-1}\) and \(\lambda^{-1}\) is \(h^2\lambda\,\mathbb E q_t(U)\). Therefore precisely the displayed stage laws give stationary variance \(\lambda^{-1}\). For the centred stationary law the off-diagonal covariances are multiplied by \(\mathbb E R_t(U)^2<1\) in each step, since the conditional innovation covariance is a scalar multiple of \(I\); hence those covariances vanish. Higher-order cross-coordinate dependence from shared \(U\) is still possible.

**3. The complete Gaussianity obstruction and fourth cumulant.** Fix one coordinate and let \(v=\lambda^{-1}\), \(r=R_t(U)\) and \(s=2h(1-2tU+t^2U)\). If \(X\sim\mathcal N(0,v)\), then conditional on \(U\), the next iterate is \(\mathcal N(0,r^2v+s)\). Its unconditional variance equals \(v\) for a calibrated law. Its fourth moment equals \(3\mathbb E(r^2v+s)^2\), exceeding \(3v^2\) unless \(r^2v+s=v\) almost surely. The difference equals \(h^2\lambda q_t(U)\), and \(q_t\) is strictly decreasing for \(0<t<1\); hence target Gaussian invariance requires and is achieved by the single deterministic stage \(U=\alpha_t\).

More generally, in the stationary law all fourth moments are finite and satisfy
\[
 M_4=\mathbb E[r^4]M_4+6v\,\mathbb E[r^2s]+3\mathbb E[s^2].
\]
Subtract the Gaussian fourth moment \(3v^2\), using \(\mathbb E(r^2v+s)=v\), to obtain
\[
 (1-\mathbb E r^4)(M_4-3v^2)
 =3\operatorname{Var}(r^2v+s)
 =3h^4\lambda^2\operatorname{Var}(q_t(U)),
\]
proving the cumulant formula and its strict positivity for every nonconstant calibrated law.

**4. Fastest exactly calibrated Gaussian contraction.** For deterministic \(U=\alpha_t\), the update is an ordinary Gaussian autoregression with multiplier
\[
 a(t)=1-t+t^2\alpha_t=2-t-\sqrt{1-t^2}\in(0,1).
\]
The exact one-step \(W_2\) contraction between point-start transition laws is \(a(t)\); equality follows from their identical Gaussian innovations and different means. Since
\[
 a'(t)=-1+\frac{t}{\sqrt{1-t^2}},
\]
its unique minimum on \((0,1)\) is at \(t=1/\sqrt2\), with \(a=2-\sqrt2\). This is also the sharp asymptotic mean-displacement contraction factor. The endpoint limits of \(a(t)\) both equal one.

## Verification

Run `python verify.py` from the extracted package root; no third-party packages are needed. It verifies exact covariance-balance and fourth-moment identities using rational arithmetic on numerous stage laws, independent recurrence calculations, the exact non-Gaussian benchmark \(t=3/5\) with stages \(0,1\), a two-eigenvalue covariance obstruction, and a numerical supplement for the unique mixing optimum. Expected output is saved in `checks.txt`.

At \(\lambda=1\), \(t=3/5\), the deterministic calibrated stage is \(\alpha_t=5/9\), and the Gaussian autoregression has multiplier \(3/5\). The alternative two-point law \(\Pr(U=1)=25/41\), \(\Pr(U=0)=16/41\) has exactly the same stationary variance one, but strictly positive fourth cumulant \(3321/10498\). This rational example independently tests the covariance-versus-law distinction. Exhaustive rational tests and numerical grid sweeps are supplementary, not substitutes for the parameter-uniform proof above.

## Relationship to prior work

He, Balasubramanian and Erdogdu, particularly Section 2 of arXiv:2011.03176v2, study uniform-stage randomized midpoint overdamped Langevin sampling and general stationary bias / convergence. Their two normalized Gaussian noise vectors have conditional cross-covariance \(\sqrt{U}I\), as in the shared-increment update here. The present proof changes the stage law and establishes an *exact finite-step Gaussian covariance/law classification*, a sharp stage threshold, and a unique calibrated mixing optimum not implied by their uniform-stage bias bounds.

Shen and Lee (2019) develop a randomized midpoint framework for **underdamped** Langevin dynamics rather than the present overdamped Gaussian-stage classification. Laurent and Vilmart (2017) provide general long-time invariant-measure order analysis for stochastic Runge–Kutta methods, but finite-order conditions alone do not give the specific all-step quadratic spectral obstruction or positive fourth-cumulant identity.

Related published exact Gaussian sampling analyses of random-order drift/diffusion splitting and of one-gradient **underdamped** schemes show analogous covariance-versus-law distinctions for different update maps. Their different amplifiers and noise covariances do not imply equations (1)–(2) or the calibrated parameter \(\alpha_t\) for this overdamped predictor/corrector. The principal comparator papers were inspected by their stated update, theorem, proof, and limitation material; historical equivalence outside the inspected sources remains possible.

## Limitations

This is a Gaussian-target theorem for a specific explicit predictor/corrector with a *shared* Brownian increment and i.i.d. scalar stage law. It does not say that its deterministic tuned member is unbiased or optimal for general nonlinear potentials, and the uniform-stage method has different stochastic quadrature motivations. For nonisotropic targets, the no-go assumes one common stage time for all eigenmodes; eigenvalue-specific stages or modified noise covariances are outside scope. Variance calibration is not equivalent to matching the full stationary law; in particular calibrated random stages are non-Gaussian. The mixing optimum is measured per step, not per unit physical time or computational cost, and is not a comparison with implicit samplers. No assertion of exhaustive publication priority is made.

## References

1. Y. He, K. Balasubramanian, and M. A. Erdogdu, *On the Ergodicity, Bias and Asymptotic Normality of Randomized Midpoint Sampling Method*, arXiv:2011.03176 (first posted 2020-11-06), especially Section 2 of v2. https://arxiv.org/abs/2011.03176v2
2. R. Shen and Y. T. Lee, *The Randomized Midpoint Method for Log-Concave Sampling*, arXiv:1909.05503v1 (first posted 2019-09-12). https://arxiv.org/abs/1909.05503
3. A. Laurent and G. Vilmart, *Exotic aromatic B-series for the study of long time integrators for a class of ergodic SDEs*, arXiv:1707.02877v1 (first posted 2017-07-10), Math. Comp. 89 (2020). https://arxiv.org/abs/1707.02877
4. *Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC*, research record 160d754f339b (2026-09-19).
5. *Spectral minimax calibration and unavoidable fourth-order dependence in random-order Langevin splitting*, research record ba2056df054f (2026-11-08).
