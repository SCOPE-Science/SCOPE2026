# Scientific review: two-hub host social-distancing network creation

## Correctness — PASS

The domain is connected spanning subgraphs of a fixed host with exactly two hubs and at least three leaves, with all utilities specified and equality handled by strict-improvement rules. For each permitted edge addition, a hub's distance sum falls by two and a leaf's by twice one plus the number of opposite-only leaves. A permissible deletion reverses those increments. Exhaustive case distinction in \(c=1\) and \(c\ge2\) proves every and only listed equilibrium type. Labeled counting uses disjoint assignments, and each edge move changes the proposed potential by the exact improvement threshold, which gives termination on finitely many count triples. The attached verifier separately computes BFS distances and exact rational payoffs rather than assuming the local formulas; 465,792 direct checks, 90 counts and 116,928 potential comparisons passed. Finite tests are not used as proof of the infinite statement.

## Originality — PASS, subject to publication-priority risk

The initiating full article (Friedrich et al., 2023; preprint April 2022) was examined in its model, potential counterexample, all-host stability bounds, and intermediate stability guarantee. These are not the present iff classification, exact labeled census or potential for the **noncactus** two-hub host \(K_{2,k}\) for all positive reward parameters. Its generic no-potential theorem does not contradict the positive restricted-host theorem. Search terms covered both \(K_{2,k}\)/complete bipartite hosts and potential/equilibrium/phase terminology, including structural neighbors; no covering claim was identified. The work is distinct from cactus-only host classifications because three or more four-cycles share edges. Remaining risks are undocumented equivalent specialist classifications or a hidden derivation in unexamined literature; failed retrieval is not proof of absolute novelty.

## Value — PASS

The question is natural within host-restricted network creation: exact stable networks and convergence in a family that is not a tree and not a cactus, while the general game admits improvement cycles. The complete parameter diagram reveals resonant equilibria at isolated tie values, and the count provides the quantitative multiplicity. A simple strict ordinal potential and explicit, uniform polynomial improvement bound explain why decentralized local dynamics converge here. These are structural results, rather than a parameter rewording or a finite census without mathematical motivation.

## Relationship and limits

Closest full-text source: Friedrich et al., *Social Distancing Network Creation*, DOI:10.1007/s00453-022-01089-6, Sections 1.1, 2.1, 3.2 and Theorems 4, 9, 10. See RESULT.md and AUDIT.json for scientific comparisons. This does not settle larger complete bipartite hosts, all-host potentials or optimal convergence length. Publication priority remains susceptible to inaccessible or unindexed equivalent results. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
