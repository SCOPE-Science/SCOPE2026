# Independent mathematical audit

## correctness

PASS

The unnormalized cube Laplacian has Walsh eigenvalue 2k on characters of weight k, so the distance-r shell is 2⁻ᵈΣ_k K_k(r)z^{k²}, with z=e⁻⁴ᵗ, K₁=d−2r and |K_k|≤binom(d,k); at r=d this is 2⁻ᵈF_d. For 0≤z≤b=1/d+1/d³≤(9/8)/d, separate k=2 and use k²≥3k for k≥3, obtaining the stated absolute tail <0.81/d². Apply the same term bounds to the derivative at z=b, using k²/k!≤(3/2)/(k−3)!, to bound |F′+d|≤2(9/8)³/d+4.51/d⁵<d. The alternating tail at 1/d has positive sign, while at b the linear part −1/d² dominates. Hence F starts positive and crosses a unique first zero z_d in the bracket, with strict negativity immediately above. For all other shells the lower bound 1−(d−2)b−0.81/d² is positive on 0≤z≤z_d. This proves the persistent horizon and its exact vanishing pattern without an assertion of uniqueness of zeros on the whole time axis. The root identity dz_d−1=binom(d,2)z_d⁴+O(d⁻⁶)=1/(2d²)−1/(2d³)+O(d⁻⁴) gives the claimed logarithmic expansion.

## originality

FAIL

Direct Walsh duality gives full exact coverage in the distinct indexed entry 11278c25117d, An alphabet-independent first positivity threshold for Gaussian kernels on Hamming products. In the binary case its Gaussian Gram eigenvalues are exactly 2^d times the biharmonic heat entries, indexed by the difference of the two heat vertices; the relation is not merely the occurrence of the same polynomial. Its all-dimension first-loss threshold, corank and sharper logarithmic expansion imply the entire frozen Finding. Its November 2 dated path is later than the frozen October 26 path; this is present coverage, not a priority finding. The October 25 entry 40e7711b848a already covers the dual threshold and vanishing pattern for d≥17.

## value

FAIL

The antipodal cutoff is a natural exact semigroup invariant, and a sharp time is more useful than qualitative eventual positivity. But the frozen new-claim content, including the sharper bracket and third logarithmic term, is mechanically implied by the all-dimension Gaussian threshold. The Fourier identification is immediate from the shell formula and no additional heat-specific regime or consequence beyond this implication is established in the Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
