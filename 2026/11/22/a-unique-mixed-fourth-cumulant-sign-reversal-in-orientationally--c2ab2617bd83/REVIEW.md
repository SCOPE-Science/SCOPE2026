# Independent mathematical audit

## correctness

PASS

For rescaled time the untilted angular semigroup is a heat semigroup weighted by the no-reset probability e^(−qt), plus a constant reset-age term; its difference from stationary projection has sup norm at most 2e^(−qt). The time-one Feynman–Kac operator is analytic near zero tilt (bounded potential), so the simple separated spectral projection and exponentially decaying complement persist locally. For any fixed initial angular law the leading prefactor equals 1 at zero tilt and is nonvanishing nearby; applying the same decomposition to the remaining fractional time gives convergence of the scaled log mgf and its Taylor coefficients. Independently, the no-reset Laplace resolvent I(z;u,w) gives the simple renewal pole q I(q+Λ;u,w)=1. For a one-parameter tilt, zI=1+Σ x^d A_d(z) where A_d is the sum over Fourier walks of d unit steps from frequency zero, each visited frequency n contributing a factor 1/(z+n²). Thus Λ=qΣ x^d A_d(q+Λ). Lagrange inversion and polarization at tilts (u,w)=(x,ix),(x,0),(0,ix) verify the exact mixed derivative 16P/[(q+1)^5(q+4)^3(q+9)^2(q+16)]. Replay: /workspace/review-evidence/5-cycle-modular.js, whose degree bound and coefficient bound turn 33 exact evaluation points at each of eight primes into a rational identity via polynomial vanishing and CRT; the same cycle equation was checked by a separate exact homogeneous expansion. This is a coefficient certificate rather than a numerical angular truncation or a general spectral proof. Descartes' rule and exact endpoint signs at 71687/100000 and 71688/100000 certify one simple positive root and the stated signs; the denominator is positive. Rescaling contributes v⁴/D_rot³, independent translation adds only a quadratic term, and stationary angular reflection kills the mean transverse displacement and cross covariance, giving the centered-squares interpretation only as specified. checker.py and VERIFICATION.md were inspected, not executed. A zero rate neither proves independence nor determines the finite-time sign.

## originality

PASS

Bounded pass for the explicit mixed-fourth long-time sign classification in the same established model, not for the model, the general joint transform or the marginal statistics. The strongest primary antecedent already provides a pole equation for the full joint transform. Obtaining the claimed classification still requires fourth-order cross-coefficient extraction, cancellations and an all-positive-rate root proof; the checked fourth-order marginal passages fix only axis restrictions. The closest distinct indexed results differ in cumulant order or model.

## value

PASS

The mixed fourth connected moment measures non-Gaussian longitudinal/transverse coupling that neither the separate fourth moments nor the long-time Gaussian scaling can detect. The exact isolated crossover between opposite signs and its invariance to independent translational diffusion are qualitative transport information across all positive reset ratios, not an unmotivated number or a table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
