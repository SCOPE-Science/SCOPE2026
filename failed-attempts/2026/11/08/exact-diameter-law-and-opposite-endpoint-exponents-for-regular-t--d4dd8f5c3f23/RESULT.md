# Exact diameter law and opposite endpoint exponents for regular-tetrahedron planar shadows

## Finding

Let \(T\subset\mathbb R^3\) be the regular tetrahedron with vertices
\[
 (1,1,1)/\sqrt3,\quad(1,-1,-1)/\sqrt3,\quad
 (-1,1,-1)/\sqrt3,\quad(-1,-1,1)/\sqrt3.
\]
For a uniform random unoriented plane \(U^\perp\), with \(U\) uniformly distributed on the unit sphere, let \(D\) be the **Euclidean diameter** of the orthogonal projection \(\Pi_{U^\perp}T\). This is the maximum pairwise projected-vertex distance, not a planar width in a separately sampled direction, not the original tetrahedron diameter, and not the enclosing-circle radius.

Write \(a\ge b\ge c\ge0\) for the ordered absolute coordinates of \(U\), and put
\[
 Y=\min\{a-b,b-c\},\qquad t_*=\frac1{\sqrt5}.
\]
Then the deterministic identity
\[
 \boxed{D^2=\frac83-\frac43Y^2}
\]
holds for every plane. In particular \(Y\in[0,t_*]\), and the sharp support of \(D\) is
\[
 \boxed{d_-:=\sqrt{\frac{12}{5}}\ \le D\le\ d_+:=\sqrt{\frac83}}.
\]
The lower endpoint occurs only for the unoriented normals obtained by signed coordinate permutations of \((2,1,0)/\sqrt5\) (twelve planes); the upper endpoint occurs exactly when at least two absolute normal coordinates coincide.

There is a complete, elementary **one-dimensional quadrature for the CDF**. For \(0<t<t_*\), set
\[
 \begin{split}
 L(t)&=\frac{t}{\sqrt{1-t^2}},\\
 H(t)&=\frac{1-t\sqrt{2-t^2}}{1-t^2},\\
 C(t)&=1-\frac{3t}{\sqrt{3(1-2t^2)}+3t},\\
 Z_2(y,t)&=\frac{y-t\sqrt{(2-t^2)y^2+1-t^2}}{1-t^2},\\
 Z_1(y,t)&=\sqrt{\frac{(1-y)^2}{t^2}-1-y^2},\\
 J(y,z)&=\frac{z}{(1+y^2)\sqrt{1+y^2+z^2}}.
 \end{split}
\]
Both square roots in these expressions are evaluated only on the corresponding indicated integration intervals, where they are real. Define
\[
 \boxed{S(t)=\frac{12}{\pi}
 \left[\int_{L(t)}^{C(t)}J(y,Z_2(y,t))\,dy
 +\int_{C(t)}^{H(t)}J(y,Z_1(y,t))\,dy\right].}
\]
Then \(S(t)=\Pr(Y\ge t)\), with continuous endpoint values \(S(0)=1\) and \(S(t_*)=0\). Thus
\[
 \boxed{\Pr(D\le r)=S\left(\sqrt{2-\frac{3r^2}{4}}\right),
 \qquad d_-\le r\le d_+,}
\]
with CDF \(0\) below \(d_-\) and \(1\) above \(d_+\).

The two endpoint laws are sharp and have **different exponents**:
\[
 \boxed{\Pr(D\le d_-+\varepsilon)
 \sim\frac{225\sqrt5}{4\pi}\,\varepsilon^2,}
 \qquad
 \boxed{\Pr(D>d_+-\varepsilon)
 \sim 3\sqrt2\,6^{1/4}\sqrt\varepsilon}
 \quad(\varepsilon\downarrow0).
\]
In the auxiliary gap variable these are equivalent to
\[
 \Pr(Y\ge t_*-\delta)\sim\frac{25\sqrt5}{3\pi}\delta^2,
 \qquad
 \Pr(Y<t)\sim3\sqrt2\,t.
\]
All normalization constants above are for the vertex normalization explicitly stated at the start. Rescaling tetrahedron edge length rescales the diameter and both endpoint constants in the evident way.

## Assumptions and scope

The plane is selected according to Haar probability on the Grassmannian of unoriented two-planes in \(\mathbb R^3\), equivalently via a spherical-uniform unit normal \(U\). The tetrahedron is a solid convex hull, but its projected diameter is attained by a pair of projected vertices. All probabilities refer to this single random plane, without an additional independent direction chosen inside it. Ties among normal-coordinate magnitudes are allowed in the deterministic identity; they are null events for the distribution. Asymptotics are one-sided as \(\varepsilon\) or \(\delta\) tends to zero through positive values. The CDF quadrature is valid throughout the open support and not merely asymptotically.

The regular tetrahedron has edge length \(\sqrt{8/3}\). For an edge-one tetrahedron, replace \(D\) everywhere by \(\sqrt{8/3}\) times the edge-one diameter.

## Proof

