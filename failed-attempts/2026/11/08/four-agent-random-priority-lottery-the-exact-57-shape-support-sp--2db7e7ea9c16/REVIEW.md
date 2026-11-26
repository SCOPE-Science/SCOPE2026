# Independent mathematical audit

## correctness

PASS

Independently counted priority multiplicities by testing every candidate matching rather than simulating priority orders. For an agent receiving object x, every object she prefers to x must have been consumed by its assigned owner first. Thus the orders realizing a matching are exactly the linear extensions of its predecessor constraints; subset DP counts them, giving zero for a cycle. Relabeling objects uniquely normalizes the first agent to the identity ranking and gives weight 24 for each of the remaining 24^3 profiles. All counts are exact, and multiplicities sum to 24 per profile. All 57 shape-frequency rows and 16 support-frequency rows match the two frozen CSVs, as do the impossible sizes, unique normalized full-support profile, mean and tail probability. Replay: python3 /workspace/review_evidence/priority.py.

## originality

FAIL

The earlier indexed Resultary record 5de01f4eeb3e explicitly classifies the same complete-matching lottery on the same labeled profile space. Its 57 signatures and counts are identical row for row after sorting multiplicities in the same direction. It gives the entire support histogram, forbidden sizes, identical-profile full-support criterion and the same mean; it additionally gives the variance and characterizes support size one. The tail probability follows by summing four tabulated cells. This is demonstrated equivalent coverage, not a priority inference from a title or a similarity score.

## value

FAIL

The original small-market census is a useful exact benchmark for lottery concentration, as opposed to a marginal assignment matrix. In this submission it is a recount of the known complete distribution; the exact tail is elementary aggregation of known cells. Independent corroboration is valuable as checking, but it does not establish a surviving new mathematical result under the audit standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
