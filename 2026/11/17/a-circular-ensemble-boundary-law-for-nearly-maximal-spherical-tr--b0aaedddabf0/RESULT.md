# A circular-ensemble boundary law for nearly maximal spherical triangle perimeters

## Finding
Let \(A,B,C\) be independent uniform points of the unit two-sphere, let \(d\) be minimizing spherical geodesic distance, and set \(P=d(A,B)+d(B,C)+d(C,A)\). The maximal possible perimeter is \(2\pi\). For \(\varepsilon\downarrow0\),
\[
\Pr\{P>2\pi-\varepsilon\}\sim C_*\sqrt{\varepsilon},\qquad
C_*=\frac{3\pi\Gamma(3/4)}{\Gamma(1/4)^3}=0.242332519572411\ldots.
\]
Beyond this scalar asymptotic, the **entire marked conditional configuration** has an explicit limit in total variation. By rotational invariance, set
\[
A=(1,0,0),\quad B=(\cos a,\sin a,0),\quad C=(\cos z\cos\theta,\cos z\sin\theta,\sin z),
\]
with \(0<a<\pi\), \(-\pi/2<z<\pi/2\), \(0\le\theta<2\pi\). Define \(u=\theta-\pi\), \(h=z/\sqrt\varepsilon\), and
\[
H(a,u)=\sqrt{\frac{2\sin u\sin(a-u)}{\sin a}}\quad(0<u<a<\pi).
\]
Conditioned on \(P>2\pi-\varepsilon\), the law of \((a,u,h)\) converges **in total variation** to the probability density
\[
p_0(a,u,h)=\frac{\sin a}{8\pi C_*}\,\mathbf1\{0<u<a<\pi,\ |h|<H(a,u)\}.
\]
Its \((a,u)\)-marginal has density proportional to \(\sqrt{\sin a\sin u\sin(a-u)}\). Equivalently, after setting \(\alpha=2u\), \(\beta=2a\), the ordered phases \(0<\alpha<\beta<2\pi\) have the **three-particle circular Dyson density with repulsion exponent \(1/2\)**, with the first phase fixed to zero. Given the angles, \(h/H(a,u)\) is uniform on \([-1,1]\) independently of the angles. In particular, conditioned on the rare event, the scaled perimeter deficit \((2\pi-P)/\varepsilon\) converges jointly and independently of the limiting angles to \(\operatorname{Beta}(1/2,1)\).

## Assumptions and scope
All three vertices are independent and uniform with respect to spherical area, on a round sphere of radius one; the edges use unique minimizing great-circle arcs almost surely. The coordinate frame is chosen measurably by the ordered pair \((A,B)\): the positively oriented equatorial basis vectors are \(A\), the normalized component of \(B\) orthogonal to \(A\), and their cross product. The third vertex latitude \(z\) is signed in that frame. The variable \(u\) is allowed in \([-\pi,\pi)\) before conditioning; the limiting density is supported on \(0<u<a\). The total-variation assertion concerns the rescaled coordinate law on the common measurable space \((0,\pi)\times[-\pi,\pi)\times\mathbb R\), not an unmarked full-rotation quotient. Scaling the sphere's radius multiplies all geodesic distances by that radius. No finite-threshold exact density or quantitative total-variation error rate is claimed.

## Proof
**1. Exact sampling measure and maximal configurations.** Rotational invariance makes \(a\) have density \(\sin a/2\), and given the pair, the third vertex has \((\theta,z)\)-density \(\cos z/(4\pi)\). For \(z=0\), the third point lies on the great circle of the first pair. The perimeter is exactly \(2\pi\) precisely when \(\pi\le\theta\le\pi+a\), up to endpoints. For other fixed \((a,\theta)\) its perimeter is strictly smaller. Thus the configurations contributing at leading order have \(0<u<a\) and \(z\to0\).

**2. Boundary quadratic form.** On every compact subset of \(0<u<a<\pi\), use the spherical distance formula
\[
P(a,\pi+u,z)=a+\arccos(-\cos z\cos u)+\arccos(-\cos z\cos(a-u)).
\]
Taylor expansion at \(z=0\), with a uniform fourth-order remainder on such compact sets, gives
\[
2\pi-P(a,\pi+u,z)=\frac{\sin a}{2\sin u\sin(a-u)}z^2+O(z^4).
\]
Therefore, with \(z=\sqrt\varepsilon h\), the rescaled rare-event indicator tends pointwise almost everywhere to \(\mathbf1\{0<u<a<\pi,\ |h|<H(a,u)\}\).

**3. No mass escapes to endpoint singularities.** Let \(s=P/2\) and let \(b,c\) be the other two side lengths. The elementary Gram-determinant identity
\[
\det\begin{pmatrix}1&\cos a&\cos b\\\cos a&1&\cos c\\\cos b&\cos c&1\end{pmatrix}
=4\sin s\sin(s-a)\sin(s-b)\sin(s-c)
\]
is checked by multiplying the spherical cosine identities (or by direct trigonometric expansion). Its left side, in the chosen coordinates, equals \(\sin^2a\sin^2z\). Since \(P\le2\pi\), on \(E_\varepsilon=\{P>2\pi-\varepsilon\}\) each sine factor on the right is at most one and \(\sin s=\sin((2\pi-P)/2)\le\varepsilon/2\), so
\[
|\sin z|\le\min\{1,\sqrt{2\varepsilon}/\sin a\}.
\]
Because \(\sin z\) is uniform on \([-1,1]\) given \(a\), the normalized event mass with \(a\) in either \((0,\delta)\) or \((\pi-\delta,\pi)\) is at most \(O(\delta\sqrt\varepsilon)\), uniformly as \(\varepsilon\downarrow0\). On a fixed \(\delta\le a\le\pi-\delta\), the displayed bound gives \(|z|=O_\delta(\sqrt\varepsilon)\). Compactness excludes angular sectors a fixed distance outside \([\pi,\pi+a]\), and angular endpoint strips of width \(\eta\) contribute at most \(O_\delta(\eta\sqrt\varepsilon)\). Letting \(\varepsilon\downarrow0\) first and then \(\eta,\delta\downarrow0\) proves that all leading mass is accounted for by the pointwise quadratic expansion.

