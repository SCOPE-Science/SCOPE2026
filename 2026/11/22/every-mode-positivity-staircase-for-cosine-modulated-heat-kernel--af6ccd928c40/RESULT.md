# Every-mode positivity staircase for cosine-modulated heat kernels on finite cycles

## Finding
Let \(N\ge3\), \(h=2\pi/N\), and \(t>0\). On the cyclic group \(\mathbb Z/N\mathbb Z\), let \(H_t\) be the heat kernel of the standard combinatorial cycle Laplacian
\[
(Lf)(x)=2f(x)-f(x-1)-f(x+1),\qquad
H_t(x)=\frac1N\sum_{n=0}^{N-1}e^{-2t(1-\cos(nh))}e^{inhx}.
\]
For real \(\beta\), form the translation-invariant Hermitian kernel
\[
K_{t,\beta}(x,y)=H_t(x-y)[1+\beta\cos(h(x-y))].
\]
Define \(A=1-\cos h>0\), \(B=\sin h>0\), and
\[
F_j(t)=e^{-2t A\cos(jh)}\cosh(2t B\sin(jh)),\quad
M=\lfloor N/2\rfloor,\quad J=\lfloor N/4\rfloor+1.
\]
Then for **every** \(N\ge3\) and \(t>0\),
\[
\boxed{K_{t,\beta}\succeq0\ \Longleftrightarrow\
\beta\ge-\frac1{\max_{J\le j\le M}F_j(t)}.}
\]
For each \(j=J,\ldots,M-1\), there exists exactly one finite positive \(t_j\) solving \(F_j(t_j)=F_{j+1}(t_j)\), and the transition times obey
\[
\boxed{0<t_{M-1}<t_{M-2}<\cdots<t_J<\infty.}
\]
Before \(t_{M-1}\) the unique maximizing representative is \(M\); between consecutive times the active representative descends by precisely one, through *all* the indices \(M,M-1,\ldots,J\); after \(t_J\) it is \(J\). At each transition \(t_j\), precisely the adjacent representatives \(j,j+1\) tie. If \(J=M\), the unique representative \(M\) is active for all \(t>0\) and there are no transitions.

At the sharp boundary \(\beta=-1/\max F_j(t)\), the zero eigenvalue frequencies are exactly the cyclic characters represented by the active index or tied indices, together with their negatives modulo \(N\). Thus the boundary circulant matrix has nullity one when the unique active index is \(N/2\) (for even \(N\)), nullity two for any other unique active index, nullity three at a transition involving \(N/2\), and nullity four at all other transitions. Above the sharp boundary all \(N\) eigenvalues are strictly positive; below it at least one eigenvalue is negative.

## Assumptions and scope
The cyclic Laplacian uses jump rate one in each direction; changing the Laplacian normalization rescales time. The parameter \(\beta\) may be any real number. Positive semidefiniteness is tested for all complex vectors on the full finite group (equivalently for all finite-site restrictions). A strict positive definite matrix on the entire finite group means every Fourier eigenvalue is positive. The assertions include all integer orders \(N\ge3\), all positive times, the exact equality boundary, and both odd and even cycle parities. An active representative \(j\in[0,M]\) corresponds to frequencies \(\{j,N-j\}\), a singleton only when \(j=0\) or when \(N\) is even and \(j=N/2\).

## Proof
**1. Exact Fourier reduction.** Fourier diagonalization of the cycle Laplacian gives strictly positive heat multipliers \(a_n=e^{-2t(1-\cos(nh))}\). Multiplication in position by \(1+\beta\cos(hx)\) shifts Fourier coefficients by one:
\[
\lambda_n=a_n+\frac\beta2(a_{n-1}+a_{n+1})
=a_n[1+\beta F_n(t)],
\]
with indices taken modulo \(N\). The addition formulas for cosine give the stated expression for \(F_n\). It is positive, and \(F_n=F_{N-n}\). Hence all eigenvalues are nonnegative if and only if \(\beta\ge-1/F_*(t)\), with \(F_*=\max_{0\le j\le M}F_j\). It remains to determine the unique or tied maximizing indices.

