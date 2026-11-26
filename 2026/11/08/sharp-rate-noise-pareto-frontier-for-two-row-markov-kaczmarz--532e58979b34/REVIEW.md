# Independent mathematical audit

## correctness

PASS

The original no-unique-optimizer wording for equal variances is false at r=c²: only α=β=1 is feasible, independently of the variances. Its nonattainment statement at r=1 also requires unequal variances. The repaired RESULT.md corrects both and states time-homogeneous row-specific innovation laws for the asserted invariant joint law. Equal conditional variances across time alone do not imply stationarity: one may alternate independent ±√v_i errors with a law taking zero half the time and ±√(2v_i) one quarter each; the exact post-update relation u_i·X_n=ε_(i,n) then forces different conditional laws at even and odd times. For the repair, choose row tangents w_i. Each switch contracts tangent magnitude by c, repeats preserve it, and the expected squared multiplicative weight per transition is bounded by θ=1−(1−c²)min(α,β)<1. Conditional centering/independence remove cross terms in the backward sum, whose jth squared contribution for j≥1 is bounded by max(v_i)θ^(j−1); this proves finite second moments and existence with stationary driving laws. Coupling invariant laws at the same row phase and using infinitely many switches proves uniqueness, including at alternation. Reversal equals forward transitions in the stationary two-state chain; conditional tangent moments obey q₁=c²q₂+(1−c²)v₂ and q₂=c²q₁+(1−c²)v₁, which give the stated affine trace risk. The polarized row-energy transfer for synchronized differences has diagonal entries 1−α,1−β and off-diagonal entries βc²,αc²; its positive left Perron vector compares the total energy to exact powers of its Perron root even at period two. For fixed p this root strictly decreases with k=α+β, forcing k=1/max(p,1−p) for best contraction. With z=|2p−1| the positive-root quadratic is (1+z)L²−2zL−c⁴(1−z)=0; L increases strictly from c² to 1, so inversion gives z_r. The affine risk forces the maximal feasible preference for the lower-noise row and, when variances differ, a unique saturated transition pair. Equal variances make every feasible policy optimal, with only alternation at r=c² and infinitely many policies for c²<r<1. At r≥1 the unequal-variance optimum is an unattained infimum because both frequencies must stay positive; the equal-variance risk is attained everywhere. Direct substitution in the given c=3/5 example yields risk 313/68 and rates (25+2√217)/75 and (25+√217)/50. The nested verifier and output were inspected, not executed. Its covariance and transfer identities are exact rational checks; spectral comparisons use floats and do not certify optimizer multiplicity. The analytic argument establishes the repaired boundaries.

## originality

PASS

The supported distinct content is the persistence invariance across the full stationary two-state fresh-noise family together with the resulting sharp rate-cap frontier over actual transition probabilities. Credit the standard moment lift/Perron-root method, exact iid MSE literature, and the known fully refreshed alternating endpoint. The closest inspected iid and cyclic results cover special observation or selection policies, not arbitrary persistence or this constrained optimization.

## value

PASS

The two-row planar system is the smallest nontrivial setting for persistent selection of nonorthogonal measurement rows. The result distinguishes holding the noise floor fixed while improving rate from biasing the policy toward the better measurement and paying a rate penalty. It gives the switching rule and its exact attainable performance, not merely a generic moment criterion or the known alternating example. Correcting the equal-noise endpoint matters for interpretation of the unique fastest policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