**4. Limiting measure and normalization.** The joint density of \((a,u,h)\) before imposing the rare event is
\[
\sqrt\varepsilon\frac{\sin a}{8\pi}\cos(\sqrt\varepsilon h),
\]
on its coordinate support. The previous localization and expansion imply convergence of the rescaled unnormalized rare-event measures, including total masses, to
\[
\frac{\sin a}{8\pi}\mathbf1\{0<u<a<\pi,\ |h|<H(a,u)\}\,da\,du\,dh.
\]
The total mass is
\[
C_* = \frac{\sqrt2}{4\pi}I,\qquad
I=\int_0^\pi\int_0^a\sqrt{\sin a\sin u\sin(a-u)}\,du\,da.
\]
Use \(\alpha=2u\), \(\beta=2a\). The integrand becomes one factor \(1/(2\sqrt2)\) times the circular Vandermonde product \(\prod_{i<j}|e^{i\theta_i}-e^{i\theta_j}|^{1/2}\) for \((\theta_1,\theta_2,\theta_3)=(0,\alpha,\beta)\). The ordered domain occupies half of the two-free-phase torus. The classical Dyson integral with parameter \(\gamma=1/4\) gives
\[
16\sqrt2 I=(2\pi)^2\frac{\Gamma(1+3/4)}{\Gamma(1+1/4)^3}.
\]
Consequently \(C_*=\pi\Gamma(7/4)/(16\Gamma(5/4)^3)=3\pi\Gamma(3/4)/\Gamma(1/4)^3\).

**5. Total variation and overshoot.** The rescaled unnormalized coordinate densities converge almost everywhere to the displayed limiting density and their integrals converge to \(C_*>0\). Scheffé's lemma now gives convergence in \(L^1\), equivalently total-variation convergence of the conditional coordinate laws. Integrating the limiting density in \(h\) yields the claimed angular density, while \(h/H(a,u)\) is conditionally uniform on \([-1,1]\). The quadratic expansion also shows that \((2\pi-P)/\varepsilon\to(h/H)^2\), which has \(\operatorname{Beta}(1/2,1)\) law and is independent of the limiting angular variables.

## Verification
A standalone NumPy/SciPy script, `check.py`, computes the two-dimensional normalization integral by Gauss–Legendre quadrature at two resolutions, compares the exact gamma constant, and independently samples eight million spherical triangles at three perimeter thresholds. It checks the \(\sqrt\varepsilon\) coefficient, the limiting mean side length \(2\pi/3\), the limiting mean of the normalized deficit \(1/3\), and its CDF at \(1/4\), equal to \(1/2\). Execute `python check.py` with the dependencies in `requirements.txt`. The script is a numerical corroboration; the infinite limiting claims rest on the proof above.

## Relationship to prior work
The **scalar perimeter density** of three uniform points on a sphere is classical: Jones and Benyon-Tinker (1994, unpublished as cited in Finch–Jones) gave an elliptic-integral representation, reproduced and discussed in Finch–Jones (arXiv:1009.5329, first posted September 27, 2010). Finch–Jones specifically note that the perimeter density diverges at \(2\pi\). Thus the existence of a scalar density and its divergence are **not** new, and the leading scalar coefficient can in principle be extracted from that known formula. The contribution here is the evaluated gamma normalization together with the explicit **marked high-perimeter boundary law in total variation**, including the circular-ensemble angular density and transverse uniform mark. General spherical-triangle shape-density literature (including Le, 1989) is a priority risk, as a full shape density can encode related conditional information. No claim of a new general formula for spherical triangle perimeter is made.

## Limitations
The result treats three area-uniform points on the complete round two-sphere only. It does not include density perturbations, caps, other curvature values, or higher-dimensional spheres. The proof yields an asymptotic and total-variation convergence without an explicit convergence rate. Existing full-shape-density theorems may allow an independent derivation of portions of this statement; historical priority and independent correctness verification are not established here.

## References
1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, publicly posted 2010-09-27 (version 3 dated 2015-12-21), especially introduction and sections 2.2–2.3. https://arxiv.org/abs/1009.5329
2. A. J. Jones and G. Benyon-Tinker, *The jet-set travelling salesman: (1) Triangular tours*, unpublished 1994 manuscript cited in Finch–Jones. Full source not obtained.
3. H. Le, *Random spherical triangles II: Shape densities*, Advances in Applied Probability 21 (1989), 581–594, DOI:10.2307/1427637. Full text not obtained.
4. F. J. Dyson, *Statistical theory of the energy levels of complex systems. I*, Journal of Mathematical Physics 3 (1962), 140–156; classical circular gamma integral, with parameter \(1/4\) in the normalization here.
