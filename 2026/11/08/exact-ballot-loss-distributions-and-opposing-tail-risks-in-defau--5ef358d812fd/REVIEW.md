# Independent mathematical audit

## correctness

PASS

A loopless functional digraph decomposes into one directed cycle plus in-trees per weak component. If any cycle voter casts, no lost ballots in that component; if every cycle voter abstains (probability p^c), c cycle ballots are lost, and each off-cycle rooted subtree contributes F_u(z)=(1-p)+p z product F_child(z). Independent casting gives the exact factorized probability generating function over components, all coefficients nonnegative summing to one. Differentiation/event counting yields EL=sum_v p^{c(v)+d(v,C(v))} and P(L>0)=1-product_C(1-p^{c}). Because all cycle lengths>=2, the largest possible number of 2-cycle vertices maximizes EL with unique equality configurations: even n all 2-cycles, odd n all but one in 2-cycles with one attached tail. Likewise cycle failure probability is maximized by floor(n/2) disjoint 2-cycles. For 6 voters, L_A=2 Bin(3,p^2), L_B=3 Bin(2,p^3), giving opposing mean and P(L>=3) with difference p^3(1-p)^2(p+2)>0. Independently enumerated all 90 loopless functional digraphs on 2..4 vertices, every cast subset with exact rational p=2/5, and matched each complete loss polynomial. Infinite n proof is functional graph decomposition, not enumeration.

## originality

PASS

The first-moment path formula and Hamiltonian-cycle minimum are known from Brill et al.; excluded from novel credit. What remains is total-ballot-loss distribution for arbitrary loopless networks, sharp maximum and equality network structures, and demonstrable reversal of risk ordering at the 3-loss tail. Grossi et al. concern expected influence, not stochastic aggregate loss; earlier equilibrium papers do not imply the same full PGF. Network-reliability polynomial equivalences remain a priority risk, but none dominating was identified.

## value

PASS

It is mathematically and substantively relevant to assess representational outage severity rather than only mean lost voting weight. The exact polynomial permits every tail query; equality classifications identify worst network topologies, and a strict six-voter example proves mean optimization can reverse large-tail ordering. These are natural finite-network reliability invariants rather than a parameter-renaming exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
