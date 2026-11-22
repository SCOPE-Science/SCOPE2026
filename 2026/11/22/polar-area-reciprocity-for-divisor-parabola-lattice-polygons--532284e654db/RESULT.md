# Polar-area reciprocity for divisor-parabola lattice polygons

## Finding
For every integer \(h\ge 2\), let
\[
 B_h=\operatorname{conv}\left(\{(0,-1)\}\cup\{(a,a^2):a\in\mathbb Z\setminus\{0\},\ a\mid h\}\right)\subset\mathbb R^2,
\]
and use polarity with respect to the origin and the standard pairing, \(B_h^\circ=\{u:\langle u,x\rangle\le1\ \forall x\in B_h\}\). Write \(1=d_1<\cdots<d_k=h\) for the positive divisors and \(S_h=\sum_{i=1}^{k-1}(d_{i+1}-d_i)^3\). Then
\[
 \operatorname{area}(B_h^\circ)=\frac{8h^3+4+S_h}{3h^3},\qquad
 \boxed{\operatorname{area}(B_h^\circ)+\frac{\operatorname{area}(B_h)}{h^3}=4+\frac2{h^3}.}
\]
Consequently, the sharp extremal subsequential limits of the polar area are
\[
 \liminf_{h\to\infty}\operatorname{area}(B_h^\circ)=6-\frac{\pi^2}{3},\qquad
 \limsup_{h\to\infty}\operatorname{area}(B_h^\circ)=3.
\]
The polar-area accumulation spectrum has the **sharp, attainable-endpoint forbidden gap**
\[
 \operatorname{Acc}_{h\to\infty}\operatorname{area}(B_h^\circ)\cap\left(\frac{11}{4},4-\frac{\pi^2}{8}\right)=\varnothing.
\]
The left endpoint is attained by \(h=2p\) along odd primes \(p\to\infty\); the right endpoint is attained by \(h=\operatorname{lcm}(1,3,\ldots,2m+1)\) as \(m\to\infty\). Thus the gap is a genuine complementary-spectrum separation and not an estimate with inaccessible endpoints.

## Assumptions and scope
All polygons use ordinary Euclidean area and standard lattice coordinates. The origin lies strictly inside \(B_h\), so its polar is bounded. The result is specific to the divisor-closed symmetric parabolic abscissae \(\{\pm d:d\mid h\}\); the exact reciprocal identity is not asserted for arbitrary finite subsets of a parabola. An accumulation value refers to a limit along integer heights tending to infinity. The previously established primal area profile is reconstructed here for completeness, not claimed as new.

## Proof
**Step 1: original area and the divisor involution.** Let \(\delta_i=d_{i+1}-d_i\). The upper horizontal edge of \(B_h\) joins \((-h,h^2)\) to \((h,h^2)\); its lower boundary is the symmetric chain through the parabolic points and \((0,-1)\). Its area by trapezoids is
\[
 A_h=2h^3-\sum_{i=1}^{k-1}\delta_i(d_i^2+d_{i+1}^2)
 =\frac{4h^3+2-S_h}{3},
\]
using \(\delta_i(d_i^2+d_{i+1}^2)=\tfrac23(d_{i+1}^3-d_i^3)+\tfrac13\delta_i^3\). The symmetry \(d_i d_{k+1-i}=h\) is a bijection of the ordered divisor list. Therefore \(r_i=1/d_i\) decreases from \(1\) to \(1/h\), and the consecutive-gap multiset of \(r_i\) is exactly \(\{\delta_i/h:1\le i<k\}\).

**Step 2: exact polar vertices.** The origin is interior, as the triangle with vertices \((0,-1),(-1,1),(1,1)\) contains it. The supporting lower line through \((a,a^2),(b,b^2)\), for adjacent positive divisors \(a<b\), is \(y=(a+b)x-ab\). Its outward polar vertex is \((a^{-1}+b^{-1},-(ab)^{-1})\). The two lower central edges give \((\pm2,-1)\), the top edge gives \((0,h^{-2})\), and the remaining vertices are reflected in the vertical axis. These are all vertices, in their respective boundary order.

**Step 3: the polar cubic-gap lemma.** More generally choose real \(1=r_1>r_2>\cdots>r_k=s>0\), retain the two central polar vertices \((\pm2,-1)\), the top \((0,s^2)\), and take the consecutive right-chain vertices \(v(u,v)=(u+v,-uv)\), reflected across the vertical axis. Then the polygon enclosed by these vertices has area
\[
 \frac83+\frac13\sum_{i=1}^{k-1}(r_i-r_{i+1})^3+\frac43s^3. \tag{1}
\]
For \(k=2\), shoelace gives \(3-s+s^2+s^3\), agreeing with (1). Inserting \(w\) strictly between consecutive parameters \(u>w>v\) replaces the polar vertex \(v(u,v)\) with \(v(u,w),v(w,v)\). Each of the two mirror-image triangles removed from the polar has area \((u-v)(u-w)(w-v)/2\): subtracting their vertex coordinates gives the determinant \((u-v)(u-w)(w-v)\) in absolute value. The total area therefore decreases by \((u-v)(u-w)(w-v)\). The cubic-gap sum in (1) changes by exactly
\[
 \frac{(u-w)^3+(w-v)^3-(u-v)^3}{3}=-(u-v)(u-w)(w-v).
\]
This proves (1) by induction on the number of parameters, with no numerical approximation.

