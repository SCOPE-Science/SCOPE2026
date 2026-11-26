# Independent mathematical audit

## correctness

PASS

The 81-state trace counts each labelled cyclic assignment once, checks every zero for exactly one 2-neighbor and every positive vertex for positive support, and accumulates each column weight once. Independently, let z,o,p count labels 0,1,2. The total number of zero-to-2 incidences is z, and each 2 has at most two zero neighbors. Thus 3w−4n=o+2(2p−z). I assigned a different nonnegative local transition cost: one per 1 in the middle column, plus twice (# positive neighbors − 1) for each 2 in that column. These costs sum to exactly the same excess on closed walks. The independently constructed graph has 468 arcs, 49 of this alternative cost zero, exactly two cyclic zero components (simple cycles of lengths 3 and 6), and six cost-one arcs admitting zero-cost returns, all of closed length 5 mod 6. Exact arbitrary-precision counting in the cost-lifted graph matched H_{n,d} for d=0,1,2,4 and every formal 1≤n≤333. This is an all-order certificate: det(I−tB(0))=(1−t^3)(1−t^6)=D, deg [q^j] det(I−tB(q))≤81, and a term with k factors of positive q-degree in the log expansion contributes to D^{d+1}Φ_d a numerator of degree at most 81k+9(d+1−k)≤81d+9 after −t times differentiation. For d=0 the numerator is −tD'. The proposed series have the same denominator divisibility and degree bound. Agreement through 333 suffices, including the formal corrections at n=1,2 (not simple-prism evaluations). Since d≡−n mod 3, the smallest allowed costs with positive counts are 0,2,4,0,2,1 in residue order; cost 1 is excluded at n≡2 mod 6. This gives both rows of the claimed minimum/multiplicity function. In particular n=8 has weight 12 and 936 minimizers. The result counts labelled functions, not orbits. The frozen verifier's unsigned __int128 is a compiler extension, so its portability claim should be read as requiring a compiler providing that type; the arbitrary-precision reproduction does not rely on it.

## originality

PASS

The distinct supported claim is the exact six-residue cyclic-prism weight and optimum census, including the one-unit excess over the rounded cubic bound precisely at residue two. The closest verified exact enumerations change the graph, and the closest Cartesian-product paper changes the invariant. The underlying local transfer and cubic counting bound are not claimed as new.

## value

PASS

An exact optimum and its multiplicity answer different natural questions about a standard domination invariant on a standard cubic family. The cubic incidence bound alone misses an infinite residue family, and counting the large low-cost degeneracies cannot be inferred from the optimum. The six-residue weights and degree-zero through degree-four counts are useful benchmarks for extremal structure and counting algorithms, independent of applications or a full optimizer classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
