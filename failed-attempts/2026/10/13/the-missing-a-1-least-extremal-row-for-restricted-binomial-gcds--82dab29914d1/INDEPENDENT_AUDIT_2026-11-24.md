# Independent mathematical audit

## correctness

PASS

Legendre's formula independently proves the coefficient values: for q<p and k=(p+1)d, the p-floor contributions for N, k, N-k are q, d, q-d, and all p^j floors for j>=2 vanish. At q=p the p-floor contributions are p+1, d, p-d, giving a difference of 1, and the p^2 floors are 1, 0, 0, giving another 1. All higher floors vanish. Thus every selected value at the target is 2, no earlier admissible row reaches 2, and p=2 has no earlier admissible multiplier (the row is 6, with coefficient 20). The gcd takes the minimum and r_p(p+1)=2 for all primes. The frozen Kummer proof gives the same result. A separate Legendre-based finite replay /tmp/opencode/frozen_independent_checks.py 3 checked 60,556 selected coefficients for primes through 113; it is supplementary, not the universal proof.

## originality

FAIL

The central least-row claim and the full claimed gcd profile are immediate specializations of the prior minus-one theorem. A separate earlier-day indexed result states the same least-row result for odd primes and acknowledges the known p=2 case. A distinct same-day result also covers every target-row coefficient via its exact multiplicity. The explicit exclusion in the October a>=2 theorem is not a literature gap at a=1.

## value

FAIL

An unknown least extremal boundary would be worthwhile, but here the result simply reads off the cases of a known general classification. The target coefficient statement is also covered by an exact multiplicity result, and the remaining smaller-row all-coefficient statement is a routine two-column no-carry observation. The short independent proof is useful exposition but leaves no distinct substantive boundary result to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
