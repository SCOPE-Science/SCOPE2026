# Independent mathematical audit

## correctness

PASS

An active root edge survives precisely when isolated as a component, while an inactive edge becomes active precisely when both endpoints are isolated vertices. Thus F(S)=I(S)⊔E(U(S)). Independently, undirected open NOR is antitone with S⊆F²(S); applying this twice in the two directions gives F³=F. The complement W of the isolated vertices and isolated-edge matching supports components of order at least three, so |W| is zero or at least three. Substituting |U|≤1, |U|=2, and |U|≥3 in the image formula gives exactly the fixed matchings and the two disjoint classes of cycles; when |U|=2 its edge joins the matching, rather than forming a separate clique case. A two-edge path is not an image and realizes one-step entry. Fibres of a clique phase of order at least three uniquely specify the isolated vertices and matching. For a matching phase its fibre additionally allows replacing at most one matching edge by two isolated vertices, which gives the extra m·a_r term and the perfect/near-perfect distinction. Removing labelled components of orders one and two gives the EGF; counting unordered complementary parts gives the orbit census. For the dominant basin the complement is the union of pair-isolation and isolated-edge events with the empty graph removed. Each event prescribes 2n−3 bits; compatible shared-endpoint pairs prescribe at least 3n−6 and disjoint pairs 4n−10. Bonferroni yields the displayed relative O(n·2^(−n)) error; the empty graph correction is smaller. The union bound gives strict majority for n≥4, and n=3 gives 5/8. An independent truth-table enumeration checked F³=F and every individual basin through n=7, including 2,097,152 inputs there and distinguished basin 2,059,625.

## originality

PASS

The complete matching-and-clique basin spectrum and two-family rare-event deficit are materially distinct from the inspected earlier and same-day results. The generic period bound, one-step entry identity, and maximal-independent-set fixed point correspondence are not credited as new.

## value

PASS

This is a natural synchronous rule on a canonical line-graph family, and generic two-periodicity leaves the distribution of initial states among orbits unresolved. Exact sizes of every individual basin expose both the matching skeleton and an explicit effect of excluding self-neighbors, including the change in the sharp leading rare-event coefficient. The classification and phase-resolved counts are materially more informative than an orbit census or a mere concentration bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
