# Independent mathematical audit

## correctness

PASS

From the complete N-point DFT (N=2m>=6), recover C0(t)=sum_{j=0}^2 |f_{t+j}|², C1(t)=f_t conj(f_{t+1})+f_{t+1} conj(f_{t+2}), and C2(t)=f_t conj(f_{t+2}). Equality C2 and f full support forces g full support and r_t conj(r_{t+2})=1 for r_t=g_t/f_t. Therefore r_{t+4}=r_t; on each parity cycle of odd length m the ratios are constant, and their moduli must be one. The nontrivial relative parity phase imposes alternating adjacent-product ratios, then a_{t+2}=a_t and f_{t+2}/f_t=ρ independent of t. Cyclicity gives ρ^m=1; solving C1 fixes delta=(B conj(A) conj(ρ))/(A conj(B)). Conversely this unique nonidentity parity rephasing preserves all three autocorrelation rows, hence all intensities. The proof includes m=3 and multiples of 3, where zero-lag inversion is unavailable. Independent direct intensities tested at N=6,18,30 for δ=-1; finite tests corroborate but are not the proof.

## originality

PASS

Prior exact boxcar theorem proves the same full-support fiber classification on the major subdomain even N>=8 with 3 not dividing N. This submission has genuine unproved-by-that-paper coverage at N=6,18,30,... (N=2m with m odd divisible by 3), via C2-only parity rigidity rather than C0 magnitude inversion; the stronger resonant-window paper also assumes zero-lag invertibility and cannot cover flat taps at 3|N. Originality accepted only for this nontrivial arithmetic completion, not for the overlapping domain.

## value

PASS

The missing 3|N arithmetic boundary is natural for length-three boxcar STFT: its zero-lag convolution is singular precisely there. A genuinely all-fiber classification (including N=6 and infinite N=6 mod12) without assuming C0 invertibility distinguishes uniqueness from an apparent amplitude obstruction. It is a motivated mathematical completion, not a one-off isolated numerical example. No stability, sparse-signal or N divisible by 4 claims are inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
