# Independent mathematical audit

## correctness

PASS

The actual finite theorem is an enclosure, not an exact modulus. For m≥2 and 0<α<1 the only branches are singleton/global at the hub and singleton/pair/global at a leaf. Apply the signed incidence after taking absolute values. In each strict cell the Jacobian splits into a diagonal leaf-only matrix of norm at most 1 and a hub-column/constant-leaf-columns matrix of Frobenius norm at most √(m+m²h²). Finite piecewise linearity and continuity extend the bound to segments including ties; the absolute-value map extends it to complex signals. With x₀=1, all leaves at U=((m+1)^(1−α)−1)/m make the global branch equal 1 while both smaller leaf branches are strictly below 1, by strict concavity of t^(1−α). Lower the leaf values slightly, keeping them positive: now only the hub chooses its singleton, and all leaves choose the global branch. Its repeated Jacobian row (h−1,h,…,h) gives the exact lower quotient on a short segment parallel to that row. Arithmetic erratum in RESULT.md line 80: the squared ratio of the lower bound to A_m=√(m+m²h²) is 1−(2h−h²)/(1+mh²), not 1−2h/(1+mh²). The correction is immediate from (1), the squeeze still holds, and none of the theorem statements needs to change. In the critical window mh²→exp(2s); the fixed-α limits follow from mh²~m^(2α−1). Norms are unnormalized, edges counted once, and s fixed. Replay: RESULT.md steps 1–4 with the ratio above; the supplied checker was inspected, not executed. It tests finite witnesses and sample pairs via the branch formulas, and checks large-m bound proxies, not the true asymptotic modulus numerically.

## originality

PASS

The distinct claim is the sharp asymptotic for arbitrary growing unweighted stars in the two-input vertex-ℓ² to edge-ℓ² modulus for strictly positive fractional orders, including the moving-order crossover. The inspected same-day P₃ statement is exact for m=2 and overlaps the finite enclosure in that case; the exact all-star ordinary statement is α=0 only. Neither determines the joint m,α limit. Earlier one-input and TV-to-TV results are not the same modulus. No priority within a shared date is inferred.

## value

PASS

The result identifies a coherent amplification across edges from the large-ball branch that is missed by single-input variation theory. The sharp ℓ² constants on a growing high-degree family and the explicit logarithmic-window profile distinguish the competing √m and m^α scales. This remains useful without an exact finite-m classification or an extension beyond stars.

The dated certificate retains the supplied scientific assessment, sources and limitations.
