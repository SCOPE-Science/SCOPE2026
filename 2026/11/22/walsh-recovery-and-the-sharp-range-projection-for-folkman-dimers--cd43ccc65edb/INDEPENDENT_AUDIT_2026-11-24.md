# Independent mathematical audit

## correctness

PASS

Each matching sends a base edge to the endpoint whose clone is matched, giving two incoming edges per vertex; within that orientation the two clone assignments at each of five vertices contribute a signed sum in {−2,0,2}, proving 32-divisibility. A vertex star flip gives a common minus sign, and the connected graph's star group has rank 19; fixing a spanning tree to positive signs covers every coset. Independent exact int64 replay python3 /workspace/review_checks/4.py (NumPy) uses clone-choice recursion instead of tournament assignments and a bit-tensor transform on both a different spanning tree and the specified BFS tree. It finds 768 matchings, reproduces the full reduced signed histogram in the BFS gauge and finds 1262164 zeros, 834988 nonzeros, least nonzero modulus 32 and maximum 768. The two gauges give common support-transform absolute sum 452160984. The full rank/nullity are these reduced counts times 2^19; there is no normalization factor in the convolution eigenvalues. The inverse transform of the support indicator vanishes off the orthogonal complement of the star group and its kernel ℓ¹ norm is 452160984/2^21. A convolution matrix's column and row absolute sums both equal this norm. Translation averaging of any projection onto the invariant range is again a projection onto that range (each conjugate is the identity there), cannot increase either norm, and gives the unique translation-invariant projection. The same argument holds over the reals since these characters are real. This establishes endpoint optimality, not just the norm of a selected projector.

## originality

PASS

Pass the Folkman-specific signed edge-incidence spectrum, divisibility/gap and exact optimal endpoint constant. The unsigned count 768 is positively identified in prior work and already credited by the original; the graph construction, Fourier diagonalization and averaging method are not novel. Other signed-matching computations show substantive methodological overlap, not the same spectral or projection result.

## value

PASS

The Folkman graph is a natural small semisymmetric test case and its doubled construction gives a local reason for strong Fourier divisibility. The rank and spectral floor quantify recoverable modes and ℓ² stability in the exact signed matching model, whereas the much larger sharp endpoint projection norm distinguishes a different functional-analytic cost. Even in a finite example that exact constant answers a natural optimization over all projections and cannot be recovered from matching-polynomial data or generic orbit averaging. This is a graph-specific result rather than novelty for the general Fourier method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
