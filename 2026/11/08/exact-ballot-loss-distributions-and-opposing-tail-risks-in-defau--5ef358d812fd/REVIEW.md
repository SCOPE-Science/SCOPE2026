# Scientific review

## Correctness — PASS

The claim concerns finite loopless functional graphs with identical independent non-casting probability \(p\in(0,1)\), and counts unrepresented **unit** ballots. A functional component consists of one directed cycle and its incoming forest. Conditional on all cycle voters abstaining, a tree root is either casting (zero lost ballots downstream) or noncasting (one lost ballot plus independent child losses), yielding the exact generating-function product. The first moment follows by path length. The maximum expectation and any-loss probabilities follow from the restriction that every directed cycle has at least two vertices and the strict inequality \(p^2>p^3\). The six-voter counterexample is a direct calculation with independent cycle-failure Bernoulli variables. A separate, exact-rational brute-force checker passed 16,739 complete graph profiles through six vertices, with 2,534 independent checks of full distributions; these computations are supporting tests, not the infinite proof. All equality conditions and finite endpoints were checked within the stated scope.

## Originality — PASS with residual risk

Brill et al. (2026, arXiv:2607.12610, full text Section 2 and Appendix B.4) already derive expected loss and prove in Proposition 19 that a Hamiltonian cycle **minimizes** expected loss. The known model, path probabilities, and this minimization are explicitly excluded from the novelty claim. That result does not state the full lost-ballot probability distribution, the sharp *maximizing* network structures with equality, or the mean/tail inversion. Grossi et al. (2026, arXiv:2608.13188) measure expected influence via random-walk-decay centrality, a different aggregate from the stochastic total-loss distribution. Earlier binary-aggregation/cycle-abstention research by Christoff and Grossi (2016) concerns a different model. Targeted published-literature searches and mathematically oriented indexed-record searches found no equivalent full statement. Residual risks: alternative network reliability formulations, unindexed literature, and material beyond the accessible sections of the additional sources.

## Value — PASS

Exact total-loss probabilities permit reliability questions unavailable from a first moment alone, including a network's chance of **any** excluded voter and the chance of a major representational outage. The complete sharp maximum and uniqueness clauses clarify which delegation-cycle structures are most vulnerable. The strict six-voter reversal shows that the networks maximizing mean loss need not maximize consequential tails, a structural warning against mean-only network design. The result is restricted but directly motivated by previously studied loss in suspendible delegation networks.

## Limits and status

The result requires independent homogeneous turnout and forbids self-delegations. It does not claim improved election outcomes, strategic equilibria, or new knowledge of the established minimum-mean topology. No external independent review has been conducted.

Self-review: passed. Independent audit: not yet performed.