**Step 4: reciprocity.** Apply (1) with \(r_i=1/d_i\) and \(s=1/h\), and use Step 1:
\[
 \operatorname{area}(B_h^\circ)=\frac83+\frac{S_h}{3h^3}+\frac{4}{3h^3}
 =\frac{8h^3+4+S_h}{3h^3}.
\]
Adding the Step 1 formula for \(A_h/h^3\) gives the claimed exact identity.

**Step 5: asymptotic extremes and the polar gap.** For a finite ordered set \(X\subset[0,1]\) containing \(0,1\), write \(F(X)\) for the sum of cubes of its consecutive gaps. Adding points can only decrease \(F\). Put \(X_h=\{0\}\cup\{1/d:d\mid h\}\). Then \(F(X_h)=S_h/h^3+1/h^3\), and Step 4 gives
\[
 \operatorname{area}(B_h^\circ)=\frac83+\frac{F(X_h)}3+\frac1{h^3}. \tag{2}
\]
All \(X_h\) are subsets of \(X_\mathrm{all}=\{0\}\cup\{1/n:n\ge1\}\). Since splitting a gap strictly reduces its cube, \(F(X_h)\ge F(X_\mathrm{all})=\sum_{n\ge1}(1/n-1/(n+1))^3=10-\pi^2\), by partial fractions and \(\sum n^{-2}=\pi^2/6\). Also \(F(X_h)\le1\). Both bounds are asymptotically sharp: take \(h_m=\operatorname{lcm}(1,\ldots,m)\) or prime \(h_m\to\infty\), respectively. Formula (2) gives the displayed polar liminf and limsup.

For every **even** \(h\), the reciprocal set includes \(0,1/2,1\), so \(F(X_h)\le1/4\), and (2) implies \(\operatorname{area}(B_h^\circ)\le11/4+h^{-3}\). For every **odd** \(h\), the reciprocal set is a subset of \(X_\mathrm{odd}=\{0\}\cup\{1/(2n+1):n\ge0\}\), hence \(F(X_h)\ge F(X_\mathrm{odd})\). Expanding consecutive-cube gaps and telescoping gives
\[
 F(X_\mathrm{odd})=\sum_{n\ge0}\left(\frac1{2n+1}-\frac1{2n+3}\right)^3=4-\frac{3\pi^2}{8}.
\]
Formula (2) yields \(\operatorname{area}(B_h^\circ)\ge4-\pi^2/8+h^{-3}\) for odd \(h\). Any convergent subsequence has a further all-even or all-odd subsequence, so its limit cannot lie strictly between \(11/4\) and \(4-\pi^2/8\). For \(h=2p\), odd primes \(p\to\infty\), \(X_h\) approaches \(\{0,1/2,1\}\) and (2) approaches \(11/4\); for the odd least common multiples in the Finding, \(X_h\) approaches \(X_\mathrm{odd}\), giving the other endpoint. This proves sharpness.

## Verification
The self-contained standard-library checker `checker.py` independently generates exact original and polar polygon vertices and computes both areas by rational shoelace determinants, rather than using the cubic-gap formulas to compute their values. It also checks the boundary lattice-point count by edge gcd and tests the insertion determinants. It passed 507 integer-height cases (all \(2\le h\le500\), plus eight additional values) and three rational insertion triples. The unbounded-height claims depend on the analytic proof, not this finite testing.

## Relationship to prior work
Hofscheier and Nill, *Reflexive polytopes can have doubly exponentially many vertices* (arXiv:2611.08819v1, first public 2026-11-06), introduced these divisor-parabola polygons and characterized their vertices and facet lattice distances for constructing many-faceted reflexive polytopes. Earlier arithmetic analysis of the **primal** polygons already supplies their lattice-boundary counts, cubic-gap area formula, and normalized area spectrum. The present contribution concerns the **polar** area and the exact finite-height reciprocal identity, whose proof depends on a separate polar-vertex insertion law. It makes polar asymptotics and a sharp polar spectral gap accessible from the primal arithmetic structure, without claiming the older primal results as new. Ordinary planar Pick/Ehrhart theory supplies the standard lattice-point interpretation but not the asserted polar relation.

## Limitations
The identity is for the specific original lattice realization and origin; translating or affinely altering a body changes its Euclidean polar area in general. No general polar reciprocity for arbitrary convex polygons, no reflexive higher-dimensional volume formula, and no assertion of the largest spectral gap are proved. The result is self-reviewed only; independent external mathematical assessment and exhaustive historical-priority adjudication are not performed.

## References
- J. Hofscheier and B. Nill, *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1, November 6, 2026, https://arxiv.org/abs/2611.08819 (especially Section 4 and Lemma 4.1).
- G. Pick, *Geometrisches zur Zahlenlehre*, Sitzungsberichte des deutschen naturwissenschaftlich-medicinischen Vereines für Böhmen „Lotos“ 19 (1899), 311–319 (classical lattice polygon area relation; only contextual here).
- Classical Basel identity, \(\sum_{n\ge1}n^{-2}=\pi^2/6\), used in the endpoint calculations.
