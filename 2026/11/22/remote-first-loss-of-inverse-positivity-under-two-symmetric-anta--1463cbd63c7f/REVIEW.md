# Independent mathematical audit

## correctness

PASS

Eliminating the fixed tridiagonal interior gives terminal coupling -1/D_m and diagonal b, including the no-interior case b=3,d=1. Reflection yields even/odd block determinants E=2(b-d)-1-(b-d)t and O=2(b+d)-1-(b+d+4)t. The positive leading diagonal and E>0 up to the first odd zero prove the exact definiteness range; O<=0 thereafter. Reconstructing the terminal inverse from the sum and difference of the two block inverses gives all four stated cofactor numerators. In particular N14(0)=d>0 and N14(d/4)<0, while the other three numerators are positive on [0,d/4]. Vieta puts the second root of N14 beyond 4/(d+2)>=4/3, so the endpoint witness remains negative for the rest of the positive-definite range. The two interior attachment columns are strictly positive even at the first zero; the positive interior Green function propagates strict positivity throughout the remaining full inverse. The continuant formula gives the exponent n-2 and both constants as stated. The classification does not extend beyond the SPD interval. Bounded replay of determinants, cofactors and limit: `python /workspace/branches/frozen_replay.py 4` (SymPy and Decimal); the argument, not the replay, covers arbitrary sizes and real strengths.

## originality

PASS

Best-of-knowledge pass for the specialized closed threshold, isolated unperturbed endpoint pair and exponential separation together, not for Schur reduction, negative-weight definiteness or the general problem of inverse nonnegativity under off-band perturbations. There is positive evidence for a closely related existing decision framework, but not for the claimed analytic classification being supplied by it.

## value

PASS

This is a concrete boundary for using definiteness as a proxy for a nonnegative response in a natural screened path: the first response that changes sign is not an entry supported on either modified edge, and the allowable strength for nonnegative response tends exponentially to zero despite a uniformly positive definiteness threshold. The exact all-size threshold and exclusive witness distinguish two natural stability notions, rather than just giving a numerical small-path example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
