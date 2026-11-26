# Independent mathematical audit

## correctness

PASS

In zero-set coordinates each update takes the opposite shore's secants (threshold two for zeros). On a noncollinear set the two-step secant map is extensive. A noncollinear set without a quadrangle is a triangle or has at most one point off a line containing three or more points: two off-line points and two of the collinear points avoiding the intersection with their joining line would give a quadrangle. These sets are fixed. A quadrangle can be put at the three coordinate points and (1,1,1); its first double-secant image adds (1,1,0),(1,0,1),(0,1,1), and the secants of this seven-point set cover every point at least twice. Thus quadrangle-containing sets reach the full shore in four updates. The collinear inputs go to the empty shore; their count, including the empty set, is 1+13+78+52+13=157. This explains the two exceptional fibers and why all 819 other fibers are singletons. I independently exhausted the 8192 masks using the Singer difference set {0,1,3,9} in Z/13 with an explicit F_3^3 coordinate identification (python3 /workspace/checks/plane.py). It reproduced the geometric phase sets, fibers 157 and 7216, and all first entry counts on each shore, including 936 at time four. The recurrent phase bijection turns the full update into swap on 821 x 821 symbols. Product fibers then give the claimed 821 fixed states, 336610 primitive two-cycles, exact basin multiset and joint first entrance counts. The factorization is exhaustive, not a direct replay of 2^26 states. The frozen proof and both supplied scripts were inspected, not executed.

## originality

PASS

The bipartite swap and eventual-period-two restrictions have precedents. The bounded comparison found no source giving or implying the sharp PG(2,3) open-neighbor strict-majority cutoff, stable phase classification and complete fiber/basin/entry census together, or the main new PG(2,3) census separately. The same-day incidence-graph record is materially relevant but distinct; no same-day priority was inferred.

## value

PASS

This natural even-degree projective incidence graph is a test case where the general period theorem says nothing about a sharp transient bound or the distribution of attraction. The complete census explains why three geometric classes yield 819 isolated phases and why only two exceptional phase symbols carry almost all of the nontrivial attraction. It provides exact benchmark data for a related family already studied on smaller cubic incidence graphs; it does not claim a theorem for other orders or tie conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
