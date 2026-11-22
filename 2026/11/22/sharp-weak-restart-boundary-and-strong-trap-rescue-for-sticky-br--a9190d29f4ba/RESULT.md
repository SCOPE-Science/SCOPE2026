# Sharp weak-restart boundary and strong-trap rescue for sticky Brownian escape

## Finding
A Brownian particle in a finite interval can linger on a **sticky reflecting wall** before escaping through the opposite absorbing endpoint. Complete independent Poisson resetting to the launch point has a unique, explicitly algebraic threshold for its *infinitesimal-rate* effect. In the limit of extremely strong stickiness, every fixed strictly interior reset site admits a finite mean escape time under any fixed positive reset rate, whereas the mean without restarting diverges. Resetting exactly at the sticky wall never helps, even for a finite resetting rate.

Write \(u=x_0/L\in[0,1)\), \(\eta=\nu/L\ge0\), and \(z=rL^2/D\). Define the cubic
\[
P_\eta(u)=5u^3+(5+20\eta)u^2+(24\eta^2+8\eta-1)u-(1+4\eta).
\]
For each \(\eta\ge0\), there is exactly one \(u_*(\eta)\in(0,1)\) with \(P_\eta(u_*)=0\). The derivative of the mean escape time with respect to the reset rate at zero has the sign of \(-P_\eta(u)\) for \(u\in[0,1)\): weak resetting decreases the mean precisely for \(u>u_*(\eta)\), increases it precisely for \(u<u_*(\eta)\), and has vanishing first variation at equality. These statements are only about sufficiently weak resetting; they do **not** classify benefit over all finite rates away from \(u=0\).

The threshold decreases strictly with stickiness, with sharp limits
\[
 u_*(0)=\frac1{\sqrt5},\qquad
 \lim_{\eta\to\infty}u_*(\eta)=0,\qquad
 \lim_{\eta\to\infty}\eta u_*(\eta)=\frac16.
\]
For every \(0<u<1\) and every fixed \(r>0\), increasing \(\eta\) indefinitely produces a finite limiting restarted mean despite the unreset mean diverging linearly. At the exceptional reset point \(u=0\), **every** positive reset rate strictly increases the mean for every finite \(\eta\ge0\).