**1. Reduction to two adjacent coordinate gaps.** The six edge vectors of \(T\), up to sign, are
\[
 \frac2{\sqrt3}(0,1,1),\quad\frac2{\sqrt3}(0,1,-1),
 \quad\frac2{\sqrt3}(1,0,1),\quad\frac2{\sqrt3}(1,0,-1),
 \quad\frac2{\sqrt3}(1,1,0),\quad\frac2{\sqrt3}(1,-1,0).
\]
Projection onto \(U^\perp\) changes the squared length of an edge \(e\) to \(\|e\|^2-(e\cdot U)^2\). Every edge has squared length \(8/3\); hence the **largest** projected edge corresponds to the **smallest** of the six squared dot products. Sorting the absolute normal coordinates gives
\[
 \min\{|U_1\pm U_2|,|U_1\pm U_3|,|U_2\pm U_3|\}
 =\min\{a-b,b-c\}.
\]
The last equality follows because, for \(a\ge b\ge c\ge0\), each sum dominates its corresponding nonnegative difference and \(a-c=(a-b)+(b-c)\). This proves the asserted squared-diameter formula; it is a pointwise identity, not a sampling approximation.

Set \(g=a-b\ge0\), \(h=b-c\ge0\), so that \((a,b,c)=(c+h+g,c+h,c)\). The unit-sphere constraint implies
\[
 1=(c+h+g)^2+(c+h)^2+c^2\ge(g+h)^2+h^2.
\]
If \(\min(g,h)\ge t\), the right-hand side is at least \(5t^2\), with equality only at \(g=h=t\), \(c=0\). Consequently \(Y\le1/\sqrt5\) with exactly the displayed extremizers. In the other direction, \(Y=0\) precisely on the two Weyl-chamber walls \(a=b\) and \(b=c\). The diameter endpoints follow.

**2. Exact distribution.** Each of the \(48\) signed coordinate-order chambers has equal spherical area. Within the chamber \(a\ge b\ge c\ge0\), write
\[
 (a,b,c)=\frac{(1,y,z)}{\sqrt{1+y^2+z^2}},\qquad 0\le z\le y\le1.
\]
The exact spherical area element in these projective coordinates is
\[
 d\sigma=\frac{dy\,dz}{(1+y^2+z^2)^{3/2}}.
\]
The event \(Y\ge t\) requires **both**
\[
 1-y\ge t\sqrt{1+y^2+z^2},\qquad
 y-z\ge t\sqrt{1+y^2+z^2}.
\]
For a fixed \(y\), increasing \(z\ge0\) can only make these inequalities harder. Feasibility at \(z=0\) gives precisely \(L(t)\le y\le H(t)\). On this interval the first condition is equivalent to \(0\le z\le Z_1(y,t)\) and the second to \(0\le z\le Z_2(y,t)\). Their bounds cross once, when \(z=2y-1\) and \((1-y)^2=t^2(1+y^2+(2y-1)^2)\). Setting \(k=1-y\) and rationalizing the positive quadratic root yields the unique crossing \(y=C(t)\), with
\[
 L(t)<C(t)<H(t).
\]
The active upper bound is \(Z_2\) on \([L,C]\), and \(Z_1\) on \([C,H]\). Integrating over \(z\) uses the explicit antiderivative
\[
 \int_0^Z\frac{dz}{(1+y^2+z^2)^{3/2}}
 =\frac{Z}{(1+y^2)\sqrt{1+y^2+Z^2}}=J(y,Z).
\]
Multiplication by the chamber weight \(48/(4\pi)=12/\pi\) proves the complete formula for \(S(t)\) and the diameter CDF.

**3. Upper-diameter endpoint.** The two disjoint (up to endpoints) boundary arcs where \(Y=0\) inside the ordered positive chamber are \(a=b\) and \(b=c\). Their spherical lengths are, respectively,
\[
 \arctan\frac1{\sqrt2}\quad\text{and}\quad\arctan\sqrt2,
\]
whose sum is \(\pi/2\). At each interior point of either arc, the relevant gap is a linear functional of ambient norm \(\sqrt2\), so its spherical gradient has norm \(\sqrt2\). The inward spherical strip \(0\le Y<t\) therefore has leading chamber area
\[
 \frac{\pi}{2}\cdot\frac{t}{\sqrt2}+o(t).
\]
Overlaps and the finitely many arc endpoints contribute only \(O(t^2)\) to this chamber area. Multiplying by \(12/\pi\) gives \(\Pr(Y<t)=3\sqrt2\,t+o(t)\). Since
\[
 d_+-D=\frac{4Y^2/3}{d_++D}=\frac{Y^2}{\sqrt6}+O(Y^4),
\]
we obtain \(Y=6^{1/4}\sqrt{d_+-D}\,(1+o(1))\), yielding the stated upper-diameter tail.

