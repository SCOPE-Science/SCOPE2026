# Independent mathematical audit

## correctness

PASS

Orthogonal monomials give K(t)=1+t/a+t²/[ab(1-t)]=(1-At-Bt²)/(1-t). The reciprocal series has c1=1/a, c2=(a-b)/(a²b), and c_n=A c_(n-1)+B c_(n-2) from n=3. Complete Pick requires nonvanishing (a kernel zero between two disc points would make the scalar values 1 and 0 pass the two-point Pick test, impossible for a contractive analytic multiplier by the maximum principle). Thus negative Taylor coefficients rule it out. The c2 and c3 tests exclude b>a and a<1, and leave only b=1 when a=1. If 1≤b≤a, the recurrence is nonnegative and both root moduli are below one: the positive root is below one by 1-A-B=1/(ab)>0 and dominates the other in modulus. If a>1 and b<1, the discriminant is [b(a+1)²-4a]/(a²b). When it is nonnegative, both roots are between zero and A<1, and c2/c1=A+a(-B)>A ensures nonnegative coefficients by the divided difference of the root powers, with a nonnegative derivative in the double-root case. In both cases the series is analytic on the disc and |F(t)|≤F(|t|)=1-1/K(|t|)<1, giving the normalized complete Pick criterion. Below the threshold, the roots q exp(±i theta) give coefficients proportional to sin((n-1)theta+phi), with positive amplitude and phi,theta in (0,pi/2). Crossing pi strictly gives the stated floor index even when a coefficient vanishes at phase pi, since the next phase is below 3pi/2. Using sin(theta)=sqrt(-Delta)/(2q), q→(a-1)/(2a), and phi=O(theta) from the phase numerator's positive limit gives the claimed scaled delay constant. The line defining u and the subsequent reference to nu are a local notation typo: the displayed expression is the unique sine weight fixed by c1 and c2, used consistently in this check. The frozen script was inspected, not executed; finite coefficient tests cannot replace the proof.

## originality

PASS

The b≥1 admissible slice, reciprocal-kernel test and generic recurrence tools are known; the supported distinct result is the full sharp boundary including b<1 and the exact first-failure law with its critical constant. No exhaustive priority is asserted.

## value

PASS

Two altered initial weights on the Hardy shift form a natural test of the gap between shift concavity and complete Pick. The sharp nonexpansive window is not determined by the known sufficient tests. The exact delay establishes that no fixed finite list of reciprocal coefficient signs can recognize the property even for this two-parameter family, and quantifies the divergence in the natural distance to the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
