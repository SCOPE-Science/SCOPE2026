# Shattering polynomial and an unbounded online gap for three-column monotone grid paths

## Finding

For each integer \(b\ge2\), take all directed monotone grid paths from \((0,0)\) to \((2,b)\), using east and north unit steps. A concept is the set of vertices visited by one path, and a query asks whether a specified vertex is visited. The complete shattered-support polynomial, including the empty support, is
\[
\Phi_b(z)=1+(3b+1)z+(2b^2+b-2)z^2.
\]
Consequently, \(\operatorname{VCdim}(\mathcal G_b)=2\) for all \(b\ge2\).

Put \(k=\lfloor(b+1)/2\rfloor\). With the usual complete binary mistake-tree definition of Littlestone dimension,
\[
\max\{2,2\lfloor\log_2 k\rfloor\}
\le \operatorname{Ldim}(\mathcal G_b)
\le\left\lfloor\log_2\frac{(b+1)(b+2)}2\right\rfloor.
\]
Thus \(\operatorname{Ldim}(\mathcal G_b)=2\log_2 b+O(1)\), while its VC dimension is always two. This is an unbounded static–adaptive separation for fixed-width directed shortest-path incidence.

## Assumptions and scope

All grid edges have unit length. Paths are strictly monotone and have both endpoints fixed. The support ground set is the set of grid vertices; the endpoints are present in every path and therefore belong to no nonempty shattered support. The column coordinate ranges over \(\{0,1,2\}\) and the height over \(\{0,\dots,b\}\). The theorem concerns the multiplicity-free collection of vertex sets of all paths, not the conventional set of one tie-broken shortest path per endpoint pair. The bounds are asserted for all integers \(b\ge2\), not extrapolated from a finite enumeration.

## Proof

**Parameterization.** Each path takes its first east step at an integer height \(r\), its second at height \(s\), with \(0\le r\le s\le b\). Conversely each such pair determines exactly one path. Thus there are \((b+1)(b+2)/2\) hypotheses. Write \(L_i=(0,i)\) for \(1\le i\le b\), \(M_j=(1,j)\) for \(0\le j\le b\), and \(R_h=(2,h)\) for \(0\le h\le b-1\). Their membership predicates are
\[
L_i\in P_{r,s}\iff r\ge i,\quad
M_j\in P_{r,s}\iff r\le j\le s,\quad
R_h\in P_{r,s}\iff s\le h.
\]
Every one of these \(3b+1\) non-endpoint queries is shattered as a singleton: its incidence takes both values.

**Exactly which pairs are shattered.** Two distinct middle-column queries \(M_p,M_q\) are always shattered when \(b\ge2\). Indeed \((r,s)=(p,p),(q,q),(\min(p,q),\max(p,q))\) realize positive singleton, other positive singleton, and both positive respectively, while choosing \(r=s\) at a third height realizes neither. No two different left-column queries can be shattered, because they are nested thresholds in \(r\); similarly none of two right-column queries can be shattered. For mixed columns the complete criteria are
\[
\begin{array}{lll}
\{L_i,M_j\}:&i\le j,\ i\le b-1,\\
\{M_j,R_h\}:&j\le h,\ h\ge1,\\
\{L_i,R_h\}:&i\le h.
\end{array}
\]
Necessity follows immediately from the displayed incidence inequalities: for \(L_i,M_j\), the case \(i>j\) forbids joint positivity and \(i=b\) makes \(L_i\) imply \(M_b\); the right case is symmetric. For \(L_i,R_h\), joint positivity requires \(i\le h\). To verify sufficiency directly, choose the following four parameter pairs, ordered by the target membership patterns \((0,0),(0,1),(1,0),(1,1)\):

* For \(L_i,M_j\), use \((0,0),(0,j),(i,i)\) when \(i<j\) or \((b,b)\) when \(i=j\), and \((i,j)\).
* For \(M_j,R_h\), use \((b,b)\), then \((h,h)\) if \(j<h\) or \((0,0)\) if \(j=h\), then \((j,b)\), and finally \((j,h)\).
* For \(L_i,R_h\), use \((i-1,h+1),(0,0),(b,b),(i,h)\).

All displayed pairs satisfy \(0\le r\le s\le b\), and the stated patterns follow from the predicates. Summing these four disjoint pair types gives
\[
\binom{b+1}{2}+2\sum_{i=1}^{b-1}(b-i+1)+\sum_{h=1}^{b-1}h
=\frac{b(b+1)}2+(b-1)(b+2)+\frac{b(b-1)}2
=2b^2+b-2.
\]

