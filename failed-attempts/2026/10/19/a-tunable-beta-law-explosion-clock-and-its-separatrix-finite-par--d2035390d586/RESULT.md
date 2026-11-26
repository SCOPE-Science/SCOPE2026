# A tunable beta-law explosion clock and its separatrix finite part in quadratic mass-action kinetics

## Finding

In the natural three-reaction quadratic kinetic family
\[
2X\longrightarrow X,\qquad X+Y\longrightarrow\varnothing,\qquad 2Y\longrightarrow3Y,
\]
with respective positive mass-action rate parameters \(a,b,c\), the deterministic concentration equations are
\[
\dot x=-a x^2-bxy,\qquad \dot y=c y^2-bxy. \tag{1}
\]
Assume \(b>a>0\) and \(c>0\). Write
\[
k=b+c,\quad d=b-a,\quad w_* =d/k,\quad P=a/d,\quad
\phi=c/k,\quad \nu=P+b/k=\frac{b^2+ac}{(b+c)(b-a)},\quad
\gamma=a+bw_*=k\nu w_*.
\]
All these parameters are strictly positive, and \(0<\phi<1\). The ray \(y=w_*x\) is invariant. Every positive initial condition lies in exactly one of the following regimes:

**Below the ray:** If \(0<w_0=y_0/x_0<w_*\), the solution exists for all \(t\geq0\), tends to the origin, and satisfies
\[
\lim_{t\to\infty}t x(t)=a^{-1},\qquad
\lim_{t\to\infty}t^{b/a}y(t)
= a^{-b/a}\left(\frac{w_*^\nu}{H_-}\right)^{1/P}>0,
\quad H_-=\frac{x_0(w_*-w_0)^\nu}{w_0^P}.
\tag{2}
\]

**On the ray:** If \(w_0=w_*\), the solution is explicitly
\[
x(t)=\frac{x_0}{1+\gamma x_0t},\qquad y(t)=w_*x(t). \tag{3}
\]

**Above the ray:** If \(w_0>w_*\), the maximal forward lifetime \(T\) is finite. For the lower incomplete beta integral \(B_z(u,v)=\int_0^z s^{u-1}(1-s)^{v-1}\,ds\),
\[
\boxed{\displaystyle T=\frac{w_*^{-\phi}w_0^P}{k x_0(w_0-w_*)^\nu}
B_{w_*/w_0}(\phi,\nu).} \tag{4}
\]
Set \(H_+=x_0(w_0-w_*)^\nu/w_0^P\). The solution has the sharp endpoint asymptotics
\[
\boxed{\displaystyle\lim_{t\uparrow T}(T-t)y(t)=\frac1c,\qquad
\lim_{t\uparrow T}\frac{x(t)}{(T-t)^{b/c}}
=c^{b/c}H_+^{(b+c)/c}.} \tag{5}
\]

**Critical explosion latency and finite part:** Fix \(x_0>0\) and vary \(w_0=w_*+\delta\), with \(\delta\downarrow0\). Then
\[
\boxed{\displaystyle T\sim
\frac{w_*^{\nu-1}B(\phi,\nu)}{k x_0}\,\delta^{-\nu},}\qquad
B(u,v)=\frac{\Gamma(u)\Gamma(v)}{\Gamma(u+v)}, \tag{6}
\]
and the stronger, finite-part identity is
\[
\boxed{\displaystyle
T-\frac{w_*^{-\phi}w_0^P B(\phi,\nu)}{k x_0\delta^\nu}
=-\frac{1}{\gamma x_0}+O_{a,b,c}\!\left(\frac\delta{x_0}\right).} \tag{7}
\]
The finite constant is precisely minus the characteristic time \((\gamma x_0)^{-1}\) in the on-ray solution (3). The positive exponent \(\nu\) is continuously tunable over the whole interval \((0,\infty)\) through the three rate constants.

