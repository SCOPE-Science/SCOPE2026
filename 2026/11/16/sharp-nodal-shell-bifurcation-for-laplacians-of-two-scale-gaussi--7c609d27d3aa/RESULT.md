# Sharp nodal-shell bifurcation for Laplacians of two-scale Gaussian mixtures

## Finding

For each dimension \(d\ge 1\), a positive mixture of two centered isotropic Gaussian heat kernels has either one or three radial nodal spheres of its Laplacian, apart from explicitly classified double- and triple-root boundaries. The **exact scale threshold** for the appearance of three distinct nodal spheres is
\[
\boxed{\frac ba>\sqrt{1+\frac2d}+\sqrt{\frac2d}.}
\]
For every scale ratio above this threshold, the complete nonempty open interval of mixing weights with three simple spheres is given explicitly below. At the threshold the unique degenerate mixture has a triple radial Laplacian zero. The weight interval opens with a sharp \(3/2\)-power cusp, while the two turning radii separate at square-root speed.

These changes occur although each mixture is strictly radially decreasing and its Fourier transform is positive at every frequency. In dimension one, “three spheres” means precisely six distinct real zeros, in three symmetric pairs.

## Assumptions and scope

Fix an integer \(d\ge1\), scales \(0<a<b\), and a weight \(0<w<1\). With the Euclidean Laplacian \(\Delta=\sum_{j=1}^d\partial_{x_j}^2\), set
\[
G_s(x)=(2\pi s^2)^{-d/2}\exp\!\left(-\frac{\|x\|^2}{2s^2}\right),\qquad
F(x)=wG_a(x)+(1-w)G_b(x).
\]
The Fourier transform is \(\widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-i\langle x,\xi\rangle}\,dx\). A radial nodal sphere is a set \(\{x:\|x\|=r\}\), \(r>0\), on which \(\Delta F(x)=0\); its multiplicity refers to the radial analytic function as a function of \(r\). For \(d=1\), the sphere consists of two antipodal points. Write
\[
v=(b/a)^2>1,\quad y=\|x\|^2/a^2,\quad
v_c=\left(\sqrt{1+2/d}+\sqrt{2/d}\right)^2.
\]
On the interval \(d<y<dv\), introduce
\[
Q(y)=v^{(d+4)/2}\frac{y-d}{dv-y}\exp\!\left(-\frac{v-1}{2v}y\right),
\qquad C=\frac{d^2(v-1)^2}{4}-2dv.
\]
For \(v>v_c\), put
\[
y_\pm=\frac{d(1+v)}2\pm\sqrt C,\quad
Q_{\max}=Q(y_-),\quad Q_{\min}=Q(y_+),\quad
w_-=(1+Q_{\max})^{-1},\quad w_+=(1+Q_{\min})^{-1}.
\]
Both \(Q_{\max}>Q_{\min}>0\) and \(0<w_-<w_+<1\) hold. At \(v=v_c\), put
\[
y_c=\frac{d(1+v_c)}2,\quad
Q_c=v_c^{(d+4)/2}\exp\!\left(-\frac{d(v_c^2-1)}{4v_c}\right),\quad
w_c=(1+Q_c)^{-1}.
\]

## Proof

**1. Reduction to a scalar intersection.** Direct differentiation gives
\[
\Delta G_s(x)=s^{-4}(\|x\|^2-ds^2)G_s(x).
\]
After extracting the strictly positive common factor \((2\pi)^{-d/2}a^{-d-2}\), the sign of \(\Delta F\) is the sign of
\[
H(y)=w(y-d)e^{-y/2}+(1-w)v^{-(d+4)/2}(y-dv)e^{-y/(2v)}.
\]
For \(0\le y\le d\), both summands are nonpositive and at least one is strictly negative. For \(y\ge dv\), both are nonnegative and at least one strictly positive. Hence **every** zero lies in \(d<y<dv\), where the condition \(H(y)=0\) is equivalent to
\[
Q(y)=\frac{1-w}{w}.
\]
Since \(Q(d+)=0\) and \(Q(dv-)=+\infty\), at least one zero exists. At each interior zero, \(H\) is a positive, nonvanishing analytic factor times \(Q(y)-(1-w)/w\), up to overall sign; therefore multiplicities agree. Because \(y=r^2/a^2\) has nonzero radial derivative for \(r>0\), multiplicities in \(r\) and \(y\) also agree.

