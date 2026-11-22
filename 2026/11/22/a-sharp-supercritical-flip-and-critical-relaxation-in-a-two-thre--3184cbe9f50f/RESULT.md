# A sharp supercritical flip and critical relaxation in a two-threshold affine relay

## Finding
Let \(\mu>0\). Consider a hysteretic planar flow with active mode \(U\) satisfying \(\dot x=-1,\ \dot y=x\), and active mode \(L\) satisfying \(\dot x=1,\ \dot y=1-x/2\). Mode \(U\) is maintained until the first subsequent hit of \(y=-\mu\), at which time mode \(L\) becomes active; mode \(L\) is maintained until the first subsequent hit of \(y=+\mu\), when mode \(U\) resumes. The mode is part of the state. For every \(0<\mu<8\), there is exactly one transverse one-lap periodic trajectory; its upper switching abscissa is \(p_\mu=\mu/2-2\), lower switching abscissa is \(s_\mu=-\mu/2-2\), and physical period is \(2\mu\).

Its one-lap return multiplier crosses \(-1\) exactly at \(\mu_{\rm c}=4\sqrt2\). The one-lap cycle attracts neighboring trajectories for \(0<\mu<\mu_{\rm c}\), is locally attracting but nonhyperbolic at \(\mu=\mu_{\rm c}\), and repels transversely for \(\mu_{\rm c}<\mu<8\). The flip is nondegenerate and supercritical: writing \(\delta=\mu-\mu_{\rm c}\) and \(B=9\sqrt2-12>0\), for all sufficiently small \(\delta>0\) there exists exactly one nearby primitive period-two orbit of the one-lap section map. It is attracting and its upper switching abscissae satisfy
\[
 x_\pm(\mu)=p_\mu\pm2\sqrt{\frac{\delta}{B}}+O(\delta).
\]
For sufficiently small \(\delta<0\), there is no nearby primitive period-two section orbit. The two-lap cycle has physical period tending to \(4\mu_{\rm c}\) as \(\delta\downarrow0\).

At criticality, for every sufficiently close initial upper switching point except the fixed point itself, the successive upper switching abscissae satisfy the sharp original-return-time law
\[
 \lim_{n\to\infty} n\left(x_n-p_{\mu_{\rm c}}\right)^2=\frac{2}{9\sqrt2-12}.
\]
No global attractor or orbit census outside the local return neighborhood is asserted.

## Assumptions and scope
The two fields and first-hit switching convention above are exact, and the threshold band is \([-\mu,\mu]\). Trajectories are considered where the two first-hit events exist and are transverse. The uniqueness assertion concerns strictly transverse **one-lap** periodic trajectories, not all periodic trajectories. For \(0<\mu<8\), the exhibited orbit crosses \(y=-\mu\) with \(\dot y=s_\mu<0\) in mode \(U\), and crosses \(y=+\mu\) with \(\dot y=1-p_\mu/2>0\) in mode \(L\). Thus a smooth local Poincaré return exists around it. The parameter endpoint \(\mu=8\), where the upper recovery is tangent, is excluded.

