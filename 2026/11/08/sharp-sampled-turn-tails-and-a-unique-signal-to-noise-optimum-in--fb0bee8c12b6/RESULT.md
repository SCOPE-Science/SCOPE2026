# Sharp sampled-turn tails and a unique signal-to-noise optimum in the Brownian gyrator

## Finding

A stationary two-temperature Brownian gyrator has an observable that differs from the unbounded finite-difference angular velocity: the signed *principal turn* between two sampled position vectors. For the model and normalization below, let \(\Theta_h\in(-\pi,\pi]\) be this turn over a sampling interval \(h>0\), and write \(\Sigma\) for the stationary positional covariance, \(S=T_x+T_y\), and \(\Delta=T_x-T_y\).

For every fixed \(0<\alpha<\pi\), the two signed macroscopic-turn probabilities have the same first-order coefficient:
\[
\lim_{h\downarrow0}\frac{\Pr(\Theta_h>\alpha)}h
=\lim_{h\downarrow0}\frac{\Pr(\Theta_h<-\alpha)}h
=\frac{S}{2\pi\sqrt{\det\Sigma}}\,H(\alpha),
\qquad H(\alpha)=\frac{\pi-\alpha+\sin\alpha\cos\alpha}{2\sin^2\alpha}.
\]
This is an explicit *large-turn profile*, not an assertion that the full angular distribution is symmetric: its signed mean is generally nonzero.

The small-sampling angular moments have a sharp transition at exponent two. For \(0<p<2\),
\[
\lim_{h\downarrow0}h^{-p/2}\mathbb E|\Theta_h|^p
=\mathbb E\left|\frac{X\sqrt{2T_y}\,G_y-Y\sqrt{2T_x}\,G_x}{X^2+Y^2}\right|^p,
\]
where \((X,Y)\sim N(0,\Sigma)\), and \(G_x,G_y\) are independent standard normal variables independent of \((X,Y)\). At \(p=2\),
\[
\lim_{h\downarrow0}\frac{\operatorname{Var}(\Theta_h)}{h\log(1/h)}
=C(u)=\frac{S}{2\sqrt{\det\Sigma}}
=\frac{S\sqrt{1-u^2}}{\sqrt{4T_xT_y+u^2\Delta^2}}.
\]
For every \(p>2\),
\[
\lim_{h\downarrow0}\frac{\mathbb E|\Theta_h|^p}{h}
=\frac{S}{\pi\sqrt{\det\Sigma}}
\int_0^\pi \alpha^p
\frac{(\pi-\alpha)\cos\alpha+\sin\alpha}{\sin^3\alpha}\,d\alpha.
\]
The improper integral is finite exactly for \(p>2\) in this expression.

The signed mean has the known instantaneous gyrator rotation rate:
\[
\lim_{h\downarrow0}\frac{\mathbb E\Theta_h}{h}
=\omega(u)=\frac{u\Delta}{2\sqrt{\det\Sigma}}.
\]
Consequently, for unequal bath temperatures, the precisely defined fine-sampling mean-square signal-to-variance prefactor is
\[
\mathcal R(u):=\lim_{h\downarrow0}\frac{\log(1/h)}h
\frac{(\mathbb E\Theta_h)^2}{\operatorname{Var}(\Theta_h)}
=\frac{\Delta^2}{S}\frac{u^2\sqrt{1-u^2}}{\sqrt{4T_xT_y+u^2\Delta^2}}.
\]
It is strictly maximized over \(0<|u|<1\) at the unique value \(u^2=y_*\in(1/2,2/3)\) solving
\[
2\Delta^2y_*^2+(12T_xT_y-\Delta^2)y_*-8T_xT_y=0.
\]
Equivalently, with \(A=4T_xT_y\) and \(B=\Delta^2>0\),
\[
y_*=\frac{B-3A+\sqrt{(B-3A)^2+16AB}}{4B}.
\]
Both signs of \(u\) attain the same signal-to-variance optimum; the signed mean changes sign. If \(\Delta=0\), the signal vanishes identically and there is no unique signal-to-noise optimizer.

## Assumptions and scope

