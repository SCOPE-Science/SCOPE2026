# Strict four-terminal connectivity association in three-hub random forests

## Finding
Let \(F\) be a random spanning forest of \(K_{3,n}\), sampled with probability proportional to \(v^{|E(F)|}\), for every integer \(n\ge4\) and every real \(v>0\). Choose four pairwise distinct vertices \(a,b,c,d\) in the class of size \(n\). Write \(X=\mathbf 1_{\{a\leftrightarrow b\}}\) and \(Y=\mathbf 1_{\{c\leftrightarrow d\}}\), where connectivity is within \(F\). Then
\[
\operatorname{Cov}(X,Y)=\frac{12v^5 R(n-4,v)}{(1+3v)^4P(n-4,v)^2}>0.
\]
The polynomials \(P\) and \(R\) are explicit below, with \(R\) having nonnegative coefficients and a strictly positive constant term. This yields an all-fugacity, all-size connectivity inequality on a noncactus family with arbitrarily many overlapping cycles.

## Assumptions and scope
The three vertices on the smaller shore are called hubs, the \(n\) others peripheral vertices. The forest includes all vertices, including isolated vertices; every acyclic edge subset is assigned mass \(v^e\), where \(e\) is its edge count. The result applies to four *distinct* peripheral vertices, uniformly positive edge fugacity, and integers \(n\ge4\). It does not assert analogous correlations for arbitrary vertex placements, arbitrary edge fugacities, or the entire random-cluster model.

Set \(m=n-4\), \(A=1+3v\), and define
\[
\begin{aligned}
P(m,v)={}&1+6v+21v^2+40v^3+48v^4\\
 &+m(3v^2+10v^3+24v^4)+3m^2v^4,\\
Q(m,v)={}&1+10v+47v^2+120v^3+144v^4\\
 &+m(5v^2+30v^3+72v^4)+9m^2v^4,\\
S(m,v)={}&3+58v+411v^2+1224v^3+1296v^4\\
 &+m(25v^2+318v^3+648v^4)+81m^2v^4.
\end{aligned}
\]
For the positivity certificate write \(R=R_0+mR_1+m^2R_2+m^3R_3\), with
\[
\begin{aligned}
R_0(v)={}&4+60v+372v^2+1261v^3+2556v^4+3024v^5+1728v^6,\\
R_1(v)={}&v+48v^2+331v^3+1090v^4+1824v^5+1440v^6,\\
R_2(v)={}&9v^3+106v^4+315v^5+396v^6,\\
R_3(v)={}&12v^5+36v^6.
\end{aligned}
\]

## Proof
Each peripheral vertex has a neighborhood that is one of the eight subsets of the three hubs, encoded by its three-bit mask. A forest cannot contain more than two peripheral vertices of degree at least two: each such vertex merges at least two hub components, and three hubs can experience at most two successful mergers without creating a cycle. If there are two such vertices, both have degree exactly two and must join *different* unordered pairs of hubs; repeating a hub pair makes a four-cycle. A single branching vertex may join any of the three hub pairs or all three hubs.

Fix the four marked neighborhood masks; there are exactly \(8^4\) possibilities. Each of the remaining \(m\) vertices is isolated or attaches to a single hub, contributing \(A^m\), except for at most two branching exceptions. Enumerate all possible exceptions: none; one of the four degree-at-least-two hub masks, with \(m\) choices of exceptional vertex; or two distinct two-hub masks, with \(3m(m-1)\) choices in total. Their ordinary single-attachment factors are divided out as \(A^{-1}\) or \(A^{-2}\). Reject any configuration containing a cycle; for each remaining configuration test the two marked terminal connections by taking the transitive closure of the selected hub-leaf edges. This is an exact finite enumeration of *all* forests for arbitrary symbolic \(m\), not a finite-length approximation.

Define the fugacity-weighted totals \(Z\), \(Z_X\), and \(Z_{XY}\) by summing, respectively, all forests, forests where \(X=1\), and forests where both events hold. The preceding census, carried out symbolically and independently checkable using the accompanying program, gives
\[
\frac{Z}{A^m}=A^2P,\quad
\frac{Z_X}{A^m}=3v^2Q,\quad
\frac{Z_{XY}}{A^m}=\frac{3v^4S}{A^2}.
\]
Consequently,
\[
Z_{XY}Z-Z_X^2=A^{2m} 3v^4(SP-3Q^2)
=A^{2m}12v^5R(m,v).
\]
Dividing by \(Z^2=A^{2m+4}P^2\) proves the displayed covariance formula. Every coefficient of \(R\) is nonnegative, and \(R_0(0)=4\), so the covariance is strictly positive for all \(m\ge0\) and \(v>0\).

## Verification
Execute `python CHECK.py` with SymPy installed. It regenerates the symbolic all-length census from the hub-neighborhood masks, checks the exact three numerator polynomials and the positive factorization, and independently exhausts every edge subset of \(K_{3,4}\), \(K_{3,5}\), and \(K_{3,6}\). It prints `ALL_K3N_FOREST_CHECKS_PASSED` when all tests succeed. The infinite-length claim is established by the bounded branching classification and symbolic identity; the finite-graph checks are supplementary.

## Relationship to prior work
Grimmett and Winkler [1] study negative *edge-occupation* association of spanning forests; those statements do not compare terminal-pair connectivity events. Çiçeksiz and Ravichandran [2, Section 6 and Conjecture 6.2] conjecture positive covariance for four distinct terminal vertices for arbitrary finite graphs, and their conclusion [2, Section 8] still lists this as an open conjecture. Positive connectivity results on cactus graphs [3] do not apply to \(K_{3,n}\), which contains overlapping four-cycles. An existing all-fugacity negative-edge-covariance result specifically for \(K_{3,n}\) [4] concerns distinct edge indicators rather than our nonlocal connectivity events. The theorem here proves one natural infinite noncactus subfamily of the larger conjecture, not the full conjecture.

## Limitations
This result covers only common edge activity, disjoint pairs of peripheral terminals, and graphs with precisely three hubs. The finite mask certificate is explicitly supplied, but no fully independent external mathematical audit or complete historical-priority certification is claimed. Relevant previously published graph-specific connectivity identities may exist under different notation.

## References
1. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185 (first public 2003-02-17), https://arxiv.org/abs/math/0302185.
2. A. Çiçeksiz and S. Ravichandran, *Negative Correlations for Forests and the q<1 Random Cluster Model*, arXiv:2610.00549 (2026), https://arxiv.org/abs/2610.00549.
3. *All-weight connectivity covariance on cactus graphs for random-cluster and forest laws*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-weight-connectivity-covariance-on-cactus-graphs-for-random-c--40f119d1bafa.
4. *Strict negative edge correlations for equal-fugacity arboreal gas on \(K_{3,n}\)*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-strict-negative-edge-correlations-for-equal-fugacity-arboreal-ga--0cd0e1e4f228.
