# Review of the uniform triple-partition dimension theorem

**Correctness.** The VC upper bound uses all-positive realizability plus within-triple transitivity and shows every purported larger support forces a negative query to be positive. The lower support has an explicit partition for each labeling using the unqueried reserve triple. For online dimension, the all-positive branch of a putative deeper tree becomes unique, and a second support has two realizing partitions for every trace, permitting a leaf-dependent final query. The \(m=1\) boundary is addressed. A standalone full enumeration for \(m\le3\) and direct recursion for online depths \(m=2,3\), together with a twelve-vertex strong-trace test, corroborate the proof.

**Originality.** The nearest directly related established result, Bressan et al. (2019), Theorem 6, treats all partitions with unrestricted block sizes and proves VC dimension \(n-1\), but contains no result for uniform triples or their online mistake dimension. Liu–Mukherjee (2021/2022) treats partition identification rather than Littlestone mistakes and neither fixes every block size nor supplies these formulas. The vector-space zero-set family of Guingona et al. (2021) is structurally different. Searches for equal-block equivalence relations, uniform 3-partitions, co-membership shattering, and adaptive dimensions found no statement covering the joint theorem. Historical priority remains uncertain, especially under unfamiliar terminology.

**Value.** The bounded-block-size requirement is substantive: unlike arbitrary partitions, the class has a sharp static–adaptive gap at every nontrivial order. The strong-trace construction explains the gap and gives a reusable structural tool for comparing constrained partitions, rather than a finite numerical recomputation. No inference about the complexities of noisy or exact-identification learning is claimed.

**Limits.** Verification is independent code rather than independent mathematical review; larger block sizes are not resolved. Sources and comparisons are documented in the accompanying result and structured audit.

Self-review: passed. Independent audit: not yet performed.
