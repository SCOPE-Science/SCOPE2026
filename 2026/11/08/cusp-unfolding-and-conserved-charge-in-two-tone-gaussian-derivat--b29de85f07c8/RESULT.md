# Cusp unfolding and conserved charge in two-tone Gaussian-derivative spectrogram zeros

## Finding
For every integer \(n\ge1\), a superposition of two nonzero complex sinusoidal tones analyzed with the \(n\)-th Gaussian-derivative window has precisely three, four, or five zeros on one fundamental time-frequency cylinder. The transition is an **exact cusp curve controlled by the tone-amplitude ratio**. At the transition the two colliding zeros have opposite signed indices, while the total index of all zeros is always \(-1\).

With \(c=\sigma^2\omega^2\), \(\lambda=\log(|a|/|b|)\), and, for \(c>n\),
\[
 v=\sqrt{1-n/c},\qquad H_n(c)=2\bigl(cv-n\operatorname{artanh}v\bigr),
\]
the number of **distinct** zeros per cylinder is
\[
 \#Z=\begin{cases}
 5,&c>n\ \text{and}\ |\lambda|<H_n(c),\\
 4,&c>n\ \text{and}\ |\lambda|=H_n(c),\\
 3,&\text{otherwise}.
 \end{cases}
\]
The four-zero case has exactly one double-fold zero; the three-zero case is regular except at \((c,\lambda)=(n,0)\), where its unique interior zero has cubic tangency and index \(+1\). Every ordinary zero has index \(+1\) or \(-1\) as specified below. There are no other collisions or zeros. The cusp opens according to
\[
 H_n(n+\delta)=\frac{4}{3\sqrt n}\delta^{3/2}\bigl(1+O_n(\delta)\bigr),\qquad \delta\downarrow0.
\]
Equivalently, for sufficiently small fixed nonzero \(|\lambda|\), the frequency-separation threshold obeys
\[
 c_*(\lambda)-n=\left(\frac{3\sqrt n}{4}|\lambda|\right)^{2/3}(1+o(1)).
\]
This is an amplitude-asymmetry unfolding of the equal-amplitude first-derivative transition, rather than a second claim to that already-known symmetric result.

## Assumptions and scope
Fix \(n\in\mathbb N\), \(n\ge1\), \(\sigma,\omega>0\), and complex \(a,b\ne0\). Define
\[
 f(s)=a e^{i\omega s}+b e^{-i\omega s},\qquad
 g_{n,\sigma}(s)=\frac{d^n}{ds^n}\exp\bigl(-s^2/(2\sigma^2)\bigr),
\]
and the non-conjugating (real-window) short-time Fourier transform
\[
 V(t,\xi)=\int_{\mathbb R}f(s)g_{n,\sigma}(s-t)e^{-i\xi s}\,ds.
\]
Although \(f\) is bounded rather than square-integrable, the integral is absolutely convergent for each real \(t,\xi\). We identify times modulo \(\pi/\omega\), since zeros are unchanged by that translation. The Gaussian-derivative windows are Hermite-polynomial multiples of a Gaussian, but for \(n\ge2\) they are **not** the same as the conventional orthonormal Hermite-function sequence. All multiplicities refer to the one-dimensional transverse frequency equation; at degenerate zeros we additionally state the local topological degree of the full two-dimensional real map. Charges are computed using orientation \(dt\wedge d\xi\).

## Proof
**Exact reduction.** Fourier transformation of a Gaussian derivative gives, with a nonzero common factor,
\[
 V(t,\xi)=\sqrt{2\pi}\sigma i^n e^{-i\xi t}\left[
 a(\xi-\omega)^n e^{-\sigma^2(\xi-\omega)^2/2}e^{i\omega t}
 +b(\xi+\omega)^n e^{-\sigma^2(\xi+\omega)^2/2}e^{-i\omega t}
 \right].
\]
At \(\xi=\pm\omega\), exactly one bracketed summand is zero, so the transform is nonzero. Set \(u=\xi/\omega\ne\pm1\). The bracket vanishes exactly when
\[
 e^{2i\omega t}=-\frac ba\left(\frac{u+1}{u-1}\right)^n e^{-2cu}.
\]
Consequently the modulus condition is the real equation
\[
 F(u)=\lambda+n\log\left|\frac{u-1}{u+1}\right|+2cu=0.
\]
Conversely every real root of \(F\) determines **one and only one** time modulo \(\pi/\omega\) through the displayed phase equation, so the root count is exactly the two-dimensional zero count.

