# Independent mathematical audit

## correctness

PASS

The bilinear edge cocycle gives commutator x_u x'_v-x'_u x_v, valid also in characteristic two. On support U, all nonzero vertex columns on an induced connected component must have a common projective line, and this condition is sufficient. For a fixed tuple, the kernel of conjugation consists of one free scalar per active component plus a free coordinate at every vertex outside N[U]. At each outside neighbor of U the coordinate is forced to zero. Thus the rank is |N[U]|-c(U), and central coordinates for a fixed column array split into cosets of size q^rank. This includes isolates and empty support and gives the frozen polynomial. Independently, putting L=(q^k-1)/(q-1), the star contributes q^(3k)+q^(3k-1)(q^(3k)-1)t+q^(3k)(q^k-1)t^3 by splitting on center membership. The triangle-plus-isolate contributes q^(4k)+q^(4k-2)L(q^3-1)t^2 by splitting on whether the triangle has any active vertex. These give the stated symbolic totals and factorization. An independent direct multiplication-and-all-conjugators replay at q=2 found 5632 commuting pairs in each group and size histograms {1:64, 2:2016, 8:192} and {1:256, 4:1344}, totaling 2272 and 1600. Its finite verification is separate from the universal proof.

## originality

FAIL

The earlier indexed joint-centralizer rank theorem for arbitrary tuples is formulated in the same coordinates and explicitly resolves the constant-projective component branch. Its proof-level rank and tuple count specialize mechanically to the commuting locus: retain the constant branch P on every component, then divide size-q^r counts by q^r. This is not an inference from the aggregated rank histogram alone. It is an exact restriction of the explicit assignment-level decomposition. Rossmann already supplies the full k=1 size distribution independently. The witness follows by evaluating the specialized formula on two four-vertex graphs; the empty-graph boundary is the trivial group and adds no separate result.

## value

FAIL

The full graphical orbit-size distribution is a natural object, but the proposed advance over the available all-tuple classification is precisely the routine choice of its constant-projective component branch. The illustrative four-vertex pair evaluates that branch. It requires only equality of the ordinary class totals, not equality of the full ordinary size profiles, which already distinguish the pair. No separate structural result or independently needed exact witness beyond the immediate specialization was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
