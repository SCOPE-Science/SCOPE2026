# Independent mathematical audit

## correctness

PASS

For all n>=3 and 0<=i<=n-2, write a,b for the edited endpoints and p,q for their two common neighbors. A relative face must contain a,b and an old independent triple made non-independent by the new edge. In a first outward column only one new vertex is a nonneighbor of both endpoints; all the allowed extras lie among this vertex, its same-column mate, and p,q, yielding the seven listed faces. At later stages, either new vertex is a nonneighbor of both endpoints, so other extras must be either p,q or its two terminal neighbors (the new mate and its predecessor). Those neighbors cannot both occur because they are nonadjacent and share a nonneighbor in {a,b}; p,q cannot both occur with a later vertex. This gives the fifteen-face list, including when both wings exist by reversing columns and exchanging rails. The latest-column stage is order preserving. Within each stage every available p-toggle is paired first, so no downward p transition can undo an upward p move; remove those matched pairs for the cycle test and apply the same argument to each successive pivot. Exactly one critical 4-cell per new column remains. The relative CW attachment thus has n-2 four-cells. The old complex is a wedge of binom(n-1,2) 3-spheres by Filakovsky's Theorem 1. Its integral square-pair basis can independently be certified: for j<k evaluate a 3-cycle on the facet consisting of the upper rail edge from square j and the lower rail edge from square k. The facet's unique perfect matching is those two edges even when the squares touch; accordingly its coefficient is ±1 for that pair and 0 for the other pairs. The old complex has dimension at most three by bipartiteness, so these evaluations split the square-pair submodule, which already has full rank. The two new triangles form a chain t_i with boundary c_i; the oriented joins t_i∧c_j (overlapping terms are zero) lie in the modified complex and map to distinct members of that primitive basis. The relative boundary is therefore injective with precisely the claimed image; primitivity and Hurewicz identify the attaching maps up to an integral wedge basis change, leaving binom(n-2,2) spheres. This includes the contractible n=3 case.

## originality

PASS

The known grid homotopy type and primitive integral square-pair basis are starting data, not the new result. The all-position relative attachment and exact inclusion kernel for the nonbipartite perturbation are distinct from the strongest inspected comparisons. The exact catalogue match is the assigned record itself.

## value

PASS

One diagonal is the simplest local edit leaving the bipartite ladder regime. It kills a number of generators growing with the whole ladder, independently of edit position, and identifies the killed integral classes, not just a rank. This gives a controlled test case for how a nonbipartite edit changes robust clique complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
