# Scientific review

## Correctness: PASS

The proof correctly separates same-part moves, whose occupied closed-neighborhood ratio is unchanged, from cross-part moves. The latter project onto adjacent vertices of a single interval of length at most \(2\min\{a,b\}\); explicit forward gains depend only on color counts and have exactly opposite signs in reverse. A potential obtained by summing these edge signs strictly increases by one on each improving jump. The projected sinks are exactly Nash equilibria, and independently counting labeled vertices, color placements, and labeled agents gives the displayed equilibrium census. Exact-rational direct-move and equilibrium checks passed 600 instances (719,520 single-agent jumps). The finite checks are independent corroboration of the all-size mathematical proof, not an infinite certificate.

## Originality: PASS, with residual literature risk

The closest initiating primary article is Friedrich et al., *Single-Peaked Jump Schelling Games* (arXiv:2302.12107): its Theorem 3.2 already implies existence in some/all relevant bicliques and is **not** claimed as new. Its Theorem 2.4 concerns a special half-peak cycle, and its other dynamics results include nonconvergence on different topologies; these do not imply an all-utility biclique ordinal potential, a uniform length bound, or exact labeled-equilibrium counts. Narayanan et al., *Diversity-seeking Jump Games in Networks* (arXiv:2305.17757), obtain a potential for a fixed linear diversity payoff on regular and spider graphs, including an overlapping balanced-biclique special case, but not the stated arbitrary-function and all-biclique result. Kanellopoulos et al. (arXiv:2005.12149) introduce the closed-neighborhood normalized utility and show cycles can occur on trees in a broader model, rather than proving this restricted topology theorem. The graph-based source Agarwal et al. (arXiv:1902.07937) studies a different utility convention. Searches for one-vacancy Schelling dynamics, complete bipartite potential games, and the equivalent two-type count quotient found no direct covering statement. Search failure is not novelty proof; unindexed material and equivalent mathematical reformulations remain possible.

## Value: PASS

The contribution resolves convergence, the maximum number of strict steps, all equilibrium states, and exact equilibrium multiplicities uniformly for an infinite network family with all type-homogeneous payoffs. In a literature where nonconvergent jump cycles occur even with one vacancy on other graphs, a simple network topology that forces convergence irrespective of nonmonotonicity identifies a structural boundary. The count is an exact structural classification, not an arbitrary finite instance or a renaming of a general existence theorem.

## Scope and limits

Exactly one vacancy, two colors, complete bipartite adjacency, and type-homogeneous arbitrary real payoffs evaluated on occupied closed neighborhoods are essential. The result does not cover more vacancies, agent-specific utilities, nor arbitrary graph topologies. External independent audit and exhaustive bibliographic priority confirmation have not been performed.

Self-review: passed. Independent audit: not yet performed.
