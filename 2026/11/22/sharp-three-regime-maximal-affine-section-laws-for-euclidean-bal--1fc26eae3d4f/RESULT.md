# Sharp three-regime maximal affine-section laws for Euclidean ball caps

## Finding
For an integer \(d\ge3\), let \(q=d-1\), \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), \(b=q\kappa_q/2\), and \(\sigma_{d-2}=2\pi^{(d-1)/2}/\Gamma((d-1)/2)\). For the solid cap
\[
K_h=\{x\in\mathbb R^d:\|x\|\le1,\ x_d\ge h\},\qquad -1<h<1,
\]
let \(X_h\) be the intrinsic \(q\)-volume of its intersection with an invariant random affine hyperplane conditioned to hit \(K_h\). If \(M_{d,h}\) is the unnormalized plane measure specified below, then the maximum is
\[
V_h=\begin{cases}\kappa_q,&h\le0,\\\kappa_q(1-h^2)^{q/2},&h>0.\end{cases}
\]
For fixed negative \(h\), put \(\alpha=\arcsin(-h)\) and \(\Omega_{d,h}=\sigma_{d-2}\int_0^\alpha\sin^{d-2}\theta\,d\theta\). For fixed positive \(h\), put \(\rho=\sqrt{1-h^2}\) and \(c=q\kappa_q h\rho^{q-2}\). Then, as \(\varepsilon\downarrow0\),
\[
\Pr(X_h\ge V_h-\varepsilon)\sim
\begin{cases}
\dfrac{2\Omega_{d,h}}{M_{d,h}\sqrt b}\,\varepsilon^{1/2},&-1<h<0,\\[4pt]
\dfrac{\sigma_{d-2}}{d(d-1)M_{d,0}b^{d/2}}\,\varepsilon^{d/2},&h=0,\\[4pt]
\dfrac{\sigma_{d-2}}{d(d-1)M_{d,h}\rho^{d-1}c^d}\,\varepsilon^d,&0<h<1.
\end{cases}
\]
For fixed \(\lambda\in\mathbb R\), take \(h=\lambda\sqrt\varepsilon\), and put
\[
a=b^{-1/2},\qquad T_\lambda=\sqrt{(\max\{\lambda,0\})^2+a^2},\qquad L_\lambda=\max\{\lambda,-a\}.
\]
Then
\[
\Pr(X_{\lambda\sqrt\varepsilon}\ge V_{\lambda\sqrt\varepsilon}-\varepsilon)
\sim\varepsilon^{d/2}\Psi_d(\lambda),\qquad
\Psi_d(\lambda)=\frac{\sigma_{d-2}}{d(d-1)M_{d,0}}
\big[(T_\lambda-\lambda)^d-(L_\lambda-\lambda)^d\big].
\]
There are branch changes at \(\lambda=-a\) and \(0\). In dimension three the nonpositive branches are polynomials of degree at most three, whereas the positive branch is proportional to \((\sqrt{\lambda^2+a^2}-\lambda)^3\). Conditional on the critical-window rare event, \((s/\sqrt\varepsilon,\theta/\sqrt\varepsilon)\) converges in law to the density proportional to
\[
r^{d-2}\,\mathbf1_{\{L_\lambda\le t\le T_\lambda,\ 0\le r\le t-\lambda\}}.
\]
The normal's azimuth is independent and uniform on \(S^{d-2}\).

## Assumptions and scope
Represent an unoriented hyperplane almost everywhere by \(H(n,s)=\{x:n\cdot x=s\}\) with \(n\cdot e_d\ge0\), \(s\in\mathbb R\); write \(\theta\) for the polar angle of \(n\). The plane measure is spherical area \(d\omega(n)\) times Lebesgue offset \(ds\), conditional on intersection. This is not a central-plane or a random-boundary-point law, and the cap is solid, not part of a surface. Tangencies and the ambiguity at the equator have measure zero. Dimensions, fixed heights and critical parameters are fixed in their respective limits.

