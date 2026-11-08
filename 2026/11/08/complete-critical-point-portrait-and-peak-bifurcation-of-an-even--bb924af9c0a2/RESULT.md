# Complete critical-point portrait and peak bifurcation of an even Gaussian spectrogram

## Finding

For every real \(a>0\), define the nonnegative even Gaussian spectrogram
\[
H_a(z)=e^{-|z|^2}|\cosh(az)|^2,\qquad z\in\mathbb C.
\]
All its stationary points are on the two coordinate axes. In particular, there are no off-axis critical points.

The zeros
\[
 z_k^{(0)}=\frac{(k+\tfrac12)\pi i}{a},\qquad k\in\mathbb Z,
\]
are all the local minima, and they are isolated, strict, nondegenerate global minima of value zero. For each integer \(k\ge0\), let \(y_k(a)\) denote the unique solution of
\[
 y=-a\tan(ay),\qquad \frac{(k+\tfrac12)\pi}{a}<y<\frac{(k+1)\pi}{a}.
\]
The points \(\pm i y_k(a)\), and only these positive-intensity points on the imaginary axis other than the origin, are stationary. All are strict nondegenerate saddles. The zeros and saddles strictly interlace on each imaginary half-axis.

When \(0<a<1\), the origin is the unique local and global maximum and is nondegenerate. At \(a=1\), it remains the unique strict global maximum but is degenerate, with quartic decay in the real direction. For \(a>1\), the origin becomes a nondegenerate saddle, and the only maxima are the two nondegenerate global maxima \(\pm x_a\), where \(x_a\in(0,a)\) is the unique positive root of
\[
 x=a\tanh(ax).
\]
These maxima bifurcate sharply at \(a=1\), with
\[
 x_a=\sqrt{6(a-1)}\bigl(1+O(a-1)\bigr)\qquad (a\downarrow1).
\]
There are no further stationary points of any type, including at the transition.

## Assumptions and scope

The parameter \(a\) is real and strictly positive. Stationarity and the Hessian are with respect to the two real coordinates \(z=x+iy\), on the entire plane (not a bounded observation window). No random coefficients are assumed. Under the standard Bargmann–Fock/Gaussian-window identification, \(H_a\), up to a positive constant and a harmless reflection of the frequency coordinate, is the spectrogram/Husimi intensity of a balanced even superposition of two real-displaced coherent Gaussians. The coherent-state separation in dimensionless Fock coordinates is \(2a\); the Gaussian weight convention is exactly \(e^{-|z|^2}\). Positive rescaling of intensity does not affect the portrait.

## Proof

**Axis confinement.** The elementary identity
\[
H_a(x+iy)=\frac12e^{-x^2-y^2}\bigl(\cosh(2ax)+\cos(2ay)\bigr)
\]
shows that its only zeros occur at \(x=0\) and \(ay=(k+\tfrac12)\pi\). Put \(D=\cosh(2ax)+\cos(2ay)\), which is strictly positive away from these zeros. Differentiating \(\log H_a\) at positive-intensity points gives
\[
 xD=a\sinh(2ax),\qquad yD=-a\sin(2ay).
\]
If both \(x\ne0\) and \(y\ne0\), the two equations imply
\[
 \frac{\sinh(2ax)}{2ax}=-\frac{\sin(2ay)}{2ay}.
\]
The left side is strictly larger than one for any nonzero real \(x\), while the right side is at most one. Hence no off-axis critical points exist. All zeros are critical points because the entire factor \(\cosh(az)\) has simple zeros. Near any zero \(z_0\),
\[
 H_a(z)=a^2e^{-|z_0|^2}|z-z_0|^2+O(|z-z_0|^3).
\]
Thus their real Hessians are \(2a^2e^{-|z_0|^2}I_2\): they are nondegenerate minima.

**Imaginary-axis saddles.** At \(x=0\), away from zeros of \(\cos(ay)\), stationarity reduces to \(y=-a\tan(ay)\). For \(y>0\), its solutions lie only in the intervals stated above. On each such interval, \(y+a\tan(ay)\) is strictly increasing, tends to \(-\infty\) at the left endpoint, and is positive at the right endpoint, so it has exactly one zero. Reflection supplies negative solutions. At each such stationary point, the mixed Hessian vanishes and the two diagonal entries of the Hessian of \(\log H_a\) are
\[
 \partial_{xx}\log H_a=2(a^2+y^2-1),\qquad
 \partial_{yy}\log H_a=-2(1+a^2+y^2).
\]
Because \(y>\pi/(2a)\), one has \(a^2+y^2>a^2+\pi^2/(4a^2)\ge\pi>1\). The Hessian therefore has opposite nonzero signs. Since \(H_a>0\), the Hessian of \(H_a\) has the same inertia at a positive-intensity stationary point. Each is a strict nondegenerate saddle.

