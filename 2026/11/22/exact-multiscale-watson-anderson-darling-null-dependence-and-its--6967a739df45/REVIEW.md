# Scientific review

## Correctness (C): PASS

The claim concerns the cross covariance of the ordinary Anderson–Darling statistic with the Hwang–Kuriki generalized Watson statistic of orders \(m\ge2\), under a fully specified continuous null and \(n\ge2\). Canonical quadratic-kernel bookkeeping leaves only matching off-diagonal pairs. Direct log-kernel integration reduces the mixed moment to a Bernoulli-polynomial integral; a second exact polynomial identity reproduces its rational constants. A positive Fourier series gives the sign, frequency likelihood-ratio ordering proves strict order decay, and the exact marginal kernel variances yield sample-size growth and the nonzero harmonic floor. Independent finite-sample simulations corroborate, but do not prove, the stated quantifiers. The included checker passed 129 assertions.

## Originality (O): PASS, with qualified historical priority

Hwang and Kuriki's 2024 paper supplies the higher-integrated Watson kernel and marginal spectral facts. A published earlier calculation already gives the ordinary Watson (order-one) and Anderson–Darling covariance, so that case is not claimed. The exact higher-order mixed coefficients, strict order monotonicity, and nonzero limiting correlation floor were absent from the inspected relevant primary statements and queried scientific-result records. Stephens's 1974 component decomposition supplies important classical context, not this cross-family sequence in the sections inspected. Earlier integrated-empirical-process work (Henze–Nikitin, 2002) could not be fully inspected; the possibility of implicit coverage elsewhere remains a real risk. Full priority cannot be independently certified.

## Value (V): PASS

The result quantifies same-sample redundancy between classical tail-weighted and modern multiscale uniformity tests, at every sample size, and shows that higher Watson integration order has a positive asymptotic dependence floor rather than making the tests decorrelate. Such exact joint-null second moments are relevant to designing combined goodness-of-fit tests and understanding the limits of tuning-scale diversification.

## Scope and limitations

The null must be fully specified and continuous; no fitted parameters, tied data, two-sample variants, general joint critical values, or simultaneous growing-order/sample-size limit are covered. A same-model analytical and computational review cannot substitute for an independent mathematical audit. The exact coefficients were verified for several orders in executable code, while the infinitely many orders are established by the proof rather than enumeration.

Self-review: passed. Independent audit: not yet performed.
