# Independent mathematical audit

## correctness

PASS

The mathematical argument is correct. In a perfect matching of the induced complete multipartite graph, every selected vertex in a part must match outside that part, giving \(s_i\le t\). Conversely, a complete multipartite graph on \(2t\) vertices with largest part at most \(t\) has a perfect matching; the selected set meets at least two parts and therefore dominates. The overloaded-part events in a \(2t\)-set are disjoint, giving the coefficient formula. Every valid set of size greater than two contains a cross-part edge, which itself is paired dominating, so the inclusion-minimal sets are exactly the edges. The package verifier independently confirms the criterion and coefficients through order nine.

## originality

FAIL

A published Resultary/SCOPE record already states the same complete-multipartite paired-domination characterization and exactly the same coefficient formula: 'Paired-domination polynomial of complete multipartite graphs' (record SCOPE-20261004-ea2bc935cbba). Its full RESULT.md was inspected. It says \(|S|=2q\) and \(s_i\le q\) for every part if and only if \(S\) is paired dominating, gives the identical double-sum coefficient formula, states all odd coefficients vanish, and gives \(d_p(G,2)=|E(G)|\) and \(\gamma_p(G)=2\). The submitted additional sentence that every inclusion-minimal paired-dominating set is an edge follows immediately from that iff criterion, because every larger valid set contains a valid cross-part two-set. Thus the entire submitted claim is covered or a routine corollary of an already published stronger result.

## value

FAIL

Because the exact all-set criterion and polynomial formula are already published, the remaining minimal-set observation is a one-line consequence of that criterion rather than an independently motivated new theorem. Correctness and a separate verifier do not create scientific value once the claimed contribution is already covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
