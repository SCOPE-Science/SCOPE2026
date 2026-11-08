# Review of the finite-round pull source reversal

## Correctness
PASS. The binomial conditioning argument gives a closed, exact two-round probability. The independent binomial transitions of the informed-count process form an exact finite Markov kernel. All stated fractions, signs and finite minima were separately verified by exact rational computation in `verify_pull.py`. The graph and update assumptions are explicit; the only finite census is the twenty unordered unequal bipartitions on at most ten vertices.

## Originality
PASS, with historical-priority uncertainty. Panagiotou–Reisser (arXiv:2110.09044) consider the homogeneous complete graph and its asymptotic pull runtime. Doerr–Kostrygin (arXiv:2303.11150) cover symmetric protocols in complete networks. Acan et al. (arXiv:1411.0948) study a different synchronous push-pull protocol and asynchronous variants. None of their relevant inspected formulations contains the two opposite source-conditioned CDF inequalities or the exact first two-round reversal cutoff. Broader bounds do not imply these exact opposite finite-time comparisons. Other undiscovered priority sources remain possible.

## Value
PASS. The first achievable completion time on a nontrivial complete bipartite graph is two rounds. The exact first reversal at eleven vertices and the three-round sign crossing provide a natural, sharply delimited obstruction to choosing a universally faster broadcasting source solely by its part size. This is a finite exact boundary result; no global source-order theorem or minimum stochastic-incomparability order is claimed.

## Scope and limitations
The claim uses independent simultaneous pull-only neighbour choices with persistent information. It does not transfer automatically to push, push-pull or asynchronous spreading, or to expected completion times. Exact rational verification is not independent auditing. Historical priority is qualified by the searched and inspected literature.

Self-review: passed. Independent audit: not yet performed.
