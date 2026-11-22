# Self-review

## Correctness — PASS
The claimed result is a global *lower* bound, supported by an explicitly constructed rank-\(n-1\) correlation matrix for every integer \(n\ge4\) and \(r>0\). Its null vector and every positive nonzero eigenvalue are verified algebraically. At that smooth semidefinite boundary, first variation of the simple zero eigenvalue produces exactly the stated Euclidean halfspace. The convex tangent-cone limit converts the absolute row sum of the corresponding orthogonal tangent projector into the ratio limit for two genuinely distinct finite inputs. An exact rational checker tests the algebra for 161 parameter cases, but the general proof is independent of these examples. The asymptotic maximum in the symmetric family follows from a uniform compactness argument and a unique maximum of a rational scalar profile. The general firm-nonexpansive estimate supplies the linear upper growth order. No global sharp prefactor is asserted.

## Originality — PASS (priority qualified)
Actual targeted published-finding corpus queries on nearest correlation/elliptope metric projection, maximum-entry Lipschitz stability, rank-deficient two-population normal directions, and linear-dimensional growth did not return an equivalent result. The closest accessible literature on metric projection onto spectrahedra concerns semismooth Newton/Jacobian conditioning, rather than a lower bound for the two-input maximum-entry operator modulus. Higham and Strabić study the *distance to* the nearest correlation matrix, not the *difference between two* nearest-correlation outputs. A general convex-set maximum-entry upper bound is broader in its domain but does not imply this lower bound because the elliptope is nonsmooth globally. No priority claim is made against inaccessible or unindexed literature.

## Mathematical value — PASS
The theorem resolves the qualitative growth order of a natural perturbation-condition number: coordinatewise sensitivity of Frobenius-nearest correlation-matrix repair is \(\Theta(n)\), despite Euclidean nonexpansivity. The exact, realizable two-population rank-deficient family and its optimized asymptotic constant explain a concrete geometric amplification mechanism. This is not merely a recomputed algorithmic output or an arbitrary parameter slice; it establishes instability that grows with the number of correlated variables.

## Closest literature and limitations
- Armijo, Bello-Cruz and Haeser, arXiv:2401.04657 (January 9, 2024), §§1–2 and 4: generalized Jacobians and nearest-correlation algorithms, not the claimed coordinatewise lower bound.
- Im, Jung, Moursi, Torregrosa-Belin and Wolkowicz, arXiv:2407.06408 (July 8, 2024), §§1, 2.1, 5.3, 6.2: elliptope nondegeneracy and projection algorithms, not the rank-one-kernel amplification coefficient.
- Higham and Strabić, DOI 10.1137/15M1052007 (first preprint 2015), §§1–3: bounds on distances to feasible correlation matrices rather than pairwise Lipschitz quotients.

The exact global leading constant and the best behavior over all other elliptope faces remain unproved. The review is not independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
