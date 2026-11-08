# Scientific review

## Correctness: PASS

Unfolding the ordinal one-point extension definition shows that rank at least three is equivalent to one vertex having both an adjacent and a nonadjacent partner with all four external adjacency profiles. Both full pairs together require three neighbors and three nonneighbors, proving the seven-vertex threshold. In any rank-three witness, the six necessary edges fall in the disjoint categories: three incident with the center, one between its neighbors, one between a neighbor and a nonneighbor, and one between its nonneighbors. At equality, the profile requirements uniquely force the edge list in RESULT.md and all other vertices isolated. A finite witness realizes the bound. Its asymmetric connected six-vertex component gives the labeled count. The universal forcing interval follows by containing this witness and, in the other direction, the disjoint union of all five-vertex graph types. This proof handles every specified size and is not extrapolated from enumeration.

The standalone checker uses an independently defined pair-profile rank test and recursively computes the witness's finite rank; it exhaustively enumerates all 33,867 labeled graphs through six vertices, all seven-vertex graphs with at most six edges, and verifies all 5,040 extremal labeled copies form one orbit. The checker is finite supporting evidence, not an infinite proof.

## Originality: PASS with historical-priority limitations

López-Callejas and Navarro-Castillo (arXiv:2604.14461v1, 2026-04-15), in their full paper on Fraïssé ranks, construct general finite witnesses and explicitly leave the graph cutoff problem open (Question 7.4), stating the earlier interval \(4\le N(3)\le |H_3|\), with \(|H_3|=11\) in the graph case. Their general construction does not yield the sharp seven-vertex rank-three onset, the six-edge minimum, or the classification of all equality graphs. Kubiś and Shelah (2024) give general ordinal rank foundations; their accessible PDF excerpt was insufficient for an exhaustive absence claim, so broader earlier coverage remains a risk. General seven-vertex graph catalogs enumerate graph types but do not by themselves identify this rank-specific extremum. Semantic searches of published research records for this exact rank, cutoff, and parameter aliases did not identify a dominating result; this is evidence of limited inspected coverage, not proof of uniqueness.

## Value: PASS

The precise cutoff \(N(3)\) is posed as a natural numerical invariant in the motivating paper. The result reduces the published gap from \(4\le N(3)\le11\) to \(6\le N(3)\le7\), a motivated finite cutoff improvement. The six-edge extremal classification supplies a sharp rank-three local obstruction with a unique graph shape and an exact labeled census for all orders; it explains the structural reason for the threshold, rather than presenting an arbitrary small-case table.

## Limits and risks

The remaining \(N(3)=6\) versus \(7\) question is not resolved. The six-edge uniqueness does not classify rank-three graphs with more edges. Broader earlier graph-rank literature could contain an equivalent characterization. The 2024 PDF was only partially reviewed. No independent historical-priority verification or mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
