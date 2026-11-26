# Independent mathematical audit

## correctness

PASS

Two independent positive-count events give the stated product. For y=bx, u=A/b, v=C/b, log F is a sum of g(log u+log y−y) and g(log v+log y), where g(s)=log(1−exp(−exp(s))) and g′(s)=R(exp(s)), R(t)=t/(exp(t)−1). R′<0 on t>0; g is increasing and strictly concave, and both inner functions have second derivative −1/y². Log F tends to −infinity at both endpoints; hence its unique maximizer is interior and the derivative determines the side of any proposed cutoff. The scaled derivative is (1−y)R(uye^(−y))+R(vy), positive at y=1, and at y=2 has the sign of ue^(−2)−v, including exact equality. This also proves the stated finite-input constraint rule. For large u at fixed v, positivity of the derivative at each fixed y>1 eventually forces y*→infinity. The stationary equation gives Q>V once y*>2, for Q=uy*e^(−y*) and V=vy*. Taking logs gives 0<Q/V−1≤log(y*−1)/(V−1) eventually; thus y*=log(u/v)+o(1). For a bounded independent replay, solve that derivative equation on [1,3] for (u,v)=(10,0.5),(10,1),(10,2),(10,10e^(−2)); multiprecision evaluation gave y*≈2.557476620, 2.191227443, 1.737010222, and exactly 2 by the identity. These are illustrative; the parameter-wide result is analytical. The supplied checker was inspected, not executed.

## originality

PASS

The nontrivial comparison is a single shared scalar input maximizing detection of BOTH targets, with exact crossover, equality, and fixed-v asymptotic in the asymmetric Poisson model. Neither the inspected published optimization claims nor the readable primary survey model covers this theorem. This is a best-of-knowledge finding; no historical priority claim is certified.

## value

PASS

A researcher optimizing joint confirmation rather than one-target detection needs to know how far the single-target optimum can miss. At twice that optimum the opposing logarithmic mean slopes balance, so the sharp threshold is decided exactly by equality of the two means there, not by a conventional dose chosen from a discrete grid. The unbounded logarithmic displacement in the fixed-b,C regime shows this is not uniformly a small correction. This is a structural benchmark under independence and an idealized attenuation curve, not empirical calibration or a laboratory recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