## Proof
**First-hit map.** Start in mode \(U\) at \((x,\mu)\). At time \(t\), \(x(t)=x-t\), \(y(t)=\mu+xt-t^2/2\). Solving \(y(t)=-\mu\), the unique positive first hitting time is \(t=x+\sqrt{x^2+4\mu}\). Hence the lower switching coordinate is \(s=-\sqrt{x^2+4\mu}<0\); the crossing derivative is \(s<0\). In mode \(L\), \(dx/dt=1\) and \(dy/dx=1-x/2\). Thus \(H(x)=x-x^2/4\) increases by exactly \(2\mu\) between the switches. Where the first upward crossing occurs before \(x=2\), solve \(H(x')=H(s)+2\mu\) using the lower root \(x'<2\). This gives the analytic local return map
\[
 P_\mu(x)=2-\sqrt{4+4\sqrt{x^2+4\mu}+x^2-4\mu}.
\]
All radicals are positive and both switches remain transverse on an open section neighborhood of the asserted orbit.

**Periodic orbit and uniqueness.** A fixed upper point \(p\) and lower point \(s\) must satisfy \(s^2=p^2+4\mu\), \(s<0\), and \(H(p)-H(s)=2\mu\). The first equality says \((p-s)(p+s)=-4\mu\); substituting in the second yields \(p-s=\mu\) and consequently \(p+s=-4\). Necessarily \(p=\mu/2-2\), \(s=-\mu/2-2\). For \(0<\mu<8\), these coordinates satisfy \(s<0\), \(s<p<2\), and the prescribed lower and upper first hits are realized. Because each horizontal velocity is of magnitude one, each leg lasts \(\mu\), giving physical period \(2\mu\).

**Stability and exact flip.** Put \(z=\mu/4\), \(X=x/2\). The normalized return is
\[
 T_z(X)=1-\sqrt{1+2\sqrt{X^2+4z}+X^2-4z},\qquad X_*(z)=z-1.
\]
Differentiation at the fixed point (the inner square root there equals \(z+1\), the outer one equals \(2-z\)) yields
\[
 q(z)=T_z'(X_*)=\frac{(z-1)(z+2)}{(z-2)(z+1)},\qquad 0<z<2.
\]
The inequalities \(\lvert q(z)\rvert<1\) for \(0<z<\sqrt2\), \(q(\sqrt2)=-1\), and \(q(z)<-1\) for \(\sqrt2<z<2\) follow by elementary multiplication with the positive denominator \((2-z)(z+1)\). Furthermore \(q'(\sqrt2)=-4\), so \(q=-1-\delta+O(\delta^2)\) with \(\delta=\mu-4\sqrt2\).

**Cubic coefficient and bifurcation.** At \(z_{\rm c}=\sqrt2\), differentiation of the explicit local map gives
\[
 T''_{z_{\rm c}}(X_*)=-12+8\sqrt2,\qquad
 T'''_{z_{\rm c}}(X_*)=-480+342\sqrt2.
\]
Writing \(u=X-X_*(z)\), the Taylor expansion has \(u\mapsto q(z)u+a(z)u^2+b(z)u^3+O(u^4)\), with analytic coefficients. At criticality, the squared map has expansion
\[
 T_{z_{\rm c}}^2(X_*+u)-X_*=u-2B u^3+O(u^4),\qquad
 B=b(z_{\rm c})+a(z_{\rm c})^2=9\sqrt2-12>0.
\]
The parameter-dependent second-return displacement factors by \(u\) because the fixed branch persists. Its quotient, near the origin, is \(2\delta-2B u^2+O(\delta^2+\lvert\delta u\rvert+\lvert u\rvert^3)\). By the standard blow-up \(u=\sqrt\delta\,v\), or the implicit function theorem after dividing by \(\delta\), there are exactly two nearby nonzero zeros for \(\delta>0\), with \(u_\pm=\pm\sqrt{\delta/B}+O(\delta)\), and none for \(\delta<0\). Since \(T_z\) exchanges the two roots, they form one primitive two-cycle. The derivative of \(T_z^2\) on it is \(1-4\delta+O(\delta^{3/2})\); hence it is attracting for small positive \(\delta\). Converting \(x=2X\) proves the abscissa asymptotic. At \(\delta=0\), the negative cubic displacement proves local attraction under even iterates; the intervening odd iterates also tend to the fixed point.

**Critical slowing.** At \(z=z_{\rm c}\), for a nonzero sufficiently small \(u_0\), the even iterates \(v_k=u_{2k}\) satisfy \(v_{k+1}=v_k-2Bv_k^3+O(v_k^4)\). They preserve their nonzero sign and tend to zero monotonically in absolute value. Thus
\[
 v_{k+1}^{-2}-v_k^{-2}=4B+O(\lvert v_k\rvert)\longrightarrow4B.
\]
Cesàro summation yields \(k v_k^2\to1/(4B)\), hence \(n u_n^2\to1/(2B)\) along both parities. Because \(x_n-p=2u_n\), the asserted limit is \(2/B\). The argument proves an infinite-time limit; finite numerical trajectories are supplementary only.

## Verification
Run `python checker.py` with SymPy and mpmath. The script checks the exact switching-coordinate algebra and sample fixed points, symbolic critical derivatives and flip coefficient, and numerical two-cycle and slow-relaxation trajectories. The analytical proof above, not finite computation, establishes uniqueness, bifurcation, and limits.

## Relationship to prior work
Carvalho–Serantola–Rangel (2026) analyze a related large-hysteresis relay with upper field \((a_1,b_1x)\) but **constant** lower vertical velocity \((a_2,b_2)\). Their exact limit-set classification and return-map method motivate the question. In contrast, the present lower mode has \(\dot y=1-x/2\); its recovery leg is parabolic, changing the return-map derivative and permitting the computed smooth flip. Their one-lap constant-recovery statement does not give this threshold or its cubic coefficient. Sella–Collins (2008) already exhibit complicated period-doubling dynamics in *other* piecewise-affine hysteresis systems; no general novelty of period doubling is claimed. Carmona et al. (2023) develop broad linear Poincaré half-map techniques, which are compatible methods rather than the specific calculation here. General local flip theory supplies a method but does not determine the model-dependent threshold or coefficient.

## Limitations
The two-lap cycle is guaranteed only locally for small positive detuning. No global classification of higher-period cycles, basin sizes, or existence beyond the transverse return domain is asserted. The recovery field is a deliberately simple affine extension of the constant-recovery setting, not a parameter specialization of it. The historical literature cannot be exhaustively excluded, and analogous findings in differently normalized relays are possible. The self-contained calculation remains subject to independent mathematical validation.

## References
- T. Carvalho, L. Serantola, B. S. Rangel, *Limit Sets and Global Bifurcation Structure in Planar Control Models with Large Hysteresis*, arXiv:2609.08974 (first public 2026-09-08), https://arxiv.org/abs/2609.08974.
- L. Sella, P. Collins, *Symbolic Dynamics for a Piecewise-Affine System with Hysteresis*, MTNS 2008, https://scholar.lib.vt.edu/MTNS/Papers/086.pdf.
- V. Carmona, F. Fernández-Sánchez, E. García-Medina, D. Novaes, *Properties of Poincaré half-maps for planar linear systems and some direct applications to periodic orbits of piecewise systems*, Electron. J. Qual. Theory Differ. Equ. 2023, no. 22, https://doi.org/10.14232/ejqtde.2023.1.22.
