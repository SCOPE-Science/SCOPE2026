# Bernstein circle covariances: exact parity ranks and sharp odd–even sampling constants

## Finding
Let \(n\ge1\) be fixed and let \(f:[0,\pi]\to\mathbb R\) be continuous and positive definite on the circle, with the absolutely convergent Schoenberg expansion
\[
f(\theta)=b_0+\sum_{m\ge1}b_m\cos(m\theta),\qquad b_m\ge0.
\]
Define its degree-\(n\) Bernstein approximant
\[
g(\theta)=\sum_{r=0}^{n}\binom nr(\theta/\pi)^r(1-\theta/\pi)^{n-r}f(r\pi/n),
\]
and the two endpoint-displacement masses
\[
D_0=\sum_{\substack{m\ge1\\m\text{ even}}}b_m[1-\cos(m\pi/n)],\qquad
D_1=\sum_{\substack{m\ge1\\m\text{ odd}}}b_m[1-\cos(m\pi/n)].
\]
Write \(\beta_0=\pi^{-1}\int_0^\pi g(\theta)\,d\theta\) and \(\beta_k=2\pi^{-1}\int_0^\pi g(\theta)\cos(k\theta)\,d\theta\) for \(k\ge1\).

**Spectral-support and strictness theorem.** For every \(k\ge1\), \(\beta_k>0\) if and only if \(D_{k\bmod2}>0\); otherwise \(\beta_k=0\). In particular, the radial kernel \((z,w)\mapsto g(d_{S^1}(z,w))\) is strictly positive definite for every finite set of distinct circle points **if and only if** \(D_0D_1>0\).

**Finite-grid ranks.** Let \(N\ge2\), \(\omega_j=e^{2\pi i j/N}\), and \(G_N=[g(d_{S^1}(\omega_j,\omega_\ell))]_{j,\ell=0}^{N-1}\). If \(N\) is odd, \(G_N\) has rank \(N\) whenever \(D_0+D_1>0\); if both vanish its rank is \(\mathbf1_{\{\beta_0>0\}}\). If \(N\) is even, its rank is: \(N\) when both masses are positive; \(N/2\) when only \(D_0>0\); \(N/2+\mathbf1_{\{\beta_0>0\}}\) when only \(D_1>0\); and \(\mathbf1_{\{\beta_0>0\}}\) when both vanish. All cases include \(N=2\).

**Sharp large-grid laws.** For \(\lambda_N=\lambda_{\min}(G_N)\), along the respective subsequences,
\[
\boxed{\lim_{\substack{N\to\infty\\N\text{ even}}}N\lambda_N=2n\min(D_0,D_1),\qquad
\lim_{\substack{N\to\infty\\N\text{ odd}}}N\lambda_N=\frac n2(\sqrt{D_0}+\sqrt{D_1})^2.}
\]
Thus an approximant supported in just one nonconstant Fourier parity is singular on all sufficiently large even grids but has a strictly positive \(N^{-1}\)-scale lower eigenvalue on odd grids. When both masses are positive, the odd-grid limiting constant is strictly larger unless \(D_0=D_1\).

## Assumptions and scope
The circle has geodesic distance in \([0,\pi]\). All Gram matrices use unnormalized kernel entries, not an additional factor \(1/N\). The Bernstein degree \(n\) and input \(f\) are fixed while \(N\to\infty\). The coefficients \(b_m\) are nonnegative and summable; the zero input is allowed. The rank theorem is exact for every \(N\ge2\). The asymptotic laws do not claim uniformity as \(n\), \(f\), or a sample geometry changes with \(N\).

## Proof
**1. Strict positivity of the basis-image Fourier coefficients.** For \(m\ge1\), the degree-\(n\) Bernstein image of \(\cos(m\theta)\), after \(t=\theta/\pi\), is
\[
Q_{n,m}(t)=\operatorname{Re}(1-t+t\zeta)^n,\qquad \zeta=e^{im\pi/n}.
\]
Its samples depend only on the folded residue \(m^\sharp=\min\{m\bmod2n,2n-(m\bmod2n)\}\in\{0,\dots,n\}\), which has the parity of \(m\). The case \(m^\sharp=0\) gives the constant polynomial \(1\). For \(1\le m^\sharp\le n\), reflection about \(t=1/2\) makes all opposite-parity positive-frequency cosine coefficients vanish.

