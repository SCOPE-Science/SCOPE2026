# Complete multipartite Crank–Nicolson positivity is governed by the smallest part

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a finite, connected, simple, unweighted complete multipartite graph. Assume \(r\ge2\), each \(a_j\) is a positive integer, and \(N=\sum_{j=1}^r a_j\ge3\). Define \(a=\min_j a_j\) and the combinatorial graph Laplacian \(L=D-A\). For every \(h\ge0\), let
\[
C(h)=(I+hL/2)^{-1}(I-hL/2).
\]
Then the exact entrywise-nonnegativity horizon is
\[
\boxed{C(h)\ge0\ \Longleftrightarrow\ 0\le h\le h_*},\qquad
h_* = \frac{a+\sqrt{a^2+4(N-a)(N-2)}}{(N-a)(N-2)}.
\]
At every positive step, all off-diagonal entries are strictly positive. All vertices in minimum-size parts, and only those vertices, have the smallest diagonal entries. Those entries are zero at \(h_*\) and negative for every larger step. The interval is therefore sharp, without subsequent positivity recovery.

In particular the threshold depends only on total order \(N\) and minimum part size \(a\), regardless of the other part sizes or number of parts. For fixed \(N\ge3\) and fixed \(2\le r\le N\), the threshold is strictly increasing as the attainable minimum part size grows. It is maximized when \(a=\lfloor N/r\rfloor\); the minimum occurs when \(a=1\) (when a singleton is possible), and then \(h_*=2/(N-2)\).

## Assumptions and scope
The graph has no loops or edge weights and is connected because there are at least two nonempty parts. \(L\) is the unnormalized Laplacian; the factor \(h/2\) in each Crank–Nicolson factor is essential. The theorem concerns the completed one-step matrix and all \(h\ge0\), not positivity of internal solver stages. The order-two graph \(K_2\), excluded by \(N\ge3\), has an unbounded positivity interval.

## Proof
Write \(s=h/2\), and let \(R(s)=(I+sL)^{-1}\). Because \(L\) is an irreducible graph Laplacian, \(I+sL\) is a nonsingular irreducible \(M\)-matrix for every \(s>0\), so \(R(s)\) has strictly positive entries. The Cayley identity gives \(C(h)=2R(s)-I\). Consequently every off-diagonal entry is strictly positive for \(h>0\), and \(C(h)\ge0\) is equivalent to \(R_{ii}(s)\ge1/2\) at every vertex.

Fix a vertex in a part of size \(b\). The orthogonal eigenspace decomposition of \(L\) is: the constant line with eigenvalue zero; the zero-sum vectors supported inside each part of size \(a_j\), with eigenvalue \(N-a_j\); and the blockwise constant vectors with total sum zero, with eigenvalue \(N\). The squared coordinate projections of this vertex onto those three classes are respectively \(1/N\), \((b-1)/b\), and \((N-b)/(bN)\). The spectral theorem thus yields, for every \(s\ge0\),
\[
R_b(s)=\frac1N+\frac{b-1}{b(1+s(N-b))}+
\frac{N-b}{bN(1+sN)}.
\]
For any two allowable part sizes \(b,c\), direct common-denominator simplification gives the exact difference
\[
R_b(s)-R_c(s)=
\frac{s(b-c)(1+(N-1)s)}{(1+Ns)(1+(N-b)s)(1+(N-c)s)}.
\]
For \(s>0\), the denominator and non-size factors are strictly positive; hence \(R_b(s)<R_c(s)\) exactly when \(b<c\). In particular, the minimum diagonal occurs exactly in parts of size \(a=\min_j a_j\).

A second exact simplification gives
\[
2R_a(s)-1=
\frac{1+as-(N-a)(N-2)s^2}
{(1+Ns)(1+(N-a)s)}.
\]
The denominator is positive on \([0,\infty)\). Because \(N\ge3\), \(a\ge1\), and \(N-a\ge1\), the numerator is a concave quadratic, positive at zero, with exactly one positive root
\[
s_*=\frac{a+\sqrt{a^2+4(N-a)(N-2)}}{2(N-a)(N-2)}.
\]
It is nonnegative precisely when \(0\le s\le s_*\), and strictly negative for larger \(s\). Since \(h=2s\), the displayed sharp \(h_*\) follows, together with non-recovery and equality cases.

Finally, at any fixed positive \(s\), the diagonal formula is strictly increasing in part size \(b\). Since each diagonal function is continuous and strictly decreasing in \(s\) from \(1\) to \(1/N<1/2\), the first crossing time is strictly increasing with \(b\). Thus \(h_*\) is strictly increasing in the minimum part size at fixed \(N\). A composition of \(N\) into \(r\) positive parts has \(a\le\lfloor N/r\rfloor\), with equality attainable, while \(a=1\) is attainable whenever \(r\le N\); this proves the extremal description. Substitution \(a=1\) reduces the root to \(h_*=2/(N-2)\).

## Verification
The standalone Python script `verify.py` runs two symbolic equalities (the diagonal-difference identity and the quadratic factorization) in SymPy, then reconstructs exact rational matrices for all 246 ordered complete-multipartite part-size profiles with total order \(3\le N\le8\). It checks 1,230 complete matrices (five rational half-steps each), verifies every off-diagonal entry is positive, computes the exact predicted minimum diagonal, and compares entrywise positivity against the stated threshold using exact algebraic-number comparisons. All checks passed on the extracted script. This finite replay does not replace the proof for arbitrary \(N\).

## Relationship to prior work
Horváth, Song and Terlaky (first publicly posted 26 June 2014) analyze positivity/invariance step thresholds for Taylor and rational discretizations on polyhedra. Their general sufficient-threshold construction does not evaluate exact complete-multipartite Crank–Nicolson thresholds.

The published *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* establishes \(C(h)=2R(h/2)-I\), a general diagonal resolvent criterion, and statewise spectral first-crossing formulas. Those identities are prior work and explicitly credited. The new claim is the complete-multipartite specialization beyond merely invoking that criterion: it proves which part controls the threshold, simplifies the entire spectral criterion to one sharp quadratic depending only on \(N\) and the smallest part, and gives the resulting partition-extremal classification. The published result's complete-graph special case \(h_*=2/(N-2)\) is recovered, not claimed independently.

## Limitations
This theorem does not extend directly to weighted, normalized, directed, or incomplete multipartite graphs. It is a graph-specific exact classification, not a new general positivity theorem for every reversible chain. The literature comparison was bounded, and an unindexed graph-specific equivalent formula may exist. The result has not undergone independent mathematical validation.

## References
1. Z. Horváth, Y. Song and T. Terlaky, *Steplength Thresholds for Invariance Preserving of Discretization Methods of Dynamical Systems on a Polyhedron*, arXiv:1406.6755 (first posted 2014-06-26), DOI: 10.3934/dcds.2015.35.2997, https://optimization-online.org/wp-content/uploads/2014/06/4408.pdf.
2. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
