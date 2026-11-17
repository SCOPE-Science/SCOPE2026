# Independent mathematical audit

## correctness

PASS

Each of the two rows uses n distinct colours and omits one among n+1, say alpha and beta. The top-edge richness condition is exactly that the lower edge in its column has colour alpha, and conversely, so each row has at most one rich edge. Rich-neighbor requires a different adjacent rich edge for each edge, hence both rows have a rich edge in the SAME unique column. Richness there forces complementary missing colours, leaving a common n-1-colour set. Other columns are exactly two permutations differing at every coordinate, i.e. a derangement. Conversely such a colouring satisfies the condition. Counting column, ordered exceptional colour pair, upper permutation and lower derangement gives n*n*(n+1)*(n-1)!D_{n-1}; quotient by column and colour permutations identifies relative derangement up to conjugacy/inversion, hence cycle type. An injection first row has (n+1)! possibilities, while second row has D_{n+1}+D_n possibilities, establishing fraction and Stirling/derangement asymptotic. For n=2 a 1-point derangement is absent; four-colour C4 solution has 24 assignments. Independent direct proper-coloring adjacency enumeration agrees at n=3..7 (72,960,32400,1330560,74793600).

## originality

PASS

The known palette optimum n+1 (Kong 2026) is not new. The earlier index theorem for all complete bipartite graphs establishes existence/optimal number of colours, but a palette-size theorem does not imply unique rich witness structure, enumeration of every named configuration, or conjugacy-class orbits. The new rigidity bijection and counts are separate, as checked against indexed rich-neighbor results. The founding 2024 full article was not read, retained as risk.

## value

PASS

Counting all labelled optimal colourings and describing their symmetry orbits for a naturally extremal complete bipartite family sharpens an already studied graph-colouring invariant; the unique witness column and fixed-point-free permutation form a reusable structural equivalence, beyond a routine substitution into a known index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
