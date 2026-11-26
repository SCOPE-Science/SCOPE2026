# Independent mathematical audit

## correctness

PASS

The disk at the origin has amplitude 5 and the annulus amplitude 2, giving 57π/4. Horizontal slices reduce each translated disk intersection to the overlap length of two intervals of fixed half-widths, a nonincreasing function of separation. The large-disk self term gives positivity for r<3 and zero for r≥3. L² translation continuity gives continuity; the Fourier quadratic form is strict because |ĝ|² is positive on a neighborhood of zero and an exponential sum of distinct frequencies cannot vanish there (restrict to a generic line and use Vandermonde). The Abel identity can also be proved without a singular limit: the J₀ series gives ∫₀ᵃ ρJ₀(ρr)/√(a²−ρ²)dρ = sin(ar)/r; pairing this integrable radial frequency window with the compactly supported F gives 2πaAₐ by Fourier inversion and Fubini. Independently checked the trigonometric Legendre formulas and all four normalization factors. For the tail, bₖ ≤ (21/8)(9/16)^k/(k!)², so convolution uses Σ binom(m,k)²=binom(2m,m)≤4^m; hₘ≤1, and the successive majorant ratio for m≥28 is ≤(9a²/4)/29². Reviewer-written exact rational replay `python /workspace/review_checks/2.py` confirms the lower-degree signs, 9A₃−A₁>1, and 5A₄−A₂<−1/200, with central value −0.005618338733205308 and certified radius less than 1.5×10⁻¹⁴. Multiplication by 2/57 gives the claimed bound; the Schoenberg obstruction follows. No properties of the coefficients above degree three were inferred. Frozen code inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the explicit compactly supported, nonnegative nonincreasing planar profile and its first negative spherical harmonic. The general even-dimensional counterexample, the Abel window, Schoenberg's test and autocorrelation positivity are not the contribution. The mathematical comparison is based on directly inspected primary and published texts, not on negative search evidence.

## value

PASS

Nonnegativity and radial nonincrease are natural covariance constraints, and dip detection through degree two would miss the obstruction. The two positive disks supply a reproducible shape-restricted counterexample, not another example solely of unrestricted even-dimensional failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
