# A nonuniform DCT limit for the AR(1) KLT under growing block length

## Result

Let
\[
R_N(\rho)=\big[\rho^{|i-j|}\big]_{i,j=0}^{N-1},\qquad 0\le \rho<1,
\]
and let \(w_N(\rho)\) be the unit eigenvector associated with the largest eigenvalue, chosen with positive entries. Let
\[
d_N=N^{-1/2}(1,\ldots,1)^T
\]
be the first DCT-II basis vector. For a sequence \(\rho_N\in[0,1)\), define
\[
\kappa_N=\frac{2N(1-\rho_N)}{1+\rho_N}.
\]
Then the alignment of the principal AR(1) KLT mode with the DCT-II DC mode has a sharp double-scaling limit.

If \(\kappa_N\to a\in[0,\infty)\), let \(\xi(a)\in[0,\pi)\) be the unique solution of
\[
\boxed{\xi\tan(\xi/2)=a.}
\]
Then
\[
\boxed{
\langle w_N(\rho_N),d_N\rangle
\longrightarrow
C(a):=
\frac{2\sin(\xi/2)/\xi}
{\sqrt{\tfrac12+\tfrac{\sin\xi}{2\xi}}},
\qquad \xi=\xi(a).
}
\]
At \(a=0\), the continuous value is \(C(0)=1\). If \(\kappa_N\to\infty\), then
\[
\boxed{
\langle w_N(\rho_N),d_N\rangle
\longrightarrow \frac{2\sqrt2}{\pi}.
}
\]
Consequently,
\[
\boxed{
\|w_N(\rho_N)-d_N\|_2\to0
\quad\Longleftrightarrow\quad
N(1-\rho_N)\to0.
}
\]
Thus the classical fixed-block statement \(\rho\to1\Rightarrow\mathrm{KLT}\to\mathrm{DCT\mbox{-}II}\) is not uniform in block length. In particular, \(\rho_N\to1\) alone is insufficient.

For the canonical local-to-unity scaling \(\rho_N=e^{-a/N}\), \(a>0\), the limiting first KLT mode is nonconstant and has a strictly positive angle from the DCT DC vector. If \(N(1-\rho_N)\to\infty\) while \(\rho_N\to1\), for example \(\rho_N=1-N^{-1/2}\), the limiting alignment is \(2\sqrt2/\pi\), so the optimal-sign row distance tends
\[
\boxed{
\sqrt{2-\frac{4\sqrt2}{\pi}}
=0.446505730854\ldots .
}
\]
This gives an operator-norm obstruction as well: after aligning row signs, the difference between the KLT and DCT-II transform matrices has spectral norm at least the distance between their first rows. Hence the fixed-\(N\) DCT endpoint cannot hold uniformly in \(N\) in any norm controlling individual basis vectors.

## Derivation

Reznik's phase equation for the AR(1) covariance gives, for the principal mode,
\[
(N+1)\omega+2\theta(\omega)=\pi,
\qquad
\theta(\omega)=\arg(1-\rho e^{-i\omega}),
\]
and the eigenvector entries are proportional to
\[
\sin\big(\omega(k+1)+\theta(\omega)\big).
\]
Eliminating \(\theta\) from the principal-mode equation gives the centered form
\[
w_k\propto \cos\!\left(\omega\left(k-\frac{N-1}{2}\right)\right).
\]
The symmetric secular equation is
\[
\cos\frac{(N+1)\omega}{2}
=\rho\cos\frac{(N-1)\omega}{2}.
\]
Writing \(\xi_N=N\omega\), elementary trigonometry yields the exact scalar identity
\[
\boxed{
2N\tan(\xi_N/2)\tan(\xi_N/(2N))=\kappa_N.
}
\]
For \(0<\xi<\pi\), the left-hand side is strictly increasing in \(\xi\). On compact subintervals of \([0,\pi)\),
\[
2N\tan(\xi/(2N))\tan(\xi/2)
\longrightarrow
\xi\tan(\xi/2).
\]
This proves \(\xi_N\to\xi(a)\) when \(\kappa_N\to a<\infty\). If \(\kappa_N\to\infty\), monotonicity forces \(\xi_N\to\pi\).

The overlap with the constant DCT vector can be summed exactly. For the normalized centered cosine above,
\[
\boxed{
C_N=
\frac{\sin(N\omega/2)/\sin(\omega/2)}
{\sqrt{N\left[N/2+\sin(N\omega)/(2\sin\omega)\right]}}.
}
\]
Substituting \(N\omega\to\xi\) gives the stated \(C(a)\). Since the limiting profile \(t\mapsto\cos(\xi(t-1/2))\) is nonconstant for every \(\xi>0\), Cauchy-Schwarz is strict and \(C(a)<1\) for every \(a>0\). Because
\[
\frac{2N(1-\rho_N)}{1+\rho_N}\to0
\quad\Longleftrightarrow\quad
N(1-\rho_N)\to0,
\]
the iff criterion follows.

The two iterated limits therefore do not commute:
\[
\boxed{
\lim_{N\to\infty}\lim_{\rho\uparrow1} C_N(\rho)=1,
\qquad
\lim_{\rho\uparrow1}\lim_{N\to\infty} C_N(\rho)=\frac{2\sqrt2}{\pi}.
}
\]

## Eigenvalue scaling and correlation-length interpretation

