# Independent mathematical audit

## correctness

PASS

When the linear part of u is nonzero, M_u(1) has a nonzero linear part and supplies exactly one dimension beyond the edge-space image of B_a. For v outside S an edge into S forces y_v=0; all other outside coordinates are free. Inside S rescale y_i=a_i t_i. The remaining equations t_i+t_j=0 give one degree of freedom per connected component in characteristic two, and per bipartite component otherwise. Since degree three vanishes and the surviving edge monomials are independent, u² is nonzero exactly in odd characteristic when S contains an edge; M_{u²} then has rank one. This proves both rank formulas and gives the stated 3-, 2-, and 1-block counts for a cube-zero map. Each support has q^m(q-1)^|S| elements; pure quadratic elements contribute rank zero only at zero, rank one elsewhere. The empty graph yields the constant 1, and singleton support gives rank 1+degree. Over F2 the nonempty support counts before weighting by 16 are 1,6,8 at ranks 2,3,4 for the paw, and 6,9 at ranks 3,4 for C4. Independently constructed small matrices for six graph-field cases over F2, F3 and F4 matched the three-variable counts over 6,604 elements. The frozen verification files were inspected, not executed; the general replay is RESULT.md Proof lines 41–60 and exact counting by support, not a finite computation.

## originality

FAIL

The main finite-field rank stratification is explicitly covered by Resultary d37be33201da on the same algebra, with the same contribution per nonempty support, even in characteristic two. The additional formal variable for square rank is not stated in that record, but is obtained mechanically for each already-enumerated support by the independent edge-basis terms of u²; the Jordan conversion then takes only the standard cube-zero block identities. There is no substantial distinct census beyond the existing supportwise count and this direct decoration. This is a coverage/implication decision, not a claim that the earlier record printed the joint polynomial or its paw table.

## value

FAIL

An elementwise Jordan census is a natural invariant, but here the remaining square-rank distinction is an immediate edge-in-support test for already-counted strata. The degree read-off and four-vertex examples are exact but routine substitutions, with no independent structural payoff beyond the established finite-field rank census. Narrowing to the extra variable would not rescue a nonmechanical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
