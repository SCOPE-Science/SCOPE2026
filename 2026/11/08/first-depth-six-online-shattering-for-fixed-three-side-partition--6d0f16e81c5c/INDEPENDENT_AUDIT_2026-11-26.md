# Independent mathematical audit

## correctness

PASS

The independent check of the frozen depth6_tree.json verified the 63 internal queries (8 distinct pairs) and every one of the 64 distinct triple witnesses on its full path. Thus depth 6 is attained. Each concept follows a unique path: 84 concepts exclude depth 7; at most 56 for 4≤n≤8 exclude depth 6, including the complementary-block duplication at n=6. Restricting queries to the original nine vertices with all added vertices in the larger block proves persistence, not an upper bound for n>9. For static shattering, a five-edge star realizes every pattern: choose ≤3 negative leaves without the center, or when there are ≥4 negatives choose the center and the ≤1 positive leaf. The three unused vertices complete the triple. A six-edge support containing a cycle fails by transitivity; otherwise it is a forest with three components. Fixing XOR labels on a tree determines the vertex bipartition up to reversal, so the allowed triple sizes are componentwise sums of the two side sizes. The seven supplied obstructions for the seven partitions of 9 into three positive parts all exclude 3; e.g. (1,3,5) gives {0,1}+{0,3}+{1,4} and (2,3,4) gives {0,2}+{0,3}+{2}. Hence VC=5, independently of the adaptive witness.

## originality

PASS

Only the online depth-six threshold for the three-versus-rest bipartitions is credited as distinct. The static dimension is a corollary of an existing exact criterion for the same class, not a new result. The frozen record explicitly identifies the sharp online threshold as its contribution. The nearby online examples use a different profile or different query domain and do not supply the depth-six lower bound on this class.

## value

PASS

Three is a natural fixed block size, and pair queries are the usual adjacency observations of a partition. The exact first order attaining depth six shows that the information bound on shattering can be achieved by the adaptive oracle before fixed supports achieve that depth. The explicit small tree provides a benchmark for future fixed-size online classifications. The static corollary is useful context for the gap, not independently credited as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
