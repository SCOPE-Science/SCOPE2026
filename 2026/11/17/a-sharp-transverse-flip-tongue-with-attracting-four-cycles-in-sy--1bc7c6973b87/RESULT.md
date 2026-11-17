# A sharp transverse-flip tongue with attracting four-cycles in symmetric Ricker competition

## Finding
For the equal-growth two-species Ricker map
\[
F_{h,c}(x,y)=\bigl(e^h x e^{-x-cy},\ e^h y e^{-cx-y}\bigr),\qquad x,y>0,\quad 0<c<1,
\]
put \(k=(1-c)/(1+c)\). Set
\[
d_0=2\operatorname{arsinh}(1)=2\log(1+\sqrt2),\quad h_0=\sqrt2d_0,\quad k_0=\sqrt2/d_0,\quad c_0=(1-k_0)/(1+k_0).
\]
There is a neighborhood of \((d_0,k_0)\) in which the following is an exact local classification. Parameterize the growth rate by \(h=h(d)=d\coth(d/2)\). The synchronous prime-two orbit has the two scaled population values \(h-d\) and \(h+d\) and is longitudinally attracting. Define
\[
Q(d)=d^2\operatorname{csch}^2(d/2),\quad k_*(d)=\frac{\sinh d}{2d},\quad \Delta(d,k)=\sinh^2(d/2)-1-Q(d)[k-k_*(d)]^2.
\]
When \(\Delta<0\), the synchronous two-cycle is a hyperbolic sink (in the full plane) and there is no nearby species-exchanging four-cycle. When \(\Delta>0\), the synchronous two-cycle is a saddle and a **unique nearby attracting species-exchanging primitive four-cycle**, up to cyclic phase, exchanges the two species after two iterations. Along \(\Delta=0\) the synchronous orbit has transverse multiplier \(-1\), with the only nearby such symmetric four-cycle collapsed to it. These assertions concern sufficiently small neighborhoods of the marked orbit and parameter cusp, not all periodic orbits globally.

The transition tongue exists exactly on the \(d>d_0\) side and its two borders have the exact form
\[
k_\pm(d)=k_*(d)\pm\frac{\sqrt{\sinh^2(d/2)-1}}{\sqrt{Q(d)}}.
\]
As \(d\downarrow d_0\),
\[
k_+(d)-k_-(d)=\frac{2^{5/4}}{d_0}\sqrt{d-d_0}+O((d-d_0)^{3/2}).
\]
Writing \(s=(1+c)(x+y)/2\) and \(v=(1+c)(x-y)/2\), the four-cycle has, at the section near \(s=h-d\), two exchange-related points \((s,\pm v)\), with
\[
v^2=\frac{\Delta(d,k)}{\gamma_0}\,[1+o(1)],\quad \gamma_0=\frac{2[(2+\sqrt2)d_0^2+6(1+\sqrt2)d_0+8+4\sqrt2]}{3d_0^2(8-d_0^2)}>0.
\]
The limit is uniform when \(\Delta>0\) and \((d,k)\to(d_0,k_0)\). The two flip boundaries are supercritical in the transverse parameter direction.

## Assumptions and scope
The original model is the positive quadrant Ricker competition map displayed above, with equal intrinsic multipliers \(e^h>1\), symmetric interspecific coefficient \(0<c<1\), and unit self-interaction. We study only an explicitly described neighborhood of the synchronous period-two orbit and the codimension-two point \((d_0,k_0)\). Prime-four means least period exactly four for \(F_{h,c}\). An attracting periodic orbit means all multipliers of its return derivative have modulus strictly below one. The class of nearby nonsynchronous four-cycles being classified consists of the exchange-symmetric ones: two applications of \(F\) exchange species. No claim of global orbit census is made.

