# Independent mathematical audit

## correctness

PASS

Independent check via conditional piecewise bridges rather than the frozen Green-kernel calculation. With gaps a=s, b=t-s, c=1-t and U=B(s), W=B(t), conditional path means are linear interpolants and the integrated conditional variance is a constant. Thus E[Q|U,W] is that constant plus [(a+b)U²+bUW+(b+c)W²]/3. For standardized X,Y, write X=D cos θ, Y=D cos(θ−δ), δ=arccos ρ, with uniform θ and E[D²]=2. Sign disagreement occupies two intervals of length δ; integration there gives Cov(X²,V)=Cov(Y²,V)=sin(2δ)/π and Cov(XY,V)=2 sin δ/π, and m=1−2δ/π. Substitution gives Cov(Q,V)=2ρ sqrt(1−ρ²)t(1−s)/(3π)=2 sqrt(abc)/(3π). Global sign reversal reduces the squared-loss conditional mean to the projection onto 1,V. The prior moments are 1/6 and 1/45 (the latter by Wick and integrating K²), giving exactly the reported decoder and risk. Endpoint, one-sign and coincident designs have no improvement by reflection; the interior improvement tends to zero along the whole boundary since 1−m²≥(2/π)sqrt(1−ρ²). At fixed ρ, b=kac with k=(1−ρ²)/ρ², so maximizing abc means maximizing ac subject to ac≤(1−kac)²/4; the unique largest feasible product has a=c. This verifies the scalar objective on all remaining candidates. Its numerator has logarithmic derivative 2(1−2ρ)/(ρ(1−ρ²)), its denominator decreases strictly, and the objective vanishes at both endpoints. Hence no optimizer has ρ≤1/2, and the fraction at ρ=1/2 is 5/(6π²). No uniqueness or certified numerical maximizing correlation follows or is asserted. The frozen numerical and symbolic verifier was inspected, not executed; the proof above is independent of it.

## originality

PASS

The qualified distinct claim is the bridge-energy decoder and strict global placement theorem for exactly two deterministic zero-threshold signs. The closest inspected same-target record uses full point values; the closest same-information records have different targets. No inspected statement or stronger applicable design theorem gives the sign-only quadratic-energy result.

## value

PASS

A canonical prior and even path functional create a sharp, useful sensing contrast: a single zero-threshold sign is uninformative, while two signs reveal a nonzero, exactly quantifiable fraction of energy variance. The fixed-correlation domination proves strict reflection symmetry for every global placement and rules out trisection, independently of numerics or uniqueness. These conclusions provide a reusable exact benchmark for quantized Gaussian sensing, not just an isolated risk evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
