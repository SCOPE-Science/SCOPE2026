# Independent mathematical audit

## correctness

PASS

Coordinatewise betweenness is equivalent to geodesic betweenness in either direction of the Manhattan distance equality. With origin corner, the noncorner pair must be strictly incomparable, and must not lie on opposite positive axes (otherwise the corner is between them). An incomparable pair is the antitone diagonal of one chosen subrectangle, and the excluded axes occupy exactly (m−1)(n−1) such diagonals. Three noncorner vertices of a legal corner-containing four-set would have strictly decreasing second coordinates when sorted by the first, so their middle vertex would be between the other two. Thus every rooted triple is maximal. Adjacent pairs are maximal by bipartite distance parity, and the opposite corner pair has a full geodesic interval; every other corner pair extends by the witnesses (1,1) for a nonneighbor axis vertex and a strictly farther point on the other axis for an interior vertex below an upper boundary. Builder-first stops at an adjacent pair; Blocker-first has upper bound three by starting at a corner, and every opening vertex off the 2×2 case lies in one of the two covering general-position triples of an isometric 2×3 strip. The 2×2 case has no legal triples. Independent replay `python3 /workspace/review_evidence/reproduce.py 5` implements Manhattan-betweenness minimax and checks exact pair identities and triples on 18 grids and 72 corner roots. The frozen code and recorded output show 14 grids in the stated small range plus four longer grids, 18 total, not 18 plus four as the prose in RESULT.md could be read to say.

## originality

FAIL

Prior results mechanically imply both putatively new parts. The prior grid-polynomial proof classifies forbidden triples geometrically, not just by aggregate counts, so it can be restricted to a corner to give all corner triples and their count, with maximal pairs precisely the vertices admitting no partner in that restricted classification. The prior classification of maximum four-sets rules out four-sets at a corner, and the earlier thin-grid classification yields a 2×3 triple cover about any opening vertex. Together with the published two-move criterion these yield the exact Blocker-first value. The lack of an earlier verbatim rooted formula or stand-alone game statement does not overcome these implications.

## value

FAIL

The natural game question and the exact corner count have expository use, but neither supplies the required independently new mathematical fact. After crediting the primary proof-level grid classifications, the remaining work is a simple restriction of their case conditions, an elementary count, and the immediate corner-opening strategy combined with the existing two-move criterion. The precise three terminal pairs are also just the three absent-partner boundary cases of those conditions. No materially distinct result remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
