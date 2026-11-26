# Independent mathematical audit

## correctness

PASS

I independently reconstructed the three generalized Petersen graphs and enumerated all labelled subsets. For each root s, I intersected the masks of all incoming shortest-path extensions at each BFS vertex v: forced(s,v) = intersection over predecessors u of (forced(s,u) union {uv}). Every shortest path to v has exactly one such final edge, so this gives the precise pair mask without edge deletion or path multiplicity. The union over selected pairs and the single-deletion test are exact by monotonicity. All six coefficient vectors, the three independence numbers (4,8,10), and the optimum structures agree. The Desargues shores are distinguished by outer index parity reversed on the inner ring. Both covers project via index reduction mod 5, since inner steps 2 and 3 project to 2 and -2. Incremental union-find on all monitoring states counted the complete component multisets at every cap from the minimum to the first connected cap (8,11,15), not merely the immediately preceding caps. In particular, caps 7,10,14 give 15,2007,101 components, respectively. Replay: /workspace/reviews/replay_meg.py and replay_meg.txt. I inspected the frozen checkers and recorded outputs; the new enumeration is independent of executing them.

## originality

PASS

Pass for the complete all-set and inclusion-minimal spectra and the all-state add/delete capacity comparison, not as a priority claim for each constituent. A distinct same-day record already contains the exact dodecahedral minimum census and its two induced shapes. Neither the date nor the absence of matching literature numbers establishes priority for those facts. The previously known independent octets are also excluded from the originality credit.

## value

PASS

The dodecahedral and Desargues graphs are natural covers of the same small benchmark, but their monitoring statistics and their valid-intermediate spare costs differ markedly. The census distinguishes minimum from inclusion-minimal placements and quantifies a genuine obstacle to relocation: at the cap immediately below connectivity, configurations can be isolated exclusively because deletions fail and additions exceed capacity. These exact all-state data and the strict dodecahedral separation from the vertex-cover construction are useful finite benchmarks, not an assertion of cover monotonicity or of a result for arbitrary GP parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
