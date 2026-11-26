# Independent mathematical audit

## correctness

PASS

A stationary state exists by finite-dimensional time averaging. Its support must be invariant under every jump (take the stationary equation on its kernel); the four nonzero local raising/lowering jumps generate the full matrix algebra, hence it is faithful. The adjoint fixed-point dissipation identity, traced against this state, forces every fixed observable to commute with every jump, so only scalars are fixed and the trace-one stationary state is unique. Phase covariance gives the stated X form. Independent exact replay with python3 /workspace/checks/qubit_algebra.py confirmed the generator equations, signs for c=ρ_10,01, and the concurrence polynomial and complementary-bath factorization. Solving gives z=(1+t²)⁻¹, c=2iJdz/(κ+iΔ) and the two extremal populations q²−d²z,(1−q)²−d²z, both positive under the strict occupation bounds. Thus the sign is that of F(z)=−h²+2d²(1−h)z−d²(1+d²)z². When d≠0 the maximizer is strictly inside (0,1), and both end values are negative. Its maximum is positive iff d²(1−2h)>h². Equality gives zero rather than positive concurrence. The strictly decreasing bijection from t≥0 to z∈(0,1] maps the two roots to the asserted finite open interval. At q=1/2 the inequality reduces to t²−2|m|t+1−m²<0, with the claimed roots and width. The result quantifies existence over J, not positivity at every J. The supplied checker was inspected, not executed.

## originality

FAIL

The exact local detuned exchange Lindbladian, general rate-symbol stationary X-state, and exact entanglement criterion were already given by Khandelwal et al. (2020). After imposing equal total rates the claimed condition and entire coupling interval are the discriminant and positive-root interval of a quadratic directly in those displayed formulas. The inverted fermionic realization in Brask et al. corroborates the resonant model for occupations above one half; it is not necessary to identify the formal Lindblad rates with physical positive-temperature bosonic rates. The earlier authors did not need to state the boundary in (q,d) coordinates for the implication to hold.

## value

FAIL

The explicit occupation coordinates and bounded window are convenient, and the derivation is correct, but the central feasibility result is a one-variable discriminant test of the prior exact stationary state and positivity criterion. The complementary-bath width is a further direct simplification. The record does not establish a substantive uncovered result beyond this reparameterization and elimination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
