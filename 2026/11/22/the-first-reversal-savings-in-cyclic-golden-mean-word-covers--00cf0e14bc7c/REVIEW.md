# Independent mathematical audit

## correctness

PASS

Each host gives a closed walk of the same length in the directed admissible overlap graph, recording its classes on successive edges. Conversely a closed walk gives the periodic host spelled by the edge symbols; overlap and closure enforce all windows, including for walks shorter than the window length. The bit-mask BFS finds a shortest return to its start with all classes visited. Independently, python3 /workspace/branches/independent_finite.py circles (NumPy integer arrays) exhausts both versions for lengths at most 28: extend all linearly legal words one symbol at a time, discard exactly those with a forbidden wrap, and test modular windows against separate oriented and reversal masks. The oriented and reversal minima, respectively, are (3,6,10,17,28) and (3,6,10,17,23) for orders 2–6. The specified 23-symbol witness was directly checked. The extra order-one comparison in the reproduction ties, with minima 2 in both versions. There is no extrapolation beyond order six.

## originality

PASS

The oriented baseline and the general unoriented graph approach are prior; the sharp restricted reversal minima and first strict saving are not established by the inspected statements. The scope is internal admissibility of targets and cyclic admissibility of the host, with only reversal identifying targets.

## value

PASS

This is the first strict gain in a natural run-length-limited cyclic covering problem, not an isolated example. Knowing that four smaller orders admit no gain and that the first saving is exactly five positions gives a sharp benchmark for constrained reversal-cover constructions: counting reversal classes alone significantly underestimates the optimum. This finite comparison is useful without an all-order formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
