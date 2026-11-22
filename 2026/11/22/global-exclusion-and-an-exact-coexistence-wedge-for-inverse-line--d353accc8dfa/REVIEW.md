# Scientific review

## Correctness — PASS

The normalized recurrence follows exactly from the three-population model with \(\sigma=0\) and negative-binomial shape-one prey escape. The exact identity \(q_{t+1}=(R_A/R_J)q_t/(1+y_t)\) and the uniform upper bound on the juvenile-stage predator give complete adult-stage predator extinction for \(R_A\le R_J\), including the equality boundary. At an interior Beverton–Holt fixed point, the first two recurrence equations force prey density \(1/R_J\); the third forces \(y=R_A/R_J-1\), and the remaining equation fixes \(x\). Strict positivity and direct substitution prove the sharp equilibrium wedge. Exact-rational checker tests passed; they are not used as a proof of the infinite-time statement.

## Originality — PASS (bounded historical comparison)

Seno–Goyal (2026), equation (13), establishes the original model and Lemma 6 supplies an equilibrium-only necessary ordering; the paper does not state global exclusion along arbitrary positive trajectories and explicitly leaves further coexistence analysis open. The result here requires the specific admissible shape-one escape laws rather than the exponential detailed example and proves both a global recurrent-state obstruction and the exact equilibrium existence region. Marcinko–Kot (2020) is a single-parasitoid comparison, not the same three-population recurrence. Published full-text material was compared by implication, and related models with different host-stage sequencing do not imply the new model-specific multiplicative identity. Residual risk: inaccessible or unindexed earlier three-population rational escape studies might contain the same identity.

## Value — PASS

Stage-specific pest/parasitoid management asks whether one specialist excludes another under oscillations and which predator productivity permits joint steady coexistence. The identity proves a global outcome, not merely stability of a particular equilibrium. The exact two-sided coexistence wedge identifies both insufficient and excessive adult-stage reproduction as obstructions to a positive three-species steady state. Both are natural quantities determined by the model's biological replacement parameters, not arbitrary finite slices.

## Scope of conclusion

There is no claim of coexistence stability, global convergence to the interior equilibrium, extinction of the juvenile predator, or applicability to prey survival or escape laws outside the specified assumptions. Historical priority is evaluated only to the limits of inspected sources.

Self-review: passed. Independent audit: not yet performed.
