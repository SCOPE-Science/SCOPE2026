# A two-inball symmetry breaking theorem for ideal hyperbolic quadrilaterals

## Finding

Let \(Q\) be a geodesically convex ideal quadrilateral of the complete hyperbolic plane of curvature \(-1\). Its inradius is the supremum of radii of closed hyperbolic metric disks contained in \(Q\). Every such quadrilateral admits a Klein-model representative with ideal vertices \((\pm c,\pm s)\), with \(c^2+s^2=1\) and \(1/\sqrt2\le c<1\), \(s=\sqrt{1-c^2}\). The sharp radius is
\[
 r(Q)=\operatorname{arsinh}\!\left(\frac{1}{\sqrt{4c^2-1}}\right).
\]
If \(c=s\) (the regular ideal quadrilateral), the unique maximal-disk center has Klein coordinates \((0,0)\), and the disk touches all four sides. For every \(c>s\), there are **exactly two** largest inscribed disks, with centers
\[
 \left(\pm\frac{c^2-s^2}{c},0\right).
\]
Each of these disks touches exactly three of the quadrilateral's four sides. As \(c\) increases from \(1/\sqrt2\) to \(1\), the inradius strictly decreases from \(\operatorname{arsinh}(1)\) toward \(\operatorname{arsinh}(1/\sqrt3)\). In particular the regular quadrilateral is uniquely maximal in this family, and its symmetry-breaking limit is sharp: every nonsquare ideal quadrilateral has two distinct maximal disks.

## Assumptions and scope

The complete curvature-\(-1\) hyperbolic plane is represented by the open unit Klein disk. An ideal quadrilateral has four distinct cyclically ordered ideal vertices; its interior is the intersection of the four geodesic half-planes. The inradius is the largest \(r\) for which some closed metric disk of radius \(r\) lies in that intersection. There are no finite vertices and no truncated sides. By the transitivity of hyperbolic isometries and their action on ideal endpoints, the intersection of the geodesic diagonals can be moved to the disk origin, making both diagonal pairs antipodal; the resulting Euclidean cyclic parallelogram is a rectangle. A rotation gives exactly the stated coordinate normalization, possibly interchanging \(c\) and \(s\).

## Proof

Write \(D=1-x^2-y^2\) and let \((x,y)\) lie in \((-c,c)\times(-s,s)\). The hyperboloid embedding is \((T,X,Y)=(1,x,y)/\sqrt D\), satisfying \(T^2-X^2-Y^2=1\). The supporting geodesic lines \(x=\pm c\) have normalized spacelike Minkowski normals \((c,\mp1,0)/s\); similarly \(y=\pm s\) have normals \((s,0,\mp1)/c\). Their point-to-geodesic distances therefore obey
\[
 \sinh d_{x=\pm c}=\frac{c\mp x}{s\sqrt D},\qquad
 \sinh d_{y=\pm s}=\frac{s\mp y}{c\sqrt D}.
\]
A disk centered at a point of this convex intersection remains inside it exactly up to the minimum distance from its center to the supporting geodesics. Hence maximizing the inradius is equivalent to maximizing
\[
 F(x,y)=\frac{1}{\sqrt{1-x^2-y^2}}
 \min\left\{\frac{c-|x|}{s},\frac{s-|y|}{c}\right\}.
\]
By reflection symmetry put \(u=|x|\in[0,c)\), \(v=|y|\in[0,s)\). Let \(A(u,v)=(c-u)/(s\sqrt{1-u^2-v^2})\) and \(B(u,v)=(s-v)/(c\sqrt{1-u^2-v^2})\). For each fixed \(u\), \(A\) is strictly increasing in \(v\) when \(u<c\) and \(B\) is strictly decreasing, since the numerator of its \(v\)-derivative after multiplying by its positive denominator is \(-1+u^2+sv<0\) (use \(1-u^2\ge s^2>sv\)).

Put \(u_*=(c^2-s^2)/c\). When \(0\le u\le u_*\), \(A(u,0)\ge B(u,0)\), so \(\min(A,B)\le B(u,v)\le B(u,0)=s/(c\sqrt{1-u^2})\). This last expression is strictly increasing for positive \(u\), reaching the prospective maximum only at \((u_*,0)\).

When \(u_*<u<c\), \(A(u,0)<B(u,0)\). Their unique intersection as functions of \(v\) is
\[
 v_*(u)=\frac{cu-(c^2-s^2)}s,\qquad 0<v_*(u)<s.
\]
Because \(A\) increases and \(B\) decreases, the maximum of their minimum at fixed \(u\) occurs exactly at this intersection. Elementary substitution using \(c^2+s^2=1\) gives
\[
 F(u,v_*(u))^2=\frac{c-u}{u+3c-4c^3}.
\]
Its derivative in \(u\) is \(-4cs^2/(u+3c-4c^3)^2<0\). Thus the global maximum is attained only for \(u=u_*\), \(v=0\). Evaluating there gives
\[
 F(u_*,0)^2=\frac1{4c^2-1}.
\]
For \(c>s\) reflection symmetry produces exactly two centers; at \(c=s\) they coincide. At each off-center maximizer the two horizontal sides and the nearer vertical side attain the common minimum, while the farther vertical side has strictly larger distance. At the regular case all four attain it. The formula for \(r(Q)\), its strict monotonicity and both endpoint values follow immediately from the monotonicity of \(\operatorname{arsinh}\).

## Verification

The analytic proof above is global for every \(1/\sqrt2\le c<1\) and every interior point. The accompanying `CHECK.py` independently evaluates the four geodesic distances and compares the predicted radius and center location with numerical differential-evolution maximization at six configurations and 12,000 independent interior samples for each configuration. All diagnostics pass. This finite test is supplementary; the derivative argument, not numerical optimization, proves the global and unique assertions.

## Relationship to prior work

Izmestiev (2014) develops Cayley–Klein and cross-ratio methods for cyclic quadrilaterals and hyperbolic isometries, but the inspected paper's results address porisms, Möbius transformations and equal lengths rather than maximal inscribed disks. Classical incenter formulas for hyperbolic triangles and the later maximal-inradius treatment of hyperbolic simplices concern triangles, not the four-sided inball-center classification. This result supplies the complete sharp center count, explicit optimal locations and the symmetry-breaking threshold for all ideal hyperbolic quadrilaterals, as opposed to these broader modeling techniques or triangle-only facts. Historical priority remains provisional.

## Limitations

The result is about geodesic ideal quadrilaterals in curvature \(-1\); it does not classify finite-vertex, partially ideal, or higher-sided hyperbolic polygons. A closed radius-\(r\) disk is understood intrinsically, not as a Euclidean Klein-model disk. Only self-review has been performed; independent historical-priority and mathematical validation are not claimed.

## References

1. Ivan Izmestiev, *A porism for cyclic quadrilaterals, butterfly theorems, and hyperbolic geometry*, arXiv:1408.2247, first submitted 10 August 2014. https://arxiv.org/abs/1408.2247
2. Bruno Duchesne and Christopher-Lloyd Simon, *Hyperbolic Simplices of Maximal Inradius*, arXiv:2512.17096, first submitted 18 December 2025. https://arxiv.org/abs/2512.17096
