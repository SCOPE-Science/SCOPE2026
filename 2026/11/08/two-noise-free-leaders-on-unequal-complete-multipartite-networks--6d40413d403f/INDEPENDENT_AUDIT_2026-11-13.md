# Independent mathematical audit

## correctness

PASS

For K_(n1,...,nr), r>=3, each n_i>=2, exactly two leaders and unit edges, grounded L_FF=M-11^T has invertible diagonal-plus-all-ones blocks. Sherman–Morrison gives exact inverse-trace J and the formulas for same-part and mixed-part placements. Same-part J(vv)-J(uu)=(N-4)(v-u)/[2(N-u)(N-v)] for u<=v, strict when u<v. For mixed u<=v, subtract same smaller-part objective; after h=u-2>=0, d=v-u>=0, R=N-u-v>=2, numerator has five strictly/nonnegatively coefficient polynomials, denominator positive. Independently verified that polynomial identity symbolically (SymPy), and exact matrix inverse traces for 213 pairs over 5 distinct multipartite graphs; K_(2,3,7) optimum 361/180. Thus every optimum is a same-smallest-part pair, count (#minimum parts)binom(m,2).

## originality

PASS

General noise-free leader criteria and optimization relaxations are established previously, and balanced multipartite and bipartite subfamilies have exact placement laws. The inspected earlier statements do not imply the strict smallest-part placement classification for unequal >=3-part graphs, with the full optimizer count and value.

## value

PASS

Two perfect leaders concentrating in one smallest, mutually nonadjacent community is a non-obvious exact optimization rule in a natural heterogeneous dense-network model. It resolves every optimizer, not a case study or trivial parameter substitution, and supplies the exact performance and multiplicity useful for network design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
