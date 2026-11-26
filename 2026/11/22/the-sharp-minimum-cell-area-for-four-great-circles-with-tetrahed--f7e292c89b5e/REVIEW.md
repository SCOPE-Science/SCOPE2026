# Independent mathematical audit

## correctness

PASS

General position gives a unique dependence with no zero coefficients. Reorienting makes all its coefficients positive and puts the origin in the interior of the normal tetrahedron. The map to dot products identifies sign regions with the intersections of the dependence hyperplane and mixed orthants. A section of each such cone by setting the weighted sum of its positive coordinates to 1 is a product of two simplices (the negative sum is then -1). This gives exactly eight triangles and six quadrilaterals. The four projected tetrahedron facets F_i tile the sphere; in each one-versus-three cell the single opposite sign inequality is redundant, giving the polar triangle of F_i with angles pi minus the corresponding side lengths. Its area is 2pi minus the facet's spherical perimeter. Each facet is a nondegenerate triangle in an open hemisphere; its perimeter is strictly below 2pi by applying the triangle inequality through an antipode of its third vertex. In L'Huilier's formula at fixed semiperimeter, pair smoothing strictly increases the tangent product when the two coordinates differ: (X-C)/(X+C) increases with X=cos((x-y)/2) because C=cos((x+y)/2)>0. Thus only the equilateral triangle maximizes area at fixed perimeter. Its area is increasing in side length and is pi at alpha=arccos(-1/3). At least one projected facet has area >=pi, hence perimeter >=3alpha and polar area <=2pi-3alpha. Equality forces every facet perimeter <=3alpha and area <=pi, so all four areas equal pi and all facets are equilateral. The resulting Gram matrix determines the tetrahedral normals up to isometry. Conversely, tetrahedral symmetry makes the six quadrilaterals congruent, of area 4alpha-2pi, larger than the triangle area since alpha>4pi/7. This checks the bound, attainment, cell counts and all equality cases. RESULT.md lines 15–72 are decisive; the reconstruction checker was inspected, not run, and its tolerance-based sampling is not needed for any universal claim.

## originality

PASS

On the inspected evidence, credit only the unrestricted general-position maximin area value and tetrahedral rigidity. Previous or related calculations of the same tetrahedral cell areas do not optimize the smallest area over arbitrary arrangements. The inspected literature and catalogue claims do not give that optimization by a change of variable or immediate consequence.

## value

PASS

This is an exact low-order case of an existing natural extremal area function, not a chosen parameter slice to fit the example. The strict polar-facet obstruction proves both the sharp number and the unique optimizer; knowing just the tetrahedral example or a different extremal statistic would not answer either global question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
