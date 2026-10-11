# Independent mathematical audit

## correctness

PASS

For complete multipartite graphs, a same-part pair has distance two and its shortest paths contain every vertex outside that part, while a cross-part pair is adjacent. Hence one interval step from a set containing two vertices in part \(V_i\) adds all vertices outside \(V_i\). If another part is non-singleton, the new set contains two vertices there and a second interval step fills the remaining vertices of \(V_i\). With exactly one non-singleton part, closure can fill outside it but cannot refill an omitted vertex inside it; with all singleton parts the graph is complete. This proves all three cases and the enumerator. A fresh independent brute closure on every complete-multipartite profile through order six matched the theorem.

## originality

FAIL

A current published same-object result, 'Geodetic polynomial of complete multipartite graphs', already proves the exact one-step shortest-path mechanism: a pair inside a part covers every vertex outside that part, and cross-part pairs add nothing. Its proof therefore immediately yields the assigned hull theorem by one further closure iteration: a heavy part creates every outside vertex, which creates a heavy second non-singleton part exactly when one exists, and that second pair fills the original part. The one-non-singleton and complete-graph boundary cases are equally immediate. The assigned three-case hull classification, minimal generators, and polynomial are consequently routine corollaries of already published same-object structure, even though 'geodetic set' and 'hull set' are distinct notions.

## value

FAIL

The hull formulas are clean and correct, but once the same complete-multipartite interval action has already been published, obtaining the two-step hull closure and its three elementary boundary cases is routine. No independent structural mechanism or motivated gap survives current coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
