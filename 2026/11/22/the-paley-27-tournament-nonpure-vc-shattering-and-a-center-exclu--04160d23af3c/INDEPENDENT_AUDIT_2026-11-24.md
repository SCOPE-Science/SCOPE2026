# Independent mathematical audit

## correctness

PASS

I recomputed the exact census with independent code. In the stated F_3 basis multiplication by u is the linear map (a,b,c)→(−c,a+c,b). The powers of u cycle through 26 nonzero elements; its even powers give Q. For each query vertex I constructed the bitset of positive centers. A support recursively partitions the full center set into the 2^k Boolean trace cells; ordinary shattering requires each cell be nonempty, and the off-support test clears the support bits in each cell first. Exhaustion through size four gave counts (1,27,351,2925,5967) and (1,27,351,2925,0), respectively. No support of size five or larger can be shattered since at most 27 distinct traces can occur. Orbit traversal by translations by 1,u,u², multiplication by u², and Frobenius generated all 22 four-support orbits with the recorded trace counts and representatives, including the seven ordinary orbits of sizes 1053 five times and 351 twice. I checked the listed witness centers and the unique in-support witness for mask 1. Deleting all triangles under the 5967 tetrahedra leaves exactly the orbit of (0,1,10), 351 triangles; each of 351 pairs occurs in exactly three of these. For homology I used coordinates for 2-cycles on just the triangles omitting 0: coefficients on triangles containing 0 are determined by the cycle equations on opposite edges, and the cone boundaries give a basis. Binary elimination in these 2600 cycle coordinates gives rank 2249. The full 2-skeleton has vanishing reduced homology below degree two, and there are no higher faces above degree three, so Betti numbers are 351 and 3718. Replay: python3 /workspace/reproductions/paley27.py.

## originality

PASS

The all-triples off-support constituent is covered by the exact prior outside-witness threshold. The supported distinct contribution is the quantified ordinary/off-support gap at size four, the exact ordinary census and orbits, and the associated nonpure incidence and mod-two homology. These are not implied by failure of universal four-query extension or by analogous computations at other fields.

## value

PASS

This is the first nonprime order congruent to three modulo four, a natural test for residue-translate VC phenomena outside prime fields. Exact enumeration gives a real change in extremal dimension upon excluding centers, and extreme ordinary supports leave a nonpure facet layer that is a balanced design. The mod-two ranks characterize the resulting finite complex beyond the dimension alone; this is a complete canonical incidence classification, not a handpicked support or another computation of the known triple threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
