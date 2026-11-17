# Sharp and unattained planar Minkowski inverse-Wasserstein Lipschitz constant

## Finding
Let \(\mu\) and \(\nu\) be balanced, nondegenerate Borel probability measures on the unit circle. Write \(K_\mu,K_\nu\) for the uniquely Steiner-centered planar convex bodies with surface-area measures \(S_{K_\mu}=2\pi\mu\) and \(S_{K_\nu}=2\pi\nu\). For geodesic-circle \(W_1\),
\[
\sup_{\mu\ne\nu}\frac{d_H(K_\mu,K_\nu)}{W_1(\mu,\nu)}=\pi.
\]
The sharp supremum is **never attained** by a distinct pair. It remains \(\pi\) when both measures have everywhere-positive smooth densities, so that their reconstructed bodies are smooth and strictly convex.

## Assumptions and scope
The circle is parametrized by \(\theta\in\mathbb R/(2\pi\mathbb Z)\). The geodesic distance is \(d_g(e^{i\theta},e^{i\phi})=\min_{k\in\mathbb Z}|\theta-\phi+2\pi k|\). A probability measure is *balanced* if \(\int e^{i\theta}\,d\mu(\theta)=0\) and *nondegenerate* if its support is not contained in a single antipodal pair. The planar Minkowski existence/uniqueness theorem supplies \(K_\mu\), and the Steiner choice removes both first support-function harmonics. Both bodies have perimeter \(2\pi\). The Hausdorff distance is Euclidean and support functions are compared in the common Steiner frame. The optimal constant applies to all such measure pairs, without density, atom-size, or separation hypotheses.

## Proof
**1. The upper estimate and strictness.** The explicit periodic even Green kernel of An [1, Section 6.1] is
\[
G(t)=-\frac{\cos t}{4\pi}+\left(\frac12-\frac{|t|}{2\pi}\right)\sin |t|,\qquad |t|\le\pi.
\]
It is the centered inverse of \(D^2+1\) on balanced signed measures, so
\[
h_{K_\mu}(\theta)-h_{K_\nu}(\theta)=2\pi\int G(\theta-\phi)\,d(\mu-\nu)(\phi).
\]
For \(0<t<\pi\), direct differentiation gives
\[
G'(t)=\left(\frac12-\frac{t}{2\pi}\right)\cos t-\frac{\sin t}{4\pi}.
\]
Using \(|\cos t|\le1\), \(\sin t\le t\), and \(0\le\frac12-\frac{t}{2\pi}\), one has
\[
|G'(t)|\le\frac12-\frac{t}{4\pi}<\frac12 \quad(0<t<\pi).
\]
Evenness and periodicity give strict geodesic \(1/2\)-Lipschitz inequality between **any two distinct circle points**: along their positive-length shortest arc, the derivative has magnitude strictly below \(1/2\) almost everywhere (a cusp at zero has zero arc length). Consequently, for any optimal \(W_1\) coupling \(\gamma\) and every \(\theta\),
\[
|h_{K_\mu}(\theta)-h_{K_\nu}(\theta)|\le 2\pi\!\int |G(\theta-x)-G(\theta-y)|\,d\gamma(x,y)<\pi W_1(\mu,\nu)
\]
whenever \(\mu\ne\nu\): positive coupling mass must lie off the diagonal, where the kernel inequality is strict. The support difference is continuous on the compact circle; its maximum is attained, so \(d_H(K_\mu,K_\nu)<\pi W_1(\mu,\nu)\). In particular, no distinct pair attains the constant. The nondistinct case has both sides zero.

