# Independent mathematical audit

## correctness

PASS

The regular polygon is the intersection of equally spaced supporting halfplanes at apothem r=R cos(pi/n). Along a ray the positive first intersection is r sec(t) for nearest-side-normal gap |t|<=pi/n; for even n the opposite ray shares the gap, for odd n it has complementary gap b-t. Uniform angular measure gives U uniform on [0,1]. Folding the odd secant sum about 1/2 proves an increasing quantile; secant addition and the even 2n quantile yield the stated rational monotone transport with positive denominator. Elementary secant and tangent integration gives exact moments, including cross-term -2 log(cos b)/sin b. The uniform Taylor remainder for b=pi/n yields coupled all-Lp deficiency limits 1-U^2 and 1/2+U-U^2, hence variance constants 4/45 and 1/180. Valid n>=3, R>0; boundary rays through vertices have angular measure zero. Independently reconstructed actual polygon-edge intersections matched 4,114 ray results (error <=2.23e-15); 1,809 transport comparisons, 34 high-precision quadrature checks, and symbolic leading-moment checks passed. Finite tests are only corroboration; analytic argument proves arbitrary integer n.

## originality

FAIL

Uwe Bäsel (2012), Section 2 equations (5), (7), (11), (14), (15) and Lemma 1, already proves an explicit all-direction, all-chord-length offset-threshold function d_n(s,phi) for EVERY regular n-gon before integrating offsets. In each angular sector those formulas solve the endpoint-side geometry as an affine equation q_k(s,psi) in s, thus specifying which chord length occurs at offset zero. Restricting that stronger directional geometry to p=0 yields the exact central angular chord profile. Pushing uniform direction through that profile, taking elementary secant sums and folding, gives the submitted odd/even laws; algebra on the two laws gives the monotone n-to-2n transport, moments and uniform Taylor variance limits. The older paper does not print the latter formulas, but its non-marginal directional theorem supplies the mathematical determination already. Its final offset-INTEGRATED CDF alone would NOT determine the center-conditioned distribution; the implication rests instead on Bäsel’s more informative, explicit Lemma 1. This is prior mathematical coverage by a stronger family of directional geometric formulas, not simply title or parameter matching.

## value

PASS

The uniform angular central-section distribution is a natural geometric invariant of regular polygons. Complete quantiles, an explicit odd-to-even cross-polygon coupling, and exact parity-separated fluctuation constants provide meaningful benchmarks for isotropic central-section measurements and convergence to the Euclidean disk. Value is intrinsic to the motivated continuum family, notwithstanding the prior mathematical determination via stronger directional chord formulas. The result is not an arbitrary small numerical instance or a mere count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
