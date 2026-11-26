# Independent mathematical audit

## correctness

PASS

An edge of T_n specifies two intersecting ground pairs, hence a unique triple and center. Two selected edges are compatible if and only if their ground supports are disjoint, so maximum size is floor(n/3) and dividing by the free-label, block and leaf permutations gives n!/(r!2^k k!). After deletion the replacement is confined to the r+3 available labels. The jump degree counts all possible marked triples there except the old one; the slide degree counts edges incident to the two endpoints of the old edge in T_{r+3} other than itself. These are disjoint alternatives, since distinct edges share at most one endpoint, and distinct deleted edges cannot yield the same neighbor. For r=0 the invariant support partition gives independent K3 center changes. For r>0 a center change followed by a slide exchanges any designated occupied label with any free label. Such transpositions generate all placements (a third slot provides a buffer for same-class transpositions), and centers can be set afterward. This also works for k=1, including n=3 where there is just one component.

## originality

PASS

The residue transition, marked-block method and multiple-of-three component formula substantially overlap the prior triangular-graph dissociation record. The supported distinct contribution is the exact comparison of both whole-matching-edge reconfiguration graphs, notably the jump degrees for r=1,2 and the slide degree for r=2. The older one-vertex move graph is not either of these graphs uniformly over the residues and its degrees are not a formula for the frozen edge-token degrees.

## value

PASS

The two natural models have the same reachable components but very different local mobility: e.g., with two free labels there are 29k jump choices but only 10k slide choices. The exact, labeled all-order comparison clarifies why allowing a whole matching edge to jump does not change reachability in this family despite adding many transitions. This is distinct utility from recomputing the known residue transition alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
