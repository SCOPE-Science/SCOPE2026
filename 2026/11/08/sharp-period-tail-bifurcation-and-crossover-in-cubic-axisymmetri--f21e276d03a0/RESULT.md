# Sharp period-tail bifurcation and crossover in cubic axisymmetric torus flows

## Finding

For each real \(a>1\), consider the smooth algebraic torus
\[
\mathcal T_a=\{(x,y,z)\in\mathbb R^3:(x^2+y^2-a^2)^2+z^2=1\}
\]
and, for each \(c\ge0\), the homogeneous cubic polynomial flow
\[
\dot x=(x^2+y^2-cz^2)y,\qquad
\dot y=-(x^2+y^2-cz^2)x,\qquad \dot z=0.
\]
Let \(\nu_a\) be the probability obtained by normalizing Euclidean surface area on \(\mathcal T_a\). For \(\nu_a\)-almost every initial point, let \(T_c\) be the least positive original-time period of its trajectory. (On the measure-zero equilibrium circles, put \(T_c=+\infty\) solely for defining a random variable.)

Set
\[
\begin{gathered}
 c_* = \frac{a^2+\sqrt{a^4-1}}{2},\quad
 u_*=-\frac{1}{2c_*},\quad \gamma=1-u_*^2,\\
 w_a(u)=\sqrt{\frac{1-u^2+4(a^2+u)u^2}{1-u^2}},\quad
 J_a=\int_{-1}^1 w_a(u)\,du,
 \qquad (-1<u<1).
\end{gathered}
\]
The following is an exact trichotomy and crossover law.

**(i) Subcritical:** for \(0\le c<c_*\), all trajectories are periodic and their periods are uniformly bounded. In particular the essential maximum period is \(2\pi/(a^2-1)\) for \(0\le c\le 1/2\), and \(2\pi/(a^2-c-1/(4c))\) for \(1/2<c<c_*\).

**(ii) Critical:** at \(c=c_*\), exactly two equilibrium latitude circles appear and
\[
 \boxed{\lim_{t\to\infty}\sqrt t\,\nu_a(T_{c_*}>t)
 = \frac{2w_a(u_*)}{J_a}\sqrt{\frac{2\pi}{c_*}}.}
\]

**(iii) Supercritical:** for \(c>c_*\), exactly four equilibrium latitude circles occur. Writing \(\Delta_c=4c^2-4a^2c+1>0\) and \(u_\pm=(-1\pm\sqrt{\Delta_c})/(2c)\),
\[
 \boxed{\lim_{t\to\infty}t\,\nu_a(T_c>t)
 = \frac{4\pi}{J_a\sqrt{\Delta_c}}\bigl(w_a(u_-)+w_a(u_+)\bigr).}
\]

**(iv) Critical scaling window:** for every fixed \(\lambda\in\mathbb R\), with \(c_t=c_*+\lambda/t\),
\[
\boxed{
\lim_{t\to\infty}\sqrt t\,\nu_a(T_{c_t}>t)
=\frac{2w_a(u_*)}{J_a\sqrt{c_*}}
\left[\sqrt{(2\pi+\gamma\lambda)_+}-\sqrt{(\gamma\lambda-2\pi)_+}\right],
}
\]
where \(r_+=\max(r,0)\). This scaling limit includes a zero-tail region, the double-root critical law, and the nearby split-root regime. It is a single simultaneous limit, not an assertion of uniform convergence for unbounded \(\lambda\).

The thresholds for positive period moments are sharp:
\[
\begin{array}{c|c}
0\le c<c_* & \mathbb E_{\nu_a}[T_c^p]<\infty\text{ for every }p\ge0,\\
c=c_* & \mathbb E_{\nu_a}[T_c^p]<\infty\ \Longleftrightarrow\ p<1/2,\\
c>c_* & \mathbb E_{\nu_a}[T_c^p]<\infty\ \Longleftrightarrow\ p<1.
\end{array}
\]
Finally, the finite mean from below diverges with the exact coefficient
\[
\boxed{\lim_{c\uparrow c_*}\sqrt{c_*-c}\;\mathbb E_{\nu_a}[T_c]
=\frac{2\pi^2w_a(u_*)}{J_a(a^4-1)^{1/4}}.}
\]

## Assumptions and scope

All parameters \(a>1\) and \(c\ge0\) are real. The torus is the specified embedded smooth surface with its Euclidean two-dimensional area measure (not the flat parameter-space measure). Original-time periods refer to the given polynomial vector field, with no time reparametrization. Equilibrium parallels have area zero. All probability limits concern the explicitly indicated fixed or varying parameters, and positive real \(t\to\infty\).

