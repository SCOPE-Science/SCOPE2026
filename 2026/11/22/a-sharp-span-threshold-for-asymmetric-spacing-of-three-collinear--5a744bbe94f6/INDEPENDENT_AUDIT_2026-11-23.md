# Independent mathematical audit

## correctness

PASS

For the three specified positive inflow speeds and x in [ℓ,L−ℓ], direct differentiation gives P′=3δ(A−B_L). Differentiation of the squared-speed factors and the cubic distance factors gives A′<0 and B_L′>0 from −3+7δh(x)<0 and 3−3δh(L)−7δh(L−x)>0. At the midpoint A>B_L because only the last turbine receives the extra full-span deficit δh(L). At x=L−ℓ, A decreases and B_L increases with L; their difference has positive limit at 2ℓ (also for ℓ=0, using the continuous extension) and negative limit at infinity. Thus the unique crossing gives the stated endpoint regime, including equality, and the derivative has a unique interior zero strictly beyond the midpoint for larger L. For the asymptotic, set R=1+κL/2 and p=κ(x_L−L/2). Stationarity gives 3 log[(R+p)/(R−p)]=2 log(u₂/u₃). Positivity bounds the ratio of distances so both are of order R, making the right-hand side O(R⁻²). The left-hand side is at least 6p/R, so p=O(R⁻¹). Then u₂−u₃=δ/(1+κL)²+O(R⁻⁴), giving x_L−L/2=δR/[3κ(1+κL)²]+O(R⁻³) and the claimed leading term. An independent direct search of the cubic objective at δ=.2, κ=1, ℓ=.5, L=3 gave x≈1.511334 and power gain ≈1.0464×10⁻⁵ over the midpoint. That finite check is supplementary; the replay path for the proof is RESULT.md §§ Proof and Verification (lines 54–122 for the decisive steps). The supplied verification/wake_layout_check.py was inspected, not executed; no formal certification is asserted.

## originality

PASS

Best-of-knowledge pass for the fixed-span, one-free-location theorem and its large-span coefficient. The Jensen/Park decay family, linear summation and the general wind-farm layout problem all predate the record. No checked primary passage or distinct indexed record proved a result covering the precise boundary crossing, optimizer uniqueness and bias. The comparison does not establish historical priority.

## value

PASS

Fixed endpoints and a minimum gap give a motivated constrained layout problem. The exact classification supplies a test for whether a solver should return an active gap constraint or an interior stationary point, and identifies a structural asymmetry: the direct wake from the first to the last turbine lowers the marginal power cost of moving the middle one downstream. Without that term the cubic objective is symmetric in the two gaps and, in this regime, has its unique optimum at equal spacing. The value is the sharp global classification and quantitative bias for this model, not the tiny illustrated yield gain or a field design recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
