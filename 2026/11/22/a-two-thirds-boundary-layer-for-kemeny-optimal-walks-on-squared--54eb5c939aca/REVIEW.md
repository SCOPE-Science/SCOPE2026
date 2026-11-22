# Scientific review: A two-thirds boundary layer for Kemeny-optimal walks on squared cycles

## Correctness — PASS

For all integers \(n\ge5\), the zero-target Kemeny sum is the inverse trace of \(I-P\) on the mean-zero subspace. It is strictly convex as a function of the independently adjustable edge probabilities on connected feasible graphs. Rotation averaging plus uniqueness identifies the unrestricted minimizer with a two-parameter circulant walk; removing diagonal holding then fixes its probability budget. Fourier eigenvalues yield a strictly convex scalar objective with one interior root. The exact resolvent follows from partial fractions and a Poisson-kernel sum over roots of unity. Uniform boundary-layer estimates and a unique limiting scalar minimizer prove the \(n^{-2/3}\) scale and exact correction. The standalone checker passed 986 finite diagnostics, including separate matrix inversion; those tests do not certify the infinite analytical claims.

## Originality — PASS, subject to access and publication risk

The general symmetry method of Boyd–Diaconis–Parrilo–Xiao (arxiv:0709.0955v1), the resistance-design framework of Ghosh–Boyd–Saberi (DOI:10.1137/070689413), and the Kemeny convex/SDP framework of Patel–Agharkar–Bullo (DOI:10.1109/TAC.2015.2426317) cover general techniques, not the explicit squared-cycle Kemeny optimizer in the read portions. Doi et al. (arxiv:2110.12614) derive hitting times for the fixed equal-edge squared-cycle walk only. The closest published squared-cycle optimization records concern SLEM and \(n^{-2}\) one-hop weights; they do not state the inverse-trace solution or the new asymptotic order. Their full manuscripts could not be materially inspected; conclusions about their uninspected contents are withheld. Another equivalent source may exist.

## Value — PASS

The family is the simplest cycle with a local competing two-hop route. The exact n-dependent probability allocation, a positive-to-vanishing short-step boundary layer, and the quantitative fourfold leading Kemeny improvement make the precise invariant worth determining beyond generic convex optimization. The second asymptotic term distinguishes competing near-optimal allocations and explains why the dominant two-hop network alone is not optimal at finite size.

## Limitations

Only symmetric, uniform-stationary stochastic walks on \(C_n^2\) are covered. No claims for other long jumps, priced conductances, biased or directed walks. The scientific status is a same-model analytical review, not independent certification; finite computations only test examples. Publication priority remains qualified by full-text access and indexing gaps.

Self-review: passed. Independent audit: not yet performed.
