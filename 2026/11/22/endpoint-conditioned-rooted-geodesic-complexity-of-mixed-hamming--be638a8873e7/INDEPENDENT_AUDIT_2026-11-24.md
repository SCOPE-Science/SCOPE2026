# Independent mathematical audit

## correctness

PASS

A rooted Hamming geodesic only activates root coordinates and keeps every activated symbol fixed. Thus reachability is x<=_r y iff every nonroot coordinate of x is the same in y, and any chain can be realized by concatenating successive activations. Dilworth gives equality of minimal rooted cover size and antichain width on the target path (overlaps in covers cause no issue, since every vertex can be assigned to one covering chain). An endpoint geodesic changes each differing coordinate once. Two vertices along it are incomparable exactly when their intervening segment has a replacement or both adding and erasing. Therefore the consecutive disjoint segments of an m-vertex antichain consume at least m-1 distinct replacements or disjoint erasure/addition pairs, bounding m by 1+h+min(e,a). A path ordering the min(e,a) disjoint pairs and then all replacements achieves this width by selecting the start and the vertex after each pair or replacement, before unused changes. This works also with no changes, yielding cover size one. Globally, h<=t and e+a<=b+t-h give h+min(e,a)<=floor((b+t+h)/2)<=t+floor(b/2). Set all t nonbinary coordinates to replacements and use disjoint erasure and addition sets of floor(b/2) binary coordinates to attain it for each root. The terminal formula concerns the maximum over geodesic orders, not each path, and the graph parameter covers one geodesic at a time, not all vertices at once.

## originality

PASS

The rooted cover and antichain-width equivalence are established and credited, as is the general distinction between fixing a root and demanding the bound for every root. The checked primary statements do not supply the mixed-clique width or the fixed-terminal maximum. The latter gives the algebraic reason that a replacement contributes one unit and other changes contribute in pairs, rather than just recasting the standard antichain formulation.

## value

PASS

The result evaluates a natural rooted single-path invariant exactly on a family where two types of complete-graph factors coexist. The terminal-conditioned result is stronger than a table of product values: it identifies how endpoint choices constrain the adversarial order and gives both a tight upper bound and an attaining geodesic. One can use the formula without enumerating product vertices or geodesics. This does not settle analogous questions for arbitrary Cartesian products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
