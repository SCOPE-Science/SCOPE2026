# Exact John and Löwner ellipsoids of equal-ball lenses in every dimension

## Finding
For each integer \(n\ge2\) and \(0<c<1\), consider the intersection of two Euclidean unit balls with centers separated by \(2c\):
\[
L_{n,c}=\{(t,z)\in\mathbb R\times\mathbb R^{n-1}:(|t|+c)^2+\|z\|_2^2\le1\}.
\]
Define \(\delta\in(c^2,1)\) by
\[
n\delta(\delta-c^2)=c^2(1-\delta),\qquad
\delta=\frac{(n-1)c^2+\sqrt{(n-1)^2c^4+4nc^2}}{2n},
\]
and put \(b^2=1-\delta\) and \(a^2=(1-\delta)(\delta-c^2)/\delta\). The unique John ellipsoid is
\[
J_{n,c}=\left\{(t,z):\frac{t^2}{a^2}+\frac{\|z\|_2^2}{b^2}\le1\right\}.
\]
The unique Löwner ellipsoid is
\[
E_{n,c}=\left\{(t,z):\frac{t^2}{(1-c)^2}+\frac{\|z\|_2^2}{1-c^2}\le1\right\}.
\]
All common boundary points of the lens and its John ellipsoid satisfy \(t=\pm a/\sqrt n\) and \(\|z\|_2=b\sqrt{(n-1)/n}\). All common boundary points of the lens and its Löwner ellipsoid are either the axial tips \((\pm(1-c),0)\), or the equator \(t=0,\ \|z\|_2=\sqrt{1-c^2}\).

For fixed \(c\in(0,1)\), the dimension limit is
\[
\lim_{n\to\infty}\sqrt n\,a=\frac{1-c^2}{c},\qquad
\lim_{n\to\infty}b=\sqrt{1-c^2}.
\]
For fixed \(n\ge2\), the shrinking-lens limit is
\[
\lim_{c\uparrow1}\frac{a}{1-c}=\frac{2\sqrt n}{n+1},\qquad
\lim_{c\uparrow1}\frac{b}{\sqrt{1-c^2}}=\sqrt{\frac{n}{n+1}}.
\]
Thus even when the generating balls are fixed, the volume-maximizing inscribed ellipsoid becomes increasingly axially compressed as the dimension rises. At \(c=0\), the lens and both ellipsoids are the unit ball.

## Assumptions and scope
The ambient space is Euclidean \(\mathbb R^n\) with \(n\ge2\). The two generating closed balls have the same positive radius, normalized to one, and their center distance is strictly smaller than two. Scaling the entire construction by a radius \(R>0\) multiplies every semiaxis by \(R\) and replaces \(c\) by the center half-distance divided by \(R\). For \(c=1\), the intersection is a singleton, so full-dimensional John and Löwner ellipsoids are not defined.

The John ellipsoid means the unique maximum-\(n\)-volume ellipsoid contained in the lens, without any a priori symmetry restriction. The Löwner ellipsoid means the unique minimum-\(n\)-volume ellipsoid containing the lens, again among all affine ellipsoids.

## Proof
**1. Radius algebra.** For \(0<c<1\), the polynomial \(F(\delta)=n\delta(\delta-c^2)-c^2(1-\delta)\) has \(F(c^2)<0<F(1)\), and derivative \(n(2\delta-c^2)+c^2>0\) on \([c^2,1]\). Hence \(\delta\in(c^2,1)\) exists uniquely. The displayed positive quadratic root follows by expansion. The prescribed semiaxes are positive and satisfy
\[
b^2-a^2=\frac{(1-\delta)c^2}{\delta}>0,
\qquad
\frac{a c}{b^2-a^2}=\frac1{\sqrt n}.
\]
The second identity follows by squaring and using \(n\delta(\delta-c^2)=c^2(1-\delta)\), with all quantities positive.

**2. John feasibility and full contacts.** Write a point of the proposed ellipsoid as \((a s,b\sqrt{1-s^2}\,\xi)\) on its boundary, with \(-1\le s\le1\) and \(\|\xi\|_2=1\). By axial symmetry, membership in the lens reduces to
\[
q(|s|):=(c+a|s|)^2+b^2(1-s^2)\le1.
\]
For \(s\ge0\), this is a strictly concave quadratic, because \(a^2-b^2<0\). Its unique maximum is at \(s=ac/(b^2-a^2)=1/\sqrt n\). The maximum is
\[
q\left(\frac1{\sqrt n}\right)
=c^2+b^2+\frac{a^2c^2}{b^2-a^2}
=c^2+(1-\delta)+(\delta-c^2)=1.
\]
Therefore the entire ellipsoid lies in the lens, and its complete contact set comprises exactly the two latitudes listed above.

