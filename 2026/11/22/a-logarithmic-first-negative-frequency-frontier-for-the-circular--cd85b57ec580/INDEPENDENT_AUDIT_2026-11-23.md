# Independent mathematical audit

## correctness

PASS

The half-line Fourier transform divided by π is e^(−n²/(4t))/(2√(πt)). Substituting x=π+v/t in its omitted tail yields the sign factor (−1)^n and multiplier e^(−π²t)/(πt); this uses integer n. Independently checked that the even extension of the J_t integrand without the cosine is the product of a Laplace kernel and a Gaussian, whose strictly positive integrable Fourier transforms give strictly positive convolution at every real frequency. This gives all odd signs, not only nearby or at large t. For the rational approximation, both the L1 norm and second derivative L1 norm of e^(−2πv)(e^(−v²/t)−1) are O(1/t), by exponential domination of the polynomial derivative bounds; its first derivative vanishes at zero. Two integrations by parts and the small-frequency L1 bound give an absolute O(1/[t(1+q²)]) error, hence a uniform relative O(1/t). The resulting log comparison is decreasing for n>0 at large t and has slope −π+o(1) near its root. At n=2πt+Δ with Δ=O(log t) the balance is −πΔ+(log t)/2+log(2π^(3/2))+O((log t)^2/t). Uniform log error keeps the sign everywhere outside the claimed strip and the even lattice gives the added two units. Independently, at each fixed t>0 the eventual sign on even n is negative: two integrations by parts in the original integral give a_t(n)=[(−1)^n f′(π)+o(1)]/(π n²), with f′(0)=0, f′(π)<0 and the remainder by Riemann–Lebesgue. Thus existence, parity, and the large-t restriction on localization are consistent. Read frozen proof and support including the reported 81 checks; uploaded checker was not run.

## originality

PASS

Qualitative non-positive-definiteness at all parameters and the logarithmic bulk-versus-endpoint mechanism for a finite grid are prior. Checked the continuum claim against those results at the level of the actual Fourier observable. The all-odd exact positivity and the uniform even-mode transition with its own constant were not established by the inspected statements. The oldest truncation result remains an explicit source-access risk.

## value

PASS

For a natural circular covariance candidate, it matters how far a spectral truncation can be taken before the first negative variance appears, not merely that some negative coefficient exists. The explicit logarithmic displacement, uniform sign separation and even-lattice ambiguity provide this information for the continuum problem; exact odd positivity also allows unrestricted selection of that parity. No finite-bandwidth exact rounding or positive definiteness of the full kernel is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
