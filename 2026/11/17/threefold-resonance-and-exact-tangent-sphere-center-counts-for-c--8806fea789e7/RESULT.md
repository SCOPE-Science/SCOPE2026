# Threefold resonance and exact tangent-sphere center counts for cyclic skew lines

## Finding
For every real \(a>0\), \(k>0\) and integer \(n\ge3\), consider the \(n\) lines
\[
\ell_j=\{(a u_j+tJu_j,kt):t\in\mathbb R\},\qquad
u_j=(\cos(2\pi j/n),\sin(2\pi j/n)),\quad
J(x,y)=(-y,x),\quad 0\le j<n.
\]
Their horizontal projections are tangents to the radius-\(a\) circle, with identical signed pitch. Set \(B=1+k^2\), and write \(E_n\) for the locus of points having the same Euclidean distance to every \(\ell_j\). Then:

1. For every \(n\ge4\), \(E_n\) is **exactly the vertical axis**.
2. For \(n=3\), \(E_3\) is the disjoint union of the vertical axis and three smooth unbounded curves. The latter have complete polar parametrizations
\[
(x,y,z)=\left(4aB\sec(3t)\cos(2\pi m/3+t),\ 4aB\sec(3t)\sin(2\pi m/3+t),\ \frac{aB}{k}\tan(3t)\right),
\quad -\frac{\pi}{6}<t<\frac{\pi}{6},\quad m=0,1,2.
\]
3. On the axis, the common squared distance is \(a^2+z^2/B\). On each nonaxial curve it is exactly
\[
\rho(t)^2=a^2\left[(4B-1)^2+\Gamma\tan^2(3t)\right],\quad
\Gamma=8B(2B-1)+\frac{B}{k^2}>0.
\]
Thus the common-distance function on \(E_3\) has precisely four strict nondegenerate local minima and no local maxima. One minimum has distance \(a\), at the origin; the other three, at \(z=0\) and horizontal radius \(4aB\), have the same distance \(a(4B-1)=a(3+4k^2)\).

In particular, for a prescribed positive sphere radius \(R\), the number of **distinct centers of spheres tangent to all three lines** is exactly
\[
N_3(R)=\begin{cases}
0,&R<a,\\
1,&R=a,\\
2,&a<R<a(3+4k^2),\\
5,&R=a(3+4k^2),\\
8,&R>a(3+4k^2).
\end{cases}
\]
For \(n\ge4\), the corresponding counts are \(0,1,2\) according as \(R<a\), \(R=a\), or \(R>a\). These counts include centers on both sides of the horizontal plane; sphere orientation is immaterial.

## Assumptions and scope
All lines are infinite and distinct, not segments or rays. Distances are ordinary Euclidean point-to-line distances in \(\mathbb R^3\); a sphere is tangent to a line precisely when the distance of its center to that line equals its positive radius. The parameter \(k\) is strictly positive, excluding the planar degeneration. The lines are pairwise skew: equality of heights forces equal line parameters, and their horizontal separation would require \((I+sJ)(u_i-u_j)=0\), impossible since \(\det(I+sJ)=1+s^2>0\). Any three distinct direction vectors are linearly independent, because their horizontal components lie at three distinct points of a circle and all have the same nonzero vertical component. No generic-position premise is needed beyond these stated assumptions.

## Proof
Put \(\phi_j=2\pi j/n\), \(p=(r\cos\theta,r\sin\theta,z)\), and \(B=1+k^2\). Orthogonal projection onto the line direction \((Ju_j,k)\) gives
\[
D_j(p)=d(p,\ell_j)^2=a^2+r^2+z^2-2ar\cos(\theta-\phi_j)
-\frac{\bigl(r\sin(\theta-\phi_j)+kz\bigr)^2}{B}.
\]
Writing \(v_j=\theta-\phi_j\), expand as
\[
D_j=a^2+\frac{2B-1}{2B}r^2+\frac{z^2}{B}
-2ar\cos v_j-\frac{2krz}{B}\sin v_j
+\frac{r^2}{2B}\cos(2v_j).
\tag{1}
\]
The zero Fourier mode is independent of \(j\). For every \(n\ge4\), the sampled first harmonics \(\cos v_j,\sin v_j\) are orthogonal to the sampled second harmonic \(\cos(2v_j)\). If all \(D_j\) are equal, their first-harmonic coefficient must vanish. In particular its component \(-2ar\) vanishes, and \(a>0\) gives \(r=0\). Conversely every point with \(r=0\) is equidistant to all lines, proving (1) of the finding. The argument also works for \(n=4\), where positive and negative second harmonics alias each other but neither aliases the first.

