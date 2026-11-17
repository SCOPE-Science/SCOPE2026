# Inverse-beta waveform and arithmetic Fourier decay in a quadratic switching center

## Finding
For the global crossing center below, the time-parametrized position is an explicit inverse-beta waveform. Its high-frequency Fourier coefficients have a two-term asymptotic with competing orders \(n^{-4}\) and \(n^{-7}\). At rational half-period fractions, one entire arithmetic progression loses the leading order, whereas at exact half-period balance every even harmonic vanishes identically. These conclusions concern the original physical time, not a reparametrization of the orbits.

Write \(A=\alpha\beta^2\), \(C=\gamma\), and \(K=(2/3)^{2/3}B(1/2,1/3)\), where \(B\) is Euler's beta function. For the orbit through \((r,0)\), set
\[
\tau_+=Kr^{-1/3}A^{-1/3},\quad \tau_-=Kr^{-1/3}C^{-1/3},\quad T=\tau_++\tau_-,\quad \theta=\tau_+/T,\quad \omega=2\pi/T.
\]
Define the normalized Fourier coefficient \(\widehat x_n=T^{-1}\int_0^T x_r(t)e^{-in\omega t}\,dt\). As the positive integer \(n\to\infty\),
\[
\boxed{\widehat x_n=-\frac{2r^2(A+C)(1-e^{-2\pi in\theta})}{T(in\omega)^4}+\frac{20r^3(A^2-C^2)(1+e^{-2\pi in\theta})}{T(in\omega)^7}+O_{\alpha,\beta,\gamma,r}(n^{-10}).}
\]
If \(\theta=m/q\) is reduced rational with \(q\ge3\), the coefficients for \(n=kq\) satisfy
\[
\lim_{k\to\infty}(kq)^7\widehat x_{kq}=\frac{40r^3(A^2-C^2)}{T(i\omega)^7}\ne0,
\]
while each nonzero residue class modulo \(q\) has a nonzero \(n^{-4}\) leading coefficient. If \(A=C\), equivalently \(\theta=1/2\), then \(x_r(t+T/2)=-x_r(t)\) and \(\widehat x_{2k}=0\) for every integer \(k\). If \(\theta\) is irrational, density of \(\{n\theta\}\) modulo one gives
\[
\liminf_{n\to\infty}n^4|\widehat x_n|=0,\qquad \limsup_{n\to\infty}n^4|\widehat x_n|=\frac{4r^2(A+C)}{T\omega^4}.
\]

## Assumptions and scope
Fix arbitrary real \(\alpha,\beta,\gamma,r>0\). Take the Carathéodory crossing solutions of the piecewise quadratic planar vector field
\[
(\dot x,\dot y)=\begin{cases}(-\alpha y^2,\beta x),&y\ge0,\\(\gamma y^2,x),&y<0.\end{cases}
\]
The right-hand side is discontinuous in its second component at the switching axis if \(\beta\ne1\), but the normal component is nonzero at each crossing \((\pm r,0)\); no sliding or ambiguous forward crossing occurs on the stated orbit. The orbit travels from \((r,0)\) to \((-r,0)\) in the upper half-plane and returns in the lower half-plane. The center and the dependence of the period on \(r\) are established prior results; only the explicit time waveform and the new Fourier conclusions are claimed here.

## Proof
**Orbit and normalized clock.** The first integrals on the two half-planes give
\[
y^3=\frac{3\beta}{2\alpha}(r^2-x^2)\quad(y\ge0),\qquad y^3=-\frac3{2\gamma}(r^2-x^2)\quad(y\le0).
\]
Substitute into \(\dot x\), integrate from \(x=r\) to \(x=-r\) and back, and change variable \(z=(r-x)/(2r)\) on the upper segment. Both normalized half-crossing times have the weight \(z^{-2/3}(1-z)^{-2/3}\). With \(Q(s)=I_s^{-1}(1/3,1/3)\), the quantile of the symmetric beta distribution (inverse in its probability argument), the exact position waveform on one full period is
\[
x_r(t)=\begin{cases}r[1-2Q(t/\tau_+)],&0\le t\le\tau_+,\\r[-1+2Q((t-\tau_+)/\tau_-)],&\tau_+\le t\le T,\end{cases}
\]
extended periodically. The beta integral yields exactly the stated \(\tau_\pm\). Strict monotonicity in each half-plane and the two switch crossings prove that \(T\) is the least physical-time period.

