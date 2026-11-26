# Independent mathematical audit

## correctness

PASS

Final claim re-audited in repairs/1/RESULT.md, with the theorem unchanged. The frozen proof said every support triple with two deleted indices supplies two relative 4-simplices; for example, at (p,q,t)=(2,3,2) only the vertex b_3 is available for index 3 and there is only one. The repair accounts for either one or two columns and proves a unit minor in both cases. Outside the complete-bipartite forest complex Q only shapes (2,2), (2,3) and (3,2) can occur by the six-vertex edge bounds. For the two larger shapes at least two matching edges must be missing by the forest edge bound, and then deleting those two edges leaves a tree. Inclusion–exclusion yields c_3=t(p−1)(q−1)−binom(t,2) and c_4=binom(t,2)(p+q−4). For two matched labels plus one unmatched label each projected column has two unit entries, in disjoint rows if both unmatched vertices exist. For three matched labels a projected row is indexed by omitting a_i,b_j for i≠j; the incidence graph of the six columns is a six-cycle. Orienting by the formal 5-simplex boundary gives a unit rank-five tree minor and the single six-term kernel generator, which vanishes under the full differential as well. Thus the projected image is primitive, the projection is injective on the full image, and the full image is the graph of an integral map on a primitive summand. The relative connecting homomorphism takes the tetrahedra containing a fixed missing pair to the tensor basis of H_2(Q) from the bipartite four-cycles, giving the stated free homology. At t=0, Q is two contractible complexes joined along the simplicial graph K_{p,q} and hence has the asserted suspension type. At t≥1 the complete two-skeleton and vanishing H_2 give two-connectivity. A map from a wedge of 3-spheres induces an isomorphism on H_3 and π_3; its mapping cylinder pair is 3-connected. Relative Hurewicz and the pair exact sequences then show that H_4 is spherical, giving the claimed wedge by homological Whitehead. This includes t=1 (contractible), and the t=3, p=q=3 case, with no 3-sphere. The repair also credits the known isolated two-deletion example and clarifies the verification limits.

## originality

PASS

For the repaired statement the distinct content is the uniform integral types for general partial matching defects and rectangular shores, not the cited intact, one-edge, or full balanced endpoints or the isolated known K_{3,3} two-deletion example. The strongest inspected same-object sources give exact face counts for the whole family but no matching uniform homotopy theorem. The nearby dissociation and cut claims are about different complexes.

## value

PASS

The partial deletions give a natural missing range between the complete-bipartite and crown calculations and include all rectangular shores, not a hand-picked slice. The exact phase change from degree two to contractibility to degree-three and degree-four wedges, and the uniform multiplicity and torsion exclusion, go beyond the enumerator and give a usable classification of these forest complexes. The rectangular block repair preserves that contribution and does not rely on any claimed equivariant or persistence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
