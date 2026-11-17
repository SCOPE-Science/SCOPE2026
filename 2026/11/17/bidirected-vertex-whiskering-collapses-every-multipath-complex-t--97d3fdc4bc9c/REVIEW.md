# Scientific review: bidirected vertex-whiskering collapse

## Correctness — PASS

For every legal face with a nonempty core-arrow subset, the selected core arrows are a disjoint union of directed paths. A terminal vertex has exactly one compatible pendant arrow in its two-direction whisker. This gives a perfect pairing in the fiber over each core multipath. Sorting core subsets by decreasing size and sorting lower faces of each fiber by decreasing size makes each paired lower face a genuine free face, because competing core cofaces lie in previously removed fibers and competing pendant cofaces were already removed in the same fiber. All core-bearing simplices disappear, leaving the join of discrete pendant pairs, the boundary of a cross-polytope. The n=1 and empty-core-arrow cases are included. The proof is infinite-parameter and does not infer it from finite tests. The standalone verifier checks 24 diverse finite digraphs, reconstructs 34,838 augmented faces, and independently replays 15,622 elementary free-face pairs.

## Originality — PASS (best-knowledge, subject to bibliographic risk)

The closest full-text comparison is Caputi–Collari–Smith's 2026 work on multipath complexes of **bare bidirected polygons** and specified attachments (arXiv:2601.05670v1). A complete published result on coherently directed sunlets has **one** oriented pendant arrow per core vertex, hence a ball/sphere dichotomy rather than our two-arrow-per-leaf cross-polytope. A complete published result on bidirected **once-subdivided forests** has a similar sphere target, but its domain excludes arbitrary cyclic cores and its sphere dimension counts original edges. Neither covers the present arbitrary directed core plus full bidirectional whiskers, even by straightforward implication. Earlier accessible claims about only a single cycle whisker or vertex-subset complexes have different inputs. Searches included equivalent formulations, stronger-coverage searches, exact recorded-results searches, and implication comparisons, documented with identifiers in `AUDIT.json`. Unindexed equivalent literature is possible; no independent priority audit has occurred.

## Mathematical value — PASS

The conclusion identifies a universal, highly nontrivial simplification under a natural graph decoration: an arbitrary core multipath complex, possibly with elaborate high-dimensional topology, becomes a **single integral sphere** of a dimension depending only on the number of core vertices. The constructive elementary collapses and the automorphism sign action add topology and naturality beyond a numerical invariant. Unlike known singly oriented sunlets, the two opposing leaf orientations are essential and create a stable cross-polytope core. This is a structural all-graph classification, not an arbitrary finite example.

## Limitations and verification state

Requires one distinct leaf at every core vertex, both opposing pendant arcs and no directed cycles in legal multipaths. Does not cover looped digraphs, arbitrary partial leaf additions, or different definitions of arrow-complex faces. The collapse sequence is not asserted equivariant. Independent mathematical validation and independent bibliographic audit are not performed. Verification checks are finite corroboration of the written proof.

Self-review: passed. Independent audit: not yet performed.