**Classification of real roots.** Differentiation on the three components of \(\mathbb R\setminus\{-1,1\}\) gives
\[
 F'(u)=2c+\frac{2n}{u^2-1}.
\]
On each exterior component \(F'>0\); \(F\) runs from \(-\infty\) to \(+\infty\) and therefore has one simple root on each. On \((-1,1)\) the function runs from \(+\infty\) to \(-\infty\). If \(c\le n\), it is strictly decreasing except for the single stationary point when \(c=n\); there is one interior root. If \(c>n\), the only stationary points are \(\pm v\), with a minimum at \(-v\) and a maximum at \(v\). Direct substitution gives \(F(-v)=\lambda-H_n(c)\), \(F(v)=\lambda+H_n(c)\). Thus the interior has three simple roots exactly for \(|\lambda|<H_n(c)\), two distinct roots (one double) on equality, and one simple root otherwise. In the three-interior-root regime the derivative signs from left to right are \(-,+,-\).

**Degeneracies and charges.** At the equality boundary with \(c>n\), the stationary point is nonzero, and
\[
 F''(u)=-\frac{4nu}{(u^2-1)^2}
\]
is nonzero there. Thus the degenerate root has quadratic fold type. At \(c=n\), the unique stationary point is \(u=0\); it is a root only if \(\lambda=0\). The convergent local expansion
\[
 F(u)=\lambda+2(c-n)u-\frac{2n}{3}u^3+O_n(u^5)
\]
proves cubic tangency at that cusp and excludes any additional degeneracies.

For a simple zero, factor out the harmless nonvanishing complex scalar and denote the two bracketed terms by \(X\) and \(Y\). At a zero \(X=-Y=:z\ne0\), with \(\partial_t(X+Y)=2i\omega z\), and \(\partial_\xi(X+Y)=zF'(u)/\omega\). Therefore
\[
 \det D_{(t,\xi)}(\Re V,\Im V)=-2|Cz|^2 F'(u),
\]
where \(C\) is the nonzero common Fourier prefactor; derivatives of \(C\) vanish from the Jacobian expression at zeros. Hence the local index is \(-\operatorname{sgn} F'(u)\). Both exterior zeros have index \(-1\). The interior simple zeros have total index \(+1\), whether there is one (index \(+1\)) or three (indices \(+1,-1,+1\)). At a quadratic fold the two nearby opposite-index zeros merge, giving degree zero, with the remaining interior zero of degree \(+1\). At the cubic cusp, the transverse cubic crosses from positive to negative, hence has degree \(+1\). In all cases the cylinder total is \(-1\).

**Sharp cusp opening.** Put \(\delta=c-n\). Since \(v^2=\delta/(n+\delta)\) and \(\operatorname{artanh}v=v+v^3/3+O(v^5)\), elementary substitution into \(H_n\) yields the displayed \(4/(3\sqrt n)\) coefficient. Moreover \(H_n'(c)=2v>0\) for \(c>n\), so for every \(\lambda\ne0\) there is a unique threshold \(c_*(\lambda)>n\) defined by \(H_n(c_*)=|\lambda|\). Inverting the asymptotic gives the \(2/3\) law. This completes the classification for all stated parameters.

## Verification
The standalone `CHECK.py` uses only the Python standard library. Running `python CHECK.py` verifies the exact root-count pattern and signed-index sum for 52 noncritical parameter configurations of derivative orders \(1,2,3,5\), checks the Fourier formula by independent Simpson quadrature for derivative orders \(1,2,3,4\), and tests fold identities and the leading cusp coefficient. It prints `ALL_CUSP_ZERO_CHECKS_PASSED`. These checks corroborate but do not replace the proof for every \(n\) and every parameter.

## Relationship to prior work
Bellourak, Meignen, Polisano, and Nahon (2026), *Zeros of the Spectrogram of White Noise with Hermite Windows*, use signed Jacobian charge for the random white-noise spectrogram with **orthonormal Hermite windows**. Their source concerns a random field, not the present deterministic Gaussian-derivative two-tone zero count or amplitude-unfolding curve. Poinas and Bardenet (2025), *On two fundamental properties of the zeros of spectrograms of noisy signals*, analyze unequal-amplitude pairs of chirps with a **Gaussian** analysis window, finding a line of zeros, rather than a cusp with opposite-charge collisions. Meignen, Laurent, and Oberlin (2022), *One or Two Ridges?*, address separation of Gaussian-window spectrogram ridges, rather than zeros for Gaussian-derivative windows.

The equal-amplitude first-derivative three-to-five transition \((n,\lambda)=(1,0)\) is treated as background in this analysis; the present contribution is the complete **unequal-amplitude fold boundary** together with its cubic cusp, degree bookkeeping, and arbitrary Gaussian derivative order. Specializing the new formulas to that earlier case is not claimed as novel. The prior literature does not establish priority for this statement; independent comparison remains necessary.

## Limitations
The result concerns exactly two pure frequencies and Gaussian-derivative analysis windows, not random signals, orthonormal higher Hermite windows, finite-duration recordings, noise, or generic multimode mixtures. It counts exact mathematical zeros on an infinite-frequency cylinder; spectral truncation or numerical thresholding can alter observed counts. Local index at a fold is zero, not a pair of individually defined nondegenerate charges. The classification does not by itself prove stability of zero detection under perturbations. A substantially equivalent bifurcation might appear elsewhere in time-frequency or catastrophe-theory literature; scholarly priority remains subject to independent verification.

## References
1. C. Bellourak, S. Meignen, K. Polisano and M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows* (first public 2026-10-09), arXiv:2610.13531, https://arxiv.org/abs/2610.13531.
2. A. Poinas and R. Bardenet, *On two fundamental properties of the zeros of spectrograms of noisy signals* (2025), arXiv:2507.13829, https://arxiv.org/abs/2507.13829.
3. S. Meignen, N. Laurent and T. Oberlin, *One or Two Ridges? An Exact Mode Separation Condition for the Gabor Transform*, IEEE Signal Processing Letters 29 (2022), 2507–2511, DOI:10.1109/LSP.2022.3226948.