In the source's concrete rates \((a,b,c)=(1,2,1)\), the exponent is \(\nu=5/3\), the ray is \(y=x/3\), and when \(\eta=y_0-x_0/3\downarrow0\),
\[
T\sim\frac{4\pi}{\sqrt3\,3^{8/3}}x_0^{2/3}\eta^{-5/3},
\quad \lim_{t\uparrow T}\frac{x(t)}{(T-t)^2}
=\frac{x_0(3y_0-x_0)^5}{243y_0^3}. \tag{8}
\]

## Assumptions and scope

Equations (1) are polynomial vector fields on the strictly positive quadrant, with physical mass-action time, and ordinary maximal classical solutions. The three reactions have positive rates \(a,b,c\) and satisfy the strict inequality \(b>a\). The theorem covers **every** \(x_0,y_0>0\) under these hypotheses, and not the boundary axes, stochastic reaction counts, diffusion, or the complementary parameter regime \(b\leq a\). The exponent and finite-part claims keep \(a,b,c,x_0\) fixed as \(\delta\downarrow0\); no uniformity in rates is asserted. Exactly at \(w_0=w_*\), expression (4) is not used.

## Proof

**Projective dynamics and integral.** Positivity follows from the factors \(x\) and \(y\) in (1) while the solution remains finite. Set \(w=y/x\). Direct differentiation yields
\[
\dot x=-x^2(a+bw),\qquad \dot w=kxw(w-w_*). \tag{9}
\]
For either open side of the invariant ray, taking the derivative of \(\log x+\nu\log|w-w_*|-P\log w\) and using \(k(\nu-P)=b\) and \(kPw_*=a\) gives zero. Therefore
\[
x(w)=H_\pm\frac{w^P}{|w-w_*|^\nu},\quad
H_\pm=\frac{x_0|w_0-w_*|^\nu}{w_0^P}. \tag{10}
\]
The sign of \(\dot w\) is the sign of \(w-w_*\), so the three regions are forward invariant and no crossings or interior turns of \(w\) occur.

