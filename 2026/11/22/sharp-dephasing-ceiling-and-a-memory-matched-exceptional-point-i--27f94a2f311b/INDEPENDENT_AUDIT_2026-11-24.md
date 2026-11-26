# Independent mathematical audit

## correctness

PASS

Conditioning on a fresh independent reset mark gives the normalized average M=e^(−γt)ρ₀+γ∫₀ᵗexp(−γ(t−s))ρ(s)ds; the initial atom is indispensable. Differentiating closes the averaged dynamics, with coherence vector initially (1,1) and derivatives (−iω,0). The characteristic discriminant is the stated Δ. Any single-mode f would force −iω as an eigenvalue, excluded by det(A+iωI)=−irω, so the mode with strictly larger real part cannot cancel. At matched rates above the critical gap the modulus after removing e^(−rt) is strictly positive and periodic (its imaginary sine term and real cosine cannot vanish together); at equality it is the modulus of a nonvanishing linear polynomial times the exponential. These give the full log limit, not merely an envelope. The positive quadratic γ|f|²+r|h|² has derivative −2rγ|f−h|², and f=h is not an eigenline for ω≠0, giving strict spectral stability. For γ<r the trace bound is strict; for d=γ−r>0, |Δ|²−(2d²−Re Δ)²=16rγd²>0 forces Re √Δ>d. At γ=r the bound is saturated exactly for |ω|≥2r. At the critical gap the nonzero off-diagonal of the repeated-root matrix guarantees a nontrivial Jordan block and the initial state gives a nonzero linear term in the observed coherence. Direct differentiation yields the stated nonpositive derivative, with only isolated zeros in the oscillatory regime and the negative critical limit for t>0. All matched-rate f are nonzero for finite times, so f(t)/f(s) defines a CPTP dephasing map; trace-distance monotonicity follows also by shrinking transverse differences while leaving diagonal differences fixed. Independently compared 21 high-precision matrix-series evaluations and checked matched-rate monotonicity there: python3 /workspace/reproductions/check_frozen_math.py 1. No uploaded checker executed.

## originality

PASS

The supported distinct content is the sharp age-rate ceiling with unique equality locus at fixed forward reset rate, proved for the clipped preferential-return protocol, together with the characterization at saturation. Do not assign independent novelty to diagonalizing a two-state fluctuator, to its coalescence, or to re-expressing its scalar coherence. The exact telegraph alias is material: it can give the same channel conclusions in a rotating frame, but an initialized scalar solution or a result at symmetric switching does not itself assert the sharp optimization over the other switching rate. No verified earlier statement of that optimization was located. The primary telegraph literature comparison remains access-limited.

## value

PASS

The age scale is a tunable parameter of a normalized memory-reset protocol. The sharp ceiling and its unique maximal-gap tuning give a concrete limit on how much changing that scale can accelerate coherence decay. The matched-rate channel shows that visible Jordan behavior and saturation of the long-time exponent do not require trace-distance revivals. The motivation is the exact reset rate/age rate tradeoff, not a new name for two-state coalescence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
