# Scientific review: four-generator zonotope circumradius equality

## Correctness — PASS

The claim is exact for all full-dimensional sums of at most four line segments in Euclidean three-space. A sign orientation of the unique generator dependence puts the origin inside their tetrahedral convex hull, so the Shephard determinant sum is a single tetrahedral determinant. Three balanced signed sums transform the volume determinant by a factor of four. Their half-sums belong to the centered zonotope, and Hadamard's inequality proves the sharp bound. Equality in both inequalities forces three perpendicular equal-length balanced sums. Inversion produces the regular-simplex vectors plus an arbitrary common shift; the remaining signed sums give exactly the stated ball constraints. The origin-in-tetrahedron condition gives precisely the four linear inequalities. Both necessity and sufficiency, including boundary cases, are established. The nonregular witness is checked with rational arithmetic and its unequal generator lengths distinguish it from the regular polyhedron.

A standalone verification script checks all sixteen signed half-sums, the tetrahedral determinant identity after kernel-sign orientation, an exact rational witness, and 4,000 additional rational examples. These finite tests support but do not replace the universal argument. No unproved analytic lemma is used beyond elementary determinant identities, Hadamard's inequality and the classical zonotope-volume decomposition, which is also reconstructible from a tetrahedral partition.

## Originality — PASS (historical priority provisional)

Joós and Lángi, *Isoperimetric problems for zonotopes* (arXiv:2206.03204; 2022), prove the sharp circumradius bound and expressly ask in Problem 1 whether equality forces regularity. Section 3.2 **already constructs small common shifts** of regular-simplex generators preserving circumradius in odd dimension, as part of a different fixed-mean-width problem. That construction is prior art and is not claimed as original here. The new claim is stronger: an exhaustive necessary-and-sufficient equality characterization for *all* spatial four-generator zonotopes, with a closed finite-inequality description of the entire three-parameter family and exact treatment of boundary configurations. In the inspected full text, the authors do not give that characterization or resolve their stated uniqueness problem.

Lángi's *An isoperimetric problem for three-dimensional parallelohedra* (arXiv:2102.11621) proves a mean-width minimization, not the equality family for fixed volume and circumradius. Bezdek's complete six-page *On Rhombic Dodecahedra* (2000) proves inradius-normalized bounds on intrinsic volumes, not this fixed-circumradius equality classification. The closest semantic research records concern vertex-transitive zonotope radii, inradius under Makeev constraints, or lattice rhombohedra; their hypotheses or invariants do not dominate this result. An unindexed equivalent equality classification and the possibility that a source author has communicated the immediate nonuniqueness observation elsewhere remain historical-priority risks. The searches do not establish priority by themselves.

## Mathematical value — PASS

The classification settles the exact equality class of a sharp natural extremal invariant of four-generator spatial zonotopes. It converts a published regularity-uniqueness question into a complete, explicit feasible set of geometric deformations. The resulting family has an open three-dimensional set of noncongruent nonregular minimizers and distinguishes combinatorially generic minimizers from boundary degenerations. Its significance is the global all-equality classification, **not** mere application of the known inequality to one perturbed example.

## Limits

The analysis does not classify higher-dimensional equality sets or zonotopes requiring five or more generators. It does not produce a stability inequality or a unique fundamental domain for the finite symmetry actions on the feasible parameter set. Historical priority is provisional, and the exact claim has not been assessed by an independent mathematician.

Self-review: passed. Independent audit: not yet performed.
