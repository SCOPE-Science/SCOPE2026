# A three-atom area law and two critical exponents for randomly translated lattice-disk hulls

## Finding

Let \(U\) be uniform on \([0,1)^2\), let \(0<R<1\), and define the random integer convex hull
\[
H_R=\operatorname{conv}\{z\in\mathbb Z^2:\|z-U\|_2\le R\}.
\]
Take its planar area \(A_R\) to be zero when it has fewer than three noncollinear points, including when the intersection is empty. Put \(R_*=1/\sqrt2\). For \(R\le R_*\), \(A_R=0\) almost surely. For \(R_*<R<1\), define
\[
L_R=2R^2\arccos\!\left(\frac1{\sqrt2R}\right)
     -\sqrt2\sqrt{R^2-\tfrac12},
\qquad
Q_R=R^2\!\left(\pi-4\arcsin\!\frac1{2R}\right)
     -2\sqrt{R^2-\tfrac14}+1.
\]
Then the **entire law** of the random area is supported on precisely three values:
\[
\boxed{\begin{aligned}
\Pr(A_R=0)&=1-2L_R+Q_R,\\
\Pr(A_R=\tfrac12)&=2(L_R-Q_R),\\
\Pr(A_R=1)&=Q_R.
\end{aligned}}
\]
In particular,
\[
\boxed{\mathbb E A_R=L_R,\qquad
\operatorname{Var}(A_R)=\tfrac12(L_R+Q_R)-L_R^2.}
\]
The joint law of area and **boundary length of the two-dimensional hull** is also determined: an area-zero hull is assigned boundary length zero, an area-\(\tfrac12\) hull has boundary length \(2+\sqrt2\), and an area-one hull has boundary length \(4\). Consequently the mean two-dimensional boundary length is
\[
\mathbb E\mathcal P_R=(4+2\sqrt2)L_R-2\sqrt2 Q_R.
\]

The first positive-area phase begins at the exact radius \(R_*\). With \(\delta=R^2-\tfrac12\downarrow0\),
\[
\boxed{\begin{aligned}
L_R&=\tfrac{4\sqrt2}{3}\delta^{3/2}+O(\delta^{5/2}),\\
Q_R&=2\delta^2+O(\delta^3),\\
\Pr(A_R>0)&=\tfrac{8\sqrt2}{3}\delta^{3/2}-2\delta^2
                 +O(\delta^{5/2}),\\
\Pr(A_R=1\mid A_R>0)&=\tfrac3{4\sqrt2}\delta^{1/2}+O(\delta).
\end{aligned}}
\]
Thus planar hulls first appear at exponent \(3/2\), while the four-point square configuration appears at exponent \(2\). The formulas are exact throughout the entire first nontrivial radius chamber \(R_*<R<1\), rather than just asymptotic.

## Assumptions and scope

All lattice points inside or on the closed disk are included. Boundary conventions have no effect on the probability law because the random shift has a density. The lattice has Euclidean unit spacing; changing spacing scales both radius and area. A uniform rotation of the lattice does not change the distribution for a circular disk. The claim concerns the random planar **area of the lattice-point convex hull**, not the number of digitized pixels or area of their union. The empty hull is assigned area zero. All probability statements use the uniform shift on the unit lattice torus.

## Proof

**1. Only one fundamental square matters.** For a center \(U=(u,v)\in(0,1)^2\), any integer point outside \(\{0,1\}^2\) has at least one coordinate at distance greater than one from the corresponding coordinate of \(U\). It therefore cannot lie in the radius-\(R\) disk when \(R<1\). Thus all possible included lattice points are the four vertices of the unit square. A planar hull has area \(1/2\) for exactly three included corners and area one for all four; otherwise its area is zero.

**2. A diagonal pair forces a triangle.** Label the square corners \(c_{00},c_{10},c_{01},c_{11}\). Their squared distances from any \(U\) obey the exact parallelogram identity
\[
\|U-c_{00}\|_2^2+\|U-c_{11}\|_2^2
=\|U-c_{10}\|_2^2+\|U-c_{01}\|_2^2.
\]
If one diagonal pair lies inside the disk and neither corner of the other pair does, the left sum would be at most \(2R^2\) and the right sum strictly greater than \(2R^2\), a contradiction. Therefore each included diagonal pair accompanies at least a third corner. If \(I_1,I_2\) indicate inclusion of the two diagonal pairs, then for every shift away from boundary ties,
\[
A_R=\tfrac12(I_1+I_2).
\]
The event \(I_1=I_2=1\) is exactly the four-corner event. The two diagonal events have equal probabilities. Inclusion-exclusion now gives the three-atom law after those two geometric probabilities are computed.

**3. Diagonal lens probability.** The set of centers whose disk includes \(c_{00}\) and \(c_{11}\) is the intersection of two closed radius-\(R\) disks whose centers are separated by \(\sqrt2\). When \(R<1\), this lens lies entirely inside the unit square: a center outside the square has distance at least one to one of those corners. Hence its area, with unit-square normalization, is its probability. The standard two-circle sector-minus-triangle calculation gives
\[
\Pr(I_1=1)=\Pr(I_2=1)=
2R^2\arccos(1/(\sqrt2R))-\sqrt2\sqrt{R^2-1/2}=L_R.
\]
For \(R\le1/\sqrt2\), the disks have zero overlap area and hence both indicators vanish almost surely.

