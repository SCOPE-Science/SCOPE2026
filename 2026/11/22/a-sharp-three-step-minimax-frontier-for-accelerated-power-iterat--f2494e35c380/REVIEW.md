# Independent mathematical audit

## correctness

PASS

Applied to the complete corrected RESULT.md: p₁=t, p₂=t[t−β(1−t)], and p₃=t²[(1+c)t−c], c=β(β+2), by the stated warm start. The leading coefficient is 1; a diagonal two-level matrix attains the operator norm on the orthogonal component, hence the exact tangent amplification. Up to c₀=q/(1−q), p₃ has its negative minimum at t=2c/[3(1+c)], and the positive endpoint extremum at q. The negative magnitude increases and the endpoint decreases, so the crossing is unique. Beyond the crossing the fixed pre-crossing minimizing spectral point already has strictly larger error. Capping at q(q+2) yields the unique tune; the branch sign F(q) is strictly increasing, negative at the golden-ratio bound and positive at one. The minimax error strictly improves on the value at c=0. For p₃(q)=0, c=c₀; feasibility reduces exactly to q²+q≤1. Its worst error is the negative lobe at 2q/3 and exceeds the equioscillating error. I checked the repaired endpoint/interior distinction exactly: p₁(q)>0 and p₂(q)≥q³, while p₂(β/(1+β))=0 for β>0 with β≤q. At q=β=1/2 the interior and endpoint values are respectively 0 and 1/8. No change is needed to the frozen verify.py or VERIFICATION.md, whose tests can be replayed as documented; I inspected them without executing uploaded code. The scalar calculus proof, not the finite tests, justifies the real-parameter result.

## originality

PASS

For the repaired claim, the recurrence itself is prior, but the source comparisons support distinct finite-step interval tuning, its cap threshold, and the contrasting endpoint notch. The corrected endpoint scope stays within the checked spectral interval and tuning objective. The step-two calculation is a scope correction, not a separately claimed novel finding.

## value

PASS

For the repaired claim, exact finite-budget tuning under a known spectral bound is a different problem from tuning the asymptotic method. The result identifies when the closed momentum cap actually binds and shows that removing the endpoint exactly can be feasible yet strictly worse in the robust interval objective. The distinguished horizon is the first at which endpoint annihilation can occur under the cap, not an arbitrary iteration chosen after a computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
