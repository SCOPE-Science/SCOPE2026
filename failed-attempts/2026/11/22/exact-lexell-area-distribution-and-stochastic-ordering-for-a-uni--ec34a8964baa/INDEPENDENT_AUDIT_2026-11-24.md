# Independent mathematical audit

## correctness

PASS

With fixed endpoints (c,±s,0), the solid-angle formula reduces to 2 atan2(sZ,c+X); using atan2 preserves the branch above area pi. On Z>=0 the angular threshold is the intersection of that hemisphere with n·C>=h for the stated n,h. At the two intersections the inward tangent normals have dot product -cos(a), so the corners are a, not its supplement. The small circle has center hn and radius s/L. Taking the in-plane vectors (s cos(a),0,sin(a))/L and the y-axis as a basis, its upper arc is parametrized by cos(theta)>=-c cos(a), with central span 2 arccos(-c cos(a)). Its signed curvature relative to the cap's inward direction is h/(s/L), giving the stated negative contribution for h<0. Gauss–Bonnet and reflection give the CDF with endpoints 0 and 1. The derivative bracket has value zero at q=-1 and strictly positive derivative 2 sqrt(1-q²) in the interior. Setting a=pi/2 verifies identifiability. At a=beta u, L is asymptotic to beta sqrt(1+u²); the case u=0 is exactly zero. At c=0 the correction vanishes uniformly. The endpoint coefficients follow from the first-order sine terms and arccos values pi-beta and beta, and 1-beta cot(beta)>0. Independent coordinate quadrature at five interior pairs agreed within 3.9e-13, a diagnostic only. The frozen checker was read, not executed.

## originality

FAIL

Finch and Jones §2.1 explicitly give the conditional area CDF for exactly this experiment. The new-looking arccos representation is a direct single trigonometric substitution in their integral; strict stochastic order also follows pointwise in that integral parameter. The identification and limits are elementary specializations or expansions. This is not a denial of the correctness of the alternative geometric proof, and it does not assert that Finch and Jones printed the arccos expression or the refinements verbatim.

## value

FAIL

An explicit distribution and its dependence on one fixed edge are natural questions. But the exact distribution was already given for this experiment, its integral has a standard elementary antiderivative, and strict ordering is already visible from its integrand. The one-threshold identity and the expansions are useful facts to record but are direct consequences of that short evaluation. No independently valuable remainder requiring a substantive new result was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
