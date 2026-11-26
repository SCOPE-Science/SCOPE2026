# Independent mathematical audit

## correctness

PASS

Equality of the standardized outputs is exactly preservation of name-equality under a one-step shift inside the interval and preservation of each outside-name indicator. If the earliest repetition ends at t and has gap d, the shift equivalence propagates that equality backward to the beginning and forward to the end. The first d names are distinct by the choice of t; with no repetition use d=ell. Any outside occurrence of an internal name forces its indicator to be constant one across the interval, excluding outside occurrences precisely in the nonconstant case. Conversely the constant and isolated periodic patterns preserve all tested equalities. Contracting the constant interval or independently partitioning the exterior of the unique residue-class pattern gives the Stirling counts, including ell=n and zero remaining blocks. Summing in k and weighting by n-ell+1 gives the Bell and total counts. Maximal constant runs already coalesce; each further loss of a run output can be charged to a distinct between-run collision. Contracting an adjacent pair gives the mean of A_n, and averaging the between-run bound gives the two claimed inequalities. The Bell ratio bound can also be recovered from log-convexity of the Poisson(1) moments B_m, which gives B_m/B_{m-1} >= B_m^(1/m); the single Dobinski term k=floor(m/log m) with k! <= k^k gives B_m^(1/m) bounded below by a constant times m/log m. Ratios with indices >= n/2 then control the weighted geometric sum starting at ell=2 and give a superpolynomial tail. The all-length proof is sufficient; the frozen finite checker and recorded counts are supporting material, not a fresh run or formal attestation.

## originality

PASS

Within the inspected literature and catalogue, no result covers the same-source two-site equality criterion and its block/distance census and exceptional-collision bound. The closest same-day records address different deletion operations or different invariants; their date gives no priority information.

## value

PASS

The result identifies an additional mechanism genuinely caused by forgetting block labels, with exact separation by deletion distance and number of blocks. It also quantifies why these exceptions rarely reduce the number of distinct deletion reads in a uniform random partition. The criterion and frequency estimate are useful when modeling deletion balls without mistaking within-source equal outputs for inter-source code confusability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
