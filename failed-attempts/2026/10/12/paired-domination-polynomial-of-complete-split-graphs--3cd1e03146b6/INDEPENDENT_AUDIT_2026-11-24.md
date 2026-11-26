# Independent mathematical audit

## correctness

PASS

The mathematical Finding is correct. With no clique vertex, domination forces selecting the whole nonempty independent part, whose induced graph has no perfect matching. With a clique vertex, domination is automatic. A perfect matching must send each of the b independent vertices to a different one of the a clique vertices; this is sufficient when a+b is even, since the remaining clique vertices pair off. This proves the coefficients by independent binomial choices, including r=1 and n=1. Every edge alone dominates and every nonempty paired-dominating set contains a matching edge, proving both size-two conclusions. The frozen proof is all-orders; the inspected verify.py and recorded finite output are not needed as proof and the frozen script was not run. The false family assertion at RESULT.md line 62 affects the prior-work comparison, not the theorem.

## originality

FAIL

The distinct Oct. 4 Resultary record establishes a broader occupancy-level theorem for all complete multipartite graphs. This includes the entire frozen family, contrary to RESULT.md line 62. The ordinary polynomial specializes verbatim by parameter choice, and marking the eligible occupancies gives the bivariate expression without new matching or enumeration information. The minimum and upper-minimum conclusions are stated or directly implied as detailed below.

## value

FAIL

The bivariate specialization is convenient exposition but adds no independent structural result or nontrivial refinement beyond the already available occupancy characterization for the broader family. There is no supported distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
