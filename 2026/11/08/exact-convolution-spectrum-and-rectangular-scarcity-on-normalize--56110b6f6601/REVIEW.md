# Mathematical review

## Correctness
PASS under same-model proof reconstruction. The normalization is a bijection; the coordinate map from the full matrix to \(B,\ell,h,c\) is an isomorphism; additive character orthogonality gives both independent image-membership conditions and all exact multiplicities. The determinant/rank-count product and dominated-convergence asymptotic were checked algebraically. Standalone checker output:

```text
PASS q=2 m=2 n=2 spectral_bands=3
PASS q=2 m=2 n=3 spectral_bands=3
PASS q=2 m=3 n=2 spectral_bands=3
PASS q=2 m=3 n=3 spectral_bands=4
PASS q=3 m=2 n=2 spectral_bands=3
PASS q=3 m=2 n=3 spectral_bands=3
PASS q=3 m=3 n=2 spectral_bands=3
PASS q=5 m=2 n=2 spectral_bands=3
NORMALIZED_SEGRE_CONVOLUTION_PASS cases= 8
```

No finite check is used as an infinite proof.

## Originality
PASS under bounded comparisons, not a historical priority guarantee. Delsarte (1978) characterizes the unrestricted rank-metric association-scheme Fourier spectrum; Orel (2011) computes the spectrum of an unrestricted symmetric rank-one matrix graph. Both differ from the total-sum-one affine Segre patch. The closest indexed rank-one Riesz and Veronese Fourier records concern restricted character families, not the full convolution spectrum. The exact simultaneous image constraints and the aspect-ratio support law are not asserted by any inspected result. Delsarte's complete primary text was inaccessible, and some possibly dominating broad result may exist.

## Mathematical value
PASS. Restricting to normalized rank-one factors is a natural discrete model of independent two-way arrays of fixed total mass. The exact complete Fourier singular spectrum identifies which modes cannot be recovered from such increments; the effective conditioning is sharp, and the fixed-width limit with its large-width decay captures a structural phase between balanced and highly rectangular arrays.

## Sources and limitations
P. Delsarte, Bilinear forms over a finite field, with applications to coding theory, J. Combin. Theory A 25 (1978), 226–241, doi:10.1016/0097-3165(78)90015-8 (first-public-date evidence: 1978-11-01).

M. Orel, Adjacency preservers, symmetric matrices, and cores, J. Algebraic Combin. 35 (2012), 633–647, doi:10.1007/s10801-011-0318-0 (online 2011-10-08).

This work does not prove invertibility and makes no external certification claim. Unnormalized counting convolution is essential to the numerical factors, and the double limit is sequential.

Self-review: passed. Independent audit: not yet performed.