The source paper establishes this torus family and classifies pseudo-type cubic flows of the form \((Ay,-Ax,0)\) with homogeneous quadratic \(A\). The present specialization uses \(A=x^2+y^2-cz^2\). The results here describe the distribution of periods under geometric surface-area sampling, which is not implied by first-integral existence or mere periodicity.

## Proof

**1. Orbit dynamics and exact period.** Put \(x=r\cos\theta\), \(y=r\sin\theta\), where \(r>0\). Direct substitution gives \(\dot r=0\), \(\dot z=0\), and \(\dot\theta=-(r^2-cz^2)\). These identities show that the polynomial flow is complete on the compact invariant torus, and every nonstationary trajectory is a latitude circle traversed at constant angular speed. Parameterize the torus by
\[
 r(s)=\sqrt{a^2+\cos s},\quad z(s)=\sin s,\quad
 (x,y)=(r(s)\cos\theta,r(s)\sin\theta),\quad 0\le s,\theta<2\pi.
\]
Writing \(u=\cos s\), the angular speed magnitude equals
\[
 |Q_c(u)|,\qquad Q_c(u)=a^2+u-c(1-u^2),\qquad
 T_c(u)=\frac{2\pi}{|Q_c(u)|}
\]
for \(Q_c(u)\ne0\). This is the **least**, not merely a return-time multiple, since the embedded latitude is a simple circle and \(\theta\) advances linearly.

