# Independent mathematical audit

## correctness

PASS

In an induced matching no clique fiber meets two distinct edges, and any two occupied adjacent fibers must share the unique chosen cross edge. Thus the occupied support consists of isolates (a internal choices each) and isolated pairs (b cross choices each), with every such labelled lift allowed. A fiber outside the closed neighborhood admits an additional internal edge since m>=2, while a dominated fiber rules out any new endpoint there. This proves the maximal-support rule, including empty and isolated-base cases. On a cycle, including the triangle, maximal supports are nonconstant cyclic words avoiding both 000 and 111. With k one-runs and k zero-runs, choosing p long one-runs and q long zero-runs requires p+q=n-2k. Marking an initial one-run counts n times the two binomial choices and counts each labelled word k times. All such coefficients are positive on precisely the claimed k interval, and its endpoints agree exactly at 3 and 5. Read the frozen proof, notes and Python checker; did not execute uploaded code. A separate direct edge compatibility and cyclic-word replay passed 150 small base/m profiles, n=3–16 at m=2,3 for the cyclic count, and the purity interval for n=3–64. It also gave 15z, 16z+2z^2, 25z^2, 99z^2+2z^3 for m=2 and n=3–6. Bounded replay: /workspace/branches/762912a8-3bac-4b50-9cb1-5c670bb72f83/independent_check.py. The general claim rests on the proof, not the finite replay.

## originality

PASS

The supported distinct claim is the closed-neighborhood criterion and the resulting weighted maximal enumerator, complete cyclic size spectrum and purity consequence. The projection precursor substantially overlaps the structure underlying the all-matching support sum; neither the projection method nor the maximum size alpha(G) is independently new here. No equivalent maximal weighted formula or complete cyclic spectrum was identified in the inspected sources.

## value

PASS

The weighted dominating-support identity makes inclusion-maximal matchings countable without enumerating edges of the expanded graph. On the natural cyclic family it yields both the full labelled distribution and the exceptional, nonmonotone purity boundary, information not obtainable from an extremal maximum-size count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
