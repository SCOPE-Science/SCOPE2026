# Sharp minimax stability for reverse perimeter profiles of triangular containers

## Finding
For a nondegenerate Euclidean triangle \(T\), let \(a\ge b\ge c>0\) be its side lengths, and set \(P=a+b+c\). Fix any area fraction \(0<\eta<1\). Define the optimal contained-perimeter profile
\[
\mathcal R_\eta(T)=\max\{\operatorname{Per}(K):K\subseteq T\text{ compact, convex, with nonempty interior and }|K|=\eta|T|\}.
\]
Put
\[
r_\eta=\sqrt{1-\eta+\eta^2},\qquad
f_\eta=\frac{1+\eta+r_\eta}{3},\qquad
\kappa_\eta=2(1-f_\eta)=\frac{2}{3}(2-\eta-r_\eta).
\]
**Theorem.** Every such triangle satisfies the **sharp global linear stability inequality**
\[
\boxed{\mathcal R_\eta(T)\ge f_\eta P+\kappa_\eta(a-c).}
\]
Equality holds **if and only if** \(T\) is equilateral. In particular, among all nondegenerate triangular containers with fixed perimeter, the equilateral triangle is the unique minimizer of the largest perimeter achievable by a convex subset occupying the fraction \(\eta\) of its area. The coefficient \(\kappa_\eta\) is best possible simultaneously over all nondegenerate triangles. Every sequence of non-equilateral triangles for which the normalized deficit-to-side-spread ratio approaches \(\kappa_\eta\) has, after ordering and normalization of its sides, the degenerate limiting similarity class \(1:1:0\); conversely that class realizes the sharp limit.

## Assumptions and scope
The parameter \(\eta\) is fixed and belongs to \((0,1)\). The triangle is planar, nondegenerate, and otherwise arbitrary; \(a,b,c\) are sorted in nonincreasing order. Perimeter and area are ordinary Euclidean functionals. For the sharpness-sequence assertion, the ratio is defined only when \(a>c\). The degenerating \(1:1:0\) configuration is **not** an admissible triangle and does not attain equality. The theorem does not assert stability of the maximizing subbody itself, or extend the container minimax to arbitrary polygons.

## Proof
**1. Explicit area-matched witness.** Write the vertices of \(T\) as \(A,B,C\), with \(|BC|=a\), \(|CA|=b\), and \(|AB|=c\). Let \(D=(1-\eta)B+\eta A\). The triangle \(K=\operatorname{conv}\{B,C,D\}\) lies in \(T\), has \(|K|=\eta|T|\), and has perimeter
\[
W_\eta(T)=a+\eta c+q,\qquad
q=\sqrt{(1-\eta)a^2+\eta b^2-\eta(1-\eta)c^2}.
\]
The area relation is immediate from the shared base \(BC\), while the length formula is the elementary squared-norm identity for the segment \(CD\). Thus \(\mathcal R_\eta(T)\ge W_\eta(T)\), independently of any classification of globally maximizing subsets.

**2. Ordered-triangle cone.** Set \(u=b-c\ge0\), \(v=a-b\ge0\), and \(w=b+c-a>0\). Then
\[
a=u+2v+w,\quad b=u+v+w,\quad c=v+w,\quad P=2u+4v+3w,\quad a-c=u+v.
\]
For shorter notation put \(z=\eta\), \(r=r_\eta\), \(f=f_\eta\), \(\kappa=\kappa_\eta\), and \(d=(2-z+2r)/3\). Direct expansion gives
\[
q^2=u^2+(2-z)^2v^2+r^2w^2+2(2-z)uv+2uw+2(z^2-2z+2)vw.
\]
Define \(L=u+dv+rw\). Substituting \(r^2=1-z+z^2\) and collecting terms gives the **exact nonnegative remainder identity**
\[
\boxed{q^2-L^2=2(1-r)uw+\frac23(2-z-r)v\bigl[2u+(2-z+d)v+(2-z)w\bigr].}
\]
Since \(0<z<1\), \(0<r<1\) and \(2-z-r>0\). All terms in this identity are nonnegative; therefore \(q\ge L\), since \(q,L\ge0\). Moreover, algebraic substitution yields
\[
a+zc+L=fP+\kappa(a-c).
\]
Consequently \(\mathcal R_\eta(T)\ge W_\eta(T)\ge fP+\kappa(a-c)\).

**3. Equality and the minimax conclusion.** If \(T\) is non-equilateral, at least one of \(u,v\) is positive. Since \(w>0\), the exact remainder is strictly positive whenever \(u>0\) or \(v>0\). Hence \(W_\eta(T)>fP+\kappa(a-c)\), proving strictness for all non-equilateral triangles. If \(T\) is equilateral, the sharp reverse isoperimetric theorem for triangle containers [1, Theorem 1] says the explicit witness in step 1 is globally perimeter maximizing; there \(u=v=0\), so \(\mathcal R_\eta(T)=fP\). This establishes equality, uniqueness, and the asserted minimax value. Only the equilateral equality case uses the known maximal-perimeter classification.

