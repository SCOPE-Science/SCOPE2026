# Centroidal chord spectrum and dual rare-direction limits of the regular tetrahedron

## Finding

Consider the regular tetrahedron
\[
K=\operatorname{conv}\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}\subset\mathbb R^3.
\]
For a uniformly distributed unit vector \(U\in S^2\), let \(L(U)\) be the Euclidean length of the entire intersection \(K\cap\mathbb R U\). This is an orientation-uniform **center-passing** line, not a motion-invariant translated random line. Then its support is exactly \([\sqrt2,4/\sqrt3]\). It has an explicit one-dimensional integral distribution (given below) and the sharp endpoint laws
\[
\Pr\{L<\sqrt2+\varepsilon\}=3\varepsilon+o(\varepsilon),\qquad
\Pr\{L>4/\sqrt3-\varepsilon\}=\frac{\sqrt3}{4\pi}\varepsilon^2+o(\varepsilon^2).
\]
The first event concentrates equally near the twelve oriented directions \((\pm1,\pm1,0)/\sqrt2\) and their coordinate permutations. In orthonormal local coordinates \((\eta,z)\), rescaling by \(\varepsilon^{-1/2}\) yields the uniform distribution on the ellipse
\[
E=\{(v,w): v^2/\sqrt2+\sqrt2\,w^2<1\}.
\]
The second event concentrates equally near the eight oriented tetrahedral vertex/antivertex directions. At \((1,1,1)/\sqrt3\), write tangent perturbations as \((a,b,c)\) in the plane \(a+b+c=0\). Rescaling by \(\varepsilon^{-1}\) yields the uniform distribution on the planar equilateral triangle
\[
T=\{(a,b,c)\in\mathbb R^3:a+b+c=0,\ a,b,c>-1/6\}.
\]
Both conditional convergence statements hold in total variation, after recording which extremizing direction is approached.

For the full distribution, put \(A(\phi)=\cos\phi+\sin\phi\) for \(0\le\phi\le\pi/4\). For \(\sqrt2<\ell<4/\sqrt3\), define \(q_*(\ell,\phi)=0\) when \(\ell\le 2/A(\phi)\); otherwise set
\[
q_*(\ell,\phi)=\min\left\{\sin\phi,\ \sqrt{\frac{\ell^2 A^4-4A^2}{A^2(\ell^2+2)+2A\sqrt{A^2(\ell^2+1)+\ell^2}}}\right\},
\]
with \(A=A(\phi)\) inside the radical. Then
\[
\boxed{\Pr\{L\le\ell\}=\frac{12}{\pi}\int_0^{\pi/4}\frac{q_*(\ell,\phi)}{\sqrt{1+q_*(\ell,\phi)^2}}\,d\phi.}
\]
Outside the support, the distribution function is zero or one as appropriate. Equality boundaries have probability zero.

## Assumptions and scope

All distances refer to the explicitly normalized tetrahedron above, whose edge length is \(2\sqrt2\) and whose centroid is the origin. The direction is uniform with respect to spherical area, normalized by \(4\pi\). The two orientations of an unoriented line have equal probabilities and identical chord lengths; the displayed count of extremizing directions is for oriented vectors. The endpoint asymptotics hold for positive \(\varepsilon\) tending to zero, with tetrahedron fixed. Smooth tangent-plane coordinates are defined in the proof; all conditional limits use the corresponding Euclidean area measure on their planar domains.

## Proof

**Chord formula and symmetry.** The tetrahedron is the intersection of the four halfspaces \(v_i\cdot x\ge-1\), where \(v_i\) are its four vertices. On a ray \(rU\), the first boundary hit in the positive direction is at \(r=(\max_i[-v_i\cdot U])^{-1}\); along the negative direction it is at \(r=(\max_i[v_i\cdot U])^{-1}\). Thus
\[
L(U)=\frac1{\max_i(v_i\cdot U)}+\frac1{-\min_i(v_i\cdot U)}.
\]
Signed coordinate permutations map the tetrahedron either to itself or to its central reflection; replacing \(K\) by \(-K\) does not change a line's length. Therefore it is enough to consider \(x\ge y\ge z\ge0\) for \(U=(x,y,z)\in S^2\). Direct comparison of the four vertex inner products gives extrema \(x+y+z\) and \(-x-y+z\), hence
\[
L(U)=\frac1{x+y+z}+\frac1{x+y-z}=\frac{2(x+y)}{(x+y)^2-z^2}.
\]
This also proves that every one of the 48 congruent spherical chambers has the same chord-length law.

**Global extrema.** Parameterize the chamber by
\[
x=\cos\theta\cos\phi,\quad y=\cos\theta\sin\phi,\quad z=\sin\theta,
\qquad0\le\phi\le\pi/4,\quad0\le\tan\theta\le\sin\phi.
\]
Write \(q=\tan\theta\) and \(A=\cos\phi+\sin\phi\). Then
\[
L=\frac{2A\sqrt{1+q^2}}{A^2-q^2},
\]
which is strictly increasing in \(q>0\). At \(q=0\) this is \(2/A\ge\sqrt2\), with equality only at \(\phi=\pi/4\). The maximal value for a fixed \(\phi\) occurs at \(q=\sin\phi\). Writing \(t=\tan\phi\in[0,1]\), it becomes \(2(1+t)\sqrt{1+2t^2}/(1+2t)\). The elementary identity
\[
4(1+2t)^2-3(1+t)^2(1+2t^2)
=(1-t)(6t^3+18t^2+11t+1)\ge0
\]
proves that this is at most \(4/\sqrt3\), with equality only at \(t=1\). Symmetry produces exactly the twelve minimum and eight maximum oriented directions stated above.

