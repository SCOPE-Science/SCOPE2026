# Independent mathematical audit

## correctness

PASS

For a threshold graph with creation word initial 0, every maximal independent set is either all 0-vertices M0 or one 1-vertex u_j with later 0-vertices M_j; queries at 1-vertices are singleton concept tests and at 0-vertices are nested prefix cuts. Thus no pair VC-shatters; if there is a 1-vertex VCdim1. Exact interval Littlestone recurrence R(a,b)=max(1, max_{k in Q,a<k<=b} 1+min(R(a,k-1),R(k,b))) uses singleton tests for rank1, prefix tests for rank>=2, and computes in O(n^3). Depth h requires 2^h hypotheses hence >=2^h-1 one-vertices; its first h-1 levels require >=2^(h-1)-1 distinct noninitial prefix cuts, each needing a separate noninitial 0-vertex, plus initial 0, giving n>=3*2^(h-1)-1. Word 01(011)^(2^(h-1)-1) has exactly those cuts to bisect hypothesis intervals into 2-element leaves, reaching h. Equality of the bound fixes cuts at every even hypothesis boundary and hence the unique creation word. Appending universal late zeros preserves ranks. Independently exhaustive across all creation words through n=9 against direct concept minimax ranks; first rank2 at n5.

## originality

PASS

After comparing exact statements, hypotheses, data orders and implications, no inspected stronger source subsumes the surviving precise claim; known prerequisite results and any overlapping subclaims are expressly credited. This is best-of-knowledge, not a claim of proof of historical priority.

## value

PASS

Exact sharp finite-graph resource threshold for an adaptive dimension that grows logarithmically although static VCdim remains 1; uniqueness of extremal threshold graph and O(n^3) rank recurrence are mathematically substantive structural results, not simple concept counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
