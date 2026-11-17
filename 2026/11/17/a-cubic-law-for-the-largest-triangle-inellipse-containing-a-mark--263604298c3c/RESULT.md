# A cubic law for the largest triangle inellipse containing a marked point

## Finding

Let \(T\) be a nondegenerate Euclidean triangle, let \(P\) be any point strictly inside \(T\), and write \(w=(w_1,w_2,w_3)\) for its positive barycentric coordinates, normalized by \(w_1+w_2+w_3=1\). Among **nondegenerate ellipses contained in \(T\), tangent to all three sides, and whose filled interiors contain \(P\)**, there is exactly one of greatest area. Its area and equation are given by the following complete rule.

If \(2\sum_{k=1}^3 w_k^2\leq1\), put \(u_1=u_2=u_3=1/3\). Otherwise there is exactly one index \(k\) for which
\[
\sqrt{w_k}>\sqrt{w_i}+\sqrt{w_j},\qquad\{i,j,k\}=\{1,2,3\}.
\]
Put \(A=1/w_k\), \(B=1/w_i\), \(C=1/w_j\). The polynomial
\[
(A+B)q^3+(A+2B)q^2-(A+2C)q-(A+C)
\]
has exactly one positive zero \(q\). Set
\[
D=A(q+1)^2+Bq^2+C,\qquad
u_k=\frac{A(q+1)^2}{D},\quad
u_i=\frac{Bq^2}{D},\quad
u_j=\frac{C}{D}.
\]
In both regimes, the unique optimal filled ellipse consists of the points \(X\) with barycentric coordinates \(x=(x_1,x_2,x_3)\) satisfying
\[
\sum_{r=1}^3u_r^2x_r^2-2\sum_{1\le r<s\le3}u_ru_sx_rx_s\le0,
\]
and its *exact normalized area* is
\[
\boxed{\frac{\operatorname{area}(E_*)}{\operatorname{area}(T)}
=\pi\sqrt{u_1u_2u_3}.}
\]
For an exterior-to-Steiner target, the target lies on the optimal ellipse; otherwise the usual Steiner inellipse is optimal.

A sharp one-dimensional consequence is obtained on any vertex median. For \(w=(t,(1-t)/2,(1-t)/2)\) with \(0<t<1\), the normalized optimal area is
\[
\boxed{H(t)=\begin{cases}
\pi/(3\sqrt3),&0<t\le2/3,\\
(\pi/2)t\sqrt{1-t},&2/3<t<1.
\end{cases}}
\]
This profile is continuously differentiable but not twice differentiable at \(t=2/3\): its left second derivative is zero and its right second derivative is \(-3\sqrt3\pi/4\). Thus imposing containment of a marked point has an exact saturation boundary and a quadratic-onset area penalty.

## Assumptions and scope

The plane is Euclidean. Triangle \(T\) is arbitrary but nondegenerate; all three coordinates of \(P\) are strictly positive. An *inellipse* is the nondegenerate filled ellipse lying in \(T\) and tangent to the relative interiors of all three sides. The marked point may lie on the ellipse boundary. The optimization is over this precisely defined class of **three-side-tangent inellipses**, not over arbitrary ellipses that might have fewer side contacts. No numerical tolerance or general-position hypothesis is used.

## Proof

**Step 1: All inellipses and their areas.** Affine covariance allows us to take \(T\) to be the unit triangle, using barycentric coordinates \(x_1+x_2+x_3=1\). Its every three-side-tangent inellipse has, up to a positive common factor, the quadratic equation
\[
F_u(x)=\sum_{i=1}^3u_i^2x_i^2-2\sum_{i<j}u_iu_jx_ix_j=0,
\qquad u_i>0,\quad\sum_i u_i=1.
\]
To see necessity, the restriction of the conic to each line \(x_i=0\) must be a perfect square, and its unique contact on that side must have nonnegative barycentric coordinates. This forces the three diagonal coefficients to be positive squares and all three mixed coefficients to be their **negative** geometric means. Conversely, for positive \(u\), the restriction to \(x_i=0\) is \((u_jx_j-u_kx_k)^2\), giving a single interior tangency; the center has barycentric coordinates \(c_i=(1-u_i)/2\) and lies strictly in the triangle. In affine coordinates \((x_1,x_2)\), the quadratic matrix has determinant \(4u_1u_2u_3\), while \(F_u(c)=-u_1u_2u_3\). Therefore the conic is a nondegenerate ellipse, its supporting side lines keep it inside \(T\), and the standard area formula for \(F_u\le0\) gives
\[
\operatorname{area}(E_u)=\pi\sqrt{u_1u_2u_3}\,\operatorname{area}(T).
\]
These facts also prove that the parameter \(u\) is unique.

**Step 2: Convex point-containment condition.** For the fixed target \(P\), put \(z_i=u_iw_i>0\). The inequality \(F_u(w)\le0\) is
\[
2(z_1z_2+z_1z_3+z_2z_3)\ge z_1^2+z_2^2+z_3^2.
\]
By Heron's identity, this is equivalent to the three positive numbers \(\sqrt{z_i}\) being side lengths of a (possibly degenerate) triangle. Equivalently, for each permutation \((i,j,k)\),
\[
z_k\le z_i+z_j+2\sqrt{z_iz_j}.
\]
The right side is concave in the positive variables \((u_i,u_j)\), since the geometric mean is concave. Consequently, each of these three inequalities defines a convex feasible set in \(u\), as does their intersection. It has positive interior (choose \(u_i\) proportional to \(1/w_i\)). On it, maximizing ellipse area is equivalent to maximizing the strictly concave function \(\sum_i\log u_i\); the maximum is attained at a unique positive parameter, since the product tends to zero at any boundary of the parameter simplex.

