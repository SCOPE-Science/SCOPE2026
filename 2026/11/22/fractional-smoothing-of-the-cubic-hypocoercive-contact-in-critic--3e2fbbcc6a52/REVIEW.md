# Independent mathematical audit

## correctness

PASS

For θ=π/(n+1), the real symmetric part H has eigenvalues −a+a cos(jθ)/cosθ and a simple zero eigenspace spanned by the normalized sine vector v. Put R=−H. Then (Gv)_j=a tanθ sqrt(2/(n+1)) cos(jθ), and the cosine square and adjacent cosine product sums give ||Gv||²=q_n and ⟨RGv,Gv⟩=h_n>0, with Gv orthogonal to v. The exponential energy identity makes equality impossible: an equality orbit would start in ker R and have a derivative remaining in ker R. The positive subordination probability law, with positive random times, then gives strict contraction for α<1 as well. On scaling the Gram matrix as (Eα(sG)*Eα(sG)−I)/s, its simple top branch starts at 2H/Γ(1+α); the first correction on v is −q_n Vα because G*v=−Gv. Taking the norm rather than the squared norm divides by two. At α=1, inserting x(s)=v+sw+O(s²) in the energy loss gives the cubic coefficient of the squared norm deficit as 2[||R^(1/2)(w+Gv/2)||²+h_n/12]. The trial vector with w=−Gv/2 attains the lower bound, giving h_n/12 for the norm deficit. Gamma-series bounds and the uniform simple eigenvalue gap on [α0,1] give a uniformly bounded fourth-order remainder and a differentiable cubic coefficient there. Its endpoint value yields the stated additional O((1−α)s³); the gamma ratio and ψ(3)−ψ(2)=1/2 give Vα>0 below 1 and Vα=1−α+O((1−α)²). The two normalizations follow in joint limits α→1, s→0; no uniformity in n or a is claimed. The frozen checker is floating-point evidence only. Independently, an equal-diagonal 2×2 triangular norm formula applied to E_(1/2)(−s) and 2s E'_(1/2)(−s) at a=1 gave a normalized quadratic deficit 0.36367249 at s=0.01, consistent with 1−2/π≈0.36338023. At α=1 its norm is exp(−s+asinh(s)), checking h_2/12=1/6. No numerical diagnostic is needed for the general proof.

## originality

PASS

The distinct contribution is the sharp fractional variance coefficient at a critical Jordan chain and its uniform matching to the classical contact law, not the classical coefficient, fractional subordination, or existence of dissipative semigroup bounds.

## value

PASS

The critical coupling eliminates the first-order norm slope, so knowing mere contractivity is quantitatively inconclusive. The result identifies the leading fractional loss as a time variance effect and resolves the singular approach to the established cubic semigroup law, giving both coefficients and the scale at which their contributions are comparable. This is a useful sharp boundary phenomenon, not a rederivation of the classical exponent alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
