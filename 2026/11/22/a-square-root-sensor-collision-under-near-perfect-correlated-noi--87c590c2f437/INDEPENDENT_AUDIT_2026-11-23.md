# Independent mathematical audit

## correctness

PASS

The two covariance eigenchannels give the stated sum- and difference-vector information decomposition. Distinct interior points yield independent rows since their second-to-first evaluation ratios are 2 cos(πx); coincident sites or endpoint rows cannot maximize. For a viable pair, a Rayleigh quotient perpendicular to the row difference gives λ_min≤2D/(2−ε), with D the squared origin-to-chord-line distance. D is bounded by the smaller endpoint squared norm, and the norm factorization gives maximum L=25/16 only at θ*=arccos√(3/8) and its reflection. Pairs tending to these opposite points would have chord distance squared 5/8, so any near-extremizing pair must coalesce at the same point. From the exact angular chord expression, putting u=cos²m and v=cos²(δ/2), the u-curvature at (3/8,1) is −56 and the v-derivative is 35/8. Thus the local deficit is (105/4) times squared midpoint error plus (35/32)δ². At m=θ*, A and A′ are perpendicular with squared norms L and 5/8 and A·A″=−35/8. Taking δ²=5ε+ε^(3/2) gives diagonal entries L−(75/16)ε+O(ε^(3/2)) and L+(5/16)√ε+O(ε), with off-diagonal O(ε); the gap leaves eigenvalue error O(ε^(3/2)). Matching this lower bound with the global chord bound first localizes every optimizer to O(√ε), then matrix convergence requires any limit of δ²/ε to be at least five. The first-order chord bound requires at most five and gives midpoint error o(√ε); substitution proves the claimed coefficient. For reflected pairs the two diagonal entries cross at u=(1−ρ)/[4(1+ρ)]≤1/4, where the smaller one changes from the increasing branch to the decreasing branch. This yields the exact restricted value and its limit. The frozen verify.py and verification_output.txt were inspected, not executed; symbolic and search checks there are supplementary, not global certificates. The result assumes fixed pair-level correlation independent of selected sites, applies only as ρ approaches one from below for the unrestricted asymptotics, and does not establish finite-ρ uniqueness.

## originality

PASS

The assessed contribution is the global, all-optima collision asymptotic in the exact continuous two-read GLS problem, including its separation and first information correction and the reflection-design comparison. The Gaussian information formula, least-eigenvalue criterion, and general correlated-design methods are established. The strongest indexed same-mode result instead combines one spatial point with temporal information; the strongest inspected broader exact GLS setup fixes a discrete design space and does not give the continuous two-read singular asymptotic. This is a best-of-knowledge, bounded decision.

## value

PASS

Two readings are the minimal exact design for two unrestricted coefficients, and fixed common calibration noise is a concrete model for the singular regime. The theorem establishes why a natural reflected design misses the limiting optimum by a factor of 25/16 and supplies a sharp gap, midpoint localization and first-order information benchmark across all optimal pairs, not just a numerical optimizer. It is a structural benchmark for prescribed pair-level noise, not a recommendation for distance-dependent spatial covariance or positive-time sensing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
