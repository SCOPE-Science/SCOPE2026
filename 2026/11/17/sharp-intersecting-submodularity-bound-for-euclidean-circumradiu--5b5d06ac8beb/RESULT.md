# Sharp intersecting submodularity bound for Euclidean circumradius

## Finding
For all integers \(d\ge 1\) and all finite nonempty \(A,B\subset\mathbb R^d\) with \(A\cap B\ne\varnothing\), write \(R(E)\) for the radius of the smallest closed Euclidean ball containing \(E\). Put \(a=R(A)\), \(b=R(B)\), \(r=R(A\cap B)\), and \(s=(a+b)/2\). The **sharp two-parameter inequality** is
\[
R(A\cup B)\le s+\sqrt{s^2-r^2}.
\]
Consequently,
\[
R(A\cup B)+R(A\cap B)\le\frac{1+\sqrt2}{2}\bigl(R(A)+R(B)\bigr).
\]
For every \(d\ge2\), the coefficient \((1+\sqrt2)/2\) is the least possible universal coefficient. For fixed \(s>0\) and every \(0\le r\le s\), the first inequality is attained with \(a=b=s\), by finite planar point sets. In dimension one the better coefficient \(1\) is sharp.

## Assumptions and scope
All sets here are finite and nonempty and have at least one common point, not merely overlapping convex hulls. The Euclidean norm is the ordinary \(\ell_2\) norm, not a general Minkowski norm. A singleton has circumradius zero. Since \(A\cap B\subseteq A,B\), we have \(0\le r\le\min(a,b)\le s\). When \(s=0\), both sets are the same singleton and the assertions are trivial. The two-parameter envelope is stated in terms of the average separate radius and the common-set radius, not in terms of all three separate radii individually.

## Proof
**1. A center-displacement lemma.** Let \(C=A\cap B\) have minimum-ball center \(o\) and radius \(r\). There are finitely many boundary points \(z_i\in C\) and nonnegative weights \(\lambda_i\) summing to one such that \(\sum_i\lambda_i(z_i-o)=0\) and \(\lVert z_i-o\rVert_2=r\). Indeed, minimizing the convex function \(x\mapsto\max_{z\in C}\lVert x-z\rVert_2^2\) gives the zero vector in the convex hull of its active gradients \(2(o-z)\); alternatively strict separation would yield a small center shift decreasing every active squared distance. This argument includes \(r=0\), when \(C\) is a singleton.

For any closed ball \(B(c,t)\) containing \(C\), averaging squared distances over those contacts gives
\[
t^2\ge \sum_i\lambda_i\lVert z_i-c\rVert_2^2
=r^2+\lVert c-o\rVert_2^2.
\]
Thus the minimum-ball centers \(c_A,c_B\) satisfy
\[
\lVert c_A-o\rVert_2\le\sqrt{a^2-r^2},\qquad
\lVert c_B-o\rVert_2\le\sqrt{b^2-r^2},
\]
and their distance \(D=\lVert c_A-c_B\rVert_2\) obeys
\[
D\le\sqrt{a^2-r^2}+\sqrt{b^2-r^2}.
\]

**2. Covering the union of two balls.** Two Euclidean balls of radii \(a,b\) with center separation \(D\) fit in a ball of radius no greater than
\[
\max\left\{a,b,\frac{a+b+D}{2}\right\}.
\]
If \(D\le |a-b|\), the larger original ball contains the smaller. Otherwise, take the center on their line of centers at distance \((D+b-a)/2\) from \(c_A\) toward \(c_B\); both component balls are then contained in a ball of radius \((a+b+D)/2\). Therefore this bound applies to \(A\cup B\).

The function \(t\mapsto\sqrt{t^2-r^2}\) is concave for \(t\ge r\) (by its second derivative, or by direct differentiation, with continuity at \(t=r\)). Jensen's inequality implies
\[
D\le 2\sqrt{s^2-r^2}.
\]
Moreover \(\max(a,b)=2s-\min(a,b)\le 2s-r\le s+\sqrt{s^2-r^2}\), because \(\sqrt{s^2-r^2}\ge s-r\) for \(0\le r\le s\). Combining the two branches proves
\[
R(A\cup B)\le s+\sqrt{s^2-r^2}.
\]

**3. Optimize the ratio.** For \(s>0\), set \(t=r/s\in[0,1]\). Then
\[
\frac{R(A\cup B)+r}{a+b}
\le\frac{1+t+\sqrt{1-t^2}}2
\le\frac{1+\sqrt2}2.
\]
The second inequality is Cauchy–Schwarz applied to \((t,\sqrt{1-t^2})\) and \((1,1)\), with equality when \(t=1/\sqrt2\).

