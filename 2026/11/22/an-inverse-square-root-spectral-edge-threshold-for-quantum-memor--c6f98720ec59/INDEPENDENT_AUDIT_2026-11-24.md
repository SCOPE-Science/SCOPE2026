# Independent mathematical audit

## correctness

PASS

The bounded Hamiltonian Volterra equation reduces in the energy representation to the stated scalar Kummer solution, with f(0 frequency,t)=1. The evolved self-adjoint kernel has squared Hilbert–Schmidt norm equal to purity, and integrating along equal gaps gives the factor 2 and the autocorrelation G. The essential uniformity check is not implied by the fixed-gap limit alone. Set z=(r+iω)t and a=iω/(r+iω). For ω≠0 the Euler integral has weight u^(a−1)(1−u)^(−a) and prefactor 1/[Γ(a)Γ(1−a)]. Subtract the leading Laplace integral of u^(a−1) on [0,∞). On [0,1/2] the weight correction (1−u)^(−a)−1 is uniformly O_r(u); on the other half the exponential dominates, since sup Re a<1 for fixed r on |ω|≤1. The reciprocal gamma prefactor stays bounded even as a tends to zero. This gives uniform relative O_r(1/t) to z^(−a)/Γ(1−a), also at ω=0 by the exact constant response. Its modulus squared has the Gaussian limit on the scale σ=r/√(2 log(rt)) and a uniform Gaussian envelope after rescaling. For α<1/2, dominated convergence gives G(0+)=(1−α)²/(1−2α). At α=1/2 the exact inverse hyperbolic sine integral gives G(δ)=(1/4)log(1/δ)+O(1); dividing by log L after rescaling leaves 1/8, with an integrable 1+|log y| bound against the Gaussian. For α>1/2, u=δv gives the beta coefficient and an integrable rescaled y^(1−2α) Gaussian envelope; integrating contributes Γ(1−α)/2, canceled by the factor 2 in purity. These checks recover all three constants for fixed r and α. The supplied finite diagnostics were inspected, not executed.

## originality

PASS

The reset equation, its scalar response, and the ordinary logarithmic law for bounded densities are known. The subcritical branch is an elementary L² extension. The distinct claim is the critical log-log enhancement and the supercritical exponent and amplitude, which require control of the divergent energy autocorrelation. Inspected overlaps did not cover these branches.

## value

PASS

A natural integrability boundary changes a physical observable in an already studied channel. The result gives the exact log-log correction at that boundary and a continuously varying decay exponent and explicit coefficient beyond it. These are substantive distinctions not captured by the square-integrable formula or pointwise gap decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
