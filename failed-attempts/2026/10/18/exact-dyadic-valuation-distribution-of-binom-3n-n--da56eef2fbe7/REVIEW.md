# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 26–47. Kummer counts carry-outs in n+2n, including exactly one possible extra carry beyond the k padded input digits, from state (1,1); the next position cannot carry. The two middle states have identical outgoing weights and equal terminal weight, so can be merged. The three continuation equations are A=1+x(A+B), B=1+x(A+zC), C=z+xz(B+C). Eliminating gives the stated rational function. Its denominator equals (1−x−x²)(1−xz)−x²(1−x)z², which gives the Fibonacci zero layer, no single-carry layer, and the stated degree-two and degree-three functions. Differentiation at z=1 and coefficient extraction give both finite moments, including the k=0 boundary; the linear and constant variance terms are 11k/12 and −14/9. Independent bounded replay: for k=0..14 histogram 2*n.bit_count()−(3*n).bit_count() over 0<=n<2^k using Legendre's formula. The 32,767 length–index pairs agree with the polynomial recurrence, low strata and both moments. The frozen script and VERIFICATION.md were inspected, not executed; the finite check is not the proof.

## originality

FAIL

Distinct same-day Resultary record 767a9e2b871f demonstrably covers the full claimed marginal at every cutoff. Its bivariate law gives exactly this rational function on setting the first valuation's weight to one, including the same terminal carry weight and the explicitly printed finite mean. The low strata, second factorial moment and variance follow mechanically. This is a failure of independent scientific distinctness on the evidence, not a chronological or authorship judgment: no authoritative within-day priority was established.

## value

FAIL

The complete dyadic distribution is a meaningful invariant in itself, but this separate package adds no independently useful unknown exact fact beyond the fully covering joint law. The marginal and its finite corrections are immediate specialization, coefficient extraction and differentiation; printing the second factorial moment explicitly is not a distinct mathematical gain. No surviving nonmechanical claim warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