**4. Lower-diameter endpoint.** Only a vanishing neighborhood of \((a,b,c)=(2,1,0)/\sqrt5\) in each chamber contributes to \(\{Y\ge t_*-\delta\}\). Use local coordinates \(g=a-b\), \(h=b-c\), and solve the smooth sphere equation for \(c\). At the extremizer the derivatives are
\[
 \frac{\partial c}{\partial g}=-\frac23,
 \qquad\frac{\partial c}{\partial h}=-1.
\]
The tangent derivatives of the sphere embedding \((g,h)\mapsto(c+h+g,c+h,c)\) are
\[
 (1,-2,-2)/3\quad\text{and}\quad(0,0,-1),
\]
so its area Jacobian is \(\sqrt5/3\). Set \(g=t_*-\delta+G\), \(h=t_*-\delta+H\), with \(G,H\ge0\). The constraint \(c\ge0\), by the implicit-function expansion, becomes
\[
 2G+3H\le5\delta+O(\delta^2)
\]
uniformly over the feasible neighborhood; the two other constraints enforce \(G,H\ge0\). The inequality \(1\ge(g+h)^2+h^2\), together with \(g,h\ge t_*-\delta\), first forces \(G,H=O(\delta)\); the sphere equation then forces \(c=O(\delta)\). Thus the Taylor remainder above is uniform on the full feasible set, not merely along individual perturbation paths. The limiting triangular region in the \((G,H)\)-plane has area
\[
 \frac12\left(\frac{5\delta}{2}\right)
 \left(\frac{5\delta}{3}\right)=\frac{25}{12}\delta^2.
\]
Therefore the normalized probability is
\[
 \Pr(Y\ge t_*-\delta)
 =\frac{12}{\pi}\cdot\frac{\sqrt5}{3}\cdot\frac{25}{12}\delta^2+o(\delta^2)
 =\frac{25\sqrt5}{3\pi}\delta^2+o(\delta^2).
\]
Finally \(D'(Y)=-4Y/(3D)\), so \(D'(t_*)=-2/(3\sqrt3)\). Hence
\[
 t_*-Y=\frac{3\sqrt3}{2}(D-d_-)+o(D-d_-),
\]
and substitution gives the constant \(225\sqrt5/(4\pi)\). These arguments establish both asymptotics as mathematical limits, not extrapolations from numerical integration.

## Verification

The standalone `check.py` directly enumerates all six projected tetrahedron edges, independently computes the sorted-coordinate formula, and verifies their agreement on \(90{,}000\) random normals. It compares numerical spherical quadrature with \(900{,}000\) independent uniform normals across seven interior thresholds, checks both endpoint coefficients at decreasing scales, and verifies that the resulting CDF has the claimed support. Reproduce with `python check.py` in an environment containing NumPy and SciPy. Successful output is `TETRAHEDRAL_SHADOW_DIAMETER_OK 900000 90000 3 3`.

Computations provide reproducibility checks, not proof of the full continuum of normals or independent validation. The exact formulas and limiting constants are proved analytically above.

## Relationship to prior work

Finch's *Planar Projections and Second Intrinsic Volume* (arXiv:1203.2464, originally made public March 12, 2012) analyzes the area, perimeter, and triangle-versus-quadrilateral counts of random tetrahedral shadows. Its relevant sections introduce precisely the Haar projection model, but do not give the diameter distribution or either endpoint coefficient.

Böröczky and Henk's *Random Projections of Regular Polytopes* (1997 preprint; later published in 2000) treats expected face counts and spherical angles of projected regular polytopes, not the pairwise distance maximum of a fixed three-dimensional tetrahedron.

The **directional width of a tetrahedron** (projection onto a random line), the **diameter of a random central section** of a different polytope, and the **radius of a random cube shadow** are different measurements and have different distributions. Geometrically, the diameter here also equals the centered circumradius of the projected difference body \(T-T\), which is a scaled cuboctahedron; searches for this dual formulation were included. None of the closest inspected records supplied the present gap law, exact quadrature, or its two endpoint constants. This comparison supports originality only to the extent of the accessible literature, and is not a guarantee of historical uniqueness.

## Limitations

The theorem is specific to a three-dimensional regular tetrahedron and orthogonal planar projection with Haar distribution. It makes no claims for distorted tetrahedra, perspective imaging, planar **section** diameters, or other projection dimensions. The integral expression is an exact one-dimensional quadrature, not asserted to be a simpler elementary closed form. The asymptotic remainders are little-\(o\), not uniform bounds at arbitrary finite thresholds. A broader previously published result might still imply the formula through the cuboctahedron difference-body reduction; independent priority checks and mathematical validation have not been performed.

## References

1. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464 (first public version 2012-03-12), https://arxiv.org/abs/1203.2464 . Relevant material: abstract, §1 and §2.1, pp. 1–4.
2. Károly Böröczky Jr. and Martin Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), subsequently *Archiv der Mathematik* (2000), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf . Relevant material: abstract, introduction, Theorem 1.1, and §2.
3. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (2026), https://arxiv.org/abs/2609.26202 . Abstract-level comparison only: a line-width law is not the orthogonal planar-shadow diameter law established here.
