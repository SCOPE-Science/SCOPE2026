# Independent mathematical audit

## correctness

PASS

The length-n admissible words label the edges of a strongly connected balanced overlap digraph; append zeros to reach the zero vertex and then append the bits of any target. At a vertex of interior weight k the sole transition is forced and occurs in an Euler circuit. At weight less than k the choice is rotation or cross. All-rotation splits the edge set into necklace cycles. A switch at v transposes successors on the two rotation classes [0v],[1v]. Each tree edge joins two distinct current cycles, so spanning trees with a prescribed included or avoided edge realize respectively the cross or rotation pairing. If the edge is a bridge, switching elsewhere cannot move between the two sides in the decomposition into necklace classes, so the rotation pairing at that edge is impossible. For a weight-m necklace, downward edges are one-position orbits under its rotation stabilizer; there is a unique downward edge exactly when its primitive period contains one 1. Two downward edges give a detour via the connected lower layers, even for parallel edges. A unique downward edge at intermediate 2≤m<k is not a bridge: add a 1 immediately after an old 1 and delete that old 1, changing two cyclic gaps from d,d to d−1,d+1; deleting the new 1 from this modified necklace reaches the same lower neighbor. The all-zero necklace and the evenly spaced top layer when k divides n give exactly the stated bridges, coinciding for k=1. Each bridge forbids two rotation windows. Counting candidates by weight gives the displayed binomial formula. Independent brute enumeration of all binary successor permutations for each of the 15 pairs 1≤k≤n≤5 tested the union directly and matched the forbidden lists, including the two omissions 00 and 11 at n=k=1.

## originality

PASS

Existence, standard joining machinery, the unrestricted endpoint and the complete cycle parametrization for bound 2 are prior. The distinct claim is the uniform explicit classification of transitions over all weight bounds, in particular the nontrivial k<n divisibility condition in the general bound and the resulting closed support count. Known existence algorithms produce particular cycles; they do not classify which transitions can be forced or avoided over the family.

## value

PASS

It gives a complete local-extension criterion for a standard family of constrained universal cycles: aside from the base forced transitions, precisely an evenly spaced saturated configuration creates extra exclusions and only under a divisibility condition. The bridge certificate also gives a concrete construction of a cycle realizing any one allowed transition, not just a count or an assertion that some cycles exist. This resolves a natural extension question throughout the bounded-density range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
