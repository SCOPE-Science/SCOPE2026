# Three-band rigidity and a sharp triple-collision law for periodic Fourier interpolation

## Finding

For every integer \(m\geq1\), set \(N=3m\). For \(0\leq\varepsilon<1\), evaluate the complete degree-\((N-1)\) Fourier basis at the \(N\) distinct points
\[
x_{3j}=\frac{3j+\varepsilon}{N},\qquad
x_{3j+1}=\frac{3j+1}{N},\qquad
x_{3j+2}=\frac{3j+2-\varepsilon}{N}
\qquad (0\leq j<m).
\]
Let \(F_{\varepsilon,N}\) be the normalized sampling matrix, with rows indexed by the sampling nodes and columns by Fourier frequencies:
\[
(F_{\varepsilon,N})_{\ell,k}=N^{-1/2}\exp(2\pi i kx_{\ell}),\qquad 0\leq\ell,k<N.
\]
Define \(\theta=2\pi(1-\varepsilon)/3\),
\[
a=\frac{1+2\cos\theta}{3},\qquad b=\frac{1+2\cos(2\theta)}{3},\qquad
\Delta=\sqrt{\frac{b^2}{4}+2a^2}.
\]
The complete squared singular spectrum consists, for every \(m\), of exactly the three values
\[
\lambda_-=1+\frac b2-\Delta,\qquad
\lambda_{\rm odd}=1-b,\qquad
\lambda_+=1+\frac b2+\Delta,
\]
each with multiplicity \(m\), with multiplicities combined at a degeneracy. For \(0<\varepsilon<1\), the least squared singular value is \(\lambda_-\). The largest switches from \(\lambda_{\rm odd}\) for \(0<\varepsilon<1/4\) to \(\lambda_+\) for \(1/4<\varepsilon<1\). The only interior band degeneracy is \(\varepsilon=1/4\), where \((\lambda_-,\lambda_{\rm odd},\lambda_+)=(1/3,4/3,4/3)\).

Writing \(t=1-\varepsilon\), the sharp triple-collision asymptotics as \(t\downarrow0\) are
\[
\sigma_{\min}(F_{\varepsilon,N})
=\frac{4\pi^2}{27\sqrt3}\,t^2(1+O(t^2)),\qquad
\kappa_2(F_{\varepsilon,N})
=\frac{81}{4\pi^2}\,t^{-2}(1+O(t^2)),
\]
with constants and remainders independent of \(m\). At the collision endpoint \(\varepsilon=1\), exactly \(m\) distinct nodes remain; the sampling matrix has rank \(m\) and squared singular levels \(0,0,3\), each repeated \(m\) times.

## Assumptions and scope

The Fourier frequencies are precisely the \(N\) consecutive integers \(0,\ldots,N-1\), the sampling weights are all \(1/N\), and the sample positions have the specified symmetric three-periodic pattern. No claim is made for arbitrary jitter, other frequency sets, or weighted least squares. The conclusions hold for every \(m\ge1\) and every real \(\varepsilon\) in the stated interval; their limit at \(\varepsilon=1\) refers to the explicitly defined endpoint matrix.

## Proof

**Polyphase reduction.** Write each frequency as \(k=q+sm\), with \(0\leq q<m\) and \(s\in\{0,1,2\}\). Set \(y_0=\varepsilon\), \(y_1=1\), \(y_2=2-\varepsilon\). At a node indexed \(3j+r\),
\[
(F_{\varepsilon,N})_{3j+r,q+sm}
=\frac{1}{\sqrt m}e^{2\pi i qj/m}
 e^{2\pi i qy_r/N}
 \frac{1}{\sqrt3}e^{2\pi i s y_r/3}.
\]
Applying a unitary \(m\)-point DFT in the \(j\) coordinate to the sample rows separates the \(q\)'s, and unit-modulus row factors remove \(e^{2\pi i q y_r/N}\). The matrix is thus unitarily equivalent to \(m\) identical copies of the \(3\times3\) matrix \(B\) with
\[
B_{r,s}=3^{-1/2}e^{2\pi i s y_r/3}.
\]
This establishes the exact size independence of its three squared singular bands.

**Exact Gram spectrum.** Direct evaluation of the three-term geometric sums shows that \(BB^*\) is unitarily diagonal-gauge equivalent to the real symmetric matrix
\[
G=\begin{pmatrix}1&a&b\\ a&1&a\\b&a&1\end{pmatrix}.
\]
The antisymmetric vector \((1,0,-1)\) has eigenvalue \(1-b\); on the symmetric subspace spanned by \((1,0,1)/\sqrt2\) and \((0,1,0)\), the restriction is
\[
\begin{pmatrix}1+b&\sqrt2 a\\\sqrt2 a&1\end{pmatrix}.
\]
Its quadratic characteristic formula gives \(\lambda_\pm\). Because the three nodes are distinct for \(\varepsilon<1\), the Vandermonde determinant is nonzero, hence all three levels are positive in that range.

