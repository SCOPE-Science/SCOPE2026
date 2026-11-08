# Review of the exact quadratic detour theorem

## Correctness
**PASS.** The maximum-separation lemma is valid for all classical \(231\)-avoiders. First crossings of the maximum force each smaller-value pair to exchange its order twice; each such exchange is a different adjacent transposition, yielding the quadratic lower bound. Rightmost-descent sorting preserves avoidance and yields the matching upper bound. The proof explicitly handles all \(n\ge2\), possible backtracking, and distinguishes unrestricted from constrained metrics. Exhaustive finite implementations using different generation algorithms agree through order \(12\); these computations do not replace the proof.

## Originality
**PASS, with historical-priority risk.** The nearest Gray-code paper (Dukes et al., arXiv:0704.2048) uses Hamming difference or multi-position generation moves, not exact legal single-adjacent-swap distance. Drake (DOI:10.37236/4000) studies restricted weak order, whose covers can jump over elements absent from the avoidance class. Hyatt--Remmel (arXiv:1208.1052) provides related decomposition and enumeration, not the constrained metric. Published results on bipermutation reversal and adjacent-swap permutation codes concern different vertex sets, permitted moves, and metrics. The reviewed candidate is an exact intrinsic-versus-ambient distance for an explicit infinite pair, not a new Catalan enumeration or a whole-graph diameter formula. A differently phrased historical occurrence is possible.

## Value
**PASS.** The finding exhibits an unbounded intrinsic-versus-ambient metric distortion in a natural, classically studied Catalan family. The linear ordinary transformation must be rerouted into a quadratic legal path, and the proof isolates the order constraint causing every smaller-value pair to switch twice. This informs geodesic reconfiguration and is not implied by Gray-code adjacency bounds, ordinary inversion distance, or enumerative identities. The all-order statement is structurally motivated rather than an arbitrary finite slice.

## Limitations
The graph diameter and all-pairs distances are not determined. Historical priority is not independently certified; the check is limited to materially inspected sources and indexed searches.

Self-review: passed. Independent audit: not yet performed.
