# Sharp invasion threshold for resident-profile dispersal

## Finding

Let a resident population occupy a spatially heterogeneous, connected habitat and let an invader choose a dispersal target proportional to the resident's positive stationary density. If the resident's target distribution is not proportional to the carrying landscape, the invader has a **strictly positive linear invasion exponent even when the two species have identical carrying landscapes**. More strongly, there is a unique, strictly subunit scalar carrying-capacity multiplier that exactly separates invasion from linear non-invasion.

Writing \(u_*\) for the resident density, \(Q=u_*/\int_\Omega u_*\), and \(m\) for the after-harvesting carrying landscape, the exact threshold is
\[
\boxed{\kappa_* = \min_{0\ne z\in H^1(\Omega)}\frac{\int_\Omega a_2|\nabla z|^2\,dx+\int_\Omega Qu_*z^2\,dx}{\int_\Omega Qmz^2\,dx}\in(0,1).}
\]
For every \(\kappa\ge0\), the invader's principal linearized growth rate is positive, zero, or negative according as \(\kappa\) is greater than, equal to, or less than \(\kappa_*\). In particular, equal capacities \(\kappa=1\) always permit linear invasion, confirming part (a), but not part (b), of Open Problem 1 in Braverman–Lawson.

## Assumptions and scope

Let \(\Omega\subset\mathbb R^d\) be bounded, connected, and have \(C^{2+\alpha}\) boundary for \(0<\alpha<1\). Assume \(P>0\) is \(C^{2+\alpha}\), \(a_1,a_2>0\) are \(C^{1+\alpha}\), and \(m>0\) is \(C^\alpha\) on the closed domain. All strictly positive functions are bounded away from zero. Let \(u_*>0\) be a classical stationary solution of
\[
\nabla\cdot\bigl(a_1\nabla(u_*/P)\bigr)+u_*(m-u_*)=0,
\qquad \partial_n(u_*/P)=0.
\]
Require that \(P\) and \(m\) are not proportional. This implies \(u_*\not\equiv m\): otherwise the resident equation would make \(u_*/P\) constant by the Neumann energy identity, hence \(m\) proportional to \(P\).

Normalize the invading species' directed-dispersal strategy to \(Q=u_*/M\), where \(M=\int_\Omega u_*\,dx\). Its after-harvesting carrying capacity is \(m_2=\kappa m\), and its linearization at the resident-only state is
\[
\mathcal L_\kappa v=\nabla\cdot\bigl(a_2\nabla(v/Q)\bigr)+(\kappa m-u_*)v,
\qquad \partial_n(v/Q)=0.
\]
The coefficient \(a_2\) can differ arbitrarily from \(a_1\) and is strictly positive. All stability claims refer **only to invasion by a rare species near the resident-only equilibrium**, not nonlinear global extinction or exclusion.

## Proof

**1. Symmetric variational reduction.** Substitute \(v=Qz\). The self-adjoint weighted Neumann eigenproblem is
\[
\nabla\cdot(a_2\nabla z)+Q(\kappa m-u_*)z=\lambda Qz.
\]
Its principal real eigenvalue is simple and admits the Rayleigh characterization
\[
\lambda(\kappa)=\sup_{z\in H^1(\Omega)\setminus\{0\}}
\frac{-\int_\Omega a_2|\nabla z|^2+\int_\Omega Q(\kappa m-u_*)z^2}{\int_\Omega Qz^2}.
\]
Uniform ellipticity, compact Sobolev embedding and strictly positive continuous \(Q\) give the principal eigenfunction and variational extrema. Moreover, for \(h>0\),
\[
h\min_\Omega m\le \lambda(\kappa+h)-\lambda(\kappa)\le h\max_\Omega m.
\]
Thus the principal eigenvalue is continuous and strictly increasing in \(\kappa\).

**2. Strictly subunit zero crossing.** Integrate the resident stationary equation and use its zero Neumann flux to get
\[
\int_\Omega u_*(m-u_*)\,dx=0,
\quad\text{hence}\quad \int_\Omega Q(m-u_*)\,dx=0.
\]
Set the generalized Rayleigh quotient \(F(z)=N(z)/D(z)\), where
\[
N(z)=\int_\Omega a_2|\nabla z|^2+\int_\Omega Qu_*z^2,
\quad D(z)=\int_\Omega Qmz^2>0.
\]
At the admissible constant function \(z=1\), \(F(1)=1\). Since \(u_*\not\equiv m\), the continuous function \(Q(u_*-m)\) is nonzero. Select a smooth \(h\) with \(\int_\Omega Q(u_*-m)h\,dx<0\). The directional derivative of \(F\) at \(z=1\) is
\[
\left.\frac{d}{dt}F(1+th)\right|_{t=0}
=\frac{2\int_\Omega Q(u_*-m)h\,dx}{\int_\Omega Qm\,dx}<0.
\]
Consequently \(F(1+th)<1\) for small positive \(t\), proving \(\kappa_*<1\). Also \(N(z)\ge (\min u_*)\int Qz^2\) and \(D(z)\le (\max m)\int Qz^2\), hence \(\kappa_*\ge\min u_*/\max m>0\). Coercivity produces a minimizer of \(F\), and its Euler–Lagrange equation gives a positive principal eigenfunction at \(\lambda(\kappa_*)=0\). Strict monotonicity then gives the claimed sign classification for all \(\kappa\ge0\), including \(\lambda(1)>0\).

