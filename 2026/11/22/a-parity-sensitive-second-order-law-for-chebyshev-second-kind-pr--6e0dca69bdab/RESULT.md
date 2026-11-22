# A parity-sensitive second-order law for Chebyshev-second-kind projection of bounded-variation data

## Finding
Let \(d\mu(x)=\frac{2}{\pi}\sqrt{1-x^2}\,dx\) on \((-1,1)\), and let \(Q_n\) be orthogonal projection in \(L^2(\mu)\) onto polynomials of degree at most \(n\). For real \(f\in BV(-1,1)\), let \(V(f)=|Df|((-1,1))\) and define
\[
 E_n^2=\sup_{V(f)>0}\frac{\|(I-Q_n)f\|_{L^2(\mu)}^2}{V(f)^2}.
\]
For every integer \(n\ge0\), this supremum is attained by a single interior unit jump. For \(n\to\infty\), the sharp squared norm satisfies the **two-term asymptotic**
\[
 \boxed{E_n^2=\frac{2}{\pi^2n}-\frac{2}{\pi^2n^2}+o(n^{-2}).}
\]
If \(\theta_n\in(0,\pi)\) is the angle of any maximizing jump, then \(\theta_n\to\pi/2\), or equivalently its jump abscissa \(\cos\theta_n\to0\). The midpoint jump is a strict local maximum of the jump residual for every even degree \(n\ge0\), but a strict local minimum for every odd degree \(n\ge1\). More precisely, writing \(R_n(\theta)\) for the squared residual of a unit jump at \(x=\cos\theta\),
\[
 \boxed{R_n''(\pi/2)=\begin{cases}
 -\frac4{\pi^2}\left(1+\frac1{n+1}\right),&n\text{ even},\\[2mm]
 \frac4{\pi^2}\left(1-\frac1{n+2}\right),&n\text{ odd}.
 \end{cases}}
\]
The midpoint's precise second-order cost is
\[
 R_n(\pi/2)=\frac2{\pi^2n}+\frac{-3+(-1)^n}{\pi^2n^2}+O(n^{-3}),
\]
so that
\[
 \boxed{n^2(E_n^2-R_n(\pi/2))\longrightarrow
 \begin{cases}0,&n\text{ even},\\2/\pi^2,&n\text{ odd},\end{cases}}
\]
where the limits are taken along their respective parities. For odd \(n\), the explicit off-center jump at \(\theta=\pi/2+\pi/[2(n+2)]\) achieves the displayed two-term sharp expansion, though it need not be an exact finite-degree maximizer.

## Assumptions and scope
The basis is \(U_k(\cos\theta)=\sin((k+1)\theta)/\sin\theta\), \(k=0,1,2,\ldots\). These second-kind Chebyshev polynomials are orthonormal for the **probability** weight \(d\mu\). The projection includes the constant \(U_0=1\). The total variation is ordinary distributional variation in the **open** interval, without an endpoint jump penalty. The norm is weighted mean-square, not uniform or unweighted mean-square error. All statements concern real-valued inputs; changing values at isolated locations does not change the \(L^2\) problem.

## Proof
**1. Reduction to a scalar jump.** Write \(h_s(x)=\mathbf 1_{(s,1)}(x)\). Every \(f\in BV(-1,1)\) admits, modulo constants and equality almost everywhere, the derivative-measure representation
\[
 f(x)=c+\int_{(-1,1)}h_s(x)\,d(Df)(s).
\]
The residual map annihilates constants; Bochner integration and Minkowski's inequality therefore give
\[
 \|(I-Q_n)f\|_2\le\int\|(I-Q_n)h_s\|_2\,d|Df|(s)
 \le V(f)\max_{-1\le s\le1}\|(I-Q_n)h_s\|_2.
\]
At the two endpoint limits the residual vanishes, whereas it is positive at some interior jump. The residual depends continuously on the jump position in \(L^2(\mu)\); hence the maximum is attained at an interior point and a unit jump proves sharpness.

