# Independent mathematical audit

## correctness

PASS

For k arms with s edges and s-k+2 vertices, a spanning tree must leave exactly one full terminal path and delete one edge on each of the others. Counting terminal/internal leaves gives z^(k-1)[sum_i prod_{j!=i}(2+(ell_j-2)z)+2k(z-1)]/tau, tau=sum_i prod_{j!=i}ell_j. For ell_a=p>=q+2=ell_b+2, balancing changes the numerator by delta*z^2 Q and tau by delta*Q(1), delta=p-q-1. The exact mixture law is old law with weight tau/(tau+delta R) plus H law with weight delta R/(tau+delta R), R=Q(1)>0. Coupling the intact path and keeping shared edge cuts yields H-L=E_a+E_b-J if intact path is in the remainder, or E_b+E_h-J / E_a+E_h-J otherwise; J=1 forces the two indicated cuts to touch the same terminal, hence each difference is nonnegative. Opposite-end cuts give strictness with positive probability, proving stochastic order and strict mean, and majorization reaches the two global extrema. Direct independent deletion-pattern enumeration reproduced exact leaf polynomials for six configurations, including (2,3,5,4); the symbolic coupling, not the finite checks, proves the universal claim. No arbitrary weighted-network/general-series-parallel extension is asserted.

## originality

PASS

Rapoport's all-finite-graph fermionic degree laws can compute the distribution in principle, but do not state or imply the strict theta balancing order across different graphs. Resultary searches found related tree leaf fluctuations and stochastic orders on complete multipartite, Cayley or Catalan graphs, not this family. The explicit cross-network monotone coupling and global majorization extrema are a distinct contribution; generic tree-count formulas and degree probabilities are credited.

## value

PASS

A genuine nontrivial distributional majorization law: it applies to every increasing leaf statistic, not merely expectation, and identifies both extremal subdivisions at fixed cycle rank and edge budget. The explicit mixture-coupling explains a strict stochastic ordering not forced by the spanning-tree count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
