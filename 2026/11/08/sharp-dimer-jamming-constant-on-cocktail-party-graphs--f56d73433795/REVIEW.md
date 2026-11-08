# Self-review

## Correctness — PASS
The exact lumped transition recurrence follows from disjoint counts of singleton–singleton, singleton–intact-pair, and inter-pair admissible edges. A finite jam can leave only one deleted pair. One-tag survival, two-tag survival, a conditional union bound and a unique-surviving-pair completion product furnish a non-experimental proof that \(nq_n\to3/4\), with quantitative remainder \(O(n^{-1/3})\). Critical conditional inequalities are algebraically verified in the supplied symbolic script. A distinct labeled-state exact recursion agrees through seven forbidden pairs. Boundary cases \(n=2\), \(L=2\), and zero-coefficient state transitions are handled explicitly.

## Originality — PASS on inspected evidence; provisional historical priority
Gamarnik–Goldberg, arXiv:0807.1277, establish greedy matching results under constant-degree and/or girth restrictions, which cannot produce the stated \(3/4\) coefficient for degree growing with size and triangles. Johnston–Kayll–Palmer, arXiv:2209.11319, treat static perfect-matching counts on the very same cocktail-party graphs, whereas this theorem concerns a dynamic process that can jam before perfection; static counting does not imply its law. Dyer–Frieze and Pippenger give foundational random greedy matching and adsorption methods, but their full original papers were not accessible for exhaustive comparison. Accessible published-result searches and source inspection did not locate the stated exact graph-family jamming recurrence or limit. No failed search alone establishes novelty. Equivalent unindexed calculations remain possible.

## Mathematical value — PASS
Cocktail-party graphs are a canonical highly connected family admitting perfect matchings. Nevertheless irreversible random deposition has a nonzero finite-size jamming probability, quantified sharply by \(q_n\sim3/(4n)\). The proof resolves a natural kinetic question and demonstrates how correlated forbidden pairs determine the leading finite-size defect coefficient. The exact all-size recurrence and rigorous two-tag bound provide reusable quantitative methods beyond a numerical table; no downstream theorem is required.

## Limits and literature
This statement is not a uniform-rates generalization, a thermodynamic phase transition, a complete characterization of other multipartite graph families, or a comparison with all possible deposition schemes. Previous full-text coverage is incomplete for Dyer–Frieze 1991 and Pippenger 1989. Mathematical sources: https://arxiv.org/abs/0807.1277 ; https://arxiv.org/abs/2209.11319 ; https://doi.org/10.1002/rsa.3240020104 ; https://doi.org/10.1137/0402034.

Self-review: passed. Independent audit: not yet performed.
