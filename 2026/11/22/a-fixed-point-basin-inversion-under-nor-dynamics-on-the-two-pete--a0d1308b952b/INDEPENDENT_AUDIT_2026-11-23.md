# Independent mathematical audit

## correctness

PASS

The precise graph scope is GP(10,2) and GP(10,3), not a classification of all Petersen covers. Reduction modulo five is locally bijective: the two inner neighbors map to distinct residues at offsets ±2, and the spoke and outer edges give the other required adjacencies. The symmetric-neighbor polarity gives S⊆F²(S) and F³=F; fixed sets are exactly independent sets dominating their complement. The largest cycle's stated basin is exactly the empty set plus total dominating sets, since F(S)=V forces S empty in a graph without isolated vertices and F(S)=∅ means the open neighborhoods of S cover V. An independent full Python census, replayable with python3 /workspace/branches/5b479397-3a7d-41f2-960e-07d992e52fa2/nor_census.py, uses subset-neighborhood-union recursion and forward walks with reverse path assignment, not the frozen peel or vectorized implementation. It classified 1,048,576 states per graph; fixed/cycle counts 295/19830 and 187/17391, depths {0:39955,1:1008621} and {0:34969,1:1013607}, fixed-basin populations 745 and 1941, two-cycle-basin populations 1047831 and 1046635, and maxima 35 and 388 agree. Its combined basin spectra agree bin by bin with the sums of the two period-specific spectra in the frozen files; subtracting the independently listed fixed-orbit basin populations recovers the two-cycle spectra, whose largest bins are unique at 156533 and 150545. The two Desargues shore masks are 0x556aa and 0xaa955. Directly in the disjoint-2-subsets Petersen representation, enumerating all subsets T of one shore and requiring each opposite 2-subset to have a disjoint member of T returns size counts 4:10, 5:72, 6:140, 7:110, 8:45, 9:10, 10:1, summing to 388. No frozen code was executed.

## originality

PASS

Best-of-knowledge pass for the specified NOR basin inversion and full spectra, not for the general fixed-point, cover, or short-orbit facts.

## value

PASS

The natural question is whether increased equilibrium multiplicity yields an increased probability of settling at equilibrium. Two natural covers with the same quotient, size, degree and one-update time ceiling show that it does not. The exact attraction distribution and 388-state shore fibers explain which configurations account for the disparity and provide useful benchmarks for dynamical comparisons; the finding is more than an isolated fixed-point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
