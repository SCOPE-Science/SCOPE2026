# Sharp five-node positivity radius for perturbed trigonometric quadrature

## Finding

For five ordered perturbed roots of unity
\[
x_j=\frac{2\pi}{5}(j+\delta_j),\quad j\in\{0,1,2,3,4\},\qquad |\delta_j|\le\alpha<\frac12,
\]
let the normalized interpolatory trigonometric quadrature rule have unique real weights \(w_j\) satisfying
\[
\sum_{j=0}^{4}w_jp(x_j)=\frac1{2\pi}\int_0^{2\pi}p(t)\,dt\quad\text{for all }p\in\operatorname{span}_{\mathbb R}\{1,\cos t,\sin t,\cos 2t,\sin 2t\}.
\]
The **sharp all-grid nonnegative-weight radius** is
\[
\boxed{\alpha_* = \frac5{4\pi}\arccos\!\left(\cos\frac\pi5-1\right)-\frac12 =0.2014594224605106\ldots.}
\]
All five weights are strictly positive whenever \(0\le\alpha<\alpha_*\); all are nonnegative when \(\alpha=\alpha_*\). For each \(\alpha\in(\alpha_*,1/2)\), the admissible vector \((\delta_0,\ldots,\delta_4)=(0,-\alpha,+\alpha,-\alpha,+\alpha)\) makes \(w_0<0\). Exactly at \(\alpha_*\), for a fixed index \(j\), equality \(w_j=0\) occurs if and only if the four other perturbations, in cyclic order from \(j\), are \((-\alpha_*,+\alpha_*,-\alpha_*,+\alpha_*)\); the perturbation at \(j\) may be any admissible value.

Thus positive quadrature weights are **not guaranteed even strictly below the one-quarter grid-perturbation threshold** governing a standard uniform Fourier-conditioning bound.

## Assumptions and scope

The integration measure is normalized Lebesgue measure on the circle. The five nodes are distinct because \(\alpha<1/2\). The interpolation space has real dimension five, with frequencies \(0,1,2\), and the weights are the unique weights exact on this entire space. This theorem concerns positivity of *unconstrained interpolatory weights*, not the existence of some other positive rule on the same or additional nodes, conditioning of the Vandermonde matrix, or asymptotic convergence as the number of nodes grows. The index \(j\) is modulo five. At the stated equality pattern the four perturbations are understood relative to the unshifted five-point base grid.

## Proof

**1. Signed weight formula.** Fix a target node \(j\), rotate all grid angles by the nominal angle \(2\pi j/5\), and lift the four other angles in the cyclic order following it to \(a<b<c<d\). These angles have the form \(2\pi(k+\varepsilon_k)/5\), for \(k=1,2,3,4\), with \(|\varepsilon_k|\le\alpha\). The target angle \(z\) lies strictly before \(a\) and strictly after \(d-2\pi\). The cardinal degree-two trigonometric polynomial is
\[
\ell_j(t)=\frac{\sin((t-a)/2)\sin((t-b)/2)\sin((t-c)/2)\sin((t-d)/2)}{D},\qquad D=\prod_{v\in\{a,b,c,d\}}\sin((z-v)/2)>0.
\]
Its normalized integral is \(w_j\). The four-sine product-to-sum identity gives
\[
w_j=\frac{S(a,b,c,d)}{8D},\qquad
S=\cos\frac{a+b-c-d}{2}+\cos\frac{a+c-b-d}{2}+\cos\frac{a+d-b-c}{2}.
\]
Therefore the sign of \(w_j\) is precisely the sign of \(S\), independent of the target-node perturbation.

**2. Extremal reduction.** Put \(u=(b-a)/2\), \(v=(c-b)/2\), \(w=(d-c)/2\), and \(T=u+2v+w\). Then
\[
S=\cos T+2\cos u\cos w.
\]
For \(\alpha\le\alpha_*<1/4\), we have \(0<u,w<\pi/2\), \(0<T<\pi\), and
\[
\frac{\partial S}{\partial a}=\frac12\sin T+\sin u\cos w>0,\qquad
\frac{\partial S}{\partial d}=-\frac12\sin T-\cos u\sin w<0.
\]
It follows that the least possible \(S\) is attained with \(a=(1-\alpha)2\pi/5\) and \(d=(4+\alpha)2\pi/5\).

Write \(r=\pi\alpha/5\), \(A=4\pi/5\), and \(B=2\pi/5\). At the remaining four corners, the values of \(S\) are, respectively,
\[
S_{\mathrm{alt}}=1+\cos A+\cos(B+4r),
\quad S_{\mathrm{mid}}=\cos(A+2r)+\cos(B+2r)+\cos(2r),
\quad S_{\mathrm{other}}=1+\cos(A+4r)+\cos B,
\]
with \(S_{\mathrm{mid}}\) occurring at two corners. The differences factor exactly as
\[
S_{\mathrm{mid}}-S_{\mathrm{alt}}=2\sin r\,[\sin(B+3r)-\sin(A+r)-\sin r],
\]
\[
S_{\mathrm{other}}-S_{\mathrm{alt}}=2\sin(2r)\,[\sin(B+2r)-\sin(A+2r)].
\]
Both are positive for \(0<r\le\pi/20\). Indeed, on this interval the first bracket is bounded below by \(\sin(2\pi/5)-\sin(\pi/5)-\sin(\pi/20)>0\), while the second is at least \(\sin(2\pi/5)-\sin(\pi/5)>0\).