## Proof
**Section and normalizer.** Write \(\rho=\sqrt{1-h^2}\) and \(u=\cos\theta\). The support in direction \(n\) is 1 if \(u\ge h\), otherwise it is \(hu+\rho\sqrt{1-u^2}\). In direction \(-n\) it is 1 if \(-u\ge h\), otherwise it is \(-hu+\rho\sqrt{1-u^2}\). Indeed, if the unrestricted support point is excluded, the maximum is attained on the rim. The sum is the width of the offset interval, namely
\[
w_h(u)=\begin{cases}
2\rho\sqrt{1-u^2},&h\ge0,\ 0\le u<h,\\
1-hu+\rho\sqrt{1-u^2},&h\ge0,\ h\le u\le1,\\
2,&h<0,\ 0\le u\le-h,\\
1-hu+\rho\sqrt{1-u^2},&h<0,\ -h<u\le1.
\end{cases}
\]
Thus \(M_{d,h}=\sigma_{d-2}\int_0^{\pi/2}w_h(\cos\theta)\sin^{d-2}\theta\,d\theta>0\). In particular, \(M_{d,0}\) is \(\sigma_{d-2}\) times the sum of the integrals of \(\sin^{d-2}\theta\) and \(\sin^{d-1}\theta\) over \([0,\pi/2]\), and dominated convergence gives \(M_{d,h}\to M_{d,0}\) as \(h\to0\).

For \(|s|<1\) and \(\theta>0\), the full ball section has radius \(R=\sqrt{1-s^2}\). In its steepest upward coordinate \(v\), height is \(s\cos\theta+v\sin\theta\). Thus
\[
X_h=\kappa_{q-1}\int_{\max\{k,-R\}}^R (R^2-v^2)^{(q-1)/2}\,dv,
\qquad k=\frac{h-s\cos\theta}{\sin\theta},
\]
where a lower endpoint at or above \(R\) means zero volume. At \(\theta=0\) the section is full if \(s\ge h\) and empty otherwise. A full section satisfies \(s\cos\theta-h\ge R\sin\theta\). More generally, for nonempty sections the lost cap of depth \(\tau=(R+k)_+\) has volume \(\kappa_{q-1}\int_0^\tau[y(2R-y)]^{(q-1)/2}\,dy\). With radii bounded away from zero, loss tending to zero forces \(\tau\to0\); in that range the loss is bounded above and below by fixed positive multiples of \(\tau^{d/2}\). These statements apply equally to sections of a ball with translated center, with coordinates taken relative to that center.

**Maximum.** For \(h\le0\), the unit-ball bound is attained precisely at \(s=0\) and \(\sin\theta\le-h\). For \(h>0\), the inclusion \(K_h\subseteq B_d(he_d,\rho)\) follows from
\(\|x-he_d\|^2\le1-2h x_d+h^2\le\rho^2\). The central horizontal disk of this ball attains the bound \(\kappa_q\rho^q\). Equality requires a central section of the enclosing ball to lie entirely above its equatorial plane \(x_d=h\), so this horizontal plane is the unique maximizer.

**Fixed negative height.** The full-ball bound \(\kappa_q(1-s^2)^{q/2}=\kappa_q-b s^2+O(s^4)\) forces \(|s|=O(\sqrt\varepsilon)\). Put \(t=s/\sqrt\varepsilon\). For fixed \(\theta<\alpha\) a section with this offset is eventually full, whereas for fixed \(\theta>\alpha\) it loses a volume bounded away from zero. Except on null boundaries the event indicator therefore tends to \(\mathbf1_{\{|t|<a,\ \theta<\alpha\}}\). Integrate over the bounded \(t\) range and hemisphere; the leading measure is \(2a\Omega_{d,h}\sqrt\varepsilon\).

**Critical window, including zero height.** With \(h=\lambda\sqrt\varepsilon\), the same full-ball bound gives \(|s|=O(\sqrt\varepsilon)\), and the loss to clipping is \(O(\varepsilon)\) since \(V_h=\kappa_q-O(\varepsilon)\). The depth bound gives \(\tau=O(\varepsilon^{2/d})\); in particular \(s\cos\theta-h\ge(R-\tau)\sin\theta\) forces \(\theta=O(\sqrt\varepsilon)\). Set \(s=\sqrt\varepsilon\,t,\ \theta=\sqrt\varepsilon\,r\). For fixed \(r>0\) and \(t>\lambda+r\), the section is eventually full. If \(t<\lambda+r\), the lost volume stays bounded away from zero, because \(k\to(\lambda-t)/r>-1\). In the full region the deficit relative to \(V_h\), divided by \(\varepsilon\), tends to \(b[t^2-(\max\{\lambda,0\})^2]\). Together these give the limiting wedge \(L_\lambda\le t\le T_\lambda,\ 0\le r\le t-\lambda\), up to null boundaries. The rescaled domain is bounded as proved above, and the measure divided by \(\varepsilon^{d/2}\) has density tending to \(r^{d-2}\,dt\,dr\,d\omega_{d-2}\) there, bounded by the same density. Integrating first over \(r\), then \(t\), gives the stated coefficient; the wedge has positive mass for all finite \(\lambda\). The same argument against bounded continuous test functions gives the conditional law. Azimuthal independence already holds before the limit by symmetry. Setting \(\lambda=0\) gives the fixed zero-height formula.

