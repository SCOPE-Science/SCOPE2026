# Independent mathematical audit

## correctness

PASS

Cai et al.'s Type-A characterization applies because two distinct equal-weight words differ in at least two positions. It also has a direct proof here: with first/last differences L<R, any common read made by deleting at i in x and j in y with i<j must satisfy i≤L<R≤j and y_m=x_{m+1} for i≤m<j. Before L both words agree, so x_i through x_L are constant and all alignments of this orientation give the same read. The other orientation similarly gives at most one. Both are needed for two distinct reads, and together force opposing alternating phases throughout [L,R]; conversely the two end alignments of such an interval give distinct reads. Fixed weight forces an even length 2t, and the one-position sum changes by ±t with 1≤t≤r, hence separates every edge modulo r+1. The proposed r+1 words have opposite phases on exactly the indicated even interval for each pair; complementing and padding cover unbalanced layers and r=0 is a singleton. The base five words have the cyclic pair intersection sizes 2 and the other five intersection sizes 0; padding preserves the differing interval, so the induced obstruction persists in every stated layer. An independent enumerator compared the interval criterion, residue and actual distinct deletion sets for 32,587 pairs through n=9 and computed all ten witness intersections (`python3 /workspace/review_checks.py 4`). The general proof does not depend on the finite census.

## originality

PASS

The binary alternating-block criterion, inversion/VT mechanism, and alternating-block clique structures are established ingredients, not new here. The evidence supports the exact full-layer proper partition with matching lower bound, together with the induced odd-hole phenomenon. Closest same-graph indexed records concern degrees and edges, unrestricted cliques, or maximum individual code size. The near-parallel Dyck result has a different vertex constraint and does not give the assigned full-layer invariant.

## value

PASS

The fixed-composition layer is a natural channel class and the minimum number of jointly reconstructible codebooks is a concrete partition cost; neither a bound on just one codebook nor edge enumeration answers it. A simple optimal syndrome and explicit sharp obstruction cover every composition, while the embedded C₅ shows that the equality is not explained by perfection. This gives a precise graph/coding distinction rather than an isolated finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
