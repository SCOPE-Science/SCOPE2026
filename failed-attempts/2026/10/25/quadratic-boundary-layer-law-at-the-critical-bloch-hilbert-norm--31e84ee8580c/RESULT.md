# Quadratic boundary-layer law at the critical Bloch–Hilbert norm transition

## Finding

Let \(\mathcal H\) be the Hilbert matrix operator on the analytic \(\alpha\)-Bloch space \(\mathcal B^\alpha\), with the standard norm \(|f(0)|+\sup_{|z|<1}(1-|z|^2)^\alpha |f'(z)|\). Set
\[
P_\alpha(t)=\int_0^t(1-s^2)^{-\alpha}\,ds,\qquad
C_\alpha=\int_0^1(1-t)(1-t^2)^{-\alpha}\,dt,
\]
\[
D_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{tP_\alpha(t)}{(1-rt)^2}\,dt\quad(0\le r<1),
\qquad D_\alpha(1)=\frac{\pi}{\sin(\pi(\alpha-1))}.
\]
The known exact norm representation for \(1<\alpha<2\) is \(\|\mathcal H\|=C_\alpha+\max_{0\le r\le1}D_\alpha(r)\). For \(\delta=\alpha-\tfrac32\downarrow0\), **every** maximizing radius \(r_\alpha\) satisfies
\[
\boxed{\displaystyle\lim_{\delta\downarrow0}\frac{1-r_{3/2+\delta}}{\delta^2}=\frac12},
\]
and the exact operator norm obeys
\[
\boxed{\displaystyle \lim_{\delta\downarrow0}
\frac{\|\mathcal H\|_{\mathcal B^{3/2+\delta}\to\mathcal B^{3/2+\delta}}
-C_{3/2+\delta}-\pi/\sin(\pi(\tfrac12+\delta))}{\delta^2}=\pi}.
\]
In particular the interior maximizers detach quadratically from the boundary, and the excess above the boundary norm formula has a sharp quadratic coefficient.

## Assumptions and scope

The unit disk and complex analytic functions are used, \(\tfrac32<\alpha<2\), and the limit is one-sided as \(\alpha\downarrow\tfrac32\). The operator acts by \((\mathcal Hf)(z)=\int_0^1 f(t)/(1-tz)\,dt\). Only the existence and norm representation of the maximizing radii are taken from [1], not the new scaling conclusions. The theorem concerns *all* choices of global maximizing radii, without assuming uniqueness for fixed \(\alpha\).

## Proof

**1. A uniform endpoint expansion.** Put \(\varepsilon=1-r\), and introduce
\[
Q_\alpha(t)=\frac{(1-t^2)^{1-\alpha}}{2(\alpha-1)},\quad
E_\alpha(t)=\int_t^1(1-s)(1-s^2)^{-\alpha}\,ds,
\]
\[
d_\alpha=C_\alpha-\frac1{2(\alpha-1)}
=\frac{\alpha-\tfrac32}{2(\alpha-1)}B\!\left(\frac12,2-\alpha\right).
\]
Direct differentiation and the limit at \(t=1\) give the exact decomposition \(P_\alpha=Q_\alpha+d_\alpha-E_\alpha\). Consequently
\[
D_\alpha(r)=\frac{M_\alpha(r)}{2(\alpha-1)}+d_\alpha J_\alpha(r)-R_\alpha(r),
\]
where
\[
M_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{t(1-t^2)^{1-\alpha}}{(1-rt)^2}\,dt,
\quad J_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{t}{(1-rt)^2}\,dt,
\]
\[
R_\alpha(r)=(1-r^2)^\alpha\int_0^1\frac{tE_\alpha(t)}{(1-rt)^2}\,dt.
\]
All the following asymptotics are **uniform** for \(\alpha\) in a sufficiently small fixed neighborhood of \(\tfrac32\), and \(\varepsilon\downarrow0\).

Under \(y=(1-t)/(1-rt)\),
\[
M_\alpha(r)=\int_0^1m_{\alpha,r}(y)\,dy,
\quad m_{\alpha,r}(y)=(1+r)^\alpha(1-y)y^{1-\alpha}
[2-(1+r)y]^{1-\alpha}(1-ry)^{2\alpha-3}.
\]
For \(\alpha\in[\tfrac32,\tfrac32+\eta]\) with \(0<\eta<\tfrac14\), differentiation gives
\[
\partial_r\log m_{\alpha,r}(y)
=\frac\alpha{1+r}+\frac{(\alpha-1)y}{2-(1+r)y}-\frac{(2\alpha-3)y}{1-ry}.
\]
For \(r\ge\tfrac12\), absolute values of \(\partial_rm_{\alpha,r}\) are dominated by a fixed multiple of \(y^{-1/2-\eta}(1-y)^{-1/2}\), which is integrable. Dominated convergence, uniform over the compact \(\alpha\)-interval, proves
\[
M_\alpha(1-\varepsilon)-M_\alpha(1)=-M'_\alpha(1)\varepsilon+o(\varepsilon),
\]
where evaluating the three beta integrals gives
\[
M'_\alpha(1)=\alpha B(2-\alpha,\alpha)+(5-3\alpha)B(3-\alpha,\alpha-1),
\qquad M'_{3/2}(1)=\pi.
\]
The exact elementary integral
\[
\int_0^1\frac{t}{(1-rt)^2}\,dt=\frac{r/(1-r)+\log(1-r)}{r^2}
\]
implies \(J_\alpha(1-\varepsilon)=2^\alpha\varepsilon^{\alpha-1}(1+O(\varepsilon|\log\varepsilon|))\) uniformly. Also,
\[
E_\alpha(1-u)=\frac{2^{-\alpha}}{2-\alpha}u^{2-\alpha}(1+O(u)),
\]
uniformly for \(u\downarrow0\). Substitute \(t=1-\varepsilon u\) in the definition of \(R_\alpha\). The bound \(E_\alpha(t)\le C(1-t)^{2-\alpha}\) and the integrable majorant \(u^{2-\alpha}/(1+u)^2\), uniformly in the compact parameter interval, justify dominated convergence. Therefore
\[
R_\alpha(1-\varepsilon)=\varepsilon\left(\frac{B(3-\alpha,\alpha-1)}{2-\alpha}+o(1)\right).
\]
The remainders are uniform: for \(R\), split the scaled integral at a fixed large \(u\), dominate its tail by integrable powers uniformly in \(\alpha\), then apply uniform convergence on the finite interval.

Since \(M_\alpha(1)/[2(\alpha-1)]=D_\alpha(1)\), the terms combine to
\[
D_\alpha(1-\varepsilon)-D_\alpha(1)
=2^\alpha d_\alpha\varepsilon^{\alpha-1}(1+O(\varepsilon|\log\varepsilon|))
-c_\alpha\varepsilon+o(\varepsilon),
\]
\[
c_\alpha=\frac{M'_\alpha(1)}{2(\alpha-1)}+
\frac{B(3-\alpha,\alpha-1)}{2-\alpha},\qquad c_{3/2}=2\pi.
\]
Here the displayed \(o(\varepsilon)\) is uniform in \(\alpha\); there is no hidden fixed-parameter limit in the joint scaling.

**2. The critical profile.** Since \(d_{3/2+\delta}=\pi\delta+O(\delta^2)\), setting \(\varepsilon=\delta^2 x\), for every compact interval \(0<a\le x\le b<\infty\), gives uniform convergence
\[
\frac{D_{3/2+\delta}(1-\delta^2x)-D_{3/2+\delta}(1)}{\delta^2}
\longrightarrow F(x)=2^{3/2}\pi\sqrt x-2\pi x.
\]
The sole maximizer of \(F\) on \([0,\infty)\) is \(x=\tfrac12\), and \(F(\tfrac12)=\pi\).

**3. Global localization, not merely a local ansatz.** At \(\alpha=\tfrac32\), the exact decomposition has \(d_\alpha=0\) and \(E_\alpha(t)>0\) for \(0\le t<1\); the strict transformed-integrand inequality \(m_{3/2,r}(y)<m_{3/2,1}(y)\) for \(r<1\) shows \(D_{3/2}(r)<D_{3/2}(1)=\pi\) for every \(r<1\). The representations above, together with dominated convergence uniformly in \(\alpha\), show joint continuity on \([\tfrac32,\tfrac32+\eta]\times[0,1]\). Thus any maximizer \(r_{3/2+\delta}\) tends to \(1\).

For sufficiently small \(\varepsilon\) the uniform expansion yields
\[
D_{3/2+\delta}(1-\varepsilon)-D_{3/2+\delta}(1)
\le C\delta\sqrt\varepsilon-c\varepsilon
\]
for fixed positive \(C,c\). The trial \(\varepsilon=\tfrac12\delta^2\) gives a gain \((\pi+o(1))\delta^2\). Every global maximizer therefore has \(\varepsilon=O(\delta^2)\), by the negative linear term, and \(\varepsilon/\delta^2\) bounded away from zero, by the upper bound \(C\delta\sqrt\varepsilon\). The compact-interval profile then forces every accumulation point of \(\varepsilon/\delta^2\) to maximize \(F\), hence to equal \(\tfrac12\). The maximum excess tends to \(\pi\delta^2\). Substituting the norm identity completes both claims. \(\square\)

## Verification

The independently evaluable identities are \(d'_\alpha|_{\alpha=3/2}=\pi\), \(M'_{3/2}(1)=\pi\), \(\lim_{\alpha\to3/2}R_\alpha(1-\varepsilon)/\varepsilon=\pi\) in the stated uniform joint boundary limit, and \(c_{3/2}=2\pi\). A supplied Python script checks the two beta formulas and numerical optimizing radii using direct integrals; finite numerical evaluations corroborate but do not replace the proof of the infinite-parameter limit. The test does not claim a machine-certified proof.

## Relationship to prior work

Cui–Lin–Lu–Ye [1] prove the exact fixed-parameter radial norm representation, the boundary formula and the fact that maximizers move into the interior for \(\alpha>3/2\). Their Proposition 3.7 gives a fixed-\(\alpha\) boundary expansion, whose remainder is not uniform as \(\alpha\downarrow3/2\); it does not imply a quadratic detachment or the coefficient \(\pi\) without the uniform linear correction and global localization above. Hu–Ye [2] give earlier two-sided bounds for the norm on the same Bloch spaces, not the critical scaling. Ye–Zheng [3] study logarithmically weighted codomains, so their sharp norm and estimates do not imply this same-space transition.

## Limitations

This is a one-sided second-order asymptotic as \(\alpha\downarrow3/2\), not an exact closed form for the optimal radius at fixed \(\alpha>3/2\), not a uniqueness assertion away from the limit, and not a result on the logarithmically weighted target spaces. Priority relative to unindexed equivalent boundary-layer analyses remains a residual risk. Independent mathematical validation has not been performed.

## References

[1] P. Cui, Z. Lin, Y. Lu, S. Ye, *Norms of the Hilbert Matrix Operator on Some Analytic Function Spaces*, arXiv:2609.27812, originally public 2026-08-20, version 3, 2026-10-21. https://arxiv.org/html/2609.27812v3

[2] H. Hu, S. Ye, *Norm of the Hilbert Matrix Operator between Some Spaces of Analytic Functions*, arXiv:2410.16598, 2024. https://arxiv.org/abs/2410.16598

[3] S. Ye, Q. Zheng, *Norm of the Hilbert Matrix Operator on Logarithmically Weighted Bloch and Hardy Spaces*, arXiv:2510.23314, 2025. https://arxiv.org/abs/2510.23314
