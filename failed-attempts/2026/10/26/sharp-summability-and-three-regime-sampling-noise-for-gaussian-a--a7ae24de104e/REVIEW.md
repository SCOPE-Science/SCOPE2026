# Independent mathematical audit

## correctness

PASS

The Gaussian restriction has argument 2|sin(πx)|/σ, so normalization cancels exp(−2σ⁻²) and gives the stated Bessel ratio. With z=2σ⁻², I₀(2z)/I₀(z)² is asymptotic to √(πz), giving c=√(2π). The ratio minus one is the squared distance to the mean and positive because the factor is nonconstant. Thus σE(σ) has positive finite extrema on the interval after extension at zero. Distinct singleton terms are orthogonal, so the uniform two-sided bound follows. Activating each finite initial segment at small enough positive ρ proves necessity for the supremum over d,ρ, including nonsummable weights; no infinite-dimensional kernel is needed. With t=p/4 the finite sum is exactly Σ_{j≤floor(ρ^{−1/t})} E(ρj^t). The stronger uniform statement E(σ)=c/σ+O(1) on (0,1] gives, after multiplying by ρ, cΣj^{−t}+O(ρ floor(ρ^{−1/t})); this proves the first two limits. For t<1, with A=ρ^{−1/t}, the sum divided by A is a Riemann sum of E(u^t). The portion j/A≤δ has mass at most a constant times δ^{1−t} using the bound by u^{−t}; this justifies the positive finite improper integral and the floor at the upper end. Independence and translation invariance give the exact variance at f=1, where the bias is zero. For general square-integrable input the integrated variance is at most ||f||₂²||K||₂²/M, so the inference about the uniform variance rate is valid. The frozen checker was inspected, not executed: for p=2 it checks a range for scaled energy, not convergence to the stated integral constant. This limitation does not affect the analytic proof.

## originality

FAIL

The comparison must use more than Sun's headline upper bound. In the full proof of Sun's Theorem 3.6, Eq. (3.7) and the displayed integral limit already give lim σ||ψ_σ||₂²=π||φ||₂², exactly √(2π) for this Gaussian. Its finite-bandwidth energy is also given there. Proposition 5.1 gives the active singleton energy identity; any finite list of weights can be extended by a positive decreasing summable tail, so the identity and the exact variance decomposition apply to each needed finite kernel even if the tested original sequence is nonsummable. With this full known energy profile, the necessity and power-weight results are direct finite-partial-sum tests, p-series summations and a Riemann sum of the already specified profile. The exact constant-input variance formula is a direct substitution in Sun's Eq. (5.14). The explicit combined statement is correct, but no distinct mathematical result past these direct consequences is established.

## value

FAIL

Diagnosing the boundary of dimension-independent noise for a fixed design is motivated. Here, however, the quantitative statement packages a known exact variance identity, a known exact radial energy profile and its known leading coefficient with routine power-series and Riemann-sum evaluations. There is no new mechanism, independent estimate, or nonmechanical boundary invariant beyond that specialization, so the frozen record does not establish a distinct valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
