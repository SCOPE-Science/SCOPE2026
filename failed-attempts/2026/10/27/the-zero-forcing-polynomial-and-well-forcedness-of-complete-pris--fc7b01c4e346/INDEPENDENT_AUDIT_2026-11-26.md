# Independent mathematical audit

## correctness

PASS

A blue vertex in a layer with u whites has u white clique neighbors plus its mate if white. A full layer can force every missing mate; two incomplete layers with at least two whites each are stuck. With just one white a_j on one side and at least two on the other, a first force exists exactly when some initially blue b_i has i!=j, and that force fills all of A. With one white on each side, n>=3 gives a blue matched pair avoiding both white indices. Counting the disjoint regimes gives each term (subtract the duplicate all-blue set; the boundary with only one blue on the sparse side contributes 2n(n-1)z^n). The minimum sets are the full layers and the indicated near-layer sets, and every successful set contains one by keeping a full layer or just one usable mate in the sparse side. At n=3 the interior sum vanishes and the coefficients in degrees 3,4,5,6 are 14,15,6,1. Summing the general coefficients gives 2(n+1)2^n-n^2-6n-1; division by 4^n gives the uniform probability. The bundled bounded script was inspected, not run; no finite census is needed for the proof.

## originality

FAIL

The prior general rook-graph forest classification covers this graph exactly, already gives its full enumerator by coefficient extraction and its minimum-set count, and specializes mechanically to the frozen regimes, compact polynomial and well-forced conclusion. A second distinct indexed finding states the compact formula explicitly; its later catalogue date is not evidence of earlier priority. The conclusion is coverage, not an attribution of derivation or authorship.

## value

FAIL

The graph, standard forcing invariant and exact probability are natural, but the frozen two-row result contributes only a routine evaluation of the covered criterion and enumerator. Even the well-forced statement follows by retaining an isolated column (or isolated row) while extending the white set. No distinct structural fact or nonroutine new consequence survives the comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
