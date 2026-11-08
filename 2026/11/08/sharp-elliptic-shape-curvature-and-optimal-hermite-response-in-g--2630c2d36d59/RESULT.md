# Sharp elliptic shape curvature and optimal Hermite response in Gaussian time–frequency localization

## Finding
Fix any phase-space area \(s>0\) and consider the family of ellipses
\[
E_{s,t}=\bigl\{(x,\omega)\in\mathbb R^2:\ \pi(e^{-2t}x^2+e^{2t}\omega^2)\le s\bigr\},\quad t\in\mathbb R.
\]
These sets all have Lebesgue area exactly \(s\); \(t=0\) is a disk and positive \(t\) stretches the time axis. Let \(\varphi(u)=2^{1/4}e^{-\pi u^2}\) and let \(P_{s,t}\) be its Gaussian short-time Fourier concentration operator on \(E_{s,t}\), as defined below. Then, for each **fixed** \(s>0\), the largest eigenvalue has the *exact local expansion*
\[
\boxed{\displaystyle \|P_{s,t}\|=1-e^{-s}-\frac{2s^2e^{-s}}{s+2}\,t^2+O_s(t^4),\quad t\to0.}
\]
The largest eigenvalue is simple for all sufficiently small \(|t|\). Its unit eigenfunction \(f_{s,t}\), uniquely phase-normalized by \(\langle f_{s,t},h_0\rangle>0\), obeys
\[
\boxed{\displaystyle f_{s,t}=h_0+\frac{\sqrt2\,s}{s+2}\,t\,h_2+O_s(t^2)\quad\text{in }L^2(\mathbb R).}
\]
Here \(h_0=\varphi\) and \(h_2\) is the unit second Hermite function whose Bargmann image is \(\pi z^2/\sqrt2\). In particular, the signal adapting optimally to ellipse anisotropy develops a linear second-Hermite component.

The curvature magnitude \(c(s)=2s^2e^{-s}/(s+2)\) is positive at every finite \(s>0\) and has exactly one global maximum among all positive areas, attained at \(s_\ast=(\sqrt{17}-1)/2\). This area calibration is a consequence of the explicit curvature, not an alternative optimization over arbitrary nonelliptic regions.

## Assumptions and scope
The short-time Fourier transform uses the normalized convention
\[
V_\varphi f(x,\omega)=\int_{\mathbb R}f(u)\overline{\varphi(u-x)}e^{-2\pi i u\omega}\,du,
\quad\|\varphi\|_{L^2}=1.
\]
The concentration operator is the positive trace-class operator specified by
\[
\langle P_{s,t}f,g\rangle=\int_{E_{s,t}}V_\varphi f(x,\omega)\overline{V_\varphi g(x,\omega)}\,dx\,d\omega.
\]
The shape parameter \(t\) is *logarithmic semiaxis stretching*, not geometric eccentricity: the semiaxes are \(e^t\sqrt{s/\pi}\) and \(e^{-t}\sqrt{s/\pi}\). All asymptotic constants may depend on fixed \(s\). No uniformity as \(s\downarrow0\) or \(s\to\infty\) is asserted. The top eigenvalue is globally optimized over all unit functions \(f\in L^2(\mathbb R)\), not over Gaussian trial functions alone.

The unitary Bargmann transform \(B\) maps normalized Hermite functions \(h_n\) to the orthonormal monomials \(e_n(z)=\pi^{n/2}z^n/\sqrt{n!}\) in the Fock space with Gaussian measure \(e^{-\pi|z|^2}\,dA(z)\). The Gaussian STFT concentration problem is unitarily equivalent to restricting this weighted Fock norm to the same planar set (the harmless reflection of the frequency axis does not change these ellipses).

## Proof
**1. Fock Gram and disk gap.** In the orthonormal basis \(e_n\), the concentration operator has entries
\[
P_{jk}(t)=\int_{E_{s,t}}\overline{e_j(z)}e_k(z)e^{-\pi|z|^2}\,dA(z).
\]
Use the area-preserving change \(z=e^t r\cos\theta+i e^{-t}r\sin\theta\), with \(v=\pi r^2\in[0,s]\). The measure becomes \(dA=dv\,d\theta/(2\pi)\). Thus all entries are analytic in real \(t\) near zero. More intrinsically, over the fixed compact disk, the operator is an integral of rank-one Fock evaluation kernels with a locally norm-convergent power series in \(t\). It is therefore a real-analytic trace-class family.

At \(t=0\) angular orthogonality diagonalizes the matrix, with
\[
\lambda_n(s)=\frac1{n!}\int_0^s e^{-v}v^n\,dv
=1-e^{-s}\sum_{k=0}^n\frac{s^k}{k!}.
\]
The top eigenvalue \(\lambda_0=1-e^{-s}\) is simple, since \(\lambda_0>\lambda_1\ge\lambda_2\ge\dots\ge0\), with gap \(\lambda_0-\lambda_1=se^{-s}>0\). For perturbations through degree two, record
\[
\lambda_0-\lambda_2=e^{-s}\left(s+\frac{s^2}{2}\right)=\frac{s(s+2)e^{-s}}2.
\]
By analytic perturbation theory for a simple isolated eigenvalue, its spectral projection and phase-normalized eigenvector vary real analytically for small \(|t|\).

