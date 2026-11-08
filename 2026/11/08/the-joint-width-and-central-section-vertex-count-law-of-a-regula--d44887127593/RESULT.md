# The joint width and central-section vertex-count law of a regular tetrahedron

## Finding

Let \(T\subset\mathbb R^3\) be a regular tetrahedron of unit edge length, centered at the origin. For a Haar-uniform unoriented plane normal \(U\in S^2\), let \(W\) be the Euclidean width of \(T\) perpendicular to \(U\), and let \(N\) be the number of vertices in the planar polygon \(T\cap U^\perp\). Then \(N\in\{3,4\}\) almost surely. Put
\[
 a=1/\sqrt2,\quad b=\sqrt{2/3},\quad c=\sqrt3/2,\quad
 \delta=\arctan\sqrt2,\quad
 \vartheta(w)=\arccos\!\left(\frac{w}{\sqrt{3(1-w^2)}}\right)\quad(a\le w\le c).
\]
The *joint subdensities* \(f_j(w)=\frac{d}{dw}\Pr(W\le w,\ N=j)\), with respect to Lebesgue measure, are exactly
\[
 f_4(w)=\frac{12}{\pi}\begin{cases}
 0,&w<a\text{ or }w>1,\\
 \delta-\vartheta(w),&a\le w<c,\\
 \delta,&c\le w\le1,
 \end{cases}
\]
and
\[
 f_3(w)=\frac{12}{\pi}\begin{cases}
 0,&w<b\text{ or }w>1,\\
 \frac{\pi}{2}-\delta-\vartheta(w),&b\le w<c,\\
 \frac{\pi}{2}-\delta,&c\le w\le1.
 \end{cases}
\]
The definitions at a finite set of endpoints do not affect the measures. In particular, all planes with \(W<b\) yield a quadrilateral almost surely, while conditional on \(W\ge c\), \(W\) is uniform on \([c,1]\) and *independent* of \(N\), with
\[
 \Pr(N=4\mid W\ge c)=\frac{2}{\pi}\arctan\sqrt2.
\]
For \(b<w<c\), \(\Pr(N=4\mid W=w)\) decreases strictly from \(1\) to \(2\delta/\pi\); it is constant for \(w\ge c\). The exact total masses are
\[
 \Pr(N=4)=\frac6\pi\arccos(-1/3)-3,
 \qquad\Pr(N=3)=4-\frac6\pi\arccos(-1/3).
\]
The claim of contribution is the *joint* law and its phase-transition/conditional-independence consequences. The marginal width law alone is not claimed as new.

## Assumptions and scope

The tetrahedron is Euclidean, regular, and has edge length exactly \(1\). A plane is taken through its centroid. The normal is distributed by normalized spherical surface measure; signs \(U\) and \(-U\) give the same plane. The section count is measured for generic orientations, excluding the measure-zero set where a vertex lies on the plane. This theorem concerns central sections, not random affine offsets, and widths are in physical units of the unit-edge tetrahedron.

## Proof

**1. Symmetric normalization.** Represent the unscaled tetrahedron by the four vertices
\[
 v_1=(1,1,1),\quad v_2=(1,-1,-1),\quad v_3=(-1,1,-1),\quad v_4=(-1,-1,1).
\]
Its edges have length \(2\sqrt2\), so divide all support-projection ranges by \(2\sqrt2\). Both width and the number of central-section vertices are invariant under permutations and sign changes of the absolute coordinates of \(U\). Indeed, any signed coordinate permutation carries the set of four vertices to itself or to its negative, and negating all vertex projections leaves both quantities unchanged. The unit sphere therefore consists, up to boundaries of area zero, of \(48\) equiprobable copies of the chamber
\[
 x\ge y\ge z\ge0,\qquad x^2+y^2+z^2=1.
\]
**2. Width and section count on the chamber.** The four unscaled scalar projections, already ordered from largest to smallest, are
\[
 h_1=x+y+z,\quad h_2=x-y-z,\quad h_3=-x+y-z,\quad h_4=-x-y+z.
\]
Thus \(W=(h_1-h_4)/(2\sqrt2)=(x+y)/\sqrt2\). We have \(h_1>0\), \(h_3<0\), and \(h_4<0\) except at negligible boundaries. A generic plane cuts exactly \(r(4-r)\) tetrahedron edges when \(r\) vertex projections are positive. Consequently \(N=4\) exactly when \(h_2>0\), equivalently \(x>y+z\), and otherwise \(N=3\).

**3. Exact area disintegration.** Set
\[
 w=(x+y)/\sqrt2,\qquad t=(x-y)/\sqrt2,
 \qquad t=\sqrt{1-w^2}\cos\phi,\quad
 z=\sqrt{1-w^2}\sin\phi.
\]
The chamber conditions \(x\ge y\ge z\ge0\) become \(0\le\phi\le\pi/2\) and
\[
 \frac{w}{\sqrt{1-w^2}}\ge \cos\phi+\sqrt2\sin\phi
 =\sqrt3\cos(\phi-\delta),\qquad \delta=\arctan\sqrt2.
\]
Latitude coordinates about the \(w\)-axis yield the *exact* sphere-area element \(d\sigma=dw\,d\phi\); no extra Jacobian is needed. In these variables, \(x>y+z\) is exactly \(\phi<\delta\). The chamber has \(1/48\) of the sphere area, hence the normalized probability measure is \(12\,dw\,d\phi/\pi\) on it.

