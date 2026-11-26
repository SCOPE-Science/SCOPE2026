# Independent mathematical audit

## correctness

PASS

For hub-to-leaf flux z_i the subgradient is (sum z_i,-z_1,...,-z_m); stationarity with admissible z is sufficient by strict convexity. For k tied leaves all free fluxes of the minimum-norm subgradient agree, by symmetry and strict convexity of the flux objective. Its derivative yields z=clip(-a/(k+1),-1,1), where a sums the untied signs. At m<=3, |a|<=m-k<=k+1 for k>=1, so hub and tied leaves have identical minimum-norm subgradient entries; all variations of subgradients are supported on tied-edge differences and are orthogonal to that minimum. With no ties the subgradient is a singleton. Burger et al. Theorem 5 applies to the resulting polyhedral absolutely one-homogeneous functional with MINSUB, and autonomous flow uniqueness yields the semigroup. Independently, one can evolve the hub and tied leaves together at speed -a/(k+1), grow the tied cluster at each collision, and move all untied leaves toward the hub at unit speed until collision. For m<=3 these fluxes are admissible at each step. Every final untied edge has retained its sign, so the time-average flux is valid at the final configuration and certifies that it is the unique proximal output. For m=4 the three certificate flux sums are 5/2,7/4,2; for m=5 they are -4,-9/4,-3. In each case subtracting the scaled sums from the current hub and adding the scaled flux to each leaf reproduces the three displayed outputs. Each flux has the required final sign or is allowed on a tie. The resulting gaps are 1/4 and 1/2 in sup norm. Appended low/high pairs have constant flux (+1,-1) at all three solves, cancel at the hub and stay strictly outside the whole range of original hub positions. Thus both parity classes and all m>=4 are covered. The checker was inspected, not executed; it prints 38 large-star sign configurations but the degree loop 4 through 40 contains 37, a reporting typo that does not affect the analytic proof.

## originality

FAIL

The small-star positive direction directly specializes Burger et al.'s sufficient diagonal-dominance class. For necessity, the distinct catalogue record fcd11a969142 provides the weighted failed-budget construction with the same star, data pattern, exact fused interval and unsaturated/saturated regimes. Specializing that construction and restarting it at the fused output gives the full large-star obstruction, including the fixed equal half-steps (see explicit comparison below). Failure of diagonal dominance alone would not imply failure, and irreversible fusion is not being equated with the semigroup as a general property. The failed-budget witness itself supplies the relevant coverage, even though the comparison record does not name the semigroup. This is a demonstrated coverage decision, not an inference about priority between entries dated the same day.

## value

PASS

A sharp vertex-degree threshold for when iterated denoising exactly equals a single solve is a natural structural question. A rational five-vertex obstruction and universal positive statement at smaller star degrees illustrate why flow and proximal regularization can separate. This conceptual use does not overcome the catalogue and primary-theorem coverage of the mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
