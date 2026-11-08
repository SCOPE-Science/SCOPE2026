# Sharp fourth-cumulant envelopes at fixed persistence and chirality in planar run-and-tumble motion

## Finding
Consider a constant-speed planar run-and-tumble particle with independent angle increments at Poisson tumbles. Prescribing only its first angular Fourier moment fixes its entire velocity covariance and active diffusivity, yet does not generally fix the sign of the long-time fourth cumulant of a Cartesian displacement. We determine exactly the feasible range of that cumulant over *all* angular-jump probability measures and prove that finite two-angle tumbling laws attain the sharp endpoints.

Write \(z=\mathbb E[e^{i\Psi}]=x+iy\), \(w=\mathbb E[e^{2i\Psi}]\), \(R=1-|z|^2\), and \(d=|1-z|^2\). Assume \(|z|<1\), and exclude \(w=1\), for which the second angular harmonic fails to relax. For a Cartesian displacement \(X_t\), define \(K=\lim_{t\to\infty}\kappa_4(X_t)/t\), where \(\kappa_4(X)=\mathbb E[X^4]-3\mathbb E[X^2]^2\). Then \(K\) exists and, with \(\alpha>0\) the tumble rate and \(v>0\) the propulsion speed,
\[
K=\frac{3v^4}{\alpha^3}\left[\operatorname{Re}\frac{1}{(1-z)^2(1-w)}-2\operatorname{Re}\frac1{1-z}\,\operatorname{Re}\frac1{(1-z)^2}\right].
\]
**The complete attainable sets at fixed \(z\) are:**

For \(y\ne0\), the compact interval
\[
\boxed{\quad
K\in\frac{3v^4}{\alpha^3}
\left[-\frac{2(1-x)^2R}{d^3},\quad
\frac{R\big((1-x)^2-y^2\big)^2}{2y^2d^3}\right].\quad}
\]
Every endpoint is attained by a turning distribution supported on exactly two angles, and every intermediate point is attained by a finite mixture. The lower bound is always negative. The upper bound is zero if and only if \(|y|=1-x\); otherwise the two possible cumulant signs coexist at the *same complete velocity autocovariance*.

For \(y=0\), writing \(z=r\in(-1,1)\), the attainable set is
\[
\boxed{\quad K\in\frac{3v^4}{\alpha^3}
\left[\frac{-3-4r}{2(1-r)^3(1+r)},\ \infty\right).\quad}
\]
The lower bound is attained by equal-angle-conjugate two-point tumbles \(\Psi=\pm\arccos r\), each with probability \(1/2\); there is no finite upper bound among admissible measures. Consequently, for \(-1<r<-3/4\) **all** admissible laws give \(K>0\); at \(r=-3/4\), \(K\ge0\) and zero is attained; and for \(-3/4<r<1\), both signs are possible. Independent translational Gaussian diffusion does not affect \(K\).

A rational witness at \(z=i/2\), with \(\alpha=v=1\), uses the two probability laws on unit complex orientations after each tumble:
\[
Q_+=\frac{13}{28}\delta_{(12+5i)/13}+\frac{15}{28}\delta_{(-4+3i)/5},\qquad
Q_-=\frac58\delta_{(3+4i)/5}+\frac38\delta_{-1}.
\]
Both have \(z=i/2\) and the same velocity correlation; their exact cumulant rates are respectively \(K_+=162/125\) and \(K_-=-288/125\). For \(z=(1+i)/2\), the two-point law giving jumps \(0\) and \(\pi/2\) with equal weights attains the sharp bound \(K=0\), and no law with this \(z\) has positive rate.

## Assumptions and scope
Let \(\Theta_0\) be uniform on \([0,2\pi)\), independent of a rate-\(\alpha\) Poisson process, i.i.d. angle increments \(\Psi_j\) of arbitrary probability law \(Q\) on the circle, and independent standard Brownian motion \(B_t\). Put \(\Theta_t=\Theta_0+\sum_{j\le N_t}\Psi_j\pmod {2\pi}\), and \(X_t=v\int_0^t\cos\Theta_s\,ds+\sqrt{2D}\,B_t\), with \(v>0\), \(\alpha>0\), \(D\ge0\). Fix the first Fourier moment \(z\) with \(|z|<1\); admissible second moments satisfy \(w\ne1\). The limiting cumulant is of the **one-dimensional projected displacement**, not a radial moment. Jump laws need not have densities; atoms and null tumbles are permitted. Rotationally uniform initial orientation is essential to the stated projected-cumulant formula. The cases \(|z|=1\) or \(w=1\) are outside its quantified domain.

