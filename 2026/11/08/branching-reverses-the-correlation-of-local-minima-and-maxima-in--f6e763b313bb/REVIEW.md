# Review: branching reversal of local-extrema dependence

## Correctness — PASS

For independent continuous vertex labels, the minimum and maximum indicators depend only on closed neighborhoods. The proof evaluates their same-vertex, adjacent-vertex and distance-two covariances by direct uniform integrals; all longer-distance terms vanish. The resulting exact formula counts degree-marked edges and distance-two pairs. For paths it simplifies to \(\operatorname{Cov}(M,P)=(8n-37)/180\) for \(n\ge4\). For the complete rooted \(m\)-ary tree, explicit configuration counts yield \(nL_m+R_m<0\) for all \(m\ge2,h\ge3\), while separately proved height-one and height-two formulas cover the boundary cases. Expansions in \(m-2\) have positive coefficients, proving the infinite sign claim. The large-height variance coefficient is strictly positive and determines the exact limiting correlations. The standalone `verify.py` checks 140 exact identities and finite enumerations, but finite enumeration is not used to prove any infinite assertion.

## Originality — PASS, with stated historical-priority risk

Krivelevich, Mészáros, Michaeli and Shikhelman, *Greedy maximal independent sets via local limits* (arXiv:1907.07216v1, 2019), study the **completed** greedy independent-set process and its expected size, although the introductory first-round parallel operation selects precisely the local minima under a random priority order. That is a different random variable and their stated theorems do not imply the two-sided first-round covariance. Burdzy and Pal, *Twin Peaks* (arXiv:1606.08025, 2016), study regular-tree peaks **conditioned** on exactly two peaks and their locations, not an unconditioned minimum–maximum count. Baldi, Rinott and Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph* (1989), study one-sided local-minimum statistics, especially normal approximation on regular graphs; they do not state this joint branching transition. Searches of published mathematical records returned nearby but non-covering random-greedy and tree covariance results. Historical priority cannot be certified solely by these searches.

## Value — PASS

A single random ordering on a tree is a natural coupled experiment. The result gives a sharp, all-heights topological boundary between positive large-path dependence and strict negative dependence on every complete branching tree, plus an exact binary-tree limit \(-19/33\) and convergence to perfect negative correlation as arity increases. It distinguishes initial parallel greedy selection from the eventual greedy MIS and supplies a meaningful structural dependence law rather than an isolated small-case computation.

## Limitations and sources

This does not classify all nonpath trees, assert intermediate-arity monotonicity, or address a joint central limit theorem. Exact computations corroborate but do not certify the analytic identities; independent verification of the mathematical argument is outstanding. Inspected primary sources: https://arxiv.org/abs/1907.07216v1 ; https://arxiv.org/abs/1606.08025 ; https://papers.neurips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf .

Self-review: passed. Independent audit: not yet performed.
