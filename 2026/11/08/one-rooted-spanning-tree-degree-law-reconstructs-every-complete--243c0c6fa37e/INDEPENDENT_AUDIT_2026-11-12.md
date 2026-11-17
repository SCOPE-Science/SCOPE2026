# Independent mathematical audit

## correctness

PASS

PASS: Classical weighted multipartite spanning-tree generating identity specializes at root v to P_v(z)=z((N-1+z)/N)^(r-2) product_{j!=i}((N-n_j-1+z)/(N-n_j))^(n_j-1). Because other part sizes are >=1, the root at -(N-1) occurs precisely r-2 times; roots at -(N-t-1) give (t-1) per nonroot part of size t>=2, after removing compulsory z at t=N-1. The remaining r-1 other parts are singletons, and known N gives root-part size. This works for r=2, complete graphs, stars, N=2. Independent exact weighted Kirchhoff cofactors on five multipartite types and all root part types at z=1,2,5 matched the stated normalized PGF; full proof is algebraic and not an extrapolation from finite tests.

## originality

PASS

PASS best of knowledge: Remmel–Williamson weighted spanning-tree enumerator is explicitly prior and gives forward joint generating functions; Rapoport general UST degree formulas and Fita Sanmartin et al node-degree moments are also forward. They do not state that one arbitrarily chosen vertex marginal, with its root part concealed, identifies every complete multipartite graph of known order. Prior co-degree reconstruction uses all common-neighbor pairs rather than one random rooted degree and excludes singleton parts. Exact inversion by factor multiplicities is a new natural injectivity assertion under tested sources.

## value

PASS

PASS: A natural one-vertex stochastic inverse graph problem admits a full all-order reconstruction, including highly asymmetric and singleton-containing complete multipartite graphs. This identifies a whole host isomorphism class from an exact scalar marginal and shows why N must be specified (universal star-leaf degree 1). The constructive root multiplicity decoder, though based on known enumerator, is a useful explicit local-to-global rigidity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
