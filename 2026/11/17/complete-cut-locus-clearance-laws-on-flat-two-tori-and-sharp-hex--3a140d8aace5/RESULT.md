# Complete cut-locus clearance laws on flat two-tori and sharp hexagonal stochastic dominance

## Finding

Fix a two-dimensional Euclidean lattice \(\Lambda\) with covolume \(A>0\), and let \(T=\mathbb R^2/\Lambda\) be the intrinsically flat torus. For a fixed \(o\in T\), let \(C(o)\) be its intrinsic geodesic cut locus. Take \(Z\) uniform for normalized area measure on \(T\), and set \(D=\operatorname{dist}_T(Z,C(o))\). The following is a complete law valid for every shape of flat two-torus, including rectangular and rhombic degenerations.

Choose a Gauss-reduced lattice basis \(u=(a,0)\), \(v=(p,q)\), with \(a>0\), \(b=\sqrt{p^2+q^2}\ge a\), \(0\le p\le a/2\), and \(q>0\). Set
\[
 c=\sqrt{(a-p)^2+q^2},\qquad s=a+b-c>0,\qquad t_*={ap\over s},\qquad A=aq.
\]
For all \(0\le r\le a/2\), the exact survival function is
\[
 \boxed{\Pr(D\ge r)=
 {4b(a/2-r)(b/2-r)\over a q^2}
 -{s^2\over a^2q^2}\bigl(\max\{t_*-r,0\}\bigr)^2.}
\]
For \(r>a/2\), this probability is zero. The formula is continuous and nonnegative; at \(r=0\) it equals one. For \(0<p<a/2\) the only interior change of quadratic branch occurs at \(t_*\); the function is \(C^1\), and the jump in its second derivative (right minus left) is exactly \(2s^2/(a^2q^2)>0\). For \(p=0\) or \(p=a/2\) there is no interior branch switch.

In a neighborhood of \(a/2\), write \(\delta=a/2-r\downarrow0\). If \(b>a\) then
\[
 A\Pr(D\ge a/2-\delta)\sim{2b(b-a)\over q}\,\delta.
\]
If \(b=a\) and \(p<a/2\), then
\[
 A\Pr(D\ge a/2-\delta)\sim {4a\over q}\,\delta^2.
\]
For \(b=a\), \(p=a/2\) (the equilateral/triangular lattice), the coefficient instead is \(2\sqrt3\), i.e. \(A\Pr(D\ge a/2-\delta)\sim2\sqrt3\,\delta^2\). In particular the upper-tail exponent is two precisely for *well-rounded* planar lattices (those with two independent shortest vectors), and one otherwise.

Among all flat two-tori with fixed area \(A\), the equilateral (triangular-lattice) torus uniquely stochastically maximizes cut-locus clearance. Precisely, if \(D_{\rm hex}\) is the same statistic for the regular hexagonal Dirichlet cell of covolume \(A\), then for every \(r\ge0\),
\[
 \boxed{\Pr(D\ge r)\le \Pr(D_{\rm hex}\ge r)
   =\bigl(\max\{1-r\sqrt{2\sqrt3/A},0\}\bigr)^2.}
\]
Unless \(\Lambda\) is similar to the triangular lattice, the inequality is strict throughout \(0<r<\sqrt{A/(2\sqrt3)}\). Consequently every increasing nonconstant power moment of clearance is uniquely maximized by the equilateral flat torus at fixed area.

## Assumptions and scope

All distances are intrinsic geodesic distances; no extrinsic embedding is used. Flat means the quotient Euclidean metric. Cut loci are taken relative to one fixed basepoint; translation invariance makes the distribution independent of the basepoint. Choosing a Gauss-reduced basis in the indicated sector is possible after reflections and basis substitutions. Equalities at lattice-moduli boundaries are included. The distribution is of distance **to a cut locus**, not the better-studied distribution of pairwise distances of two independently sampled torus points.

## Proof

