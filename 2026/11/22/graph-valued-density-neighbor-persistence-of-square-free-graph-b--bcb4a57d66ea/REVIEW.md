# Independent mathematical audit

## correctness

PASS

For support in one fiber the witness count is s_j. For support meeting distinct fibers, any two common base witnesses would give a four-cycle, so the witnesses are either absent or exactly one complete fiber of weight w_i. Thus the active fiber simplices and neighbor-union simplices cover exactly the required complex. The nonempty intersections are full simplices, and an intersection of at least two distinct neighbor-union simplices is a single fiber, whose vertex in the nerve is active since s_j>=w_i for each incident active center. Pair each nerve face on at least two centers with the face augmented by that unique fiber index. Removing these pairs in decreasing center count leaves no competing coface and gives a collapse onto the stated incidence graph. For naturality, use the poset of (nonempty face, nonempty set of active cover indices containing it), ordered by face inclusion and reverse index-set inclusion. The lower fiber over a face contracts by adjoining any fixed active cover index containing that face, then keeping only that index and enlarging to the face. The lower fiber over a nerve face in the opposite face poset contracts by dropping extra indices and enlarging to the full nonempty intersection. Both projections are natural in the threshold, and so are the graph-to-nerve inclusions; their levelwise equivalences give the asserted zigzag, including empty stages. For each graph inclusion, projecting the later integral cycle group onto the new-edge coordinates has the earlier cycle group as kernel. Its image is free, proving primitivity and splitting; extending spanning forests gives compatible cycle births. The component and Euler-characteristic formulas and the empty-space convention are consistent. Independent direct face enumeration and mod-two boundary reduction on the two-triangle heterogeneous example reproduced H1 ranks 0,1,3 at thresholds 3,2,1, and at unit-weight C4 gave ordinary Betti pairs (2,0) for the complex and (2,2) for the incidence graph. Replay: /workspace/branches/f2e9cad4-af06-4dc6-9fc1-9f1a03499984/independent_check.py, with independent_check_output.txt in the same directory. These finite tests do not check integral persistence; the poset and graph arguments do. The frozen checker and recorded output were inspected, not rerun.

## originality

PASS

The supported distinct claim is the explicit naturally filtered graph model at all positive thresholds for heterogeneous blowups of arbitrary C4-free bases, and the integral persistence consequences. The underlying multineighbor construction and ordinary graph-like neighborhood phenomena are antecedents, not new claims. No inspected stronger result supplies the same weighted filtration and its maps.

## value

PASS

The result replaces potentially exponentially many faces of a blowup by a graph on at most twice the base vertex count across the entire density filtration. It preserves inclusion maps, hence computes the actual integral persistence and both barcodes by graph algorithms; replacing levelwise ranks alone would not have achieved that. The heterogeneous example exhibits genuine multi-stage cycle birth, and the C4 control delineates the hypothesis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
