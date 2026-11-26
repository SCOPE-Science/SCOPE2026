# Independent mathematical audit

## correctness

PASS

The frontier transition preserves connectivity and parity by adding each old component once, and tests precisely the components that can no longer connect to the right. An extra empty mask tests closure. A new implementation using row-mask intersections reproduced 19 states, 119 transitions, the exact characteristic factorization, root isolation above 6, all eight listed counts, and a direct flood-fill census through n=5. A full column followed by one more full column if needed supplies an odd cap at width 3; every state thus returns to the empty state, whose loop proves primitivity. In an extendible strip word, an interior component already has odd size. Full columns at the occupied ends merge the boundary components, after which one added column on a suitable end toggles each even merged component, including the case of one component meeting both ends. Padding to two columns per end with zeros makes the map injective and proves the language bounds for all lengths, not just the tested boards. Independent strips with an empty spacer row give the claimed per-site lower bound. The replay verifies the strict width-two comparison with rational root enclosures and verifies 0.48216 by a rational exponential bound.

## originality

PASS

The inspected comparisons cover the underlying multidimensional shift and the exact two-row case, not the degree-eleven three-row entropy or the resulting numerical planar lower bound. The strict comparison with width two is mathematical; the catalogue dates alone do not show which result had historical priority.

## value

PASS

Width three is a natural next strip after the two-row calculation and requires distinguishing connectivity across an empty middle row. The exact spectral invariant controls both finite-board and actual strip growth, and the independent-strip construction strictly improves a quantitative lower bound for the full planar entropy. It does not purport to determine that planar entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
