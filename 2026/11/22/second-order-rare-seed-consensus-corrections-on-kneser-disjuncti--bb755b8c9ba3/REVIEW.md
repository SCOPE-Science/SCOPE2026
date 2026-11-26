# Independent mathematical audit

## correctness

PASS

For every pair of Kneser vertices, including repeated endpoints, a common neighbor exists since n≥3k. Thus every nonempty state reaches all one by step two; the empty state remains empty and all-one is absorbing. One-step coverage is equivalent to the absence of a transversal of size at most k, since such a transversal can be extended to exactly k. Up to k seeds always have one; k+1 seeds have one iff they intersect in some pair. In an independent ordered draw of k+1 ordered k-sets, the disjointness probability is (n)_{k(k+1)}/(n)_k^{k+1}; conditioning on distinct seeds multiplies by 1+O(n^{-k}). Subtracting the first and second sums of falling-factorial log terms gives log D=−A/n−(B+A²/2)/n²+O(n^{-3}), with the asserted signs after exponentiating. For k+2 seeds, use independent ordered draws without repetition within each seed. A fixed admissible equality pattern of codimension d on the k(k+2) coordinate slots has probability O(n^{-d}) (match its blocks to distinct ground points). With at most two lost distinct points there is either one triple block or two double blocks; the saving of two transversal picks requires a triple from distinct seeds or two double blocks on four different seeds. With double blocks sharing a seed, even choosing both block points saves at most one. These exact patterns are disjoint and each has probability n^{-2}+O(n^{-3}), from the falling-factorial count; conditioning away repeated entire seeds again costs O(n^{-k}). Independent small symbolic/count checks recovered (A,B,C)=(54,−1215,1485) and (160,−11600,12800) for k=3,4, with the respective triple/pair split (270,1215), (1280,11520). For M≥k+3 and failure, some ground k-set is hit by at least k+3 selected seeds. Its hit-family has O(n^{k−1}) possible seeds, so the (k+3)th binomial factorial-moment bound gives O(n^{-k-3}) per transversal candidate and O(n^{-3}) overall. The finite collection of fixed-count binomial masses differs from the Poisson masses by O(1/N); this also controls the baseline tail via its complement. Subtract p^N, negligible in the expansion, to distinguish first hitting from all-one at t=1. This proves the normalization and the stated uniform-in-n remainder for fixed k,λ.

## originality

PASS

Best-of-knowledge pass for the quantitative first-hit expansion, not for OR-network propagation or deterministic minimum total domination. The nearest theorem gives the eventual k+1/disjoint threshold; the nearest exact polynomial covers rank two only; and the distinct same-day Johnson record treats a different adjacency and regime. The new content is the second-order rare-seed correction, including the k+2 transversal obstruction coefficient and the control needed to mix over all larger families.

## value

PASS

In a natural bounded-time OR process on a standard family, the rare-seed approximation quantifies when one update suffices rather than two. The first two correction orders resolve a deterministic threshold, a disjointness penalty, and two non-equivalent multi-seed collision mechanisms; the second-order term cannot be read off the minimum total domination number. The explicit coefficient and all-sizes remainder are useful for finite-size comparison at fixed rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