## Proof
**1. Exact synchronous family and multipliers.** Put \(s=(1+c)(x+y)/2\), \(v=(1+c)(x-y)/2\). The map becomes
\[
(s',v')=e^{h-s}\bigl(s\cosh(kv)-v\sinh(kv),\ v\cosh(kv)-s\sinh(kv)\bigr).
\]
The invariant line \(v=0\) carries \(s'=s e^{h-s}\). For every \(d>0\), let \(a=h(d)-d\), \(b=h(d)+d\), where \(h(d)=d\coth(d/2)\). The identities \(e^{h-a}=b/a\) and \(e^{h-b}=a/b\) show that \(a\mapsto b\mapsto a\); since \(a,b>0\) and \(a\ne b\), this is a prime-two orbit. The Jacobian of \(F^2\) at \((a,0)\) is diagonal with longitudinal and transverse multipliers
\[
m=(1-a)(1-b)=1-2h+Q,\quad \mu=(1-ka)(1-kb)=1-2kh+k^2Q,\quad Q=ab=d^2\operatorname{csch}^2(d/2).
\]
At \(d_0=2\operatorname{arsinh}1\), \(h_0=\sqrt2d_0\), \(Q_0=d_0^2\), and \(m_0=(d_0-\sqrt2)^2-1\in(-1,1)\) because \(\sqrt2<d_0<2\sqrt2\). By continuity the longitudinal return multiplier remains strictly inside the unit circle in a fixed neighborhood.

The identity \(h^2/Q=\cosh^2(d/2)\) gives the *exact* transverse discriminant reduction
\[
\mu+1=Q(k-k_*)^2-\Delta_0(d)=-\Delta(d,k),\qquad k_*=h/Q=\sinh d/(2d),\quad\Delta_0=\sinh^2(d/2)-1.
\]
At the marked point \(\mu=-1\). Nearby, \(\mu<1\) strictly (since \(\mu\) is near \(-1\)); hence \(\Delta<0\) gives a sink, whereas \(\Delta>0\) makes the synchronous orbit transversely unstable. Because \(\Delta_0\) is strictly increasing, it changes sign only at \(d_0\), and the displayed borders follow by solving the quadratic. Differentiating \(\Delta_0\) gives \(\Delta_0'(d_0)=\sqrt2\); since \(Q(d_0)=d_0^2\), the border width has the asserted square-root expansion. For each fixed \(d>d_0\) sufficiently near \(d_0\), both \(k_\pm\) lie in \((0,1)\), so they correspond to physical \(c\in(0,1)\).

**2. Reduced nonlinear equation, with explicit positive cubic.** Write the first-step map near \(v=0\) in the even/odd form
\[
s'=A(s)+B(s)v^2+O(v^4),\qquad v'=C(s)v+D(s)v^3+O(v^5),
\]
where
\[
A(s)=s e^{h-s},\quad B(s)=e^{h-s}(sk^2/2-k),\quad C(s)=e^{h-s}(1-ks),\quad D(s)=e^{h-s}(k^2/2-sk^3/6).
\]
For \(G=F^2\), around \((a,0)\) write \(s=a+u\). Direct composition yields
\[
G_s=a+mu+Hv^2+O(u^2,uv^2,v^4),\quad G_v=\mu v+Puv+Tv^3+O(u^2v,uv^3,v^5),
\]
with all coefficients evaluated at the indicated \(a,b\):
\[
\begin{aligned}
H&=A'(b)B(a)+B(b)C(a)^2,\\
P&=C'(b)A'(a)C(a)+C(b)C'(a),\\
T&=C'(b)B(a)C(a)+C(b)D(a)+D(b)C(a)^3.
\end{aligned}
\]
Species exchange is the involution \(S(s,v)=(s,-v)\), and \(G\) commutes with \(S\). We solve the symmetric-four-cycle equation \(G(s,v)=S(s,v)\). Since \(m-1\ne0\), its even first component gives, by the analytic implicit-function theorem, a unique local even solution
\[
u=\frac{H}{1-m}v^2+O(v^4).
\]
Substituting into the odd component and dividing by \(v\ne0\) gives
\[
0=\mu+1+\gamma(d,k)v^2+O(v^4),\qquad \gamma=T+PH/(1-m).
\]
At \((d_0,k_0)\) the identities \(a=d_0(\sqrt2-1)\), \(b=d_0(\sqrt2+1)\), \(k_0=\sqrt2/d_0\), \(e^{h_0-a}=3+2\sqrt2\), \(e^{h_0-b}=3-2\sqrt2\) give
\[
\begin{aligned}
H_0&=1+\sqrt2,\\
P_0&=4+3\sqrt2-(1+\sqrt2)d_0,\\
T_0&=[2+\sqrt2-(9+6\sqrt2)d_0]/(3d_0^2).
\end{aligned}
\]
Inserting these into \(T_0+P_0H_0/(1-m_0)\), simplifying, and using \(d_0^2<8\) gives the displayed strictly positive \(\gamma_0\). In fact \(\gamma_0\approx2.18375756345\). This is a nonlinear statement: the Floquet multipliers alone do not determine the sign of the cubic coefficient.

**3. Existence, uniqueness, primitivity and attraction.** Let \(t=v^2\). The analytic reduced equation has the form \(-\Delta+\gamma(d,k)t+O(t^2)=0\). By the implicit-function theorem at \((d_0,k_0,t=0)\), there is precisely one local analytic branch \(t(d,k)\), with \(t=\Delta/\gamma_0[1+o(1)]\). In a sufficiently small neighborhood, \(t>0\) exactly when \(\Delta>0\). It gives precisely the exchange-related solutions \(v=\pm\sqrt t\) of \(G(s,v)=S(s,v)\). These are one primitive four-cycle under \(F\): \(G\) switches its two unequal states and hence neither is fixed by \(G\); their first iterates lie near the other, distinct synchronous phase. The physical populations remain positive by proximity to \(a,b>0\).

For stability put \(H_*=S\circ G\), so that these points are fixed by \(H_*\), and, because \(S\) commutes with \(G\), the four-step return equals \(H_*^2\). At the cusp the multipliers of \(H_*\) are \(m_0\in(-1,1)\) and \(1\). Along the nonzero branch its slow multiplier equals \(1-2\Delta+o(\Delta)\), uniformly as \((d,k)\to(d_0,k_0)\) with \(\Delta>0\), by differentiation of the reduced odd scalar equation and the nonvanishing fast-direction Schur complement. The other multiplier tends to \(m_0\). Both have modulus below one for sufficiently small \(\Delta>0\); their squares are the four-step multipliers. This proves attraction and the local supercritical opening on both borders.

## Verification
The accompanying `verify.py` recomputes the exact local Taylor coefficients and checks the identity for \(\gamma_0\) symbolically, evaluates the cusp constants and Floquet multipliers, and solves the exchange equation at three near-cusp parameters to confirm primitive four-cycles and their two stable return multipliers. The code is a finite reproducibility check; the infinite and local-neighborhood assertions follow from the displayed analytic implicit-function arguments, not from numerical examples.

## Relationship to prior work
Goldar and coauthors (2026) study boundedness, persistence, equilibria and numerical periods in the general two-species Ricker competition map, including stable period-two orbits. The 2022 study *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability* reports numerically the appearance of out-of-phase period-four modes and branches of a resonance boundary. Those qualitative modes are **not** claimed here as newly discovered. A published synchronous-Ricker spectral Floquet reduction supplies a more general linearization framework and implies the multiplier factorization above. The new contribution is the exact analytic codimension-two threshold, the nonzero cubic coefficient, the local existence/uniqueness/attraction theorem for the shrinking four-cycle tongue and its sharp square-root width. These nonlinear local conclusions do not follow merely from the Floquet polynomial. Relevant older center-manifold literature may contain equivalent local normal forms; see limitations.

## Limitations
This is a local analytical theorem. It does not classify other four-cycles, other attractors, global basins, or the entire two-parameter diagram. The 2022 paper already describes related mode changes numerically; no priority claim is made for their qualitative occurrence. The relevant sections of Luís–Elaydi–Oliveira (2011) were compared in the searchable PDF text: they concern equilibria, exclusion cycles, and general bifurcation scenarios, not the present analytically resolved transverse tongue. Its mathematical techniques and wider bibliography remain a historical-priority consideration; the PDF screenshot service did not load. The present proof does not establish novelty over undiscovered older local bifurcation formulas and has not undergone independent review.

## References
1. S. Goldar et al., *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society, 2026, DOI: 10.1155/ddns/7255117. First published 2026-09-16. https://onlinelibrary.wiley.com/doi/10.1155/ddns/7255117
2. *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics 10 (2022), 1076. https://www.mdpi.com/2227-7390/10/7/1076
3. R. Luís, S. Elaydi, H. Oliveira, *Stability of a Ricker-type competition model and the competitive exclusion principle*, Journal of Biological Dynamics 5 (2011), 636–660. https://doi.org/10.1080/17513758.2011.581764
4. *Synchronous Ricker spectral Floquet reduction*, published mathematical record (2026-09-20). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-synchronous-ricker-spectral-floquet-reduction--5261a9c6ad45
