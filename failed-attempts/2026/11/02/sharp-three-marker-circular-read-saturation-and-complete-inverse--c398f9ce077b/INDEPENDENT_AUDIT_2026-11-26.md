# Independent mathematical audit

## correctness

PASS

Let the three positive clockwise spacings sum to n. At n≥3k−1 at least one is long (≥k). Pair correlations at offsets below k are recovered by summing the observed counts of factors containing the two specified ones. If no factor sees all three ones, no two consecutive spacings sum to less than k, and those correlations exactly give the multiset of short spacings. The empty and singleton correlations are fixed; with the triple correlations zero, Boolean inclusion–exclusion recovers the full spectrum from the pair correlations. If a factor sees all three markers, it specifies the ordered short spacings and the total n fixes the remaining long one, so the source is fixed up to rotation. There are respectively 1_{n≥3k}, k−1, binom(k,2)−floor((k−1)^2/4), and binom(k−1,2) labels. Every label is realized in its stated range. Marking the unique short spacing in B or unique long spacing in C and D gives n placements per ordered cyclic configuration. For A, an indexed word with a distinguished marker has n times the number of weak compositions of n−3k into three parts as its total count over all words; division by three handles periodic words without a freeness assumption. These yield every stated fiber size, also for k=2, and the deficit of exactly one label at n=3k−1 proves permanent stabilization at 3k.

## originality

FAIL

The earlier 2026-10-26 three-marker reconstruction record contains a stronger gap-spectrum lemma in its proof. On the same observation model it already classifies equality of all spectra lacking a three-one factor, and proves uniqueness up to rotation whenever such a factor is present. Its theorem about reconstruction length is not the decisive overlap; the underlying lemma and triple-factor argument cover the entire equivalence classification asserted here. The new displayed numbers follow mechanically by counting those known labels and their indexed realizations.

## value

FAIL

Exact channel sizes and collision fibers are useful quantities, but this frozen claim is a routine enumeration of the already characterized classes after imposing the at-most-two-short-spacings condition. It adds no independent structural step beyond a change of coordinates and elementary counts of labeled placements. The formulas are correct and convenient, but not a distinct scientific contribution under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
