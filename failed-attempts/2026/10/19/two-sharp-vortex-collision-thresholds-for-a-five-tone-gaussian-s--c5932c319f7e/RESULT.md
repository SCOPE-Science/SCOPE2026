# Two sharp vortex-collision thresholds for a five-tone Gaussian spectrogram

## Finding
Let \(\Delta>0\), \(g(t)=e^{-\pi t^2}\), and
\[
f_\Delta(t)=\sum_{k=-2}^{2}e^{2\pi i k\Delta t}=1+2\cos(2\pi\Delta t)+2\cos(4\pi\Delta t).
\]
For \(V_gf(x,\xi)=\int_{\mathbb R}f(t)g(t-x)e^{-2\pi i\xi t}\,dt\), identify time modulo \(T=1/\Delta\). Define
\[
s=e^{-2\pi\Delta^2},\quad s_\mathrm{B}=\frac{\sqrt5-1}{4},\quad
\Delta_\mathrm{A}=\sqrt{\frac{\log2}{2\pi}},\quad
\Delta_\mathrm{B}=\sqrt{\frac{\log(1+\sqrt5)}{2\pi}}.
\]
There are always exactly four STFT zeros per cylinder \((\mathbb R/T\mathbb Z)\times\mathbb R\), counted with multiplicity. Their *entire* geometry undergoes precisely two transitions, at \(\Delta_\mathrm{A}\) and \(\Delta_\mathrm{B}\). Before the first transition, four distinct simple zeros lie on the central-frequency line \(\xi=0\). Between the transitions, four distinct simple zeros form a reflection-symmetric off-axis rectangle. After the second transition, four distinct simple zeros lie on the half-time line \(x=T/2\), at two pairs of opposite frequencies. At either transition, exactly two distinct double zeros occur and there are no other zeros.

More explicitly, set
\[
h(s)=1-4s+8s^3=(2s-1)(4s^2+2s-1),\qquad
 y_\pm(s)=\frac{-1\pm\sqrt{h(s)}}{4s^{3/2}}.
\]
For \(0<\Delta<\Delta_\mathrm{A}\), both \(y_\pm\in(-1,1)\), and the zeros are
\[
(x,\xi)=\left(\frac{\pm\arccos(y_\pm)}{2\pi\Delta}\pmod T,\ 0\right).
\]
At \(\Delta=\Delta_\mathrm{A}\), the two double zeros are \((3T/8,0)\) and \((5T/8,0)\). For \(\Delta_\mathrm{A}<\Delta<\Delta_\mathrm{B}\), let \(u>0\), \(\theta\in(\pi/2,\pi)\) be determined uniquely by \(\cosh(u+i\theta)=y_+(s)\), with the square root in \(y_+\) chosen to have positive imaginary part. Then the zeros are exactly
\[
(x,\xi)=\left(\frac{\pm\theta}{2\pi\Delta}\pmod T,\frac{\pm u}{2\pi\Delta}\right),
\]
with the two signs chosen independently. At \(\Delta=\Delta_\mathrm{B}\), write
\(\rho=\operatorname{arcosh}(1/(4s_\mathrm{B}^{3/2}))/(2\pi\Delta_\mathrm{B})\); the two double zeros are \((T/2,\rho)\) and \((T/2,-\rho)\). For \(\Delta>\Delta_\mathrm{B}\), both \(y_\pm<-1\), and the four zeros are
\[
(x,\xi)=\left(T/2,\frac{\pm\operatorname{arcosh}(-y_\pm)}{2\pi\Delta}\right).
\]
Every simple zero has local phase winding \(-1\) in the positively oriented \((x,\xi)\)-plane; each double zero has winding \(-2\). There are no zero collisions except at the two stated parameter values. As \(\Delta\to\infty\), the four frequencies approach the four adjacent-tone midpoints \(\pm\Delta/2\) and \(\pm3\Delta/2\).

## Assumptions and scope
The signal is a bounded tempered distribution (not a square-integrable signal), and the Gaussian-window integral converges absolutely. Five tones have equal complex amplitude \(1\) and frequencies \(\{-2\Delta,-\Delta,0,\Delta,2\Delta\}\). Frequency \(\xi\in\mathbb R\) is unrestricted; only time is identified modulo its actual period \(T\). Zeros refer to the *complex STFT*, equivalently zeros of its squared modulus, not critical points or ridges of that modulus. Multiplicity is analytic multiplicity in the coordinate \(z=\xi+i x\).

## Proof
**Exact reduction.** Gaussian integration yields, for each real \(\omega\),
\[
\int_{\mathbb R}e^{2\pi i\omega t}e^{-\pi(t-x)^2}e^{-2\pi i\xi t}\,dt
=e^{-\pi(\xi-\omega)^2+2\pi i(\omega-\xi)x}.
\]
Putting \(q=e^{-\pi\Delta^2}\) and \(w=2\pi\Delta(\xi+i x)\) gives the exact identity
\[
V_gf_\Delta(x,\xi)=e^{-\pi\xi^2-2\pi i\xi x}
\left[1+2q\cosh w+2q^4\cosh(2w)\right].\tag{1}
\]
The prefactor never vanishes. The map \((x\bmod T,\xi)\mapsto e^w\) identifies the time-frequency cylinder bijectively with \(\mathbb C^\times\). Thus the zero count, with multiplicity, equals the number of nonzero roots of the reciprocal quartic
\[
q^4(v^4+1)+q(v^3+v)+v^2=0.\tag{2}
\]
Its constant coefficient is nonzero, so it has exactly four nonzero roots counted with multiplicity.

