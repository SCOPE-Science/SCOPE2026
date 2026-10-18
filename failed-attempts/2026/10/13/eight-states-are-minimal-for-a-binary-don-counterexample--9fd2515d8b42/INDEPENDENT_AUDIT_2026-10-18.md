# Independent mathematical audit

## correctness

PASS

Given the published full-cycle-letter necessity for binary complete reachability, choosing b(q)=q+1 mod n and enumerating all a:Q->Q is exhaustive. Reproduced with separately compiled C++ exact subset-image BFS for all n=2..8, including all 8^8=16,777,216 letter maps: completely reachable counts 2,18,128,1200,9936,105840,1093632 and violations 0 through n7, exactly 544 at n8. Every violating presentation has one six-element target at minimum distance17. Cyclic conjugation partitions 544 into 68 free size8 orbits. An independent Python BFS confirms every one of the 255 subsets reachable for the representative a=(0,0,3,5,1,2,6,7), unique violation S={0,1,2,4,5,6}, shortest witness abbbbbbabbbbbabbb of length17. Counting is finite but exhaustive after normalization, not an asymptotic inference.

## originality

FAIL

FAIL: Zhu’s original 2024 *Around Don’s conjecture for binary completely reachable automata* itself explicitly reports 8-state counterexamples and 68 nonisomorphic cases (Table 1, around pages 7–8), as well as Figure 1 8-state witness, in addition to constructing an infinite family at even n>=10. The submission incorrectly reads the analytic family lower cutoff as the prior known smallest counterexample; the sharp 8-state onset and the 68 classes were already published. The 544 presentations are exactly 68 cyclic-labeling copies because these rank-(n-1) cyclic maps have free rotation action. New single-subset/17-step details, even if not printed there, cannot restore the false claimed new sharp minimum.

## value

FAIL

FAIL: The mathematically motivating milestone—the first binary completely reachable Don counterexample at eight states and 68 classes—is an existing published result. Re-enumerating normalized labeled maps and tabulating the one-step overrun on already-classified examples has no substantiated distinct mathematical question or structural role sufficient to survive as an independent claim. Computational correctness alone is not value, and disclaimers cannot rescue the already-covered main result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
