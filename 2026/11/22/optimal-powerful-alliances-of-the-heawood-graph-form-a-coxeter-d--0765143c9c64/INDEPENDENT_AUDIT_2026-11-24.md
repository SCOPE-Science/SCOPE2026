# Independent mathematical audit

## correctness

PASS

In the cubic graph the four-element closed-neighborhood inequality is precisely at least two selected per closed neighborhood. Every selected vertex has ≤2 outside neighbors and every omitted vertex has ≥2 selected neighbors. Counting crossing edges gives |S|≥7; equality would give a perfect matching on the selected seven vertices and is impossible. If |S|=8, its six omitted vertices cannot contain a collinear point triple or a concurrent line triple: the witness line or point would violate the same closed-neighborhood inequality whether selected or omitted. A cap has size ≤4, and a four-point cap is the complement of a line, since its six secants account for its twelve incidences. At most one line can meet it in ≤1 point, so the omission splits as three points and three lines. For three nonconcurrent lines, the omitted points cannot include a pairwise intersection; they must be the single point off the three lines and two private points, since the three private points are collinear in binary coordinates. These choices satisfy the inequality on both shores: within the omission every vertex has ≤1 omitted neighbor, and the cap conditions forbid a selected vertex from having three omitted neighbors. Thus there are 28×3=84 optima. The intersection triangle Q has exactly the three omitted lines as its side lines; the omitted point triangle P is disjoint from Q. For fixed Q the allowed point triples differ by one point; for fixed P the dual private-point argument gives three line triples differing by one line. A jump preserves exactly one coordinate, yielding the line graph of the bipartite Coxeter double; shore balance rules out all slides. Binary linear changes of basis permute any chosen triangle of independent line equations and its private-point positions, giving transitivity. An independent binary-vector Fano construction and closed-neighborhood scan of every subset of size at most eight in /workspace/reviews/evidence/heawood.py verified the optimum count, the ordered-pair bijection and every jump/slide comparison. All 84 BFS layer vectors were (1,4,8,16,28,22,4,1), confirming connectedness and diameter seven; the same checker produced 168 jump edges and a single collineation orbit under 168 maps.

## originality

PASS

Pass for the alliance-specific extremal membership criterion and reconfiguration identification, not for constructing the Coxeter double or taking its line graph. The strongest distinct match is a same-day three-vertex-path cover result with exactly the same ordered triangle pairs as edges of its mobile component. It supplies the graph framework but not the correspondence with minimum closed-neighborhood majority sets or their moves.

## value

PASS

A complete minimum double-domination/limited-packing classification on the canonical cubic incidence cage connects a natural local feasibility predicate to Fano triangle geometry. The bijection explains every optimizer and why jumping connects them while sliding cannot even start. The reusable contribution is this structural explanation and exact small-graph benchmark, rather than the bare lower bound or a new name for a known graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
