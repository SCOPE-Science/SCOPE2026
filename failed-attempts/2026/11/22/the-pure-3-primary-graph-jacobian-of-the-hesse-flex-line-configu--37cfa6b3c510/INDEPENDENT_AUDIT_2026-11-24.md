# Independent mathematical audit

## correctness

PASS

Take a flex as elliptic-curve origin. The flexes are E[3], and distinct triples are collinear exactly when their sum is zero; in (Z/3)^2 this is affine collinearity. There are 9 points, 12 lines and 36 incidences. BB^t=3I+J gives Laplacian factors t(t−7), (t−3)^3 and (t²−7t+9)^8, giving matrix-tree count 3^18. Independent exact replay: enumerate distinct triples of F₃² summing to zero, and add the outer product (e_p−e_l)(e_p−e_l)^t for each point–line incidence. Delete row and column 20 in lexicographic point/triple order; SymPy 1.14 smith_normal_form over ZZ gives 1^12,3,9^4,27^3, and exact determinant 387420489. The rectangular incidence matrix instead gives 1^6,3^3. Gluing rational components at distinct marks gives stability by minimum valency 3 and genus 36−21+1=16. For nodal curves the first-order map to local smoothing parameters is surjective and deformations are unobstructed; choose all node parameters nonzero to first order and algebraize the resulting polarized formal family over k[[t]]. This gives split uv=t local equations up to units and regular total space. The component group is the degree-zero multidegree lattice modulo the intersection lattice (matrix −L). The argument does not imply a degeneration of the initial smooth cubic.

## originality

FAIL

The indexed resolved Ceva nine-line net has the same abstract dual graph, states the same exact Smith group, and gives the same thickness-one component-group application. This is material equivalent coverage, not a coincidentally equal group. The two records share a date, which does not establish priority. The Hesse description of the graph does not change the invariant, and choosing different marked points on the rational components does not change the Néron component group under these hypotheses.

## value

FAIL

The integral Smith group would be a useful exact invariant of a canonical graph if not already available. The Ceva calculation supplies it for precisely the same graph and already applies it to a regular unit-thickness smoothing of the same dual-graph type. The different geometric label and standard auxiliary gluing add no independently useful unknown exact fact; the record explicitly makes no claim about a degeneration of the original cubic. No surviving substantive repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
