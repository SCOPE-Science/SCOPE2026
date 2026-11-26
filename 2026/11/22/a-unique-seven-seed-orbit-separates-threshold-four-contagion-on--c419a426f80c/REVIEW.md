# Independent mathematical audit

## correctness

PASS

The synchronous threshold-four rule on either six-regular graph deletes precisely the inactive vertices of residual degree at most two. A nonempty induced minimum-degree-three subset can never peel; if peeling stalls, its nonempty residual is such a subset. Successful seeds are an up-set, so all single deletions failing is necessary and sufficient for inclusion-minimality. An independent exact reproduction enumerated all 65,536 masks on each graph, finding nonpercolation by enumerating minimum-degree-three subsets and propagating containment, and cross-checking every mask by a FIFO activation-time recurrence. Shrikhande yields (6,3):96, (6,4):336, (6,5):1152, (6,6):576, (7,3):64, total 2224; the rook graph yields (6,3):288, (6,5):576, total 864. No others occur. Exact degree-signature and seven-set comparisons reproduce both claims, including the witness activation layers. Independent adjacency-preserving permutation enumeration returns 192 Shrikhande automorphisms and the same 64-set orbit. The twelve linear maps in the frozen certificate are invertible because their images contain the generating difference set; their translations therefore give 192 distinct automorphisms, so the reproduced orbit is also their affine orbit. Degree six and common-neighbor count two give the same adjacency spectrum (6, 2, -2 with multiplicities 1, 6, 9); rook neighborhoods are two disjoint triangles, whereas Shrikhande neighborhoods are cycles of length six. Replay: python3 /workspace/reproductions/graph_census.py. Both frozen checkers were inspected, not executed.

## originality

PASS

Best of current knowledge: pass the complete inclusion-minimal size/time separation and the exact 64-set orbit and induced-degree characterization. Neither the definition, the three-core reduction nor the rook minimum of six is new. The verified prior theorem proves the rook minimum but does not count minimal seeds or constrain their full geometry or timing. No exact prior census is established; search gaps remain.

## value

PASS

This natural strongly regular graph pair has matching parameters and spectrum, and even matches on minimum contagious cardinality at this threshold. The upper size of an inclusion-minimal contagious set is nevertheless different; the exact completion-time census and a complete affine-orbit characterization identify precisely how. This gives a concrete invariant and a reusable benchmark for finite bootstrap or core-deletion arguments, not merely another computation of the known rook minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
