# Independent mathematical audit

## correctness

PASS

The private leaf forces each pair to weigh at least one, with (0,1) the only weight-one pair. Weight-at-least-two sites dominate the base graph because an uncharged site's leaf contributes only one and a positive original neighbor must be charged. A minimum dominating set attains the lower bound with (1,1) on that set. At equality the charged set has size gamma(H) and every charged pair weighs two. If B consists of positive original vertices, every vertex outside N[B] must be an inactive charged site. Conversely B union U(B) already dominates, so gamma(H) squeezes the number of inactive charged sites to exactly |U(B)|. Then (2,0) and (1,1) are free choices on B, while all remaining labels are fixed. This argument includes an isolated base vertex and works without connectivity. On cycles, n-u≤3b and b+u=ceil(n/3) leave only b=k except for residue one, when b=k-1 is possible. For u=0, the three residue counts of labeled centers are 3, n(k+1)/2 and n respectively (ordered gap deficits 0, 2 and 1, with n/k accounting for the marked start). For u=1 the uncovered site fixes the tiling of the other 3m sites by disjoint triples, giving n further choices with weight 2^m. The boundary cases n=3,4,5 follow from the same argument. Independent direct checks covered all 75 labeled simple base graphs on 1–4 vertices and sunlets of lengths 3–6, with (minimum weight, count) = (4,6), (6,32), (7,20), (8,12); separate tight-set counts through n=18 agreed. These corroborate the proof; the frozen checker was inspected, not executed.

## originality

FAIL

The distinct October 13 Resultary record 9dede768c463, whose publication date is explicit in its metadata, already gives the exact labeled sunlet formulas and the complete active/inactive optimizer bijection. The arbitrary-base form is an immediate graph-independent rewriting of its optimum-pair argument, not a nontrivial extension of its cycle-specific gap analysis. The earlier primary rooted-product paper also covers the minimum weight. This is actual overlap and implication, not a title match or a failed literature retrieval.

## value

FAIL

A new full optimizer census on sunlets would be meaningful, but it is already available. The only apparent remainder is eliminating the charged-set variable in the known local active-site bijection via the minimality of S. That useful algebraic restatement is mechanically implied and supplies no independently new exact invariant or classification; no surviving substantive claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