**Fixed positive height.** First localize using the enclosing ball centered at \(he_d\). Write \(z=s-h\cos\theta\) and \(R'=\sqrt{\rho^2-z^2}\). The near-maximum event implies \(|z|=O(\sqrt\varepsilon)\) and loses at most \(\varepsilon\) of the enclosing section to the equatorial halfspace \(x_d\ge h\). Its corresponding cap depth \(\tau'\) is \(O(\varepsilon^{2/d})\), so \(z\cos\theta\ge (R'-\tau')\sin\theta\). In particular \(\theta=O(\sqrt\varepsilon)\) and \(z\ge c_0\theta\) for some fixed \(c_0>0\). For sufficiently small \(\varepsilon\), \(s-h=z-h(1-\cos\theta)\ge c_0\theta/2\ge0\). The full section of the original unit ball has volume \(V_h-c(s-h)+O((s-h)^2)\), with \(c>0\). Since that volume is at least \(V_h-\varepsilon\), now \(s-h=O(\varepsilon)\) and \(\theta=O(\varepsilon)\).

Put \(s=h+\varepsilon t,\ \theta=\varepsilon r\). For \(r>0\) and \(t>\rho r\), the section is eventually full. For \(t<\rho r\), \(k\to-t/r>-\rho\), so the clipping loss stays bounded away from zero. The full-section deficit divided by \(\varepsilon\) tends to \(ct\). The limiting wedge is \(0\le t\le 1/c,\ 0\le r\le t/\rho\); the same dominated convergence argument now gives the unnormalized measure asymptotic to \(\sigma_{d-2}\varepsilon^d/[d(d-1)\rho^{d-1}c^d]\). Dividing the measures in all cases by the stated normalizers proves the claims.

## Verification and limitations
The supplied `verify.py` is a finite numerical checker for dimension three, based on circular segments and numerical integration. It is not needed for the proof. The three regimes are pointwise in the fixed height, and the critical result is pointwise in \(\lambda\); no uniform error bounds, simultaneous dimension limit, or result for different section laws is asserted.

## Relationship to prior work
Gille (2005) treats line chords of a hemisphere, Coleman (1992) sections of spherical shells, Kim, Yaskin and Zvavitch (2015) central sections, and Moseeva, Tarasov and Zaporozhets (2020) sections of spherical bodies on the sphere. These are not the conditional affine-plane volume law for a solid Euclidean cap. A close planar analogue is the circular-segment rare-long-chord result indexed in [6], whose stated exponents are \(1/2,1,2\) with a square-root height crossover. Here the angular measure and clipping estimates give the higher-dimensional exponents and marked wedge. The relationship to the full text of Coleman's 1989 random-section study [5] and historical priority for the higher-dimensional statements remain unresolved.

## References
1. W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24–28. https://www.thescipub.com/jmss/jmssp.2005.24.28
2. R. Coleman, *The stereology of spherical shells*, Acta Stereologica 11 (1992), 137–142. https://ias-iss.org/acta/ActaStereologica_pdf/AS_1887.pdf
3. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*. https://arxiv.org/abs/1512.07289
4. T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*. https://arxiv.org/abs/2007.07297
5. R. Coleman, *Random sections of a sphere*, Canadian Journal of Statistics 17 (1989), 27–39. https://doi.org/10.2307/3314760
6. *Three rare long-chord regimes and a critical crossover for circular segments*, Resultary, 2026-11-22, catalogue entry. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-three-rare-long-chord-regimes-and-a-critical-crossover-for-circu--c92902291168
