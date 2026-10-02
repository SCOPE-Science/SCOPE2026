# Independent mathematical audit

## correctness

PASS

The exact-rational Riccati interval inclusions at ±3/5 were recomputed and match the package: at +3/5 the even-step image is [-231/50,-119/110] and the odd-step image is [133/250,53/50], with the mirrored inclusions at -3/5. The alternating ratio signs give the stated 5/5 Sturm counts. Thus the displayed 0.6 gap is mathematically correct.

## originality

FAIL

A stronger result follows immediately from standard singular-value and Hermitian perturbation inequalities. After odd/even permutation, the zero-diagonal part is [[0,B],[B^T,0]] with B=S+W, where S is diagonal with entries at least 1.4 and W is a weighted one-step shift of operator norm at most 0.6. Hence sigma_min(B) >= 1.4-0.6 = 0.8. The diagonal disorder has operator norm at most 0.1, so Weyl's inequality leaves five eigenvalues at most -0.7 and five at least +0.7. Therefore the whole claimed (-0.6,0.6) gap, including the 5/5 split, is a direct corollary of a stronger textbook estimate.

## value

FAIL

For this parameter box the headline gap and exact spectral split are obtainable by a short standard perturbation argument that is both simpler and strictly stronger (0.7 versus 0.6). Comparing only against Gershgorin/Brauer/T^2-Gershgorin therefore does not establish mathematical value for this particular final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