For \(\tau\ge0\), the stationary propulsion velocity satisfies
\[
\mathbb E[v\cos\Theta_t\,v\cos\Theta_{t+\tau}]
=\frac{v^2}{2}\operatorname{Re}e^{-\alpha(1-z)\tau}
=\frac{v^2}{2}e^{-\alpha(1-x)\tau}\cos(\alpha y\tau).
\]
It depends on \(z\), not \(w\). The long-time active diffusivity is \((v^2/2)\operatorname{Re}[\alpha(1-z)]^{-1}\); independent translational diffusion adds \(D\).

## Proof
**1. Fourth-cumulant rate.** It suffices to take \(D=0\), because independent Gaussian summands have zero cumulants above order two. Set \(a_j=\alpha(1-\mathbb E[e^{ij\Psi}])\) and \(A_j(s)=1/(s+a_j)\) for \(j=1,2\). The angular generator acts diagonally on Fourier modes: \(L e^{in\theta}=-a_n e^{in\theta}\). Define \(m_{k,n}(t)=\mathbb E[X_t^k e^{in\Theta_t}]\). Differentiating and using \(\cos\theta=(e^{i\theta}+e^{-i\theta})/2\) yields
\[
\dot m_{k,n}=-a_n m_{k,n}+\frac{kv}{2}(m_{k-1,n-1}+m_{k-1,n+1}),
\]
with \(m_{0,0}(0)=1\) and all other initial moments zero. Write \(S(s)=A_1(s)+\overline{A_1(\bar s)}\) and \(T(s)=A_1(s)^2A_2(s)+\overline{A_1(\bar s)^2A_2(\bar s)}\). Solving the finite hierarchy gives exact Laplace transforms
\[
\mathcal L\mathbb E[X_t^2](s)=\frac{v^2S(s)}{2s^2},\qquad
\mathcal L\mathbb E[X_t^4](s)=\frac{3v^4}{2}\left[\frac{S(s)^2}{s^3}+\frac{T(s)}{s^2}\right].
\]
Since \(\operatorname{Re}a_1>0\) and \(\operatorname{Re}a_2>0\), their rational inversions have an exponential remainder, apart from polynomial terms. If \(S(s)=S_0+S_1s+O(s^2)\), then \(S_0=2\operatorname{Re}(1/a_1)\) and \(S_1=-2\operatorname{Re}(1/a_1^2)\). With \(T_0=2\operatorname{Re}(1/(a_1^2a_2))\), coefficient extraction gives
\[
\mathbb E[X_t^2]=\frac{v^2}{2}(S_0t+S_1)+o(1),\quad
\mathbb E[X_t^4]=\frac{3v^4}{4}S_0^2t^2+\frac{3v^4}{2}(2S_0S_1+T_0)t+O(1),
\]
and therefore \(K=(3v^4/2)(S_0S_1+T_0)\), exactly the displayed formula. This derivation independently checks the normalization of the established full fourth-moment transform in Sevilla, Eq. (54).

**2. Exact feasible angular-moment disk.** For \(U=e^{i\Psi}\) on the unit circle, Jensen/Cauchy-Schwarz gives \(|w-z^2|=|\mathbb E[(U-z)^2]|\le\mathbb E|U-z|^2=1-|z|^2=R\). Conversely, for every unit complex direction \(e^{i\phi}\), the line through interior \(z\) in that direction cuts the unit circle at two points. Their unique barycentric probabilities giving mean \(z\) yield \(\mathbb E[(U-z)^2]=Re^{2i\phi}\). Thus the entire boundary of the disk \(|w-z^2|\le R\) is attained by two-point laws, and the interior follows by convex mixtures of boundary laws with the same mean \(z\). This proves exact feasibility rather than merely an outer bound.

