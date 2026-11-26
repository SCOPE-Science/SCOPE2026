# Independent mathematical audit

## correctness

PASS

RESULT.md lines 36–67 give the correct analytic coefficient. The KKT multipliers on an active contiguous block are weighted prefix residual sums, positive for data strictly decreasing inside the block; separate block means yield strictly slack interblock constraints, so any contiguous averaging partition occurs locally on an open cell. A step across edge i yields either the unchanged step (different blocks) or a single fractional block average (same block), with mass fraction (Q_q-Q_i)/(Q_q-Q_p) on block [p+1,q]. Weighted variation of this response is exactly the chord ordinate at Q_i, including boundary pooling when a nonexistent edge has weight zero. Steps span the quotient by constants isometrically as a weighted l1 basis. Thus the maximum piece norm is the chord/weight maximum, and each chord is witnessed in a strict cell. Continuity and segment subdivision (or approximation by generic segments) globalize. The maximum chord ordinate is the upper convex hull of the plotted points, for which fixed-abscissa extrema have at most two endpoints; adjacent nonincreasing slopes are equivalent to equality with the majorant. At n=4, a_i=1 and w=(1,epsilon,1), the middle majorant ordinate is 1, so the coefficient diverges as epsilon tends to zero. Independent replay `python3 -I /workspace/review-work/replay.py 3` constructed hulls by a monotone stack and used max-min interval formulas, not the supplied PAVA checker, confirming 160 exact attaining pairs and 2,400 exact pair inequalities. Frozen verification code inspected, not executed; finite replay is not the proof.

## originality

FAIL

Strong positive indexed coverage, not a failed literature lookup: the earlier 2026/11/17 Resultary c4a7412f8310 statement gives the same finite weighted least-squares isotonic problem, same two-input weighted edge-variation ratio of the least concave majorant in cumulative mass coordinates, same slope criterion, and an attained constant. A distinct same-day record also gives the exact quotient. Endpoint chord notation, the four-site example, and the local form of attainment do not supply a distinct scientific remainder. The indexed evidence establishes statement-level coverage; the full mirror texts were not available and no conclusion about priority among same-day records is inferred.

## value

FAIL

The invariant itself is natural and useful, but this frozen record recomputes the earlier exact attained invariant for the same operator and gives no additional motivated classification or independent structural claim. The endpoint notation and a four-site specialization aid exposition rather than constituting a valuable separate finding under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
