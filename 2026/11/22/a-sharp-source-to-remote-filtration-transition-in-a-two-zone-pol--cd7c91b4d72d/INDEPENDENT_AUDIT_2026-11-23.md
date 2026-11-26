# Independent mathematical audit

## correctness

PASS

For equal volumes and the stipulated symmetric exchange, the two-by-two balance matrix has positive determinant Δ=(r+m+B−y)(r+m+y)−m² and negative dynamical trace; the equilibrium is unique and attracting. Its concentrations are C₁=q(r+m+y)/Δ and C₂=qm/Δ. The numerator of Δ²C₁′/q is r(r+2m)+2(r+m)y+y²>0, while C₂ is minimized by maximizing the concave quadratic Δ, uniquely at B/2. To independently replay the whole-space result, set W=r+2m+y and T=B+2r+4m. With J=C₁+C₂, q/J=Δ/W=T−W−mT/W. This is strictly concave in W, with maximum at √(mT) if feasible. It is at the left endpoint W=r+2m when B≤2r+r²/m, including equality. In the other regime, (r+2m+B/2)²−mT=r(r+2m)+(r+m)B+B²/4>0, placing the maximizer strictly below the equal split and giving exactly the stated positive y. Thus y is asymptotic to √(mB) and J_opt=q/(T−2√(mT)) is asymptotic to q/B versus q(r+2m)/[(r+m)B] at y=0, confirming the fractional reduction. A separate solve of the stationary equations and direct scalar minimization for r=.5, m=1, B=6, q=40 gave remote y≈0.816625 and mean concentration ≈4.580065 versus 4.878049 at y=0 and 5.714286 at y=3. These are model checks, not measurements. RESULT.md lines 17–76 give the analytic replay; the supplied checker.py was inspected but not executed.

## originality

PASS

Best-of-knowledge pass for the continuously variable, globally optimal whole-space allocation and exact threshold and asymptotics, together with the objective comparison. The model and the source-only versus equal-split numerical experiment already exist in Airgle; their two-point comparison does not optimize over a divisible budget. The equal-split law for the remote-only objective is also present in a distinct indexed endpoint-allocation result. No novelty is assigned to that overlap, a change from sum to equal-volume mean, or the benchmark's old endpoints. The historical result is not a priority certification.

## value

PASS

A divisible clean-air budget and different choices of whose concentration to minimize are motivated by actual model comparisons. The exact activation condition answers when moving filtration away from the emitter first helps total burden, even where the usual equal-split comparison suggests source-only placement. Above that condition the whole-space solution strictly improves on both discrete designs, and the gain over source-only has a positive fractional limit even though the remote share tends to zero. The value is this objective-specific analytic benchmark with a precise budget decision, not a recommendation for particular buildings, devices or health outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