Let \(T_x,T_y>0\), \(-1<u<1\), and let independent standard Brownian motions \(B_x,B_y\) drive the stationary diffusion
\[
dX_t=(-X_t+uY_t)\,dt+\sqrt{2T_x}\,dB_x(t),\quad
dY_t=(uX_t-Y_t)\,dt+\sqrt{2T_y}\,dB_y(t).
\]
This theorem concerns the unique stationary law and finite sampled principal turns, not continuously unwrapped windings or the rational increment \((X_t\Delta Y-Y_t\Delta X)/(h(X_t^2+Y_t^2))\). Set \(Z_t=(X_t,Y_t)\),
\[
\Theta_h=\operatorname{atan2}(X_tY_{t+h}-Y_tX_{t+h},X_tX_{t+h}+Y_tY_{t+h}).
\]
Gaussian nondegeneracy makes this defined almost surely. The branch is \((-\pi,\pi]\); the probability of the branch endpoints is zero. Limits are for fixed physical parameters and \(h\downarrow0\), without simultaneously taking a temperature or singular-coupling limit.

## Proof

**1. Stationary covariance and density at the origin.** Put \(M=\bigl(\begin{smallmatrix}-1&u\\u&-1\end{smallmatrix}\bigr)\) and \(D=\operatorname{diag}(T_x,T_y)\). The stable drift and positive diffusion give the unique centered invariant Gaussian \(N(0,\Sigma)\) determined by \(M\Sigma+\Sigma M+2D=0\). Direct elimination gives
\[
\Sigma_{12}=\frac{uS}{2(1-u^2)},\quad
\Sigma_{11}=T_x+u\Sigma_{12},\quad
\Sigma_{22}=T_y+u\Sigma_{12},\quad
\det\Sigma=\frac{4T_xT_y+u^2\Delta^2}{4(1-u^2)}.
\]
Its smooth density is \(\rho(z)\) with \(\rho(0)=\rho_0=(2\pi\sqrt{\det\Sigma})^{-1}\).

**2. Macroscopic turns as a chord-angle geometry.** Conditional on \(Z_t=z\), the exact transition is \(Z_{t+h}=e^{Mh}z+\eta_h\), with centered Gaussian \(\eta_h\) independent of \(z\), covariance \(\Sigma-e^{Mh}\Sigma e^{Mh}\). The covariance is \(2hD+O(h^2)\). The contribution to an event \(|\Theta_h|>\alpha\) comes from \(|z|=O(\sqrt h)\). Substitute \(z=\sqrt h\,w\) and \(\eta_h=\sqrt h\,V_h\); \(V_h\) converges to \(V\sim N(0,2D)\). The drift correction \((e^{Mh}-I)w\) is negligible in this rescaled integral.

For a fixed nonzero chord \(v\) of length \(\ell\), elementary inscribed-angle geometry gives the area on **each** side of the chord for which the principal angular turn exceeds \(\alpha\) in the corresponding sign:
\[
A_\alpha(\ell)=\frac{\ell^2}{4\sin^2\alpha}
(\pi-\alpha+\sin\alpha\cos\alpha)
=\frac{\ell^2}{2}H(\alpha).
\]
This follows by subtracting the appropriate circular sector/triangle from the circle of radius \(\ell/(2\sin\alpha)\) passing through both chord endpoints; the formula also covers major segments for \(\alpha<\pi/2\). A sign corresponds to one of the two mirror-related sides and therefore has the same area. Integrating first over \(w\), then \(V\), yields \(\rho_0\mathbb E(|V|^2)H(\alpha)/2=\rho_0 S H(\alpha)\), since \(\mathbb E|V|^2=2S\). Gaussian tails and a partition at \(|z|=R\sqrt h\) justify the limit by dominated convergence followed by \(R\to\infty\). For the outer region, the event requires a Gaussian displacement of order \(|z|\), giving a bound \(Ch e^{-cR^2}\) after integration. This proves both signed limits.