**Crossing jets.** On either side of a switching event, write locally \(\dot x=k y^2\), \(\dot y=m x\), with \(x(0)=R=\pm r\), \(y(0)=0\). Analytic uniqueness and the symmetry \((t,y)\mapsto(\zeta t,\zeta y)\) for cubic roots of unity \(\zeta\) show that the Taylor series of \(x\) contains only powers \(t^{3j}\). Direct substitution gives
\[
x(t)=R+\frac{km^2R^2}{3}t^3+\frac{k^2m^4R^3}{36}t^6+O(t^9).
\]
Consequently the jumps \(\Delta_j(t_*)=x^{(j)}(t_*^+)-x^{(j)}(t_*^-)\) satisfy
\[
\begin{array}{c|cc} &t_*=0&t_*=\tau_+\\ \hline
\Delta_3&-2r^2(A+C)&2r^2(A+C)\\
\Delta_6&20r^3(A^2-C^2)&20r^3(A^2-C^2)
\end{array}
\]
and all jumps at derivative orders \(0,1,2,4,5,7,8\) vanish. Piecewise analytic solutions have integrable bounded derivatives of every fixed order up to the closed switching endpoints.

**Fourier expansion and resonance.** For a piecewise analytic periodic function whose derivative jumps through order eight are as above, repeated integration by parts, or distributional differentiation, gives
\[
\widehat x_n=\frac1T\sum_{t_*\in\{0,\tau_+\}}e^{-in\omega t_*}\left[\frac{\Delta_3(t_*)}{(in\omega)^4}+\frac{\Delta_6(t_*)}{(in\omega)^7}\right]+O(n^{-10}).
\]
The remainder bound follows by retaining the order-nine jumps and integrating the piecewise tenth derivative once; it is uniform in integer \(n\) at fixed positive parameters. Substituting the jump table proves the displayed two-term formula. When \(\theta=m/q\), exact cancellation of \(1-e^{-2\pi in\theta}\) occurs precisely at \(q\mid n\). For \(q\ge3\) one has \(A\ne C\), so the second term there is nonzero. For \(\theta=1/2\), the two rescaled half-wave shapes coincide with opposite signs; their exact time-shift antisymmetry proves all even-mode zeros, not merely an asymptotic cancellation. Finally, when \(\theta\) is irrational, the phases \(e^{-2\pi in\theta}\) are dense in the unit circle and the remaining terms are \(O(n^{-7})\), proving the liminf and limsup.

## Verification
A standalone checker named `check.py` evaluates the inverse-beta waveform with SciPy, checks its half-turn symmetry in the balanced case, confirms the predicted full-time beta quantile values, and compares a discrete Fourier transform at increasing harmonics with the two-term analytical expansion for three different parameter sets. The checker reproduces the special resonant \(n^{-7}\) channel for \(\theta=1/3\) and the nonresonant \(n^{-4}\) regime. These numerical checks are diagnostic, **not** substitutes for the analytic proof above. Reproduce with `python check.py` using Python 3, NumPy and SciPy.

## Relationship to prior work
Tang, arXiv:1708.03444 (first public 2017-08-11; journal DOI 10.3934/dcds.2018082), classified the existence and global behavior of this piecewise quadratic center, established its nonisochrony, and investigated perturbative cycles. Chen–Llibre–Tang (2019), DOI 10.3934/dcdsb.2019150, gave a broader piecewise quasi-homogeneous center treatment and already supplied an exact beta-function **period** for the same quadratic system. Neither center existence nor period scaling is new here. General Fourier reconstruction results for piecewise-smooth functions, such as Batenkov–Yomdin, arXiv:1005.1884, already establish the relevance of derivative jumps to high-frequency coefficients. The claim here is the oscillator-specific inverse-beta waveform, explicit sixth-order jump contribution, and parameter-controlled rational/irrational harmonic cancellation spectrum. The named predecessors do not state these conclusions in the inspected material.

## Limitations
The estimates fix \(\alpha,\beta,\gamma,r>0\); the \(O(n^{-10})\) constant is not uniform in parameters approaching zero or infinity. The result concerns the horizontal coordinate and this particular crossing-center family, not all piecewise smooth oscillators. This provides no assertion that all exact finite-frequency Fourier coefficients are nonzero, nor a uniformly controlled transition when parameters vary with \(n\). General Fourier-jump theory contains the method of the asymptotic step; independently derived or less readily indexed oscillator-specific formulas remain a publication-priority risk. There has been no independent mathematical validation.

## References
1. Y. Tang, *Global dynamics and unfolding of planar piecewise smooth quadratic quasi-homogeneous differential systems*, arXiv:1708.03444 (2017), https://arxiv.org/abs/1708.03444; published as *Global dynamics and bifurcation of planar piecewise smooth quadratic quasi-homogeneous differential systems*, DCDS 38 (2018), 2029–2046, https://doi.org/10.3934/dcds.2018082.
2. H. Chen, J. Llibre, Y. Tang, *Centers of discontinuous piecewise smooth quasi-homogeneous polynomial differential systems*, DCDS-B 24 (2019), 6495–6509, https://doi.org/10.3934/dcdsb.2019150. Author accepted manuscript: https://ddd.uab.cat/pub/artpub/2019/221337/CheLliTan2018b_preprint.pdf.
3. D. Batenkov, Y. Yomdin, *Algebraic Fourier reconstruction of piecewise smooth functions*, arXiv:1005.1884 (2010), https://arxiv.org/abs/1005.1884.