**Below and on the ray.** If \(w_0<w_*\), then \(w\) decreases, \(x\) decreases, and \(x\) remains positive for finite times because \(\dot x\geq-(a+bw_0)x^2\). Thus the solution is global. Moreover \(x(t)\leq x_0/(1+a x_0t)\to0\). Formula (10) forces \(w\to0\), as \(w\) would otherwise be bounded away from zero while \(x\to0\). Since \((x^{-1})'=a+bw\to a\), Cesàro averaging gives \(t x(t)\to1/a\). Formula (10) near \(w=0\) gives \(w\sim(w_*^\nu x/H_-)^{1/P}\), hence (2) because \(1+1/P=b/a\). If \(w_0=w_*\), (9) reduces to \(\dot x=-\gamma x^2\), giving (3).

**Finite-time explosion and beta clock.** If \(w_0>w_*\), then \(w\) increases and (10) gives
\[
\frac{dt}{dw}=\frac{1}{kH_+}\,w^{-P-1}(w-w_*)^{\nu-1}. \tag{11}
\]
As \(w\to\infty\), the integrand is asymptotic to a positive multiple of \(w^{-1-\phi}\), whose tail is integrable since \(\phi>0\). Integration from \(w_0\) to infinity gives a finite lifetime; \(w\) cannot stop at any finite larger value by uniqueness and (9). With the substitution \(s=w_*/w\), (11) becomes \(w_*^{-\phi}(kH_+)^{-1}s^{\phi-1}(1-s)^{\nu-1}ds\), yielding (4). Equation (10) also implies \(x\sim H_+w^{-b/k}\), \(y\sim H_+w^{c/k}\), so \(x\to0\) and \(y\to\infty\) at finite \(T\). Since \((y^{-1})'=-c+b/w\to-c\), integration up to \(T\) gives \(y(t)(T-t)\to1/c\). Also \(xy^{b/c}\to H_+^{k/c}\), proving both limits in (5).

**Singular scale and finite part.** Put \(\delta=w_0-w_*>0\), \(z=w_*/w_0=1-\delta/w_0\). Because \(0<\phi<1\), the beta tail is
\[
B(\phi,\nu)-B_z(\phi,\nu)
=\frac{(1-z)^\nu}{\nu}+O((1-z)^{\nu+1}). \tag{12}
\]
Substituting into (4) gives (7), since
\[
\frac{w_*^{-\phi}w_0^P}{k x_0\delta^\nu}\frac{(\delta/w_0)^\nu}{\nu}
=\frac{w_*^{-\phi}w_0^{-b/k}}{k\nu x_0}
=\frac1{k\nu w_*x_0}+O(\delta/x_0)
=\frac1{\gamma x_0}+O(\delta/x_0).
\]
Its dominant positive term gives (6), using \(P-\phi=\nu-1\). For \((a,b,c)=(1,2,1)\), \(B(1/3,5/3)=4\pi/(3\sqrt3)\), proving (8); its last coefficient is (5) rewritten through \(H_+\). Finally, for fixed \(b>0\), \(\nu=a/(b-a)+b/(b+c)\) is continuous as \((a,c)\) ranges over \((0,b)\times(0,\infty)\). Its attainable values approach zero when \(a\downarrow0,c\to\infty\), and are unbounded when \(a\uparrow b\). By connectedness, every strictly positive value is attained.

## Verification

The standalone standard-library program `verify.py` checks, for five distinct positive rate triples including both \(\nu<1\) and \(\nu>1\), the rational conservation/differential identities, the beta-quadrature transformation against independent Simpson quadrature, and stable evaluations of the normalized finite-part correction. It additionally checks the source-rate coefficient \(4\pi/(\sqrt3\,3^{8/3})\). Running the script in the package yields `VERIFIED 51 finite rational/analytic/numerical diagnostics`. These finite diagnostics support but do not prove the universal claims, which follow from the preceding exact analysis.

## Relationship to prior work

Yeung and Erban [1, §2, Example 2.2] identify the invariant ray and give a first integral for the special rate choice \((a,b,c)=(1,2,1)\), as part of a qualitative classification of highly degenerate chemical equilibria. This geometric result and the single-model first integral are prior work; they do not state a physical-time incomplete-beta lifetime across positive rate ratios, a freely tunable critical exponent, or the finite-part identity (7). The broader directional blow-up treatment [2, §2.1–2.2] treats an illustrative, different-sign quadratic flow and general time reparametrizations, not these reaction-rate-dependent original-time formulas. The quadratic Lotka–Volterra orbital-linearization work [3] concerns neighborhoods of equilibria with nonzero hyperbolic eigenvalues, unlike the present zero-Jacobian kinetic origin. A general classical homogeneous-ODE formula may imply parts of the derivation; exact priority beyond the checked literature remains a limitation.

## Limitations

The result concerns deterministic mass-action trajectories, not finite molecule stochastic effects or physically regularized dynamics near blow-up. The exact clock and exponents are valid only for \(a,c>0\) and \(b>a\). The finite part is defined by subtracting the **full** singular beta profile with the varying \(w_0^P\) factor; replacing it by only the leading constant multiple of \(\delta^{-\nu}\) generally changes the subleading behavior. There is no assertion of uniformity as the reaction-rate parameters approach their boundaries, nor any independent mathematical or bibliographic audit.

## References

[1] N. Yeung and R. Erban, *Classification of strongly non-hyperbolic critical points of planar second-order chemical reaction systems*, arXiv:2610.06130v1, posted 2026-10-05, §2 Example 2.2, https://arxiv.org/html/2610.06130v1 .

[2] *Blowing-Up Asymptotically Autonomous Planar Vector Fields: Infinite Delay Equations and Invariant Manifolds*, Journal of Dynamics and Differential Equations, https://doi.org/10.1007/s10884-025-10423-9 , §§2.1–2.2.

[3] J. Giné and S. Maza, *Orbital Linearization in the Quadratic Lotka–Volterra Systems Around Singular Points Via Lie Symmetries*, Journal of Nonlinear Mathematical Physics 16 (2009), 455–464, https://doi.org/10.1142/S1402925109000480 .
