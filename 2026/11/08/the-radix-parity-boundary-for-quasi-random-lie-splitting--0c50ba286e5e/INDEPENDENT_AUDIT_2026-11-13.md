# Independent mathematical audit

## correctness

PASS

For R even, the leading radical-inverse digit decides upper/lower half of [0,1), hence ξ_n depends only on n mod R and is balanced with partial sums O(R). Uniform bounded-generator Lie local Taylor error is τ² ξ_j[A,B]/2+O(τ³). Product telescoping and summation by parts with W_{n,j+1}−W_{n,j}=O(τ) give bounded signed commutator sum and O(Nτ³)=O(τ²) remainder. For R odd, the central base-R digit alone recurses; block sums yield S_{m(R^k−1)/(R−1)−1}=1−mk. For A=E12,B=E23, AB=E13 is central and BA=0, so exact product equals exp(T(A+B)+τ² S_N E13/2) on e3 and yields the claimed norm for every N. For R=2 successive factors group into symmetric Strang propagation. All limits hold at fixed T, bounded A,B, exact subflows.

## originality

PASS

Best-of-knowledge PASS relative to the actual Li–Liu–Wan two-operator rule: their general discrepancy bound O(log N) and convergence theorem provide only O(τ² log N), not bounded even-base sign sums or a sharp odd-base 3×3 lower bound. Strang composition and digital discrepancy identities are known separate ingredients; the sharp rule-dependent arithmetic dichotomy survives.

## value

PASS

This precise parity boundary is a useful classification of convergence order for a natural quasi-random numerical scheme, including a matching counterexample that shows the logarithm cannot generally be removed for odd radices. Even-base full second order has direct method-selection significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
