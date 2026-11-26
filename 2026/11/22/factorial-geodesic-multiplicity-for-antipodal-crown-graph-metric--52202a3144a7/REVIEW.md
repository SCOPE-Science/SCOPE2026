# Independent mathematical audit

## correctness

PASS

For vertices, two omitted indices leave their same-shore vertices indistinguishable, and a chosen landmark distinguishes either endpoint of its own index from every other index. For edges a coordinate equals 1 away from both endpoint indices, 0 at a chosen endpoint and 2 at a chosen opposite vertex of an endpoint index. This decodes the side and location of the detected endpoints and recovers a missing endpoint at the sole omitted index. Conversely if i,j are omitted, the edges a_i b_t and a_j b_t for a third index t are indistinguishable. Thus the minimum basis family is the same for both metrics. A slide necessarily sends a token to the unique vacant index and flips its side; every such move is legal. With m=n-1, length equals m+2d for d decreasing moves. The initial b₀ must be removed, and an a₀ must be separately installed before the last move removes it to finish on the B shore. These are two separate decreases. With exactly two, the initial strictly increasing excursion visits distinct nonzero indices and is closed by the first decrease removing b₀. The next move must place a₀: otherwise b₀ is reinstalled and would require another decrease. If the excursion visits t+1 nonzero indices, it leaves t B landmarks; 1≤t≤m-1 is necessary and sufficient. The second decrease can use any one of those t B landmarks. Thereafter only increasing moves are possible: the remaining m-t A landmarks at nonzero indices can be visited in any order, followed by the forced slide from 0. This yields (m)_(t+1)·t·(m-t)!=m!t(m-t) distinct labelled paths and realizes the lower bound m+4. The sum is m!·m(m-1)(m+1)/6=(n-1)! binom(n,3). In particular n=3 allows t=1 and gives two length-six paths. Inspected artifacts/verify_original.py, artifacts/verify_quotient.py and recorded verification_output.txt without replay: they supply respectively direct finite BFS for n=3..7 and weighted orbit BFS for n=3..100, not the proof for all n.

## originality

PASS

The common basis family, vacancy move model, length n+3, two-decrease lower bound and example optimal routes have prior coverage. The supported distinction is the necessary and sufficient itinerary classification of every shortest route for these endpoints, with the resulting closed count in both metrics.

## value

PASS

These endpoints are natural extremal placements with a shared vacant pair and every occupied shore reversed. Distance tells the smallest relocation time, but not the diversity of choices at that time. The factorial count and explicit classification give all optimal schedules without exploring the exponential basis graph, and apply to both resolution notions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
