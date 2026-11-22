# Scientific review: universal critical microbial extinction

## Correctness — PASS

The statement fixes the exact \(\theta_i=1\) one-resource equations, strictly ordered break-even levels, positive initial states, and the dimensionless time convention. The continuous strictly increasing balance equation determines the selected equilibrium and all exchange thresholds. A relative-entropy Lyapunov function remains finite and dissipative when equilibrium biomass components vanish. Its derivative is an exact sum of a shared-resource square, nonpositive transfer terms, and nonpositive invasion exponents. The transfer signs follow from two explicitly stated arithmetic–geometric-mean inequalities. Compact invariant sublevels and LaSalle's principle establish global convergence, including at zero invasion exponents. A simple zero eigenvalue at each distinct-species threshold and a stable complementary block give the exact center reduction, proving the universal \(\tau N_j\) limit and nutrient coefficients. The standalone `check.py` passed symbolic identity and rational-parameter numerical checks. Computations illustrate, but do not replace, the general proof.

## Originality — PASS, literature-bounded

ElGamel and Mugler, arXiv:2611.00222v1, sections II, III.1, and supplemental VI–VII, develop the original model, a two-species full-isolation stationary coexistence criterion, and simulated survivor fractions. These yield neither a global theorem for arbitrarily many extinct/critically neutral species nor a \(1/\tau\) critical extinction coefficient. Related fixed-isolation mathematical statements previously give equilibrium support and attraction only away from zero-invasion faces or condition their conclusion on an interior coexistence equilibrium. Neither implies the present nonhyperbolic asymptotics. Chemostat global-stability articles by Mazenc–Malisoff and Abdellatif–Fekih-Salem–Sari, and spatial chemostat work by Haidar–Rapaport–Gérard, Wang, and Yu–Song–Wang, use different consumer/resource or patch-motion equations; the checked accessible material does not provide this particular formula. The full initiating article and supplement were inspected. Some older related papers could only be compared through abstracts or introductory material; an unindexed equivalent argument remains possible and historical priority is not independently certified.

## Mathematical value — PASS

The exact equilibrium-only survivor staircase does not determine whether an extinct population disappears quickly, slowly, or after an initial-condition-dependent transient. The theorem settles that natural dynamical gap for all positive starting states: strict exponential decay off the threshold, but a parameter-explicit inverse-time signature exactly at each species-loss boundary. The nutrient coefficients identify how the central and niche pools share the critical bottleneck. The result is a useful diagnostic for interpreting finite-time survival counts and a tractable analytic baseline for spatially structured resource competition. This concerns a motivated family in a published ecology model rather than an arbitrary numerical parameter slice.

## Boundaries and independent checking

The claims are deterministic and confined to one abiotic nutrient, fixed full isolation, distinct break-even levels, linear uptake, positive constant rates, and dimensionless time. They do not treat adaptive localization, stochastic environmental variation, repeated break-even ratios, or real-world extinction probabilities. The review verifies the proof internally; it is not an independent replication or historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
