# Independent mathematical audit

## correctness

PASS

From zero the update length is |b_I|/R_I. Row selection gives the conditional ratio with numerator Σ|b_i|^qR_i^{2s−q} and denominator ΣR_i^{2s}. For s=0 Gaussian density near one row origin gives q<d. Otherwise concatenate the rows in dimension md and write a=rθ. The ratio is r^(−q) times an angular function whose denominator is bounded above and away from zero. The squared length of each angular block is beta(d/2,(m−1)d/2); its contribution is integrable exactly when q<d+2s for an active b_i. Near r=0 the noncentral Gaussian density is bounded above and away from zero, giving q<md. One active row small with other rows bounded away from zero witnesses angular divergence; angles with every row bounded away from zero witness radial divergence, including at equality. Gaussian decay controls the tails. At s=1,q=2 the ratio reduces to ||b||²/||a||²; the reciprocal noncentral chi-square Poisson mixture yields the stated series, with positive weight on the divergent central component if md≤2. The central gamma/beta formula follows by separating total squared length from independent row-length fractions, and finite averaging only rescales σ. The wording 'nonsingular noiseless design' in the divergent case is properly read as full column rank (m=2,d=1), not a square inverse, consistent with the stated assumptions. Independent checks found 1.0040434±0.0020231 (one SE) versus 1.0042743 analytically in the central benchmark, and reciprocal Poisson series versus independent Laplace quadrature agreeing to about 4.2×10^(−16) relative at md=4, λ=3, σ=0.8.

## originality

FAIL

The principal claim is covered in the current corpus by a distinct, stronger result, 81db12815a13. With k=1, x₀=0 and β=2s, its freshly drawn candidate rows and weighted projection have exactly the frozen first-step law for all frozen parameters. Its exact central formula also specializes by b_i=1 and Γ(z+1)=zΓ(z). The later catalogue date of the comparison is not evidence of anticipation or loss of historical priority; the decision is about verified mathematical coverage, not provenance or attribution. The explicit noncentral reciprocal-χ² series is not stated in the matching passages; it is an ancillary evaluation by direct cancellation and the standard Poisson-mixture identity, not a separate surviving valuable frontier to which to repair the finding.

## value

PASS

As mathematics, the sharp frontier distinguishes isolated small-row events from simultaneous small-matrix events and shows precisely which divergence can be removed by changing sampling weights or increasing the number of rows, even with a full-column-rank mean design and arbitrarily small coefficient noise. This separates finite conditional behaviour from potentially divergent unconditional moments. The mathematical value of the main phenomenon is separate from the demonstrated overlap; the explicit noncentral coefficient alone is a standard special-function calculation, not a substantive standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
