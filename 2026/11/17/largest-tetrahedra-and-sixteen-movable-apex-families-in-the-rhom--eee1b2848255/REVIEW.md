# Independent mathematical audit

## correctness

PASS

Any tetra inside the convex hull has its absolute volume maximized at polytope vertices by successively maximizing a convex absolute-affine determinant in each chosen corner; thus 24 choose 4=10,626 vertex quadruples are exhaustive for the maximum. Inspected actual CHECK.py exact Z[sqrt2] pair arithmetic, SPECTRUM.csv and source RESULT.md; independently enumerated all 10,626 determinant values with a separate quadratic-integer determinant implementation: exactly 23 absolute levels, maximum 32+20sqrt2 with multiplicity 48. For every signed (±1,±1,±1) face normal, a triangle with support L+2 has two maximizing base triples whose three signed determinants agree, hence any apex in the face by affine interpolation is optimal; independent reconstruction yields 16 face/base families and their coverage of all 48 vertex-maximal tetrahedra. Orthogonal face pyramid areas give polytope volume (96+80sqrt2)/3 and exact occupancy (1+5sqrt2)/56. Explicitly does NOT claim classification of every nonvertex maximizer.

## originality

PASS

Best-knowledge PASS. The inspected Steininger–Yurkevich 2021/2022 Rupert-problem primary preprint lists the rhombicuboctahedron coordinate model but asks about projection containment, not the largest inscribed tetrahedron, multiplicity spectrum or movable-apex extremizers. Searched similar Archimedean solids and different rhombic solids: 48-vertex truncated cuboctahedron, 24-vertex snub cube and 32-vertex rhombic triacontahedron are distinct. No exact same 24-vertex determinant spectrum/maximizer publication found, but uncatalogued finite-tetrahedron databases remain a priority risk.

## value

PASS

Maximum inscribed simplex volume is a natural affine-geometric invariant; exact 48 vertex optimizers and full 23-level spectrum plus continuous maximal families display meaningful rigidity/flexibility structure in a standard Archimedean solid. A self-contained exact finite classification is valuable despite not covering all nonvertex equality cases or generalizing all polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
