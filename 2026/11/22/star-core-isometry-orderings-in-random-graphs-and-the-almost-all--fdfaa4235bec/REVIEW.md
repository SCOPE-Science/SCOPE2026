# Independent mathematical audit

## correctness

PASS

For prefixes within N[v], nonadjacent vertices see each other at distance two via v; for later prefixes the whole N[v] is available, and the certificate supplies a retained common neighbor for each nonedge. This works for every ordering within the two blocks. For a fixed nonedge involving v the n-2 candidate witnesses each use a distinct pair of edges. For a fixed nonedge avoiding v, the witness v uses two edges and the n-3 other candidates use disjoint triples of edges, also disjoint from the nonedge being tested. This gives the two exact witness-failure probabilities, not exact ordering-success probabilities. Union bounds over pairs and then centers give the stated B_n(p) and n B_n(p). Since p^2>=p^3, the exponential bounds give the two stated logarithmic conditions, and fixed p in (0,1) gives exponential convergence. In the labelled-to-unlabelled transfer, a permutation moving m vertices can fix only pairs of unmoved vertices and at most m/2 transposed pairs. At least m(n-2)/2 edge positions move, so the nonidentity contributions to normalized Burnside counts are bounded by sum_{m>=2}(n 2^{-(n-2)/4})^m=o(1). The labelled disconnection estimate also tends to zero, by bounding the k-th term by (n 2^{-n/2})^k for k<=n/2. This gives the proportion for uniform unlabelled connected classes, not general p-weighted classes. The nesting is stronger than existence of one isometric induced subgraph of every size.

## originality

PASS

The supported distinction is the common star core for all pairs at a fixed center, the arbitrary-within-block ordering guarantee with explicit sparse-to-dense finite probability bounds, and the application to uniform unlabelled connected classes. The older distance-preserving property and conjecture, the star-prefix idea, and general random common-neighbor and orbit-counting methods are not first claims here.

## value

PASS

The certificate makes nested isometry explicit with substantial ordering freedom, and the probability estimates apply down to densities vanishing with n. The same argument yields a concrete stronger conclusion for a natural almost-all graph-class question, with a quantified and independently checked transfer between labelled and unlabelled counting. These claims go beyond a census or proving generic two-step distances alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