**3. Explicit strict invasion with a five-percent carrying disadvantage.** On \(\Omega=(0,1)\), take \(P=1\), \(a_1=1/10\), \(a_2=1/100\), and write \(c(x)=\cos(\pi x)\). Define
\[
 u_*(x)=1+\tfrac15c(x),\qquad m(x)=u_*(x)+\frac{\pi^2c(x)}{50u_*(x)},\qquad Q(x)=u_*(x).
\]
These are smooth, \(m>0\), \(\int_0^1Q=1\), and direct substitution proves the Neumann resident equation. At \(\kappa=19/20\), use \(z=1+c\). Elementary cosine moments yield
\[
\int_0^1Qz^2\,dx=\frac{17}{10},
\quad\int_0^1Qmz^2\,dx=\frac{387}{200}+\frac{\pi^2}{50},
\]
\[
-\int_0^1a_2|z'|^2\,dx+\int_0^1Q(\tfrac{19}{20}m-u_*)z^2\,dx=\frac{56\pi^2-387}{4000}>0.
\]
Therefore the principal eigenvalue obeys the explicit certified bound
\[
\boxed{\lambda(19/20)\ge\frac{56\pi^2-387}{6800}>0.}
\]
The strict sign follows already from \(\pi>3\); no numerical integration is required.

## Verification

The proof is analytic. Its crucial strict inequality arises from the first variation at the constant trial function, rather than interpreting a nonnegative Rayleigh lower bound as strictly positive. The explicit example was independently checked by evaluating exact cosine moments and by the accompanying \(\texttt{verification_checker.py}\) using composite Simpson quadrature and a separate two-site rational consistency test. Those checks confirm algebra and do not replace the PDE argument.

## Relationship to prior work

Braverman and Lawson (2025), Theorem 3.4 and its Appendix A, give an invasion result under a strict carrying-capacity advantage; their Section 5 explicitly asks in Open Problem 1(a) whether such an advantage can be removed. Their variational formula supplies the starting point, but their displayed constant-function estimate becomes only \(\lambda\ge0\) at equal capacities and does not prove the required strict sign. The first-variation argument above gives the missing strict step, while the generalized quotient identifies the full sharp carrying-multiplier frontier.

Braverman and Kamrujjaman (2016) study directed-dispersal competition, with results for ideal-free carrying-aligned strategies and common chosen strategies. Cantrell, Cosner and Lou (2010) investigate ideal-free advection–diffusion strategies. Neither inspected setting states the present resident-equilibrium-matching sharp multiplier threshold; existing general variational principles are acknowledged rather than claimed as new.

## Limitations

The invasion threshold is local and linear. In particular, proof of invasion at equal capacities **does not** prove global exclusion of the resident (Open Problem 1(b)), existence/uniqueness of a nonlinear coexistence state, or persistence under stochastic effects. All conclusions require positive regular coefficients, a connected bounded smooth habitat, and the invader's exact resident-profile strategy. The value \(\kappa_*\) is an exact variational invariant, not generally a closed-form elementary number. Further historical-priority review, including potentially inaccessible related full texts, remains appropriate; no independent audit has been performed.

## References

1. E. Braverman and J. Lawson, *Trimming to coexistence: how dispersal strategies should be accounted for in resource management*, Journal of Mathematical Biology 92, 8, online 6 December 2025; https://doi.org/10.1007/s00285-025-02324-8 . Accessible preprint: https://arxiv.org/abs/2512.10898 (11 December 2025).
2. E. Braverman and Md. Kamrujjaman, *Lotka systems with directed dispersal dynamics: Competition and influence of diffusion strategies*, Mathematical Biosciences 279 (2016), 1–12; https://doi.org/10.1016/j.mbs.2016.06.007 .
3. E. Braverman and Md. Kamrujjaman, *Competitive-cooperative models with various diffusion strategies*, Computers & Mathematics with Applications 72 (2016), 653–662; https://arxiv.org/abs/1606.02779 .
4. R. S. Cantrell, C. Cosner and Y. Lou, *Evolution of dispersal and the ideal free distribution*, Mathematical Biosciences and Engineering 7 (2010), 17–36; https://doi.org/10.3934/mbe.2010.7.17 .
