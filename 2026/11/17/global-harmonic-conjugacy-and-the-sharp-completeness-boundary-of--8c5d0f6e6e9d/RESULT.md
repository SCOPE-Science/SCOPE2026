# Global harmonic conjugacy and the sharp completeness boundary of a quadratic torus flow

## Finding
For the explicit quadratic subfamily of the polynomial vector fields on an algebraic torus classified by Jana, the entire three-dimensional dynamics away from the vertical axis admits an **exact, physical-time, real-analytic conjugacy** to a rigid two-frequency flow on a half-cylinder. This gives the maximal two-sided complete set, a common meridional period for an open family of invariant tori, a rational/irrational orbit dichotomy, an exact finite escape lifespan outside the complete set, and two different sharp escape scales at its boundary.

Put \(k=a^4-1>0\), \(\sigma=\alpha\sqrt{k}/2\), and \(u=x^2+y^2\). For \(u>0\), use
\[
X=\frac{k}{u}-a^2,\qquad Y=\frac{\sqrt{k}\,z}{u},\qquad \theta=\arg(x+iy)\pmod{2\pi}.
\]
Then the exact transformed vector field is
\[
\boxed{\dot X=-\sigma Y,\quad\dot Y=\sigma X,\quad\dot\theta=-\Omega},\qquad X>-a^2.
\]
This is an analytic diffeomorphism from \(u>0\) onto \(\{X>-a^2\}\times\mathbb S^1\), with inverse \(u=k/(X+a^2)\), \(z=\sqrt{k}Y/(X+a^2)\), and \((x,y)=\sqrt u(\cos\theta,\sin\theta)\).

Let \(\rho=\sqrt{X^2+Y^2}\). The **entire set of initial points with solutions defined for every positive and negative time** is exactly
\[
\boxed{\mathcal C=\left\{(x,y,z):2a^2(x^2+y^2)>z^2+a^4-1\right\}.}
\]
It is the union of a periodic core circle \(\rho=0\) and the invariant tori \(0<\rho<a^2\); every other initial condition blows up in finite forward and backward original physical time. For each \(0<\rho<a^2\), the meridional period is \(2\pi/|\sigma|=4\pi/(|\alpha|\sqrt{a^4-1})\), independent of \(\rho\). When \(|\Omega/\sigma|=m/n\) in lowest positive terms, every trajectory on every such torus has least period \(2\pi n/|\sigma|\); when \(\Omega/\sigma\) is irrational, every trajectory on each torus is dense and uniquely ergodic with respect to its angular Haar measure.

At \(\rho\ge a^2\), the maximal two-sided lifespan is exactly
\[
\boxed{L(\rho)=\begin{cases}2\pi/|\sigma|,&\rho=a^2,\\ 2\arccos(-a^2/\rho)/|\sigma|,&\rho>a^2.\end{cases}}
\]
In particular, \(L(\rho)\downarrow\pi/|\sigma|\) as \(\rho\to\infty\). At each forward blow-up time \(T\), writing \(\tau=T-t\downarrow0\), the Euclidean radius \(r=\sqrt{x^2+y^2}\) and the height obey
\[
\begin{aligned}
\rho>a^2:&\quad r\sim\left[\frac{k}{|\sigma|\sqrt{\rho^2-a^4}}\right]^{1/2}\tau^{-1/2},\qquad z\sim\frac{2}{\alpha\tau};\\
\rho=a^2:&\quad r\sim\frac{\sqrt{2k}}{a|\sigma|}\tau^{-1},\qquad z\sim\frac{4}{\alpha\tau}.
\end{aligned}
\]
The vertical axis \(x=y=0\) has \(\dot z=\alpha(z^2+k)/2\) and is also incomplete in both time directions, with lifespan \(\pi/|\sigma|\).

## Assumptions and scope
The parameters satisfy \(a>1\), \(\alpha\in\mathbb R\setminus\{0\}\), and \(\Omega\in\mathbb R\setminus\{0\}\). The equations, in unrescaled original time, are
\[
\begin{aligned}
\dot x&=\tfrac\alpha4 xz+\Omega y,\\
\dot y&=\tfrac\alpha4 yz-\Omega x,\\
\dot z&=\tfrac\alpha2[-a^2(x^2+y^2)+z^2+a^4-1].
\end{aligned}
\]
This is the constant-angular-speed subfamily \(f=\Omega\) of Jana's quadratic normal form, not the entire general normal form with nonconstant \(f\). No completeness conclusion is asserted when \(\alpha=0\). The torus dynamics and all escape times are with respect to the displayed physical time, with \(\theta\) interpreted modulo \(2\pi\).

