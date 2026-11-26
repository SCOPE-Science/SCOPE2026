# Independent mathematical audit

## correctness

PASS

For one component and the minimal half-spin class, strict-partition Bruhat cells give Euler characteristic 2^n. Independently, the Weyl dimension polynomial for the half-spin highest weight times k has nontrivial degree factors only for positive roots e_i+e_j. The Weyl-vector coordinates run from n to 0, so the Hilbert leading coefficient is the reciprocal of ∏_(0≤i<j≤n)(i+j). Multiplication by M! gives the degree; grouping by j yields the proposed factorial expression. The legal-corner recurrence for shifted staircase tableaux gives the same counts. My separate exact Weyl-product replay (/workspace/independent_checks.py, spinor) obtained 1, 1, 2, 12, 286, 33592 for the first six degrees. Cancelling adjacent products gives the stated binomial ratio and the product of (2n+1+s)/(n+s) for s=1,…,n(n−1)/2. This is 1 at n=1, 2 at n=2, and greater than 2 for n≥3. The normalized comparison therefore drops once, is flat from n=2 to 3, and then increases, with the unique threshold between 12/16 and 286/32. Finite replay checks arithmetic, not the infinite conclusion.

## originality

FAIL

The two exact invariant formulas are already supplied by the classical Schubert and shifted-tableau results on this very family. The threshold and adjacent ratio are direct consequences of those explicit results, not just outputs obtainable in principle from an unrelated general method. No independent exact-wording duplicate is needed: the known degree product gives the ratio by cancellation, whose first factor is 2 and whose remaining factors are strictly greater than 1; the known n=4,5 formulas then decide all ranks.

## value

FAIL

The comparison is natural, but this particular cutoff and its normalized growth require no additional structural result beyond the established exact formulas and elementary product cancellation. The record does not add a nonroutine comparison tool, a geometric relationship between the counts, or a separate valuable remainder. A repackaged proof or extra finite certification would not address that limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
