# Independent mathematical audit

## correctness

PASS

Ultrahomogeneity and the finite extension property identify nonalgebraic singleton types with positive distance vectors satisfying all Katětov inequalities. At base distances 1, 2 and 3 the forbidden endpoint label pairs are respectively {(1,3),(3,1)}, the empty set and {(1,1)}. Therefore the exact change is C13+C31-C11, using all unchanged constraints; the support sum in the frozen checker also follows by fixing the ones and independently placing threes outside that support and its distance-one neighborhood. For the two-shore family the only old triangles altered have side lengths (1,1,2) changed to (3,1,2), both admissible. With endpoint labels (1,1) every satellite independently takes 1 or 2. With (1,3), X takes 1 or 2 and Y takes 2 or 3, and only simultaneous use of 1 in X and 3 in Y is excluded; no within-shore constraint further restricts those palettes. Interchanging palettes gives C13=C31=2^p+2^q-1, so the difference is exactly 2-(2^p-2)(2^q-2), negative precisely for p,q>=2. This is an all-order argument. The independent exhaustive replay (python3 /workspace/branches/5215f64e-71a1-40cf-8e6b-670b2ebf2e30/replay.py; full_run.txt lines 1–7) tests both metrics for every ternary candidate with d(0,1)=1 and counts the conditional cases directly rather than using the packaged support method. It reproduces minima (1,2,2,2,-2), all strict increases through five points, and 401356 increases, 96 ties and 24 decreases among 401476 switchable metrics at six. All decreases have conditional counts (16,7,7) and the claimed two-shore structure. The six choices of the two vertices in X and the four internal distance patterns account for the 24; permitting a swap of the unordered distinguished pair combines the two one-internal-two patterns, giving three classes of sizes 6,12,6. The fixed labeled pair and the unordered pair stabilizer for isometry are different conventions, as stated in the source. The frozen artifact output agrees, including the three example before/after counts. No census is asserted at higher orders.

## originality

PASS

Credit is due to the sharp first loss and complete six-point census for a metric-preserving one-to-three elongation, and to the unbounded two-shore family with its exact loss law. The general Katětov correspondence and the graph-metric partition-function identity are prior; the local changed-pair identity is an elementary consequence, not a separate originality claim.

## value

PASS

The elementary admissibility rules pull in opposite directions under this elongation, so monotonicity cannot be read off one side of the triangle inequality. The natural single-coordinate question has a sharp minimum obstruction, a complete classification at that boundary, and an analytic family with losses growing exponentially. The result distinguishes first occurrence from magnitude and does not simply present an arbitrary metric slice or claim an all-order census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
