# Independent mathematical audit

## correctness

PASS

With the stated unnormalized lag DFT, replacing x+t_i by independent summation variables gives the product of the r Fourier factors including the negative sum frequency, with no normalization factor. Shifting the x-sum by N/2 proves every odd autocorrelation zero; the Fourier support and conjugate symmetry are as asserted. For equal power and equal selected samples the unit ratios satisfy h(2j+1)=h(2j−1)h(1)^2. Thus with z=h(1) they satisfy h(2j+1)=z^(2j+1). At N=4m the terminal indices 2m+1 and 2m−1 are paired by negation; at N=4m+2 the terminal index M=2m+1 is self-conjugate and its ratio is ±1. Both give z^N=1, including N=4 and 6; all ratios are precisely those of a cyclic translation. For reconstruction, the initial phase is an unknown parameter, not a freely chosen final phase: the normalized measured phases fix each higher phase as a monomial in it, and the terminal relation fixes its N-th power. For the lower bound, at fixed positive magnitudes and optionally fixed Nyquist sign the signal family is a full m-torus. Each individual coefficient is zero or a constant times a character there. Fewer than m such rows in the integer exponent matrix have a positive-dimensional kernel. A finite translation orbit cannot exhaust a fiber; this proves the claimed fixed, nonadaptive individual-entry lower bound.

## originality

PASS

The distinct indexed full-fourth-order coset theorem already implies full-spectrum reconstruction for this class. The supported increment is the exact minimum number of individual entries with the power spectrum, including the specified deterministic design, proof for all allowed signals, and lower bound against every fixed smaller design. A generic few-measurement theorem or the larger full-spectrum result does not determine the number or this subset; generic recursive phase recovery is prior method, not itself credited.

## value

PASS

The proof turns a full higher-order spectrum into an explicit set of only floor(N/4) entries once power is known, in a natural all-zero-bispectrum family. The sharp match to a lower bound, including the two parity cases and every full-odd-support signal, is the valuable increment, not reconstruction using the entire fourth-order array.

The dated certificate retains the supplied scientific assessment, sources and limitations.
