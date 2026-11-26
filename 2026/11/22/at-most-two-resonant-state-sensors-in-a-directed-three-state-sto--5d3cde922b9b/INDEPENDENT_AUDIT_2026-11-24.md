# Independent mathematical audit

## correctness

PASS

Flux balance gives pi_i r_i=abc/P. Independently, for Re(s)>0 the transform of the return probability to i is [1/(s+r_i)]/[1−product_j r_j/(s+r_j)], by exponential holding and renewal after each full clockwise trip. Centering subtracts pi_i/s from the return transform; multiplying by pi_i and taking twice the real part gives the stated two-sided normalization (the covariance is even). Exponential decay gives the value at zero by continuity. Symbolic simplification recovers the exact numerator, with coefficient 2abc/P, and denominator ω⁴+Lω²+P². As a function of z=ω², the derivative's numerator is Δ_i−2H_i z−z², so it has one strictly positive zero iff Δ_i>0; if Δ_i=0 the leading spectral decrement is −(2abc/P)H_i ω⁴/P⁴. The sum of the three discriminants is (P−L)(3P+2L)≤0, and H_i−H_j=(r_j−r_i)(a+b+c). Hence resonance is a suffix ordered by exit rate, with ties respected. At every z>0 the normalized profile is strictly decreasing in H_i; if the better sensor has a positive-frequency maximum, comparing at the worse sensor's positive maximizer, or comparing against its zero-only gain 1, proves the claimed strict ranking for unequal rates. The Δ factors at (t,1,1) are (t−1)(t+5) and two copies of −(t−1)(t³+2t²+t−1). The cubic is strictly increasing for positive t, and the relaxation discriminant t(t−4) is negative throughout 0<t≤theta. Replay: `python /workspace/review-evidence/reproduce.py 4` reconstructs the full Fourier rational identity from renewal and checks the exact factorizations.

## originality

PASS

General fluctuation spectral methods and a prior one-indicator, one-fast-rate formula are credited. The supported distinction is the simultaneous census at arbitrary positive exit rates, the exact relative ranking of the three fixed sensors, and the full two-equal-rate count including the zero/two transition on the slow-rate side. One sensor's spectrum, an all-observable efficiency bound, or existence of some nonmonotone observable is not that joint classification.

## value

PASS

An experiment measuring just one occupation indicator need not have access to an optimized real observable. The joint all-rate bound, rate ordering and reentrant phase determine which of the actual binary channels can show a peak. The nonreal relaxation regime without any binary peak is a clear obstruction to reading spectral modality off the eigenvalues. This is a useful all-rate structural classification rather than the previously known one-sensor calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
