# Independent mathematical audit

## correctness

PASS

For c=i+t marked components, an outside vertex w meeting at least two marks cannot repeat a component. Contracting the marked components and keeping the incidences to these outside vertices gives a forest on c+|W| vertices, hence sum_w(deg_A(w)-1)<=c-1. Internal nonsingleton open traces can come from at most m-i-2t marked vertices by the two leaves in every nontrivial component. With one empty trace and at most m singletons this gives 2m-t. At 2m, t=0 and all small traces plus m-1 distinct outside nonsingletons are forced. Equality in the edge budget forces all of those outside witnesses to have degree two in the incidence graph and makes it connected; suppression recovers the labelled tree. For the converse, subdivide its edges and give each mark a private leaf. These distinct singleton and pair witnesses must all be unmarked, so at order 3m-1 their forced edges already span a tree: there is no freedom left in the marked host. Cayley applies including the one-family m=1 convention; at m=0 every vertex of a nonempty host supplies the empty trace. The displayed sharpness example has t=0. Even the stronger interpretation for every feasible t is true: use t marked disjoint edges and m-2t isolated marks, connect the m-t components by a tree of new degree-two unmarked connectors, add a private leaf at each mark and append one vertex beyond a private leaf for the empty trace. This gives exactly 1+m+(m-t-1) traces and stays a tree. An independently written bitmask DFS that branches on each edge and adds it only when its endpoints are disconnected enumerated 2932 and 36961 labelled forests at orders 6 and 7, respectively. With the first m labels marked for each m, it observed 2761 and 36079 instances of 2m traces, all consistent with the bound, trace classification and host-order lower bound.

## originality

PASS

No equivalent or dominating theorem was identified in the bounded comparison. The distinct contribution is the refined exact open bound with its labelled equality families and marked minimum-host rigidity; neither contraction of components nor Cayley's formula is new.

## value

PASS

For a basic forest shatter invariant, the strengthened bound detects the cost of internal marked adjacency. The theorem converts every maximizer into an arbitrary labelled tree, and additionally determines the exact minimum realization and its rigidity. These facts are more informative than the asymptotic linear bound or the leading constant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