## Assumptions and scope
Fix \(D,L>0\), \(\nu\ge0\), \(x_0\in[0,L)\), and \(r\ge0\). The unreset position process is the sticky reflecting diffusion whose interior generator is \(\mathcal Lf=Df''\) on \((0,L)\), with Feller-Wentzell boundary condition \(f'(0)=\nu f''(0)\) and killing at \(L\). The endpoint \(0\) is conservative and carries positive residence mass if \(\nu>0\); it is not a partially absorbing Robin boundary. At independent Poisson times with rate \(r\), the full Markov state is reinitialized at the deterministic \(x_0\), including release from the sticky endpoint. The experiment stops upon reaching \(L\). Let \(\tau_r\) be that first-escape time and \(T_r=\mathbb E\tau_r\).

Define \(q=\sqrt z\) and \(H_\eta(q,y)=\cosh(qy)+\eta q\sinh(qy)\), for \(y\in[0,1]\). This normalization makes \(z=rL^2/D\), \(u=x_0/L\), and \(\eta=\nu/L\) dimensionless. The Brownian convention is variance \(2Dt\) away from the boundary. Strictly positive weak-reset effects mean that for all sufficiently small \(r>0\) the sign of \(T_r-T_0\) is as stated; at the threshold only its first derivative is classified.

## Proof
**1. Unreset first-passage transform.** Let \(\tau\) denote the unreset hitting time of \(L\). For \(s>0\), the resolvent \(\phi_s(x)=\mathbb E_x e^{-s\tau}\) solves \(D\phi_s''=s\phi_s\) on \((0,L)\), \(\phi_s(L)=1\), and \(\phi_s'(0)=\nu\phi_s''(0)=\nu(s/D)\phi_s(0)\). Consequently, with \(q=L\sqrt{s/D}\),
\[
\phi_s(x_0)=\frac{H_\eta(q,u)}{H_\eta(q,1)}.
\]
For a full Poisson renewal restart at rate \(r>0\), conditioning on the first attempted passage versus first reset gives the standard identity \(T_r=(1-\phi_r(x_0))/(r\phi_r(x_0))\). Hence
\[
\boxed{\frac{DT_r}{L^2}=\frac{H_\eta(q,1)-H_\eta(q,u)}{q^2H_\eta(q,u)},\qquad q=\sqrt{rL^2/D}.}
\]
The Taylor expansion at \(q=0\) yields \(DT_0/L^2=(1-u^2)/2+\eta(1-u)\). Both expressions include \(u=0\) by continuity.

**2. Exact weak-rate sign.** Expand the analytic even functions \(H_\eta\) through order \(q^4\) and divide. Uniformly for each fixed \((u,\eta)\) as \(z=q^2\downarrow0\),
\[
\frac{DT_r}{L^2}=\frac{1-u^2}{2}+\eta(1-u)
-\frac{(1-u)P_\eta(u)}{24}z+O_{u,\eta}(z^2).
\]
In particular,
\[
\left.\frac{dT_r}{dr}\right|_{r=0+}
=-\frac{L^4}{24D^2}(1-u)P_\eta(u).
\]
An independent check uses the backward moment recursion: the mean \(m_1(y)=(1-y^2)/2+\eta(1-y)\) in units \(L^2/D\) and second moment \(m_2\) solve \(m_2''=-2m_1\), \(m_2'(0)=\eta m_2''(0)\), \(m_2(1)=0\). Direct integration verifies \(m_1(u)^2-m_2(u)/2=-(1-u)P_\eta(u)/24\), the universal zero-rate restart derivative.

**3. Exactly one critical launch point and its movement.** The descending-sign coefficient sequence of \(P_\eta\) is positive, positive, either sign, negative. By Descartes' rule it has precisely one positive real root, counting multiplicity (existence follows from opposite signs at zero and one): \(P_\eta(0)=-(1+4\eta)<0\), \(P_\eta(1)=8+24\eta+24\eta^2>0\). Thus its sign is negative below, positive above \(u_*(\eta)\), with no other positive sign reversals. At \(\eta=0\) factorization gives \(P_0(u)=(u+1)(5u^2-1)\), hence \(u_*(0)=1/\sqrt5\).

For \(u\ge1/\sqrt5\), \(P_\eta(u)>0\) for all \(\eta>0\) because \(P_0(u)\ge0\) and \(\partial_\eta P_\eta(u)=48\eta u+20u^2+8u-4>0\) in this region. For every fixed \(0<u<1/\sqrt5\), express \(P_\eta(u)=24u\eta^2+(20u^2+8u-4)\eta+(1+u)(5u^2-1)\). This upward quadratic has negative constant and therefore exactly one positive root in \(\eta\), changing sign from negative to positive there. This proves that \(u_*(\eta)\) is strictly decreasing. Substituting \(u=t/\eta\) gives \(P_\eta(t/\eta)/\eta\to24t-4\) uniformly on compact positive \(t\)-sets, so bracketing the unique root about \(t=1/6\) proves \(\eta u_*(\eta)\to1/6\). The remaining limit follows.

**4. Strong-stickiness rescue and boundary exception.** For fixed \(q>0\) and \(0<u<1\), the ratio of hyperbolic functions satisfies
\[
\lim_{\eta\to\infty}\frac{DT_r}{L^2}
=\frac1{q^2}\left(\frac{\sinh q}{\sinh(qu)}-1\right)<\infty.
\]
But \(DT_0/L^2=(1-u^2)/2+\eta(1-u)\to\infty\); thus \(T_r/T_0\to0\) for any fixed positive rate. At \(u=0\), instead, \(H_\eta(q,0)=1\), so
\[
\frac{D(T_r-T_0)}{L^2}
=\frac{\cosh q-1-q^2/2}{q^2}
+\eta\left(\frac{\sinh q}{q}-1\right)>0
\]
for all \(q>0\) (strict positive terms in the power series of the first summand). This proves the all-rate boundary exception and completes the asserted classification.

## Verification
The standalone `verify.py` checks the transformed Wentzell boundary-value problem, reconstructs the second hitting-time moment independently from its differential equation, verifies the exact polynomial identity symbolically with SymPy, checks the non-sticky normalization, tests the single-root and sharp large-stickiness scaling numerically, and compares the transform with a separately discretized sticky finite-volume Markov generator. It additionally tests weak-rate slopes and fixed-rate strong-stickiness limits. The checker passed **118 assertions** on the packaged source. Finite-volume discretization and numerical probes are corroboration, not the proof of the universal assertions.

## Relationship to prior work
Bressloff (2023, arXiv:2302.13986v1) establishes the underlying Feller-Wentzell sticky-boundary physics, including the boundary condition in Eq. (2.23). Scher, Reuveni and Grebenkov (2023, arXiv:2305.08701v1) give the *unreset sticky slab escape transform* in Eqs. (4), (6) and (9) for a reversible adsorption-desorption wall. Its rapid-binding limit produces the same Wentzell escape transform, so the base first-passage distribution, moments and hyperbolic kernel are **not claimed new**. The classical renewal-restart identity is also established prior work (e.g. Pal and Prasad, 2019). The assessed contribution is the exact sticky-strength-dependent weak-reset **sign boundary**, proof of its strict movement and \(1/6\)-law, together with the noncommuting strong-stickiness/launch-at-wall rescue distinction. These statements require analyzing the combined renewal transform as a two-parameter optimization problem, rather than simply reporting an existing first-passage formula.

The published partially reactive-interval result for a Robin-reactive **absorbing** endpoint and an opposite **reflecting** endpoint concerns a different boundary generator and gives a different global condition; that result does not imply a Wentzell-sticky reflecting wall opposite an absorbing endpoint. Pal and Prasad's two-absorbing-endpoint interval has a different boundary structure. Song and Wang's sticky reflecting diffusions with double-exponential jumps use non-reset jump dynamics. Search and source coverage are detailed in `AUDIT.json` and `REVIEW.md`.

## Limitations
The threshold is for the derivative at reset rate zero, not a global if-and-only-if benefit criterion at all rates. No uniqueness of a positive-rate optimum or sign of the second-order rate effect at \(u=u_*(\eta)\) is asserted. The large-stickiness rescue is pointwise at fixed \(u>0\) and fixed \(r>0\), not uniform as the launch site approaches the sticky wall or the reset rate approaches zero. The limit \(\eta=\infty\) is only an asymptotic limit of finite-stickiness processes. This is a complete-state Poisson reset, not a reset that preserves surface residence or partial adsorption. Unindexed prior equivalent analyses remain a publication-priority risk. No independent scientific review is claimed.

## References
- P. C. Bressloff, *Close encounters of the sticky kind: Brownian motion at absorbing boundaries*, arXiv:2302.13986v1 (first public 2023-02-27), especially Eq. (2.23), https://arxiv.org/abs/2302.13986.
- Y. Scher, S. Reuveni and D. S. Grebenkov, *Escape of a Sticky Particle*, arXiv:2305.08701v1 (first public 2023-05-15), especially Eqs. (4), (6), (9), https://arxiv.org/abs/2305.08701.
- A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, Phys. Rev. E 99, 032123 (2019), https://doi.org/10.1103/PhysRevE.99.032123.
- S. Song and Y. Wang, *On first passage times of sticky reflecting diffusion processes with double exponential jumps*, J. Appl. Probab. 57 (2020), https://doi.org/10.1017/jpr.2019.93.