**No three-query support.** Every shattered triple would have all of its two-element subsets shattered. Since same-side pairs never shatter, such a triple has at most one \(L\) and at most one \(R\). Three middle queries at heights \(p<q<t\) cannot be shattered: membership of both outer heights forces membership of the intervening height. If the triple is \(L_i,M_p,M_q\) with \(p<q\), pairwise shattering forces \(i\le p\), but \(L_i=0\) and \(M_q=1\) imply \(r<i\le p<q\le s\), hence \(M_p=1\); one required pattern is missing. In the symmetric case \(M_p,M_q,R_h\), pairwise shattering forces \(q\le h\), whereas \(M_p=1\) and \(R_h=0\) force \(r\le p<q\le h<s\), hence \(M_q=1\). The remaining case \(L_i,M_j,R_h\) has \(i\le j\le h\) from its pairs; if both end-column queries are negative, \(r<i\le j\le h<s\), so the middle query is positive. Therefore no triple shatters; by downward closure no larger set shatters. This completes the polynomial proof.

**Online bounds.** A depth-\(d\) complete mistake tree needs at least \(2^d\) distinct hypotheses (one per leaf); this gives the logarithmic upper bound from hypothesis count. For the lower bound, fix \(k=\lfloor(b+1)/2\rfloor\) and retain only the \(k^2\) paths with \(r\in\{0,\dots,k-1\}\) and \(s\in\{k,\dots,2k-1\}\). This is valid because \(2k-1\le b\). Queries \(L_i\) threshold the independent variable \(r\); queries \(R_h\) threshold the independent variable \(s\). Balanced binary comparisons can distinguish the \(k\) choices of each variable in a complete mistake tree of depth \(\lfloor\log_2 k\rfloor\). Concatenating one such tree for \(r\) with one for \(s\) gives depth \(2\lfloor\log_2 k\rfloor\). A shattered pair independently ensures depth two. The lower and upper bounds differ by at most a constant as \(b\to\infty\), yielding the stated online growth.

## Verification

The standalone standard-library checker `check_grid.py` independently enumerates paths as step words, in addition to enumerating the \((r,s)\) parameter pairs. For every \(2\le b\le12\), it checks all pairs against the classification and every triple against the no-shattering assertion. For \(b\le7\), it verifies the two representations yield exactly the same vertex traces. For \(b\le10\), a memoized complete decision-tree calculation verifies that the proven online lower and upper bounds bracket the exact finite Littlestone dimension. Run `python3 check_grid.py`; success prints `THREE_COLUMN_MONOTONE_PATH_VC_ONLINE_PASS`. All universal conclusions are proved above independently of this finite replay.

## Relationship to prior work

Graph VC set systems are an established subject. Le and Wulff-Nilsen, *VC Set Systems in Minor-free (Di)Graphs and Applications*, arXiv:2304.01790, analyze distance-difference sets, directed graph balls, and edge sets of shortest-path trees; their path-tree set systems do not enumerate the vertex traces of **all** fixed-endpoint shortest paths in a rectangular strip. De Lima, da Silva and Vignatti, *A Range Space with Constant VC Dimension for All-pairs Shortest Paths in Graphs*, DOI 10.7155/jgaa.00636, study canonical tie-broken paths as elements of a range space and associated subpath-containment ranges; their dimension-two theorem is not an implication for the present dual vertex-membership support count or its online dimension. The use of binary-search trees for finite thresholds and the generic cardinality bound for online dimension are standard ingredients; the all-parameter four-type shattered-pair classification and its coupling to an unbounded gap are the asserted new combination.

## Limitations

The exact Littlestone dimension for each \(b\) is not established, only the stated tight-order bounds. The theorem is specifically for width two (three vertex columns), and does not claim a support polynomial for arbitrary grid width. Independent priority review is outstanding; related interval-threshold descriptions may appear under different terminology. Exhaustive checks at finite heights cannot independently certify the universal proof.

## References

1. Hung Le and Christian Wulff-Nilsen, *VC Set Systems in Minor-free (Di)Graphs and Applications*, first submitted April 4, 2023, arXiv:2304.01790, https://arxiv.org/abs/2304.01790.
2. Alane M. de Lima, Murilo V. G. da Silva and Andre L. Vignatti, *A Range Space with Constant VC Dimension for All-pairs Shortest Paths in Graphs*, *Journal of Graph Algorithms and Applications* **27**(7), 603–619 (2023), DOI: 10.7155/jgaa.00636.
