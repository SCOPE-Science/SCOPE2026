# Independent mathematical audit

## correctness

PASS

Deleting within a cyclic run gives one necklace. If two deletions produce the same necklace, their survivor alignment has an aligned ℓ-block crossing neither deletion seam since n−1>2ℓ. Under factor uniqueness this block starts at the same source position in both words. Read both lists from that position: between the two omitted sites they are offset by one, so equality forces every symbol from one omitted site to the other along that arc to agree. This proves run-exactness under uniqueness and the unconditional upper bound D≤2R. For factor equality at shift s, directed constraint edges are a subset of translation orbits; a cycle (including a duplicated edge for an orbit of size two) would require the whole orbit inside the interval of edge starts. The minimum arc span of such an orbit is n−gcd(n,s)≥n/2, impossible here. A v-vertex tree component contributes p^v+(1−p)^v≤(1−p)^(v−1), giving (1−p)^ℓ for the forest; conditioning independent Bernoulli(p) bits on exactly k ones gives the displayed denominator and the coupling bound. Rooting one of the r one-runs gives the two positive compositions and the n/r factor in the exact reference law. For each fixed j, the ordered disjoint edge collections give limiting factorial moment λ^j, and c<j path components give O(n^c(k/n)^(j+c))=o(1); the fixed-j cycle exception is absent for sufficiently large n. The chosen ℓ is o(n), and the error O(n^(−15/4)) multiplied by (2k)^2 still vanishes, so the first two moments of the bounded-at-each-n deficits transfer as well as the event of zero deficit. The result is for indexed sources, not uniform sampling of rotation classes. An independent bounded collision check over 110 admissible (n,k,ℓ) cases for 4≤n≤12 found agreement; the frozen verify.py was inspected but not executed. Neither finite check establishes the limit.

## originality

PASS

The deterministic short-factor lemma, run enumeration and standard adjacent-pair Poisson mechanism are antecedents. The defensible addition is the biased-source collision estimate conditioned on exact weight and its quantitative transfer to the necklace-valued deletion observable at the sparse birthday scale, including the first two moments.

## value

PASS

The finite TV estimate converts a synchronization ambiguity observable into a computable full reference distribution under a natural fixed-content source model. At the birthday scale it establishes an even-valued Poisson deficit, including the limiting probability of maximum degree and its nontrivial variance, rather than only a generic upper run bound. The reduction is useful precisely because rotation can merge outputs of distinct runs and a run law alone would not answer the deletion question. The result does not claim run-exactness for arbitrary words or multiple deletions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
