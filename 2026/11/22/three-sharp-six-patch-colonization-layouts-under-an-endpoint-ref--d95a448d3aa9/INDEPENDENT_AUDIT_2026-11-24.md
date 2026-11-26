# Independent mathematical audit

## correctness

PASS

Each arm is a capped Poisson arrival count. If Q_k=Pr[Poisson(τ)<k] and H_k is the mean capped count, the independent-arm expected reward is H_m+H_(6−m)+R(1−Q_m Q_(6−m)). This pays the bonus only once. Exhausting m=1,2,3 gives U₂−U₁=A₁−RB₁ and U₃−U₂=A₂−RB₂. The positive occupancy increments are p₂+p₃+p₄ and p₃; the reliability slopes are the two stated differences of products of truncated Poisson sums. Symbolic factorization from those sums gives the stated ratios. After canceling positive factors, their gap has numerator polynomial τ⁴+2τ³+10τ²+24τ+24, strictly positive at every positive deadline. The signs therefore give exactly the three strict regimes and the two adjacent ties, with no third maximizer. There are at most two unordered positive splits for fewer than six sites. A truncated-mass calculation reproduces 2.011511800830, 2.058940000562 and 2.045818834977 at τ=1, R=0.6.

## originality

PASS

Poisson/Erlang arrival counts, parallel path reach, and linear tradeoffs are standard. The supported distinct claim is that combining expected occupied sites with a single either-refuge reward produces two explicit strictly ordered thresholds for every deadline in the minimal six-site case. Path reliability alone determines neither the occupancy term nor the ordering of the two tradeoff slopes. The strongest inspected serial-chain and asymmetric-reliability analogues do not supply that ordering.

## value

PASS

This is the smallest two-arm instance in which a third integer design could be preferred. Two reasonable design objectives conflict, and opposite rankings alone could leave the middle layout nonoptimal for every reward. Showing that it is uniquely supported by a nonempty weight interval at every positive deadline, with exact endpoints and ties, supplies a natural small benchmark for stochastic habitat design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
