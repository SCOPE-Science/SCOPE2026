# Independent mathematical audit

## correctness

PASS

Frobenius splits F^(ℓb) into b independent order-ℓ differences along residue classes. The kernel on each class has ℓ initial values, with Pascal basis degrees 0 through ℓ−1 and unit leading coefficients since ℓ≤p. Evaluation on the distinct sampled residues in F_p therefore has rank min(c_r,ℓ). The bilateral inhomogeneous recurrence is onto because both extreme coefficients are units. The antecedent traces are cosets of the kernel trace; if that trace space is proper, choose a trace outside the coset of the prescribed v, extend it to a full configuration and apply F^(ℓb) to obtain a missed target. Consequently success at clock ℓb is equivalent to max c_r≤ℓ, and first sampled success is equivalent to max c_r=ℓ, as in the displayed theorem; the opening sentence conflates the two. Neither an unsampled first iterate nor a joint multilevel Poisson law is asserted by the formulas. The two coefficient formulas count choices within disjoint buckets. For s=ℓ+1, the binomial ratio in the k-th factorial moment is (m)_(sk)(pb−m)_(k(p−s))/(pb)_(pk), giving the stated intensity. Larger bucket counts vanish in the critical window, the lower and upper neighboring clocks give the two-point limit, and first moment plus prefix coupling gives subcritical and supercritical limits, including ℓ=1 and ℓ=p−1. The independent recurrence-matrix replay at `/workspace/branches/689d15cc-71ec-4827-af26-ca4d4d8e9e37/replay_record3.py` checked all 126 supports of size 4 for p=b=3 at each of the three clocks; CDF numerators were 0, 108, 126 and the directly enumerated deficiency histograms agree with the coefficient formula. This finite test does not establish the asymptotics.

## originality

PASS

At the sampled clocks the individual residue-block rank is standard polynomial evaluation, and multiple occupancy with Poisson asymptotics is a standard mechanism. The supported distinction is the arbitrary-support cellular-automaton covering-clock identification coupled to the exact fixed-capacity, without-replacement deficiency law and its level-dependent thresholds. The nearest related catalogue results cover specific geometries, not that combined claim.

## value

PASS

For a standard linear automaton the result converts a deterministic extension problem with arbitrary missing coordinates into a computable law of randomly sampled observations. The full deficiency counts, symbol independence, distinct level scales and explicit intensities answer a quantitative question not settled by qualitative eventual surjectivity. The scientific contribution is the connection and exact consequences in the sampled model, not a new Poisson mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