**2. Exact residual.** Set \(s=\cos\theta\), \(0\le\theta\le\pi\), and \(p(\theta)=(\theta-\tfrac12\sin2\theta)/\pi\). The complementary orientation of the indicator is immaterial because constants are projected exactly. Its nonconstant polynomial coefficients have magnitudes
\[
 |a_k(\theta)|=\frac1\pi\left|\frac{\sin k\theta}{k}-\frac{\sin(k+2)\theta}{k+2}\right|,\qquad k\ge1.
\]
The orthogonality identity, including the constant, gives
\[
 R_n(\theta)=p(\theta)(1-p(\theta))-\sum_{k=1}^na_k(\theta)^2.
\]
Completeness of the orthonormal second-kind system and Parseval give the equivalent nonnegative tail
\[
 R_n(\theta)=\sum_{m=n+2}^\infty\frac4{\pi^2}
 \frac{[\cos\theta\sin(m\theta)-m\sin\theta\cos(m\theta)]^2}{(m^2-1)^2}.
\]
Both representations are exact for all \(n\ge0\) and \(\theta\in[0,\pi]\).

**3. Parity of the midpoint curvature.** Differentiate the finite coefficient formula twice. At \(\theta=\pi/2\), \(p=1/2\), \(p'=2/\pi\), and \(p''=0\). For even \(k\ge1\), \(a_k=0\) and \((a_k')^2=4/\pi^2\); for odd \(k\), \(a_k'=0\) and \(a_ka_k''=-4(k+1)^2/[\pi^2k(k+2)]\). Consequently
\[
 R_n''(\pi/2)=\frac8{\pi^2}\left[-1-\lfloor n/2\rfloor+
 \sum_{\substack{1\le k\le n\\k\text{ odd}}}\frac{(k+1)^2}{k(k+2)}\right].
\]
Using \((k+1)^2/[k(k+2)]=1+1/[k(k+2)]\) and the telescoping sum
\[
 \sum_{j=0}^{r-1}\frac1{(2j+1)(2j+3)}=\frac12\left(1-\frac1{2r+1}\right)
\]
yields precisely the two curvature formulas in the finding. The midpoint is therefore strictly suboptimal for **every odd** \(n\), not merely asymptotically.

**4. Uniform high-degree comparison.** Write \(N=n+2\), \(S_N=\sum_{m=N}^\infty m^{-2}\), and \(A_N(\theta)=\sum_{m=N}^\infty\cos(2m\theta)/m^2\). From
\[
 \frac{2[\cos\theta\sin(m\theta)-m\sin\theta\cos(m\theta)]}{\pi(m^2-1)}
 =-\frac{2\sin\theta\cos(m\theta)}{\pi m}
 +O\left(\frac{|\cos\theta|}{m^2}+\frac1{m^3}\right)
\]
and summability, uniformly for \(0\le\theta\le\pi\), follows
\[
 R_n(\theta)=\frac{2\sin^2\theta}{\pi^2}[S_N+A_N(\theta)]
 +O\left(\frac{|\cos\theta|}{n^2}+\frac1{n^3}\right).
 \tag{1}
\]
The constants in this asymptotic are absolute for \(n\) sufficiently large. Elementary integral comparison or Euler summation yields
\[
 S_N=\frac1n-\frac3{2n^2}+O(n^{-3}). \tag{2}
\]
For every fixed \(\varepsilon\in(0,\pi/2)\), two applications of summation by parts to the oscillating sequence \(e^{2im\theta}\) yield uniformly on \([\varepsilon,\pi-\varepsilon]\)
\[
 \sum_{m=N}^\infty\frac{e^{2im\theta}}{m^2}
 =\frac{e^{2iN\theta}}{N^2(1-e^{2i\theta})}+O_\varepsilon(N^{-3}). \tag{3}
\]
In particular, \(A_N=O_\varepsilon(n^{-2})\), so \(nR_n(\theta)\to 2\sin^2\theta/\pi^2\) uniformly on those compact subintervals. At the endpoint arcs \(\theta\le\pi/6\) or \(\theta\ge5\pi/6\), the elementary bound \(|A_N|\le S_N\) in (1) gives \(nR_n(\theta)\le1/\pi^2+o(1)\), strictly below the centered leading value \(2/\pi^2\). Thus every global maximizing sequence \(\theta_n\) tends to \(\pi/2\).

**5. Sharp second term.** For any maximizing \(\theta_n\to\pi/2\), equation (3) gives
\[
 A_N(\theta_n)\le\frac{1+o(1)}{2n^2}.
\]
Since \(\sin^2\theta_n\le1\) and \(\cos\theta_n=o(1)\), equations (1)–(2) imply
\[
 E_n^2\le\frac2{\pi^2n}-\frac2{\pi^2n^2}+o(n^{-2}).
\]
For even \(n\), choose \(\theta=\pi/2\); then \(e^{2iN\theta}=1\). For odd \(n\), choose \(\theta=\pi/2+\pi/(2N)\); again \(e^{2iN\theta}=1\). Both choices have \(\sin^2\theta=1+O(n^{-2})\) and \(|\cos\theta|=O(n^{-1})\), and equation (3) gives \(A_N=1/(2n^2)+O(n^{-3})\). These two witnesses supply the matching lower bound. Evaluating (1) directly at \(\theta=\pi/2\) gives \(A_N=(-1)^n/(2n^2)+O(n^{-3})\), producing the midpoint expansion and both parity-dependent sharp deficits.

## Verification
The accompanying self-contained Python script `checker.py` checks 100 exact rational midpoint-curvature identities, compares the two independent Parseval and coefficient representations at 56 finite inputs, and tests the two-term expansion and its parity behavior at 10 cutoffs. Six finite dense-grid probes are additional consistency checks. These tests do not prove an infinite supremum or an asymptotic limit: those follow from the variation-measure argument, uniform summation-by-parts estimates, and matching witnesses above. The all-degree curvature assertion is proved by an exact telescoping identity rather than numerics.

## Relationship to prior work
The standard second-kind Chebyshev coefficient and spectral-expansion framework motivates the question of simultaneous, rather than coefficientwise, control of projection error on rough inputs. Orel and Perne (2014) study half-range Chebyshev–Fourier collocation for boundary-value problems; Xiang (2014) studies interpolation convergence for limited-regularity inputs. Akansha (2024) obtains different Chebyshev coefficient and \(L^1\)-approximation estimates for approximated coefficients. Sluchak (2026) explicitly treats sharp bounds on **individual** second-kind Chebyshev coefficients. None of these inspected statements directly supplies the joint-tail sharp second-order norm or the all-cutoff midpoint curvature law. A first-kind Chebyshev residual theorem uses the arcsine weight and a cosine system, whereas here the semicircle weight induces the sine system. Legendre and other Jacobi weights likewise have different projectors and do not imply this result merely by parameter renaming.

## Limitations
The theorem does not prove the precise maximizing jump positions at individual finite degrees, nor a unique global maximizer for each even cutoff. It establishes only the convergence of all maximizing positions toward the midpoint, a sharp two-term norm, and the exact local midpoint curvature classification. The odd-degree nearby-jump witnesses achieve the two-term asymptotic, not necessarily the exact finite-degree supremum. The novelty assessment remains vulnerable to an overlooked equivalent historical result. No independent mathematical audit has been performed.

## References
1. B. Orel and A. Perne, *Chebyshev-Fourier Spectral Methods for Nonperiodic Boundary Value Problems*, Journal of Applied Mathematics (2014), DOI: 10.1155/2014/572694, publicly dated 2014-06-01.
2. S. Xiang, *On Interpolation Approximation: Convergence Rates for Polynomial Interpolation for Functions of Limited Regularity*, arXiv:1411.7746, posted 2014-11-28.
3. S. Akansha, *Exploring Chebyshev Polynomial Approximations: Error Estimates for Functions of Bounded Variation*, arXiv:2404.18723, posted 2024-04-29.
4. V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067, posted 2026-11-02, especially the section on second-kind Chebyshev coefficients.
