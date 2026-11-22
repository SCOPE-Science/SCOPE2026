# A joint fast-alarm law for reset counts and search exposure with visible stochastic returns

## Finding

Consider a Brownian target search interrupted by rapid Poisson alarms, with a noisy return to home that can itself discover the target. As the alarm rate \(r\) tends to infinity, the number of alarms diverges as \(\sqrt r\), the accumulated free-search duration vanishes as \(r^{-1/2}\), and the physical completion time stays nondegenerate. Their *joint* limit is

\[
\left(T_r,\frac{N_r}{\sqrt r},\sqrt r\,S_r\right)\Longrightarrow (T,Z,Z).
\]

For fixed \(D,L,\kappa>0\), set \(\phi(x)=\kappa x^2/(2D)\), \(H(x)=\int_0^x e^{\phi(y)}\,dy\). For every \(s\ge0\), let \(A_s\), \(B_s\) be the unique solutions on \([0,L]\) of

\[
Df''(x)-\kappa xf'(x)=sf(x),\quad
A_s(0)=1,\ A_s'(0)=0,\quad B_s(0)=0,\ B_s'(0)=1.
\]

Define

\[
m_s=\sqrt{\frac{2\kappa}{D}}\,
\frac{\Gamma\big((1+s/\kappa)/2\big)}{\Gamma\big(s/(2\kappa)\big)},\quad s>0,
\qquad m_0=0.
\]

Then the limiting Laplace transform is explicitly

\[
\boxed{\mathbb E e^{-sT-qZ}=\frac{1}{A_s(L)+\big(m_s+2q/\sqrt D\big)B_s(L)}}
\qquad (s,q\ge0).
\]

Here \(T\) has the ordinary first-passage-time law of the unreset Ornstein--Uhlenbeck diffusion \(dX_t=-\kappa X_tdt+\sqrt{2D}\,dW_t\) from zero to \(L\), whereas \(Z\) has an exponential marginal with mean \(2H(L)/\sqrt D\). They are not independent. Indeed their covariance is finite and strictly positive:

\[
\boxed{\operatorname{Cov}(T,Z)=\frac2{\sqrt D}\left[
\frac1D\int_0^L e^{\phi(x)}\int_0^x e^{-\phi(y)}\big(H(L)-H(y)\big)\,dy\,dx
+\sqrt{\frac{\pi}{2\kappa D}}\,H(L)^2\right]>0.}
\]

Moreover, writing \(p_r\) for the chance that one search-plus-possible-return cycle finds the target,

\[
p_r\sim\frac{\sqrt D}{2H(L)\sqrt r},\qquad
\sqrt r\,\mathbb ES_r\longrightarrow\frac{2H(L)}{\sqrt D},
\qquad \Pr(\text{discovery during return})\longrightarrow1.
\]

Thus an unbounded count of alarms and a vanishing total exposure to the search phase coexist with an order-one completion time, with a nontrivial positive time–count dependence.

## Assumptions and scope

The position starts at home \(0\). In each search phase it is an independent one-dimensional Brownian diffusion with generator \(D\partial_{xx}\), killed upon hitting \(L>0\). A fresh independent exponential alarm of rate \(r>0\) interrupts a search that has not hit the target. At that instant the position is retained, and the phase switches to an Ornstein--Uhlenbeck diffusion of the same diffusivity, with generator \(D\partial_{xx}-\kappa x\partial_x\), where \(\kappa>0\) is fixed as \(r\to\infty\). On a return starting at \(x<0\), the first hit of zero triggers a fresh search; on a return starting at \(0<x<L\), the first hit of either 0 or \(L\) triggers a new search or absorption, respectively. No alarms occur during returns, and absorption at \(L\) is active in both phases. The total physical duration, number of search-to-return switches, and total search-phase duration are denoted by \(T_r,N_r,S_r\). All statements concern \(r\to\infty\) at fixed \(D,L,\kappa\). The claim is a distributional limit; the covariance displayed is for the limiting pair \((T,Z)\).

## Proof

**1. Killed search resolvent.** Let \(\theta>0\), \(x<L\), and write \(k_\theta=\sqrt{\theta/D}\). The Brownian resolvent before hitting \(L\), started at 0, is

\[
G_\theta(x)=\int_0^\infty e^{-\theta t}\Pr_0\{X_t\in dx,\ t<\tau_L\}/dx\,dt
=\frac{e^{-k_\theta|x|}-e^{-k_\theta(2L-x)}}{2Dk_\theta}.
\]

The discounted probability of reaching \(L\) before an alarm is \(d_\theta=e^{-Lk_\theta}\). For \(s\ge0\), let \(u_s(x)\) be the discounted probability that a return started at \(x\) finishes at target \(L\) (rather than home), and \(v_s(x)\) the analogous discounted probability of returning home (rather than hitting target). For \(x\le0\), \(u_s(x)=0\) and \(v_s(x)=\mathbb E_x e^{-s\tau_0}\), whereas for \(0<x<L\) the two functions solve the OU boundary equation with \((u_s(0),u_s(L))=(0,1)\) and \((v_s(0),v_s(L))=(1,0)\). Consequently,