**Sharp ordering and unique transition.** For \(0<\varepsilon<1\), we have \(0<\theta<2\pi/3\), so \(a>0\) and \(a-b=\frac23(\cos\theta-\cos2\theta)>0\). If \(b\le0\), then \(\lambda_{\rm odd}>\lambda_-\) immediately; if \(b>0\), use \(a>b\) to obtain \(\Delta>3b/2\), giving the same inequality. Also \(\lambda_+>\lambda_-\). The upper-band difference is \(\lambda_+-\lambda_{\rm odd}=\Delta+3b/2\). If \(b\ge0\) this is positive; if \(b<0\), its sign equals the sign of \(a+b=2a\cos\theta\). Thus its only zero in the open parameter range is \(\theta=\pi/2\), equivalently \(\varepsilon=1/4\); the ordering changes as stated. Substitution gives the three exact threshold values. At \(\varepsilon=0\), \(a=b=0\) and all levels equal one.

**Sharp collision expansion.** Put \(\theta=2\pi t/3\). Elementary Taylor expansion of the explicit radicals gives
\[
\lambda_-=\frac{\theta^4}{27}+O(\theta^6),\quad
\lambda_{\rm odd}=\frac{4\theta^2}{3}+O(\theta^4),\quad
\lambda_+=3+O(\theta^2).
\]
Taking square roots and dividing the largest singular value by the smallest yields the displayed coefficients. As \(t\to0\), the three nodes within each three-point block converge to their common center; their \(m\) centers remain distinct, so the full Fourier sampling matrix has rank \(m\). Equivalently, the limiting \(3\times3\) Gram matrix is all ones and has eigenvalues \(3,0,0\).

## Verification

The self-contained diagnostic file \(checker.py\) constructs the full normalized matrices directly for eight sizes \(N\in\{3,6,9,12,15,18,24,36\}\), compares the first three full-matrix Gram spectral power sums against the predicted bands at eleven perturbations per size, and checks the quarter-threshold and three near-collision limits. Execution completed with 88 full-matrix spectral-moment checks and the supplementary transition/collision checks. Those finite numerical tests do not prove the theorem, which follows from the polyphase decomposition and analytic \(3\times3\) diagonalization above.

## Relationship to prior work

The motivating 2026 study of Chen, Lin, and Zhang develops nearly optimal bounds for singular values of nonuniform Fourier matrices and their links to periodic nonuniform sampling, but its clustered-node theorem assumes a rectangular matrix with at least four times as many Fourier measurements as samples, and its perturbed-grid results give general estimates rather than this exact three-periodic singular spectrum. The 2006 work of Strohmer and Tanner develops reconstruction algorithms for periodic nonuniform sampling and discusses conditioning of interleaved systems, but does not identify the specific symmetric triple-collision law or the sole quarter-step eigenvalue crossing. Prior exact two-periodic, single-pair-collision and frequency-substitution results concern different sampling geometries and do not supply these formulas. This is a statement about the examined comparisons, not a proof that no earlier equivalent formulation exists.

## Limitations

This theorem concerns a structured finite Fourier interpolation family, not arbitrary nonuniform matrices. The asymptotic has a uniform-in-size coefficient only because the three-periodic pattern admits an exact repeated-fiber reduction. It does not assert optimality over all sampling patterns or all reconstruction algorithms. Older specialized polyphase or three-coset calculations may provide equivalent formulas; a complete historical bibliography is not claimed. Independent validation has not been performed.

## References

1. L. Chen, R. Lin and H. Zhang, *Smallest Singular Value Estimates for Nonuniform Fourier Matrices via Periodic Nonuniform Sampling*, arXiv:2608.21960 (first public 2026-08-22), https://arxiv.org/abs/2608.21960.
2. T. Strohmer and J. Tanner, *Fast Reconstruction Methods for Bandlimited Functions from Periodic Nonuniform Sampling*, SIAM Journal on Numerical Analysis 44 (2006), 1073–1094, https://doi.org/10.1137/040609586.
3. A. P. Austin and L. N. Trefethen, *Trigonometric interpolation and quadrature in perturbed points*, SIAM Journal on Numerical Analysis 55 (2017), 2113–2122, https://doi.org/10.1137/16M1106287.
