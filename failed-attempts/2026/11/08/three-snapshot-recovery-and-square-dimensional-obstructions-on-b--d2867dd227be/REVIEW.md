# Independent mathematical audit

## correctness

PASS

Put T=Σxᵢ and u=n−2k. The trivial components of the three homogeneous Walsh spaces restrict to 1,u,(u²−n)/2. The centered degree-one map is injective by coordinate swaps, and the centered degree-two partner restricts to u times the same function since Σaᵢ=0. For edge coefficients with zero row sums, the shell value is four times their sum over pairs contained in A. In the squared norm of this sum, ordered pairs of equal, adjacent and disjoint edges contribute respectively D, −2D, D, where D=Σ|cᵢⱼ|²: the adjacent sum follows by squaring each zero row sum, and the disjoint sum by squaring the zero total sum. The probabilities that each type is contained in A give the positive coefficient in the proof. This sector is orthogonal to constants and point-standard functions by its zero total and row sums. The unsigned incidence has rank n over C (aᵢ+aⱼ identically zero forces all aᵢ=0), so the remaining visible sector has dimension n(n−3)/2. Distinct geometric sequences with bases 1,e^(−2τ/n),e^(−4τ/n) have the stated Vandermonde ranks in every sector, including at m=1. The resulting generic, central and square cases give exactly the asserted nullities. Independent replay: python3 /workspace/reproductions/frozen_checks.py 4 gives 80 bounded rank witnesses at heat step multiplier 1/3, including full stacked matrices at n=9,k=3 and 6. Modular pivots give lower bounds at this rational specialization, and the analytic argument supplies the upper bounds and all other heat steps. The frozen CHECK.py's last three assertions merely check a₀∈{2,3}; they do not independently verify square-resonant ranks.

## originality

FAIL

The full formula is a direct consequence of the degree-resolved shell incidence blocks already supplied by the 2026-10-11 quadratic-band static analysis and the standard time Vandermonde. The earlier static paper does not print the temporal formula or claim its own positive-eigenvalue collision at u²=n; those are different statements. The failure is because the frozen finite-time characterization is mechanically implied by the prior spatial blocks, not because the two named resonances are identical.

## value

FAIL

Heat recovery on a symmetric sampling set is well motivated and the formula is useful as a worked example. Here the radial zeros, invisible dimensions and time thresholds are the immediate rank bookkeeping of known shell incidence sectors with three Vandermonde columns. No independently new invariant, sharper stability bound or additional obstruction survives that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
