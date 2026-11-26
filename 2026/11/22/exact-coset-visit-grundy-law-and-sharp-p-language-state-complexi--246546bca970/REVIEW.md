# Independent mathematical audit

## correctness

PASS

The product of the suffix after prefix j is p_j^{-1}p_n, so its membership in H is equality of the left cosets p_jH and p_nH, without normality. The legal predecessors are the earlier visits to that coset, ordered with Grundy values 0 through one less than the number of such visits, by induction and mex. The prefix-product map is a bijection on G^n. Conditional on the final coset, the first n−1 nonempty prefix products match it independently with probability |H|/|G|. The conditional count does not depend on the final coset, so adding the empty-prefix match adds an independent Bernoulli variable of the same parameter. The empty word has value zero. For normal H, the quotient state x and the visited set V induce the normalized state T=x^{-1}V containing 1, plus a freshness bit. Reading y takes T to y^{-1}T ∪ {1}, with freshness iff y is not in T. For T≠{1}, choose x=t^{-1} with t∈T other than 1, visit the elements of xT starting at 1 and ending at x for the first time, then append an identity letter to obtain the other freshness bit. The full alphabet permits every transition. The empty continuation distinguishes different bits; a letter from the symmetric difference of two sets distinguishes different sets. This proves exactly 2^[G:H] states including the H=G and H={e} cases. Independent bounded check: python3 /workspace/checks/frozen_math_checks.py 4 computes signatures from raw, unnormalized S3 histories for subgroup orders 1, 2, 3, 6 and finds 64, 8, 4, 2 distinct signatures respectively.

## originality

PASS

The general regularity of Grundy level sets and the strongly Bernoulli decomposition are prior input, not the contribution. The combination of a pointwise left-coset visit law, its exact uniform-word binomial histogram, and a tight full-alphabet Myhill–Nerode count survives the inspected comparisons.

## value

PASS

A finite-group product condition is a natural family of regular suffix-deletion rules. The theorem determines every game value and its full uniform-input law, and shows an exponential separation between a small rule automaton and the minimal complete P-position recognizer over the full alphabet. The exact state count and short distinguishing continuations are meaningful beyond a census of small groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
