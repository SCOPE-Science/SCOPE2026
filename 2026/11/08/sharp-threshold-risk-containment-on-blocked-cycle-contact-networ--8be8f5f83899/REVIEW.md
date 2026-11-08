# Scientific review

## Correctness (C): PASS

The probability formula is derived by counting all open \(h\)-site windows and all qualifying maximal open clusters, with the uniform-seed size bias handled by summing cluster vertex counts. When two paths have length at least \(h\), a conserving replacement by one longer path and one \(h-1\) path strictly lowers the risk by \((h-1)p^h\); transfer from a long path to an undersized short one lowers it by a strictly positive linear slope. This proves the complete all-size minimizer and equality cases. The six-vertex transition is verified by exact polynomial signs, and sharpness below six is proved by the absence of two qualifying paths (for \(h\ge3\)) and an exact formula for \(h=2\). The mean objective has strictly positive discrete second difference. The standalone exact checker independently enumerates all retained-edge states in 2,964 finite comparisons and checks 990 partition-parameter cases. Its finite range is not an infinite proof.

## Originality (O): PASS within inspected evidence

Direct reading of Moore and Newman's percolation paper, Enright and Meeks's deletion paper, and Enns and Brandeau's full open-access article establishes three distinct prior contexts: local-cluster distributions, deterministic component-size constraints, and expected-infection algorithm comparisons. None of the inspected claims gives both a universal finite-ring **probability-tail** minimizer under a specified number of blocked edges and the smallest transmissibility-dependent **maximizer** switch with its contrast against the mean. Kenah and Robins emphasize that independent bond percolation must not be silently interpreted as generic SIR. Semantic research-record searches for cycle edge deletion, threshold events, gap partitions and the six-site crossover returned other network/percolation results without this implication. A closely related finite-path vertex-vaccination tail result was compared: it removes one vertex and conditions on the remaining uniform source, a different optimization domain and action, and does not imply the present multi-edge ring construction. Unindexed optimization tables and general graph-polynomial classifications remain a historical-priority risk. The zero-risk case is not independently advanced as novel.

## Value (V): PASS

The exact minimum is nontrivial when complete protection cannot be achieved, giving an explicit budget-and-threshold rule for all ring sizes. The sharp six-site example reveals a meaningful design contradiction: balancing the sizes of contact segments minimizes expected infections but can maximize the probability of crossing a threshold. This distinguishes two standard outbreak objectives under the same transmission assumptions and cuts, and supplies an interpretable, self-contained structural benchmark rather than an arbitrary chosen parameter sample. Not an empirical epidemic forecast.

## Boundaries and audit status

Primary mathematical source: Moore and Newman (2000), arXiv:cond-mat/0001393, submitted 2000-01-26. Later comparisons: Enright and Meeks (2015), Enns and Brandeau (2015), Kenah and Robins (2006), Ball et al. (2018). Relevant primary full texts were examined, except the last cited large-network work, for which abstract and method-level scope only were consulted. No external priority or expert certification has been asserted.

Self-review: passed. Independent audit: not yet performed.
