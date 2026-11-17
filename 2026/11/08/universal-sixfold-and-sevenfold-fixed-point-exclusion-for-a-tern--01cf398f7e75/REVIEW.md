# Independent mathematical audit

## correctness

PASS

Invertibility extends every T^(mk)-fixed state to an mk-periodic word satisfying x_n=x_{n-k}+1[x_{n-1}!=0]. Organize m cyclic rows and k columns: each column difference Dy equals the prior column support mask, rotated at wrap, so telescoping forces binary mask weight divisible by 3. For m=6,7 enumerate all admissible binary masks up to cyclic rotation and all three lifts y_t=a+sum_{i<=t}b_i mod3; retain successor masks also of weight multiple 3. Independently implemented the full quotient mask graphs (6 vertices at m6 and 7 at m7) and verified all nonzero vertices are acyclic, with only zero-loop closed walk. Cyclic rotation at wrap preserves reachability. Hence every mk-periodic word is zero uniformly for all k, not inferred from finite k checks. Direct enumerations k=2..9 also each give one fixed state at both multipliers; T_2 has an 8-cycle at the known endpoint.

## originality

PASS

Best-of-knowledge original final claim after direct statement/implication comparison; earlier general frameworks, alternative rules or smaller families are credited, with access and historical priority risks explicitly retained.

## value

PASS

Uniform spectral gaps for a natural and independently studied finite-field quadratic permutation are useful exact period-structure data, with a short finite symbolic obstruction valid for arbitrary memory length. Together with the known 5k gap and 4k cycle count, 6k and 7k fill the next two natural multipliers, not an arbitrary unmotivated slice of experimental lags.

The dated certificate retains the supplied scientific assessment, sources and limitations.
