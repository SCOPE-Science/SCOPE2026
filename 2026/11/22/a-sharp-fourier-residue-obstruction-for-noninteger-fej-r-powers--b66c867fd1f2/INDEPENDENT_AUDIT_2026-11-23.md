# Independent mathematical audit

## correctness

PASS

Integer powers have nonnegative Fourier coefficients by finite convolution (the zeroth power is one). At each nontrivial root θ_j=2πj/N the expansion is F_N(θ_j+u)=u² times a smooth positive factor of value N/[4 sin²(πj/N)]; θ=0 is smooth and nonzero. With β=2γ, Abel regularization of |u|^β gives the transform 2Γ(β+1) Re(ε+im)^(-β-1), tending away from zero frequency to −2Γ(β+1) sin(πβ/2)m^(-β-1). Subtracting the homogeneous model from its localization is rapidly decaying away from zero frequency, by taking sufficiently many integrable derivatives of the smooth difference. For the amplitude remainder, subtract its constant and linear parts: the linear term is one frequency derivative of the model transform up to a constant. The remaining local factor is |u|^β u² times a smooth compactly supported function and has integrable distributional derivative of order ceil(β+2), giving O(m^(-β-2)) or better. Restoring the translation phase and 1/(2π), conjugate zero pairs give precisely the real S profile in the claim. The zero residue is positive and the residue sum is zero, so there is also a negative residue. The sign of sin(πγ) determines which gives an eventually negative progression. Negative coefficients exclude PSD; explicitly, the normalized circulant eigenvalues at a fixed bad frequency converge to its negative coefficient as the grid is refined. The estimate is for fixed N,γ, with no sign implied when the leading residue vanishes. Replay: frozen RESULT.md Steps 1–5 and VERIFICATION.md; verify_fejer_powers.py inspected, not executed. As an independent finite check, for N=2, γ=1/2 direct integration gives coefficient −2√2/(15π) at m=2, agreeing with the diagnostic midpoint quadrature and the predicted sign.

## originality

PASS

The supported distinct result is the explicit multi-zero Fejér residue profile with controlled remainder and forced negative arithmetic progressions for all N and noninteger powers. The one-cusp transform, the classical Fejér triangle, integer-power positivity and the one-zero case are not independent novelty. The yes/no PSD exclusion also admits a shorter general argument using smoothness at the identity for positive-type functions; the quantitative residue law is the material addition.

## value

PASS

Nonnegative pointwise values do not suffice for covariance admissibility. In this canonical finite-band kernel family the quantitative result locates spectrally forbidden modes throughout an explicit infinite arithmetic progression and determines their leading decay, where a binary impossibility or a finite numerical example would not. The dependence on all nodes, including exact residue cancellation, is mathematical content beyond the older single-cusp obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
