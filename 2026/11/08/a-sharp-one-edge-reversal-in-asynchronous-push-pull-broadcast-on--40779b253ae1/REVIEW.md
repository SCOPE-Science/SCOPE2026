# Mathematical review

## Correctness (C): PASS
The independent edge-clock construction agrees with the standard asynchronous protocol. The two competing initial events on the augmented star, the subsequent two state cases, and the Laplace transform of the maximum of \(m-2\) exponential random variables produce the exact expectation. The cleared-denominator identity holds by rational algebra; the polynomial positivity argument covers all \(m\ge6\), while exact rational boundary values settle \(2\le m\le5\). The product bound proves the asymptotic gap. A distinct labeled-state dynamic program cross-checks 20 finite graph cases, without replacing the infinite proof.

## Originality (O): PASS, qualified
The closest foundational source is Acan et al., arXiv:1411.0948, Proposition 13 and Section 2: it gives the exponential-edge method and ordinary-star asymptotics, but not the exact edge-addition comparison. Daknama et al., arXiv:1902.07618, Sections 1 and 3, examine graph-edit robustness through *synchronous* rounds and expander edge deletions, not this exact asynchronous finite family. Doerr–Kostrygin, arXiv:2303.11150, concerns principally synchronous complete-network protocols. An independently identified deterministic graph-burning statement includes stars with one added leaf edge, but uses a different evolution and invariant. Direct comparisons of the statements and their assumptions found no implication to the present sharp threshold. Searches are not a uniqueness certificate; omitted or inaccessible published sources might contain equivalent work.

## Value (V): PASS
This is a natural, narrowly defined robustness question: does giving the informed leaf one additional neighbor always speed dissemination? The theorem identifies an exact reversal at five leaves, which cannot follow from the star expectation alone, and shows an asymptotically persistent \(1/3\) penalty. The threshold is an all-parameter structural comparison, not a routine finite-table computation. It isolates a degree-normalization mechanism that may matter when adding social-network links.

## Limits and literature
The setting is one source leaf, one added incident leaf edge, unweighted graphs, independent rate-one calling clocks, and expected complete dissemination time. The result does not claim a universal smallest graph or stochastic dominance. Sources: https://arxiv.org/abs/1902.07618 ; https://arxiv.org/abs/1411.0948 ; https://arxiv.org/abs/2303.11150 . Historical priority remains a qualified assessment.

Self-review: passed. Independent audit: not yet performed.
