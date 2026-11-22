# Scientific review

## Correctness

**PASS.** The pivotal forced-block lemma is reconstructed from the two aligned phase pointers: immediately after the first kept symbol, the deleted track expects that same symbol, forcing the next \(q-1\) original letters to remain. Repeating yields exactly \(m\) rotation blocks. The minimal nonnegative increments reconstruct a valid interleaving whenever their sum does not exceed \(qk\); a bijection with \(m\) bounded digits establishes the count and sharp saturation threshold. Empty-word boundaries and the fixed-alphabet normal limit are separately addressed. Two independent programs verify the full finite residual sets and the counting formula.

## Originality

**PASS within checked evidence.** The primary complement-scattered-factor paper gives general algorithms, singleton properties, and shuffle relations rather than the q-ary multi-deletion exact phase language. Previously published alternating-binary results cover only \(q=2\); the existing permutation-power result covers only one removed copy, \(k=1\). The new claim addresses the joint range \(q\ge3\), \(k\ge2\) with a precise new structural criterion and exact all-parameter count, not merely a relabeling. The embedding-multiplicity result concerns a different conditional statistic. Full texts of the two published binary results and of the embedding-multiplicity result were inspected. Risk: older unindexed shuffle-quotient enumerations might subsume the statement; global uniqueness is not certified.

## Value

**PASS.** Fixed-pattern complement deletion is a natural inverse-shuffle channel, and prescribing a repeated permutation is a canonical structured test family. The result settles every deletion budget and survivor length over every alphabet size, exhibiting a sharp complete-support boundary and an exact random-digit transition law. The scope is mathematically motivated rather than an arbitrary finite slice; elementary coefficient extraction alone is not the contribution, which depends on the forced-block characterization.

## Limitations and comparison

The proof requires pairwise distinct letters per period, and the normal limit assumes a fixed alphabet. The work does not settle general complement sets or arbitrary shuffle instances. The original 2026 paper's Sections 3–5, the two binary alternating papers, the complete existing one-copy permutation-power theorem, and the cyclic permutation embedding-multiplicity paper were compared by mathematical implication; no checked statement supplies the joint \(q\ge3,k\ge2\) classification. Earlier unindexed equivalents remain possible, and independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