\[
u_s'(0+)=\frac1{B_s(L)},\qquad
v_s'(0+)=-\frac{A_s(L)}{B_s(L)},\qquad
v_s'(0-)=m_s.
\]

The negative-side formula follows from the solution decaying at negative infinity \(e^{\kappa x^2/(4D)}D_{-s/\kappa}(-\sqrt{\kappa/D}\,x)\) of the OU equation, normalized to 1 at zero; the standard parabolic-cylinder values at zero yield the stated gamma quotient. At \(s=0\), return hits home almost surely from the negative half-line, so \(m_0=0\). These functions are differentiable one-sided at the origin, bounded between 0 and 1, and their derivatives have the displayed signs.

**2. Marked renewal transform.** Every failed return to home creates a fresh statistically independent cycle. Put

\[
a_r(s)=r\int_{-\infty}^L G_{r+s}(x)u_s(x)\,dx,\qquad
b_r(s)=r\int_{-\infty}^L G_{r+s}(x)v_s(x)\,dx.
\]

A cycle ends either by direct search success, by alarm followed by target success, or by alarm followed by a home return. Marking every alarm by \(e^{-q/\sqrt r}\) gives the *exact* transform for all \(s,q\ge0\):

\[
\mathbb E e^{-sT_r-qN_r/\sqrt r}
=\frac{d_{r+s}+e^{-q/\sqrt r}a_r(s)}{1-e^{-q/\sqrt r}b_r(s)}.
\]

If, instead, one marks the total search-phase duration by \(e^{-q\sqrt r S_r}\), exactly the same renewal expression holds with the search resolvent parameter \(r+s\) replaced throughout by \(r+s+q\sqrt r\), and no explicit alarm mark. The return-phase transforms \(u_s,v_s\) remain unchanged.

**3. Boundary layer and the limiting transform.** For each fixed \(s\ge0\), the resolvent concentrates on \(|x|=O(r^{-1/2})\). Expanding \(u_s(x)=u_s'(0+)x+O(x^2)\) for positive \(x\) and \(v_s(x)=1+v_s'(0\pm)x+O(x^2)\) on either side, and integrating the exponential first moments, yields

\[
\sqrt r\,a_r(s)\longrightarrow\frac{\sqrt D}{2}u_s'(0+),\qquad
\sqrt r\,[1-b_r(s)]\longrightarrow
\frac{\sqrt D}{2}\big(v_s'(0-)-v_s'(0+)\big).
\]

The image term and direct success are exponentially small in \(\sqrt r\), while \(s/r=o(r^{-1/2})\). The bounds on \(u_s,v_s\) justify dominated remainder estimates after the rescaling \(x=y/\sqrt r\). A factor \(e^{-q/\sqrt r}\) contributes \(q/\sqrt r\) to the renewal denominator. The same leading term comes from increasing the search killing rate by \(q\sqrt r\). Therefore both marked transforms tend to

