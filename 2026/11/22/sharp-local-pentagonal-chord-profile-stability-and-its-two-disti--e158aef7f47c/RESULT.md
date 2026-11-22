# Sharp local pentagonal chord-profile stability and its two distinct soft Fourier modes

## Finding
Write \(\|h\|_2^2=(2\pi)^{-1}\int_0^{2\pi}|h(\theta)|^2\,d\theta\). Let \(f\) be a real \(2\pi\)-periodic \(C^2\) function with \(\widehat f(0)=\widehat f(1)=\widehat f(-1)=0\), and let \(\gamma_f(\theta)=(1+f(\theta))(\cos\theta,\sin\theta)\). For \(k\in\{1,2\}\) define the point \(\Theta_{k,f}(\theta)\) to be the unique advance from \(\theta\) by \(k/5\) of the **total Euclidean arclength** of this positively oriented curve, and define
\[
C_{k,f}(\theta)=|\gamma_f(\Theta_{k,f}(\theta))-\gamma_f(\theta)|,
\qquad \overline C_{k,f}=\frac1{2\pi}\int_0^{2\pi} C_{k,f}(\theta)\,d\theta.
\]
There are positive absolute constants \(\eta_k,K_k\) such that if \(\|f\|_{C^2}<\eta_k\), then the curve is strictly convex and
\[
\boxed{\quad\|C_{k,f}-\overline C_{k,f}\|_2\ge
[\delta_k-K_k\|f\|_{C^2}]\,\|f\|_2,\quad
\delta_1=\frac{3\sqrt5-5}{7}\sin\frac\pi5,\qquad
\delta_2=\frac56\sin\frac\pi5.\quad}
\]
Both coefficients \(\delta_k\) are **optimal at first order**: the minimum singular values of the linearized chord-profile maps on \(\widehat f(0)=\widehat f(\pm1)=0\) are attained **only** by frequencies \(n=\pm7\) at \(k=1\) and \(n=\pm6\) at \(k=2\), respectively. The two different soft modes give a sharp contrast between the two pentagonal fractions.

