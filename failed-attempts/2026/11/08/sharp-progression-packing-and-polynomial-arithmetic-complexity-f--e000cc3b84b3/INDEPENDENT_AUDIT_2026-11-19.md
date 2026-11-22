# Independent mathematical audit

## correctness

PASS

For r>=2 sampled powers b^{e0}<...<b^{e_{r-1}}, the integer AP step divides b^{e0}(b^g-1), where g=gcd(e_i-e0). Thus index span >=(b^E-1)/(b^g-1)=sum_{t=0}^{E/g-1} b^{gt}>=sum_{t=0}^{r-2}b^t. Equalities r>=3 force g=1, consecutive exponents, first/last one at endpoints and maximal step, proving H, minimum length and rigidity. For three or more ones g is a proper divisor of E, so n-1>=b^{E-g} and g<=E/2 imply E<=2 floor(log_b(n-1)); the first two one indices and their exponent gap determine the entire sampled binary factor by the explicit rational formula, yielding the reported O_b(n^2 log n) counting bound. Boundary r=1,2, a=0 and composite bases are covered. Independently tested 2,352 exponent sets (126 minimizers) in bases 2..8 and 843,360 AP windows in bases 2,3,4,6 for lengths 1..12; finite checks do not prove infinite quantifiers.

## originality

FAIL

Decisive prior coverage from the 2026-11-02 pure-power arithmetic-progression theorem: the characteristic word c_b(t)=1_{t+1=b^e} and this record w_b(t)=1_{t=b^e} satisfy w_b(a+jd)=c_b(a-1+jd) for all a>=1. Thus earlier maximal occupancy and rigid critical witnesses transfer verbatim. The omitted boundary a=0 yields at most n additional length-n factors: if d divides some b^e, let e0 be least such exponent and j0=b^{e0}/d; its marked sample indices are exactly j0*b^k for k>=0, so the factor is determined by j0 in {1,...,n-1} or is all zero. Therefore P_w(n)<=P_c(n)+n=O_b(n^2), strictly stronger than the submitted O_b(n^2 log(n+1)). This mathematical implication was independently reconstructed from both full RESULT texts; the submitted work has no surviving non-implied theorem.

## value

FAIL

The fixed-base power-marker word and arithmetic-sampling factor language are mathematically natural, but this submitted exact occupancy, unique critical patterns and O(n^2 log n) bound are already established or strictly sharpened by the earlier 2026-11-02 all-base theorem after an elementary one-index shift plus <=n boundary words. The submitted work does not solve exact P_b(n), improve the quadratic bound, or supply an independently motivated new lemma. Independent verification and a second derivation are not a distinct mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
