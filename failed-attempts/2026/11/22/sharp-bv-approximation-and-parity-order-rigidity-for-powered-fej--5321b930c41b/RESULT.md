# Sharp BV approximation and parity-order rigidity for powered Fejér–Jackson kernels

## Finding

Fix integers \(n\ge2\) and \(q\ge2\). On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), define
\[
P_n(z)=\sum_{j=0}^{n-1}z^j,\quad
A_{n,q}(k)=[z^{q(n-1)+k}]P_n(z)^{2q}
\quad (|k|\le q(n-1)),
\]
and extend \(A_{n,q}(k)=0\) outside that range. Put \(a_{n,q}=A_{n,q}(0)>0\), and define the probability density
\[
j_{n,q}(\theta)=\frac{1}{2\pi a_{n,q}}
\left(\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right)^{2q}
\]
by continuous extension at multiples of \(2\pi\). Let \(T_{n,q}f=j_{n,q}*f\), where convolution uses ordinary Lebesgue measure and no additional normalization. For real periodic \(f\in BV(\mathbb T)\), set \(V(f)=|Df|(\mathbb T)\). Then
\[
\boxed{\sup_{V(f)>0}\frac{\|T_{n,q}f-f\|_{L^1(\mathbb T)}}{V(f)}
=C_{n,q}=\frac\pi2-\frac4{\pi a_{n,q}}
\sum_{\substack{1\le k\le q(n-1)\\k\text{ odd}}}
\frac{A_{n,q}(k)}{k^2}.}
\]
The supremum is attained, and equality holds **exactly** for nonconstant two-level functions whose upper level set is a semicircle, up to equality almost everywhere. This includes arbitrary rotations, adding constants, and nonzero rescaling.

The sharp error for an indicator of an arc of length \(\ell\in[0,2\pi]\), divided by its variation \(2\), is \(L_{n,q}(\ell)\). It uniquely peaks at \(\ell=\pi\) and, for \(\delta\downarrow0\), has the exact parity-dependent rigidity laws
\[
C_{n,q}-L_{n,q}(\pi-\delta)=
\begin{cases}
\displaystyle \frac{\delta^2}{2\pi a_{n,q}}+O_{n,q}(\delta^4),&n\text{ odd},\\[6pt]
\displaystyle \frac{(n/2)^{2q}\delta^{2q+2}}
{\pi a_{n,q}(2q+1)(2q+2)}+O_{n,q}(\delta^{2q+4}),&n\text{ even}.
\end{cases}
\]
Thus the degenerate maximum has order \(2q+2\) for even \(n\), but order two for odd \(n\).

For the classical squared-Fejér Jackson case \(q=2\),
\[
a_{n,2}=\frac{n(2n^2+1)}3,\qquad
\boxed{\lim_{n\to\infty}nC_{n,2}=\frac{6\log2}{\pi}.}
\]
The limiting integral itself is classical; the result here is its role as a sharp BV approximation norm within the full finite-degree and extremizer theorem.

## Assumptions and scope

All functions are real and considered modulo equality almost everywhere. Distributional variation includes jumps across the seam of the circle. The \(L^1\)-norm is unnormalized Lebesgue \(L^1\) on any interval of length \(2\pi\). The kernel is the strictly nonnegative power \(2q\) of the Dirichlet-ratio, normalized to have integral one; it has only finitely many zeros and is positive almost everywhere. The notation \([z^r]\) denotes the coefficient of the indicated power in a finite polynomial. The variation vanishes only for constant inputs, which are excluded by \(V(f)>0\). The theorem is uniform in every integer \(n\ge2\), \(q\ge2\), with the displayed big-O terms for fixed \(n,q\). No claim about simultaneous large-\(n\), large-\(q\) asymptotics is made.

## Proof

**1. Normalization and spectral expression.** For \(z=e^{i\theta}\),
\[
\left(\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right)^{2q}
=z^{-q(n-1)}P_n(z)^{2q}
=\sum_{k=-q(n-1)}^{q(n-1)}A_{n,q}(k)e^{ik\theta}.
\]
The middle coefficient is the integral average. Consequently \(j_{n,q}\) integrates to one, its Fourier coefficient at frequency \(k\) is \(A_{n,q}(k)/a_{n,q}\), and its density is positive outside finitely many points. The absolutely convergent Fourier series
\[
|\theta|=\frac\pi2-\frac4\pi\sum_{k\ge1,\;k\text{ odd}}\frac{\cos(k\theta)}{k^2}
\qquad(-\pi\le\theta\le\pi)
\]
yields \(\int_{-\pi}^{\pi}|\theta|j_{n,q}(\theta)\,d\theta=C_{n,q}\), exactly as displayed.

