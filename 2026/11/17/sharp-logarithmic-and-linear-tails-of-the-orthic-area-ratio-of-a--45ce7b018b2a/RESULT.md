# Sharp logarithmic and linear tails of the orthic-area ratio of a random cyclic triangle

## Finding
Let \(T\) have vertices at three independent uniform points on a fixed Euclidean circle. Let \(F(T)\) be the triangle formed by the feet of the three altitudes of \(T\), allowing feet on extended sides. Let \(Q=\operatorname{area}(F(T))/\operatorname{area}(T)\). The exact mean and both sharp endpoint laws are
\[
\mathbb E Q=\frac14+\frac3{\pi^2},\qquad
\mathbb P(Q\le t)\sim\frac6{\pi^2}t\log(1/t),\qquad
\mathbb P(Q>2-t)\sim\frac{t}{\pi\sqrt3}.
\]
In particular the geometric maximum of \(Q\) is \(2\), approached by flat triangles, not by equilateral ones. The lower tail is logarithmically enhanced by a simultaneous right-angle/flat-triangle degeneracy.

## Assumptions and scope
Exactly three independent circle points have the uniform angular distribution. With probability one they are distinct and form a nondegenerate Euclidean triangle with internal angles \(A,B,C>0\) and \(A+B+C=\pi\). We use **unsigned** areas, including for obtuse triangles; dropping the absolute value in the displayed ratio would alter the statement. Each assertion holds for every circle radius by scale invariance. The endpoint limits fix the sample size at three.

## Proof
**Angle distribution and orthic identity.** The three cyclic angular gaps divided by two are, up to a cyclic permutation, the three angles \(A,B,C\). The normalized gaps have the \(\operatorname{Dirichlet}(1,1,1)\) law. Hence \((A,B)\) has constant density \(2/\pi^2\) on \(\{A>0,B>0,A+B<\pi\}\). The classical altitude-foot geometry, or coordinate projection of each vertex onto the opposite side line and a determinant, gives
\[
 Q=2|\cos A\cos B\cos C|.
\]
For acute triangles the orthic triangle lies in the original; for an obtuse triangle the sign of the product reverses, while its absolute area retains the formula. Since at most one cosine is negative and \(\prod |\cos A|\le1\), we have \(0\le Q\le2\); \(Q\to2\) as one angle tends to \(\pi\) and the other two to zero.

**Mean.** Write \(P=\cos A\cos B\cos C\). The product-to-sum identity and the uniform angle simplex yield \(\mathbb E P=-1/4\). The acute region, where \(P>0\), has probability \(1/4\). Conditioned on acuteness, \((U,V,W)=(\pi-2A,\pi-2B,\pi-2C)\) is again uniformly distributed on the positive angle simplex. The elementary identity
\[
4\sin(U/2)\sin(V/2)\sin(W/2)=\cos U+\cos V+\cos W-1
\]
and \(\mathbb E\cos U=4/\pi^2\) on that simplex give
\[
\mathbb E[P\mathbf1_{\mathrm{acute}}]=\frac{3}{4\pi^2}-\frac1{16}.
\]
Thus \(\mathbb E Q=2(2\mathbb E[P\mathbf1_{\mathrm{acute}}]-\mathbb E P)=1/4+3/\pi^2\).

**Lower endpoint.** The zero set of \(Q\) comprises the three right-angle segments \(A=\pi/2\), \(B=\pi/2\), \(C=\pi/2\). Away from the three corner points \((0,\pi/2,\pi/2)\) and permutations, each zero is transverse and its fixed-neighborhood contribution to \(\Pr(Q\le t)\) is \(O(t)\). Near \(A=0\), put \(x=A\ge0\), \(y=B-\pi/2\), so \(C=\pi/2-x-y\) and
\[
 Q=2|\cos x\sin y\sin(x+y)|=2|y(x+y)|(1+O(x^2+y^2)).
\]
Set \(s=y\) and \(v=x+y\), with Jacobian one and wedge \(v\ge s\). Inside a fixed small square the area cut out by \(|sv|\le h\) is \(2h\log(1/h)+O(h)\): the two same-sign wedges each contribute \(\frac h2\log(1/h)+O(h)\) and the allowed opposite-sign quadrant contributes \(h\log(1/h)+O(h)\). With \(h=t/2\), this corner contributes \(t\log(1/t)+O(t)\) of angle-simplex area. The smooth multiplicative correction and fixed cutoff change only \(O(t)\); this follows by sandwiching between constant multiples on a shrinking corner box and then sending that box radius to zero. Summing the three disjoint corners and multiplying by density \(2/\pi^2\) proves the first tail coefficient.

**Upper endpoint.** The only maximum-approaching regions are the three flat corners of the simplex, where one angle approaches \(\pi\). Near \(A=\pi\), write \(B=u\ge0\), \(C=v\ge0\) so \(A=\pi-u-v\). The positive product identity yields
\[
2-Q=2(u^2+uv+v^2)+O((u+v)^4).
\]
The quadrant \(u,v\ge0\) ellipse sector satisfying \(2(u^2+uv+v^2)<t\) has area \(\pi t/(6\sqrt3)\): the transformation \((u,v)\mapsto (u+v/2,\sqrt3v/2)\) has Jacobian \(\sqrt3/2\) and sends the quadrant to a sector of opening angle \(\pi/3\). Three equal flat corners, weighted by density \(2/\pi^2\), give \(\Pr(Q>2-t)\sim t/(\pi\sqrt3)\).

## Verification
The accompanying standalone `orthic_checker.py` directly constructs the three perpendicular feet for randomly selected triangles and compares their unsigned area ratio with the cosine-product formula. It also reproduces the exact mean numerically and checks endpoint ratios from independent samples. It prints `ORTHIC_AREA_RATIO_CHECKS_OK` on success. Stochastic calculations support but cannot establish the analytic asymptotic limits; those follow from the simplex integrals and corner expansions above.

## Relationship to prior work
Classical orthic-triangle (pedal-triangle) geometry supplies the cosine-product area relation. Koroleva and Nikitin (first public arXiv posting 2013-01-07) establish extreme *original-polygon* perimeter and area laws for circle-sampled points; they do not consider altitude feet or the distribution of an orthic-area ratio. Marckert (first posting 2014-02-14) instead studies convex position of area-uniform points in a disk. Published published-finding corpus records concerning the ordinary inradius, original area, and acute-triangle transport use different geometric statistics. Neither their scalar outputs nor a reduction to an original-area law implies this orthic-area ratio distribution. The explicit three-point angular law is a standard starting point and is not claimed as new. No definitive historical-priority certificate is claimed.

## Limitations
Only the exact mean and the two leading endpoint equivalents are established, not the full closed-form density or higher-order remainders. All three vertices must be independently uniform in angle on one circle. An obtuse triangle requires feet on extended side lines. Priority remains provisional, and no independent mathematical audit has been conducted.

## References
- E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (2013), https://arxiv.org/abs/1301.1360.
- J.-F. Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512 (2014), https://arxiv.org/html/1402.3512v1.
- *Orthocenter / Orthic Triangle*, Brilliant Math & Science Wiki, https://brilliant.org/wiki/triangles-orthocenter/ (classical geometric background, not a priority claim).