**2. Two matrix derivatives.** For the Gaussian basis vector,
\[
P_{00}(t)=\frac1{2\pi}\int_0^s\!\int_0^{2\pi}
\exp\bigl[-v(\cosh(2t)+\sinh(2t)\cos2\theta)\bigr]\,d\theta\,dv.
\]
Since the angular average of \(\cos2\theta\) vanishes and its mean square is \(1/2\), the coefficient of \(t^2\) in the integrand is \(e^{-v}(v^2-2v)\). An integration by parts gives
\[
\int_0^s e^{-v}(v^2-2v)\,dv=-s^2e^{-s};
\quad P'_{00}(0)=0,\quad P''_{00}(0)=-2s^2e^{-s}.
\]
The first variation of an off-diagonal entry \(P_{n0}\) has only angular frequencies \(\pm2\). Orthogonality forces \(P'_{n0}(0)=0\) for every \(n\ne2\). Explicitly differentiating \(\overline{z}^2\) and the Gaussian weight gives
\[
P'_{20}(0)=\frac1{\sqrt2}\int_0^s e^{-v}(2v-v^2)\,dv
=\frac{s^2e^{-s}}{\sqrt2}.
\]
The same computation gives its complex conjugate \(P'_{02}(0)\), which is real.

**3. Perturbed optimum, not merely a Gaussian trial.** The standard Rayleigh–Schrödinger formula for the first eigenvalue of a self-adjoint analytic family, using the complete unperturbed eigenbasis, reads
\[
\lambda_{\max}''(0)=P''_{00}(0)+2\sum_{n\ge1}
\frac{|P'_{n0}(0)|^2}{\lambda_0-\lambda_n}.
\]
Only the \(n=2\) summand survives, so
\[
\lambda_{\max}''(0)=-2s^2e^{-s}
+2\frac{s^4e^{-2s}/2}{s(s+2)e^{-s}/2}
=-\frac{4s^2e^{-s}}{s+2}.
\]
The eigenvector derivative in the phase convention of the theorem is
\[
f'_{s,0}=\sum_{n\ge1}\frac{P'_{n0}(0)}{\lambda_0-\lambda_n}h_n
=\frac{\sqrt2s}{s+2}h_2.
\]
A quarter-turn \(z\mapsto iz\) carries \(E_{s,t}\) to \(E_{s,-t}\) and is unitarily implemented on Fock space; thus \(\lambda_{\max}(t)=\lambda_{\max}(-t)\). Real analyticity excludes all odd powers and improves the eigenvalue remainder to \(O_s(t^4)\). The normalized eigenvector remainder is \(O_s(t^2)\) in the Hilbert norm.

**4. Area of greatest sensitivity.** For \(c(s)=2s^2e^{-s}/(s+2)\), its logarithmic derivative is
\[
\frac{c'(s)}{c(s)}=\frac2s-1-\frac1{s+2}
=\frac{4-s-s^2}{s(s+2)}.
\]
There is exactly one positive root \(s_\ast=(\sqrt{17}-1)/2\). Since \(c(s)\to0\) at both \(s\downarrow0\) and \(s\to\infty\), it is the unique global maximizer. This finishes the proof.

## Verification
The standalone `check_elliptic_stft.py` independently integrates the Fock Gram matrix over area-preserving ellipses using Gauss–Legendre radial nodes and uniform angular cubature, diagonalizes its finite leading sections, and tests the analytic derivative and eigenvector predictions. Execute with Python, NumPy and SciPy: `python check_elliptic_stft.py`. The verified run returned `ELLIPSE_STFT_CURVATURE_CHECKS_PASS 148`. Evaluated areas were \(s\in\{0.4,1,3,5\}\), with small positive deformations \(t\in\{0.005,0.01,0.02\}\). These finite-dimensional numerical checks corroborate but do not prove the result. The infinite-dimensional assertion is proved by the analytic trace-class family, exact disk spectrum, and first two matrix derivatives above.

## Relationship to prior work
Nicola and Tilli proved the globally sharp Gaussian STFT Faber–Krahn inequality and the exact disk optimizer. That pre-existing theorem yields the zeroth-order value and strict deficit away from disks, but not the local sharp coefficient or optimal signal derivative on a fixed anisotropic ellipse. Gómez, Guerra, Ramos and Tilli proved quantitative stability estimates; their 2023 preprint explicitly notes the lack of known first eigenfunctions even for ellipses of small eccentricity (Introduction, p. 4). Their second variations involve *signal-determined superlevel sets*, not this fixed area-preserving ellipse's optimized eigenvalue. Ramos's 2026 inverse/free-boundary paper also constructs perturbed domains and establishes quadratic deficit orders and local rigidity, but does not state the exact ellipse curvature or the first Hermite response for fixed ellipses. Abreu and Dörfler supply the inverse Hermite-eigenfunction disk-rigidity theorem, not an ellipse perturbation coefficient. Our claim is only the explicit local ellipse expansion, its optimal eigenfunction, and its immediate area-curvature consequence; none of the general disk extremality, stability exponents or inverse results is new here.

## Limitations
Historical originality remains provisional; implicit specializations of general spectral shape derivatives could reproduce the coefficient. The conclusions apply to one-dimensional signals, the normalized Gaussian window, centered axis-aligned ellipses with determinant-one linear shape change, and fixed area. Rotated ellipses have the same eigenvalues by symmetry, with the Hermite correction transformed accordingly. No exact finite-eccentricity eigenfunction, arbitrary-shape sharp Hessian, non-Gaussian-window result, finite-sampling guarantee, or uniform-in-area remainder is claimed. Independent mathematical validation has not been performed.

## References
1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the Short-time Fourier transform*, original arXiv posting 2021-06-07, arXiv:2106.03423, https://arxiv.org/abs/2106.03423.
2. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber-Krahn inequality for the Short-time Fourier Transform*, first posted 2023-07-18, arXiv:2307.09304v1, https://arxiv.org/abs/2307.09304.
3. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, first posted 2026-07-23, arXiv:2607.21590, https://arxiv.org/abs/2607.21590.
4. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841, https://arxiv.org/abs/1202.5841.
