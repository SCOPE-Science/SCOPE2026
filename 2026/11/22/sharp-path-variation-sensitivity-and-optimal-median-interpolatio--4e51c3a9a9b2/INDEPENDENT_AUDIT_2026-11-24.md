# Independent mathematical audit

## correctness

PASS

The two inputs have separate sample-dependent centers and share the same radius τ>0. In each strict rank-and-clip chamber the rows of the derivative are coordinate selectors or the same center row. On the quotient by constants the unit steps form the ℓ1 coordinate basis for path variation, so it suffices to bound one step response at a time. Piecewise affinity and continuity extend the bound to every pair, including ties. In odd size every response is binary. A median in the first position and an alternating mask to its right with a first-edge cut attain n−1. In even size, if both central sites are on the same side, that side is constant and contains at least two sites; this bounds the response by n−2. If they straddle the cut, the common value is s=θ or 1−θ, the sidewise oscillations are bounded by s and 1−s, and the bridge by 1. This yields 1+(n−2)max(θ,1−θ). To attain the first even branch, put the two central ranks at positions 1 and 2 and cut after position 2; to attain the other, cut after position 1 and place the larger interpolation weight on the left, with both central sites active. In each case alternate the masks to the right as in the proof. Both central values can be chosen in a narrow strict interval, with precisely half the remaining values below and half above it; each side then permits distinct strictly interior and exterior choices independently of the spatial mask. Finite sufficiently small step perturbations stay in the chamber and attain the announced ratios. At n=2 a strict identity cell gives 1 for every θ. Solving the inequality between the two even branches gives the singleton minimizer at n=4 and the claimed plateau at even n≥6. Single-input diminution follows from the scalar 1-Lipschitz property at its own center. The finite rational checker was inspected, not executed; the argument covers all n, θ and positive τ without enumeration.

## originality

PASS

The supported distinct result is the sharp size- and interpolation-dependent law for a global order-statistic center, particularly the exact even-size minimizer set. Local step/activation methods and related clipping, rectification, Winsorization and rank-filter stability results are precedents, not claimed new. This is a bounded comparison, not a historical-priority attestation.

## value

PASS

Choosing a sample median convention really changes worst-case perturbation amplification for a natural robust clipping rule, although no convention increases individual path variation. The classification says when midpoint centering is uniquely optimal and when an interval of asymmetric conventions is equally good. Attaining tests with strict ranks and clipping decisions distinguish true instability from a boundary-only linearization artifact. No assertion about statistical-risk optimality is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