**3. Nonreal first harmonic.** For \(y\ne0\), the closed disk for \(c=1-w\) has center \(1-z^2\) and radius \(R\); its squared center modulus minus squared radius equals \(4y^2\). Inversion \(B=1/(1-w)\) therefore maps it bijectively onto the closed disk of center \(\overline{(1-z^2)}/(4y^2)\) and radius \(R/(4y^2)\). For fixed \(z\), the dimensionless rate \(F=\alpha^3K/(3v^4)\) is the real affine functional \(F=\operatorname{Re}[B/(1-z)^2]-2\operatorname{Re}[(1-z)^{-1}]\operatorname{Re}[(1-z)^{-2}]\). Its minimum and maximum over this disk are the center value minus/plus the radius multiplied by \(|1-z|^{-2}\). Direct expansion gives exactly the two endpoints above. The extreme \(B\) values lie on the boundary, hence have two-atom witnesses, and connectedness yields all intermediate values. The sign conditions follow since \(R>0\), \(1-x>0\), and the upper numerator is a square.

**4. Real first harmonic.** If \(z=r\in(-1,1)\), the allowed disk \(|w-r^2|\le1-r^2\) touches \(w=1\). Excluding that point, inversion \(B=1/(1-w)\) maps it exactly to the right half-plane \(\operatorname{Re}B\ge1/[2(1-r^2)]\). Now \(F=(1-r)^{-2}\operatorname{Re}B-2(1-r)^{-3}\), so its image is the stated half-line, with minimum \((-3-4r)/[2(1-r)^3(1+r)]\). The two-angle symmetric law \(U=e^{\pm i\arccos r}\) gives \(w=2r^2-1\) and attains the minimum. Boundary laws approaching \(w=1\) give unbounded positive rates while remaining in the stated domain. The sign threshold follows by checking \(-3-4r\) on \((-1,1)\).

## Verification
The supplied `verify.py` uses exact symbolic algebra to check the Möbius-disk extrema, exact rational two-atom witnesses, the sharp real-axis boundary, and a four-state tilted-generator check that distinguishes fixed orientation cosets from the stated uniform initial angle. A separate truncated Fourier-mode Feynman–Kac calculation numerically approaches the analytical fourth-cumulant rate at increasing times. It also checks many rational two-angle mixtures against the sharp envelopes. Execute with `python verify.py` (Python, SymPy, NumPy, SciPy). The independent computations check finite/algebraic instances; the proofs above establish the quantified continuum statements.

## Relationship to prior work
Britton, Zhang, Han and Bertrand (arXiv:2608.23519, first submitted August 24, 2026) derive exact preferred-reorientation RTP fields, MSD and higher-order moments. Their Section 3.5 identifies the dependence of fourth moments on the second angular Fourier mode and their discussion gives a Gaussian leading-order limit, not a classification of all angular laws at fixed first mode. Sevilla (arXiv:1905.07090, Eq. (54)) already derives an exact arbitrary-turning-angle Laplace transform of the full fourth moment; that **forward result is prior work**. Its following discussion notes that angular Fourier modes are constrained and studies chosen laws, but does not give a complete sharp feasible fourth-cumulant interval, two-angle extremizers or the positive/negative/zero boundary. Olsen and Löwen (arXiv:2405.14326, Phys. Rev. E 110, 064606) optimize second-moment diffusion for strategic reorientations, not this fourth-cumulant envelope. The present contribution is therefore the sharp **inverse design/attainability theorem**, not the original fourth-moment transform, the Gaussian limit, or the existence of higher-harmonic effects.

## Limitations
The theorem requires \(|z|<1\), \(w\ne1\), an independent Poisson tumble clock, i.i.d. jumps, spatially isotropic initial angle and constant speed. The excluded \(w=1\) case has a nonrelaxing second harmonic and may have different asymptotics. The bounds concern the linear-in-time fourth cumulant of a Cartesian projection, not finite-time excess kurtosis or the complete spatial law. Two-atom turning laws and null tumbles are admissible; requiring a smooth strictly positive turning density would change attainment to closure statements. The general exact fourth-moment formula is known, and a different published global angular-moment extremal theorem might subsume this optimization; no independent publication-priority certification has been performed.

## References
1. C. Britton, Z. Zhang, S. Han, T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519, first posted 2026-08-24, https://arxiv.org/abs/2608.23519 . Section 3.5 and discussion of Fourier modes.
2. F. J. Sevilla, *Two-dimensional active motion*, arXiv:1905.07090, first posted 2019-05-17, https://arxiv.org/abs/1905.07090 . In particular Eq. (54) and its surrounding discussion (original full fourth-moment transform).
3. K. S. Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326, first posted 2024-05-23, https://arxiv.org/abs/2405.14326 ; Phys. Rev. E 110, 064606 (2024). First-two-moment diffusion optimization.
