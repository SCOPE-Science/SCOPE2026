# Independent mathematical audit

## correctness

PASS

Edge transpositions generate S₁₀ by connectivity; relabeling all tokens carries any start to identity and preserves moves. Every transposition changes parity and the fifteen different edges give distinct neighbors. I independently exhausted the metric using Python layer BFS with two five-symbol direct rank lookups and Floyd–Warshall for graph distances. It processed 3,628,800 distinct states with the exact 18 claimed shell counts, ending in the four strings 7895623401, 7895634012, 8956723401 and 8956734012. These give the stated rail swap with respective shifts independently 2 or 3 and 4·10!/2=7,257,600 unordered diametral pairs. I separately applied the explicit route and obtained the first string in 17 legal swaps. Each move reduces total displacement by at most two; the full census gives maximum ceiling-half deficit 4 at 1,440 states, and B=15 at each antipode. Both frozen C++ implementations were inspected: their different representations enumerate the same 15 neighbors, assign depths by FIFO and compute the correct transportation normalization. They were not executed. Independent replay: python3 /workspace/audit_replay/prism.py; output at /workspace/audit_replay/prism.txt.

## originality

PASS

No compared exact source supplies the pentagonal prism metric or the maximum transport deficit for its edge generators. Close matches were inspected for the Petersen graph and same-day open five-rung ladder and three-cube entries. Their graph, edge sets or number of vertices differ materially. Known Cayley graph arguments and BFS yield a method but not these specific shell counts or antipodes.

## value

PASS

The pentagonal prism is a canonical small non-tree cubic graph with two interacting rail cycles. Its full sequential-swap distribution and structured four extremizers are reusable benchmarks, not just an unexplained diameter constant. The worst transportation deficit and its multiplicity measure the accuracy of a standard lower bound on exactly this graph; notably, worst-gap placements are not the most distant placements. These exact facts are useful even without a formula for larger prisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
