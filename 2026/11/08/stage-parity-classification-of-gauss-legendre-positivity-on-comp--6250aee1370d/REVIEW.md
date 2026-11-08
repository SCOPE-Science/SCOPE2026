# Self-review

## Correctness — PASS

The claim follows from an explicit spectral decomposition of every complete multipartite Laplacian, not numerical sampling. The nonstandard central lemma is proved coefficientwise: the rational quotient of the even and odd parts of the diagonal Padé polynomial is nondecreasing, so the normalized Padé decrement is strictly decreasing. An exact integration-by-parts identity makes the even-stage scalar Padé multiplier positive for every positive argument. The odd-stage stiff-limit matrix and the separate two-vertex case complete the classification. The finite symbolic and rational checker passed 741 assertions; it supplements, and does not establish, the infinite stage-number theorem.

## Originality — PASS, qualified

Banjai and Ferrari (arXiv:2212.07170) establish the Gauss/Padé stability-function machinery but not the graph heat matrix-positivity classification. Zappavigna, Colaneri, Kirkland and Shorten (doi:10.1016/j.laa.2011.12.021, especially Section 4) analyze positivity obstructions and Hurwitz-system restrictions, not this all-steps conservative graph family. Related special cases concern explicit RK4 on multipartite graphs and two-stage Gauss on strongly regular and cycle graphs. These are not claimed new for their overlapping special cases. Comparisons of mathematical statements in related literature did not show an implication covering all stage numbers and unbalanced part sizes. Specialist terminology and historical publications are residual originality risks, not proof of absence.

## Value — PASS

The theorem supplies a natural exact classification, across arbitrary graph sizes and numerical orders, of when an A-stable high-order collocation step also obeys a discrete maximum principle. All offdiagonal entries remain positive regardless of parity, and the entire obstruction for odd stages is the asymptotic diagonal. The distinction between complete multipartite networks and general generators is structurally informative for positive numerical integration.

## Limits

Only unweighted undirected complete multipartite Laplacians, one-step endpoints, and exact arithmetic are covered. No positive internal-stage assertion, generic Markov operator theorem, odd-stage finite threshold, or unconditional physical accuracy claim is made. Independent scientific review is not included.

Self-review: passed. Independent audit: not yet performed.