**3. Moment transition.** Differentiating the angle tail profile gives
\[
-H'(\alpha)=g(\alpha)=
\frac{(\pi-\alpha)\cos\alpha+\sin\alpha}{\sin^3\alpha},\qquad
H(\alpha)\sim\frac\pi{2\alpha^2}\quad(\alpha\downarrow0).
\]
A uniform bound \(\Pr(|\Theta_h|>\alpha)\le C\min\{1,h/\alpha^2\}\) follows from the same chord-area argument plus the uniformly \(O(h)\) angular distortion of \(e^{Mh}\), which is positive definite for sufficiently small \(h\). Layer-cake integration \(\mathbb E|\Theta_h|^p=p\int_0^\pi \alpha^{p-1}\Pr(|\Theta_h|>\alpha)d\alpha\), followed by dominated convergence for \(p>2\), and integration by parts gives the displayed \(g\)-integral. The boundary term vanishes since \(p>2\).

For \(0<p<2\), at each nonzero \(z=(x,y)\), the conditional \(h^{-1/2}\Theta_h\) tends to \((x\sqrt{2T_y}G_y-y\sqrt{2T_x}G_x)/(x^2+y^2)\). A conditional \(p\)-moment bound proportional to \(1+|z|^{-p}\) holds uniformly for small \(h\); its integrability against the two-dimensional stationary Gaussian follows exactly from \(p<2\). This proves convergence of the absolute moments.

At the borderline \(p=2\), write \(z=r(\cos\varphi,\sin\varphi)\) and integrate over the intermediate annulus \(L\sqrt h\le r\le\varepsilon\). Conditional angle linearization, valid uniformly after choosing \(L\) large, gives
\[
\mathbb E(\Theta_h^2\mid z)=
\frac{2h}{r^2}(T_y\cos^2\varphi+T_x\sin^2\varphi)
+O\left(h^2+\frac{h^{3/2}}{r^3}+\frac{h^2}{r^4}\right).
\]
Its stationary integral has the leading term \(2\pi\rho_0 S h\log(\varepsilon/(L\sqrt h))=\pi\rho_0 S h\log(1/h)+O(h)\). The inner disk contributes \(O(L^2h)\) since turns are bounded; the outer region contributes \(O_\varepsilon(h)\). For fixed \(L,\varepsilon\), errors are \(O_L(h)\); allowing \(L\) large and \(\varepsilon\) small gives the claimed coefficient. The mean is \(O(h)\) as shown next, so subtracting its square does not alter the leading variance.

