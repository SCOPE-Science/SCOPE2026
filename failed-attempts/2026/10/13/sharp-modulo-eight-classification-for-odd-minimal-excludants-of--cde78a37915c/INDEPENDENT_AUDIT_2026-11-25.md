# Independent mathematical audit

## correctness

PASS

Independently, prescribed mex k has forced factors 2q^m/(1-q^m) for m<k, no factor for the absent k, and optional factors (1+q^m)/(1-q^m) for m>k. This gives the stated exact series for odd k=2j+1. Modulo 8, j>=2 vanish and j=1 reduces to 4q^3/((1-q)(1-q^2)); its coefficient is floor((n-1)/2) after removing the factor 4, including n=1,2. For j=0, Jacobi gives (1+2A)/(1+2S), where A=-q/(1+q) and S=sum_{k>=1}(-1)^k q^(k^2). The inverse gives 1+2(A-S)+4(S^2-AS) modulo 8. In characteristic two the quadratic term S^2 counts twice-squares, while AS counts positive k^2<n. At n=k^2 the signed terms cancel, n is not twice a square, and k-1 plus floor((k^2-1)/2) is even for both parities of k. Nonsquares therefore give exactly one of 2,6. By independent direct enumeration of ordinary partitions, weighting each by 2^(number of distinct sizes) times its odd-filtered mex, I obtain F(36)=852984, with remainders 56 mod 64 and 8 mod 16; the check also matches the mod-8 formula for n=1..40. The formal power series proof, not the finite check, gives the all-index classification.

## originality

FAIL

The main claim is demonstrably covered by distinct indexed Resultary record bee256e63339: definition, all-index mod-8 expression, and its complete square-zero classification coincide after renaming, and that record also counts residue classes. Same-day dates do not establish order or priority and the decision makes no such inference. The only substantive difference in the frozen Finding is the single mod-16 witness, obtainable by finite coefficient extraction from the already published exact series. It does not turn the covered all-index classification into a distinct finding.

## value

FAIL

An exact mod-8 classification of this natural statistic would be worthwhile, but the indexed theorem already answers it. The remaining F(36) check illustrates sharpness and is mathematically correct; on its own it is a routine coefficient calculation from the available series, not a new congruence classification or a substantive surviving theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
