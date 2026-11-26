# Independent mathematical audit

## correctness

PASS

Contract the prescribed ordered k-edge path to a vertex of weight k+1, with unit weights elsewhere. Weighted Prüfer enumeration gives (k+1)n^(n−k−2) completions, with each incident edge on the contracted vertex specifying its own attachment choice. Excluding a given path endpoint from all attachments replaces the weight and total weight by k and n−1, respectively. An off-path unit-weight vertex is a leaf iff absent from the contracted Prüfer code, yielding probability r_n^(n−k−2). Internal vertices cannot be leaves; the full spanning path case separately has two leaves, agreeing with the formula. Summing gives F_n(k); the Prüfer unconditional mean matches F_n(1). The sign of the exact difference is the sign of 2(n−1)−k(k+1)^2=2(n−N_k). N_1=3<n and N_(n−2)>n, so there is precisely the proposed peak or adjacent tie, and solving the cubic to bounded error gives the stated n^(1/3) scale. The distance tail is the product of (1−j/n) for j=2,...,k+1 from telescoping the path count, hence typical distances are of order sqrt(n). Uniformly for k=O(sqrt(n)), expanding r_n^(−k) to second order in 1/n in the exact centered mean yields e^(−1)[1−2/(k+1)−k²/(2n)+O((k+1)/n+(k³+1)/n²)]. Substitution at the maximum gives the −3·2^(−1/3) coefficient; substitution at k/sqrt(n)→x gives the claimed limit.

## originality

FAIL

Direct prior coverage. Two earlier Resultary records have the same exact total-leaf conditional mean and forward difference, all maximizing distances including the ties, the cubic-root peak scale and leading uplift. Earlier exact formulas also determine both highlighted additional asymptotics by routine uniform expansion. The relationship-to-prior-work account misses the earlier total-leaf results; the issue is not an inaccessible source or the same-day priority ambiguity.

## value

FAIL

The exact regression, exceptional peaks and separation of the maximizing and typical scales form a meaningful mathematical observation, but the central discovery is already available. The residual sharpened coefficient and limiting sign description are routine Taylor consequences of an already exact formula, not a distinct useful finite crossing, conditional law or structural theorem. There is no worthwhile supported remainder that can justify a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
