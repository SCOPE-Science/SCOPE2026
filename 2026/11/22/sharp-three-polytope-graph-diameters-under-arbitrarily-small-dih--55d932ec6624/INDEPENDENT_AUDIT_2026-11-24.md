# Independent mathematical audit

## correctness

PASS

The existence and diameter claims hold for every fixed f≥4 and δ>0. The geometry can be checked directly from RESULT.md §1: choose R>4 large enough that arcsin(4/R)<δ. The projected initial three normals surround zero strictly (each successive angular gap, including the wraparound gap, is <π). With their positive vertical coordinates and the downward base normal they positively span in 3D. The three side planes at offset 1 and the base z=0 bound a full-dimensional tetrahedron. The normal recurrence follows from roots R and exp(±iθ); its positive coefficients express the new normal in the interior of the normal cone at the current top vertex. A sufficiently shallow cut removes just that vertex, creates a triangle, and preserves simplicity. Side facet neighbors have index difference at most three by induction. Their horizontal dot products for differences 1, 2, 3 are −1/R, 2/R²−1, 3/R−4/R³, respectively; the vertical contribution is ≤1/R², so the normalized dot products are <4/R, and base-side dihedrals are acute. For the graph, at k≥5 the new vertices U_k,W_k,T_k link to W_(k−1),U_(k−2),U_(k−1), respectively, with H differences 3; the replacement triangle has differences 1,1,2. The base tetrahedron and the two exceptional steps k=3,4 obey the same bound by direct substitution. Consequently the specified endpoints are at distance at least ceil((2k−1)/3). Every intermediate distance layer separating endpoints has at least three vertices by 3-connectivity. Euler and minimum degree three yield V≤2f−4 also for nonsimple polytopes, giving the matching universal upper bound. CHECKER.py was inspected, not executed; it checks finite graphs only and is not needed for the argument.

## originality

PASS

Pass for the simultaneous angle-constrained extremal diameter at every facet count and its explicit pair/height argument in the given chain, not for the realization in isolation or the classical diameter bound. Neither the comparison with those known ingredients nor the indexed candidates establishes prior coverage of the joint claim. This is a best-of-knowledge judgment with unresolved primary-source access risk.

## value

PASS

This resolves whether a stringent geometric restriction costs any graph diameter: it does not, even with arbitrarily small positive dihedral excess and at every facet count. The all-order Lipschitz potential certifies an explicit extremal pair without shortest-path searches and isolates the combinatorial reason the realization is sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