For brevity write \(m=m^\sharp\), \(\vartheta=m\pi/(2n)\), and \(J=\lceil n/2\rceil\). For \(k\ge1\) of matching parity, the exact endpoint-integration formula from the source (also obtainable by repeated integrations by parts) is
\[
\beta_k(Q_{n,m})=4n!\sum_{j=1}^{J}\frac{(2\sin\vartheta)^{2j-1}\sin((2j-1)\vartheta)}{(n-2j+1)!(k\pi)^{2j}}.
\]
When \(k\ge m\), the positive coefficients preceding \(\sin((2j-1)\vartheta)\) decrease strictly with \(j\): their adjacent ratio is
\[
\frac{4\sin^2\vartheta\,(n-2j+1)(n-2j)}{(k\pi)^2}<1,
\]
where \(2\sin\vartheta\le m\pi/n\le k\pi/n\). The partial sine sums equal \(\sin^2(j\vartheta)/\sin\vartheta\ge0\), with the first strictly positive. Summation by parts proves \(\beta_k>0\); when \(J=1\), its single term is directly positive.

For \(1\le k<m\) of matching parity, the same source's exact remainder formula reads
\[
\beta_k(Q_{n,m})=\frac{4n}{k\pi}\int_0^1 (1-u)^{n-1}\cosh(au)\sin(bu)\,du,
\qquad a=\frac{k\pi}2\cot\vartheta,\quad b=\frac{k\pi}2.
\]
Here \(n\ge2\) and \(0\le a\le n-1\), by \(\tan\vartheta\ge\vartheta\) and \(k<m\le n\). The weight \(w(u)=(1-u)^{n-1}\cosh(au)\) is positive and strictly decreasing for \(0<u<1\), because
\[
(\log w)'=-\frac{n-1}{1-u}+a\tanh(au)<0.
\]
Writing \(W(v)=w(v/b)\), integration by parts gives
\[
\int_0^b W(v)\sin v\,dv=W(b)(1-\cos b)-\int_0^bW'(v)(1-\cos v)\,dv>0.
\]
The endpoint term is nonnegative, while the integral is strictly positive. Thus every parity-compatible coefficient is strictly positive, not just nonnegative. Nonnegative summation over the \(b_m\) proves the stated support equivalence.

**2. Mean and Fourier tails.** Direct integration gives \(\beta_0(Q_{n,m})=0\) if \(m\) is odd, \(1/(n+1)\) if its folded residue is positive even, and \(1\) if its folded residue vanishes. Hence \(\beta_0\ge0\). Let \(P(t)=g(\pi t)\). The Bernstein endpoint derivatives are
\[
P'(0)=-n(D_0+D_1),\qquad P'(1)=n(D_0-D_1).
\]
Twice integrating by parts, then repeating to the end of the fixed-degree polynomial, gives the exact finite inverse-even-power expansion and consequently
\[
\beta_k=\frac{2[(-1)^kP'(1)-P'(0)]}{\pi^2k^2}+O_{n,f}(k^{-4})
=\frac{4nD_{k\bmod2}}{\pi^2k^2}+O_{n,f}(k^{-4}).
\]
If a parity mass vanishes, the corresponding coefficients vanish *exactly*, not merely asymptotically.

**3. Exact cyclic ranks.** Define the two-sided Fourier masses \(c_0=\beta_0\), \(c_{\pm k}=\beta_k/2\) for \(k\ge1\). The circulant eigenvalues of \(G_N\), indexed by \(j=0,\dots,N-1\), are
\[
\Lambda_{N,j}=N\sum_{r\in\mathbb Z}c_{j+rN}.
\]
Every term is nonnegative. If \(N\) is odd, the residue class of any \(j\) contains infinitely many positive integers of each parity, so any nonconstant parity gives strictly positive eigenvalues. If \(N\) is even, all indices in a residue class have the same parity; the odd classes are positive precisely when \(D_1>0\), the nonzero even classes precisely when \(D_0>0\), and the class \(j=0\) is additionally positive when \(\beta_0>0\). This proves all rank formulas.

**4. Strict positive definiteness.** If both masses are positive, every positive-frequency coefficient is positive. For distinct points \(z_1,\ldots,z_L\), a vector with zero quadratic form must satisfy \(\sum_i u_i z_i^k=0\) for all positive integers \(k\). Taking \(k=1,\ldots,L\) gives an invertible Vandermonde matrix, so \(u=0\). Conversely, if only even positive frequencies occur, the kernel has period \(\pi\), hence two antipodal points yield identical rows. If only odd nonconstant frequencies (and possibly a constant) occur, the alternating vector \((1,-1,1,-1)\) on four successive quarter-circle points annihilates the constant and every odd frequency. A constant kernel is never strictly positive definite. This proves necessity and sufficiency.