## Assumptions and scope
The polar radius is normalized to one at \(f=0\). Removing the average and first harmonics fixes the infinitesimal dilation and translation gauges. The remainder is measured in \(\|f\|_{C^2}=\max_{j=0,1,2}\|f^{(j)}\|_\infty\); its smallness ensures \(1+f>0\) and strict positive curvature through \((1+f)^2+2(f')^2-(1+f)f''>0\). The chord endpoint is defined by **arclength fraction**, not by fixed polar-angle separation. The mean of each actual chord profile is subtracted with respect to polar angle \(d\theta\); it is not a statement about area-bisecting chords or arbitrary distant convex bodies.

## Proof
**Step 1: full linearization, including endpoint motion.** Fix \(k\) and put \(\alpha=2\pi k/5\), \(s=\sin(\alpha/2)\), \(c=\cos(\alpha/2)\). Perturb the unit circle by \(\varepsilon f\). Its arclength speed is \(1+\varepsilon f+O(\varepsilon^2)\), and, because \(\int f=0\), its perimeter is \(2\pi+O(\varepsilon^2)\). The unique endpoint has expansion
\[
\Theta_{k,\varepsilon f}(\theta)=\theta+\alpha-
\varepsilon\int_\theta^{\theta+\alpha} f(u)\,du+O(\varepsilon^2).
\]
Differentiating the Euclidean chord length (whose unperturbed value is \(2s>0\)) gives the linear operator
\[
(L_k f)(\theta)=s\bigl(f(\theta)+f(\theta+\alpha)\bigr)
-c\int_\theta^{\theta+\alpha}f(u)\,du.\tag{1}
\]
For \(n\ne0\), its multiplier on \(e^{in\theta}\) is
\[
m_{k,n}=2e^{in\alpha/2}
\left[s\cos\frac{n\alpha}{2}-\frac{c}{n}\sin\frac{n\alpha}{2}\right],\tag{2}
\]
with \(m_{k,1}=m_{k,-1}=0\). On mean-zero inputs the output has zero angular mean. Hence the optimal linear constant on the stated gauge slice is \(\inf_{n\ge2}|m_{k,n}|\).

**Step 2: exact infinite-frequency minimization.** Set \(u=\cos(2\pi/5)=(\sqrt5-1)/4\), \(v=\sin(2\pi/5)\), \(s_*=\sin(\pi/5)=2uv\), and \(\varphi=(1+\sqrt5)/2\). Divide the real bracketed multiplier \(b_{k,n}=e^{-in\alpha/2}m_{k,n}\) by \(s_*\). Direct trigonometric reduction for the finite exceptional ranges gives

| \(k\) | \(n\) | exact \(b_{k,n}/s_*\) |
|---|---:|---|
| 1 | 2 | \((\varphi-3)/2\) |
| 1 | 3 | \((2-4\varphi)/3\) |
| 1 | 4 | \(-5\varphi/4\) |
| 1 | 5 | \(-2\) |
| 1 | 6 | \(-5\varphi/6\) |
| 1 | 7 | \((8-6\varphi)/7=(5-3\sqrt5)/7\) |
| 2 | 2 | \(-(3\varphi+1)/2\) |
| 2 | 3 | \(-(2\varphi+4)/3\) |
| 2 | 4 | \(5/4\) |
| 2 | 5 | \(2\varphi\) |
| 2 | 6 | \(5/6\) |

The smallest absolute entries are, respectively, \((3\sqrt5-5)/7\) and \(5/6\), and are strict within these finite ranges. All integer multiples have \(|\cos(n\pi/5)|\ge u\) and \(|\cos(2n\pi/5)|\ge u\), because fifth roots of unity are involved. When \(k=1\) and \(n\ge8\), the triangle inequality gives
\[
|m_{1,n}|\ge 2(s_*u-\cos(\pi/5)/8)
>2(s_*u-\cos(\pi/5)v/7)=\delta_1,
\]
where strictness follows from \(v>7/8\). For \(k=2\) and \(n\ge7\), since \(\cos(2\pi/5)=u\),
\[
|m_{2,n}|\ge 2u(v-1/7)>5s_*/6=\delta_2,
\]
using \(s_*=2uv\) and \(v>6/7\). Both elementary trigonometric bounds follow, for example, from \(v^2=(5+\sqrt5)/8>81/100\). Thus the minima and unique Fourier-frequency equality spaces are proved over **all** frequencies, not just a numerical truncation. Parseval proves \(\|L_k f\|_2\ge\delta_k\|f\|_2\).

**Step 3: uniform nonlinear remainder.** Write \(\eta=\|f\|_{C^2}\) and \(h=\|f\|_2\). For sufficiently small \(\eta\), the exact speed satisfies
\[
w_f=\sqrt{(1+f)^2+(f')^2}=1+f+E_f,\qquad 0\le E_f\le C(f')^2.
\]
By periodic integration by parts and Cauchy–Schwarz,
\[
\|E_f\|_{L^1}\le C\|f'\|_2^2
=-\frac{C}{2\pi}\int f f''\le C\eta h,\tag{3}
\]
where harmless measure-normalizing constants are absorbed into \(C\). Let \(\Delta(\theta)=\Theta_{k,f}(\theta)-\theta-\alpha\). In the defining arclength equation, subtract \(\alpha+\int_\theta^{\theta+\alpha}f\), use \(\int f=0\), positivity of the speed, and \(\|f\|_\infty\le\eta\). The convolution bound \(\sup_\theta|\int_\theta^{\theta+\alpha}f|\le\sqrt{2\pi}\,h\) and (3) first give \(\|\Delta\|_\infty+\|\Delta\|_2\le C h\); reinserting them in the equation gives
\[
\left\|\Delta+\int_\theta^{\theta+\alpha} f(u)\,du\right\|_2
\le C\eta h.\tag{4}
\]
Expand the endpoint \((1+f(\theta+\alpha+\Delta))e^{i(\theta+\alpha+\Delta)}\) about \(\Delta=0\), using \(\|f'\|_\infty\le\eta\), and then Taylor-expand the norm around the nonzero baseline chord. All second-order products have \(L^2\) norm at most \(C\eta h\): for example \(\|\Delta^2\|_2\le\|\Delta\|_\infty\|\Delta\|_2\le C\eta h\). Equations (1) and (4) therefore yield the **relative** error estimate
\[
\|C_{k,f}-2s-L_kf\|_2\le C_k\eta h.\tag{5}
\]
Orthogonal projection of (5) onto mean-zero functions, followed by Parseval, gives the claimed nonlinear inequality.

**Step 4: optimality.** For \(k=1\) take \(f_\varepsilon(\theta)=\varepsilon\cos(7\theta)\); for \(k=2\) take \(f_\varepsilon(\theta)=\varepsilon\cos(6\theta)\). These are strictly convex for small nonzero \(\varepsilon\), and (5) implies that the corresponding chord-profile-to-perturbation norm ratios converge to exactly \(\delta_1\) and \(\delta_2\). The exact first-order coefficients cannot be increased.

## Verification
The standalone standard-library script `verify_chord.py` checks the exact finite-mode formulas numerically at high precision permitted by double-precision trig, strict finite and tail comparisons, and differentiates the actual **arclength-defined** chord profile by trapezoidal arclength integration with fine grids for the two extremal harmonics. This independent discretization corroborates the linearization; the analytic infinite-frequency and nonlinear remainder arguments above, not the numerical tests, establish the theorem. Run `python3 verify_chord.py`.

## Relationship to prior work
Asipchuk and Kosmakov (2026, arXiv:2611.18381v1) give a Fourier proof that constant-length chords at perimetral density \(1/5\) or \(2/5\) globally force a disk for strictly convex \(C^1\) bodies; their theorem is qualitative and does not supply the **sharp local inverse stability coefficient, the perturbed endpoint multiplier (2), or the distinct minimizing Fourier modes**. Bracho, Montejano and Oliveros (2004) discuss Zindler carousels and the earlier global pentagonal rigidity via period and angle constraints. A distinct accessible local near-circular Sobolev stability claim for reduced odd fractions of denominator **at least seven** does not include the denominator-five case; its one-derivative Sobolev scale is also different from the present zero-derivative \(L^2\) estimate. The new conclusion is quantitative and stronger in the restricted near-circle regime, not a new proof of global uniqueness.

## Limitations
The estimate is restricted to sufficiently small real \(C^2\) radial perturbations after fixing the first three Fourier gauges. Constants \(K_k,\eta_k\) are existential and not optimized. Sharpness concerns the coefficient of the first-order \(L^2\) inequality, not a finite-amplitude global best constant. No claim of historical uniqueness or independent external validation is made. A non-exhaustive literature search cannot exclude unindexed local calculations.

## References
1. O. Asipchuk and M. Kosmakov, *Fourier Harmonics and Pentagonal Rigidity in the Planar Ulam Floating Body Problem*, arXiv:2611.18381v1, publicly posted 13 November 2026, https://arxiv.org/abs/2611.18381.
2. J. Bracho, L. Montejano and D. Oliveros, *Carousels, Zindler curves and the floating body problem*, Periodica Mathematica Hungarica 49 (2004), 9–23, https://www.matem.unam.mx/~roli/investigacion/articulos/CarrouP.pdf.
3. J. Bracho, L. Montejano and D. Oliveros, *A Classification Theorem for Zindler Carousels*, Journal of Dynamics and Control Systems 7 (2001), 367–384, as cited in reference 2.
