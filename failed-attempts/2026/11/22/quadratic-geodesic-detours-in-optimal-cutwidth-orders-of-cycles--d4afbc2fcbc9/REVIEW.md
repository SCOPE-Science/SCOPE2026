# Independent mathematical audit

## correctness

PASS

Each nonempty proper cycle subset has boundary size twice its number of cyclic components, and singleton cuts already have size 2. Thus feasible prefixes are cyclic intervals, with a root and n−2 independent end choices, then a forced last vertex. Only the intermediate prefix of a swap changes. At the first swap the root moves one step and the first bit flips, at the last the final bit flips, and internally precisely adjacent unequal bits may be exchanged. This also holds at n=3, when the two boundary swaps are distinct and there are no internal swaps. Degree is two plus the number of switches, so the binomial distribution and edge count follow. Particles can be moved right and removed, connecting each root layer, and first swaps connect the roots. For fixed equal roots, bringing the next target vertex left preserves connectivity: it is adjacent to the agreed prefix, contained in every changed prefix with that vertex inserted. Each such swap removes one Kendall inversion; every adjacent-swap path costs at least the Kendall distance. Between all-one states, equal interior occupancies force equal signed net flux F through every one of the n−1 interfaces, with F≡k modulo n because of the root change. This gives the lower bound (n−1)min(k,n−k); passing a vacancy across the word advances the root by one in n−1 swaps, and reversal of that path retreats by one. The unconstrained distance counts the k(n−k) inverted pairs between the two rotated blocks, yielding the claimed excess. Fresh permutation enumeration used explicit cycle-edge boundary sizes and BFS and confirmed the counts, connectivity, rotations and all root-zero pairs for 3≤n≤8 (root symmetry handles the other labels). This is finite corroboration, not an all-pairs or all-size numerical proof.

## originality

FAIL

The labelled optimum-cutwidth graph is exactly the established arc-permutation graph and a Yoke graph. More decisively, the sharp rotation-distance formula including the lower bound is an exact specialization of Jennings's distance lemmas. The uncredited overlap is not just a general relaxation bound or a superficially similar detour. The remaining elementary censuses and rooted isometry do not establish a distinct material result beyond that literature.

## value

FAIL

The cycle cutwidth viewpoint provides a useful interpretation of a familiar graph. However, the central sharp quadratic detour is a parameter specialization of a published metric reduction and exact distance calculation. The other quantities are the prior vertex count, simple switch counts from the published moves, and a standard fixed-prefix insertion argument. There is no demonstrated distinct valuable theorem left to repair in the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
