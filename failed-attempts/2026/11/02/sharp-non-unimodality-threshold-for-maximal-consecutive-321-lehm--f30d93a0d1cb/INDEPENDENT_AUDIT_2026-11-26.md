# Independent mathematical audit

## correctness

PASS

Consecutive descents in a permutation are exactly strict descents of adjacent Lehmer coordinates. Writing the defects e_i=n-i-p_i, avoidance requires the positions with e_i>e_{i+1} to cover every edge of the path on the n−1 comparison positions. For a given cover S the smallest admissible defects are the lengths of successive runs in S starting at i (zero off S); their positive support is exactly S. Therefore minimal defects correspond precisely to inclusion-minimal covers. The omitted positions are independent and dominating, so their first and last gaps to the ends yield blocks of lengths 1 or 2 and the interior gaps yield lengths 2 or 3. A block of length b contributes binomial(b,2), giving the stated rational generating function including n=2. Coefficients from the block counts give the odd valley (m−1,m−2,(m−2)(m−3)) for m≥5; the even valley has first two entries binomial(m−2,2)>binomial(m−3,2) and last-to-middle ratio 2(m−5)/3>1 for m≥7. The recurrence verifies the remaining small strings, including the n=12 recovery. Reversal preserves unimodality. The independent exact replay `python /workspace/branches/independent_reproduction.py 5` matched direct permutation/Pareto histograms at n=2..8 and recurrence shape at n=2..160; the analytically proved valleys, not the finite test, give exhaustion. The frozen verification notes and code are finite diagnostics and were inspected without execution.

## originality

FAIL

A distinct earlier indexed result contains the identical generating function and sharp all-length classification (including the same exceptional recovery), with the same parity-valley proof and exceptional coefficient strings. It is not merely a search hit on a similar title or an inference from the date. No distinct additional result is stated in this record.

## value

PASS

As a mathematical result the sharp shape boundary is substantive: it concerns the natural inversion grading, identifies a genuine transient recovery, and proves persistent valleys rather than extrapolating a table. This does not confer value as a new contribution over the matching result; that lack of increment is decisive under originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
