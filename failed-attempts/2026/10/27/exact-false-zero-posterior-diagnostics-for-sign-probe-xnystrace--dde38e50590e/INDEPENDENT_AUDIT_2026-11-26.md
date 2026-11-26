# Independent mathematical audit

## correctness

PASS

In exact arithmetic A<X> is A^(1/2) times the projector onto the whitened sketch span times A^(1/2). On the active two coordinates, a monochromatic sketch of projective sign s has residual (c/2)[[1,-s],[-s,1]], c=2ab/(a+b); both signs give zero residual. A held-out sign t therefore gives centered basic error -cst in the former case and zero in the latter. For m>=3 the all-equal, singleton-minority, and remaining sign families have counts 2, 2m, and 2^m-2m-2; the singleton case has only one nonzero basic error c and gives Q=c^2/m^2. The mean is unbiased; MSE and expected squared diagnostic have ratio m+1. Each basic variance is c^2*2^(2-m), and any pair's covariance c^2*2^(1-m) because both are nonzero only in the all-equal case. At m=2 both errors equal -c*s_1*s_2, so the correlation is one and Q=0. The result is for unnormalized independent Rademacher probes and the mathematical pseudoinverse, not a finite-precision inverse. The supplied standard-library checker check_xnys.py was inspected, not run; independent exact rational sign enumeration at (a,b)=(2,5), m=2 through 8 corroborated the law, ratio and correlation. To replay that panel enumerate the 2^m sign tuples per m, construct A-vv^T/(a+b) for the rank-one residual with v=(a,bs), or use zero for a two-sign sketch; accumulate the joint law and pair moments. Finite enumeration is not the arbitrary-m proof.

## originality

FAIL

A distinct prior indexed Resultary finding proves the complete effect at a scalar two-dimensional identity and gives per-basic-estimate projector rules. The present centered basic-estimate vector is exactly that prior vector at scale lambda=c, under the same sign coupling. Adding inactive coordinates and changing (a,b) merely applies the deterministic shift T-2c to each uncentered estimate and to the true trace. The two-probe case also follows immediately from the prior per-sketch rule: each leave-one-out direction is the other probe, so both estimates are lambda for agreeing signs and 3lambda for opposite signs. Neither the already-covered law nor this short endpoint substitution survives as a distinct scientific finding.

## value

FAIL

False-zero calibration of a standard diagnostic is scientifically useful, but the centered law and its consequences are unchanged from the prior finding. The nonidentity matrices here introduce no different sign geometry, and m=2 is an immediate substitution in the same basic-estimate rule. There is no substantive independently useful remainder in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
