# Independent mathematical audit

## correctness

PASS

The sink stabilizer in S_5 has exactly the two stated nonsink orbits, so fixed representatives suffice; the polynomials are not averaged over source choices. The reduced Laplacian has determinant 2000 (equivalently, the nonzero full Laplacian eigenvalues are 2 with multiplicity five and 5 with multiplicity four, and the tree count is 2^5 5^4/10). An independent exact replay computed the determinant by Bareiss and found all 2000 recurrent states by the orbit of the nine addition maps from the all-two recurrent state, a different enumeration from the uploaded scripts' tests of all stable states. The replay checks the burning inequality at the seed, legal stabilization, and conservation; addition preserves recurrence, and the orbit count equals the entire recurrent count. Adding at {2,3} and {0,2} then recovered every one of the 14 near and 30 far cells, including zero avalanches and the six (24,6) events (no masses 20–23); the reproduced CSV matches byte for byte, SHA-256 2c719d3d02fac224e9245c81f79600d913ff6cbb2ce71907aa55c8ace582bf21. The common branch replay path is /workspace/branches/f3fc71e7-5020-49c0-bfec-83e723b506b7/replay_petersen.py (run without arguments for the full check); the output there is REPRODUCED_JOINT_COUNTS.csv. The two supplied programs and frozen table were read, not executed. Marginal sums agree, including the palindrome of the positive near masses and mean mass 3 or 4 and mean loss 1. Analytically, all-two is recurrent by connectedness and monotonicity makes its odometer an upper bound for every stable configuration. From all-two the first wave reaches all nonsinks; the source is then stable if near. If the source is far, each further wave reaches all six far vertices along their induced 6-cycle. In wave two each of the three near vertices starts at height one, receives two grains and topples once, ending at zero. In wave three each receives only two and does not topple; the far source now stabilizes. Thus the sharp odometers are all ones for near and 2 on near, 3 on far for a far addition, giving the claimed 9 and 24. Stationary conservation gives mean loss one independently, and the two-shell reduced Poisson equations verify the mean masses. The correctness conclusion is for this finite graph, these sources and total individual topplings, not the number of distinct toppled sites.

## originality

PASS

The contribution is the complete joint source-orbit census of individual topplings and sink loss on Petersen (including the verified exceptional tail), not the general sandpile machinery, recurrent count, Green-function means or the previously understood full-avalanche event. The retrieved papers and catalog comparisons supply frameworks and other hosts, but did not establish an explicit two-orbit Petersen law or a host-specific theorem determining these coefficients without a new census.

## value

PASS

Petersen is a canonical symmetric cubic graph with exactly two physically meaningful source positions relative to a sink. Joint mass/loss is needed to distinguish interior redistribution from dissipation, and total topplings distinguish repeated waves from a footprint. The same graph exhibits an exact 9-versus-24 change in worst-case activity with the two source classes, plus an exceptional far tail and side-by-side joint distributions; neither a determinant nor a response function resolves those. The census is a precise benchmark for source-conditioned algorithms and avalanche identities, not an arbitrary slice or a claimed universal law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
