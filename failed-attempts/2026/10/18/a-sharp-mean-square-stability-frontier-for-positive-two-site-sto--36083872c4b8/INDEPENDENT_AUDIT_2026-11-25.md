# Independent mathematical audit

## correctness

PASS

For independent fresh diagonal factors their means and mixed moment are one and their diagonal second moments are v=exp(σ²h). Expanding the covariance map in (u,w,d) gives the printed positive two-by-two block and the separate multiplier v exp(−2ah). The Perron root of the unscaled block exceeds vc>v and its smaller eigenvalue is positive (determinant v), so its Perron root gives the full spectral radius. It is strictly increasing in v≥1, starts below exp(2ah) at v=1 and diverges. Substituting q=exp(2ah) in the characteristic polynomial gives v*=q(q−c)/(qc−1). For v>1, the left Perron weight can be written (1,sinh(2bh)/(λ+−c)), with second weight strictly below one since λ+ increases from c+sinh(2bh). Any nonzero deterministic initial satisfies u>0 and |w|≤u, so its Perron coefficient is positive even for opposite-sign initials. This directly proves the nonzero limiting squared norm at equality and geometric growth above. The prose about positive definiteness after one step needs the exception already noted immediately afterward: if only one initial coordinate is nonzero, one step is still rank one and a second step suffices. The strict left-weight check does not require this intermediate definiteness. Expansion at h=0 and q≫c as h→∞ give the two limits as stated. The continuous covariance drift has symmetric block [−2a+σ²,2b;2b,−2a] and remaining exponent −2a+σ², which is strictly dominated by the larger block eigenvalue. Positive determinant and the negative second diagonal give the continuous threshold. Hence the stated strict noise band exists and the conclusion is about fixed-step second moments, not almost-sure instability. Positivity follows pathwise from the nonnegative heat matrix and positive diagonal factors.

## originality

FAIL

Two distinct indexed records treat a=2b and contain more than a matching special-case cutoff: they give the complete two-site moment transfer, one gives the exact two eigenvalues, and one gives the continuous moment generator. The full a>b family is mechanically obtained by factoring a scalar damping multiplier out of each sample matrix. The general discrete and continuous thresholds, including both limits and the stable-SDE/unstable-large-step window, then follow by solving the same quadratic or shifting the generator. The extra arbitrary-sign assertion is a direct left-weight consequence of that same block; it does not sustain an independently valuable replacement. The related records are later by catalogue date; this is a coverage finding, not a claim of earlier priority or attribution.

## value

FAIL

The base stability-gap phenomenon is a useful benchmark, but is already expressly established for this splitter on the two-node grid. The extension only multiplies every step by a common scalar, and the resulting family of thresholds and signs is obtained directly from the known moment blocks. Neither the shift nor the elementary all-sign Perron-weight check warrants a separate exact benchmark or replacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
