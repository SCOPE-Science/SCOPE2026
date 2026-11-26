# Independent mathematical audit

## correctness

PASS

For a point at coordinate t on edge xy the distance from vertex v is min(d(v,x)+t,d(v,y)+1−t). Write the radius as s+δ, s integral. When δ<1/2 the farther endpoint cannot contribute via vertices at distance s there, and vertices within s−1 there are within s of the other endpoint. Hence distance-s vertex balls generate. When 1/2≤δ<1 the allowed vertices belong to the union of the two distance-s balls, and the midpoint realizes that whole union. At scale 3 the unions are exactly V minus an off-diagonal cross pair. This is the join of two simplex boundaries with only the interiors of the n diagonal facets omitted: each codimension-one face of an omitted facet is also in an off-diagonal facet. The pair (J,K) has n relative d-cells, d=2n−3≥3; the coherent fundamental cycle maps to the primitive diagonal. The long exact sequence gives free homology only in degree d−1, and relative cellular connectivity, Hurewicz and homological Whitehead give the wedge, not just its Betti numbers. Model the join sphere in the direct sum of two standard (n−1)-dimensional permutation hyperplanes: the diagonal permutation has determinant +1; the factor swap has determinant (−1)^(n−1). This twists the coherent relative facet permutation and descends to the stated integral quotient and traces. The quotient's S_n coinvariants are Z/n rather than zero for the augmentation sublattice (all ordered differences have the same coinvariant class and e_i−e_k=(e_i−e_j)+(e_j−e_k)). At scale 4 the distance-two balls miss only the matched partner, giving the simplicial boundary; at scale 5 a midpoint sees all vertices, giving a simplex. This checks n=3 and the real half-open endpoints. The wedge is nonequivariant. The finite Python tests are not needed for these integral or all-order conclusions.

## originality

PASS

The known graph Čech generator lemma and established non-cover construction are inputs, not new. The exact specialization at scale three, notably the homotopy and integral module of the crown's non-cover complex, survives the comparisons. The closest same-graph result concerns scale two; the closest full-filtration result assumes intact complete bipartite adjacency and gives a different scale-three complex.

## value

PASS

Removing a matching from an intact complete bipartite graph changes a contractible stage into a highly connected sphere wedge with a nontrivial integral permutation quotient. This is a complete and uniform comparison for a natural sparse graph defect, and the integral answer contains information not captured by just the character or wedge multiplicity. The next two stages put the exception in the filtration without claiming a calculation of the earlier inclusion maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