**(1) Cut locus and Voronoi erosion.** Let \(V\) denote the Dirichlet–Voronoi cell of \(0\) for \(\Lambda\). Almost every quotient point has a unique representative in \(V\), uniformly distributed there. The lift of \(C(o)\) is the union of the boundaries of all Voronoi translates. For a representative in the interior of \(V\), the nearest point on this union lies on \(\partial V\): any path leaving \(V\) meets \(\partial V\) first. Thus \(D\) has the law of the Euclidean distance from an area-uniform point of \(V\) to \(\partial V\). Consequently, with \(V_r=\{x\in V:\operatorname{dist}(x,\partial V)\ge r\}\),
\[
 \Pr(D\ge r)={\operatorname{area}(V_r)\over A}.
\]

**(2) Exactly six candidate facet half-planes.** The Gauss-reduced basis has obtuse superbase \(u,v-u,-v\): all three pairwise scalar products are nonpositive because \(p\le a/2\) and \(b\ge a\). The standard two-dimensional Voronoi first-kind criterion, or an elementary reduction by lattice-coordinate sectors, shows all relevant normals are among \(\pm u,\pm v,\pm(v-u)\). The halfspaces are
\[
 V=\{x:\ |x\cdot u|\le a^2/2,\ |x\cdot v|\le b^2/2,\ |x\cdot(v-u)|\le c^2/2\}.
\]
The corresponding eroded cell has the same inequalities with each supporting distance reduced by \(r\), hence after writing \(x=(X,Y)\),
\[
 |X|\le\alpha=a/2-r,\quad |pX+qY|\le B=b(b/2-r),\quad |(p-a)X+qY|\le C=c(c/2-r).
\]
The geometric inradius is \(a/2\): the original incenter is \(0\), the closest facets are distance \(a/2\), and no larger inscribed disk exists since the pair of \(u\)-normal opposing facets are separated by \(a\).

**(3) Cross-section integral.** For \(0\le X\le\alpha\), the admissible vertical-section length is
\[
 \ell_r(X)=\frac1q\min\{2B,\ B+C-aX\}.
\]
The competing constraints and their reflected copies yield the above minimum (the remaining candidates are redundant on this half of the centrally symmetric cell). Its switch is at \(X_0=(C-B)/a\); reduced-basis inequalities ensure \(0\le X_0\), and the sections remain nonempty up to \(\alpha\). Reflecting over \(X=0\) gives
\[
 \operatorname{area}(V_r)=2\int_0^{\alpha}\ell_r(X)\,dX.
\]
If \(\alpha\le X_0\), it equals \(4\alpha B/q\); otherwise direct integration gives
\[
 \frac2q\left[(B+C)\alpha-\frac a2\alpha^2-\frac{(C-B)^2}{2a}\right].
\]
Moreover \(a\alpha-(C-B)=ap-sr=s(t_*-r)\), so the latter is exactly \(4\alpha B/q-s^2(t_*-r)^2/(aq)\). Divide by \(A=aq\) to obtain the displayed law. Because \(0\le p\le a/2\) and \(c\ge b\), one has \(0\le t_*\le a/2\). Differentiating the square-defect representation yields the claimed unique interior second-derivative jump.

**(4) Exact endpoint classification.** If \(p<a/2\), then sufficiently near the terminal radius \(r=a/2\) the square defect vanishes, and the eroded area is \(4b\delta[(b-a)/2+\delta]/q\). This is linear when \(b>a\) and quadratic when \(b=a\). If \(p=a/2\), then \(c=b\) and \(t_*=a/2\); subtracting the active square defect changes only the quadratic term and hence retains the linear law when \(b>a\). When \(a=b\), the allowed equilateral boundary \(p=a/2\) gives area \(4A\delta^2/a^2=2\sqrt3\delta^2\). Gauss reduction ensures that \(b=a\) exactly characterizes the presence of two independent shortest vectors.

