# Independent mathematical audit

## correctness

PASS

Reconstructed the asymptotics for fixed c, α>0 and a normalized fixed mixing density with endpoint constant H. Let ℓ=log n and L=cℓ. I_c is strictly increasing from 0 to infinity above c, so the saddle t exists and is unique. For k=tℓ+O(log ℓ) and λ≤L, the tail/mass series is geometrically dominated uniformly, since L/k stays below 1; replacing ∏(k+v) by k^j gives 1/(1-λ/k) with O(k^-1) error via a summable j(j+1) bound. For the intensity deficit s=L-λ, the mass ratio is exp(s)(1-s/L)^k, tending to exp(-(t/c-1)s) with an integrable exponential envelope after multiplying by the rescaled density bound Cs^(α-1). Away from the endpoint the exponentially small conditional mass bounds the integral using only total mixing mass, so no interior boundedness of h is needed. The limit integral is H Γ(α)L^-α (t/c-1)^-α/(1-c/t) times p_k(L). Stirling contributes n^-1 exp(-log(t/c)(k-tℓ))/sqrt(2πtℓ), with uniform Taylor error O((log ℓ)^2/ℓ); the resulting constant is HΓ(α)√t/[√(2π)(t-c)^(α+1)]. Hence the level centering and sharp log log n coefficient hold, and iid counts give the maximum law along lattice-aligned thresholds, not a continuous full-sequence Gumbel law. For the marks, adding j to k contributes (c/t)^j, with a summable uniform geometric bound; combined with the same deficit domination the limiting conditional kernel factors as the specified normalized geometric law and Gamma(α, rate t/c-1). The count mark is an excess and the intensity mark a deficit. For c=1 and h=1 the saddle is e. The recorded finite numerical assertions were inspected as diagnostics, not rerun or used to establish the limits.

## originality

PASS

The supported distinct result combines a moving logarithmic endpoint with a nonvanishing Poisson tail/mass factor and gives the density-shape centering and the joint normalized latent-intensity and count marks. Fixed-endpoint asymptotics and analogous Gamma localization are established precedents; the standard Stirling and endpoint-Laplace methods are not claimed new. Two plausible Poisson-extreme comparators could not be fully inspected and do not support a claim about absolute priority.

## value

PASS

The calculation separates the Poisson saddle from the mixing endpoint cost: the density exponent changes the sharp log log n centering and determines a measurable Gamma localization for latent intensity. The independent geometric count excess quantifies a different, lattice-scale effect. These exact constants and marks are useful for the non-Gumbel full-sequence regime and go beyond applying an iid maximum identity to an unspecified tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
