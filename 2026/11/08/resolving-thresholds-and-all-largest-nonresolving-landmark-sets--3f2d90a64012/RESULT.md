# Resolving thresholds and all largest nonresolving landmark sets in mixed Hamming graphs

## Finding
Let \(d\ge 2\), let \(q_1,\ldots,q_d\ge2\) be integers, and put \(G=\square_{i=1}^{d}K_{q_i}\), \(N=\prod_iq_i\), \(q=\max_iq_i\). A landmark set \(S\subseteq V(G)\) *resolves* \(G\) when the distance vectors to \(S\) distinguish every pair of vertices. The **resolving threshold** \(r(G)\) is the smallest integer such that every set of \(r(G)\) vertices resolves \(G\). Equivalently, this is the resolving number (also termed metric-dimension threshold), not the ordinary metric dimension.

Write \(b=|\{i:q_i=2\}|\), \(t=|\{i:q_i=3\}|\), \(c=|\{i:q_i=4\}|\), and \(a=|\{i:q_i=q\}|\). The exact threshold is \(r(G)=Nh+1\), and the number \(M(G)\) of **distinct** nonresolving landmark sets of cardinality \(r(G)-1\) is:

\[
\begin{array}{c|c|c}
\text{condition} &h&M(G)\\ \hline
q\ge5 &(q-2)/q &a\binom q2\\
q=4 &1/2 &6c+2\binom b2\\
q=3,\ b\ge2 &1/2 &2\binom b2\\
q=3,\ b\le1 &1/3 &3t+6\binom t2+6bt\\
q=2 &1/2 &2\binom d2
\end{array}
\]

Every maximum nonresolving set is precisely a full distance bisector \(B(u,v)=\{w:d(w,u)=d(w,v)\}\) of a pair of distinct vertices. All pairs achieving the maximum can be classified by their set \(T=\{i:u_i\ne v_i\}\) of differing coordinate indices: \(\{i\}\) with \(q_i=q\) when \(q\ge5\); either a single four-symbol coordinate or two binary coordinates when \(q=4\); exactly two binary coordinates when \(q=3,b\ge2\) or \(q=2\); and exactly one ternary coordinate or two coordinates containing at least one ternary coordinate when \(q=3,b\le1\). These are exhaustive, with the table giving the number of distinct bisector *sets*, rather than the number of vertex pairs.

## Assumptions and scope
All graphs are finite, simple and undirected. The graph has labelled coordinate factors; swapping equal factors is an automorphism but does not identify vertex subsets in \(M(G)\). Each coordinate alphabet can have a different size. Graph distance is Hamming distance, and a landmark set is allowed to include vertices it identifies. The restrictions \(d\ge2\) and \(q_i\ge2\) are essential to the stated five-way table. For the one-factor complete graph \(K_q\), the threshold separately equals \(q-1\).

## Proof
**1. General sharp obstruction.** For distinct vertices \(u,v\), define the bisector \(B(u,v)=\{w:d(w,u)=d(w,v)\}\). A landmark set fails to resolve \(G\) if and only if it is contained in some \(B(u,v)\). Consequently the maximum size of a nonresolving set equals \(F=\max_{u\ne v}|B(u,v)|\), and \(r(G)=F+1\). Furthermore, every nonresolving set of size \(F\) is a full bisector of size \(F\), so counting distinct maximum bisectors also counts all critical nonresolving sets. This general reduction is known from the resolving-number literature; it is used here, not claimed as new.

**2. Independent-coordinate equality.** Fix \(u\ne v\) and let \(T=\{i:u_i\ne v_i\}\). Choose a uniformly random vertex \(W\). For \(i\in T\), define \(X_i=d(W_i,u_i)-d(W_i,v_i)\). Independence of coordinates and elementary counting give
\[
\Pr(X_i=1)=\Pr(X_i=-1)=1/q_i,\qquad
\Pr(X_i=0)=(q_i-2)/q_i.
\]
The common coordinates contribute zero, so
\[
|B(u,v)|/N=\Pr\!\left(\sum_{i\in T}X_i=0\right).
\]
This probability depends only on the alphabet sizes of the differing coordinates, not on the chosen symbols or on other coordinates.

**3. Sharp concentration and equality.** When \(q_i\ge3\), the largest atom of \(X_i\) is \(p_i=(q_i-2)/q_i\). For any independent sum \(Y\), convolution gives \(\Pr(X_i+Y=0)\le p_i\). If \(q_i\ge4\), zero is the unique mode of \(X_i\), so equality requires \(Y=0\) almost surely; with other differing coordinates this is impossible because each such coordinate has both positive and negative values with positive probability. For \(q_i=3\), the masses at \(-1,0,1\) all equal \(1/3\); equality holds exactly when the sum of all remaining differing-coordinate increments is supported on \(\{-1,0,1\}\). Because every increment has \(\pm1\) in its support and the increments are independent, this holds exactly when there is **at most one** additional differing coordinate.