It remains to exclude an interior minimum below the corners. For either \(b\) or \(c\), with the other variables fixed, \(S\) satisfies \(S''+S/4=0\). On an interval of length \(L=2\alpha(2\pi/5)<2\pi\), its value is the sine interpolation of its two endpoint values:
\[
S(x)=\frac{\sin((x_+-x)/2)}{\sin(L/2)}S(x_-)+\frac{\sin((x-x_-)/2)}{\sin(L/2)}S(x_+).
\]
The coefficients are nonnegative and their sum is at least one. Consequently, whenever both endpoint values are at least a nonnegative \(m\), every intermediate value is at least \(m\). For \(\alpha\le\alpha_*\), the four corner values are all at least \(S_{\mathrm{alt}}\ge0\), so applying this interpolation successively to \(b\) and \(c\) proves \(S\ge S_{\mathrm{alt}}\) over the whole four-node box. For \(\alpha=0\), the box is a singleton.

**3. Sharp threshold.** The function \(S_{\mathrm{alt}}=1+\cos(4\pi/5)+\cos(2\pi/5+4\pi\alpha/5)\) is strictly decreasing for \(0\le\alpha<1/2\). Its unique zero is the displayed \(\alpha_*\), and elementary angle bounds give \(0<\alpha_*<1/4\). Below it, the universal lower bound on \(S\) is strictly positive; at it, \(S\ge0\). Strictness in the endpoint comparisons and in the monotonic adjustments of \(a,d\), together with the sine interpolation, implies the asserted equality pattern for a vanishing weight.

For \(\alpha>\alpha_*\), take \(\delta_j=0\), and after \(j\) take the four other perturbations \((-\alpha,+\alpha,-\alpha,+\alpha)\). Then \(S=S_{\mathrm{alt}}<0\), while \(D>0\), yielding \(w_j<0\). Cyclic relabeling completes the claim for all five weights.

## Verification

The standalone file `verify_five_node.py` independently solves the full five-by-five Fourier-moment system, compares each weight with the four-sine mean identity on 1,250 sampled perturbation configurations (6,250 weight comparisons), and checks all 16 corners for six radii through the threshold. It also checks the sign reversal at perturbations just below and just above the exact critical radius. Run with `python verify_five_node.py` using Python 3 and NumPy. All supplementary tests passed. The proof above establishes the continuum statement; finite tests are not an exhaustive proof.

For the alternating perturbations at \(\alpha=0.24\), the normalized weight at the unperturbed node is approximately \(-0.0571643783884\), despite \(0.24<1/4\).

## Relationship to prior work

Austin's 2016 thesis and Austin–Trefethen (first arXiv version 2016) analyze interpolation and quadrature on arbitrary perturbed periodic grids, including numerical exploration of negative weights at larger grid sizes. The thesis gives experimental negative-weight patterns for seven and nine nodes, but no exact five-node all-perturbation positivity radius in the inspected quadrature section. Yu–Townsend (first arXiv version 2022) prove that for any fixed positive perturbation, some sufficiently large trigonometric quadrature can have a negative weight; their alternating perturbation construction and their quantitative lower bound on the required size are already known and are **not** claimed as discoveries here. The present theorem isolates the sharp universal radius and extremizer classification at the first five-node degree-two case, a finite problem not implied by those asymptotic statements. A related published degree-one three-node result has a different perturbation barrier and does not imply the degree-two formula.

## Limitations

The result applies only to the five-node, second-harmonic interpolatory rule, and only to worst-case bounded independent node perturbations on a periodic base grid. It does not determine the sharp radius for seven or more nodes, any probabilistic positivity frequency, or reconstruction accuracy for arbitrary functions. Some earlier numerical experiments already exhibited negative weights under sub-quarter perturbations; the contribution is the rigorous sharp five-node boundary and equality classification, not the mere possibility of negative weights. Historical prior art under alternative trigonometric moment or convex-geometric formulations remains a publication-priority risk.

## References

1. A. P. Austin, *Some New Results on and Applications of Interpolation in Numerical Computation*, University of Oxford DPhil thesis (2016), archived 2016-12-08, https://doi.org/10.5287/ora-dqjx80ezd (especially section 3.5.2).
2. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (first posted 2016-12-13), https://arxiv.org/abs/1612.04018; SIAM J. Numer. Anal. 55 (2017), 2113–2122.
3. A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (first posted 2022-02-09), https://arxiv.org/abs/2202.04722; section 4.1 and Appendix B.
