# Independent mathematical audit

## correctness

PASS

The explicit five rational vertices form a 3D triangular bipyramid with six facets: (0,1,2),(0,1,3),(0,2,3),(1,2,4),(1,3,4),(2,3,4), each checked as supporting plane via exact rational determinant signs in the source CHECK.py. At x1=L t, Minkowski section of one t=0 segment and one t=1 triangle has A(t)=4epsilon t-(10epsilon/3)t^2, integral 8epsilon/9 and interior axial CDF F_I(t)=9t^2/4-5t^3/4, giving Gini g_I=39/140. The six facet area law yields boundary F_B(t)=alpha t+beta t^2 below t=1 and an end-face atom; exact area-square bounds imply 0.019<alpha<0.021, 0.979<beta<0.982 and Gini g_B<1347243/5000000. Axial projection plus transverse diameter <2001/1000 establishes Δ(K)-θ(K) > 1000[39/140-1347243/5000000-2001/1000000]=31158/4375>7.12. The argument uses *normalized* volume and surface laws in ambient Euclidean metric, with no unjustified inference from one-dimensional strict inequality. The script implements exact rational determinant, squared-area and Gini certificates, not Monte Carlo; the analytic comparison justifies the strict spatial mean inequality.

## originality

PASS

The primary August 2026 Shen paper supplies a six-vertex stretched convex-body counterexample and the longitudinal Gini method. The present five-vertex *triangular* end section differs combinatorially from the six-vertex rectangle and changes the volume slice polynomial and facet-weighted boundary axial distribution. Existence at six vertices does not entail existence at five by removing a vertex because both normalized measures change, so this explicit rational five-vertex certificate is a genuine further refinement on inspected prior statements. A centrally symmetric 3D polytope cannot have only five vertices, so centrally symmetric constructions do not dominate this claim. No minimality of five among all polytopes is asserted.

## value

PASS

Reducing the explicit spatial counterexample from six vertices to five reaches the simplest nonsimplicial combinatorial class in three dimensions: a triangular bipyramid with all facets triangles. The result establishes failure of the conjectured volume/surface distance comparison with a transparent exact rational witness at a meaningful geometric boundary, not a tiny arbitrary numeric optimization. It does NOT establish optimality versus tetrahedra and need not do so to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
