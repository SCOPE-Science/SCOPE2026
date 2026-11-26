# Independent mathematical audit

## correctness

PASS

Analyticity of the rational Laurent multiplier near the unit circle gives an absolutely summable real kernel. The kernel sign sequence at a fixed output coordinate attains the absolute row sum, as does the analogous row test on each cycle. With h=λ^(−1/4), the lower quadratic bound on the Laplacian symbol gives L¹ Fourier convergence after scaling to (1+ξ⁴)^(−1), hence uniform coefficient-profile convergence and convergence of absolute masses on fixed scaled compact intervals. Differentiating the multiplier and integrating its squared derivative after θ=hξ gives Σ k²|g_k|²=O(h^(−1)); Cauchy–Schwarz then bounds the mass at |hk|>R by O(R^(−1/2)), so passage to the full absolute sum is valid. The continuum kernel has signed mass one, and its negative intervals after x/√2 scaling give absolute negative mass e^(−3π/4)/[√2(1−e^(−π))], yielding the claimed constant. For fixed λ, periodization preserves the row sum and changes its absolute mass by at most twice the mass outside any finite kernel window whose indices have distinct residues. For fixed n, the nonconstant Fourier modes vanish as λ→∞ and the constant mode is exactly averaging, with induced maximum norm one. Both orders of limits are proved. The verification note's shorthand about a unique inner quartic root should be read with the branch condition in RESULT.md and the checker; the full quartic has a conjugate pair inside, and the branch fixes which one is used before taking twice the real part.

## originality

FAIL

The central lattice endpoint coefficient and sharp absolute-kernel mass law were already established for exactly the same bilateral resolvent in Resultary 6e210e2d0823. The use of a variation seminorm rather than a maximum norm in that statement does not change the gain: both induced gains equal the absolute sum of precisely that kernel for every λ. The two cycle limits were not found stated together in the inspected sources, but follow by the standard periodization of that known absolutely summable kernel and the known fixed-cycle convergence to averaging. Thus the distinct phrasing and a different lattice proof do not supply a distinct quantitative claim of the scope asserted.

## value

FAIL

Worst-case overshoot is a motivated quantity, and the distinction of limits is a useful illustration. But the only nontrivial sharp number and the requisite bilateral scaling were already obtained. The remaining cyclic observation is a direct application of absolute summability and constant-mode projection, with no new cyclic sharp law or uniform estimate. Narrowing the claim to that observation would not leave a separately worthwhile new result under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
