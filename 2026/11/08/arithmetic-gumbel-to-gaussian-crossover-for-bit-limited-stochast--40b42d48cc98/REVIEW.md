# Self-review

## Correctness — PASS
The exact transition follows from the integer identity \(\lfloor 2^rj-j/q\rfloor=2^rj-\lceil j/q\rceil\). Independent geometric holding times yield the entire finite distribution and moments. For fixed \(q\), coupling the waiting times with exponential spacings proves convergence to an average of \(q\) independent Gumbel variables. For diverging \(q\), a uniform third-moment bound and a two-case Lyapunov estimate prove the normal law. Boundary assumptions are explicit; the executable checker supports the finite identities with 6,961 checks. This is self-review, not independent certification.

## Originality — PASS, with priority risk
Closest literature: El Arar–Fasi–Filip–Mikaitis 2026 gives the limited-precision rounding convention and finite computation error bounds; Fitzgibbon–Felix 2025 quantifies rounding bias; Xia–Massei–Hochstenbach 2025 proves fixed-point gradient-descent expected convergence bounds; Hathcock–Strogatz 2021 establishes broad extinction-time universality, including Gumbel and Gaussian cases. These general antecedents are acknowledged, so the paper does not present those categories alone as new. The more specific exact bit-dependent pure-death kernel, \(q\)-Gumbel average and all-diverging-\(q\) normal law were not located in the inspected relevant sources or mathematical-record searches. A specialized unindexed equivalent and the possibility of a direct corollary of a general Markov theorem remain residual risks.

## Value — PASS
A finite random-bit probability budget is a concrete design constraint in low-precision fixed-point computations. The theorem gives exact termination-time means, variances and tails for a natural scalar descent benchmark, and exposes a change of fluctuation shape from one Gumbel to a \(q\)-fold average to Gaussian. The distinction matters for probabilistic iteration budgets even when first-moment convergence bounds already exist. The result is not a general algorithmic convergence guarantee.

Self-review: passed. Independent audit: not yet performed.