**(5) Sharp distributional comparison, including equality.** The erosion \(V_r\) is a convex polygon with at most six sides (possibly fewer, or empty). Write \(g(r)=\operatorname{area}(V_r)\), \(P_r=\operatorname{perimeter}(V_r)\). Polygonal area evolution gives \(g'(r)=-P_r\) wherever the combinatorial type is stable; the identity extends almost everywhere. The sharp perimeter–area inequality for polygons with at most six sides gives
\[
 P_r^2\ge 4\cdot6\tan(\pi/6)\,g(r)=8\sqrt3\,g(r),
\]
with equality at positive area only for a regular hexagon. Hence \(\frac{d}{dr}\sqrt{g(r)}\le-\sqrt{2\sqrt3}\) whenever \(g(r)>0\). Integrating from \(g(0)=A\) gives
\[
 g(r)\le \bigl(\max\{\sqrt A-r\sqrt{2\sqrt3},0\}\bigr)^2.
\]
For the regular hexagonal Voronoi cell every erosion is a concentric similar regular hexagon, so equality holds throughout. If \(V\) is nonregular, the strict polygonal isoperimetric inequality applies on an initial nonempty interval, making the integrated inequality strict at every subsequent \(r\) strictly below the regular-hex terminal radius. A regular hexagonal lattice Voronoi cell is equivalent to an equilateral lattice up to similarity. Tail integration then gives the strict comparison for all positive power moments.

## Verification

A standalone NumPy checker in `check_cut_clearance.py` computes the stated formula, independently clips the six shifted halfplanes and measures their polygon area, performs direct uniform-torus sampling using nearest-lattice reduction, and checks the area-normalized hexagonal upper bound. In its recorded execution it verified \(158\) lattice parameter configurations at \(29\) offsets each, with maximum normalized clipping discrepancy below \(7\times10^{-15}\), and tested six configurations by Monte Carlo. Output: `PLANAR_TORUS_CUT_CLEARANCE_OK 158 29 6 max_clip_error 6.994e-15 max_dominance_defect 2.220e-16`. The computations are finite corroboration and are not a substitute for the proof.

## Relationship to prior work

Koçak and Ratiu (public preprint 2010) prove the general piecewise-polynomial inner-tube property for Euclidean polytopes and analyze polygonal erosion and smoothness; none of those general principles is claimed new here. McKilliam and Grant (public preprint 2012) analyze Voronoi first-kind lattice cells and their relevant vectors, supplying a known facet-reduction principle. Chitsakul (2013) describes the flat-torus cut-locus geometry using bisectors, rather than the distribution of distances to it. The present result combines their settings into a complete Gauss-parametrized probability law, classifies the endpoint exponent and interior transition, and identifies the strict fixed-covolume stochastic optimum. Standard sharp polygonal isoperimetry is acknowledged as the central extremal input.

## Limitations

The theorem concerns dimension two, ordinary Euclidean flat metrics, Haar-area point sampling, and distance from one point to another point's cut locus. It does not address curved tori, higher-dimensional lattices, nonuniform measures, or distances between two random points. Historical priority is provisional because no literature search guarantees exhaustive coverage, and a general erosion/isoperimetric result might already imply the stochastic optimum as a corollary. The numerical checker uses floating-point computations with finite samples; analytic claims do not depend on their numerical accuracy. Independent audit has not been performed.

## References

1. Şahin Koçak and Andrei V. Ratiu, *Inner tube formulas for polytopes*, arXiv:1008.2040v1, first submitted 2010-08-12, https://arxiv.org/abs/1008.2040v1 .
2. Robert McKilliam and Alex Grant, *Finding short vectors in a lattice of Voronoi's first kind*, arXiv:1201.5154v1, first submitted 2012-01-24, https://arxiv.org/abs/1201.5154v1 .
3. Pakkinee Chitsakul, *Some Properties of Cut Locus of a Flat Torus*, International Journal of Mathematical and Computational Sciences 7(12) (2013), https://publications.waset.org/9996880.pdf .
4. Classical polygonal isoperimetric inequality: a Euclidean polygon of at most \(m\) sides and area \(g\) has perimeter at least \(2\sqrt{m\tan(\pi/m)g}\), with equality only for the regular \(m\)-gon.
