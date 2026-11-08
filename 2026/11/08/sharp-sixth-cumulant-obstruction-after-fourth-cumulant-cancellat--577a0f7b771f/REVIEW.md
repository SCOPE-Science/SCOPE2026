# Review of the fourth/sixth cumulant cancellation threshold

## Correctness

**PASS.** The six-moment finite Fourier closure follows from a path-length bound: mode four cannot contribute to a sixth-order displacement derivative at the origin. The isolated eigenvalue of the seven-mode truncation has an exact four-mode determinant whose coefficients give the displayed second, fourth and sixth cumulant growth rates. The two quadratic nonnegative-polynomial tests on \([-1,1]\) yield necessary sharp third-moment bounds; explicit endpoint two-atomic distributions and their mixtures prove sufficiency. The threshold \(-5/7\) and unique three-angle equality law follow by a factored comparison. The included standard-library program passed 271 exact arithmetic and independent Fourier-ODE checks. Scope restrictions, including the difference between linear cumulant growth and finite-time Gaussianity, are explicit.

## Originality

**PASS, qualified.** Close primary literature is treated by implication rather than title. The 2020 partial-reorientation paper already covers fourth-order kurtosis, the 2023 work supplies a finite-Fourier-moment method, and the August 2026 source supplies a full higher-even-moment computation framework; none of the inspected relevant passages states the displayed general sixth linear-cumulant coefficient together with the sharp feasibility interval, threshold and unique equality law. Prior fourth-cumulant formulas and general higher-moment machinery are not claimed as new. Search results did not reveal an explicit published classification, but absence from indexed sources cannot establish universal novelty. The remaining risk is an unindexed specialization or supplemental computation of the general existing hierarchy.

## Value

**PASS.** Long-time Gaussian diffusion masks information in higher turning harmonics. Nullifying the leading excess kurtosis without automatically nullifying higher non-Gaussianity is a natural discrimination problem for particles with indistinguishable diffusion rates. The sharp \(-5/7\) boundary separates an impossible regime from a fully realizable double-cancellation regime and identifies the only critical turning protocol. The result supplies exact experimental moment targets without asserting that microscopic measurements can resolve them at arbitrary noise levels.

## Closest literature and limitations

Britton–Zhang–Han–Bertrand, arXiv:2608.23519, Section 3.5; Villa-Torrealba–Chávez-Raby–de Castro–Soto, arXiv:2002.02872, fourth-moment and partial-turning calculations; Jung, arXiv:2308.00554, finite angular harmonics for even moments; and Santra–Basu–Sabhapandit, arXiv:2211.07337, including an explicit sixth moment for uniform turning, whose first and second relaxation rates coincide and thus cannot satisfy fourth-rate cancellation. Their general frameworks overlap in methodology but were not found to assert the exact classification stated here. The claim only concerns independent symmetric Poissonian angular turns, uniform initial orientation, and asymptotic projected-displacement cumulants through order six. No independent validation or generalization to interacting systems is claimed.

Self-review: passed. Independent audit: not yet performed.
