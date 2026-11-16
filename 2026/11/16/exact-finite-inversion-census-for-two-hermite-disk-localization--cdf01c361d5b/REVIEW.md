# Self-review

## Correctness — PASS

Using the normalized STFT convention and area parameter, the Hermite–Laguerre radial density yields \(\lambda_k=(1+\rho)q_k+(k-s)p_k\); independent substitution shows \(\lambda_k-\lambda_{k+1}=p_k[(s-k)(s-k-1)+\rho s]/(k+1)\). Off-interval positivity, the \(k=0\) boundary and the quadratic discriminant for \(k\ge1\) prove every order switch and the exact index count. For \(0<\rho<1\), the count is \(\lceil (1-\rho)^2/(4\rho)\rceil\). At integer area every positive mixture has strictly positive adjacent gaps. A direct independent quadrature and symbolic checker passed 3,081 assertions; the proof, not enumeration, handles all indices.

## Originality — PASS (provisional historical priority)

The closest source is Svela, arXiv:2410.18769, §§3.3, 5.2, 6 and Proposition 6.7: its mixed-state localization theorem covers diagonalization and general eigenvalue-integral formulas, which are **not** claimed as novel. The new assertion is the sharp weight-dependent **ordering and exact finite reversal-count** phase diagram, including tangencies and infinite-to-finite regularization. Alaifari–Yang, arXiv:2410.05486, motivates independent Hermite windows for multiwindow phase retrieval, but treats ambiguity stability rather than disk eigenvalue crossings. A dedicated earlier ordering analysis could still exist; literature indexing is not a proof of worldwide priority. Searches compared mixed-state terminology, weighted Laguerre spectrograms, order inversion, and available previously published pure-Hermite disk findings.

## Value — PASS

Mixing two natural and individually solvable spectrogram localization channels is directly motivated by multiwindow measurement design. The classification quantifies a qualitative discontinuity: any positive Gaussian weight reduces infinitely many unstable adjacent index orderings to a finite number, with an exact \(\rho^{-1}\) divergence rate as its share vanishes, and \(\rho=1\) the sharp universal monotonicity threshold. It states a complete natural phase diagram rather than an arbitrary small-parameter calculation.

## Limitations and priority risks

Spectral eigenbasis and general integral representation are covered by established prior theory. The theorem neither asserts optimal phase retrieval nor classifies nonconsecutive eigenvalue ties. Independent audit and exhaustive worldwide historical-priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
