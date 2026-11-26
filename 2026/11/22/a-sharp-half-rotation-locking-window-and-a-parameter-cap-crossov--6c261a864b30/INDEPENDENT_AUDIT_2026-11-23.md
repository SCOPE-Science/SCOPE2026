# Independent mathematical audit

## correctness

PASS

At a₀=1/(2d), write a=a₀+cb² and F=x+1/2+b h(x)+b² k(x)+O(b³), where h=(Ω/d)sin(2πx), k=dc−a₀sin²(2πx). Then h(x+1/2)=−h(x) and k(x+1/2)=k(x), so the second iterate has coefficient 2k−hh′, namely 2dc−a₀+a₀cos(4πx)−π(Ω/d)²sin(4πx). The remainder is uniform in C² on bounded c and compact Ω ranges with d>0. For small b, g(x)=1−(Ω−b sin(2πx))² is positive and F′>0 on the relevant parameter strip. In fact ∂ₐF²(x)=g(F(x))+F′(F(x))g(x)>0. Thus there is a unique periodic profile a=𝒜_b(x) (inside (0,1) at fixed |Ω|<Ω_c by uniform bracketing), analytic even through b=0 before selecting extrema, with 𝒜_b−a₀ divisible by b². Its scaled profile tends in C² to the single frequency-2 harmonic plus a constant; its four simple critical points persist with no additional ones. The map x↦F_{𝒜_b(x)}(x) is C¹-close to a half-turn, preserves the profile and pairs the two maxima and the two minima; a regular level therefore gives precisely two primitive orbits. Since ∂ₓ(F²−x−1)=−∂ₐ(F²−x−1)𝒜_b′ along the profile, signs give one attracting and one repelling orbit, while at extrema the second derivative is nonzero and ∂ₐ(F²−x−1)>0, giving nondegenerate saddle-nodes. Half-turn conjugacy under b↦−b makes the analytic extreme values even, so the remainder is O(b⁴). For Ω=0, G=F−1/2 is increasing and G²=F²−1; G²(x)=x iff G(x)=x. The increment range gives the exact symmetric interval. Near Ω_c the same profile extends through the cap; ∂_Ω a₀(Ω_c)=2√2, which gives the stated unique local cap edge and its coefficient (√(1+4π²)−1)/(2√2). At the edge only the lower endpoint is admissible. Inspected the frozen verification and numerical script without running it. The analytic comparison controls the all-orbit count and uniformity, not a grid search.

## originality

PASS

The exact map, its harmonic decomposition and some period-one and numerical dynamics are prior. The strongest examined same-map and general resonant comparisons do not give the half-rotation profile with these harmonics tied to a single capped gain, the explicit width and symmetric slice, or the resulting cap edge.

## value

PASS

The two contributions to the resonance have the same perturbative order and affect the lower and upper edges differently. The width and complete local census are quantitative results for a studied map, and the strictly positive cap shift shows that small coupling permits locking in a region forbidden at zero coupling. The cap is a pre-existing model constraint, not a slice chosen merely to get a solvable example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