**2. A sharp quadratic derivative criterion.** Let
\[
D=\frac{d(v-1)}2,\qquad h=y-\frac{d(1+v)}2.
\]
As \(d<y<dv\), \(-D<h<D\) and \((y-d)(dv-y)=D^2-h^2>0\). Logarithmic differentiation yields the exact identity
\[
\boxed{\frac{Q'(y)}{Q(y)}=
\frac{(v-1)(h^2-C)}{2v(D^2-h^2)}.}
\]
The function \(C(v)\) changes sign once for \(v>1\): the equation \(C=0\) is \(d(v-1)^2=8v\), whose unique solution \(v>1\) is exactly \(v_c\).

If \(v<v_c\), then \(C<0\) and \(Q\) is strictly increasing, with positive derivative everywhere. Every weight gives **one simple sphere**. If \(v=v_c\), then \(Q\) is still strictly increasing, but its derivative vanishes to order two at \(y_c\). It follows that there is one sphere, which is **triple precisely at \(w=w_c\)** and simple for all other weights.

If \(v>v_c\), then \(0<C<D^2\), so the only critical points are \(y_-=d(1+v)/2-\sqrt C\) and \(y_+=d(1+v)/2+\sqrt C\). The derivative has signs positive, negative, positive on the three successive subintervals. Thus \(Q(y_-)\) is a strict local maximum and \(Q(y_+)\) is a strict local minimum, with \(Q_{\max}>Q_{\min}\). A horizontal line at \((1-w)/w\) intersects the graph three times precisely when \(Q_{\min}<(1-w)/w<Q_{\max}\), equivalently \(w_-<w<w_+\). All three intersections are simple. For \(w\notin[w_-,w_+]\) there is one simple sphere. On either boundary \(w=w_-\) or \(w=w_+\), there are exactly two distinct spheres, one double and one simple. In particular, no fourth nodal sphere is possible.

**3. The cusp and separation constants.** Put \(\varepsilon=v-v_c\downarrow0\). Differentiation of the exact quadratic expression gives
\[
C(v)=\gamma_d\varepsilon+O_d(\varepsilon^2),
\qquad \gamma_d=d\sqrt{2d+4}>0,
\]
so the turning-point separation obeys
\[
\boxed{y_+-y_-\sim2\sqrt{\gamma_d}\,\varepsilon^{1/2}.}
\]
Using the exact formula for \(Q'/Q\), integrate from \(y_-\) to \(y_+\), or equivalently from \(h=-\sqrt C\) to \(h=+\sqrt C\):
\[
\log\frac{Q_{\max}}{Q_{\min}}
=\int_{-\sqrt C}^{\sqrt C}
\frac{(v-1)(C-h^2)}{2v(D^2-h^2)}\,dh
\sim\frac{v_c-1}{3d\,v_c^2}\gamma_d^{3/2}\varepsilon^{3/2}.
\]
The equivalent follows uniformly on the shrinking interval because \(D^2\to2dv_c>0\) while \(|h|\le\sqrt C\to0\), and \(\int_{-\sqrt C}^{\sqrt C}(C-h^2)\,dh=4C^{3/2}/3\). Both extreme values tend to \(Q_c\). Applying the derivative of \(z\mapsto(1+e^z)^{-1}\) at \(z=\log Q_c\) proves the positive sharp cusp constant
\[
\boxed{w_+-w_-\sim K_d\varepsilon^{3/2},\quad
K_d=\frac{Q_c}{(1+Q_c)^2}\frac{v_c-1}{3d\,v_c^2}
\bigl(d\sqrt{2d+4}\bigr)^{3/2}.}
\]
Finally, \(b/a>\sqrt{v_c}=\sqrt{1+2/d}+\sqrt{2/d}\), and binomial expansion gives \(\sqrt{v_c}=1+\sqrt{2/d}+1/d+O(d^{-2})\) as \(d\to\infty\).

**4. Positivity in Fourier space and unimodality.** Since
\[
\widehat F(\xi)=w e^{-a^2\|\xi\|^2/2}+(1-w)e^{-b^2\|\xi\|^2/2}>0,
\]
all mixtures are positive definite. For every \(r>0\), \(\partial_rF(r)=-r\bigl(w a^{-2}G_a(r)+(1-w)b^{-2}G_b(r)\bigr)<0\). Thus the three-shell regime coexists with strict radial unimodality and a zero-free Fourier transform.

## Verification

Run `python3 verify.py` from the directory containing this result. This standard-library checker evaluates the logarithmic derivative against finite differences, locates the one- and three-shell regimes, verifies the root equations by the original two-exponential Laplacian expression, tests double-root locations and the sharp cusp equivalent across seven dimensions. The supplied run passed 308 numerical/algebraic checks. It is **supplementary** to the proof above and is not an exhaustive infinite-domain certificate.

For a concrete three-shell witness, take \(d=2\), \(a=1\), \(b=3\), and \(w=1/10\). Here \(v=9>v_c=(1+\sqrt2)^2\); direct evaluation gives \(0.05174<w_-<0.05175\) and \(0.20001<w_+<0.20003\), so all three zeros occur. More generally the exact formulas supply an immediate reproducible weight interval in every dimension and scale above threshold.

## Relationship to prior work

Mahmud, Winship, Lash, Ostrowski and Herrman (first public preprint April 10, 2026) investigate the **difference of two discrete normalized Gaussians** on a periodic grid, especially its Fourier symbol and a block encoding. Their accessible full mathematical preliminaries and main statements do not assert the **Laplacian of a positive continuous two-Gaussian mixture**, its complete nodal-shell count, or the dimension-dependent threshold. Difference-of-Gaussian approximations to a Laplacian-of-Gaussian motivate the distinct operator studied here; their spectral and block-encoding theorems do not imply the displayed cusp law.

The accessible manuscript *A sharp dimension-dependent log-concavity threshold for two-scale Gaussian mixtures* analyzes the **Hessian of the logarithm** of the same centered scale mixture, including a positive log-curvature shell and projection phenomena. This is the strongest directly comparable prior result inspected in full. Although \(\Delta F=F(\Delta\log F+\|\nabla\log F\|^2)\), a sign description of the log-Hessian does not determine the zeros of \(\Delta F\), and that manuscript does not state the three-shell classification or its cusp. The distinction between these two curvature invariants is essential.

Marta and Causin (first public preprint August 24, 2026) study diffusion and heat-kernel mixtures on compact manifolds and their dynamical behavior. Their inspected heat-mixture statements concern different geometries and phenomena. Classical Laplacian-of-Gaussian edge-detection and scale-space zero-crossing literature explains why nodal contours matter but, based on the accessible material, does not furnish this precise sharp two-scale positive-mixture theorem. No inference of universal novelty is made from failed searches.

## Limitations

The theorem is for **exactly two** positive, centered **isotropic** Gaussian components on Euclidean space, using a spatial Laplacian and positive interior mixture weights. It does not classify nonconcentric means, anisotropic covariance matrices, three or more scales, arbitrary mixtures, discrete periodic approximations, or time-evolution of the zero set of a fixed initial datum. The cusp describes the weight-window opening as \(v\downarrow v_c\), not a global extrema statement over other families. The supplied computer verification samples finitely many cases and does not itself prove the theorem. Earlier image-processing literature may contain an equivalent nodal-shell calculation under different terminology; that remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. J. Mahmud, J. Winship, T. Lash, J. Ostrowski and R. Herrman, *Explicit Block Encoding of Difference-of-Gaussian Operators on a Periodic Grid*, arXiv:2604.09538 (first publicly posted 2026-04-10), https://arxiv.org/abs/2604.09538.
2. *A sharp dimension-dependent log-concavity threshold for two-scale Gaussian mixtures*, publicly available manuscript (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-sharp-dimension-dependent-log-concavity-threshold-for-two-scal--f938c6ccc9e9/RESULT.md.
3. A. Marta and P. Causin, *A Theory of Speciation in Generative Diffusion Models on Compact Riemannian Manifolds*, arXiv:2608.23798 (first publicly posted 2026-08-24), https://arxiv.org/abs/2608.23798.
4. *Scaling Theorems for Zero-Crossings*, Massachusetts Institute of Technology repository (1983), https://dspace.mit.edu/entities/publication/bc73455a-3663-43ae-9707-08623c84b468 (abstract-level comparison only).
5. *Zero Crossings of the Laplacian of a Gaussian of the Image Brightness Function*, https://users.fmrib.ox.ac.uk/~steve/review/review/node13.html (background exposition).