For \(n=3\), \(3\phi_j\) is a multiple of \(2\pi\), so
\[
\cos(2v_j)=\cos(3\theta)\cos v_j+\sin(3\theta)\sin v_j.
\]
The two sampled first harmonics are independent. Apart from \(r=0\), equality in (1) is therefore equivalent to
\[
-2ar+\frac{r^2}{2B}\cos(3\theta)=0,\qquad
-\frac{2krz}{B}+\frac{r^2}{2B}\sin(3\theta)=0.
\]
Dividing by \(r>0\) gives exactly
\[
r\cos(3\theta)=4aB,\qquad z=\frac{r\sin(3\theta)}{4k}.
\]
Necessarily \(\cos(3\theta)>0\), so \(\theta\) lies in one of precisely three disjoint open angular sectors, \(\theta=2\pi m/3+t\) with \(|t|<\pi/6\). The displayed parametrizations follow and are bijections onto their respective curves. Each curve escapes to infinity at both angular endpoints; the three curves are disjoint and separated from the axis by \(r\ge4aB\), proving the component classification.

For \(n=3\), averaging (1) over all three line indices cancels both nonconstant sampled harmonics. At an equidistant point, each \(D_j\) equals this mean:
\[
\rho^2=a^2+\frac{2B-1}{2B}r^2+\frac{z^2}{B}.
\]
On the nonaxial branches substitute \(r=4aB\sec(3t)\) and \(z=aB\tan(3t)/k\); using \(\sec^2 w=1+\tan^2 w\) gives the asserted formula with positive \(\Gamma\). The derivative with respect to \(t\) is \(6a^2\Gamma\tan(3t)\sec^2(3t)\), which vanishes only at \(t=0\); the second derivative there is \(18a^2\Gamma>0\). There can be no other stationary point or local maximum. On the axis, \(a^2+z^2/B\) has its unique strict minimum at \(z=0\), also nondegenerate.

Finally, for a fixed radius \(R\), the axis contributes zero, one, or two centers as \(R<a\), \(R=a\), or \(R>a\). Each nonaxial branch contributes zero centers when \(R<a(4B-1)\), one at equality, and two when the inequality is reversed, since \(\tan(3t)\) ranges strictly monotonically from minus infinity to plus infinity. Summing yields the complete exact center-count law and its higher-\(n\) counterpart. This is exhaustive, not a finite search.

## Verification
The companion standalone Python file `check.py` performs 2,796 deterministic numerical checks of the exact polar parametrizations, common squared distances, axis normalization, and nonaxial exclusions for representative parameter values. It uses only the Python standard library. Execute `python check.py` from the directory containing this file. The proof above, not numerical sampling, establishes the infinite-parameter claims. In addition, averaging (1) yields \(\max_j D_j(p)\ge a^2+(2B-1)r^2/(2B)+z^2/B\ge a^2\), with equality only at the origin, confirming independently that the smallest Euclidean ball intersecting all sites has radius \(a\) and a unique center.

## Relationship to prior work
Everett, Lazard, Lazard and Safey El Din (2007/2009) proved that the trisector for three pairwise skew lines on one hyperboloid of revolution decomposes into a cubic and a line, and that it has four real unbounded branches. Those facts are **not** claimed as new. Papadopoulou, Suderland and Wang (2026) established general bounds of four local maxima and eight local minima of the common-distance function along an arbitrary three-line trisector and a degree-twelve algebraic procedure for its critical points. The present theorem instead obtains an explicit complete distance spectrum, the exact 1/2/5/8 tangent-sphere count at every radius in a canonical cyclic symmetric family, and the exact three-versus-four-or-more site harmonic dichotomy. These quantitative conclusions do not follow merely from the cited branch count or upper bounds. Hemmer, Setter and Halperin (2010) give a general exact Voronoi implementation rather than this closed-form special-family spectrum.

## Limitations
The classification is for identical pitches and equally spaced tangency directions on one circle. It is not a classification of arbitrary skew-line configurations, and the three nonaxial curves should not be expected to persist in the same elementary form under perturbation. The result supplies no tightness claim for general three-line critical-point upper bounds. The original scientific priority remains subject to further literature assessment; the closest broad published treatments are cited explicitly.

## References
1. E. Papadopoulou, M. Suderland, Z. Wang, *A Collapse Process for Farthest Voronoi Diagrams of Lines in Three Dimensions*, arXiv:2609.29865, first public version 2026-09-24. https://arxiv.org/pdf/2609.29865
2. H. Everett, D. Lazard, S. Lazard, M. Safey El Din, *The Voronoi Diagram of Three Lines*, Discrete & Computational Geometry **42** (2009), 94–130; available author's manuscript https://perso.lip6.fr/Mohab.Safey/Articles/Voronoi.pdf
3. M. Hemmer, O. Setter, D. Halperin, *Constructing the Exact Voronoi Diagram of Arbitrary Lines in Space with Fast Point-Location*, 2010. https://www.cgl.cs.tau.ac.il/wp-content/uploads/2023/09/voronoi_lines.pdf