**2. Universal BV upper bound.** For the translation \(\tau_s f(x)=f(x-s)\), the standard BV translation bound on the circle is
\[
\|\tau_s f-f\|_1\le d_{\mathbb T}(s,0)V(f),
\qquad d_{\mathbb T}(s,0)=\min_{m\in\mathbb Z}|s-2\pi m|.
\]
It follows first for absolutely continuous functions by integrating their derivatives and then for every distributional BV function by smooth approximation with convergent variation. Since \(j_{n,q}\) is a positive probability density, Minkowski's integral inequality gives
\[
\|T_{n,q}f-f\|_1
\le\int_{-\pi}^{\pi}j_{n,q}(s)\|\tau_s f-f\|_1\,ds
\le C_{n,q}V(f).
\]

**3. Arc leakage and attainment.** For an arc \(I\) of length \(0<\ell\le\pi\), positivity of the density gives
\[
\|T_{n,q}\mathbf1_I-\mathbf1_I\|_1
=2\int_I\!\int_{I^c}j_{n,q}(x-y)\,dy\,dx=2L_{n,q}(\ell),
\]
where symmetry and elementary overlap counting give
\[
L_{n,q}(\ell)=2\int_0^\pi\min\{s,\ell\}j_{n,q}(s)\,ds.
\]
For longer arcs use \(L_{n,q}(\ell)=L_{n,q}(2\pi-\ell)\). The derivative for \(0<\ell<\pi\) is \(L'_{n,q}(\ell)=2\int_\ell^\pi j_{n,q}(s)\,ds>0\). Hence \(L\) has its unique maximum at the semicircle, with
\[
L_{n,q}(\pi)=2\int_0^\pi s j_{n,q}(s)\,ds=C_{n,q}.
\]
As \(V(\mathbf1_I)=2\), this attains the operator norm.

**4. Exhaustive classification of equality.** Every finite-perimeter measurable subset \(E\) of the circle is, modulo null sets, a finite union of disjoint arcs. If it has \(r\ge1\) proper connected components \(I_j\), its perimeter is \(2r\). The triangle inequality gives
\[
\|T_{n,q}\mathbf1_E-\mathbf1_E\|_1
\le\sum_{j=1}^r\|T_{n,q}\mathbf1_{I_j}-\mathbf1_{I_j}\|_1
=2\sum_{j=1}^rL_{n,q}(|I_j|)\le2rC_{n,q}.
\]
Equality requires every component to be a semicircle; more than one disjoint proper component cannot meet this requirement. Thus equality for any nontrivial finite-perimeter indicator occurs only for a semicircle. For general real \(BV\) functions, layer-cake representation plus the triangle inequality and the coarea identity \(V(f)=\int_{\mathbb R}\operatorname{Per}(\{f>t\})\,dt\) transfer the bound. Equality forces almost every nontrivial superlevel set to be a semicircle. Superlevel sets are nested; two nested semicircles must agree almost everywhere. Hence \(f\) takes exactly two essential values on complementary semicircles. Conversely every such function attains equality.

**5. Local extremal rigidity.** Subtracting the two overlap integrals gives the identity
\[
C_{n,q}-L_{n,q}(\pi-\delta)
=2\int_0^\delta (\delta-u)j_{n,q}(\pi-u)\,du.
\]
For odd \(n\), the Dirichlet-ratio is \(\pm1+O_n(u^2)\) at \(\pi-u\), so \(j_{n,q}(\pi-u)=1/(2\pi a_{n,q})+O_{n,q}(u^2)\). For even \(n\), it is \(\pm(n/2)u+O_n(u^3)\), giving
\[
j_{n,q}(\pi-u)=\frac{(n/2)^{2q}}{2\pi a_{n,q}}u^{2q}
+O_{n,q}(u^{2q+2}).
\]
Integrating \(\int_0^\delta(\delta-u)u^r\,du=\delta^{r+2}/((r+1)(r+2))\) proves both exact leading constants and their remainders. Strict positivity of the leading coefficients proves the asserted orders.

**6. Jackson asymptotic.** For \(q=2\), the middle coefficient of \(P_n(z)^4\) is \(a_{n,2}=n(2n^2+1)/3\), either by finite convolution or Parseval. On scaling \(x=n\theta\), the probability density of \(x\) converges to
\[
\frac{3}{4\pi}\left(\frac{\sin(x/2)}{x/2}\right)^4\,dx.
\]
The scaled densities have a uniform majorant \(C(1+|x|)^{-4}\) on \([-\pi n,\pi n]\), allowing convergence of the first absolute moments. Integration by parts and the Dirichlet integral give
\[
\int_0^\infty\frac{\sin^4u}{u^3}\,du
=\int_0^\infty\frac{\cos2u-\cos4u}{u}\,du=\log2.
\]
The first absolute moment of the limiting density is \(6\log2/\pi\), so \(nC_{n,2}\) converges to that constant. No unproved exchange of nonintegrable moments is used.

## Verification

A standalone standard-library Python checker accompanies this result. It expands the finite polynomial powers independently of the inclusion–exclusion formula, checks normalization and exact parity-vanishing moments, compares the spectral constant against numerical quadrature for \(2\le n\le12\), \(2\le q\le5\), checks arc leakage and the explicit \(q=2\) large-degree limit. Its finite checks corroborate but do not establish the universal BV statements, which follow from the analytic proof above. Run `python checker.py` with Python 3.9 or later.

## Relationship to prior work

Classical Fejér and Jackson summation and the Jackson–Stechkin theory motivate the positive convolution family. Nielsen (2010 research report; 2013 journal version) studies matrix-weighted \(L^p\) convergence of Jackson summation, whereas Babenko–Kryakin–Staszak (2013) derive approximation inequalities for continuous functions and periodic splines. Neither result supplies the present sharp unnormalized BV-to-\(L^1\) norm, equality classification or parity-order law. Catala–Hockmann–Kunis–Wageringel (2024), especially §3.3 and Remark 3.4, establish Wasserstein estimates for measure approximation, give the Jackson kernel and a coarse first-moment bound; their sharp delta-mass transport observation and the current BV variation-seminorm problem have different domains. The classical integral \(\int_0^\infty\sin^4u/u^3\,du=\log2\) is not claimed as new. Prior investigations of the ordinary Fejér kernel \(q=1\) establish a quadratic/quartic rigidity split, but not the full powered hierarchy at \(q\ge2\) with finite-degree sharp BV coefficients. Other research on powered Fejér kernels concerns bounded-input-to-Lipschitz norms, not this approximation error. Historical priority for the exact finite constants and the equality/rigidity classification is subject to additional independent literature review.

## Limitations

Only real, unweighted, one-dimensional periodic BV inputs and positive integral powers of the standard Fejér kernel are covered. The result is not a best-polynomial-approximation theorem, does not optimize among all positive convolution kernels of a given Fourier degree, and does not assert a uniform large-power limit. The rigidity expansion concerns one-arc perturbations of a semicircle, not a global distance-to-extremizer stability theorem. Some older non-digitized approximation literature remains a priority risk.

## References

- M. Nielsen, “Summation of Multiple Fourier Series in Matrix Weighted \(L^p\)-Spaces,” *Journal of Mathematics* (2013), DOI: 10.1155/2013/135245; 2013 journal version published March 20, 2013; an earlier university research report, R-2010-01, is dated to 2010 without a verified day. https://doi.org/10.1155/2013/135245
- A. G. Babenko, Y. V. Kryakin, P. T. Staszak, “Special Moduli of Continuity and the Constant in the Jackson–Stechkin Theorem,” *Constructive Approximation* 38 (2013), 339–364, DOI: 10.1007/s00365-013-9210-6. https://doi.org/10.1007/s00365-013-9210-6
- P. Catala, M. Hockmann, S. Kunis, M. Wageringel, “Approximation and Interpolation of Singular Measures by Trigonometric Polynomials,” *Constructive Approximation* 60 (2024), 405–442, DOI: 10.1007/s00365-024-09686-0, especially Remark 3.4. https://doi.org/10.1007/s00365-024-09686-0
