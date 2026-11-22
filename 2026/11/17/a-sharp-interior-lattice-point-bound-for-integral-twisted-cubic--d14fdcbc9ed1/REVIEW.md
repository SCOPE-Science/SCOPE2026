# Independent mathematical audit

## correctness

PASS

The claim applies to any finite T⊂Z with at least four distinct integer parameters, in the standard (t,t²,t³) monomial lattice Z³, span L=maxT−minT≥3. Integer translation is a triangular unimodular change of lattice coordinates. For four ordered vertices with positive integer gaps x,y,z, the Vandermonde tetrahedral volume is V=xyz(x+y)(y+z)(x+y+z)/6, and projected (t,t²) quadrilateral area is A=(x+y)(x+z)(y+z)/2. From Fu Liu’s established dimension-three integral cyclic-polytope Ehrhart coefficients E(m)=1+Lm+Am²+Vm³, reciprocity yields I=V−A+L−1. Direct independent SymPy reconstruction gives a 48-term nonnegative integer polynomial D=6[I−2*binom(L−1,3)] after x=u+1,y=v+1,z=w+1, with v-independent part uw(positive polynomial) and every coefficient of v¹,...,v⁴ strictly positive. Thus I≥2 binom(L−1,3) for all positive gaps and equality exactly y=1 and (x=1 or z=1). Taking any four vertices of arbitrary T containing both endpoints gives an inscribed tetrahedron, whose interior integer points are interior to C3(T), proving the all-cardinality lower bound; hollowness forces L=3 and four consecutive parameters. The checker’s exact barycentric enumeration for seven small tetrahedra supplements the global polynomial certificate, not substitutes for it. Equalities for >4 vertices are deliberately not classified.

## originality

PASS

Fu Liu’s exact Ehrhart coefficient formula is prior and expressly used, not rediscovered. Accessible original arXiv:math/0409337 Theorem 1.2 provides coefficient data and general integral moment-curve theory but not the fixed-span extremal minimization, two endpoint-cluster minimizers, or global hollow classification in the inspected result. Konoike’s 2026 zonotope averaging and general lattice-free polyhedron results have broader objects but do not provide a displayed implication of the exact fixed-span bound. Resultary semantic search located the assigned current record, not an earlier exact table. Original full-text access to Konoike beyond abstract was limited; a lawful arXiv full-text request was unavailable and subsequent authorized institutional retrieval reported VPN disconnected, with no bypass/retry. Material inspected and this residual priority risk are explicit.

## value

PASS

Interior lattice-point count and hollowness are canonical invariants of the integral cyclic three-polytope family. A sharp uniform lower bound at fixed parameter span with fully determined tetrahedral equality configurations and all-cardinality hollow classification solves a naturally motivated infinite discrete extremal problem; it is not merely a finite table or restatement of Ehrhart coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
