# Independent mathematical audit

## correctness

PASS

White noise with covariance proportional to exposure time gives squared matched-filter SNR proportional to ||S_T||_2^2/T; dividing by the positive cycle duration gives Q_h. Expanding the squared norm as a double time integral counts lags with triangular weight 2(T-u). For k(u)=K(au), let A(T)=integral from 0 to T of u k(u). Then F'=2A/T^2>0 and F''=2k(T)/T-4A/T^3<0 by strict decrease of k, without differentiating k. Thus (T+h)F'-F decreases strictly from h to -2M_0 (use A(T)<=M_1); its unique crossing is the global maximizer. The inverse stationarity equation h=F/F'-T is strictly increasing in T and has limits 0 and infinity. Integrating the local cusp gives F-T F' asymptotic to 2 kappa nu T^(nu+1)/[(nu+1)(nu+2)]; F' tends to 1 at zero. At infinity F tends to 2M_0 and T^2 F' tends to 2M_1, giving h/T^2 tending to M_0/M_1. Gaussian autocorrelation uses c=a/(2 sigma), with moments sqrt(pi)/(2c) and 1/(2c^2), agreeing with both constants. Independent Simpson integration of the stationarity numerator on 4096 panels and bisection give T_h=1.378327080411 for c=h=1. Frozen support was inspected but not executed.

## originality

PASS

The supported distinct theorem is the autocorrelation-class result: strict uniqueness and comparative statics for all the specified decreasing kernels, a small-overhead law with a profile-dependent exponent, and a large-overhead moment law. The Gaussian subcase has demonstrable equivalent coverage in a distinct indexed record, and earns no separate originality credit. Their within-day priority is not established. The frozen 'In particular' Gaussian calculation is an illustration of the broader theorem, not the basis for this originality pass.

## value

PASS

For a natural observing objective the theorem identifies precisely when a unique duration can be chosen from the autocorrelation, and what features of a non-Gaussian profile determine the response to overhead. In particular, a cusp changes the small-overhead exponent, whereas finite integrated correlation and first moment set the large-overhead constant. This is a transferable model diagnostic, not just the Gaussian calculation or a fit to one simulated transit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
