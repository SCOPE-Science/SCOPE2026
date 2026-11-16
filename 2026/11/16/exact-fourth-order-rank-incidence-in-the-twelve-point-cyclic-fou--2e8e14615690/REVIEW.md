# Scientific review

## Correctness — PASS

The claimed data concern exactly \(\binom{12}{4}^2=245025\) ordered pairs. The complex-to-finite-field equivalence is proved for **all** minors of size up to four using the four conjugate determinants and the strict inequality \(p>4^8\); it would be invalid to use an arbitrary small modulus instead. The two provided standalone programs use different primes with primitive twelfth roots and independently enumerate every restriction. Both passed, producing the same exact rank totals, and the Python program independently checks all 21 affine orbits, their disjointness, complete coverage and constant profiles. The 24 full-spark rows agree with an independently published classification. No numeric tolerance or extrapolation is involved.

## Originality — PASS under bounded comparison

Actual targeted searches included `Fourier matrix order 12 full spark subsets 4x4 minor rank distribution cyclic twelve roots of unity`, `cyclic 12 Fourier minors rank two 1224 rank three 39384 and nonsingular 204417`, and `complete 4x4 Fourier minor rank distribution of Z12 21 row profiles`. Directly inspected online records cover full spark for order 12, rank censuses for orders 15/16, and order-12 exact-support uncertainty. Their statements do not imply the new order-12 rank-count table or the 21 incidence profiles. Alexeev–Cahill–Mixon's primary full text and Delvaux–Van Barel's technical report were inspected for plausible stronger coverage; the former concerns all-or-nothing full-spark properties and the latter subgroup constructions/Hamming numbers, not the stated exact census. Search is not proof of historical priority; inaccessible or unindexed equivalent tables remain a residual risk.

## Mathematical value — PASS

Fourier submatrix rank is exactly the number of recoverable degrees of freedom from a prescribed four-frequency sampling pattern. The cyclic group of order 12 is the smallest mixed-prime-power Fourier order \(4\cdot3\), distinct from both pure prime-power and squarefree-product examples: its nested divisors generate several nontrivial rank-loss levels. The complete, natural 21-affine-orbit classification separates rank-two failures from rank-three failures and refines the previously known 24 full-spark row sets. It supplies an exact benchmark for nonuniform recovery rather than an arbitrary parameter perturbation. No general modulus or stability result is inferred.

## Principal limits and risk

This is an exact finite census, not a general theorem about all moduli; independent validation is outstanding. An unseen more general rank-incidence theorem would supersede the result, but none of the materially inspected relevant sources did so.

Self-review: passed. Independent audit: not yet performed.