Let \(\lambda_{1,N}\) be the largest eigenvalue of \(R_N(\rho_N)\). From the exact formula
\[
\lambda_{1,N}
=
\frac{1-\rho_N^2}
{1-2\rho_N\cos\omega_N+\rho_N^2},
\]
if \(N(1-\rho_N)\to a<\infty\), then
\[
\boxed{
\frac{\lambda_{1,N}}{N}
\longrightarrow
\frac{2a}{a^2+\xi(a)^2}
=\frac{\sin\xi(a)}{\xi(a)}.
}
\]
The last equality uses \(a=\xi\tan(\xi/2)\).

When \(\rho_N=e^{-a/N}\), the covariance entries are exactly
\[
\rho_N^{|i-j|}=e^{-a|i-j|/N},
\]
so the matrix is a uniform-grid discretization of the classical exponential covariance kernel on a unit interval. The parameter \(N(1-\rho_N)\sim a\) is therefore block length divided by correlation length. The limiting principal profile is the standard exponential-kernel KL eigenfunction with Robin boundary conditions. That continuum eigenproblem is classical; the point here is the resulting sharp nonuniformity criterion for the discrete KLT-to-DCT approximation.

For small \(a\),
\[
\xi(a)^2=2a-\frac{a^2}{3}+O(a^3),
\qquad
C(a)=1-\frac{a^2}{360}+O(a^3),
\]
so
\[
\boxed{
\|w_N-d_N\|_2\sim\frac{a}{\sqrt{180}}
}
\]
in the local-to-unity limit followed by \(a\downarrow0\). This quantifies how small the block-length/correlation-length ratio must be for the principal DCT mode to be a close geometric approximation.

## Relation to exact fast AR(1) KLT factorizations

Reznik (2026) factors the exact AR(1) KLT into a butterfly, fixed DCT-II/DCT-IV cores, and \(\rho\)-dependent orthogonal correction factors, and notes that for fixed \(N\) the corrections tend to identities as \(\rho\to1\). The theorem above identifies a nonuniform regime hidden by that fixed-size limit: along \(\rho_N=e^{-a/N}\) with fixed \(a>0\), even the first KLT basis vector retains a nonzero angle from the corresponding DCT-II basis vector. Thus omitting the correction cannot be uniformly accurate over growing block sizes in a norm that controls individual transform rows.

This does not contradict the classical statements that DCT and AR(1) KLT are asymptotically equivalent in transform-coding or other aggregate senses. It distinguishes those weaker performance notions from basis-vector or operator-norm convergence.

## Verification

`artifacts/verify_local_to_unity.py` evaluates the exact phase equation, the closed-form overlap, and the eigenvalue formula, and compares them with dense symmetric eigendecomposition of \(R_N(\rho)\). It also checks the local-to-unity limits, a diagonal sequence with \(\rho_N\to1\) but \(N(1-\rho_N)\to\infty\), fixed-\(\rho\) convergence, and the small-\(a\) distance expansion. The included output was produced with Python 3.13.5 and NumPy 2.3.5.

Among the checked local-to-unity cases, the largest discrepancy between the closed-form principal overlap and direct eigendecomposition was \(6.661\times10^{-16}\); the largest discrepancy for \(\lambda_1/N\) was \(1.293\times10^{-10}\). For \(a=1\), the limiting values are
\[
\xi=1.306542374189\ldots,
\quad
C=0.997807929634\ldots,
\quad
\lambda_1/N=0.738810809416\ldots.
\]

## Limitations

The sharp iff statement concerns the principal KLT basis vector. It proves nonuniformity of the full transform through a one-row lower bound, but it does not characterize the full spectral norm, Frobenius norm, coding gain, or rate-distortion penalty of dropping all correction factors. Classical transform-coding asymptotic equivalence can therefore coexist with the rowwise obstruction established here.

The continuum exponential-covariance eigenproblem and its Robin eigenfunctions are classical and are not claimed as new. The main originality claim is the explicit growing-block double-scaling law, the exact principal-mode overlap limit, the iff criterion \(N(1-\rho_N)\to0\) for DCT-DC convergence, and their interpretation as a nonuniformity obstruction for the new exact factorization's fixed-size DCT endpoint.

## References

1. Y. A. Reznik, “Exact fast factorizations of the AR(1) Karhunen-Loève transform,” arXiv:2609.20221v1, 2026. https://arxiv.org/abs/2609.20221
2. A. K. Jain, “A Sinusoidal Family of Unitary Transforms,” IEEE Transactions on Pattern Analysis and Machine Intelligence, 1(4), 356–365, 1979. DOI: 10.1109/TPAMI.1979.4766944.
3. R. J. Clarke, “Relation between the Karhunen-Loève and cosine transforms,” IEE Proceedings F, 128(6), 359–360, 1981. DOI: 10.1049/ip-f-1.1981.0061.
4. M. U. Torun and A. N. Akansu, “An Efficient Method to Derive Explicit KLT Kernel for First-Order Autoregressive Discrete Process,” IEEE Transactions on Signal Processing, 61(15), 3944–3953, 2013. DOI: 10.1109/TSP.2013.2265225.
5. C. Safta and H. N. Najm, “Numerical Considerations for the Construction of Karhunen-Loève Expansions,” arXiv:2603.19108, 2026. https://arxiv.org/abs/2603.19108
