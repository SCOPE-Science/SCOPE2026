# Independent mathematical audit

## correctness

PASS

Comparing two deletion starts i<j after removing the common prefix and suffix shows the outputs coincide precisely when all lag-b comparisons from i+1 through j are equalities. Each fiber is an interval, so the count is one plus the lag-b mismatches. Distinct edges are pairwise independent, including edges with a shared endpoint, proving the two-length covariance and means. At L=a+b the lag graph is the disjoint union of cycles of addition by a modulo L, one per residue mod g=gcd(a,b). The earliest whole cycle has last vertex L−g+1. At that length the other residues are intact paths (at most one vertex was removed per cycle), and for n>L every extra vertex attaches to its own residue component, so the cycle rank is max(0,n−L+g). In the forest regime all edge indicators jointly factor by root-first exposure. Outside it, the probability of all endpoint equalities is q^(κ−n); division by q^(a−n)q^(b−n) proves the exact certificate and excludes independence. In the three-length expansion every forest term vanishes; each triangle contributes −(q−1)/q³ for mismatches. The extreme positions have gap c, so the two possible middle positions exist exactly at c=a+b and give 2(n−c) triangles. Direct enumeration independently corroborated every pair joint table and triple centered moment for (q,n)=(2,10),(2,11),(5,5), outside the supplied grid. Replay: python3 branches/independent_checks.py 1 (standard library).

## originality

FAIL

The strongest indexed tandem-duplication result is not merely a parameter match: its exact distinct-descendant count equals the frozen burst-deletion count pointwise on every source word. This proves equivalent coverage of the two-length covariance and independence theorem, with the same lag-graph cycle decomposition. The simultaneous-minimum ratio is the all-equalities specialization of the verified arbitrary-graph product-moment identity, with cycle rank from that decomposition (and unchanged residue connectivity after n=a+b). The three-length formula likewise specializes the published graph-coloring edge-product identity to three edges: only triangles contribute, and the two orders of the inner lag on a line give the factor 2(n−c). No independent substantive part of the stated result remains. The indexed comparison is dated later and demonstrates present equivalent coverage, not earlier priority; the primary graph-coloring identity predates the record.

## value

FAIL

Quantifying when two burst cardinalities cannot be modeled as independent is a natural question. But its main law transfers unchanged from the pointwise identical tandem count, and the ratio and additive mixed moment use direct cycle-rank and triangle substitutions into the known product formula. Converting the output interpretation or naming the additive case does not leave a separate exact fact requiring new mathematical work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
