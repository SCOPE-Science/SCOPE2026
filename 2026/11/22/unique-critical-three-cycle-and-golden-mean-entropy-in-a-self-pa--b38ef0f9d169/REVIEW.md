# Independent mathematical audit

## correctness

PASS

With A=37/25+C/4, the first critical image runs from 321/400 to 371/400. The right branch gives the second image (15−8A)(72A+1)/1024, positive and at most 1.98(1−321/400)<1/2, so the third iterate uses the left branch for the entire range. Independent integer polynomial multiplication gave third-iterate-minus-one-half numerator coefficients (−2096927,93600,5522816,−3594240,331776), ascending in A at denominator 4194304, agreeing with the stated factorization. Only the increasing quadratic factor changes sign in the range. Its admissible root gives the stated C and ℓ<h with ℓ<1/2<h, so the least period is three. The endpoints 0,ℓ,1/2,h,1 map to 0,1/2,h,ℓ,0, proving the four transitions by branch monotonicity. Both branch slopes have magnitude at least A>1; cylinders shrink and the expanding Markov entropy formula gives log ρ(M)=log φ, since the other components have radii at most one. On [ℓ,h] the core transition matrix is primitive, so cylinders inside any open subinterval eventually cover both cells for all sufficiently large iterate times. Points above h enter (0,ℓ); a positive point remaining below ℓ would increase to a positive fixed point there, impossible, and when it crosses ℓ it cannot overshoot 1/2. Only the two endpoints fall to 0 without entering the core. The supplied symbolic checker was read, not run; the proof, not a finite orbit sample, supports expansion, mixing and finite absorption.

## originality

PASS

The map is an exact instance of Paul et al.'s published design, and the entropy and mixing mechanism once the critical itinerary is known are standard. The supported distinct contribution is identifying the unique exact control of that family and range with this orbit, and specifying its global interval/core dynamics. The conclusion is bounded by the sources actually read.

## value

PASS

An exactly located postcritically finite parameter in a published numerical design supplies a calibration point where entropy and the basin of a mixing core can be distinguished rigorously from measures based on finite observations. The all-control uniqueness and almost-full interval absorption are substantive parts of the result. No digital, cryptographic or global parameter-curve consequence is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