**4. The angular intervals and three width phases.** Write \(q(w)=w/\sqrt{1-w^2}\). The inequality has no solutions for \(w<a=1/\sqrt2\). For \(a\le w<c\), let \(\vartheta(w)=\arccos(q(w)/\sqrt3)\). The permitted angles in \([0,\pi/2]\) are
\[
 [0,\delta-\vartheta(w)]
 \quad\text{and, when }w\ge b=\sqrt{2/3},\quad
 [\delta+\vartheta(w),\pi/2].
\]
The second interval first appears when \(q=\sqrt2\), which is precisely \(w=b\). At \(w=c=\sqrt3/2\), \(q=\sqrt3\), and all \(\phi\in[0,\pi/2]\) are permitted thereafter. The first interval is wholly in the \(N=4\) region \(\phi<\delta\), while the second lies wholly in the \(N=3\) region. Multiplication of their lengths by \(12/\pi\) proves both displayed subdensity formulas, including normalization and all endpoints.

**5. Conditional shape and monotonicity.** When \(w\ge c\), the two interval lengths are constant: \(\delta\) and \(\pi/2-\delta\). Hence the density of \(W\) is \(6\) on \([c,1]\), and the type probabilities there do not depend on \(w\); this proves the conditional independence. For \(b<w<c\), the conditional quadrilateral probability is
\[
 R(w)=\frac{\delta-\vartheta(w)}{\pi/2-2\vartheta(w)}.
\]
Differentiation with respect to \(\vartheta\) gives
\[
 \frac{dR}{d\vartheta}=\frac{2\delta-\pi/2}{(\pi/2-2\vartheta)^2}>0.
\]
Because \(\vartheta(w)\) strictly decreases with \(w\) and \(\delta>\pi/4\), \(R\) strictly decreases as claimed.

**6. Marginal-mass cross-check without integrating the formula.** Each of the six edges crosses the central plane if and only if its two endpoint projections have opposite signs. Each pair of tetrahedron vertex vectors meets at angle \(\arccos(-1/3)\), so for a uniform normal the crossing probability is that angle divided by \(\pi\). Linearity of expectation gives \(\mathbb E N=6\arccos(-1/3)/\pi\). As \(N\in\{3,4\}\), \(\Pr(N=4)=\mathbb E N-3\), establishing the total-mass identities independently.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. The program integrates each joint subdensity over all three width intervals, independently checks the total section-count probability, and checks the first two marginal width moments against the published formulas. It also samples 500,000 independent Haar normals, computes widths directly from four vertex scalar products, independently checks the sorted-absolute-coordinate width identity, determines section type from vertex signs, and compares ten bin/type masses against the analytic formulas. The fixed-seed run returned `VERIFY_OK` with maximum absolute empirical mass discrepancy below \(0.00077\). The finite simulation is a consistency check; the spherical disintegration above establishes the continuous-orientation quantifiers for every normal outside the specified null set.

## Relationship to prior work

Finch's 2011 preprint, *Width Distributions for Convex Regular Polyhedra* (arXiv:1110.0671), gives the tetrahedron's mean and second moment and identifies the then-unknown marginal density as a problem. A substantially later 2026 preprint by Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (arXiv:2609.26202), explicitly derives the regular tetrahedron's **marginal width density**. That marginal result is credited in full and is **not** claimed as a discovery here. The joint measure resolved by section vertex count, the two threshold implications, and the high-width conditional independence are not statements of the accessible abstract of that work; its complete full text could not be examined, leaving a live priority risk. Feldman and Klain (2008, arXiv:0809.3459) study the vertex count of random *orthogonal projections* of simplices, a distinct observable from the centroidal plane-section vertex count used here. Neither its projection-angle formula nor the marginal width density implies the specific joint distribution without additional geometric analysis.

## Limitations

The theorem is restricted to regular tetrahedra and central planes, with exact Haar orientations. It does not provide a stable estimator from finite noisy observations, and it does not classify random affine-offset sections or arbitrary tetrahedra. The 2026 broad polyhedral width-density theory could contain uninspected material relevant to historical priority; mathematical correctness of the independently derived bivariate formula does not establish absolute novelty. No independent audit has been performed.

## References

1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first publicly posted 2011-10-04, https://arxiv.org/abs/1110.0671.
2. D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459, first posted 2008-09-19, https://arxiv.org/abs/0809.3459.
3. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first posted 2026-08-10, https://arxiv.org/abs/2609.26202.
4. K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, DOI:10.1111/j.1365-2818.1982.tb00443.x (abstract consulted; not available in full).
