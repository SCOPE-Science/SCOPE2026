# Exact physical-time statistics and arrest scaling of an algebraic limit cycle

## Finding
For the polynomial oscillator of Belattar, Cheurfa, Bendjeddou and Santana (2023), the attracting algebraic oval has an exactly calculable physical-time phase law. For every \(h>0\) and \(0<w<4\), let \(\alpha=w/4\), \(\delta=\sqrt{1-\alpha^2}\), and \(\eta=\sqrt{(1-\alpha)/(1+\alpha)}\). Its least physical period and nontrivial transverse Floquet multiplier are
\[
T=\frac{2\pi}{\delta},\qquad \Lambda=\exp\left(-\frac{2\pi w}{\delta}\right).
\]
If an initial point is sampled uniformly in *physical time* along the periodic orbit, the position \(X\) has the exact density
\[
f_{h,w}(x)=\frac{\delta}{\pi\sqrt{h-x^2}\left[1-\frac{w^2x^2(h-x^2)}{4h^2}\right]},\qquad -\sqrt h<x<\sqrt h.
\]
For either of the two natural half-orbit slow-gate sectors, the gate-centered tangent phase divided by \(\eta\) has exactly the standard Cauchy law. As \(w\uparrow4\), the physical-time position law converges weakly to \(\tfrac12\delta_{-\sqrt{h/2}}+\tfrac12\delta_{\sqrt{h/2}}\), with the exact concentration statistic
\[
\mathbb E[X^2]=\frac h2,\quad
\mathbb E\left[\left(X^2-\frac h2\right)^2\right]
=\frac{h^2\delta}{4(1+\delta)}
\sim\frac{h^2}{4\sqrt2}\sqrt{4-w}.
\]
In particular, \(T\sim2\pi\sqrt2\,(4-w)^{-1/2}\), while \(-\log\Lambda\sim8\pi\sqrt2\,(4-w)^{-1/2}\). These temporal and metric laws refine, without replacing, the known algebraic-oval and phase-portrait classification.

## Assumptions and scope
The equations are the exact autonomous planar polynomial system from [1], not an arbitrary vector field with a similar oval. Write \(\dot x=y\), \(\dot y=f_3(x)y^3+f_2(x)y^2+f_1(x)y+f_0(x)\), with real parameters \(h>0\) and \(0<w<4\), where
\[
\begin{aligned}
f_3(x)&=-\frac w{2h},\\
f_2(x)&=-\frac{3w^2(x^3-hx)}{4h^2},\\
f_1(x)&=-\frac38\left(\frac wh\right)^3x^6+\frac{3w^3}{4h^2}x^4-\frac{w(3w^2+20)}{8h}x^2+w,\\
f_0(x)&=-\frac{x}{16h^4}(w^2x^4-hw^2x^2+4h^2)(w^2x^4-2hw^2x^2+h^2w^2+4h^2).
\end{aligned}
\]
The known invariant oval is
\[
\Gamma_{h,w}=\left\{(x,y):x^2+\left(y+\frac{w}{2h}(x^2-h)x\right)^2=h\right\}.
\]
For \(0<w<4\), [1, Theorem 1.1] proves this is the unique attracting hyperbolic limit cycle. All distributions below are for the uniform-*physical-time* probability measure on that cycle, not uniform arclength, uniform angle, or a basin distribution. The boundary value \(w=4\) itself is a nonperiodic degeneracy; asymptotics use \(w\uparrow4\) from below.

## Proof
**1. Algebraic invariant and normal multiplier.** Set \(c(x)=w(x^2-h)x/(2h)\), \(R=x^2+(y+c(x))^2\), and \(F=R-h\). Direct polynomial differentiation using the displayed equations yields
\[
\dot R=-\frac wh R(R-h),\qquad
\dot F=-wF\left(1+\frac Fh\right).
\]
The first identity is also equivalent to the nonautonomous first integral in [1]. On \(F=0\), the normal variational equation in the transverse coordinate \(F\) is \(\dot{\Delta F}=-w\Delta F\). Once the least period is known, its exact nontrivial Floquet multiplier is \(\exp(-wT)\). Because \(\nabla F\ne0\) along the regular oval, this is the planar transverse multiplier in any smooth nonvanishing normal coordinate.

**2. Original-time angular law and period.** Parameterize \(\Gamma_{h,w}\) by
\[
x=\sqrt h\cos\theta,\qquad
y=\sqrt h\sin\theta-\frac{w}{2h}(x^2-h)x
=\sqrt h\sin\theta+\frac w2\sqrt h\cos\theta\sin^2\theta.
\]
Using the *original* equation \(\dot x=y\), division by \(-\sqrt h\sin\theta\) away from the two zeros, followed by continuity, gives
\[
\dot\theta=-\left(1+\frac w4\sin2\theta\right)=-(1+\alpha\sin2\theta).
\]
This is strictly negative for \(0<\alpha<1\), so one full turn is precisely one minimal orbit. The standard tangent substitution (or a direct contour integral) gives
\[
T=\int_0^{2\pi}\frac{d\theta}{1+\alpha\sin2\theta}
=\frac{2\pi}{\sqrt{1-\alpha^2}}.
\]
Inserting \(T\) into Step 1 proves the multiplier. Since \(1-\alpha^2\sim(4-w)/2\), both claimed sharp boundary equivalents follow.