**2. Strict continuous unimodality.** Extend \(F_j\) to
\[
F(\theta)=e^{-u\cos\theta}\cosh(v\sin\theta),\quad
u=2tA>0,\quad v=2tB>0,\quad0\le\theta\le\pi.
\]
The logarithmic derivative is \(u\sin\theta+v\cos\theta\tanh(v\sin\theta)\), strictly positive on \((0,\pi/2]\). For \(\pi/2<\theta<\pi\), set \(y=-\cos\theta\in(0,1)\). Divide the derivative by \(\sin\theta\) to obtain
\[
u-v^2 y\frac{\tanh(v\sqrt{1-y^2})}{v\sqrt{1-y^2}}.
\]
The function \(z\mapsto\tanh(z)/z\) decreases strictly for \(z>0\) (differentiate and use \(\sinh(2z)>2z\)). Because \(\sqrt{1-y^2}\) decreases with \(y\), the product \(y\tanh(v\sqrt{1-y^2})/(v\sqrt{1-y^2})\) is strictly increasing. Therefore the derivative changes sign at most once, from positive to negative. Thus \(F\) increases strictly up to one maximum (possibly the right endpoint) and then decreases strictly. In particular, a tie at two consecutive sampled points forces the continuous maximum strictly between them and those two points are the *only* sampled maximizers.

**3. Each upper-half adjacent comparison crosses once.** For \(J\le j<M\) we have \(\pi/2<jh<(j+1)h\le\pi\). Put \(c_j=\cos(jh)\) and \(s_j=\sin(jh)\). Then \(\Delta c=c_j-c_{j+1}>0\) and \(\Delta s=s_j-s_{j+1}>0\). The logarithmic comparison divided by \(2t\) is
\[
D_j(t)=\frac{\log F_j(t)-\log F_{j+1}(t)}{2t}
=-A\Delta c+\int_{B s_{j+1}}^{B s_j}\tanh(2t w)\,dw.
\]
Every integration variable is nonnegative and the interval has positive length. Thus \(D_j\) strictly increases in \(t\). At \(t\downarrow0\), its limit is \(-A\Delta c<0\); at \(t\to\infty\), the trigonometric addition identities yield
\[
\lim_{t\to\infty}D_j(t)=-A\Delta c+B\Delta s=-2A\cos(jh)>0.
\]
Hence the unique positive root \(t_j\) exists and \(F_j(t)>F_{j+1}(t)\) exactly when \(t>t_j\).

**4. No lower indices can compete.** The strict derivative sign makes \(F_j<F_{j+1}\) whenever \((j+1)h\le\pi/2\). Only the straddling pair \(j=J-1=\lfloor N/4\rfloor\) requires examination. If \(N\equiv0,1\pmod4\), then \(s_j>s_{j+1}\), and the same integral expression for \(D_j\) is increasing but its limiting value is \(-2A\cos(jh)\le0\); hence \(F_j<F_{j+1}\) at every finite positive time. If \(N\equiv2\pmod4\), the sines are equal and the strictly increasing cosine phase favors \(j+1\). If \(N\equiv3\pmod4\), both the cosine exponential and the hyperbolic-cosine factor favor \(j+1\). Consequently the maximizing representative always belongs to \(\{J,\ldots,M\}\).

**5. Ordered, exhaustive transitions.** At \(t=t_j\), Step 2 shows that exactly \(j,j+1\) globally maximize the sampled \(F\). For any \(j'<j\), their sampled \(F_{j'}<F_{j'+1}\) at \(t_j\), so Step 3 implies \(t_j<t_{j'}\). Thus \(t_{M-1}<\cdots<t_J\), without simultaneous crossings. Before the first crossing all upper-half comparisons point toward \(M\); after each successive crossing exactly one comparison reverses; after the last they all point toward \(J\). All intermediate representatives therefore occur, with no skipped mode or triple tie.

