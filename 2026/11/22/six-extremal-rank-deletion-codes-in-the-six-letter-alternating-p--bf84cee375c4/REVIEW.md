# Scientific review

## Correctness — PASS
The specified finite model reduces exactly to independent sets in a 61-vertex, 480-edge confusability graph. A complete source and deck enumeration is reconstructed in an embedded standalone checker. Both pairwise deck intersection and a separate inverse-insertion construction produce the collision graph. Exhaustive, unpruned Bron–Kerbosch traversal of the compatibility graph yields exactly 33,202 maximal cliques with sizes 6–11, including exactly six of size 11. Every independent set extends to a maximal one, proving both the extremum and the six equality cases; the latter are checked directly. The intersection of seven and involution orbits are computed directly, with explicit lists. Risk: finite computation rather than a short closed-form argument; mitigated by complete inspectable code and two collision constructions.

## Originality — PASS (qualified)
The 2014 Gabrys–Yaakobi–Farnoud–Sala–Bruck–Dolecek paper presents the rank-deletion model, the deletion/insertion equivalence, the signature-pair VT construction, and asymptotic unrestricted bounds. Its Construction 1 already supplies an 11-word lower-bound class when restricted to the prescribed signature; this is explicitly credited. Its stated results do not imply the sharp constrained upper bound, exactly six equality codebooks, seven-word common intersection, or five reverse-complement orbits. Searches of published research records for alternating permutation deletion code capacities, zigzag one-deletion corrections, and standardized-deletion optima found results on related but different models, not those four finite claims. Full source was inspected, not merely its title. Risk: an unindexed or inaccessible finite table may supply equivalent counts; no independent literature audit has been done.

## Mathematical value — PASS
This gives the exact zero-error constrained deletion capacity at a natural nontrivial Euler-zigzag source size and a surprisingly rigid classification of every optimizer. Seven of the eleven words are forced in all maximum codebooks, and only six codebooks attain a bound whose mere feasibility was already furnished by a general code construction. Equality structure and sharp constrained optimality address questions not answered by a generic lower bound. Scope is deliberately finite and does not purport to cover other block lengths.

## Closest literature and limits
Gabrys et al., *Single-Deletion-Correcting Codes over Permutations* (2014), DOI:10.1109/ISIT.2014.6875337, is the main direct comparison. The existing construction's size-11 lower bound is not claimed as new. The analysis is for strict up-down length-six rank permutation reads only, and an unindexed finite classification remains a historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
