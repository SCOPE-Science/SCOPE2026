# Independent mathematical audit

## correctness

PASS

Gaussian STFT square completion gives a nowhere-zero prefactor times P(u)=Z0+sqrt(beta) Z1 u+Z2 u^2; omega<balanced mu is |u|<1. For a boundary-root-free quadratic, Rouché applied to conj(C)P-A P* = u[D+du] gives N=1 iff |D|>|d|. Independent complex-Gaussian orthogonalization reduces to |T|<|sqrt(beta)Z1| for T standard real normal, yielding q=E exp(-T^2/beta)=sqrt(beta/(beta+2)). Reversal symmetry gives tails (1-q)/2; two simple nonzero roots almost surely. Valid all beta>0, no finite Monte Carlo used as proof.

## originality

PASS

The fully read prior same-three-tone source computes first intensity; its E[N]=1 does not imply the three-point count variance. General Gaussian-zero correlation literature is credited and may provide an alternative derivation, but no inspected explicit beta law subsumes the claim.

## value

PASS

At an intrinsic balance frequency, the count is a complete natural second-order invariant for spectrogram zeros: the mean stays exactly one while variance 1-sqrt(beta/(beta+2)) decreases continuously from 1 to zero with no singularity at the earlier intensity-shape transition beta=4. This distinguishes individual realizations from expected maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