**4. Optimal coefficient.** Consider triangles with \(a=b=1\) and \(c=\varepsilon\downarrow0\). The witness in step 1 has perimeter \(1+\eta\varepsilon+\sqrt{1-\eta(1-\eta)\varepsilon^2}\to2\). The full container perimeter equals \(2+\varepsilon\to2\), and perimeter monotonicity under inclusion gives \(\mathcal R_\eta(T)\le2+\varepsilon\). Thus \(\mathcal R_\eta(T)\to2\), while \(P\to2\) and \(a-c\to1\). A universally valid coefficient greater than \(2-2f=\kappa\) would contradict this limit. This proves sharpness without invoking an extremal-subbody formula for the degenerating triangles.

**5. Unique sharpness mechanism.** Whenever \(a>c\),
\[
\frac{\mathcal R_\eta(T)-fP}{a-c}\ge \kappa+\frac{q^2-L^2}{(q+L)(u+v)}.
\]
Normalize \(P=1\). The closed cone \(u,v,w\ge0\), \(2u+4v+3w=1\) is compact. Its nonnegative remainder vanishes only when \(v=0\) and \(uw=0\): the equilateral ray \(u=v=0\), or the degenerate ray \(v=w=0\). Near the equilateral ray, \(w\to1/3\) and the displayed positive remainder is bounded below by a positive multiple of \(w(u+v)\), so its quotient by \((q+L)(u+v)\) does not tend to zero. Indeed, the two linear \(uw\) and \(vw\) contributions have strictly positive coefficients for fixed \(z\in(0,1)\). Therefore a sequence with deficit-to-side-spread ratio tending to \(\kappa\) must approach \(v=w=0\), \(u=1/2\). The converse is the family in step 4. In side lengths this is exactly the class \(1:1:0\).

## Verification
The exact polynomial remainder and the linear identity in step 2 were independently recomputed by symbolic arithmetic under the relation \(r^2=1-z+z^2\) using the supplied `check.py`. Its deterministic test also examines 30,000 positive ordered-triangle parameter tuples and 15 slender-triangle boundary examples. All checks passed. The symbolic identity validates the critical algebra; the universal sign argument, sharpness, and uniqueness are proved above and do not rely on finite sampling. Run `python check.py` with SymPy 1.12 or later. The cited paper's equilateral equality case was checked against its primary full text.

## Relationship to prior work
Ait El Manssour, Fattah, and Ftouhi [1, Theorem 1] give the **exact maximum perimeter for every fixed triangle** at fixed area fraction and characterize maximizing subtriangles. The present result is a different, second-stage optimization **over the containers themselves**: it proves a dimensionless minimax inequality across all triangular shapes with the optimal global linear side-spread coefficient, strict equality characterization, and unique degeneration for asymptotic sharpness. The cited exact formula implies the problem can be attacked, but does not state or prove this sharp uniform stability optimization. In fact, our inequality uses only one explicit witness and invokes their theorem solely to certify equality at the equilateral container. The classical inclusion-constrained framework of Bogosel [2] establishes existence and polygonal maximizers for polygonal containers, but neither the triangular minimax inequality nor its sharp coefficient. Drach and Tatarko [3] prove other reverse-isoperimetric stability statements for curvature-constrained bodies; those do not imply the triangular-container result. Searches of related mathematical research records revealed no matching sharp container-side-spread theorem; that search is not a certification of historical priority.

## Limitations
This is a first-order **linear** stability estimate in the side spread \(a-c\), not a Hausdorff estimate for the maximizing subset. The coefficient is optimal only uniformly over all triangles; on a compact nondegenerate shape class it can be strengthened. Sharpness is approached only by a degenerate limiting triangle, not attained away from equilateral. The result is a new optimization of a known 2026 explicit profile, not a new determination of that profile. Definitive historical priority and independent mathematical validation have not been established.

## References
[1] R. Ait El Manssour, Z. Fattah, I. Ftouhi, *The reverse isoperimetric inequality for convex shapes included in a triangle*, arXiv:2610.36220v1, first posted 2026-10-26. https://arxiv.org/html/2610.36220

[2] B. Bogosel, *A reverse isoperimetric inequality for convex shapes with inclusion constraint*, arXiv:2402.05648, first posted 2024-02-08. https://arxiv.org/abs/2402.05648

[3] K. Drach, K. Tatarko, *Stability of reverse isoperimetric inequalities in the plane: area, Cheeger, and inradius*, arXiv:2410.06096, first posted 2024-10-08. https://arxiv.org/abs/2410.06096
