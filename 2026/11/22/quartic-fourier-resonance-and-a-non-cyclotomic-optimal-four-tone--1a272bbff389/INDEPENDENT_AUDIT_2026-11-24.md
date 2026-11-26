# Independent mathematical audit

## correctness

PASS

Global phase and argument rotation uniquely set the first two coefficients to 1. For w=V/U, Parseval applied to P_m^4 splits into blocks [mj,mj+4]. In the separated-block Laurent polynomial the phase exponent difference is at most two, and the second harmonic comes only from j=2, exponent offset 2, with coefficient 6²=36. At w=1 the sum of squared binomial coefficients gives 70²=4900. At w=−1 the circle averages of |1+z|^(8−2j)|1−z|^(2j) are 70,10,6,10,70; multiplying by the corresponding squared binomial weights gives 676. These fix the remaining Laurent coefficients and yield 2644+2112 Re(w)+144 Re(w)², strictly increasing in Re(w). At m=4 the four adjacent overlaps add 2 Re(UK(w)), with coefficients 4,24,24,4. For h=|1+w| the absolute value is 4h(h²+3); maximizing or minimizing in U therefore yields the stated two envelopes. The upper envelope increases to 5012. The lower derivative divided by 24 is the strictly increasing cubic 6h³−h²+76h−1, with its root in (0,1/75) and a value strictly below 676 at h=1/76. Equality forces the stated unique U for each of the two w values. The normalized torus is connected, so there are no gaps in the ranges. The primitive cubic is irreducible by the rational-root bound and is not monic, so ρ is not integral; a root of unity w would make ρ²=2+w+w^(-1), hence ρ, integral. Normalizing root-of-unity phases retains root-of-unity phases. Binary phases have minimum 676. Frequency differences in |P_m|^8 are at most 4(m+1), verifying the stated finite-sampling condition.

## originality

PASS

The distinct contribution supported by the comparison is the resonant m=4 lower endpoint, equality cases, and arithmetic obstruction for the adjacent-pair support. Even-moment convolution and the phase ordering in the separated rectangle case are established methods/results; no originality credit is assigned to those ingredients or to phase alignment at the maximum. The closest indexed resonance and phase-frustration results address materially different supports or objectives.

## value

PASS

The adjacent-pair support has a natural first unresolved alias at the eighth moment. What matters is not the small numerical gain over 676: the optimizing relative phase moves off the antiphase point, and no finite root-of-unity alphabet recovers the exact optimum even though binary phases solve the separated case. The exact endpoint and equality conditions identify when this arithmetic distinction first appears for the support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
