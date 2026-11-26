# Independent mathematical audit

## correctness

PASS

For pairs at distance two, centers at the query points give the singleton traces, and a midpoint gives the full trace. For an adjacent pair, a step away from either query point in a different Cartesian factor separates it from the other; d≥3 guarantees at least two factors. The union bound on two balls gives the empty trace. Thus the quadratic coefficient counts exactly pairs at distance at most two. For triples, the full trace places the support in a centered ball. Two query points in different arms have only the original center and their two-coordinate combination as common centers; a third arm, a second point in one arm, or the original center eliminates the latter. In the two-points-in-one-arm case the pair within that arm can be realized without the original center (for a nonadjacent Shrikhande pair use its other common neighbor). Mixed pair traces and singleton traces follow by choosing one or two coordinates accordingly; for a centered triple with two complete arms, the original-point singleton uses a third factor, available for d≥3. The single-arm cases reduce exactly to factor traces: for a center at outside distance r, the distance to any query equals r plus the selected-factor distance. Hence outside coordinates only add singleton and empty traces, all of which can be achieved when there is another factor. This justifies transferring the checked Shrikhande table (14 unique-center noncentral triples, plus nine centered triples with center multiplicities 1,1,1,3,3,3,3,3,3); no single complete arm has a doubleton trace. For four points in at least three arms, a triple in separate arms has only the original center. In at most two active factors the same distance decomposition embeds every trace into the template with spare factors, which suffices in the direction needed for nonshattering. The independent checker reproduced the local tables and found no shattered centered four-set among all 715, 1820 and 3876 candidates in the three templates. For the algebra, write g_i=3a_i with a_i=1 or 2. Splitting each weight-two index into two distinct unit copies, the mixed-arm terms account for 27[binom(d,3)+binom(d,2)−m], and the single-arm contribution adds 19m. The resulting T=27 binom(d+1,3)−8m is positive for d≥3. Vertex transitivity and reciprocal common-center weighting give 4^dT distinct triples. The cubic arithmetic then proves the fixed-diameter distinction.

## originality

PASS

The quaternary Hamming specialization and the separate diameter-two Shrikhande/rook comparison are prior catalogue results. Neither implies the uniform per-factor defect in all products of diameter at least three. The supported distinct claim is the mixed-Doob polynomial and its fixed-diameter separation, obtained by controlling trace interactions in the Cartesian factors.

## value

PASS

This gives an exact graph-isomorphism invariant that distinguishes every member of a standard fixed-diameter family sharing both an intersection array and VC dimension. The per-factor arithmetic is a concise structural explanation and a way to recover the number of Shrikhande factors from trace counts, rather than just another enumeration of one tabled graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
