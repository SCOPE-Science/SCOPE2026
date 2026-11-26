# Independent mathematical audit

## correctness

PASS

At fixed positive age the model is a positive multiple of a Gaussian with covariance Σ=2τD. Its log is a+bᵀx−xᵀH x/2 with H=Σ⁻¹ positive definite and b=Hμ. Completing the square recovers μ=H⁻¹b, D=H⁻¹/(2τ), and M=(2π)^(d/2)√det(H⁻¹) exp(a+bᵀH⁻¹b/2). Every such real a,b and SPD H is admissible. Taking logs is injective, and evaluation of these quadratics is injective exactly when its kernel in the full quadratic space is zero: a nonzero kernel vector can perturb any admissible coefficients by a sufficiently small amount without leaving the open negative-definite cone. Rank gives the lower bound and 0,e_i,2e_i,e_i+e_j successively kill all constant, axis and cross terms of a kernel quadratic, proving sharpness in every d≥1. The planar conic wording covers linear zero loci as well, since a line is contained in a degenerate conic. At one unknown-age clock time, keeping τD fixed keeps the entire field fixed for the same center and mass. At two post-release times an unisolvent array gives the two inverse covariance matrices, whose ratio ρ>1 gives t₀=(ρt₁−t₂)/(ρ−1) and then D, μ and M. This is sufficiency, not a two-time minimum or a stability claim. Inspected the frozen supplemental checker and 1509-check report without executing the uploaded script; the proof does not depend on numerical tests.

## originality

FAIL

No distinct mathematical contribution beyond the standard Gaussian form and polynomial interpolation/rank calculation is established. The main sensor theorem is a direct specialization of quadratic evaluation to an open coefficient set, with an invertible change of parameters. The count and geometry are exactly the usual interpolation dimension and kernel. The temporal observations follow by substituting Σ=2(t−t₀)D into the same classical profile and taking one matrix difference or keeping the product fixed. This is an implication assessment, not a claim that a matching paper states the combined physical application verbatim.

## value

FAIL

The exact noiseless rank test is a useful implementation guideline, but the asserted mathematics is textbook interpolation of a quadratic after taking logs, followed by covariance scaling. The count is merely the coefficient dimension, the construction is coordinate quadratic interpolation, and the one- and two-time claims are immediate scalar-product identifiability observations once the covariances are known. There is no nonroutine result on sharp multi-time design, constrained sensor geometries or stability in the finding. Better motivation alone would not salvage a distinct scientific claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
