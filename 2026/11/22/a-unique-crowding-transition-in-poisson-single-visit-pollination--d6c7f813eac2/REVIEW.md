# Scientific review: Poisson single-visit allocation

## Correctness — PASS

For every integer \(n\geq2\) and budget \(B>0\), the proof begins from the exact Poisson singleton success probability \(f(u)=ue^{-u}\). Boundary solutions cannot maximize because \(f'(0)>f'(u)\) for all \(u>0\). Lagrange stationarity and the sign of \(f''(u)=(u-2)e^{-u}\) reduce every global maximizer to equal means or one overloaded flower plus equal remaining means. For \(n=2\), the strictly increasing function \(t\coth t\) proves the unique threshold and its scaling. For general \(n\), convexity in budget of \(\log\sum_i p_i e^{B(1/n-p_i)}\), maximized over fixed simplex shares, proves one and only one global transition; the cubic expansion at mean two visits and strict local concavity establish the sharp interval and discontinuity for \(n\geq3\). Stationarity gives the large-budget limit. The checker completed 62,645 supplementary diagnostic assertions but is not used as an infinite-domain proof.

## Originality — PASS, conditional on accessible evidence

Després (2003) motivates brood-pollinator seed parasitism; Holland, Bronstein and DeAngelis (2004) consider excess flower production; Ezoe (online 2016) considers flower-production and fruit-abortion strategies in a related mutualism, rather than a fixed-number-of-flowers visit-intensity simplex with its exact global transition. Mathar and Žilinskas (1993), examined as a complete nine-page source, optimize the distinct shared-channel Bernoulli success probability \(\sum_i p_i\prod_{j\neq i}(1-p_j)\), not the independent-channel Poisson singleton sum. Broader Poisson throughput and resource-allocation statements were searched. The closest relevant literature does not logically imply the claimed continuous two-flower and discontinuous many-flower classification, but full access to Ezoe and DeAngelis–Holland was unavailable, leaving priority risk. There is no claim of exhaustive priority certification.

## Value — PASS

Brood-pollinator over-oviposition couples pollination benefits to repeat-visit harm. Within the precisely specified idealization, the theorem identifies a structural management and experimental-design boundary: at high unavoidable visitor traffic it is mathematically better to sacrifice one flower to excess visits than to spread every visit equally. The sharp difference between two and at least three flowers is qualitatively important and not an automatic consequence of the single-site Poisson formula. Natural flowers need not obey exact-one success or controllable arrival intensities, so the result is a mathematical benchmark rather than a field prescription.

## Limits and historical risks

Independent validation has not occurred. The numerical three-flower threshold lacks an interval certificate and does not drive the proof. Ezoe's publicly exposed abstract and first introductory material and DeAngelis–Holland's abstract were compared, but full text could not be obtained through open channels; those are unresolved historical-priority risks rather than proofs of coverage or noncoverage.

Self-review: passed. Independent audit: not yet performed.
