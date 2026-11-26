# Independent mathematical audit

## correctness

PASS

The mandatory-part bijection gives the exact survivor quotient, with h=rAℓ(m). For m≡s mod ℓ the sum of allowed parts is ρℓ m²/2+sm/ℓ+(s−s²/ℓ)/2; the preceding shift is h−rm. The uncoloured Rademacher formula in Agarwal–Garg–Maji Corollary 2.3 has leading term ℓ⁻¹ᐟ² ∂NI₀(2√(μℓ(N+(ℓ−1)/24))). Its I₁ expansion gives (2) with dℓ=√μℓ(ℓ−1)/24−3/(16√μℓ). For the rest, Theorem 3.7 bounds the exponential sum by Oℓ,ε(N¹ᐟ² k¹ᐟ²⁺ε). With I₁(u)≤u eᵘ the differentiated Bessel term is Oℓ(k⁻² exp(u)); at k≥2 its exponent is at most half the principal exponent, and ∑k⁻³ᐟ²⁺ε converges. The finitely many other k=1 terms have smaller exponential rates. This justifies the quantitative input, not merely the leading equivalent. For t=n⁻¹ᐟ⁴, y=mt, κ=√μℓ and L(h)=log[pℓ(n−h)/pℓ(n)], on compact y-windows L(h−rm)−L(h)=κ r y t+O(t³), while exp(L(h))=exp(−γy²)[1−κ r s y t/ℓ+O(t²)]. Their product exp(L(h))·[exp(L(h−rm)−L(h))−1] gives the stated uniform mass coefficient κ²r²y²(1/2−s/ℓ). For clarity, the square-root-log cutoff in m in step 4 requires h=O(√n log n), larger than the window initially stated in (3). The same Taylor expansion gives the displayed main terms there with remainder O(n⁻¹(1+log n)³), which suffices for the extension invoked in step 4. The survivor at sufficiently large cutoff is O(n⁻²); summing the local error yields O(t² polylog n)=o(t). Shifted Euler–Maclaurin has no order-t contribution from the leading mass function because it vanishes at zero; the second Gaussian integral gives (ℓ−2s)Cℓ,r and hence strict eventual ordering for fixed ℓ,r. The uploaded test and retained output were read only; no finite test is used as an asymptotic argument.

## originality

PASS

The exact point law and its leading local Rayleigh term are prior, and the coefficient expansion is an input, not a new partition asymptotic. The genuinely distinct result is the uniform signed second local term and the nonzero residue-class correction with eventual strict order. The closest indexed finite-size bias concerns a different random mark of the same gap.

## value

PASS

The Rayleigh limit is blind to residue order. The second local term identifies precisely how the omitted arithmetic progression affects where the first deficient part lands, and the summed signed coefficient yields asymptotically strict ordering not visible in the leading law. This is a sharp structural correction for a previously studied statistic, not just an improved numerical fit or a new name for the exact count formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
