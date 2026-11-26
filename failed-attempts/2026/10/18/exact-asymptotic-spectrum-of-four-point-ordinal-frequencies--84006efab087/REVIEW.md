# Independent mathematical audit

## correctness

PASS

Under atomless i.i.d. sampling every relative order on a window union is equiprobable, and disjoint windows give zero cross-covariance. Summing all ordered lags with finite-sample multiplicities K and (K−h)_+ gives the asserted limiting covariance, unchanged by using K=n−3 rather than n as divisor. Independent linear-extension subset recursion for two chain constraints (`python /workspace/branches/replay_ordinal.py`) reconstructs the integer D and matches the full characteristic polynomial in exact arithmetic, with trace 17064. A separate exact Newton trace calculation agrees. The zero multiplicity is six, and positive semidefiniteness of the covariance makes the other 18 roots positive. The finite-dependent vector CLT and continuous mapping give 24 times the covariance eigenvalues, hence r/840 as stated. This is an asymptotic test law, not finite-sample calibration. The frozen verifier was inspected, not executed.

## originality

FAIL

The decisive distinct Resultary record already gives this exact 24-category covariance limit, including all 576 integer entries at scale 20160, the rank and the Gaussian limit. All 576 entries were independently compared in the same lexicographic rank-vector convention, with zero discrepancies. Its text expressly does not report the explicit eigenvalues; nevertheless the claimed coefficients and their factorization are obtained directly by standard exact charpoly and factor on its already packaged matrix. The Pearson weights are then the polynomial roots divided by 840. This is mechanical implication for the exact same matrix, not just a general formula requiring a new specialization or the detection of an identical source record.

## value

FAIL

The calibration observable itself is natural and the exact weights are convenient, but the claimed advance is limited to computing and factoring the characteristic polynomial of an identical already disclosed small exact matrix and rescaling its roots. It does not derive a structural spectral decomposition, classify contrasts, or establish a new test property. As stated, this is a routine exact-invariant recomputation rather than a distinct valuable mathematical gap; availability of an independent replay does not change that judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
