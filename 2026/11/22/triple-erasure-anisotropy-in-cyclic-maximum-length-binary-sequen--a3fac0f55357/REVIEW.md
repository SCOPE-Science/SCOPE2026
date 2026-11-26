# Independent mathematical audit

## correctness

PASS

Primitivity lists every nonzero query vector once, and multiplication by alpha traverses each phase state; a nonzero state cannot give the zero sequence by trace nondegeneracy. Dependent coordinates miss a labeling even before deletions. For independent k-sets, all fibers have 2^(m−k) elements; omit zero only from the zero-label fiber. This gives the baseline for k≤m−1, and forbids larger supports. At k=m−1 the kernel is {0,w}; the zero label dies on erasing w; a nonzero label dies exactly if both members of a pair with sum w are erased. Each surviving w contributes the unordered bases of w-perp. At k=m−2 only the zero label can die with three erasures, and only when the deleted states are exactly the nonzero part of its two-dimensional kernel. The three nonzero pair sums of an independent triple are distinct from the states, whereas for a line they are the states. Lower layers survive. This also covers m=3. The lower saturation bound is counting singles and pairs; the upper splits the vector space into complementary subspaces and uses each cross-sum. An independent dot-product replay enumerated all 128 erasure subsets at m=3 and all layers for five patterns at each of m=4,5. It tested for accepted supports by taking the set of observed binary masks on each support; no frozen code was executed. At m=4 the two triple cases gave coefficients (1,15,102,336) and (1,15,105,252) in increasing degree, compared with (1,15,105,420) before erasure.

## originality

PASS

Credit prior work for un-erased phase-dimension concepts, the LFSR independence criterion, the saturation criterion itself and the bounds' standard finite-geometric ingredients. The supported distinct claim is the phase-erasure top coefficient and the explicit transfer of erasure geometry to loss in two different shattering layers. None of the compared passage-level results computes these counts or the opposing effects of a line versus an independent triple across those layers.

## value

PASS

The quantity is the loss of realizable Boolean queries after removing hypotheses from a canonical recurrence family, not loss from arbitrarily chosen objects. Three deletions of equal cardinality have opposite effects by layer: a binary line loses fewer maximum supports than an independent triple yet uniquely loses penultimate supports. The exact count makes that failure of cardinality-only robustness explicit and identifies which top queries survive any erasure set. The old saturation bounds alone are not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
