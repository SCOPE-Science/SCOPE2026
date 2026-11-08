# Scientific review

## Correctness — PASS

The infinite theorem is a uniform consequence of elementary lower and upper bounds for odd-multiplicity binary partitions and a large-deviation estimate for how many levels are occupied. The explicit support-count inequality ensures that the exceptional set of partitions with fewer than \((1-\varepsilon)m\) positive power levels is exponentially negligible relative to all partitions. Weighting each partition by its number of optional overlines produces the claimed logarithmic ratio; the \(N=1\) boundary and even-index reductions are described. The standalone checker validates the recurrence/partition interpretations for \(1\le N<130\) and the reported finite values. It does not certify the limit by experimentation.

## Originality — PASS with residual literature risk

Ballantine and Beck's 2023 paper gives the two partition models and in Section 12 explicitly proposes comparing the asymptotic growth of their odd-indexed subsequences. Keith and Munagi's earlier work describes the semi-Pell composition model and generating function, not this relative exponent. OEIS A030067 and A129095 have both original sequences and enumerations, but not the near-full-support concentration theorem or the \(N^{1+o(1)}\) comparison. Searches under sequence names and their equivalent overpartition/weighted-binary-partition formulations found no matching stronger published claim. General asymptotic theorems indexed differently may still dominate this result; Andrews's original 2019 article PDF was unavailable at the journal download link.

## Mathematical value — PASS

The open growth-rate comparison is naturally sensitive to a second-order scale: each sequence has logarithm of order \((\log N)^2\), whereas the logarithm of their ratio has order \(\log N\). The present proof determines the coefficient of that relative scale sharply as one. This distinguishes the enumerations quantitatively without claiming an unproved multiplicative constant, and the support-concentration argument explains the phenomenon.

## Limits and literature

The finding does not give an asymptotic constant, a sharp error term, or comparisons with semi-Tribonacci, semi-Padovan or semi-Lucas. The closest inspected primary sources are Ballantine–Beck (arXiv:2303.11493v1, Sections 1, 6, 12) and Keith–Munagi (Online Journal of Analytic Combinatorics 18, Paper 2, Sections 1, 2, 5). OEIS A030067 and A129095 supply exact sequence records; Andrews (2019) is cited for the original partition model.

Self-review: passed. Independent audit: not yet performed.