**3. Physical-time angle law, tangent Cauchy identity and position density.** Uniform physical time gives the normalized phase density
\[
\rho_{\alpha}(\theta)=\frac{\delta}{2\pi(1+\alpha\sin2\theta)}.
\]
Define \(\theta_1=3\pi/4\), \(\theta_2=7\pi/4\). Partition the phase circle into the two semicircles \(I_j=(\theta_j-\pi/2,\theta_j+\pi/2)\pmod{2\pi}\), assigning boundary points arbitrarily (they have zero measure). The law is invariant under \(\theta\mapsto\theta+\pi\), so \(\Pr(\theta\in I_j)=1/2\). On \(I_j\), write \(u=\theta-\theta_j\in(-\pi/2,\pi/2)\) and \(z=\tan u/\eta\). Since \(\sin2\theta=-\cos2u\), the change of variables \(t=\tan u\) gives
\[
\frac{\delta}{2\pi}\frac{du}{1-\alpha\cos2u}
=\frac{\delta}{2\pi}\frac{dt}{(1-\alpha)+(1+\alpha)t^2}
=\frac{\eta}{2\pi}\frac{dt}{\eta^2+t^2}.
\]
After conditioning on either \(I_j\), \(z\) therefore has the exact density \(1/[\pi(1+z^2)]\) on the whole real line, for **every** \(0<w<4\). To obtain the marginal of \(X=\sqrt h\cos\theta\), sum the two inverse branches \(\theta=\pm\arccos(x/\sqrt h)\); their opposite \(\sin2\theta\) values cancel the linear term and yield the stated \(f_{h,w}\). This density is normalized because it is a pushforward of \(\rho_\alpha\), and it is zero outside \([-\sqrt h,\sqrt h]\).

**4. Exact squared-position concentration.** Put \(r=\alpha/(1+\delta)\in(0,1)\). In each slow-gate sector the normalized phase density has the ordinary Poisson-kernel expansion
\[
\frac{\delta}{1-\alpha\cos2u}
=1+2\sum_{n\ge1}r^n\cos(2nu).
\]
This is an absolutely convergent series for fixed \(\alpha<1\). Consequently, \(\mathbb E[\cos2\theta]=0\) and \(\mathbb E[\cos4\theta]=-r^2\), since the gate centers have \(2\theta_j\equiv3\pi/2\pmod{2\pi}\). With \(X^2=h(1+\cos2\theta)/2\),
\[
\mathbb E[X^2]=h/2,\qquad
\mathbb E[(X^2-h/2)^2]=\frac{h^2}{8}(1-r^2)
=\frac{h^2\delta}{4(1+\delta)}.
\]
The exact Cauchy gate identity represents \(\theta\) conditional on \(I_j\) as \(\theta_j+\arctan(\eta Z)\), with \(Z\) a standard Cauchy random variable. As \(\eta\downarrow0\), each conditional angle converges in probability to its gate center, and its position converges to \(\sqrt h\cos\theta_j\). Averaging the two equal masses proves the asserted weak two-atom limit. More sharply, conditional on gate \(I_j\), \((X-\sqrt h\cos\theta_j)/(\eta\sqrt{h/2})\) converges in distribution to a standard Cauchy variable (possibly sign-reversed, which has the same law). The leading concentration constant follows from \(\delta\sim\sqrt{(4-w)/2}\).

## Verification
`CHECK.py` reproduces the defining polynomial vector field and verifies symbolically that \(\dot R=-wR(R-h)/h\) and that the phase-parameterized orbit satisfies **both** original differential equations. At four parameter values it independently integrates the original-time phase density and verifies normalization, mean square, exact variance, period, and the gate-local Cauchy density. Run with Python 3, SymPy and SciPy using `python CHECK.py`; the analytical all-parameter identities above, not these finite tests, prove the theorem.

## Relationship to prior work
Belattar et al. [1] establish the explicit polynomial system, the invariant oval, its nonautonomous first integral, stability, and the global phase-portrait regimes. Those are not claimed as new. The classical Adler phase-drift equation [2] already supports familiar tangent-integration and Poisson-kernel calculations in an abstract angular normal form. What is supplied here is the exact *identification* of original-time phase drift and its specific Euclidean coordinate pushforward in the algebraic polynomial oscillator, including the parameter-dependent physical-time squared-position concentration and exact transverse multiplier. The phase law and Cauchy tangent representation are equivalent formulations rather than separate independent novelties. Similar Cauchy slow-gate mechanisms in other dynamical systems do not determine this system's coefficients or physical-coordinate law.

## Limitations
The formulas apply to the specific Belattar et al. polynomial family and the unique orbit with \(h>0\), \(0<w<4\); they are not general statements for all algebraic limit cycles or trajectories in the basin. The Cauchy tangent transform is a standard distributional identity once the Adler-type phase reduction has been obtained; mathematical priority therefore rests on the system-specific reduction and complete quantitative profile, not on inventing a new distribution. At \(w=4\) the curve includes equilibria, and there is no finite least period. We do not claim independence of a mathematical review, nor rule out equivalent formulas in unindexed literature.

## References
[1] M. Belattar, R. Cheurfa, A. Bendjeddou, P. Santana, “A class of nonlinear oscillators with non-autonomous first integrals and algebraic limit cycles,” *Electronic Journal of Qualitative Theory of Differential Equations* 2023, No. 50, pp. 1–13; appeared 2023-12-14. DOI: 10.14232/ejqtde.2023.1.50. Full text: https://www.math.u-szeged.hu/ejqtde/p10493.pdf .

[2] R. Adler, “A Study of Locking Phenomena in Oscillators,” *Proceedings of the IRE* **34** (1946), pp. 351–357. DOI: 10.1109/JRPROC.1946.229930. Abstract and bibliographic record: https://ieeexplore.ieee.org/document/1697085/ .
