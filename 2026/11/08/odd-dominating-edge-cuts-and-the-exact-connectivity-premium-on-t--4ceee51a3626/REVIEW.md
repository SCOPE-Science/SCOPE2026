# Scientific self-review

## Correctness — PASS
The theorem fixes the closed-neighborhood parity definition on \(T_n=L(K_n)\). For every binary selected edge indicator \(x_{ij}\), the independently reconstructible quantities \(d_i\) satisfy \(d_i+d_j+x_{ij}=1\); the double-counting identity \(\sum_i d_i=0\) forces the even-\(n\) uniqueness and allows exactly the even-cardinality \(d_i=1\) subsets for odd \(n\). The reverse construction is checked explicitly by recomputing the parities. The disjoint-clique decomposition proves the full weight distribution, connectivity criterion and both minima, for all \(n\ge3\). The two executable checks independently enumerate and solve finite instances, and their recorded outputs are inspected. Finite tests do not establish the infinite formula; the symbolic parity reduction does.

## Originality — PASS, with priority risk
The 2003 Caro–Klostermeyer paper sets the odd-domination framework; the relevant introductory text focuses on complete-partite graphs, cycles and grids, not an explicit triangular-graph cardinality-and-connectivity profile. The 2005 Caro–Klostermeyer–Yuster full paper studies connected odd domination and treats grid graphs, cycle powers, complete multipartite graphs and path powers. The checked text and graph-family comparison do not establish the new full classification of odd-dominating sets on \(L(K_n)\) or the exact connectivity premium. published-finding corpus searches for line-graph parity solutions, triangular graph weight distributions, and connected odd domination returned other graph families and different invariants rather than implication-equivalent classifications. Recoverable historical claim searches found no identical result. Search noncoverage is not a mathematical proof of priority, and the 2003 scanned text was not read in full; this remains a stated risk.

## Value — PASS
General odd domination and connected odd domination are established motivating problems. Triangular graphs are a canonical infinite line-graph/Johnson-graph family. The theorem determines every parity-feasible configuration and its weight, shows a sharp even/odd phase change in solution-space dimension, and quantifies a quadratic connectivity penalty for every odd size at least five. This answers a precise connected-versus-unrestricted comparison, instead of merely repeating generic existence or reporting a small finite count. The proof also explains the nonconnectivity through the forced disjoint-clique geometry.

## Scope and limitations
Only closed-neighborhood odd domination on \(L(K_n)\), \(n\ge3\), is addressed. The two programs independently validate finite ranges; no other graph family or independent external audit is claimed. The scanned 2003 source's full text was not inspected and historical-priority certainty is not asserted.

Self-review: passed. Independent audit: not yet performed.
