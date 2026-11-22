# Scientific review: threefold ternary Cantor convolution

## Correctness — PASS
The count of binary input-digit triples is \((1,3,3,1)\), giving exact carry matrices for carries zero and one. Tensor squaring and summing over each output digit gives \(T\). The exact vector identity \(T^2w_0=26Tw_0-90w_0\), not numerical extrapolation, proves the energy recurrence for **all** depths. The stationary carry law \((4/5,1/5)\) is checked by rational multiplication and gives the stated output frequencies; finite-state ergodicity supplies the a.s. limit. Direct no-carry digit realizations prove full support, and convolution with an atomless factor proves non-atomicity. The standard Haar digit strong law separates measures. The delivered checker performed 9,993 exact tests; the infinite arguments are in RESULT.md. Boundary \(k=0\), carries beyond the modulus, and ordered versus unordered summands were accounted for.

## Originality — PASS with historical-priority risk
The closest inspected primary source is Abram–Lagarias, *p-adic path set fractals and arithmetic*, arXiv:1210.2478, especially Theorem 1.3 and §4.2. It proves closure of support sets under Minkowski addition via an unweighted automaton, but no displayed exact measure-specific weighted energy law or almost-sure output digit frequencies for three independent fair Cantor summands. The separate multiplicative-intersection paper concerns other sets; Nazarov–Peres–Shmerkin concerns real convolutions with different scales. Searches for the same threefold law, its energy recursion, and its algebraic dimension did not identify an exact covering theorem. The closest existing comparison of a distinct four-adic self-convolution with digits \(\{0,1,3\}\) has a different transfer law. An earlier weighted-carry theorem may imply the result implicitly; the absence of a matching search result alone proves no priority claim.

## Mathematical value — PASS
Three independent ternary Cantor factors have summed input dimensions \(3\log_3 2>1\), yet their sum measure is *still singular* on a space it supports everywhere. The exact nonuniform output-frequency vector gives a measurable obstruction, while the algebraic collision dimension quantifies its persistent concentration at **every modular depth**. The simple support equation \(C+C=\mathbb Z_3\) would not determine either statistic. This is a complete natural arithmetic-measure invariant, not a chosen finite slice or a renaming of the unweighted path-set closure theorem.

## Residual limits
The reviewed claim concerns precisely the triple fair-digit convolution over \(\mathbb Z_3\). An unrecognized general weighted-carry formula or unindexed earlier computation could cover it. Independent confirmation of originality and the full mathematical proof has not been performed.

Self-review: passed. Independent audit: not yet performed.
