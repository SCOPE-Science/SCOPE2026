# Independent mathematical audit

## correctness

PASS

Identify SU(2) with unit quaternions and take two independent Haar-uniform conjugacy-class samples. Their scalar convolution is exactly uniform on [a,1] with a=cos(2theta), L=1-a; the Haar scalar density is (2/pi)sqrt(1-t²). Radial conditional angular measures agree, so the full-group TV is the one-dimensional half-L1 distance. On L<=pi/2, F=H(a); otherwise F=H(a)+2/pi asin(b)-b/L with b=sqrt[1-pi²/(4L²)]. The interval [a,1] fully covers (-b,b) since L³(2-L)<=27/16<pi²/4. Differentiation gives the sign of 4L^7(2-L)-4pi²L²+pi⁴; its derivative is negative on [pi/2,2], and endpoints have opposite signs. Unique root gives the only minimizing scalar a and two supplementary theta; at theta=0,pi TV=1. Independent root and integration corroborate TV~0.102530046. The proof, not the sample grid, establishes global uniqueness.

## originality

PASS

Bounded PASS: the two-step SU(2) conjugacy-class TV minimization is a different objective from one-step mean-zero L² class-walk tuning and from hemispherical absolutely continuous walks. Relevant primary sphere geodesic-walk theorems do not state the SU2 two-step L1 optimizer.

## value

PASS

At one step every conjugacy-class law is singular to Haar (TV=1), so horizon two is the first nontrivial exact TV optimization. The result gives an exact globally unique optimal parameter and distinguishes TV from equatorial and spectral L² tunings. Natural finite-time Markov-mixing problem, not arbitrary optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
