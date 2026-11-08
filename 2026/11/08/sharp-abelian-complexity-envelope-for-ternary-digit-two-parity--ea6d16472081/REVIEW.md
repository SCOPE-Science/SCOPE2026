# Scientific review: ternary digit-two parity Abelian complexity

## Correctness — PASS

The proof covers every integer \(k\ge0\) and every factor length \(1\le n\le3^k\). The key prefix-extrema recurrence is exact because signed supertiles concatenate as \(W_kW_k(-W_k)\), with unit total sum; it yields \(M_k=k+1\) and \(m_k=\min\{0,2-k\}\). Every short factor crosses at most one aligned supertile boundary, so the three explicitly bounded cases cover all factors, including degenerate endpoint cases. The fixed-point factor language is complement closed; the observed opposite extremal windows and the sliding-window interpolation prove exactly \(2k+2\) Parikh classes at the geometric scales. The accompanying program reproduces finite boundary cases but is not used as an infinite proof.

## Originality — PASS, subject to historical-priority risk

The October 2026 source addresses a different morphic parameter and asks about other parameters, including the studied binary specialization. The 2013–2014 general uniform-binary classification gives an asymptotic upper order in the positive-excess case but does not yield the exact sharp geometric-scale envelope or logarithmic coefficient. The 2016 general computation paper was identified, but its complete text could not be accessed; the accessible abstract describes an algorithmic regularity result, not the stated explicit formula. Searches for the exact substitution, its ternary-digit-parity equivalent, the power-of-three formula, and related general growth statements did not uncover covering results. Search incompleteness and possibly unindexed prior specific computations remain risks.

## Value — PASS

The sharp constant and exact scale-by-scale maximum settle an infinite structured special case of the lower-growth issue for uniform binary substitutions with unit image-count difference and positive excess. This distinguishes actual logarithmic growth from the previously established generic upper estimate and links it to a concrete base-three automatic word. The proof gives an explicit structural mechanism, not an arbitrary finite table or numerical improvement.

## Scope and limitations

The claim is not an all-length exact complexity formula, nor an all-parameter classification. An independent scientific audit and comprehensive publication-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