**2. Actual surface-area law.** The two tangent vectors of the parameterization have orthogonal lengths \(r(s)\) and \(\sqrt{r'(s)^2+\cos^2s}\). Hence
\[
 dA=\tfrac12\sqrt{\sin^2s+4(a^2+\cos s)\cos^2s}\,d\theta\,ds.
\]
Pushing forward the normalized area to \(u=\cos s\) (two values of \(s\) for interior \(u\)) gives exactly
\[
 (u)_\#\nu_a=\frac{w_a(u)}{J_a}\,du.
\]
Indeed, \(w_a\) is positive smooth in \((-1,1)\) and has only integrable square-root singularities at the endpoints. Thus, for every \(t>0\), the **exact** period-survival formula is
\[
 \nu_a(T_c>t)=\frac{1}{J_a}\int_{-1}^{1}
 {\bf1}_{\{|Q_c(u)|<2\pi/t\}}w_a(u)\,du.
\tag{1}
\]
The set where \(Q_c=0\) has area zero; its treatment does not affect (1). Surface area is invariant under this flow because \(u\) is fixed and the angular variable undergoes a translation at speed depending only on \(u\).

**3. Zero-set transition.** The quadratic can be completed as
\[
 Q_c(u)=c\left(u+\frac{1}{2c}\right)^2+
 \left(a^2-c-\frac{1}{4c}\right)\qquad(c>0).
\]
For \(0\le c\le1/2\), its minimum on \([-1,1]\) occurs at \(u=-1\), and equals \(a^2-1\). For \(c>1/2\), the minimum occurs at \(-1/(2c)\). Its first zero at positive \(c\) is the larger root \(c_*\) of \(c^2-a^2c+1/4=0\), and the resulting zero is double in \(u\). Beyond it, the two simple roots \(u_\pm\) lie strictly within \((-1,1)\), because both endpoint values \(Q_c(-1)=a^2-1\) and \(Q_c(1)=a^2+1\) are positive. Each interior root corresponds to two stationary latitude circles, proving the stated zero counts and finite upper bounds below the transition.

**4. Fixed-parameter period tails.** At the threshold, \(Q_{c_*}(u)=c_*(u-u_*)^2\). Consequently, (1) integrates over \(u\in(u_*-\sqrt{2\pi/(c_*t)},u_*+\sqrt{2\pi/(c_*t)})\), for sufficiently large \(t\). Continuity of \(w_a\) at \(u_*\) proves the critical constant. Above threshold, \(Q_c'(u_\pm)=\pm\sqrt{\Delta_c}\). For small \(\delta=2\pi/t\), the preimage \(|Q_c|<\delta\) comprises two disjoint intervals, each of length \(2\delta/\sqrt{\Delta_c}+o(\delta)\). Substitution into (1) proves the supercritical constant.

**5. Simultaneous crossover.** Fix \(\lambda\in\mathbb R\) and put \(c_t=c_*+\lambda/t\). At \(u=u_*+v/\sqrt t\), the polynomial identity yields
\[
 tQ_{c_t}(u)=c_*v^2-\gamma\lambda+
 O_{\lambda}\bigl(t^{-1/2}(|v|+|v|^3)+t^{-1}v^2\bigr)
\]
uniformly for \(v\) in compact sets. Because \(Q_{c_*}\) has a unique zero and grows quadratically nearby, every \(u\) contributing to (1) is within \(O_\lambda(t^{-1/2})\) of \(u_*\). The scaled domain therefore converges in measure to
\[
 \{v\in\mathbb R:|c_*v^2-\gamma\lambda|<2\pi\}.
\]
Its Lebesgue length is
\[
 \frac{2}{\sqrt{c_*}}
 \left[\sqrt{(2\pi+\gamma\lambda)_+}
 -\sqrt{(\gamma\lambda-2\pi)_+}\right].
\]
The density tends uniformly to \(w_a(u_*)/J_a\) in the shrinking window. This proves the crossover, including the boundary cases where the limiting domain has zero width.

**6. Moments and mean blow-up.** In (1) the only divergent periods arise at polynomial zeros. A zero of order \(k\) produces local \(T_c\asymp|u-u_0|^{-k}\), with area density bounded above and below by positive constants, so \(T_c^p\) is integrable exactly when \(kp<1\). There are no zeros below the threshold, one double \(u\)-zero at criticality, and two simple \(u\)-zeros above. Finally, write \(\epsilon=c_*-c\downarrow0\), \(v=u+1/(2c)\), and
\[
 Q_c(u)=cv^2+m_c,\quad
 m_c=a^2-c-\frac{1}{4c}=\gamma\epsilon+O(\epsilon^2).
\]
The diverging mean is localized near \(u_*\), where \(w_a(u)=w_a(u_*)+o(1)\). Rescaling \(v=\sqrt{\epsilon}\,s\) and using \(\int_{\mathbb R}(c_*s^2+\gamma)^{-1}ds=\pi/\sqrt{c_*\gamma}\) gives
\[
 \lim_{\epsilon\downarrow0}\sqrt\epsilon\,\mathbb E T_{c_*-\epsilon}
 =\frac{2\pi^2 w_a(u_*)}{J_a\sqrt{c_*\gamma}}.
\]
The identity \(c_*\gamma=\sqrt{a^4-1}\) gives the stated coefficient. This completes the proof.

## Verification

The exact radius/angle and square-completion identities were checked symbolically by `CHECK.py`, and direct numerical evaluation of the surface-area integral at \(a=3/2\), \(t=10^4,10^6\), and \(\lambda\in\{-10,-2,0,2,10\}\) was compared with the closed crossover law. The exact general theorem is proved above and does not rely on finite numerical sampling. Reproduction instructions and representative output appear in `VERIFICATION.md`.

## Relationship to prior work

Jana's *Characterization and dynamics of certain classes of polynomial vector fields on the torus* (arXiv:2401.07843, initially posted 2024-01-15), specifically Theorem 2.3 in a later version / Theorem 4.3 in another posted version, classifies pseudo-type fields \((Ay,-Ax,0)\) and proves complete integrability. This is the starting structural result, **not** a new claim here. Its inspected results on invariant parallels, meridians, singularities and periodicity do not give the surface-area period law, sharp tail constants, or scaling window. Llibre and Rebollo-Perdomo (2013) classify configurations of invariant parallels, meridians and limit cycles on algebraic tori; their inspected complete open preprint concerns existence/configuration rather than the present metric distribution. Related period-divergence laws for meridian cycles or planar polynomial centers concern different flows and do not imply the four formulas above. Searches do not establish exhaustive novelty; unindexed equivalent work remains possible.

## Limitations

Only the specified homogeneous cubic axisymmetric family, its fixed smooth torus, and normalized Euclidean surface-area sampling are treated. The angular period equation is elementary, but its geometric area-weighted distribution, transition constants and simultaneous critical crossover require the area density and root-localization analysis. No claim is made about polynomial fields with general angle-dependent \(A\), full three-dimensional volume sampling, the stability of fixed latitude circles under perturbations, or uniformity in an unbounded scaling parameter. Independent audit is not performed; prior-literature comparisons remain subject to bibliographic incompleteness.

## References

1. S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843 (initial public posting 2024-01-15), https://arxiv.org/abs/2401.07843 ; full text https://arxiv.org/html/2401.07843v2 .
2. J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in* \(\mathbb R^3\), Journal of Dynamics and Differential Equations 25 (2013), 777–793, DOI:10.1007/s10884-013-9315-4 ; open preprint https://ddd.uab.cat/pub/artpub/2013/gsduab_3215/InvParInvMeronTori.pdf .
3. J. Llibre and J. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, 2011 (bibliographic mention in reference 1; complete main text not inspected).
