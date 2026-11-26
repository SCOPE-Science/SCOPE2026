# Independent mathematical audit

## correctness

PASS

In dimension three a simplex of the double has at most two pair-vertices, because their disjoint union must have at most four vertices. The opposite-pair adjacency identifies its tetrahedron uniquely. Stellar subdivision retains all six facet pairs, removes their three opposite-pair adjacencies, and adds four graph vertices wx. Each old pair yz is now adjacent within the replacement to the two wx for x outside yz, giving exactly the subdivision of K4 under complement relabeling. This connected gadget reroutes every path using a deleted edge, so no old component splits; exactly the k components touching those six vertices merge. The three old disjoint edges bound k by three. The change in E−V+c is 9−4+1−k=6−k; graph homology is free. The four-simplex boundary has double KG(5,2), connected with 10 vertices and 15 edges, hence circle rank six. Successive stackings preserve connectivity and increase rank by five, giving 5n−19. All quantifiers hold without orientability or manifold assumptions for the local part. Independent replay: python3 /workspace/branches/independent_double.py 9, output /workspace/branches/independent_double_5_9.txt; pair-union enumeration and union-find confirm 1, 5, 40, 440 and 6160 stacked facet sets on 5–9 vertices and the graph changes at k=1,2,3. In particular the facets 0123,0145,0245 realize k=2 at 0123, not sampled in the frozen EXPECTED.txt. The frozen script was inspected, not executed; neither replay nor frozen samples are needed for the infinite proof.

## originality

FAIL

The distinct Resultary record 0cf993a2096b explicitly gives the identical 5n−19 wedge classification for exactly the same stacked boundaries, together with every stack's five-loop increment, counts and local adjacency replacement. The arbitrary pure-complex statement is broader in domain and its k-formula is not quoted as such there, but follows mechanically from that identical local replacement, the same path rerouting without a global connectivity assumption, and the graph Euler formula. There is no distinct non-mechanical finding to retain. This is demonstrated coverage, not a historical-priority determination or evidence that the theorem is false.

## value

FAIL

The stacked-sphere homotopy classification and the connected local gadget were substantive in the predecessor, but give no new value here. The remaining k-dependent statement is useful as bookkeeping, yet both formulas are immediate consequences of the previously described connected replacement at the same six attachments and E−V+c. No additional structural result about which configurations realize or constrain k is part of the finding. Removing the duplicated headline therefore leaves a mechanically implied restatement, not a standalone valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
