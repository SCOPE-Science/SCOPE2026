# Independent mathematical audit

## correctness

PASS

For fixed labelled terminals in K_{a,b}, all xy cross-terminal edges are mandatory. Each same-shore pair has a shortest path through every vertex of the other shore, so after deletion any opposite nonterminal may retain at most one edge to that terminal shore. These are all the original geodesics, and the A_0 by B_0 edges affect none. Thus the classes of selected edges are independent; their factors are z^{xy}, H_x per B_0 vertex, H_y per A_0 vertex and 1+z per nonterminal-nonterminal edge. With no terminal neighbors the factor is 1; otherwise a minimum leaves exactly one, and no free edge can be in an inclusion-minimal set. This gives the minimum, count and exchange connectivity by changing one survivor at a time. The factorization has only nonpositive real roots and contiguous positive coefficient support, so Newton's inequalities give log-concavity and unimodality. When both terminal shores are occupied, the excess over x+y-1 is (b-1)(x-1)+(a-x)(y-1), zero in a non-star precisely for x=y=1. With terminals all on one shore the minimum is the opposite shore size times |T|-1; a star gives equality in every eligible placement, including when its center is a terminal. Inspected the supplied BFS verifier and verification notes; the 92 small-profile exhaustive checks and 92 larger formula-only checks are separate and neither replaces the block proof. No supplied code was executed.

## originality

FAIL

A distinct indexed result, Local clique factorization of semi-cutting sets at terminal diameter two (01e47751469e), demonstrably covers the biclique theorem. Its complete multipartite specialization gives the whole labelled census and stronger coefficient/exchange statements; it gives rigidity for |T|>=3, and its explicit minimum formula gives the remaining two-terminal cases. Both indexed records are dated November 22, 2026; the lack of verified within-day priority does not erase the mathematical coverage. This is not a finding that the assigned record necessarily appeared second.

## value

PASS

As mathematics, the exhaustive structure on this natural dense family is useful: it answers the motivating minimum-structure and sharp-bound questions for every terminal placement and counts all feasible deletions as well as the optimizers. This is not an independently new contribution given the broader coverage documented on the originality axis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
