# Parabolic boundary blow-up and sharp area singularity of cyclic polygons

## Finding
For every fixed \(n\ge5\) and positive short-side vector \(b=(b_1,\ldots,b_{n-1})\), put
\[
S=\sum_{i=1}^{n-1}b_i,\qquad H=S^3-\sum_{i=1}^{n-1}b_i^3>0.
\]
The long side of a near-degenerate cyclic polygon is \(a_\varepsilon=S-\varepsilon\), where \(\varepsilon>0\) is the polygon-inequality slack. Let \(R_\varepsilon\) and \(A_\varepsilon\) be its circumradius and area. As \(\varepsilon\downarrow0\),
\[
\boxed{R_\varepsilon=\sqrt{\frac{H}{24\varepsilon}}\,(1+O(\varepsilon)),\qquad A_\varepsilon=\sqrt{\frac{H\varepsilon}{6}}\,(1+O(\varepsilon)).}
\]
Thus \(R_\varepsilon^{-2}\) and \(A_\varepsilon^2\) have real-analytic extensions through the limiting boundary of the side-length feasibility cone, with first derivatives \(24/H\) and \(H/6\), respectively. The area itself has exactly square-root order (and is not differentiable as a function of the slack at zero). The constants are explicit and sharp for every prescribed short-side vector.

For the upper polygonal chain write \(u_0=0\) and \(u_j=b_1+\cdots+b_j\), so \(u_{n-1}=S\). Rotate and translate the polygon so the last edge joins \((0,0)\) to \((S-\varepsilon,0)\), with the other vertices above it. Then for all vertices,
\[
\boxed{x_j=u_j+O(\varepsilon),\qquad \frac{y_j}{\sqrt\varepsilon}=\sqrt{\frac6H}u_j(S-u_j)+O(\varepsilon).}
\]
In particular the **vertex set** converges to samples of a parabola under the anisotropic mapping \((x,y)\mapsto(x,y/\sqrt\varepsilon)\). The whole polygon converges in Hausdorff distance to the **piecewise-linear** polygon joining these sampled points, not to the entire curved parabolic segment. The errors are uniform on each compact set of positive short-side vectors, for fixed \(n\).

## Assumptions and scope
Assume \(n\ge5\), each \(b_i>0\), and \(0<\varepsilon<\varepsilon_0(b)\). The polygon is the convex, non-self-intersecting cyclic one, unique up to rigid motion and reflection by the classical existence-and-uniqueness theorem for feasible side lengths. For sufficiently small \(\varepsilon\), the side \(S-\varepsilon\) is the unique longest and subtends the unique major circular arc. No assertion is made for arbitrary slack far from the boundary. The side lengths have physical length units, so \(H\) has length-cubed units and each formula is dimensionally consistent.

## Proof
**1. Exact scalar closure.** Write \(t=(2R_\varepsilon)^{-1}\). For the short edges define their positive minor central gaps by \(\delta_i=2\arcsin(b_it)\). Let \(\Delta=\sum_i\delta_i\). For the shallow convex polygon, \(\Delta<\pi\), whereas the opposite long edge subtends the complementary major arc. Therefore the exact closure equation is
\[
S-\varepsilon=\frac{\sin(\sum_i\arcsin(b_it))}{t}.
\]
The right side is an even real-analytic function of \(t\) in a neighborhood of zero (the singularity at zero is removable). Taylor expansion of \(\arcsin z=z+z^3/6+O(z^5)\) and \(\sin z=z-z^3/6+O(z^5)\) yields
\[
\varepsilon=\frac H6t^2+O(t^4).
\]
Because \(H>0\), the inverse function theorem in the variable \(v=t^2\) supplies a unique positive branch \(v(\varepsilon)=6\varepsilon/H+O(\varepsilon^2)\), real-analytic at zero. The cited classical uniqueness theorem identifies this local branch with the globally unique convex cyclic polygon; no extra solutions are asserted or discarded merely by numerical root search. Hence \(R_\varepsilon=(2\sqrt v)^{-1}=\sqrt{H/(24\varepsilon)}(1+O(\varepsilon))\) and \(R_\varepsilon^{-2}=4v=24\varepsilon/H+O(\varepsilon^2)\).

