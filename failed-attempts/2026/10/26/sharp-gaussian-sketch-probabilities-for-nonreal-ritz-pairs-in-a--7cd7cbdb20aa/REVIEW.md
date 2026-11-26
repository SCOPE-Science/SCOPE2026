# Independent mathematical audit

## correctness

PASS

Verified the fixed real iid Gaussian model in RESULT.md lines 5–78. Full column rank holds a.s. already at ℓ=2. The residual contributes only c times the regression vector in column two; conditioning on the Gaussian Gram matrix and integrating its Wishart density gives ν(1+||w||²)^(-(ν+2)/2)/(2π), ν=ℓ−1. Polar integration gives radial survival (1+r²/c²)^(-ν/2) for cw. With (x,y)=cw the discriminant is y²+4b(b+x); its negative region has closest radius b, and the negative circle-intersection coordinate there is 2b−sqrt(r²+8b²). This gives exactly the stated angular fraction and an open set of strictly positive probability. At r=b+z the arccos argument is 1−2z/(3b)+O(z²), giving 2sqrt(z)/(π sqrt(3b)); the logarithmic radial exponent has local slope b/(b²+c²) after the factor 1/2. Substitution z=v/ν gives Γ(3/2) and the stated prefactor. Beyond a fixed neighborhood the entire radial probability is bounded by the strictly smaller survival at its boundary. The diagonal shift cancels, and in ambient dimension two full rank reduces the sketch to ordinary symmetric Rayleigh–Ritz. The exact rational witness was checked from its normal equations. The frozen script was read, not executed; diagnostics are not needed for the proof.

## originality

FAIL

The central quantitative claim, not just the qualitative possibility of nonreal eigenvalues, has equivalent coverage in the distinct indexed record 71e006218203. Its catalogue path is later-dated than the assigned path, so this is a finding of demonstrated statement coverage, not a finding that the assigned authors derived it later, public priority, or provenance. Rotate the two trial coordinates with columns (-1,1)/sqrt(2) and (1,1)/sqrt(2): the model becomes the indexed one with α=d−b, δ=2b, t=c/sqrt(2), μ=d, h=b/c. Gaussian rotation invariance and equivariance of the full-rank pseudoinverse preserve the sketched eigenvalues. The indexed parabola b_ext>h+u²/(4h) uses b_ext=−w₁ and u=w₂, so both integrals compute exactly the same probability by integrating in a different order. Its q/(h sqrt(3πs)) q^(−s/2), q=1+h² and s=ℓ, is the same leading term with ν=s−1. Although its theorem is phrased for s≥3, its density step explicitly holds for s≥2 and both subsequent exact integration steps apply unchanged at two rows. Neither the alternate quadrature nor this boundary repackaging separates the main result.

## value

FAIL

A sharp rare-event benchmark for Gaussian sRR is a worthwhile quantity. As a distinct finding, however, the frozen record supplies the same benchmark as the equivalent indexed model. The alternative integration order, automatic two-row endpoint, and elementary invariant-subspace minimality observation do not provide a separate unknown benchmark or a substantive extension. The negative assessment concerns the added result, not the importance of quantifying the event.

The dated certificate retains the supplied scientific assessment, sources and limitations.