**4. Sharpness and the whole envelope.** Given \(s>0\) and \(0<r\le s\), put \(h=\sqrt{s^2-r^2}\) and consider four planar points \(u_\pm=(\pm r,0)\), \(v_\pm=(0,\pm(s+h))\). Set \(A=\{u_+,u_-,v_+\}\), \(B=\{u_+,u_-,v_-\}\). Their intersection is \(\{u_+,u_-\}\), with radius \(r\). The ball of radius \(s\), centered at \((0,h)\), contains all of \(A\), and its center is a convex combination of the three points, so it is a smallest enclosing ball; the reflected statement holds for \(B\). The pair of opposite apices has distance \(2(s+h)\), and the ball centered at zero of radius \(s+h\) covers all four points. Hence \(R(A)=R(B)=s\) and \(R(A\cup B)=s+h\). At \(r=0\) use a shared origin and opposite points \((0,2s)\), \((0,-2s)\). Choosing \(s=\sqrt2\) and \(r=1\) gives the sharp explicit witness
\[
A=\{(-1,0),(1,0),(0,1+\sqrt2)\},\qquad
B=\{(-1,0),(1,0),(0,-1-\sqrt2)\}.
\]
Here \(R(A)=R(B)=\sqrt2\), \(R(A\cap B)=1\), and \(R(A\cup B)=1+\sqrt2\), proving optimality for every \(d\ge2\) by isometric embedding in a two-dimensional affine subspace.

**5. The line.** For finite subsets of \(\mathbb R\), \(2R(E)\) equals the length of its smallest enclosing interval. The intervals for \(A\) and \(B\) overlap because the sets share a point. The length of their union plus the length of their interval intersection equals the sum of their lengths, while the interval enclosing \(A\cap B\) lies inside the interval intersection. Division by two proves \(R(A\cup B)+R(A\cap B)\le R(A)+R(B)\). Equality occurs for nested non-singleton sets.

## Verification
The standalone standard-library script `verify_circumradius_submodularity.py` independently computes smallest enclosing balls by enumerating affinely independent support sets and solving their center equations. It checked the explicit planar extremizer, the published planar counterexample, and 1,752 randomly sampled intersecting pairs in dimensions two, three, and four. All tested instances satisfied the stronger two-parameter inequality and the optimal multiplicative inequality. To reproduce, run `python3 verify_circumradius_submodularity.py`. These floating-point checks are supplementary only; the universal proof and exact extremizer follow from the arguments above.

## Relationship to prior work
Bryant and Tupper (2026), Section 4 Example 15, give four planar points for which Euclidean circumradius fails the ordinary intersecting submodularity inequality: \(R(A\cup B)=2\), \(R(A\cap B)=1\), and \(R(A)=R(B)=5/4\), yielding the ratio \(6/5\). Their example demonstrates failure but does not determine a sharp universal relaxation. The present constant \((1+\sqrt2)/2\) exceeds \(6/5\) and is optimal over all dimensions at least two. Bryant, Huber, Moulton, and Tupper (2023), Theorem 2.1, prove the ordinary diversity triangle inequality \(R(A\cup B)\le R(A)+R(B)\) when the sets overlap; their characterization theorems do not imply the stronger estimate involving \(R(A\cap B)\). This is not a claim about arbitrary convex gauge bodies, and no embedding-based submodularity result is asserted.

## Limitations
The constant applies to ordinary Euclidean circumradii of finite **intersecting** sets. It is not asserted for arbitrary norms, unbounded sets, or configurations whose convex hulls overlap but whose point sets do not. The sharp envelope uses only \(s\) and \(r\) and does not classify all equality configurations. Priority remains provisional: earlier or differently expressed inequalities for Euclidean minimum enclosing balls could subsume the result. Independent audit has not been performed.

## References
Bryant, D., and Tupper, P. F., *Submodular and strongly submodular functions and diversities*, arXiv:2608.11468v1 (first public 2026-08-11), https://arxiv.org/abs/2608.11468. See Section 4, Example 15.
Bryant, D., Huber, K. T., Moulton, V., and Tupper, P. F., *Diversities and the Generalized Circumradius*, *Discrete & Computational Geometry* (2023), DOI: 10.1007/s00454-023-00493-1, https://link.springer.com/article/10.1007/s00454-023-00493-1, especially Theorem 2.1.
