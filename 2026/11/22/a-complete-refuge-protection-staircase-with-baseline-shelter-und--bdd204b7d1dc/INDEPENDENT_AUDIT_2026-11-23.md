# Independent mathematical audit

## correctness

PASS

For the corrected record, the fixed-initial-abundance hazard gives expected survivors N exp(−Td₀) Σᵢ exp(−a/(b+rᵢ)), a=Td₁N>0, with zero survival at zero total cover. The simplex is compact and the zero-cover extension is continuous. With pair total cover C fixed and x<C/2, the derivative of the pair objective has the sign of H(x/C)−a/C. Writing y=(C−x)/x>1 gives H=2y log(y)/(y²−1), strictly increasing in x/C from 0 to 1: log(y)−(y²−1)/(y²+1) is positive by differentiation from y=1. Thus an unequal interior pair is strictly below an endpoint or the midpoint on its feasible interval; every maximizing allocation has j equal positive supplements R/j, with arbitrary occupied labels. After dropping the common baseline and prefactor, the support objective is Qⱼ=j[exp(−θuⱼ)−exp(−θv)] for β=b/R>0, θ=a/R, uⱼ=j/(1+βj), v=1/β. Qⱼ₊₁/Qⱼ is (j+1)/j times the upper-tail probability of [uⱼ₊₁,v] under density proportional to exp(−θt) on [uⱼ,v]. This decreases strictly by exponential tilting, starts above 1 at θ↓0 by the interval lengths, and tends to 0. Hence each adjacent equality occurs once. For continuous support x>0, Q′ has the sign of 1/λ−L(z), where λ=θ/β, z=λ/(1+βx), and L(z)=∫₀¹(1−s)exp(−zs)ds. L increases strictly as x increases, to 1/2. The derivative is strictly positive when λ≤2; when λ>2 it changes sign once from positive to negative since L(λ)<1/λ. Consequently at an adjacent equality exactly those two integers are global maximizers. At θⱼ the next larger support is already worse than j+1, and the next smaller is already worse than j; the strict ratio monotonicity orders their crossings θⱼ₊₁<θⱼ<θⱼ₋₁ wherever defined. Thus the staircase has no skips or extra tie sizes. At β=0 the objective becomes j exp(−θj); its adjacent ratios give ordered crossings log((j+1)/j). Bracketing the positive-baseline root with points on either side of the zero-baseline crossing proves convergence as β↓0. The independent replay reproduced the four-patch β=1/2 crossing values 1.358513260963, 1.496945595991 and 1.828133590308 and the strict support-2 optimum at θ=1.6. The 20,460 simplex-lattice comparisons had no discrepancy beyond roundoff (maximum excess 5.55e−17). Reading the bundled checker and recomputing loop counts gives 1,632, 523,590, 56,000, 119,988, 552 and 614,215 diagnostics, totaling 1,315,977; the first count denotes support values across 136 exact tie cases.

## originality

PASS

Best-of-knowledge pass for the explicit shifted inverse-exponential support selector with strictly ordered positive-baseline crossings and exact ties, not for S-shaped resource allocation, the hazard model or the general idea of a staircase. General identical-plant allocation is a real equivalence risk: the available historical abstracts could cover the structural reduction, but they do not establish the particular parameter-dependent crossing and no-skip theorem. This is not a claim of exhaustive priority.

## value

PASS

For a fixed supplement across identical patches, the theorem determines exactly when to spread protection and when to concentrate it as the held hazard increases. Every support size occurs on a nonempty interval, and baseline-dependent thresholds distinguish equal-support ties from regimes with a single maximizing support size. The result is an exact benchmark with a transparent scope, beyond the existence of an allocation rule or a finite numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
