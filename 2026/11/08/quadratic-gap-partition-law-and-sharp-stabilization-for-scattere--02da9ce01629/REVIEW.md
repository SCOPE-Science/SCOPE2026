# Scientific review

## Correctness — PASS

The claim applies to *scattered* `010` occurrences in indexed binary words. Formula (6) follows by assigning each occurrence to its central one in a unique zero-gap decomposition; the two exterior gaps are unconstrained, giving a direct bijection behind the formal generating function. For fixed positive frequency \(k\), the minimum interior-gap weight \(t-1\) bounds the number of zeros by \(k+1\), making the coefficient polynomial finite. The crucial global length inequality \(t+\sum g_j\leq k+2\) is proved algebraically and its equality cases are enumerated exactly, yielding the three highest-degree contributions (one when \(k=1\)) and the sharp stabilization boundary. Two independently written finite algorithms passed all stated tests; these are checks, not substitutes for the all-parameter proof.

## Originality — PASS, with residual priority risk

The motivating June 30, 2026 preprint by Bruda proves *eventual* polynomiality and a degree criterion for every binary scattered pattern with at least two runs. Its direct implication for `010` is only eventual degree one; it does not specify the full polynomials, the quadratic-weight partition series, or the sharp starting length. Menon–Singh (2023) handles frequencies through four and proves the zero-frequency enumeration, so none of those earlier cases is claimed independently. Tian (2025) supplies occurrence and primitive-word construction algorithms, but does not state the explicit all-frequency result or the universal transition. Searches for equivalent formulas, partition-weight presentations, exact tables, and the polynomial boundary did not reveal a dominating statement; absence from search indexes is not a novelty proof. An unindexed equivalent specialization remains possible.

## Value — PASS

The smallest nonmonotone three-letter scattered pattern is a canonical test case for quantitative subsequence-frequency enumeration. Rather than only establishing eventual polynomial degree, the finding determines the entire joint length/frequency distribution via finite, computable quadratic-weight partitions for each fixed positive frequency. It gives all leading coefficients by a locally finite infinite product-series, identifies a *sharp* linearity transition at \(n=k+1\), and computes its exact boundary defect. These are structural all-parameter assertions that cannot be read off from the previously known eventual-degree theorem; their coefficients show irregular arithmetic behavior, not merely a substituted binomial count.

## Closest literature and limitations

- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578 (2026-06-30), especially Theorem 1.4, proof in §2, and §4.
- K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870 (2023-06-13), especially §3. Earlier frequencies \(k\leq4\) and the avoidance count are not asserted to be new.
- R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205 (2025-07-03), especially §§4–5 on occurrence enumeration and primitive words.

The formula is specialized to `010`/`101`. No explicit elementary asymptotic of its slope sequence is claimed. The proof is symbolic; checks are finite; historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
