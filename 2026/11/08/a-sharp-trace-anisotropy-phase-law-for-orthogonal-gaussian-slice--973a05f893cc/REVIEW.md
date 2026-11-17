# Independent mathematical audit

## correctness

PASS

The exact centered one-dimensional Gaussian Wasserstein cost is (sqrt(1+εuBu)-sqrt(1+εuCu))². Uniform Taylor expansion on S¹ gives ε²(uDu)²/4+O(ε³). Rotate D to write uDu=m+r cosφ and use E cos²φ=1/2 and E cos⁴φ=3/8. The checked variances are ε⁴r⁴/128+O(ε⁵) for perpendicular pairing and ε⁴r²(r²+16m²)/256+O(ε⁵) for iid pairing; their ratio tends to 2r²/(r²+16m²) for r>0. At r>4|m| orthogonal sampling is worse, at 0<r<4|m| better, while r=4|m| and r=0 have no claimed strict conclusion. Swapped unequal diagonal covariances make costs pointwise quarter-turn invariant, exactly attaining factor 2. Independent rational moment algebra and selected Gaussian quadrature support but do not replace the uniform proof.

## originality

PASS

Prior orthogonal sliced-Wasserstein work establishes qualitative counterexamples, not this near-isotropic 2D Gaussian trace–anisotropy classification or its exact Gaussian maximizers. Self/related index hits were excluded as novelty evidence. Qualified best of knowledge, not historical certification.

## value

PASS

Sharp variance-order boundary and the extremal Gaussian family are directly useful in deciding whether orthogonal projection coupling reduces or increases Monte Carlo error for a natural Gaussian transport estimator; the known generic counterexample itself is not counted as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
