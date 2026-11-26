# Independent mathematical audit

## correctness

PASS

The graph reduces to a 2q-cycle and two tails each of lengths l and r. A tail bridge separating h vertices from the rest contributes h(2m−h) to the unordered-pair index, independently of all other bridges. For the cycle contribution, collapse each tail to its corner, adding mass l or r there. On a length-L cycle the kernel at distance d is d(L−d)/L, the pair sum is (L³−L)/12 and the row sum is (L²−1)/6. Across either rung use d=1; among the four left-right pairs there are two each at d=q−1 and q. Adding the base cycle, the extra corner masses and the bridge sums exactly reproduces the stated expression, including zero tails. At fixed q the only imbalance term is m(l−r)²/2; balance yields the parity penalty in F_m. Recomputing the neighbor differences of H=5(q−(3m+6)/5)²+3ε gives the stated two tables. Further to the right the quadratic grows more than the maximal parity loss and −3m/q increases strictly. Moving d steps left loses at most (5/2)d from −3m/q because q≥2 and m/q_*≤5/3; the quadratic-parity increment is at least 4 at d=1 and at least 5d²−4d−3 for d≥2, both strictly larger than (5/2)d. Therefore q_* is the unique legal optimal cycle parameter, even at the small endpoint cases. Only m≡0 mod 5 has an odd tail sum at q_*, so it supplies exactly the two reflected placements. With q_*=(3/5)m+O(1) the cubic part gives (5−6·(3/5)+5·(3/5)²)/6=8/15; all remaining terms are O(m²) or smaller.

## originality

PASS

The formula for evaluating a unicyclic resistance index uses known principles. The creditable claim is the exact all-m discrete minimizer and tie classification in the two-rung design family, with the resulting sharp leading value. Comparisons found related ladder-like calculations, a distinct one-link design theorem and general unicyclic formula leads, but no demonstrated coverage of that optimizer. Full-text access limits are material to historical priority, not a negative finding about what those papers contain.

## value

PASS

Adding two corresponding cross-links on equal paths is a natural constrained design problem, and total pairwise resistance is a standard connectivity objective. The exact result determines where to put the links at each size and when two designs tie. It rules out an end-rung heuristic, exhibits an interior 1/5–4/5 rule, and quantifies the minimum at cubic order. That complete classification is useful beyond a circuit identity or finite graph enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