**Critical parameters.** With \(y=\cosh w\), the bracket in (1) is
\[
Q_q(y)=4q^4y^2+2qy+1-2q^4.
\]
Its discriminant is \(4q^2h(s)\), where \(s=q^2\) and \(h(s)=(2s-1)(4s^2+2s-1)\). The only zeros of this discriminant for \(0<s<1\) occur at \(s=1/2\) and \(s=s_\mathrm{B}\). Additionally, \(Q_q(1)=1+2q+2q^4>0\), while
\(Q_q(-1)=1-2q+2q^4>0\) for every \(q>0\): its unique positive critical point is \(q=4^{-1/3}\), where the minimum is \(1-3/(2\cdot4^{1/3})>0\). Hence no root \(y\) ever crosses \(\pm1\), and every STFT multiplicity change must come from the quadratic discriminant. Both discriminant crossings are simple in \(s\), and \(\sinh w\ne0\) at their associated \(w\)-values, so each collision has multiplicity exactly two.

**Three complete geometric regimes.** At \(q=1\), the two quadratic roots are \((\sqrt5-1)/4\) and \(-(\sqrt5+1)/4\), strictly between \(-1\) and \(1\). Since they cannot cross \(\pm1\), both remain in this interval whenever \(s>1/2\). The equation \(\cosh w=y\in(-1,1)\) has precisely two solutions \(w=\pm i\arccos y\) modulo \(2\pi i\), proving the first case. At \(s=1/2\), the common root is \(-1/\sqrt2\), so \(w=\pm3\pi i/4\), giving the two stated double points.

When \(s_\mathrm{B}<s<1/2\), the two roots are nonreal conjugates with negative real parts. One has a unique inverse-cosh representative \(u+i\theta\) with \(u>0\), \(\pi/2<\theta<\pi\); the full inverse image of both conjugates modulo \(2\pi i\) is \(\{\pm u\pm i\theta\}\). This proves the off-axis rectangle and excludes any other zeros.

At \(s=s_\mathrm{B}\), the common root is \(-1/(4s_\mathrm{B}^{3/2})<-1\) (indeed \(s_\mathrm{B}<1/3\)). It has inverse images \(\pm\operatorname{arcosh}(1/(4s_\mathrm{B}^{3/2}))+i\pi\). For smaller \(s\), the two roots remain real and below \(-1\): this holds, for example, at \(s=1/4\), and continuity plus \(Q_q(\pm1)>0\) prevents a crossing. Consequently \(w=\pm\operatorname{arcosh}(-y_\pm)+i\pi\), giving the final regime. In all three open regimes all zeros are simple.

**Winding and distant-tone limit.** The bracket in (1) is holomorphic in \(z=\xi+i x\). At a zero of analytic multiplicity \(m\), its phase winds \(+m\) in the positively oriented \((\xi,x)\)-plane and therefore \(-m\) in the positively oriented \((x,\xi)\)-plane. The nonzero smooth prefactor contributes no local winding. Finally, as \(q\downarrow0\), the quadratic roots satisfy \(y_+=-(2q)^{-1}(1+O(q^2))\) and \(y_-=-(2q^3)^{-1}(1+O(q^2))\). The identity \(\operatorname{arcosh} r=\log(2r)+O(r^{-2})\) gives the four claimed midpoint asymptotics (with errors \(O(e^{-2\pi\Delta^2}/\Delta)\)).

## Verification
The standalone file `verify_five_tone.py` checks the exact polynomial discriminant factorization using rational coefficients and performs 2,109 independent finite comparisons of the five-Gaussian-term STFT against (1), all four predicted zeros at multiple gaps in the three regimes, and vanishing first but nonvanishing second analytic derivatives at both critical scales. The checker uses standard Python complex arithmetic and exact rational polynomial multiplication. Execute `python3 verify_five_tone.py` from the directory containing the files. The universal classification is proved by the analytic steps above, not by finite sampling.

## Relationship to prior work
Chand, Nolen, and Wu (2026) analyze spectral interference and phase winding for a **two-component** Gaussian-window model, and their Gaussian formula motivates the multi-component question. Their full-text Section 2 explicitly specializes to two components; the five-tone two-threshold zero bifurcation is not a stated result of their model. Standard Gaussian integration, Bargmann holomorphy, and elementary polynomial identities are prior mathematical tools, not claimed as novel. General work on Wigner/STFT zero-free conditions and Gaussian Weyl–Heisenberg zero statistics concerns different classes and conclusions. The present claim is limited to a complete and explicit four-zero geometry, two collision scales, and multiplicities for the symmetric equal-amplitude five-component model. Priority remains qualified by the possibility of an unindexed equivalent calculation or a stronger exponential-polynomial zero theorem.

## Limitations
No claim is made for unequal component amplitudes, nonequidistant frequencies, other analysis windows, spectrogram ridge bifurcations, stochastic signals, or noisy finite-time observations. Analytic zero multiplicity and phase winding do not by themselves imply a numerical zero-detection guarantee. The proof uses an elementary exact reduction; independent scientific auditing and exhaustive historical-priority certification have not been performed.

## References
1. S. Chand, J. Nolen, and H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910 (first posted 2026-01-15), https://arxiv.org/abs/2601.10910 . Full text also accessible at https://www.researchgate.net/publication/399876106_On_spectral_interference_of_the_short-time_Fourier_transform_and_its_nonlinear_variations .
2. K. Gröchenig, P. Jaming, and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937 (2018), https://arxiv.org/abs/1811.03937 .
3. *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge*, Journal of Statistical Physics (2022), https://doi.org/10.1007/s10955-022-02917-3 .
