# Independent mathematical audit

## correctness

PASS

A disconnected symmetric difference lets one toggle a proper subset of components, giving a distinct midpoint representation and ruling out adjacency. For one component, fix common coordinates to 1 and coordinates outside the union to 0, and impose tight matching degree constraints at internal path vertices or all cycle vertices. This face has one free alternating coordinate and hence is just the segment. Binary coordinates make squared length the number of toggled edges. Choosing j old matched pairs, arranging and orienting them yields the counts: divide by 2 for reversal with two matched endpoints; start at the chosen uncovered endpoint with one uncovered endpoint; fix an orientation of the two chosen uncovered labels with two uncovered endpoints; and use cyclic order modulo reversal for cycles. The lengths are 2j-1, 2j, 2j+1, 2j respectively. A single uncovered pair uses no matched edges, and a j=2 cycle has two reconnections. Write a_k=2^(k-1)k!: normalized path weight for j=k-r is (2^r r!)^(-1) times 1, 2s or s(s-1). The j=0 weight is negligible, and normalized cycles are negligible by the 1/j factor at j>k/2 and the factorial tail otherwise. This yields the asserted degree equivalent, independent Poisson(1/2) defect and three-point offset, with denominator s^2+s+1, and the length normalization. This review used an analytical proof reconstruction rather than running the supplied checker.

## originality

PASS

The established matching adjacency framework and its four path/cycle classes are prior work. The complete-graph multiplicities are a direct refinement of that framework, not an independent adjacency theorem. The validated distinct contribution is the local metric distribution and its explicit Poisson-scale fixed-s limit with parity and endpoint-type dependence, which is not equivalent to the closest checked local or published results.

## value

PASS

The question concerns the lengths in the actual one-skeleton rather than a chosen edit graph. The explicit limiting law distinguishes typical long exchanges from short-exchange traversals and gives endpoint-type and parity effects invisible to a degree count or a leading-order length estimate. The finite enumerator also gives the complete local spectrum rather than isolated counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