**Real-axis maxima and the threshold.** At \(y=0\), stationarity is \(x=a\tanh(ax)\). For positive \(x\), the ratio \(a\tanh(ax)/x\) is strictly decreasing from \(a^2\) to zero. Therefore a unique positive solution exists precisely when \(a>1\), and it lies in \((0,a)\). At such a solution, strict downward crossing gives \(a^2\operatorname{sech}^2(ax_a)<1\), and the diagonal Hessian entries of \(\log H_a\) are
\[
 -2+2a^2\operatorname{sech}^2(ax_a),\qquad
 -2-2a^2\operatorname{sech}^2(ax_a),
\]
both negative; the mixed entry is zero. The Hessian at the origin is diagonal with entries \(2(a^2-1)\) and \(-2(a^2+1)\), so the origin is a nondegenerate maximum for \(a<1\) and a nondegenerate saddle for \(a>1\). At \(a=1\),
\[
\log H_1(x,0)=-\frac{x^4}{6}+O(x^6),\qquad
\log H_1(iy)=-2y^2+O(y^4),
\]
proving quartic degeneracy and strict local maximality. Expanding \(\tanh(ax)=ax-(ax)^3/3+O(x^5)\) at the unique small positive root gives \(x_a^2=3(a^2-1)/a^4+O((a-1)^2)=6(a-1)+O((a-1)^2)\), proving the bifurcation law.

**Global optimality and completeness.** For every \(x,y\),
\[
H_a(x+iy)\le e^{-x^2-y^2}\cosh^2(ax)\le e^{-x^2}\cosh^2(ax),
\]
with strict inequality for \(y\ne0\). The one-variable derivative of the last expression has the sign of \(a\tanh(ax)-x\). Its only maximizing points are exactly those classified above. All critical points have already been exhausted by axis confinement, including the zeros.

## Verification

The companion `check_spectrogram.py` uses symbolic differentiation to verify the gradient and Hessian identities and the quartic boundary expansion. It also brackets and checks representative roots of the transcendental real/imaginary axis equations for four parameter values. Its successful output is `EVEN_FOCK_MORSE_CHECK_PASS symbolic=7 numeric=87 stationary_axis_roots=20`. These finite checks are corroborative only: the completeness of the infinite stationary set, the exclusion of off-axis points, strict Hessian signatures and the all-parameter threshold are established by the preceding inequalities.

## Relationship to prior work

Abreu (2022) studies critical points, maxima and saddle intensities of Gaussian-window spectrograms of **complex white noise**, via Gaussian entire functions and the Fock covariant derivative. The general critical-point equation is part of that literature. The result here concerns instead the deterministic symmetric two-coherent-state function \(\cosh(az)\) and determines its entire global critical-point portrait and a sharp separation threshold. Miranowicz, Bajer, Wahiddin and Imoto (2001) give Husimi distributions and phase/entropy analysis of coherent-state cats, including the even state; the explicit intensity is background, but its complete planar stationary-point and Hessian classification is a distinct assertion. Equivalent Husimi, Gaussian short-time Fourier and Fock-weighted formulations were compared; neither inspected treatment states the complete portrait or its all-parameter proof.

## Limitations

This classification holds for balanced even two-Gaussian superpositions with real opposed displacements. General unequal-amplitude, odd-cat, multimode, noisy, or non-Gaussian signals are not covered. No assertion of historical uniqueness is made: a specialized earlier Husimi-landscape classification not located in the reviewed literature could overlap. Numerical root tests are not proofs of exhaustiveness. The critical value \(a=1\) depends on the stated Fock-space normalization.

## References

1. L. D. Abreu, “Local Maxima of White Noise Spectrograms and Gaussian Entire Functions,” arXiv:2210.06721 (first posted 2022-10-13), *J. Fourier Anal. Appl.* **28**, 88 (2022), doi:10.1007/s00041-022-09979-7. https://arxiv.org/abs/2210.06721 .
2. A. Miranowicz, J. Bajer, M. R. B. Wahiddin, N. Imoto, “Wehrl information entropy and phase distributions of Schrödinger cat and cat-like states,” arXiv:quant-ph/0107107 (2001), *J. Phys. A* **34**, 3887–3896 (2001), doi:10.1088/0305-4470/34/18/315. https://arxiv.org/abs/quant-ph/0107107 .
