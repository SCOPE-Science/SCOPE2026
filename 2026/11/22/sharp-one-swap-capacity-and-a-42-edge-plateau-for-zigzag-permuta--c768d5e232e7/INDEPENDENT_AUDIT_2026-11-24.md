# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/5/RESULT.md. Radius-one balls in the full adjacent-position Cayley graph intersect exactly at center distance ≤2. With the same sign string, one swap reverses a central sign, disjoint swaps leave such reversals unrepaired, and overlapping swaps rotate an alternating triple and reverse at least one comparison. For opposite orientations each swap affects at most three signs; chosen centers spaced by three cover all comparison indices with ceil((n−1)/3) swaps. At an interior center both outer labels must be strictly between the two swapped labels; endpoint conditions form a chain. The directed inequalities are acyclic because the local systems are glued successively at only one shared vertex. Topological ordering attains the bound for every n≥2. A fresh full graph census through n=8 using pair-order bit masks plus exact componentwise independent subset enumeration gave edge counts (0,1,4,10,22,42,42,0), capacities (1,1,2,5,16,80,502,2770), and maxima counts (1,2,2,4,9216,2^42,2^42,1). At six and seven it found the claimed matchings and 12/18/12 and 42 center counts. Separate exact calculations through n=7 and topological witnesses through n=100 are in /workspace/branches/dd7beb38-3a1a-492d-89eb-29e89342e185/. The frozen sentence calling eight the absolute first conflict-free length was false at n=1; the corrected RESULT.md and REVIEW.md specify n≥2 and keep the singleton. The frozen verify.py called int.bit_count() despite specifying Python 3.9; the supplied replacement uses bin(mask).count('1') on nonnegative masks, an equivalent size calculation in 3.9. The replacement's exact finite logic was inspected; the uploaded code was not run.

## originality

PASS

The supported distinct claim is the sharp minimum across opposite zigzag orientations, its nontrivial conflict-free threshold, and the small constrained-source graph census including the two matchings. The Euler numbers and metric coding criterion are not new. Neither the metric's standard formulations nor the most relevant inspected constrained coding and exchange graphs cover this result.

## value

PASS

For a classical constrained source, the threshold answers whether one-error correction requires removing any codewords; the two adjacent lengths below it exhibit a precise disjoint-conflict structure rather than just an edge total or a single code. The constructive sharp opposite-orientation bound and exact constrained optimum counts are independently useful benchmarks. No broader claim for unrestricted rank-modulation capacity or multiple swaps is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
