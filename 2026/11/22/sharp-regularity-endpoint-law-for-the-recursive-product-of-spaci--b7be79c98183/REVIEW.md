# Independent mathematical audit

## correctness

PASS

The continuous specified null gives iid uniforms after the probability-integral transform and density (m−1)! with respect to the first m−1 spacing coordinates. Iterating adjacent sums and dividing by the sum on each level cancels intermediate normalizations; the resulting linear windows are the Pascal rows of B_k. AM–GM bounds each negative log product by j log j, and the first level forces the unique equality point D₀=1/m. The first-level log barrier and lower bounds on later levels confine all small sublevel sets to that point. In D=D₀+Az coordinates, the differential of each normalized j-window vector is m P_j B_k A/(j2^k); this follows by quotient differentiation at a constant vector whose unnormalized sum is j2^k/m. At the uniform vector the linear term of the negative log product annihilates every tangent change, including second-order normalization terms. Its Hessian is j² times the pullback of the Euclidean quadratic form by that differential, giving exactly Q_m. The first level m²AᵀA has determinant m^(2m−1) and is positive definite; all additions are positive semidefinite. For m≥3, B₁ applied to the tangent e₁−e_m gives e₁−e_(m−1), so its centered contribution is nonzero, strictly increasing the determinant after conjugating by the first level's inverse square root. The Taylor remainder gives a two-sided ellipsoid squeeze after rescaling by √ε, with volume of the unit ball times 2^((m−1)/2)/√det Q_m and the stated Dirichlet density factor (no extra Jacobian in these coordinates). The score event is exactly T_m−b_m≤b_mη/(1−η). For m=2 the exact raw-excess CDF is √(1−exp(−ε)), and for m=3 det Q₃=1215/4 yields C₃=8π/√1215 and ratio 2/√5. `python /workspace/replay_checks.py 5` independently differentiates the recursive log expressions at m=2,…,5, matching the exact Hessian at m=3 and the four listed determinants. The theorem is fixed-size, at the regularity endpoint only.

## originality

PASS

The origin paper already supplies the statistic, its minimum, its one-observation distribution, and the interpretation of the first level as Moran. The generic ellipsoid argument and the one-observation case are not new. The supported distinct piece is the explicit full-chain rational Hessian for every fixed size, its leading determinant coefficient, and the quantitative strict comparison with the Moran coefficient. The inspected extreme RPS tails concern the opposite endpoint; priority against the inaccessible doctoral thesis remains unresolved.

## value

PASS

Exact near-regular null calibration is useful for a published statistic whose inspected paper calibrates multi-observation samples numerically. The full-chain curvature is a natural nontrivial invariant, supplies every fixed-size leading probability, and quantifies why comparing equal raw excesses to Moran is not neutral. This is not a general finite-threshold or test-power claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