**6. Positivity and boundary rank.** Since \(a_n>0\), the eigenvalue \(\lambda_n\) vanishes at the cutoff exactly when \(F_n=F_*\). Steps 2–5 classify those frequencies. Cyclic reflection \(n\mapsto N-n\) gives one, two, three, or four distinct zero eigenvalues as claimed, depending on parity and ties. Every other eigenvalue remains strictly positive at equality. If \(\beta\) falls strictly below the cutoff, any maximizing frequency has negative eigenvalue, proving necessity and sharpness.

## Verification
Run `python3 checker.py`. The dependency-free checker evaluates the stable log-cosh Fourier-ratio identity, brackets each adjacent crossing by bisection, verifies its unique sign orientation and strict ordering, and tests the maximizing mode on numerous times for every \(N=3,\ldots,200\). It reports 200246 assertions passed. At large time for \(N\equiv0\pmod4\), two modes become exponentially close; numerical comparisons permit roundoff-level ties instead of claiming an exact numerical sign. The analytic argument establishes strict inequalities for each finite \(t>0\) and every \(N\ge3\); bounded numerical checks alone do not prove this.

As a representative instance, \(N=12\) has \(J=4\), \(M=6\), and transitions \(t_5\approx0.2881788\) and \(t_4\approx0.4028305\), yielding active representatives \(6\), then \(5\), then \(4\).

## Relationship to prior work
Chinta–Jorgenson–Karlsson–Smajlović (first public arXiv version 2024-09-22) give the discrete Gaussian and cyclic heat spectral/Bessel identities. Karlsson–Neuhauser derive cyclic heat kernels, theta identities, and zeta formulas in earlier work. These give the unmodulated Fourier multipliers used in Step 1, but not the signed multiplicative perturbation or its complete active-frequency phase diagram. Bédos–Conti (2024) study positive Fourier heat multipliers on groups and their smoothing properties, rather than the sharp finite-cycle signed-modulation frontier. The published sampled two-harmonic von Mises spectral-order theorem concerns spatial exponential *sampling* and ordering of its coefficients, not multiplication of the inverse-Fourier cycle heat kernel by a signed first-harmonic mask. Infinite-circle geodesic-exponential modulation and circle-heat modulation have different Fourier laws, infinite character sets, and different phase diagrams; none of their compared statements specializes to this finite-cycle theorem.

## Limitations
The theorem concerns the nearest-neighbor heat semigroup on a single finite cycle and exactly one cosine factor. It does not assert the same ordering for more general graphs, higher harmonic masks, or mixtures of distinct heat times. There is no claimed numerical closed-form expression for the unique transition times; each is specified by a one-variable strictly monotone equation. The historical originality assessment is best-knowledge rather than exhaustive, and independent mathematical review is not performed.

## References
1. G. Chinta, J. Jorgenson, A. Karlsson, L. Smajlović, *The discrete analogue of the Gaussian*, arXiv:2409.14344v1, first submitted 2024-09-22. https://arxiv.org/abs/2409.14344
2. A. Karlsson and M. Neuhauser, *Heat kernels, theta identities, and zeta functions on cyclic groups*, *Contemporary Mathematics* 2006. https://www.unige.ch/math/folks/karlsson/heatcyclicfinal.pdf
3. E. Bédos and R. Conti, *Heat Properties for Groups*, *Journal of Fourier Analysis and Applications* 30 (2024), article 46, first published 2024-08-14. https://doi.org/10.1007/s00041-024-10103-0
4. *Two sharp spectral-order thresholds for sampled two-harmonic von Mises kernels*, published mathematical research record, 2026-10-26.
5. *Exact every-mode staircase for even-harmonic geodesic-exponential circle covariances*, published mathematical research record, 2026-11-16.
6. *A countably faceted positivity frontier for quadratically modulated circle heat kernels*, published mathematical research record, 2026-11-16.
