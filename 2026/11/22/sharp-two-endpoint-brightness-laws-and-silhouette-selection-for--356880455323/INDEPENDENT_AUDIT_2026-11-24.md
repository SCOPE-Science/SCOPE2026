# Independent mathematical audit

## correctness

PASS

Cauchy's projection identity halves the facet sum and cancels that factor against opposite pairs, in units of one pentagonal face area. Independent signed-Gram counting with pair products +/-1/sqrt(5) gives the four norm levels and multiplicities 12,20,20,12; the 12 face normals have support value 1+sqrt(5) and their fivefold symmetry aligns the signed gradient, exhausting the top level. A positive spherical linear form is strictly concave along chamber arcs, including edges, so minima can occur only at crossings. Every triple of unit normals has positive Gram determinant 2/5 +/- 2/(5 sqrt(5)), so the crossings give 15 distinct antipodal pairs. Icosahedral symmetry (a fivefold stabilizer cycles the other axes) is transitive on pairs; at the representative e_x the value is 2(1+phi)/R and this axis goes through the edge midpoint (1/phi,0,0). Above the second-largest norm the upper event is precisely the union of the twelve face-normal caps. The squared radius-cosine at the stated gap is q_+^2/b_+^2>4/5, placing each cap inside its ten-sided chamber and below half the minimum separation; summing cap areas yields 6 epsilon/b_+ over the specified interval. The statement does not require that this interval exclude its endpoint: by continuity the law also holds there. Scaled cap coordinates have asymptotically constant density on the stated disk. Near a cross axis the exact tangent chart expression is b_- sqrt(1-r^2)+L(theta)r with L(theta)=(2/R) max(|cos theta|,phi |sin theta|). L is bounded below; the small sublevel radius is uniformly epsilon/L+b_- epsilon^2/(2 L^3)+O(epsilon^3). Spherical radial area is r^2/2+O(r^4), and integrating L^-4 over a quadrant, split at arctan(1/phi), gives (4/(3 (2/R)^4))(phi^-1+phi^-3). Multiplication by 4 times 30/(4 pi) gives the cubic coefficient; the leading rectangle has area sqrt(5). Compactness localizes to the 30 neighborhoods, with equal weights by symmetry and uniform limiting rectangle measure in the rescaled chart. A sign pattern contributes N=15-H silhouette edges, where H is the integer signed pair interaction, because adjacent signed facets disagree in front/back sign exactly for the two edge incidences per discordant pair of axes. At e_x the equal-sign choices on the two vanishing products yield 12 edges and the opposite-sign choices 10. The two sign lines cut equal triangles from the limiting rectangle, proving the split. Independent finite signed-Gram count and constants are replayable with python3 /workspace/review_checks/brightness.py. The frozen verifier was read, not run; its quadrature and finite orientation checks do not replace the analytic argument.

## originality

PASS

Best current evidence supports the endpoint probability analysis, particularly the cubic correction and joint local angular/silhouette conclusions. The exact cap interval is a close use of previously studied chamber geometry, not a new projection identity or novel endpoint brightness values. Distinct same-day analogues do not have the same solid/observable, and the same-solid prior moments do not supply the lower expansion, or the combined endpoint laws.

## value

PASS

For a standard convex solid and an isotropic viewing distribution, the result quantitatively distinguishes rare dim and bright shadows: different exponents, an exact nonzero upper regime, a computable lower correction, and distinct limiting direction shapes and silhouette types. These are precise motivated conditional geometric invariants rather than new names for known extrema or a recalculation of a central moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