**3. John optimality among every affine ellipsoid.** Apply the linear map \((t,z)\mapsto(t/a,z/b)\), so the candidate ellipsoid becomes the unit ball. For each transverse coordinate vector \(e_j\) (\(j=1,\ldots,n-1\)), take the four normalized contact vectors
\[
u_{j,\varepsilon,\sigma}=
\left(\frac{\varepsilon}{\sqrt n},\;\sigma\sqrt{\frac{n-1}{n}}\,e_j\right),
\qquad\varepsilon,\sigma\in\{-1,1\}.
\]
With common positive weight \(n/[4(n-1)]\), these vectors satisfy
\[
\sum_{j,\varepsilon,\sigma}w u_{j,\varepsilon,\sigma}=0,
\qquad
\sum_{j,\varepsilon,\sigma}w u_{j,\varepsilon,\sigma}u_{j,\varepsilon,\sigma}^T=I_n.
\]
Indeed the first-coordinate variance is \(1/n\), and each of the other coordinate variances is also \(1/n\), with all cross terms cancelling by signs. The contact characterization of John's theorem implies that the displayed ellipsoid is the unique global maximum-volume inscribed ellipsoid; no symmetry assumption about a competing ellipsoid has been made.

**4. Löwner feasibility and full contacts.** At a boundary point of the lens, write \(|t|=(1-c)v\), \(0\le v\le1\). The largest permitted transverse norm is \(\|z\|_2^2=1-[c+(1-c)v]^2\). Therefore
\[
\frac{t^2}{(1-c)^2}+\frac{\|z\|_2^2}{1-c^2}
\le v^2+\frac{1-[c+(1-c)v]^2}{1-c^2}
=1-\frac{2c}{1+c}v(1-v)\le1.
\]
The inequality is strict for \(0<v<1\), and equality on the lens boundary occurs exactly at \(v=0\) (the full equator) or \(v=1\) (the two axial tips). Thus the proposed ellipsoid contains the lens and has precisely the claimed contacts.

**5. Löwner optimality.** Normalize this containing ellipsoid to the unit ball. Its contact set contains \(\pm e_i\) for all \(i=1,\ldots,n\). Assign weight \(1/2\) to each of these \(2n\) points. Their weighted vector sum is zero and the weighted sum of outer products is \(I_n\). The Löwner contact theorem gives uniqueness and global minimum enclosing volume, without a symmetry restriction on competitors.

**6. Boundary laws.** For fixed \(c>0\), the defining quadratic yields \(\delta=c^2+(1-c^2)/n+O_c(n^{-2})\). Substitution into the semiaxes gives \(a=(1-c^2)/(c\sqrt n)+O_c(n^{-3/2})\) and \(b\to\sqrt{1-c^2}\). For fixed \(n\), set \(\epsilon=1-c\). Solving the same quadratic to first order gives \(1-\delta=2n\epsilon/(n+1)+O_n(\epsilon^2)\) and \(\delta-c^2=2\epsilon/(n+1)+O_n(\epsilon^2)\). Consequently \(a=2\sqrt n\epsilon/(n+1)+O_n(\epsilon^2)\) and \(b=\sqrt{2n\epsilon/(n+1)}(1+O_n(\epsilon))\), which proves the two remaining limits.

## Verification
The self-contained Python file `check_lens_ellipsoids.py` computes the semiaxes from the explicit radical formula and checks feasibility and tangency on a dense but finite set of sample dimensions, separations, and boundary parameters. It checks the exact contact identities numerically and samples both containment inequalities. It uses no nonstandard Python dependencies. Execute with `python check_lens_ellipsoids.py` from the directory containing the extracted file. The proof above is analytic; these finite tests are supplementary and are not presented as certification of the universal quantifiers.

## Relationship to prior work
Drach and Tatarko establish that equal-ball lenses are the reverse-isoperimetric volume extremizers among \(\lambda\)-convex bodies of prescribed boundary area in every Euclidean dimension and constant-curvature model spaces. The present theorem does not re-prove that extremal inequality: it computes two classical affine approximation invariants of its Euclidean extremal objects and supplies exact contact sets and two distinct asymptotic regimes. John's 1948 contact characterization provides the optimality criterion used here. Kahan's ellipsoid-intersection results treat centrally located generating ellipsoids; their common-center hypotheses do not cover two equal balls with distinct centers. Separate literature studies lens mean width and enclosing or inscribed spheres; these quantities do not determine the ellipsoid semiaxes.

## Limitations
Only intersections of two congruent Euclidean balls with nonempty interior are treated. Unequal radii, more than two balls, constant-curvature analogues, and non-ellipsoidal approximation are not addressed. The proof gives no independent priority certification; an equivalent closed formula might exist in older optimization literature on intersections of quadrics. No claims are made about Banach–Mazur optimal affine comparison of the lens with a ball; the volume-extremal ellipsoids need not solve that different optimization problem.

## References
1. K. Drach and K. Tatarko, *A complete solution to the reverse isoperimetric problem for \(\lambda\)-convex bodies*, arXiv:2610.40291v1 (first public 2026-10-29), https://arxiv.org/abs/2610.40291 .
2. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant* (1948), pp. 187–204.
3. W. Kahan, *Circumscribing an Ellipsoid about the Intersection of Two Ellipsoids*, *Canadian Mathematical Bulletin* 11 (1968), pp. 437–441; accessible expanded exposition (2006), https://people.eecs.berkeley.edu/~wkahan/Ellipint.pdf .
4. W. M. Henk, *Löwner–John ellipsoids*, *Optimization Stories*, Documenta Mathematica extra volume (2012), pp. 95–106.
