# Independent mathematical audit

## correctness

PASS

The vertex test is exactly the intersection of the two strict inward half-circles of its incident edges, and any direction satisfying it also lights the interiors of both edges. A pair of vertices has a common direction iff the incident oriented edges have a complementary circular gap greater than pi. In the adjacent and nonadjacent configurations the internal gaps are individual turns below pi, so the only candidate is the complementary gap. Thus a neighboring pair is compatible iff its two turns sum to less than pi, and a diagonal is compatible iff the complementary neighboring turn pair sums to greater than pi. Nonconsecutive failed neighboring tests are impossible since their four turns sum to 2pi minus a positive fifth turn. With no failure, compatibility is C5, the two-hits-per-direction bound is sharp by taking copies of the five pairs and a three-pair cover for odd m. With failed tests {i} or {i,i+1}, the respective incompatible triples are {i,i+1,i+3} and {i,i+1,i+2}; they force 3m. Three compatible pair directions in the first case, and two pair directions plus an inward direction at i+1 in the second case, give the matching covers. Uniform half weights on the five cycle pairs or one unit on each direction of the three-cover establish the fractional bounds with the same incidence certificates. Equality is handled exactly by strict inwardness. Independent replay: python3 -I -B /workspace/reproduce.py 5 checked 26,277 exact turn fans, including 12,120 equality cases, by a half-step angular mesh that includes critical rays; exact multicover recursion on 31 maximal-incidence profiles matched for m=1..4. This is bounded corroboration, not the unrestricted proof; the uploaded checker was only inspected.

## originality

PASS

Inspected sources cover the regular pentagon for all multiplicities and the favorable unrestricted two-fold case. The favorable upper bound for higher multiplicities is incremental (repeat a two-fold cover and append a three-direction cover as needed). The distinct contribution is the exact arbitrary-pentagon classification, especially the incompatible triple and 3m lower bound when any test fails, including equality, with the sharp fractional dichotomy. No inspected stronger statement covers this remainder. This is a best-of-current-knowledge comparison, not a priority guarantee.

## value

PASS

This resolves a natural first odd-sided polygon case beyond triangles with arbitrary, not regular, turns. It identifies exactly when repetition lowers the per-fold cost below three and why parallel-critical equalities destroy that gain. The incompatible triple is a useful finite obstruction and the constructive direction choices match it for every multiplicity; the contribution is more than computing a few polygon examples or iterating the known two-fold favorable case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