\[
\frac{u_s'(0+)}{v_s'(0-)-v_s'(0+)+2q/\sqrt D}
=\frac1{A_s(L)+(m_s+2q/\sqrt D)B_s(L)}.
\]

At \(s=q=0\) the limiting expression is 1, continuous in the nonnegative quadrant. Multivariate Laplace-transform continuity gives the joint weak limit \((T_r,N_r/\sqrt r)\Rightarrow(T,Z)\). Putting \(q=0\) and matching the derivative across zero identifies \(T\) as OU first passage to \(L\). Putting \(s=0\), one has \(A_0(L)=1\), \(B_0(L)=H(L)\), and \(m_0=0\), giving the exponential marginal of \(Z\).

**4. Joint convergence with search exposure.** Let \(M_r=N_r-rS_r\). Its counting-process compensator is zero-mean with predictable quadratic variation \(rS_r\), because alarms are active only during search. The one-cycle success probability is

\[
p_r=d_r+r\int G_r(x)u_0(x)\,dx
\sim\frac{\sqrt D}{2H(L)\sqrt r},
\]

as \(u_0'(0+)=1/H(L)\). The number of attempted cycles is geometric with parameter \(p_r\); the terminal direct-success probability is exponentially small, hence \(\mathbb EN_r=O(\sqrt r)\). Optional stopping after localization and monotone convergence give \(\mathbb E M_r^2=r\mathbb ES_r=\mathbb EN_r\). Thus

\[
\mathbb E\left(\frac{N_r}{\sqrt r}-\sqrt r\,S_r\right)^2
=\frac{\mathbb EN_r}{r}=O(r^{-1/2})\longrightarrow0.
\]

This proves the stated *three-variable* joint limit. Also \(\mathbb ES_r=\mathbb EN_r/r\), and the precise geometric-cycle calculation gives \(\mathbb EN_r\sim1/p_r\), establishing its sharp mean coefficient. A direct search-phase target hit before an alarm has probability \(e^{-L\sqrt{r/D}}\) per cycle, so its fraction among successful cycles tends to zero.

**5. Strictly positive limiting covariance.** Put \(F(s)=A_s(L)+m_sB_s(L)\) and \(C(s)=2B_s(L)/\sqrt D\). Then \(\mathbb E e^{-sT-qZ}=[F(s)+qC(s)]^{-1}\), with \(F(0)=1\). Differentiation at the origin yields

\[
\operatorname{Cov}(T,Z)=C(0)F'(0)-C'(0)
=\frac2{\sqrt D}\big(H(L)F'(0)-\partial_sB_s(L)|_{s=0}\big).
\]

The gamma quotient gives \(m'_0=\sqrt{\pi/(2\kappa D)}\). Differentiating the two initial-value OU equations in \(s\) and applying the integrating factor \(e^{-\phi}\) yields

\[
\partial_s A_s(L)|_{0}=\frac1D\int_0^L e^{\phi(x)}\int_0^x e^{-\phi(y)}dy\,dx,
\quad
\partial_s B_s(L)|_{0}=\frac1D\int_0^L e^{\phi(x)}\int_0^x e^{-\phi(y)}H(y)dy\,dx.
\]

Substitution gives the boxed covariance. Its first integral has strictly positive integrand on a set of positive measure because \(H(L)>H(y)\) for \(y<L\), and the second term is positive. Hence the two limiting observables are strictly positively correlated rather than independent.

## Verification

Run \(\texttt{python verify.py}\) with Python 3, NumPy and SciPy. The independent checker constructs finite-rate killed-Brownian resolvent integrals, solves the return boundary ODE, and compares alarm-marked and search-duration-marked transforms with their analytic limit at 15 parameter/rate combinations. It also checks nine success-probability asymptotics, five drift-free exact finite-rate probabilities, four elementary limiting-transform identities and four limiting-covariance derivatives. These finite computations test the formulas; the proof of the infinite-rate limit is the analytic boundary-layer and renewal calculation above.

For a drift-free return (the continuous boundary case \(\kappa=0\)), the cycle success probability is exactly \(p_r=(1-e^{-2L\sqrt{r/D}})/(2L\sqrt{r/D})\), and for \(s>0\) the joint limit simplifies to

\[
\mathbb E e^{-sT-qZ}=
\frac{e^{-L\sqrt{s/D}}}{1+q(1-e^{-2L\sqrt{s/D}})/\sqrt s}.
\]

Its continuous \(s=0\) value is \((1+2qL/\sqrt D)^{-1}\). At this boundary \(T\) has infinite mean, so the finite positive covariance assertion is restricted to \(\kappa>0\).

## Relationship to prior work

Dubey and Pal (2026) derive the exact mean first-passage time for switching potentials and compare stochastic returns with instantaneous resetting, including target-visible return trajectories. Frydel (2025) formulates the same return-visible cyclic search mechanism, gives geometric cycle statistics and the limiting mean identification with continuous harmonic search. Biswas, Kundu and Pal (2023) establish a general renewal framework, while Biswas and collaborators (2024) treat drift-diffusive stochastic-return search. These sources provide the starting renewal structure, splitting probabilities and, in applicable cases, the limiting *mean* of completion time; those are not claimed as new. The result here is the \(\sqrt r\) *joint distributional* limit for alarm counts and active-search exposure together with physical completion time, its closed marked Laplace transform, and strict positive limiting time–count covariance. Prior work on instantaneous resetting with local-time/count conjugacy uses a different return mechanism and does not directly establish this three-observable finite-return limit.

## Limitations

The main result assumes fixed \(\kappa,D,L>0\), free Brownian search, exponential alarms and active target detection during first-hit returns. It does not establish uniformity when \(\kappa\) changes with \(r\), nor finite-rate error constants, nor convergence of unbounded covariance moments from the finite-rate process. The \(\kappa=0\) boundary has an infinite mean completion time. The transform can be understood through classical diffusion local-time and excursion theory; no new abstract excursion theory is claimed. An unindexed equivalent analysis of this marked stochastic-return limit remains a possible priority risk, and some relevant published record full texts could not be inspected beyond their available abstracts.

## References

- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814, first public version 13 October 2026. https://arxiv.org/abs/2610.18814
- D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials*, arXiv:2511.14646, first public version 18 November 2025. https://arxiv.org/abs/2511.14646
- A. Biswas, A. Kundu and A. Pal, *Search with stochastic home-returns can expedite classical first passage under resetting*, arXiv:2307.16294, first public version 30 July 2023. https://arxiv.org/abs/2307.16294
- A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: speed-up beyond optimal instantaneous return*, arXiv:2406.08975, first public version 13 June 2024. https://arxiv.org/abs/2406.08975
