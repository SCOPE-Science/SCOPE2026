# Independent mathematical audit

## correctness

PASS

The normalized full-softmax map has zero first softmax variation at sign-aligned e2 configurations, because horizontal tangent perturbations have zero derivative in every dot product. For synchronized and antipodal configurations, the unnormalized outputs respectively scale by 1−ηb and 1−ηb tanhβ. The one-step horizontal Jacobians are (I+ηa A_C)/(ηb−1) and (I+ηa A_B)/(ηb tanhβ−1). Eigenvalues on the symmetric/antisymmetric tangent modes exactly yield the claimed squared Floquet multipliers. Both cycles exist and attract hyperbolically precisely when b tanhβ>a and η>2/(b tanhβ−a). The boundary has multiplier one and is not asserted attracting; no global classification. Direct independent central-difference Jacobians at a=1,b=3,β=1,η=3 matched both predicted eigenspectra; code checked directly from check.py blob beb7887e2da47c912fbffd7f47f4cb5605b352eb. This is a mathematical argument, not merely VERIFY_OK.

## originality

FAIL

FAIL: A published 2026-10-18 theorem is exactly equivalent, model for model, to the new 2026-11-08 coexistence finding, giving the identical sharp b tanhβ>a, η>2/(b tanhβ−a), the same two cycles, their full transverse Floquet multipliers, and separate attraction neighborhoods. Its hypothesis 0<a<b is automatic from the new threshold since tanhβ<1. An even stronger 2026-10-26 theorem reproduces both flip boundaries and additionally the resonance-circle normal spectrum. Actual RESULT.md texts of both earlier records were fetched and read completely, not inferred from titles. The present finding is scientifically correct but entirely covered.

## value

FAIL

FAIL: Although coexistence of two locally attracting period-two cycles in a normalized attention map is mathematically motivated, the exact threshold, spectra, and local coexistence were already published with equal or stronger hypotheses. Re-presenting the same theorem without a distinct uncovered invariant or deduction does not constitute a new valuable mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
