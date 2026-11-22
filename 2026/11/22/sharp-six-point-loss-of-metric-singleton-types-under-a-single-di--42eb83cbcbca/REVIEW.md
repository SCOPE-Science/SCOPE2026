# Review of the metric singleton-type elongation theorem

## Correctness — PASS

The admissibility table for a prospective distance vector in the discrete \(\{1,2,3\}\)-metric follows directly from both triangle inequalities. Old distance \(1\) excludes exactly labels \((1,3)\) and \((3,1)\); new distance \(3\) excludes exactly \((1,1)\). Cancelling unchanged assignments gives \(\Delta=C_{13}+C_{31}-C_{11}\). For the two-shore family, all triangle inequalities hold both before and after the one-edge alteration, and independent satellite assignments give \(C_{11}=2^{p+q}\) and \(C_{13}=C_{31}=2^p+2^q-1\). Hence \(\Delta=2-(2^p-2)(2^q-2)\), with a strictly negative value precisely when both shores contain at least two points.

The exact finite boundary was checked over every possible assignment to all unspecified old-pair distances, with explicit metric checks before and after elongation. The exact subset formula independently derived in the proof counts every admissible one-point vector. For \(n=2,3,4,5,6\), there are respectively \(1,6,98,4036,401476\) switchable labelled metrics fixing the altered pair. No nonpositive defect occurs below six; six points have precisely \(24\) negative defects (all \(-2\)), \(96\) zero defects, and \(401356\) positives. Each negative case was checked against the two-shore shape, with all three marked-isometry classes. A separate Python program directly enumerates ternary vectors for three representatives. Both implementations returned `VERIFY_OK`. Finite enumeration is used only for orders at most six; the arbitrary-size claim is analytic.

## Originality — PASS, with historical limits

Sauer's *Distance sets of universal and Urysohn metric spaces* (arXiv:1107.4794, 2011) was examined for its type-function construction and realization of Katětov extensions. It establishes the ambient framework and local triangle inequalities but not an extremal census under one distance change. The published *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* was inspected in full, including its proof. It provides the graph-metric \(\{1,2\}\)-slice identification and the local constraint table; it does not compare that count with the changed metric containing a distance-three pair, and it does not imply the sharp first-reversal threshold or the two-shore exact defect. Searches for equivalent Katětov-count, homomorphism-count, metric perturbation, and one-point extension formulations returned no identified coverage of the joint theorem. Matching words or failed searches are not accepted as proof of originality. Other examined published metric-type statements concern different parameter families or different changes of distances. The residual risk is unindexed prior metric-extension or three-state constraint enumeration results, and incomplete accessible historical material.

## Mathematical value — PASS

The quantity counted is a natural intrinsic extension invariant of the homogeneous metric structure. The same monotone change of an existing distance both relaxes a difference inequality and imposes a new sum inequality, so its effect is not sign-obvious. The theorem determines the exact first failure of monotone behavior, completely classifies the first failing marked bases, and supplies an infinite family with an exponentially large loss, independent of internal shore distances. These are motivated structural facts rather than a normalization test, isolated example or arbitrary parameter computation.

## Boundaries and documentation

No claim is made about a complete higher-order classification, other distance alphabets, simultaneous changes or independent scientific verification. Finite exhaustive checks and analytic proof serve different ranges and are not conflated. Source code, expected outputs and three explicit six-point witnesses are packaged with the result; independent scholarly priority and validation are open.

Self-review: passed. Independent audit: not yet performed.
