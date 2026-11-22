# Scientific review

## Correctness — PASS

The lower bound separates excursions outside the two initially full endpoints into crossing excursions, which cost at least the alternate-path length, and return excursions. If all excursions return, the initial saturation forces one excursion; if this were the only excursion, the returning token would remain at its original endpoint with both ends saturated again and the target unreachable. Hence at least two return excursions are necessary, adding at least four moves. Two fully explicit legal move sequences attain the minimum of the crossing cost and the two-return cost, for every connected host with at least three vertices and every capacity at least two. The embedded verifier independently checks forty-six finite cases, including the bridge boundary and all five cost regimes.

## Originality — PASS, with residual priority risk

The model itself comes from Song et al. (arXiv:2604.04845); its 2026 follow-up by Cai et al. (arXiv:2611.06275), sections 4.1–4.4, gives whole-configuration diameters in other regimes and a complete-host shortest-path theorem. The triangle case of this new formula is already contained in the complete-host theorem, but the local edge-cycle-length law for all host graphs is not implied by that special case or their star/odd-cycle diameter statements. Searches for saturated-stack exchanges, distinguishable capacity-two token swaps and edge-girth shortcuts identified no stronger applicable theorem. A prior equivalent result not indexed in those sources remains possible.

## Value — PASS

The statement determines a natural exact metric of capacity-constrained labelled rearrangement on **every** connected host graph. The sharp cycle-length threshold and capacity-independent congestion surcharge explain when a detour around an edge beats two temporary buffer excursions. It provides structural local-distance information complementary to existing global-diameter work, not a fixed arbitrary small enumeration. It neither asserts a new complete-host subcase nor claims to resolve the unsolved odd-cycle diameter formula.

Self-review: passed. Independent audit: not yet performed.
