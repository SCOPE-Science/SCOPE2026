# Independent mathematical audit

## correctness

PASS

I independently replayed all four prisms with `python /workspace/replay/combinatorial.py prism <frozen-dir>/prism6_certificate.json`. Recursive matching generation pairs the least uncovered vertex with each available neighbor, giving each perfect matching exactly once. A support is extended only if its every trace cell splits nontrivially on the new edge; heredity and ordered extension make this a complete enumeration, giving (1,9,3,0,0), (1,12,42,0,0), (1,15,60,5,0), and (1,18,117,138,0). For adaptive depth d>0 the replay checks whether some edge has two restricted concept sets both realizable to depth d-1; fewer than 2^d concepts makes this impossible. The matching counts are 4,9,11,20, and the resulting (VC,Littlestone) pairs (2,2),(2,2),(3,3),(3,4). I also checked all 20 specified masks, and the distinct witnesses at all sixteen depth-four leaves against every label on their paths. The structural VC upper bound is valid: with rungs present, the remaining path segments require synchronized pairs of rail edges, and with no rungs the even cycles give the two synchronized and two staggered choices. Each rail edge of P6 appears in at most six matchings, below the eight needed on any positive branch of a shattered quadruple, so all four would be rungs. A consecutive triple is obstructed by 1,0,1; otherwise the rungs have pattern {0,1,3,4} up to rotation, with the stated obstruction forcing both vertices of column one into column two and leaving column three blocked. For connectivity, two deletions in one rail leave the other cycle intact and every surviving vertex on the damaged rail linked to it; one deletion per rail leaves two paths joined by surviving rungs. Bipartiteness follows by taking alternating colors on each even rail with opposite phases, and every edge is in a matching by the all-rung or one paired-cut construction. This verifies the first gap within the family only.

## originality

PASS

Credit the prior perfect-matching counts and earlier adaptive gaps in open ladders and their bridge chains. The supported distinct claim is the adaptive vs. static comparison in circular prisms, including the exact first gap and its edge-query support census, not an assertion that no earlier graph exhibits an adaptive gap.

## value

PASS

The first gap in a canonical circular family replaces open, lower-connectivity or bridge-bearing examples with a highly symmetric, three-connected, cubic, bipartite planar graph whose every edge is usable. It gives an explicit compact adaptive witness, a structural static obstruction and the precise threshold; the exact support face counts locate how common static shattering is before the obstruction. This motivates the finite domain without any unsupported global-minimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
