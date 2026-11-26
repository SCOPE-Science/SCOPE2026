# Independent mathematical audit

## correctness

PASS

Center at A^{-1}b. On coordinate i the i.i.d. update is (y,z) -> (y−βξz,y), ξ Bernoulli(p_i). With h=βp/(1+βp) and c=h+β²p/2, Q=[[1,−h],[−h,c]] is positive definite since c>h>h². Direct expansion of the conditional Q-energy gives drift (β²p/2−h)(y²+z²); the mixed term cancels by βp(1−h)=h. Its sign is exactly that of pβ²+β−2. Comparison of Q with the Euclidean square gives geometric decay, exact conservation, or geometric growth for the state pair. At and above threshold the instantaneous mean square is also bounded below by a positive constant times the preceding pair's mean square: (1−p)y²+p(y−βz)² is positive definite because 0<p<1. Finite summation with fixed positive a_i, decreasing βcrit(p), and nonzero starts supported on a maximizing coordinate give the global frontier. The expansion at p=1/n is correct. Verification notes and rational checker were inspected, not executed; the all-time result is algebraic.

## originality

FAIL

A distinct Resultary result already proves the same sharp criterion and boundary classification for exactly the same stochastic process. The frozen diagonal system's centered update is the identity-system additive stale Kaczmarz update, with α=β and the same sampling and initial pairs. Replacing the Euclidean norm by the norm with fixed positive diagonal weights changes neither the mean-square boundary nor geometric rates. The frozen text gives a different short Lyapunov certificate, not a distinct sampling frontier. No priority inference is needed from catalog dates.

## value

FAIL

A sharp nonuniform-sampling boundary for a stale update would be useful as a new result, but the identity-system theorem already supplies it. Diagonal weighting and rebranding the same process do not create a new stability regime. The alternative positive quadratic certificate is a compact proof, with no separate scientifically needed invariant or new boundary established as the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
