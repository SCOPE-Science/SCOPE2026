# Sharp uniform-grid monotonicity contrast for unmodified natural cubic splines

## Finding

Let \(n\ge2\), let \(y_0<y_1<\cdots<y_n\) be real data at the equally spaced knots \(0,1,\ldots,n\), and let \(S\) be the ordinary natural cubic interpolant. Put \(d_j=y_{j+1}-y_j>0\), \(m=\min_jd_j\) and \(M=\max_jd_j\). If
\[
\boxed{\frac{M}{m}\le 2+\sqrt3,}
\]
then \(S'(x)\ge0\) on the *entire* interpolation interval. The constant is the **largest possible bound uniform in the number of knots**: for each \(R>2+\sqrt3\), some finite strictly increasing data with all slopes in \(\{1,R\}\) have a natural spline with \(S'(0)<0\).

In fact the underlying *sharp* operator estimate, valid for every finite real slope vector (without positivity assumptions), is
\[
\boxed{\|S'\|_{L^\infty[0,n]}\le\sqrt3\max_{0\le j<n}|d_j|,\qquad
\sup_{n\ge2}\sup_{d\ne0}\frac{\|S'\|_\infty}{\|d\|_\infty}=\sqrt3.}
\]
The supremum over all grid lengths is approached by alternating signed slopes.

## Assumptions and scope

Here \(S\) is the unique globally \(C^2\), piecewise-cubic interpolant satisfying \(S(j)=y_j\) and natural boundary conditions \(S''(0)=S''(n)=0\). The knot count is an arbitrary but finite integer \(n+1\ge3\). An affine rescaling of the horizontal grid preserves the slope contrast and monotonicity. The boundary conditions are *not* clamped, periodic or not-a-knot. Only first differences are constrained; no higher smoothness is assumed of the data.

## Proof

**1. Cubic curvature and a symmetric whole-line extension.** Define \(d_j=y_{j+1}-y_j\) for \(0\le j<n\), and \(m_j=S''(j)\), so \(m_0=m_n=0\). On each unit cell, put \(u=x-j\in[0,1]\), \(A(u)=-2+6u-3u^2\), \(B(u)=3u^2-1\). The standard cubic formula yields
\[
S'(j+u)=d_j+\frac{m_j}{6}A(u)+\frac{m_{j+1}}6B(u),\quad
m_{j-1}+4m_j+m_{j+1}=6(d_j-d_{j-1})\quad(1\le j<n).
\]
Reflect the *finite secant array* at both endpoints to a bounded \(2n\)-periodic bi-infinite array \(D_j\), specified by \(D_{-1-j}=D_j\) and \(D_{n+j}=D_{n-1-j}\) for \(j\ge0\), followed by periodic continuation. Its difference forcing \(D_j-D_{j-1}\) is odd about both integer nodes \(0\) and \(n\). Let \(r=2-\sqrt3\), \(q=-r\) and \(G_k=q^{|k|}/(2\sqrt3)\). Direct substitution verifies
\[
G_{k-1}+4G_k+G_{k+1}=\mathbf1_{\{k=0\}}.
\]
Consequently, the unique bounded solution of the bi-infinite curvature recurrence is
\[
\widehat m_j=6\sum_{k\in\mathbb Z}G_{j-k}(D_k-D_{k-1}).
\]
The series is absolutely convergent, since \(G\in\ell^1\) and \(D\) is bounded. The even Green kernel preserves the reflected odd forcing, hence \(\widehat m_0=\widehat m_n=0\). On \(0\le j\le n\) this is precisely the unique finite natural-spline curvature solution (the tridiagonal matrix is strictly diagonally dominant). Therefore the finite spline derivative is the restriction of a translation-invariant derivative operator applied to the reflected array, and \(\|D\|_{\ell^\infty}=\|d\|_{\ell^\infty}\).

**2. Exact norm of the infinite-line derivative operator.** On the unit cell at the origin, expand the derivative as \(\sum_{k\in\mathbb Z}c_k(u)D_k\). Write \(C=1/(2\sqrt3)\),
\[
\begin{aligned}
p(u)&=(1+r)A(u)-(1+r^{-1})B(u),\\
q(u)&=(1+r^{-1})A(u)-(1+r)B(u),\\
c_0(u)&=1+C(1+r)(A(u)-B(u)),\\
c_k(u)&=C(-r)^k p(u)\quad(k\ge1),\\
c_{-k}(u)&=C(-r)^k q(u)\quad(k\ge1).
\end{aligned}
\]
These formulas follow by collecting the coefficient of each secant in the absolutely convergent Green convolution. In particular \(c_0(u)>0\), so the exact pointwise \(\ell^\infty\)-operator norm is
\[
\Lambda(u)=c_0(u)+\frac{Cr}{1-r}\big(|p(u)|+|q(u)|\big).
\]
Set \(u_-=(3+\sqrt3-\sqrt6)/6\), \(u_+=(3-\sqrt3+\sqrt6)/6\), so \(0<u_-<1/2<u_+<1\). Direct quadratic factorization gives the sign patterns
\[
(p,q):\qquad (+,-)\ (0\le u\le u_-),\qquad (+,+)\ (u_-\le u\le u_+),\qquad (-,+)\ (u_+\le u\le1).
\]
At endpoints where a coefficient vanishes either neighboring sign convention gives the same value. Substitution reduces the full norm to
\[
\Lambda(u)=\begin{cases}
\sqrt3-3(\sqrt3-1)u^2,&0\le u\le u_-,\\
6u(1-u),&u_-\le u\le u_+,\\
\sqrt3-3(\sqrt3-1)(1-u)^2,&u_+\le u\le1.
\end{cases}
\]
The middle expression is at most \(3/2<\sqrt3\), and both outer expressions are at most \(\sqrt3\). Thus \(\|S'\|_\infty\le\sqrt3\|D\|_\infty=\sqrt3\|d\|_\infty\), uniformly over all finite grids.

**3. From operator stability to monotonicity.** The spline derivative operator reproduces a constant secant array: if each secant equals \(b\), the interpolant is affine and \(S'\equiv b\). Decompose each positive secant as \(d_j=(M+m)/2+e_j\) with \(|e_j|\le(M-m)/2\). By the operator bound,
\[
S'(x)\ge \frac{M+m}{2}-\frac{\sqrt3}{2}(M-m)
\ge0
\]
for all \(x\) precisely under \(M/m\le(\sqrt3+1)/(\sqrt3-1)=2+\sqrt3\). Hence the ordinary natural cubic is nondecreasing without any nonlinear slope modification.

**4. Sharpness on finite positive data and the exact norm.** For every integer \(m\ge1\), choose \(n=2m\) cells and alternating secants \(d_{2j}=1\), \(d_{2j+1}=R\), \(0\le j<m\). Define integers \(a_0=1\), \(a_1=5\), \(a_{m+1}=4a_m-a_{m-1}\). Solving the finite tridiagonal curvature system by consecutive continuants (equivalently, substituting this recurrence and the two zero-curvature boundary conditions) gives the exact left-end derivative
\[
\boxed{S'(0)=\frac{a_m-Ra_{m-1}}{a_m-a_{m-1}}.}
\]
One may check the continuant identity by induction on \(m\), beginning with \(n=2\), for which \(S'(0)=(5-R)/4\), and using the common tridiagonal characteristic recurrence \(a_{m+1}=4a_m-a_{m-1}\). More explicitly, if \(t_m=a_m/a_{m-1}\), then \(t_1=5\), \(t_{m+1}=4-1/t_m\); these ratios strictly decrease to the larger root \(2+\sqrt3\) of \(t^2-4t+1=0\). Given any \(R>2+\sqrt3\), choose \(m\) so that \(t_m<R\); then \(S'(0)<0\), even though all observed values strictly increase. With signed alternating secants \(d_{2j}=1\), \(d_{2j+1}=-1\), the same identity yields \(S'(0)=(a_m+a_{m-1})/(a_m-a_{m-1})\to\sqrt3\); this proves the constant in the derivative norm is also sharp. □

## Verification

The standalone `verify.py` reproduces the exact Green recurrence and all polynomial norm identities in SymPy, checks the finite-grid endpoint identity with *symbolic* rate parameter \(R\) for 12 even-grid sizes, checks the sharp ratio recurrence, and independently solves finite natural-spline systems for random positive secants. The numerical tests supplement rather than replace the all-grid proof. Execute `python verify.py` with Python, SymPy and NumPy.

## Relationship to prior work

Aràndiga, Baeza and Yáñez (2021) analyze sufficient monotonicity conditions for cubic Hermite/spline interpolation and develop nonlinear derivative rules. Their inspected Sections 1–3 do not give the universal sharp secant-contrast guarantee for the *unmodified natural* spline. Fritsch and Carlson (1980) give cellwise conditions and shape-preserving Hermite alternatives, not this finite-grid natural-boundary threshold. Classical whole-line cardinal splines provide the Green recurrence used here, but the established sharp *bounded-variation* gain \((2+\sqrt3+2\sqrt{2-\sqrt3})/3\) measures an inequivalent variation norm; the sharp \(\ell^\infty\)-secant-to-derivative bound \(\sqrt3\) and its sharp monotonicity consequence do not follow from that BV bound alone. Published four-knot natural-spline variation calculations treat a fixed knot count and a different stability norm; they cannot imply the sharp all-grid envelope. The exact numerical constant and conclusion might have appeared in older unindexed spline literature; no exhaustive priority guarantee is made.

## Limitations

The conclusion is a uniform sufficient monotonicity guarantee and a sharp *uniform-in-\(n\)* threshold, not a necessary condition for monotonicity of each individual dataset. In particular, some datasets with larger contrast can still have monotone splines. The bound does not cover nonuniform knots or different endpoint conditions. No numerical convergence or interpolation-error improvement is asserted. Historical-priority comparison with every classical monograph remains incomplete.

## References

1. F. Aràndiga, A. Baeza, D. F. Yáñez, *Monotone cubic spline interpolation for functions with a strong gradient*, arXiv:2102.11564v1 (2021-02-23), https://arxiv.org/html/2102.11564v1.
2. F. N. Fritsch, R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM J. Numer. Anal. 17 (1980), 238–246, https://doi.org/10.1137/0717021.
3. I. J. Schoenberg, *Cardinal Spline Interpolation*, SIAM reissue (2012), https://epubs.siam.org/doi/10.1137/1.9781611970555.
4. *Sharp bounded-variation norm of whole-line \(C^2\) cardinal cubic-spline interpolation*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-bounded-variation-norm-of-whole-line-c-2-cardinal-cubic-sp--12f2cdbed39e.
5. *Sharp total-variation amplification of the first coupled natural cubic spline*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-total-variation-amplification-of-the-first-coupled-natural--287732549e93.
