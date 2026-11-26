# Independent mathematical audit

## correctness

PASS

The outward facet normals are the directed edge differences on seven nodes, with the fixed endpoint of each single-coordinate bound treated as ground. Their matrix is totally unimodular. I reproduced the finite face certificate without the supplied code: take all six-edge spanning trees of the grounded graph on the twelve labelled inequalities, propagate the tight differences from ground 0, discard infeasible points and deduplicate. This gives 40 vertices. For each mask of the twelve inequalities take its matching vertices, discard empty sets, and deduplicate by intersecting all active masks of its vertices. Graph rank (seven minus the number of components) of the resulting tight mask equals face codimension. This gives all faces, since each vertex arises from six independent active normals and every nonempty face is an intersection of the inequalities. All twelve single-facet masks occur; the face vector is (40,132,186,139,57,12,1). Active masks with more edges than rank give (16,28,16,3,0,0,0) singular orbits by face dimension; their inclusion-minimal masks are {2,3,7,8}, {8,9,11,12}, {4,5,9,10}. Here simplicial implies smooth by total unimodularity, so there is no lattice-index exception. The outer pair forces incompatible values of y₂. The two adjacent intersections are edges, one with only y₃ free on [1,2], one with only y₁ free on [3,4]. Common subfaces describe the orbit-closure intersections, and each edge gives a complete normal toric curve, hence P¹. For each maximal singular face the four normals satisfy v₁+v₂=v₃+v₄ in the displayed order, and any independent triple gives a basis of the rank-three saturated span by total unimodularity. In the cone basis of the proof the dual semigroup is {(x,y,z)≥0 : z≤x+y} on integers; its generators (1,0,0), (0,1,0), (1,0,1), (0,1,1) have the single sum relation pairing opposite generators. This gives the transverse node, with a torus factor at the associated orbit. The same nonsimplicial cones determine the non-Q-factorial locus.

## originality

FAIL

Batyrev–Ciocan-Fontanine–Kim–van Straten already prove for the partial-flag ladder toric degeneration that the singular locus has precisely the codimension-three orbit closures indexed by four-edge boxes, with ordinary double point transverse type. That is a stronger same-object result, not merely a face-count or a rule for testing individual cones. In the regular GL4 ladder its three boxes are exactly the four-facet sets in the finding. Pairwise incidence requires only substituting the forced equalities into the written inequalities. Simpliciality plus the known unimodularity of the remaining cones gives the non-Q-factorial assertion. The absence of the three frozen names or the printed GL4 incidence chain in the general theorem does not make this specialization materially distinct.

## value

FAIL

Reduced singular support of a natural toric degeneration is a useful invariant, but here the established theorem already provides each component and its generic local type. The only additional tabulation in the central claim is the immediate pairwise compatibility check for three known boxes: two pairs fix all but one free coordinate and the third is infeasible. Together with the standard normal-fan criterion for non-Q-factoriality this is a routine small-instance specialization, not a surviving substantial new classification. No intersection singularity or scheme calculation is supplied as an independent remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
