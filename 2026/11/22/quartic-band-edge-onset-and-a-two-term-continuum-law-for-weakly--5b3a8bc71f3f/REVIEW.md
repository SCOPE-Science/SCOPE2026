# Independent mathematical audit

## correctness

PASS

Finite rank preserves the free essential band. An exterior eigenvector has x₀≠0 by recurrence, so Cauchy–Schwarz in the shift form gives |⟨Jx,x⟩|≤2t||x||√(||x||²−|x₀|²)<2t||x||², justifying strictness in the matching step. Chebyshev solutions on the prefix and the unique ℓ² tail give t sin(mθ)=exp(η)sin((m+1)θ). For λ=2 cosh η the exact tail Schur complement has last diagonal exp(η), the other diagonals λ and off-diagonals −t. It is strictly above its η=0 limit for η>0, so threshold zero directions do not contribute to the negative inertia. At t=1 the limiting form is positive (sum of adjacent squares plus the left endpoint square), and division by t makes the diagonal strictly decreasing. Its only positive crossings for t>1 are the listed cos((m+1)θ)=0 roots in 0<θ<π/2, each simple by the Jacobi recurrence. Secant expansion gives m²(t_{m,j}−1)=a_j−2a_j/m+O(m⁻²), so the critical state really exists. For δ=1/m and fixed σ=√(2α−κ²)>0, θ=δσ+O(δ³) is analytic near δ=0 after choosing the odd extension. The matching residual divided by δ is −G+δH+O(δ²), with the stated H; at every continuum root G'=(2α/σ²)(1+κ)sinσ and H=2αsinσ. Monotone intersection on each stated σ interval and the exact count exhaust all roots; ordering is opposite that of σ. The implicit correction is δσ²/(1+κ); at κ=0 it is positive δ·2a_j. Converting via 2cosh(δκ_m) gives both gap laws with their remainders. Rotations of the shift are unitarily equivalent, giving the numerical radius formula. The frozen checker was inspected, not executed. An independent Jacobi ratio iteration at 55 digits (replay: /workspace/branches/replay_jacobi_edge.py) checked j=1,2 in noncritical and critical examples; at m=2048 the four coefficient ratios were 0.999850, 0.997273, 0.998295, 0.984853. These are corroboration only.

## originality

PASS

Best-of-knowledge pass for the fixed-α growing-prefix expansion, including the explicit first correction of every existing positive branch and the quartic gap of the newly born branch at α=a_j. The finite-prefix secular machinery and its exact thresholds are pre-existing or directly extracted from it and are not credited as new; nor is the leading square-well matching equation on its own.

## value

PASS

A leading continuum model alone predicts a threshold resonance with zero gap at α=a_j. The exact finite branch instead binds there at a smaller identifiable scale. The first branch-by-branch drift and the separate critical coefficient quantify both effects for a natural finite block without conflating eigenvalues with resonances or treating the standard finite-prefix equation as the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
