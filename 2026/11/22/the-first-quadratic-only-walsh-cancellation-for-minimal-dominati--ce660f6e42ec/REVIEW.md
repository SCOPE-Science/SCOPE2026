# Review of the finite minimal-domination Fourier finding

## Correctness — PASS
The membership test follows from the private-neighbor criterion, and its completeness for every one of the \(2^{17}\) masks is explicit. An independent incremental minimal-transversal algorithm reproduces precisely the same 268 masks and likewise agrees for each smaller order. Exact integer Walsh transforms determine all 131,072 coefficients and the canonical projection kernel; a translation-averaging lemma yields optimality among all projections. Every finite certificate checks out. No inference beyond path order 17 is made.

## Originality — PASS (bounded historical comparison)
The most relevant earlier work is the 2009 path domination polynomial of Alikhani–Peng a 2013 interval/permutation-graph minimal-domination enumeration and counting paper, and two 2014 minimal-domination enumeration papers by Kanté and collaborators. The former counts all dominating sets; the latter describe the right minimal family and algorithms but not signed Walsh zero sets. Published results for maximal independent sets on paths involve a strict subfamily, and complete-bipartite minimal-domination spectra concern a different graph class. Another previous path minimal-domination result concerns VC/Littlestone dimensions. These do not imply the specific 15 quadratic cancellations or norm. Residual risk: an unindexed or hidden signed-incidence table may already contain equivalent values.

## Value — PASS
The first-order/second-order separation gives a sharp natural finite cutoff: the first singular minimal-domination path with no vanishing singleton Fourier multiplier is \(P_{17}\). Its exact convolution rank and optimal recovery projection norm provide a reproducible benchmark for weighted domination-enumeration methods. Such a boundary result is of independent interest without an all-order theorem.

## Boundaries
No all-order classification, asymptotic estimate or external independent validation is claimed. The computation is exhaustive only for the explicitly stated finite range.

Self-review: passed. Independent audit: not yet performed.
