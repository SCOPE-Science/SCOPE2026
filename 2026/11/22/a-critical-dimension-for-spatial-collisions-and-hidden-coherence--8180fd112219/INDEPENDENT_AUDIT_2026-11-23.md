# Independent mathematical audit

## correctness

PASS

Condition on the last reset age (density r exp(-rt)); the no-reset contribution has trace norm bounded by exp(-rt), and the integral of rank-one projectors gives the unique stationary state. The product free probabilities give the product overlap S(t,s)^d. All integrands in the overlap/Green representation are nonnegative, so Tonelli and monotone convergence apply even when the limit is infinite. For B(t)=ΣJ_n(2κt)^4, Parseval of the characteristic function gives its angular J_0² average. In Step 2 interpret the sine inequality on 0≤θ≤π after using evenness, equivalently |sin(θ/2)|≥|θ|/π; the literal signed inequality on negative angles is a typo. Integrating (1+κt θ)⁻¹ gives the stated logarithmic bound. S(t,s)≤√(B(t)B(s)) then proves finiteness for d≥3, with strict positivity near (0,0). Independently expanding J₀(4κt sin(θ/2)) through θ⁴ gives moments 2u² and 6u⁴+2u², u=κt. Cauchy–Schwarz above u² yields probability ≥1/8; both outer tails are ≤1/32 each when R≤u≤2R. Thus each disjoint ℓ∞ annulus at R=32^j contributes at least a positive constant times κ⁻². With reset, retain R≤κ/r where exp(-rt)≥exp(-2) on those intervals, giving the stated logarithmic lower bound. Integrating B with the exponential weight and splitting κt at 1 and κ/r yields O(κ⁻¹ log²(κ/r)); squaring gives the planar upper bound. The exact one-dimensional Fourier multiplier r/√(r²+16κ²sin²(θ/2)) gives Q₁ by Parseval and a tangent substitution. The absolute difference of two independent Exp(r) ages is Exp(r), giving the stated purity integral. Averaging the J₀ addition identity gives the elliptic transform with complementary modulus r/√(r²+16κ²), hence the logarithm. The origin-neighbor matrix element is -ir(1-P_d)/(4dκ) by integration by parts and |J₀(x)|<1 for x>0; its squared modulus contributes to the strict off-diagonal gap. Dominated convergence gives P_d/r→M_d for d≥3 and hence the stated ratio. Source checker inspected, not executed: its 55 finite assertions concern truncated quadrature and algebra; the witness is sampled at five d values {1,2,3,4,6}, not at d=5. Neither the checker nor the theorem gives an exact planar equivalent.

## originality

PASS

The audited new result is the infinite-lattice square-summability threshold and its quantitative contrast with coherent purity (including nontrivial bounds at d=2), not the stationary density operator, the one-dimensional profile/Parseval specialization, standard Bessel identities or full-purity asymptotics. Closest concrete sources do not give an infinite-lattice diagonal Green-function criterion or its implication for the comparison.

## value

PASS

A pair of independent positions from the reset stationary state gives a directly defined collision statistic, distinct from a quantum-state purity measurement. The theorem pins down the dimension at which its renormalized coefficient is finite and shows that in higher dimensions coherence dominates it by an inverse-rate factor. The exact dimension threshold depends on both upper and critical lower estimates; it is not mere evaluation of the known ensemble return integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