**4. Fourfold probability.** Write \(U=(\tfrac12+x,\tfrac12+y)\). The largest squared distance from \(U\) to a square corner is
\[
\tfrac12+x^2+y^2+|x|+|y|.
\]
Thus all four corners lie in the radius-\(R\) disk precisely when
\[
x^2+y^2+|x|+|y|\le\delta,
\qquad\delta=R^2-\tfrac12.
\]
Using reflection symmetry and setting \(b=\sqrt{R^2-\tfrac14}-\tfrac12\), the area of this fourfold region equals
\[
4\int_0^b\left(\sqrt{R^2-(x+\tfrac12)^2}-\tfrac12\right)\,dx
=R^2\left(\pi-4\arcsin\frac1{2R}\right)-2\sqrt{R^2-\tfrac14}+1=Q_R.
\]
This is the exact square-hull probability, and the first three displayed laws follow from \(\Pr(I_1=I_2=1)=Q_R\) and \(\mathbb EA_R=L_R\). Since \(A_R^2=(I_1+I_2+2I_1I_2)/4\), its second moment is \((L_R+Q_R)/2\), proving the variance formula.

**5. Threshold exponents.** In coordinates \(w=x+y\), \(z=x-y\), one diagonal lens near onset is
\[
|w|+\tfrac12(w^2+z^2)\le\delta,
\]
with Jacobian \(1/2\) between the two coordinate systems. Integrating first in \(z\), and using \(w=O(\delta)\), proves
\[
L_R=2\int_0^{\sqrt{1+2\delta}-1}
      \sqrt{2\delta-2w-w^2}\,dw
=\tfrac{4\sqrt2}{3}\delta^{3/2}+O(\delta^{5/2}).
\]
The fourfold region is \(x^2+y^2+|x|+|y|\le\delta\). Rescale \((x,y)=\delta(s,t)\): its area is \(\delta^2\) times the area of \(|s|+|t|+\delta(s^2+t^2)\le1\). This is a perturbation of the area-two \(\ell_1\)-unit diamond by \(O(\delta)\), giving \(Q_R=2\delta^2+O(\delta^3)\). Substitution gives the last two expansions, including the conditional square probability.

## Verification

The bundled standard-library script `verify.py` checks the area of convex hulls computed from actual included corner sets on a grid of shifted disk centers, compares frequencies to the closed probability formulas, and independently evaluates the diagonal lens and fourfold intersection areas by numerical slicing and quadrature. It also checks finite-radius onset approximations and seeded Monte Carlo frequencies. The script completed with the marker `DISPLACED_DISK_HULL_AREA_LAW_CHECKS_PASSED` when run as `python verify.py`. These finite checks corroborate, but do not replace, the exact geometric proof above.

## Relationship to prior work

The natural background is the randomized integer convex-hull model introduced by Bárány and Matoušek, which studies expected vertex count and missed area for sufficiently large convex bodies. Ngoc and Reitzner subsequently investigated mean width in the same random-lattice model, again with large-dilation bounds. Those bounds do not give the present exact finite-radius hull-area distribution. Baudrier and Mazo and Huxley and Žunić study configurations arising from translated digitization; their stated results primarily concern counting distinct digitizations and their asymptotics, rather than the measure of shifts realizing a given hull area. An exactly equivalent short-radius law in earlier digital-geometry work cannot be excluded without exhaustive historical inspection.

## Limitations

The explicit three-atom law is restricted to circular disks of radius strictly less than one lattice unit in the square lattice. At radius one and beyond, additional lattice points can enter on positive-measure shift sets and the three-atom description no longer applies. Rotations of the disk are immaterial because the disk is rotationally symmetric. The result does not provide laws for general convex bodies, arbitrary lattices, higher dimensions, or other digitization conventions. The edge cases \(R=1/\sqrt2\) and boundary points are understood almost surely. The argument uses an exact square-lattice model; further related results may exist under other digitization terminology.

## References

1. I. Bárány and J. Matoušek, *The Randomized Integer Convex Hull*, Discrete & Computational Geometry 33 (2005), 3–25. DOI 10.1007/s00454-003-0836-1. Freely accessible author PDF: https://www.renyi.hu/~barany/cikkek/95.pdf.
2. B. H. Ngoc and M. Reitzner, *Expected mean width of the randomized integer convex hull*, first public arXiv version 2003.06864 (15 March 2020); Mathematika 67 (2021), 422–433. DOI 10.1112/mtk.12080. https://arxiv.org/abs/2003.06864.
3. É. Baudrier and L. Mazo, *Combinatorics of the Gauss Digitization Under Translation in 2D*, Journal of Mathematical Imaging and Vision 61 (2019), 224–236. DOI 10.1007/s10851-018-0846-5.
4. M. N. Huxley and J. Žunić, *Different Digitisations of Displaced Discs*, Foundations of Computational Mathematics 6 (2006), 255–268. DOI 10.1007/s10208-005-0177-y. Only the abstract was available in the present literature comparison.
5. E. Roldán-Pensado, *The Probability that a Convex Body Intersects the Integer Lattice in a k-dimensional Set*, Discrete & Computational Geometry 47 (2012), 288–300. DOI 10.1007/s00454-011-9389-x. A related author's thesis chapter was consulted.