**Step 3: The saturated regime.** Without the point constraint, the arithmetic-geometric mean inequality gives the unique optimum \(u_i=1/3\). The containment test there simplifies exactly to
\[
F_{(1/3,1/3,1/3)}(w)=\frac{2\sum_iw_i^2-1}{9}.
\]
Hence the Steiner inellipse is optimal precisely when \(2\sum_iw_i^2\le1\), including equality.

**Step 4: The active corner and cubic.** Suppose \(2\sum_iw_i^2>1\). The Heron criterion shows there is a unique \(k\) with \(\sqrt{w_k}>\sqrt{w_i}+\sqrt{w_j}\). Consider first just the single convex constraint
\[
\sqrt{w_ku_k}\le\sqrt{w_iu_i}+\sqrt{w_ju_j}.
\]
Its log-product maximizer cannot be strictly feasible, since then stationarity in the interior simplex would force \(u=(1/3,1/3,1/3)\), which violates this constraint. Thus equality holds. Because the three square roots remain positive, equality of this one triangle inequality automatically makes the other two strict; the maximizer for this single constraint is therefore feasible for the original three constraints and is the desired unique global maximizer.

Put \(v_r=\sqrt{w_ru_r}\) and write \(v_i=qv_j\), \(v_k=(1+q)v_j\), where \(q>0\). Normalization \(\sum u_r=1\) yields the displayed formulas for \(u\) and \(D\). Its product is
\[
u_iu_ju_k=\frac{ABCq^2(q+1)^2}{[A(q+1)^2+Bq^2+C]^3}.
\]
The derivative of its logarithm vanishes exactly when
\[
(A+B)q^3+(A+2B)q^2-(A+2C)q-(A+C)=0.
\]
The coefficient signs in descending powers are \(+,+,-,-\), so Descartes' rule of signs gives at most one positive root. The polynomial is negative at zero and positive at infinity, giving exactly one. The product tends to zero as \(q\downarrow0\) or \(q\to\infty\), so the root is the unique maximum. This finishes the formula and uniqueness proof for every admissible target.

**Step 5: Median threshold.** For \(w=(t,(1-t)/2,(1-t)/2)\), the Steiner condition becomes \(t\le2/3\). Beyond it \(B=C\), so the unique positive cubic root is \(q=1\); hence \(u=(1-t,t/2,t/2)\). Substitution gives \(H(t)\). Direct one-sided differentiation gives the asserted \(C^1\)-but-not-\(C^2\) transition and the exact second-derivative jump.

## Verification

The proof above applies to all positive barycentric targets and is not based on finite enumeration. In `check.py`, exact rational arithmetic verifies the nontrivial example \(w=(4/5,1/10,1/10)\), \(u=(1/5,2/5,2/5)\), for which \(F_u(w)=0\) and the area ratio is \(2\pi/(5\sqrt5)\). Deterministic randomized tests reconstruct the optimal parameter for 500 target triples, independently sample 300,000 feasible competitors, verify the predicted boundary activity and AM–GM upper bound, and check six median targets across the transition. An additional SciPy optimizer comparison was performed separately for 30 random target triples, with three independently initialized optimizations per triple. These finite tests detect implementation errors but do not replace the proof's convexity and uniqueness arguments.

To replay the included self-contained checker: `python3 check.py`. It requires only the Python standard library and prints `POINT_CONSTRAINED_TRIANGLE_INELLIPSE_CHECKS_OK` on success.

## Relationship to prior work

The Steiner inellipse and its unrestricted maximum-area property are classical, as is the center-based area formula. Horwitz (2015) parametrizes triangle inellipses and studies their incidence with two prescribed points, or a prescribed point and tangent direction. Juhász (2012) gives a control-point parametrization of all triangle inellipses. These results establish the natural underlying family but do not state the area maximization subject to **containing a marked point**, the exact active-corner cubic, or the median saturation law. The present statement is a constrained optimum, not a new proof of the unrestricted Steiner theorem. Related extremal-ellipsoid results for truncated simplices and inellipses of quadrilaterals address different feasible bodies or objectives and do not imply this marked-point profile.

## Limitations

The theorem is only about ellipses tangent to **all three sides**, with a target strictly inside the original triangle; allowing fewer side contacts or moving the target to the triangle boundary changes the problem. It does not provide an analogous formula for higher-dimensional simplices, more than one target, or arbitrary polygons. Historical priority is assessed from the sources below and mathematical-index searches; undiscovered equivalent classical descriptions remain a residual risk. The result has not received independent mathematical validation.

## References

- A. Horwitz, *Dynamics of ellipses inscribed in triangles*, arXiv:1504.05141, first public version April 20, 2015. https://arxiv.org/abs/1504.05141
- I. Juhász, *Control point based representation of inellipses of triangles*, Annales Mathematicae et Informaticae **40** (2012), 37–46. https://real-j.mtak.hu/22331/1/AnnMathInf_40_2012.pdf
- E. W. Weisstein, *Inellipse*, MathWorld; contains the classical center-area formula and references to G. D. Chakerian (1979). https://mathworld.wolfram.com/Inellipse.html
- E. W. Weisstein, *Steiner Inellipse*, MathWorld; records the classical unrestricted maximum-area property. https://mathworld.wolfram.com/SteinerInellipse.html
