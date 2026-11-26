# Independent mathematical audit

## correctness

PASS

The complex scalar action on the plane gives the single-step square gain (1−ah+r²h²/4)/(1+ah+r²h²/4) with positive denominator. Multiply two such gains and use h₁+h₂=H and h₁h₂=H²q. The common part of numerator and denominator is w²+R−4σ²(w−1), w=1+Rq; their antisymmetric part is ±aHw. Dividing by w gives (U−aH)/(U+aH), an increasing function of U=w+(R+4σ²)/w−4σ². Its strictly convex minimization is projection of √(R+4σ²) onto [1,1+R/4], so q and the unordered length pair are unique even at phase boundaries. The lower endpoint condition is R≤1−4σ², and the upper endpoint condition is (R−4)²≤64σ²; the two lower thresholds differ by (1−2σ)(3−2σ) for σ<1/2. These inequalities include σ=0, σ=1/2 and all stated endpoint cases. The short length tends to 2/r since q=R^(−1/2)+O(R^(−1)); the other gain tends to 1, giving (r−a)/(r+a), while two equal lengths both diverge and give product gain 1. When b=0 one length 2/a makes a Cayley numerator zero, feasible exactly for H≥2/a. Direct numerical substitution at a=b=1,H=10 independently gave short fraction 0.145348129877 and gains 0.108027069187 vs 0.211102994887 for equal lengths. The supplied verifier and output were inspected, not executed; neither the sample nor the author's grid certifies global optimality.

## originality

PASS

The supported distinct result is the full optimum and sharp phase diagram for two real lengths with fixed sum applied to one normal damped mode. Cayley factors and trapezoidal composition are prior tools. The strongest indexed comparisons change the generator or the rational filter and objective, and the inspected composite, complex-weight, and ADI sources do not entail this constrained optimum.

## value

PASS

The damped complex mode is a standard test for numerical attenuation. The exact result identifies when spending a fixed budget on a second nonzero solve helps and when the common equal split is optimal. The reentrant unequal optimum exposes residual damping even when both equal large steps would nearly preserve the norm. This is a useful sharp performance benchmark for the stated objective, not a claim that such splitting improves accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
