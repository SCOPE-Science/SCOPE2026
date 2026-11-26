# Independent mathematical audit

## correctness

PASS

For any putative positive-finite-mean stationary law the arrival rate λ=1−p₀ is positive and less than one: at λ=1 every finite state can hit zero via successive empty arrivals, so a stationary law cannot have p₀=0. For fixed 0<λ<1, negative unit-service drift off zero and irreducibility give a unique queue invariant law, with moments from geometric drift. In fact P(z)=(1−λ)exp(λ(z−1))/(1−∫₀^λ exp(s(z−1))ds), giving a compound-geometric factor and validating its evaluation at two for λ=2−√2, since e^λ−1<1. Stationarity requires p₀=1−λ. Expanding the PGF at one gives m=λ+λ²/[2(1−λ)] and Var=m+[λ²/(2(1−λ))]²+λ³/[3(1−λ)], with mean a bijection onto (0,∞) and variance 4/3 at mean one. The squared-survival identity with independent copies gives G(X)≤1−(2−√2)²<2/3, while the mean-one geometric law gives exactly 2/3. The independent PGF-convolution replay using outward-rounded rational intervals and a 35-term survival sum encloses G between 0.5799288331138616032330 and 0.5799288331138616032368; the squared tail is bounded by 3.772×10⁻²¹. This independently certifies the wider frozen decimal bracket without treating ordinary rounded Decimal arithmetic alone as a certificate.

## originality

FAIL

The earlier revision of the very same arXiv source already gives the exact self-consistent mean-one PGF, the same variance, and the direction and numerical value of the Gini reversal against 2/3. The v2 PDF has the arXiv stamp 22 July 2026 UTC, preceding the frozen October record. The general-mean parametrization is a routine inversion of the same fixed-arrival queue PGF derivative; the proof of the already reported direction follows from one known survival probability. The more precise rigorous bracket is not present in the inspected revision, but does not rescue the original finding's claim of a distinct analytic law and reversal.

## value

FAIL

Correcting the original inequality claim and obtaining the exact mean-one benchmark would be useful, but the earlier revised paper already does both. The residual general-mean formulas amount to standard queue moments and the inversion of one quadratic; the improved decimal certificate is not motivated by any decision near the Gini gap, which is already separated using the first survival term. No independently worthwhile unresolved target remains as framed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