**5. Sharp parity-dependent limits.** For \(j/N\to u\in(0,1)\), the Fourier tail expansion and absolutely convergent alias sums give the following expressions for \(N\Lambda_{N,j}\), uniformly when \(u\) stays in compact subintervals of \((0,1)\):
\[
N\Lambda_{N,j}=\begin{cases}
\dfrac{2nD_{j\bmod2}}{\sin^2(\pi u)}+o(1),&N\text{ even},\\[8pt]
\dfrac n2\left(\dfrac{D_{j\bmod2}}{\sin^2(\pi u/2)}+
\dfrac{D_{1-j\bmod2}}{\cos^2(\pi u/2)}\right)+o(1),&N\text{ odd}.
\end{cases}
\]
These follow from
\[
\sum_{r\in\mathbb Z}(u+r)^{-2}=\frac{\pi^2}{\sin^2(\pi u)},\quad
\sum_{r\text{ even}}(u+r)^{-2}=\frac{\pi^2}{4\sin^2(\pi u/2)},\quad
\sum_{r\text{ odd}}(u+r)^{-2}=\frac{\pi^2}{4\cos^2(\pi u/2)}.
\]
If both masses are positive, edge indices \(j/N\to0\) or \(1\) cannot minimize because their scaled eigenvalues diverge: a fixed index has \(N\Lambda_{N,j}\asymp N^2\), and a divergent sublinear index has scaled lower bound of order \((N/j)^2\). Both residue parities are dense among interior fractions. On even grids, minimizing \(1/\sin^2(\pi u)\) gives \(2n\min(D_0,D_1)\). On odd grids, minimizing \(A/\sin^2v+B/\cos^2v\) over \(0<v<\pi/2\) gives \((\sqrt A+\sqrt B)^2\), attained at \(\tan^2v=\sqrt{A/B}\).

If exactly one mass is positive, sufficiently large even grids have zero eigenvalues by step 3. For odd grids choose indices of the **inactive** parity with \(j\to\infty\), \(j/N\to0\) to attain the boundary value \(nD_{\mathrm{active}}/2\); the general lower bound follows from the positive active-parity tail in the alias sum. Indices of active parity near the boundary have divergent scaled eigenvalue. When both masses vanish, \(g\) is constant and \(\Lambda_{N,j}=0\) for all nonzero \(j\). These cases complete both limits.

## Verification
The standalone `checker.py` constructs all Bernstein cosine-basis images with high-precision arithmetic for \(1\le n\le9\), tests their exact endpoint-integration Fourier coefficients through frequency \(30\), and compares direct covariance eigenvalues to exact trigonometric formulas for a degree-two mixed-parity example. It also tests convergence toward both predicted limits. The recorded successful run reports 7,807 finite assertions. Numerical checks are supplementary; the all-degree and all-grid claims rely on the proof above.

For the explicit illustration \(n=2\), \(f(\theta)=1+\cos\theta+\cos(2\theta)\), one has \(D_0=2\), \(D_1=1\). Hence \(N\lambda_N\to4\) through even grids, versus \(N\lambda_N\to(1+\sqrt2)^2\) through odd grids. These constants are sharp.

## Relationship to prior work
Otten–Nguyen–Watts (2026) prove that ordinary Bernstein operators preserve circle positive definiteness and derive nonnegative Fourier-basis coefficients. The present finding does not re-claim that theorem: it establishes their **strict** parity support, exact full-rank/singularity classification for all cyclic sampling grids, and two different sharp eigenvalue asymptotics. General strict positive-definiteness criteria for compact abelian groups (Emonds–Führ, 2010) provide background but do not yield these Bernstein-specific constants. Other accessible positive-definite Bernstein sampling work concerns node flexibility or higher-dimensional spheres, rather than this covariance Gram limit. Known cyclic aliasing and reciprocal-square summation identities are used explicitly, not claimed new.

## Limitations
The exact eigenvalue asymptotics assume fixed Bernstein degree and fixed positive-definite input; the theorem does not cover jointly growing degree and grid size, irregular point sets in the quantitative part, or higher-dimensional spheres. The source's coefficient formula is a stated starting identity, reconstructed above by endpoint integration. Older equivalent periodic-spline or covariance discretization formulas may exist beyond the inspected sources; no claim of worldwide priority or independent external certification is made.

## References
1. M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, first public August 5, 2026, arXiv:2608.04836. https://arxiv.org/abs/2608.04836
2. J. Emonds, H. Führ, *Strictly positive definite functions on compact abelian groups*, arXiv:1002.3017 (2010). https://arxiv.org/abs/1002.3017
3. *Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle*, public record dated November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quadratic-rigidity-and-cubic-node-freedom-for-positive-definite--b87f6c90a4aa