**2. Balanced near-extremizers.** Write \(\sigma=d\theta/(2\pi)\) and \(0<\varepsilon<\pi/2\), and set \(c=\cos\varepsilon\), \(a=1-c\). Define the balanced probability measures
\[
\nu_0=\frac{\delta_0+\delta_\pi}{2},\qquad
\mu_\varepsilon=\frac{\delta_\varepsilon+\delta_{-\varepsilon}+a\delta_{\pi/2}+a\delta_{-\pi/2}+2c\delta_\pi}{4}.
\]
Indeed, their masses sum to one, and their sine and cosine first moments vanish: \(2c-2c=0\). Although \(\nu_0\) is degenerate, for any fixed \(0<\eta<1\) the measures
\[
\nu_\eta=(1-\eta)\nu_0+\eta\sigma,\qquad
\mu_{\varepsilon,\eta}=(1-\eta)\mu_\varepsilon+\eta\sigma
\]
are balanced and nondegenerate. A valid coupling moves mass \(1/4\) from \(0\) to each of \(\pm\varepsilon\), and mass \(a/4\) from \(\pi\) to each of \(\pm\pi/2\); the other mass stays fixed. Coupling the common uniform part identically gives
\[
W_1(\mu_{\varepsilon,\eta},\nu_\eta)\le(1-\eta)\left(\frac\varepsilon2+\frac{\pi a}4\right).
\]
The Green-kernel values \(G(0)=-1/(4\pi)\), \(G(\pi)=1/(4\pi)\), and \(G(\pi/2)=1/4\) give **exactly**
\[
\begin{aligned}
h_{K_{\mu_{\varepsilon,\eta}}}(0)-h_{K_{\nu_\eta}}(0)
&=(1-\eta)\,\frac\pi2\left[2\bigl(G(\varepsilon)-G(0)\bigr)+2a\bigl(G(\pi/2)-G(\pi)\bigr)\right]\\
&=(1-\eta)\left[\frac{\pi-\varepsilon}{2}\sin\varepsilon+\frac\pi4(1-\cos\varepsilon)\right].
\end{aligned}
\]
Hence the ratio of Hausdorff distance to Wasserstein distance is at least
\[
\frac{(\pi-\varepsilon)\sin\varepsilon/2+\pi(1-\cos\varepsilon)/4}{\varepsilon/2+\pi(1-\cos\varepsilon)/4}\ \longrightarrow\ \pi
\quad\text{as }\varepsilon\downarrow0.
\]
Together with the upper bound, this proves sharpness.

**3. Smooth strictly convex sharpness.** For each \(\varepsilon\), convolve both \(\mu_{\varepsilon,\eta}\) and \(\nu_\eta\) with the same smooth positive circular approximate identity of sufficiently small width. The resulting smooth densities remain balanced; the \(\eta\sigma\) term ensures positivity uniformly on the circle. Their reconstructed support functions satisfy \(h+h''=2\pi f>0\), hence define smooth strictly convex bodies. The mollified measures converge in \(W_1\), and by the kernel formula their support functions converge uniformly. Choose mollification widths separately for each \(\varepsilon\), tending to zero fast enough relative to \(\varepsilon\), to retain the limiting ratio \(\pi\).

## Verification
The supplementary standalone standard-library program `verify.py` independently evaluates the kernel identity, exact support gap, balanced atomic weights, explicit transport cost, and limiting ratios for several positive parameters. It checks the Green-kernel strict Lipschitz estimate on a fine angular grid. These samples are **not** used to infer the universal theorem: strictness, the coupling, the exact support formula, and convergence are proved above.

## Relationship to prior work
Congpei An [1, Proposition 6.1] established the upper bound \(d_H\le\pi W_1\), and [1, Proposition 6.3] proved sharpness of the **exponent**, not of the multiplicative constant. Immediately after Proposition 6.3, [1] expressly states that the optimal Lipschitz constant in Proposition 6.1 is *not determined*. The present result resolves that particular open constant question, adds strict nonattainment, and establishes sharpness under smooth positive curvature. Earlier stability work cited by An in higher dimensions uses different distance and nondegeneracy normalizations; no implication proving sharpness of this fixed-centering planar coefficient was located. Historical priority remains subject to further literature review.

## Limitations
The theorem fixes circle geodesic \(W_1\), the perimeter \(2\pi\) normalization, and Steiner centering. It does not determine analogous optimal constants for chordal transport, variable perimeter, translation-optimized Hausdorff error, or higher dimensions. The extremal constant is a supremum, not an attained maximum. The proof assumes the classical planar Minkowski reconstruction and the Green-kernel identities, both explicit in [1]. No independent audit or exhaustive priority certification has been performed.

## References
[1] Congpei An, *Gauss–Chebyshev Quadrature, \(\mathbb S^1\)-Designs, and the Planar Minkowski Inverse Problem: A One-Dimensional Model for Design-Induced Convex Geometry*, arXiv:2610.11814v1, first publicly submitted 2026-10-08, especially Section 6.1–6.3 and Propositions 6.1 and 6.3. https://arxiv.org/abs/2610.11814
