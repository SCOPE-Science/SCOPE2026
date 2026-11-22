# Independent mathematical audit

## correctness

PASS

For a sorted unit normal in the coordinate-sum-zero hyperplane, simplex widths decompose into positive adjacent gaps times counts C(A) of crossing connected tubes. Triangle inequality with the centered cut indicators proves a reduction to cut widths, and equality with more than one gap is impossible because nested distinct centered indicators are not positive collinear. In K_c joined to an independent class m, C(a,b)=(2^c-1)2^m-2^{a+b}-2^{n-a-b}+2^b+2^{m-b}; independent manual subset-count reconstruction agrees. Independently reran an exact integer certificate over all 1,830 (n,c) profiles with 4<=n<=63, 750,605 admissible cut classes and all 4,116 equality classes, matching the actual verify.py specification. For n>=64 the source inequalities bound noncentral cut counts below by B[1-(4/3)(2^-k+2^(k-n))] and compare their normalized widths to central cuts, so all noncentral cuts are strictly wider; central C minimizes when b is one of the two middle integers and n cut size is central. Correct switch at n=15, all equality normals and strict lack of ties follow. This is all n, not an extrapolation of the finite table.

## originality

PASS

The graph is the complete split join, neither a complete graph nor a genuine complete biclique. Prior published fifteen-vertex transitions share a threshold and the cut-reduction technique but use different crossing-tube families; their statements do not imply the split two-class all-parameter formula or exact minimizer classes. Best-of-knowledge.

## value

PASS

Euclidean minimum width and its complete normal classification are natural optimization invariants of the canonical graph-associahedron realization. The universal cutoff and double balancing across clique and independent classes provide a nontrivial structurally useful classification for a graph family not covered by neighboring complete/biclique results; this is more than repeating a numerical threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
