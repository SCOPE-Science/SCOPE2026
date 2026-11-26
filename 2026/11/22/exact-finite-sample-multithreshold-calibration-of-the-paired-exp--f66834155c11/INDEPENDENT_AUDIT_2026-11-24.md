# Independent mathematical audit

## correctness

PASS

For a common-rate exponential pair the sum and fraction have joint density λ²s exp(−λs) on s>0, 0<t<1; folding t gives a uniform ratio independent of the sum. Conditional on all labeled sums, the marks remain iid uniforms, and sorting the sums only permutes them. With any nonempty sum-measurable K fixed by this conditioning, adding the next uniform and truncating at jc exactly propagates the restricted partial-sum density. The zero and one CDF boundaries follow from the open uniform support. The maximum has no atoms, since each level set lies in the union of finitely many nonconstant linear level sets. The upper scan p-value is therefore uniform conditional on the sums and hence unconditionally, at every λ. The lower scan follows by reflection, not by combining two unadjusted tails. The stated covariance follows from sharing k uniform terms between prefixes k and ℓ. Independently, in the four-pair example write u=Z₁+Z₂. For u≤3/2 the feasible area in (Z₃,Z₄) is 1 up to u=1, then 1−(u−1)²/2 up to 5/4, then 2−u+7/32 up to 3/2, and zero above. Weighting by the triangular density gives 1/2+1331/6144+409/3072=5221/6144, distinct from the marginal product 19159/24576. This is a CDF value; at that observed maximum the upper p-value is 923/6144.

## originality

PASS

The supported distinct result is the exact dependent finite-sample null calculation for a nested scan of sum-ranked prefixes, valid conditional on a sum-only choice of ranks. The ratio, sum–fraction independence, convolution and probability-integral transform are established ingredients. The closest inspected fixed-threshold and permutation-averaged antecedents address different outputs and do not supply this selection-conditional scan calibration. This is a bounded assessment, not a historical-priority certification.

## value

PASS

Choosing a threshold after examining the scan invalidates single-threshold calibration when the same marks recur in several prefixes. This result gives an exact finite-sample answer to that multiplicity problem at unknown rate, including flexibility to choose the set of candidate ranks from all pair sums. The four-pair discrepancy makes the dependence practically relevant even at very small sample sizes. It does not claim power superiority or an efficient large-sample implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