**Exact distribution.** The spherical area element in the chamber is \(\cos\theta\,d\theta\,d\phi=dq\,d\phi/(1+q^2)^{3/2}\). Monotonicity in \(q\) shows that \(L\le\ell\) holds on the interval \(0\le q\le q_*\). Solving \(\ell^2(A^2-q^2)^2=4A^2(1+q^2)\) for its smaller nonnegative root and rationalizing the subtraction yields the displayed expression for \(q_*\). Integrating \(dq/(1+q^2)^{3/2}\) gives \(q/\sqrt{1+q^2}\), and dividing the 48 congruent chamber integrals by total spherical area \(4\pi\) gives the factor \(12/\pi\).

**Minimum endpoint and marked limit.** At \(U_0=(1,1,0)/\sqrt2\), use \(x=\sqrt{1-z^2}\cos(\pi/4+\eta)\), \(y=\sqrt{1-z^2}\sin(\pi/4+\eta)\), with \(z\) small and either sign permitted. Substitution into the exact chord formula yields the local Taylor expansion
\[
L-\sqrt2=\eta^2/\sqrt2+\sqrt2\,z^2+O((|\eta|+|z|)^4).
\]
Spherical area is \((1+o(1))\,d\eta\,dz\). Each minimum therefore contributes area \(\pi\varepsilon+o(\varepsilon)\): the ellipse of normalized deficit has area \(\pi\), since the product of its quadratic coefficients is one. There are twelve separated oriented minima. Division by \(4\pi\) yields the constant \(3\). The normalized area measures of their rescaled sublevel sets converge in \(L^1\), proving the asserted uniform-ellipse total-variation limit.

**Maximum endpoint and marked limit.** Near the maximizing direction \(U_+=(1,1,1)/\sqrt3\), write \(U=(U_++\delta)/\sqrt{1+\|\delta\|^2}\), where \(\delta=(a,b,c)\) and \(a+b+c=0\). The four vertex products are \(\sqrt3+O(\|\delta\|^2)\) and \(-1/\sqrt3+2a+O(\|\delta\|^2)\), \(-1/\sqrt3+2b+O(\|\delta\|^2)\), \(-1/\sqrt3+2c+O(\|\delta\|^2)\). Thus, uniformly on the tangent plane,
\[
\frac4{\sqrt3}-L(U)=-6\min(a,b,c)+O(\|\delta\|^2).
\]
The linear sublevel set \(a,b,c>-\varepsilon/6\) in the plane \(a+b+c=0\) is an equilateral triangle with side \(\varepsilon/\sqrt2\) and Euclidean area \(\sqrt3\,\varepsilon^2/8\). Spherical area agrees with planar area to leading order. There are eight symmetry-equivalent directed maxima, giving \(8(\sqrt3/8)/(4\pi)=\sqrt3/(4\pi)\). Rescaling and dominated convergence of the uniform bounded densities on the shrinking triangle-shaped regions gives total-variation convergence. The singular edges of the piecewise-linear deficit have planar measure zero.

## Verification

The standalone file `check.py` independently computes the line intersection from all four facet inequalities, compares it against the sorted-coordinate formula on 120,000 fixed-seed spherical samples, integrates the exact distribution at seven interior thresholds, and numerically tests each endpoint coefficient at four positive deficits. The computed maximum disagreement between the two chord formulas was below \(9\times10^{-16}\); the distribution quadrature and simulation agreed within \(0.001\) at the seven printed thresholds. The checker is deterministic given its pinned seed and its requirements, and exits nonzero if its assertions fail. These finite checks do not constitute a proof of the continuum statements; the exact inequalities, chamber integral, and local expansions above provide that proof.

## Relationship to prior work

Ciccariello's 2005 intersect/chord-length distribution of the regular tetrahedron is the closest classical primary paper. Its reported distribution concerns the (translation-averaged) integral-geometric/correlation-function ensemble, whereas this finding fixes every line through the centroid and averages only orientation; the two probability measures are different. Ciccariello's 2020 full-text general polyhedron chord-distribution treatment likewise derives the covariogram-related chord-length distribution, not the centroidal directional law. Brzezinski's 2013 central-section study concerns planar section volumes, rather than the lengths of centroid-passing one-dimensional sections. Published geometric records on random tetrahedral shadow diameters and plane-section outer radii concern different observables; neither their stated conclusions nor the average translated-line distribution implies the formulas above without an additional directional inversion. This comparison supports a best-knowledge distinction, not absolute priority. The complete 2005 paper was not accessible in the source investigation, so unexamined historical material remains a specific risk.

## Limitations

The theorem concerns one exact Euclidean regular tetrahedron and Haar-uniform centroid-passing lines. It does not give the motion-invariant translated-line chord distribution, interior random-point distances, arbitrary translated tetrahedra, or uniform assertions over varying simplex shapes. Finite simulation cannot substitute for the analytic endpoint proof, and no claim of independent historical-priority certification is made.

## References

- S. Ciccariello, "The intersect distribution of the regular tetrahedron," *Journal of Applied Crystallography* **38** (2005), 97–106, published online January 27, 2005. DOI: https://doi.org/10.1107/S0021889804028328.
- S. Ciccariello, "The chord-length distribution of a polyhedron," *Acta Crystallographica A* **76** (2020), 474–488. Full open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7331884/.
- P. Brzezinski, "Volume estimates for sections of certain convex bodies," *Mathematische Nachrichten* **286** (2013), 1726–1743. DOI: https://doi.org/10.1002/mana.201200119.