When all differing coordinates are binary, their increments are independent fair signs. If \(|T|\) is odd, the zero-sum probability is zero; if \(|T|=2s\), it is \(\binom{2s}s/4^s\). The latter strictly decreases in \(s\ge1\), since consecutive terms have ratio \((2s+1)/(2s+2)\). Therefore the sharp binary-only value is \(1/2\), attained precisely at \(|T|=2\).

Compare these bounds. When \(q\ge5\), \((q-2)/q>1/2\), and equality requires a single coordinate of largest alphabet size. At \(q=4\), both a singleton four-symbol coordinate and a binary pair attain \(1/2\). At \(q=3\), a binary pair wins if two binary axes exist; otherwise one ternary axis or any pair including a ternary axis attains \(1/3\). When \(q=2\), only binary pairs maximize. This proves all values \(F=Nh\), all equality types, and the threshold formula.

**4. Counting distinct critical failures.** For a maximizing one-coordinate pair on an alphabet of size \(q\ge4\), the bisector is the union of all coordinate fibers whose entry avoids an unordered pair of letters. There are \(\binom q2\) distinct such sets on each eligible axis. For a pair of binary coordinates, the bisector is one of the two parity classes on the corresponding two-coordinate projection, yielding exactly two distinct sets per binary axis pair. For two ternary coordinates, the bisector projects to the graph of a permutation of the three letters (three cells in a \(3\times3\) board), giving exactly \(3!=6\) distinct sets per pair. For one binary and one ternary coordinate, it projects to two cells having different ternary symbols, one in each binary row, giving \(3\cdot2=6\) sets per mixed axis pair. A maximizing singleton ternary coordinate has three possible one-letter fibers. The different coordinate supports and these projection patterns give distinct subsets, including across the listed types. Summing their multiplicities yields every formula for \(M(G)\).

## Verification
The accompanying standalone `verify.py` constructs the labelled Hamming vertex sets, computes distances directly, enumerates all vertex-pair bisectors and their distinct maximum-size sets, and compares with the closed expressions and allowed support types. It examines 61 mixed-alphabet profiles with two to four coordinates, alphabet sizes two through six, and at most 100 vertices. Across these profiles 82,284 distinct vertex pairs are tested. For graph orders at most 12 it also enumerates every vertex subset of the predicted critical size and checks resolvability directly. It reports `VERIFY_OK`. No finite computation is used as a substitute for the unrestricted concentration proof.

## Relationship to prior work
The resolving-number identity \(r(G)=1+\max_{u\ne v}|B(u,v)|\) is Proposition 2.1 of Garijo, González and Márquez (2013); the same graph parameter was later called *metric dimension threshold* by Korivand, Khashyarmanesh and Tavakoli (2022). The 2019 preprint of Laird, Tillquist, Becker and Lladser characterizes resolving sets of uniform-alphabet Hamming graphs by a constrained linear system. Its general decision criterion is relevant, but neither the sharp maximum bisector concentration for arbitrary *unequal* alphabets nor the above five-case formula and critical-failure multiplicities is given in the inspected material. The present work is the explicit sharp evaluation and structural classification, not invention of the parameter, Hamming-distance identity, or general resolvability criterion.

## Limitations
The proof concerns the *worst-case arbitrary-landmark threshold*, not minimum-cardinality resolving sets, fault tolerance after prescribed deletions, or all coefficients of the resolving polynomial. The originality assessment is provisional: equivalent formulas could occur under *resolving number*, *metric dimension threshold*, *distance bisector*, or concentration terminology in literature not located or examined. The general algorithmic criteria in the cited papers may facilitate other derivations but do not themselves supply the reported closed classification. No independent mathematical audit has been performed.

## References
1. L. Laird, R. C. Tillquist, S. Becker and M. E. Lladser, *Resolvability of Hamming Graphs*, arXiv:1907.05974 (first submitted 2019-07-12); SIAM Journal on Discrete Mathematics **34** (2020), 2063–2081. https://arxiv.org/abs/1907.05974
2. D. Garijo, A. González and A. Márquez, *The resolving number of a graph*, arXiv:1309.0252 (first submitted 2013-09-01). https://arxiv.org/abs/1309.0252
3. M. Korivand, K. Khashyarmanesh and M. Tavakoli, *Metric Dimension Threshold of Graphs*, Journal of Mathematics (2022), article 1838719, first published 2022-09-14. https://doi.org/10.1155/2022/1838719
