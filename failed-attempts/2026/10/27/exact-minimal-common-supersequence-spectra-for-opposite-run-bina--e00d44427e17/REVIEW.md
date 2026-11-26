# Independent mathematical audit

## correctness

PASS

For any two embeddings, intersecting zero sets force disjoint one sets. Thus a common supersequence needs at least 2m copies of one letter. In a minimal word every pair of embeddings covers all positions, giving at most 2m of each. If both counts were 2m, the embeddings starting with the first m copies of their respective initial letters and continuing greedily would share the later of the two m-th positions, leaving an unused position. For a zero-rich word with m+j ones, split the ones into x,y,z around the m-th and (m+1)-st zero. Embeddability is y+z>=m and x+y>=m. When j>0, an empty flank would permit deletion of a one from the other flank or the center; with both flanks present, deleting a one on either side must violate the corresponding inequality, so both are tight. The j=0 case also forces tightness. Conversely, tightness makes every one essential, and deleting a zero violates the required 2m count. The separating zero positions make the factorization unique, and the two orientations are disjoint. The length and binomial-square formulas follow, including m=1; the backward ratios are at most 1/4 and tend to 1/4 at each fixed distance from the top, giving the 4/3 multiplier by geometric domination, then Stirling gives the total and longest-length fraction. Inspected frozen RESULT.md, VERIFICATION.md and check_minimal.cxx; the recorded exhaustive range m=1..5 is supplementary, not replayed or necessary for the proof.

## originality

FAIL

The distinct earlier Resultary record 10a0d52c68a3 states the same deletion-minimal word classification, admissible lengths and exact counts for the same pair, as well as the same total asymptotic. The limiting maximum-length fraction is an immediate ratio of the already stated extreme count and total asymptotic. This is established coverage, not merely a possible overlap with general enumeration algorithms.

## value

FAIL

A length-refined classification of deletion-minimal rather than shortest supersequences is a useful exact result in principle. Here the classification and spectrum are already available for this very family, and the stated longest-length fraction adds no independent invariant beyond dividing known quantities. There is no surviving distinct contribution under the narrow-exact-result standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
