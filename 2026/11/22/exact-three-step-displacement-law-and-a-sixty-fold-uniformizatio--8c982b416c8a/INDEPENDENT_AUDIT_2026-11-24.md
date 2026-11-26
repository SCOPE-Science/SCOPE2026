# Independent mathematical audit

## correctness

PASS

Conditional on Y0, X1 is Haar, so the full tent pushes X1 to Haar and Y1 and f(Y1) are conditionally Haar. This proves the second displacement uniform; the first is just f(Y0) modulo 1. For the third lag I used the uniform (X1,Y0) chart and D=f(Y0)+f(Y1)+f(Y2), eliminating the unused last vertical shear. The independent standard-library replay /workspace/record2_replay.py clips 80 rational polygons and fans them into 128 positive-area triangles, of total area 1. The projection of a triangle by an affine map whose ordered vertex values are a≤b≤c has two linear density pieces of peak height 2(area)/(c−a) by similar triangles, with tied values handled by endpoint jumps or an atom. The exact wrapped projection has no atoms and all density jumps cancel; the remaining twelve slope jumps match every stated d_r. A continuous periodic spline is determined by those jumps and unit mass; the stated Bernoulli formula has these properties. Its knot evaluations give the stated unique minimum knot and two maximum knots, and strict positivity. In the spectral numerator the two fifth-turn groups have opposite coefficients and contribute a nonzero irrational part when 5 does not divide k; for k=5j the rational numerator has period 12 in j and is zero only at j=0 mod 12. The first numerator is −646/11025−(250/441)√5; division by −4π²k² gives the stated first harmonic. Fourier uniqueness then proves Haar pushforward exactly for integer multipliers divisible by 60. A separate exact computation in the original chart also recovered 8, 56, 320 cells with unit area throughout and the same coefficients. Frozen checker inspected, not executed. The zero frequency is 1, not zero; this is a marginal under stationary Haar, not a claim about joint independence or longer lags.

## originality

PASS

The audited identity was retrieved in the index and excluded as the same record. The strongest distinct same-map results give conditional parabolic residence areas or asymptotic correlation estimates. The short-time Fourier result that is closest in question uses a different map. None of these supplies the exact third-lag law or cancellation set. The finding does not claim the map, generic polygon integration, or a new mixing theorem.

## value

PASS

The diagonal Haar transport observable is natural for the canonical symmetric map at the loss of exponential mixing. Locating the first nonuniform lag and giving its full law and exact smallest arithmetic uniformizer supplies a useful benchmark for finite-time transport and harmonic cancellation, not merely a sampled harmonic or a general-purpose mixing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