## Proof
Write \(u=x^2+y^2>0\), \(p=1/u\), and \(k=a^4-1>0\). Direct calculation gives
\[
\dot u=\tfrac\alpha2 zu,\quad \dot p=-\tfrac\alpha2 zp,\quad \dot\theta=-\Omega,\quad
\dot z=\tfrac\alpha2(-a^2/p+z^2+k).
\]
Set \(X=kp-a^2\) and \(Y=\sqrt{k}\,zp\). Thus
\[
\dot X=-\tfrac{\alpha\sqrt{k}}2Y=-\sigma Y,\quad
\dot Y=\tfrac{\alpha\sqrt{k}}2(-a^2+kp)=\sigma X.
\]
The inverse formulas in the finding hold and are smooth and analytic on \(X>-a^2\); hence the conjugacy is global on the punctured-axis region, not merely a local normal form. In particular \(\rho\) is a first integral. Jana's rational integral \(H=((u-a^2)^2+z^2-1)/u^2\) is related by \(\rho^2=1+kH\).

For \(0\le\rho<a^2\), the complete harmonic circle \(X^2+Y^2=\rho^2\) lies strictly inside the allowed half-plane \(X>-a^2\). The core \(\rho=0\) corresponds to \(u=k/a^2\), \(z=0\), so it is one circle of physical period \(2\pi/|\Omega|\). At \(0<\rho<a^2\), \((\arg(X+iY),\theta)\) are torus coordinates rotating with the fixed frequencies \((\sigma,-\Omega)\). Elementary Kronecker rotation theory yields the claimed least periods and unique ergodicity. The condition \(\rho<a^2\), when squared and written in \((u,z)\), is precisely \(2a^2u>z^2+k\).

For \(\rho=a^2\), each harmonic revolution has one boundary contact \(X=-a^2,Y=0\), leaving one connected open angular interval of length \(2\pi\). For \(\rho>a^2\), the portion of the harmonic circle permitted by \(X>-a^2\) is a single arc with angular length \(2\arccos(-a^2/\rho)\). Because the angular velocity is the constant \(|\sigma|\), dividing the angle by that speed yields exactly the maximal interval length \(L(\rho)\), independent of initial phase. Its two endpoints correspond to \(u=k/(X+a^2)\to\infty\), so neither side can be continued in finite coordinates. The complement of the complete set also includes the invariant vertical axis, where the Riccati equation has all maximal intervals of length \(\pi/|\sigma|\).

For \(\rho>a^2\), at the forward endpoint, \(Y\to\operatorname{sgn}(\sigma)\sqrt{\rho^2-a^4}\) and \(X+a^2\sim |\sigma|\sqrt{\rho^2-a^4}\,\tau\). Substitution into the inverse formulas gives the first pair of asymptotics. At \(\rho=a^2\), the contact is tangent and the harmonic expansion instead gives \(X+a^2\sim a^2\sigma^2\tau^2/2\), \(Y\sim a^2\sigma\tau\); substitution gives the second pair. The expansions also apply at backward endpoints with the corresponding time direction and signs.

## Verification
The included standalone checker `checker.py`, run with Python 3, SymPy, and NumPy, checks exact symbolic Lie-derivative identities for \(X\), \(Y\), \(H\), and \(\theta\), confirms the integral relation \(\rho^2=1+kH\), tests inverse-coordinate solutions at representative parameter values, and checks the limiting lifetime formulas. It printed `QUADRATIC_TORUS_HARMONIC_CONJUGACY_CHECK_OK`. These finite numerical tests are auxiliary; the exact analytic proof above establishes the all-parameter assertions.

## Relationship to prior work
Jana's paper (first public arXiv version, 2024-01-15) gives the quadratic normal form in Corollary 4.2 and a rational first integral in Remark 4.5, and studies invariant meridians/parallels and singularities on a specified invariant torus. Those established facts are the starting point, not new claims. The novelty assessed here is the explicit global **time-preserving** harmonic conjugacy for the constant-\(f\) subfamily, the resulting exact maximal-completeness region, uniform torus rotation vector, lifespan function, and separate sharp blow-up laws. Earlier torus papers by Llibre–Medrado and Llibre–Rebollo-Perdomo address invariant meridians/parallels and limit cycles, not the stated whole-space completeness classification in the accessible material. Priority for an unindexed equivalent linearization has not been independently established.

## Limitations
The conjugacy excludes the vertical axis, which is treated separately. The boundary \(\rho=a^2\) is **not** a complete invariant torus: its solutions reach infinity in finite time. Rational versus irrational rotation statements concern the nondegenerate complete invariant tori only. The theorem makes no assertions about the general nonconstant-\(f\) quadratic family or perturbative persistence. The earlier Llibre–Medrado paper's full text was not accessible in the available sources, so equivalence beyond its stated scope remains a literature risk. No independent mathematical audit has been performed.

## References
1. S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843 (first posted 2024-01-15), Corollary 4.2, Remark 4.5, and Sections 5–6. https://arxiv.org/abs/2401.07843
2. J. Llibre and J. C. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, Bulletin des Sciences Mathématiques 135 (2011), 1–9. https://doi.org/10.1016/j.bulsci.2010.06.005
3. J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in \(\mathbb R^3\)*, Journal of Dynamics and Differential Equations 25 (2013), 777–793. https://doi.org/10.1007/s10884-013-9315-4
