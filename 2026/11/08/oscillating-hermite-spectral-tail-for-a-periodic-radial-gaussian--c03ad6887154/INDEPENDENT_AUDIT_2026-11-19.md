# Independent mathematical audit

## correctness

PASS

Directly reconstructed the normalized STFT/Hermite radial density exp(-r)r^k/k!, k>=0, under r=pi(x^2+xi^2), giving eigenvalues as Gamma(k+1,1) probabilities in the union of [jT,jT+s]. The Gamma law is the (k+1)-fold circular convolution of wrapped Exp(1) on R/TZ; its strictly decreasing density p_T(t)=exp(-t)/(1-exp(-T)) makes an interval [0,s] the unique best shift. Every wrapped convolution power has density at least exp(-T)/(1-exp(-T)), and circular averaging gives the uniform positive gap m_T(T*lambda0-s). Fourier coefficients (1+2pi i n/T)^(-(k+1)) and aperture e^{pi i n s/T}sin(pi n s/T)/(pi n) give the leading n=1 term and an O(rho2^(k+1)) summable remainder. The limit s/T, noncompactness and singleton essential spectrum follow. For theta=arctan(2pi/T) in (0,pi/2), irrational circle rotation or a rational orbit of at least five equally spaced angles supplies cosines of each strict sign; rho2<rho1 makes both infinite subsequences rigorous. Independent 55-digit Gamma-cell and 600/2500-harmonic comparisons passed 35 finite cases, with max discrepancy 6.76e-11 due Fourier truncation, and tested positive gap and error envelopes. Git tree SHA recomputed with Git tree-object hashing for all 7 inspected blobs. Finite checks are corroboration, not proof of universal quantifiers.

## originality

PASS

The exact unit-period radial comb and Gaussian Hermite formula were already studied by Knutsen (2020), while a November 1 published theorem proves a stronger trace-class, oscillating-tail result for the included special case (T,s)=(2,1); neither the norm formula on its known small-width domain nor the T=2,s=1 tail is a novel constituent. The inspected primary results do not explicitly derive the uniform positive Gaussian gap and two-sided exponentially oscillating tail simultaneously for every real T>0, 0<s<T. This all-parameter statement is a mathematically natural generalization, but it follows by elementary Fourier-period substitution plus a circular rearrangement argument once the prior papers are known. Thus the remaining novelty is incremental and best-of-knowledge, not a new method or a claim of historical uniqueness.

## value

PASS

The infinite planar-measure radial comb was explicitly studied in Knutsen 2020, so both object and observable (Hermite localization spectrum) have established mathematical motivation. The unknown all-period, all-duty positive gap and the distinction between a uniquely optimal Gaussian mode and a nonzero essential limit oscillated across infinitely often are natural exact spectral facts that are not obtained by a finite table. A future investigator studying radial Toeplitz/Fock localization can use the exact gap and first exponential harmonic across parameter space; no general new theory is necessary for this exact classification to have value. The T=2,s=1 special case is already known and the Fourier method is simple; the value assessment concerns the sharp qualitative all-parameter classification, not the known norm bound by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
