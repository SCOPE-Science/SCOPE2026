# Independent mathematical audit

## correctness

PASS

For a unit index modulo p, division with remainder and invertibility of p² modulo n reduce the gcd to gcd(n,t_r). At n=pm the gcd is m gcd(p,ap^(k−2)m^(k−1)), so the only exception to the zero value on multiples of p is (k,n)=(2,p). CRT lets a unit fiber realize H=1 immediately before a shift into a nonunit fiber if p does not divide the shift, and lets any prime in Q witness failure of a shift not divisible by that prime. After imposing pQ divisibility, a shift of p-adic order one would force equal prime supports on every lift of a given unit mod p (choose n divisible by exactly one prime of Q in a symmetric difference). For p not dividing k, the nonzero binomial slope runs through all representatives u+jp; u and u+p are coprime and the latter is greater than one. For p dividing k the slope vanishes so pQ suffices. All CRT witnesses recur at arbitrarily large n, including for p=2; if Q=1 the same argument applies without auxiliary primes. The isolated exception prevents starting at or before p and averaging each unit fiber by CRT gives the density; one partial period and one exceptional point give a uniform O(P) remainder. Both examples were checked independently against the floor-based predicate across two periods in /workspace/branches/reproduce_decisive.py; the frozen finite parameter sweep was inspected, not executed or used as a general proof.

## originality

PASS

The distinct result is the least eventual period for a prime-square denominator at every exponent k≥2, in particular its exact p-adic loss governed by k. The prime-denominator CRT lemma and the quadratic periodic-plus-spike/density machinery have direct antecedents and are not the originality basis.

## value

PASS

Prime squares are the first denominator where the exponent derivative controls the p-adic part of the true periodicity length. The criterion distinguishes periods that an upper-period or density theorem cannot separate, and the sharp period and onset give the exact finite cycle needed for rational floor coprimality. The quadratic spike and CRT averaging alone are not the contribution supporting this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
