# Independent mathematical audit

## correctness

PASS

For a generic Gaussian normal G, the section meets the relative interior of each of the two i-facets exactly when |G_i| is less than the sum of the other absolute coordinates. These transverse intersections give all section facets without duplication; inactive equalities and nongeneric ridge degeneracies have Haar measure zero. At most one strict dominance is possible. Independently, for m=d−1 use absolute coordinate ratios x_i=|G_i|/|G_0| on the solid simplex sum x_i<1. The z^m Jacobian for z=|G_0| gives the normalization c^m E|G_0|^m/m!=1/[π^(m/2)Γ(m/2+1)] by duplication. Under the unweighted normalized product measure the ratios are the first m coordinates of Dirichlet(1,...,1) with one slack coordinate, and z² is χ²_(m+1), independently. Thus the remaining factor is E exp(−X), X=(z²/2) sum x_i². A symbolic calculation via multinomial index partitions reproduced all four moments about 1; the first two are −2/(m+2) and (3m+8)/[(m+2)(m+4)], with the third and fourth O(m^−2). Since X−1≥−1, the cubic Taylor remainder is bounded by e|X−1|^4/24, giving the claimed 7/(2m) and error order; multiplying by d and applying Stirling gives the displayed equivalent. Independent symbolic replay: python3 /tmp/opencode/nov02-independent-checks.py 1 (SymPy). Numerical sampling in the frozen companion is diagnostic only and was not executed.

## originality

FAIL

Direct equivalent coverage: the separately dated 2026-11-01 Resultary record 33fb29274ae4 proves the same sharp probability for the event of a section with the minimum vertex count. Both events are the same strict single-coordinate dominance cone a.s.; the earlier work gives the identical gamma normalization, e^−1, 7/[2(d−1)] and relative error order, with the same exact Dirichlet mixture. The frozen record expressly does not claim the facet characterization as new.

## value

FAIL

The sharp rare-event expansion is intrinsically useful, but this record gives no additional sharp invariant, regime, or method beyond the existing expansion for the identical event. The elementary facet interpretation is useful context but explicitly background here; it is not a surviving stand-alone research claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