**4. Signed mean and optimum.** The stationary probability current is
\[
j(z)=(Mz-D\nabla\log\rho(z))\rho(z)
=\frac{u\Delta}{2}\,J\Sigma^{-1}z\,\rho(z),\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
The current's angular-flux integral (or antisymmetrizing the two-time Gaussian law under interchange of endpoints) gives the short-lag signed turn rate
\[
\lim_{h\downarrow0}h^{-1}\mathbb E\Theta_h
=\int\frac{z_1j_2(z)-z_2j_1(z)}{|z|^2}\,dz
=\frac{u\Delta}{2}\int\frac{z^T\Sigma^{-1}z}{|z|^2}\rho(z)\,dz.
\]
The inner disk contributes no anomalous signed order-\(h\) term: under \(z=\sqrt h\,w\) its leading angle law is reflection-symmetric for each fixed noise displacement, and the first antisymmetric correction is \(o(h)\) after integrating over \(w\); outside this disk the current identity is justified by smooth test-function approximation. In polar coordinates the remaining integral equals \(2\pi\rho_0=1/\sqrt{\det\Sigma}\), since \(\int_0^\infty r a(\varphi)e^{-a(\varphi)r^2/2}dr=1\), with \(a(\varphi)=e_\varphi^T\Sigma^{-1}e_\varphi\). This yields \(\omega(u)\).

Combining \(\omega(u)\) and \(C(u)\) proves the displayed signal-to-variance limit. Let \(y=u^2\), \(A=4T_xT_y>0\), \(B=\Delta^2>0\). Ignoring a positive constant, maximize \(F(y)=y\sqrt{1-y}/\sqrt{A+By}\) for \(0<y<1\). Its logarithmic derivative has the sign of the strictly concave quadratic \(P(y)=2A+(B-3A)y-2By^2\). We have \(P(0)>0\), \(P(1)<0\), and the product of its roots is negative. Thus exactly one root lies in \((0,1)\); the endpoint values of \(F\) vanish, so it is the unique global optimizer. Moreover \(P(1/2)=A/2>0\) and \(P(2/3)=-2B/9<0\), proving \(1/2<y_*<2/3\). The quadratic formula gives the asserted expression. For \(\Delta=0\) the signed signal is identically zero.

## Verification

The standalone `checker.py` evaluates the Lyapunov covariance identity, the elementary chord area and its derivative, the exact optimizer polynomial and uniqueness inequalities, positive improper moment integrals, and short-lag full-Gaussian transition simulations at multiple sampling intervals. It compares the signed macroscopic-turn rate, moment scaling and drift to independently generated conditional Gaussian transitions. Execute `python3 checker.py` with Python, NumPy and SciPy. The numerical checks are diagnostics only: exact symbolic algebra and the proof above establish the asserted continuum limits and optimizer, not finite samples.

For example, \(T_x=1\), \(T_y=5\) gives \(A=20\), \(B=16\), and \(y_*=5/8\), so the signal-to-variance optimal coupling magnitude is \(|u|=\sqrt{5/8}=0.790569\ldots\). At \(u=1/2\), \(\det\Sigma=8\), \(C=3/\sqrt8=1.060660\ldots\), \(\omega=-1/\sqrt8=-0.353553\ldots\), and each signed tail at \(\alpha=\pi/2\) has coefficient \(3/(4\sqrt8)=0.265165\ldots\).

## Relationship to prior work

Viot, Argun, Volpe, Imparato, Rondoni and Oshanin (2023) derive the stationary Brownian-gyrator angular-velocity law under a rational finite difference and its \(|\mathcal W|^{-3}\) tails, and give the known mean rotation rate; they also note that actual measured angle differences are bounded at any finite sampling interval. Their mean rate and formal angular-velocity tail coefficient are *prior results*, not new findings here. In particular, the logarithmic variance coefficient is compatible with their high-velocity tail; its contribution here is the rigorous finite-principal-angle interpretation.

Le Doussal, Etzioni and Horovitz (2009) study centered *rotationally invariant* Gaussian winding processes, and earlier work of Vakeroudis concerns the *continuously unwrapped* isotropic Ornstein–Uhlenbeck winding. Those settings do not specify the anisotropic, nonequilibrium, two-temperature principal-turn large-angle profile or a coupling optimum. General complex-Gaussian phase-difference literature is also relevant, but the inspected accessible works concern proper scattering or neural signal models rather than the stated nonreversible Brownian-gyrator singular small-lag regime. The particular asymptotic formulas may admit other derivations from general Gaussian angular statistics; publication priority beyond the inspected material is not certified.

## Limitations

All formulas are single-lag stationary ensemble statements and do not establish independence between sampled turns or a trajectory-level central limit theorem. A bounded principal turn is not an unwrapped winding number, which can have very different moment properties. The optimality statement is solely for the displayed leading *mean-square signal divided by single-increment variance* under fixed unequal temperatures; it is not a claim of maximum thermodynamic work, energy efficiency or long-time estimation precision. Bounds and limits are not uniform as \(|u|\uparrow1\) or a bath temperature approaches zero. Numerical trials corroborate rather than replace the proofs. The cited Gaussian-phase literature limits any strong priority assertion.

## References

1. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248, first posted 2023-07-11. https://arxiv.org/abs/2307.05248
2. P. Le Doussal, Y. Etzioni, B. Horovitz, *Winding of planar gaussian processes*, arXiv:0904.0582, first posted 2009-04-03. https://arxiv.org/abs/0904.0582
3. S. Vakeroudis, *On hitting times of the winding processes of planar Brownian motion and of Ornstein-Uhlenbeck processes, via Bougerol's identity*, arXiv:1007.4648, 2010. https://arxiv.org/abs/1007.4648
4. S. Afifi, R. Dusséaux, *Multilook phase difference distribution for slightly rough boundary layered ground*, IET Microwaves, Antennas & Propagation (2021), https://doi.org/10.1049/mia2.12071
5. K. N. Urban, H. Bong, J. Orellana, R. E. Kass, *Oscillating neural circuits: Phase, amplitude, and the complex normal distribution*, Canadian Journal of Statistics (2023), https://doi.org/10.1002/cjs.11790
