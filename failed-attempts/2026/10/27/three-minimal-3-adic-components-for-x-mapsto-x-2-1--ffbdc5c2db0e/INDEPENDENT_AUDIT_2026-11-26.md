# Independent mathematical audit

## correctness

PASS

The mod-3 transitions are 0→1→2→2 and f is an isometry on the class 2, by f(x)-f(y)=(x-y)(x+y). Direct squaring modulo 27 gives exactly the three listed cycles. A finite arithmetic replay of the key valuation avoids large polynomials: with g=f³, the mod-81 trajectories of 2, 8, 17 are 2→5→26→29, 8→65→14→35, and 17→47→23→44. In each case g(x)-x≡27 mod 81. At any other phase of the same cycle the congruence persists because g commutes with f and f'(x)≡1 mod 3 in B. It persists throughout each mod-27 ball by g'(x)≡1 mod 3. For any return map H with δ=H(x)-x of valuation n≥2 and d=H'(x)≡1 mod 3, H³(x)-x≡(1+d+d²)δ modulo 3^(2n). Since 1+d+d²≡3 mod 9 and 2n≥n+2, the new valuation is n+1. The first lift and each further lift therefore join all three classes, giving cycle length 3^(n-2) on each component for n≥3 and the common 3-cycle modulo 9. Coherent cycle labellings give translation by one on the inverse limit of the cyclic 3-power quotients, hence the adding-machine conjugacy and minimality. The three clopen sets exhaust B, so the entry bound gives unique basins throughout Z_3 and rules out periodic points outside as well as inside B.

## originality

FAIL

The exact residue list was not located as a published statement. Nevertheless the entire finding is a mechanical specialization of the published cycle-growth criterion, not just an application of an abstract existence theorem after new dynamical analysis. The only input beyond the existing criterion is the elementary finite cycle table at moduli 3, 9, 27 and 81 and the derivative mod 3. The direct computation and implication are given below; this verdict is not based on unavailable sources or on the quadratic classification over the wrong prime.

## value

FAIL

This is a correct illustration of the small-prime split-before-growth behavior, but for this one map the reported datum is exactly what the standard cycle-growth test reads from three return computations modulo 81 and the mod-3 entry table. The record supplies neither a new boundary for the test nor a separate invariant, parameter phenomenon, or need for these precise residue representatives beyond illustrating the established criterion. As a standalone research result it does not establish value beyond a worked example of an existing method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