**2. Exact area.** Since the long-edge contribution is subtracted from the short fan, the shoelace/circular-sector identity is
\[
A_\varepsilon=\frac{\sum_i\sin\delta_i-\sin\Delta}{8t^2}.
\]
Here \(\sum_i\sin\delta_i=2St-(\sum_i b_i^3)t^3+O(t^5)\), and \(\sin\Delta=2St+((\sum_i b_i^3)-4S^3)t^3/3+O(t^5)\). Thus \(A_\varepsilon=Ht/6+O(t^3)\), proving the stated area law. Moreover \(A_\varepsilon=tG(t^2)\), where \(G\) is analytic and \(G(0)=H/6\). Consequently \(A_\varepsilon^2=vG(v)^2\) is real-analytic in \(\varepsilon\), with derivative \(H/6\).

**3. All vertices and the limiting polygon.** Put \(\theta_j=\sum_{i\le j}\delta_i\), with \(\theta_0=0\). An exact circle parameterization in the chosen chord coordinates is
\[
x_j=\frac{\sin(\theta_j-\Delta/2)+\sin(\Delta/2)}{2t},\qquad
y_j=\frac{\cos(\theta_j-\Delta/2)-\cos(\Delta/2)}{2t}.
\]
Uniform Taylor expansion, using \(\theta_j=2u_jt+O(t^3)\) and \(\Delta=2St+O(t^3)\), gives \(x_j=u_j+O(t^2)\) and \(y_j=t\,u_j(S-u_j)+O(t^3)\). Substituting \(t/\sqrt\varepsilon=\sqrt{6/H}+O(\varepsilon)\) proves both coordinate estimates. The vertexwise limits imply convergence of the polygon edges and their convex hull in Hausdorff distance, because the number of vertices is fixed. Analytic remainders and \(H\) bounded away from zero establish uniformity on compact positive side-length sets.

## Verification
Run the independent numerical checker `check.py` under Python with SciPy: `python check.py`. It computes circumradii by solving the exact scalar chord equation, computes area independently from the shoelace formula on generated vertices, and checks the analytic area, radius, and all-vertex predictions for six side vectors of lengths three through eight and four decreasing slacks. The recorded output ends in `CYCLIC_BOUNDARY_PARABOLIC_CHECKS_OK`. Numerical tests illustrate but do not establish the infinite-parameter theorem; the proof is the uniform analytic calculation above.

## Relationship to prior work
The existence and uniqueness of the convex cyclic polygon with prescribed feasible lengths is the classical result reproved by Kouřimská, Skuppin and Springborn (first preprint 26 June 2015). Their published variational analysis addresses feasibility and uniqueness, including a boundary maximizer, rather than the explicit rate of circumradius blow-up, area-squared boundary derivative and anisotropic all-vertex limit established here. Connelly's 2009 treatment of Robbins' generalized Heron polynomials gives algebraic polynomial relations for area for arbitrary \(n\), not this explicit boundary branch, its derivative or its vertex geometry. For \(n=3,4\), the area coefficient can also be obtained by expanding the classical Heron and Brahmagupta formulas; those lower-dimensional special cases are not separately claimed as novel. This statement is restricted to \(n\ge5\). The comparison does not constitute an exhaustive historical priority determination.

## Limitations
The claim concerns the near-saturated single polygon inequality with all other edges positive and fixed, or uniformly bounded within a compact positive family. It does not give a finite-slack global area bound, stability for simultaneous collapse of several short sides, or asymptotics when \(n\) increases. The smooth parabola describes limiting **vertex positions**; for fixed finite \(n\) the polygonal edges remain straight. No independent expert audit or formal proof certification has been undertaken.

## References
1. H. Kouřimská, L. Skuppin, B. Springborn, *A variational principle for cyclic polygons with prescribed edge lengths*, arXiv:1506.08069, first posted 2015-06-26. https://arxiv.org/abs/1506.08069
2. R. Connelly, *Comments on generalized Heron polynomials and Robbins' conjectures*, Discrete Mathematics 309 (2009), 4192–4196; online 2009-01-10. https://connellytensegrity.com/pdf/10.1016_j.disc.2008.10.031.pdf
3. D. P. Robbins, *Areas of Polygons Inscribed in a Circle*, American Mathematical Monthly 102 (1995), 523–530. https://doi.org/10.1080/00029890.1995.12004612
