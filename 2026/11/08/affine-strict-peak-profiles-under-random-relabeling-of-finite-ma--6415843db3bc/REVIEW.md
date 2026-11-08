# Scientific review: affine strict-peak profiles under random relabeling

## Correctness — PASS

The statement quantifies over every function \(f:[n]\to[n]\), \(n\ge4\), and every interior position. The proof splits unordered source triples into exactly one, two, or three distinct images. One-image triples never generate strict peaks. Two-image triples generate the sole positional dependence, with the two source-image incidence motifs generating opposite slopes. Injective triples away from invariant three-sets contribute \(1/3\); invariant permutations on three-sets produce the exact fixed-point and directed 3-cycle corrections. All cases rely only on uniform relative order, not asymptotics. The standalone exhaustive/sampled checker gives `VERIFY_OK 10603 exact assertions`. The chief proof-sensitive point is that the three original source labels occupy consecutive positions; that is incorporated explicitly.

## Originality — PASS, qualified

Compared against Leckey–Wormald (2018, arXiv:1803.02667) on fixed-indegree random mapping six-length, Mutafchiev–Finch (2023, arXiv:2301.13829) on deepest random-mapping cycles, Fulman–Kim–Lee (2019, arXiv:1902.00978) on peak laws in permutation conjugacy classes, and Gessel–Zhuang (2020, arXiv:2001.00654) on exact permutation peak/cycle-type generating functions. The last two give powerful covering results for bijective cases, which are not separately claimed novel. The new structural content is uniform over noninjective self-maps, with ties and two mixed coalescence motifs; this is not a consequence of the identified primary statements. An earlier general relabeling theorem could still imply this formula. Negative literature search is not proof of uniqueness.

## Value — PASS

The formula compresses every strict-peak location probability into an exact affine profile and classifies its increasing, constant, or decreasing direction using two intrinsic source/target configurations. It shows precisely what information comes from indegree collisions versus directed cycles. The problem is natural for order observations of randomly labeled functional digraphs, and the classification is stronger than a total-peak expectation or a finite enumeration.

## Limitations and priority risks

No joint peak distribution, map reconstruction, or independent mathematical audit is asserted. Prior permutation results are credited. Unlocated general labeling identities remain possible sources of stronger coverage.

Self-review: passed. Independent audit: not yet performed.
