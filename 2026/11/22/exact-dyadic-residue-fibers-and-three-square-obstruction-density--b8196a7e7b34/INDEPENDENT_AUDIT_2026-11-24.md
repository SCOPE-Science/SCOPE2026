# Independent mathematical audit

## correctness

PASS

The generating product over the two distinguishable colors satisfies B(x)=(1−x)^(-2)B(x²). For each section, the B(x²) factor passes through as B(x); the indicated Vandermonde transformation computes coefficients of the remaining multiplier exactly. I independently rebuilt the full state space using rational multipliers P(x)/(1−x)^d rather than Newton coefficients: the next numerator is the even/odd section of P(x)(1+x)^(d+2), with denominator (1−x)^(d+2). The reproduced graph has 100 states; its histograms at depths 11 and 12 are (66,62,65,67,63,64,62,62) and (130,126,129,131,127,128,126,126), and all 800 consecutive recurrence residuals vanish in dimension 100. Taking predecessor closures of both labels gives 37 unstable states; exactly ten paths reach unstable states at depth seven and the next 100 differences vanish. Cayley–Hamilton applied to the integer transition matrix extends both identities to all later depths. The ten paths bound the change under any higher digits; together with the −2 offset they give error at most 12 per aligned dyadic block of length ≥2^11. Binary decomposition gives ordinary discrepancy O(1+log X), including real cutoffs by rounding. Positive values 112 mod 128 are 4²(8u+7), so the full obstruction lower density is at least 1/32, not necessarily exactly 1/32.

## originality

PASS

The exact eight dyadic histogram cells and the ordinary 112-fiber logarithmic discrepancy are distinct from prior automaticity, scalar valuations, and even the earlier two-color obstruction progressions. The claim is not new for automaticity or for the existence of a positive-density obstructed subset.

## value

PASS

This is a motivated modulus and fiber: a single congruence yields a three-square obstruction and directly improves the earlier bound from 1/64 to 1/32. The stabilization and bounded number of suffixes sensitive to high digits give a quantitative all-prefix answer rather than just a dyadic-limit census. The simultaneous eight-cell histogram gives further usable residue information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
