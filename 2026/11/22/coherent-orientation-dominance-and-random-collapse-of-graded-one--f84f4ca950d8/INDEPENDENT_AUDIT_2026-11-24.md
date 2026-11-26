# Independent mathematical audit

## correctness

PASS

Only directed cycles of length three are forbidden. Free amalgamation and homogeneity identify types with admissible ternary assignments. Independently of the Hölder proof, on each fixed support encode + as 1 and − as 0. For each old arrow u→v the constraint is x_u≤x_v. The zero set is an ideal in the reachability poset after collapsing strongly connected components, and each ideal is determined by its antichain of maximal components. Choosing one fixed representative from each component sends those antichains injectively to independent sets of the supported undirected graph. For a coherent biclique reachability consists just of edges, so every independent set is attained: 2^p+2^q−1. A noncoherent nonempty biclique has an incident pair with opposite direction bits (its line graph is connected), hence a directed two-edge path whose two leaves are an independent set that cannot occur together in the antichain image. This also gives strictness on every larger support containing that path. The cubic calculation is four sign choices on a mixed star versus five on a pure star, and no other three-vertex support loses any choices. Degrees 0–2 and the 1-by-1 case agree with the polynomial. For the random model, conditioning on A statuses of counts p,q gives expected B factors 1+2^{-p}+2^{-q}, independent across B vertices. With h=ceil(3 log_2 n), each of p=0 and q=0 contributes 4^n(1+O(n^{-2})), and the intersection is 3^n. For p,q positive: both large contribute O(3^n); one small and one large contribute at most (3+o(1))^n exp(O(log^2 n)); both small contribute at most 2^n exp(O(log^2 n)). The deterministic lower bound 2·4^n−1 and the resulting O(n^{-2}) bound on expected relative excess yield L1 and almost-sure convergence without cross-size independence. The supplied code and finite output were inspected, not executed; they serve as finite checks rather than proof of the limit.

## originality

PASS

Pass the exact graded deficit profile and fair-random limit in this fixed-biclique type problem to the best of current knowledge. Neither weak Hölder on bicliques nor the standard ideal–antichain correspondence is new, and the latter makes the basic supportwise extremum a short deduction. The checked prior statements do not supply the graded cubic deficit together with the random count and its asymptotic law.

## value

PASS

The basic extremal comparison alone is an elementary consequence of standard ideas. The exact first deficit identifies the obstruction as a directed two-edge path; the same witness makes the deficit strict at every larger degree. More importantly, the universally admissible one-sign assignments asymptotically account for the whole count on fair random bases, even almost surely under arbitrary couplings across sizes. This pins down a natural typical scale and its exponential separation from the coherent extremum, rather than reporting only small-matrix counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
