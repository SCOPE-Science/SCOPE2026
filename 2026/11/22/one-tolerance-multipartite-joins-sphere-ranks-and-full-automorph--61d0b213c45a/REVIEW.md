# Independent mathematical audit

## correctness

PASS

The face excess is the sum over parts of max(0, occupancy-1). The faces with their possible doubled part i form Xi, the complete-graph one-skeleton in part i joined to the other discrete sets. Distinct Xi intersect exactly in K. The inclusion of the discrete set in its connected graph is nullhomotopic; joining the homotopy makes the inclusion of K factor up to homotopy through a contractible cone on the remaining factors. At each successive union both maps from K are thus null, the inclusions are cofibrations, and the homotopy pushout adds Xi and one suspension of K as wedge summands. The connectedness needed for this splitting holds even at r=2. A complete graph on a_i vertices has circle rank binomial(a_i-1,2), zero for a_i=2; combining its join contribution with the r-1 suspensions gives the stated integer B. For the trace, a fixed face is a union of vertex cycles. On a length-ell orbit of parts the at-most-one-per-part choices are empty or a vertex cycle of length ell, of which there are f_O. The unique doubled part must be individually fixed; inside it the pair is two fixed points or one transposition. The reduced alternating contribution of a fixed oriented simplex with k vertex cycles is (-1)^(k-1), including -1 for the empty face; hence the formula, without dividing by any 1-f_O or assuming equal sizes. In the all-size-two case each Xi is contractible, and in the exact sequence of (X,K) the relative groups identify naturally with the copies of H_(r-1)(K) indexed by the parts; their boundary is the sum. K is the boundary sphere of the cross-polytope, so its orientation character is the determinant of the signed permutation of the coordinate axes. The augmentation kernel therefore gives the claimed integral lattice, not merely the same trace. CHECK.py and VERIFICATION.md were inspected, not executed: the five test group orders are 48, 384, 144, 1296 and 576, for 2448 trace checks; the modular boundary checks are not used to infer the integral homotopy or module statement.

## originality

PASS

The supported refinement is the explicit full-group trace including exchanges of equal-sized parts, with an integral description when all sizes are two. Identification with a matroid elongation and the ordinary top-dimensional wedge are prior consequences; the product multiplicity is a direct exact evaluation rather than a new structural matroid theorem.

## value

PASS

The first nontrivial tolerance extension of the ordinary multipartite join is a natural structured test family. A compact trace formula for the whole automorphism group resolves the missing information about part exchanges, allowing direct invariant-subspace and representation calculations beyond the known non-equivariant wedge. The all-size-two lattice also distinguishes the actual integral action from its trace. The bare wedge deduction alone would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
