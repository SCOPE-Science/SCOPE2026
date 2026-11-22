# Review of the affine peak law and one-sixth deletion transition

## Correctness — PASS

The labelled graph is unambiguously specified for all integers \(n\ge2\), \(0\le m\le n\), including the disconnected boundary \((n,m)=(2,2)\). The proof conditions on the highest-labelled vertex's shore and decomposes the peak count into the initial same-shore run plus at most one extra peak. The two exclusive extra-peak mechanisms have conditional probabilities \(m(n-k)/n^3\) and \(\mathbf1_{k=1}m(2n-1)/n^3\), respectively. This derives the entire finite distribution, not only the mean. The product expansion has uniformly summable error and exponentially small tails, establishing the \(O(n^{-2})\) total-variation remainder uniformly over the deletion count. An independent vertex-subset dynamic program and direct permutation enumeration exactly reproduce all tested cases. The arbitrary-order result rests on the proof; finite computations alone are not an infinite proof.

## Originality — PASS, provisional historical priority

The eligible source *The Exact Stabilization Time of Self-Stabilizing Coloring: Mean, Variance, and Distribution* (arXiv:2611.17989v1) identifies the peak/recolouring equivalence, gives general moment identities, and treats bipartite Erdős–Rényi models. Its inspected relevant sections and appendix do not give the law on \(K_{n,n}\) after deleting a matching, the exact affine-mixture identity, or the one-sixth sharp total-variation transition. The general equivalence is inherited, not new. *Twin peaks* studies random labellings with conditioned peaks on grids and trees, not the evaluated matching-deletion family. The indexed description of Baldi–Rinott–Stein concerns normal approximation on general graphs; its full archival report was not accessible, so historical coverage cannot be conclusively excluded. Related published calculations on crown-graph FirstFit colouring and random greedy matching concern different stochastic rules and do not imply the present peak distribution. Prior-claim and source searches showed no stronger covering evaluated formula, but search absence is not a proof of absolute novelty.

## Value — PASS

The exact, all-order distributional identity shows that deleting any number of independent cross-edges changes the peak law *affinely*, despite strong dependence among local maxima. The sharp limiting total-variation coefficient is nonmonotone: it decreases under initial matching deletion, attains its unique minimum at density \(1/6\), and then increases. This quantitatively exposes a structural robustness-and-crossover phenomenon in random-order local maxima on a natural dense bipartite family, and translates directly to recolouring counts for the established random-daemon model. It is not a mere degree-sequence mean or an arbitrary finite table.

## Closest literature, checks and limitations

- É. de Panafieu et al., arXiv:2611.17989v1, Sections 1, 3, 5.4 and Appendix F: underlying peak-process identity and bipartite random-edge model, but no evaluated matching-deletion law.
- K. Burdzy and S. Pal, arXiv:1606.08025, especially introductory and graph-labeling sections: random local maxima, but different graph families and conditioned questions.
- P. Baldi, Y. Rinott and C. Stein, Stanford report EFS NSF 306 (1988): landing page available, complete report not accessible; residual priority uncertainty.
- Published indexed crown-graph studies on random-order FirstFit colouring and greedy matching: similar graph objects but different observables, with no demonstrated implication to the peak law.

The result does not extend to arbitrary deleted edges, unequal bipartitions or nonuniform priorities. Its limiting comparison is to the fixed geometric distribution on positive integers. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
