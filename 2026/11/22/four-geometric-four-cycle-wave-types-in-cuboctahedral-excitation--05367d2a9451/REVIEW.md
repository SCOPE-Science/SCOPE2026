# Independent mathematical audit

## correctness

PASS

I independently reconstructed the full map on 531441 labelled states using disjoint excited/refractory masks. Iterated images of the entire state set descend until stabilization at the tenth image. On that image the map is a finite surjection, hence a permutation, and every cycle lies in every image. Traversing this permutation and propagating first-entry layers via the successor array reproduced every cell of the original joint table, including 480 depth-ten states and least witness 3856. The recurrent counts are 1, 40740, and 192 at periods 1, 3, and 4. The eight star triangles recover the underlying cube (there are no cube triangles and all pairwise-intersecting triple edges have a common endpoint). A cube symmetry is fixed by the image of 0 and the permutation of its three incident directions; hence exactly the 48 coordinate permutations/translations are needed. Testing those permutations on all phases of each cycle gives 319 geometric classes at period three. At period four the four (representative, class size) pairs are (14,24), (637,6), (1169,12), and (1358,6), with the middle two giving distinct orbits having three excitable-state-1 sites at every phase. The proof uses exact exhaustion of the fixed finite state space, not tests of sample initial states.

## originality

PASS

The rule and automorphism group are known, and exact censuses of related graphs are prior art. The closest same-graph catalogue match other than this record uses threshold two instead of one. The strongest inspected general theories classify qualitative behaviour, not the exact basin and symmetry-resolved populations. No independent covering result was identified within the checks below.

## value

PASS

An exact classification of a canonical Archimedean network with both triangular and square faces is a useful benchmark: even fixing the temporal period and per-phase excitation population does not fix the geometry. The two size-distinct geometric classes with a constant population of three are an exact example. The full entrance table and the ten-step cutoff distinguish basin structure from the periodic count and calibrate other state-space or symmetry-quotient methods. No graph-family generality is needed or claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
