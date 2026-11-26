# All connected dominating sets of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(M=\{a_i b_i:1\le i\le n\}\) is the deleted perfect matching. For a set \(S\subseteq V(\operatorname{Cr}_n)\), define
\[
P=\{i:a_i\in S\},\qquad Q=\{i:b_i\in S\}.
\]
Then \(S\) is a connected dominating set if and only if
\[
|P|\ge2,\qquad |Q|\ge2,
\]
and the single exceptional configuration \(|P|=|Q|=2\) with \(P=Q\) does not occur.

Therefore the connected domination polynomial is
\[
C(\operatorname{Cr}_n;x)=\big((1+x)^n-1-nx\big)^2-\binom{n}{2}x^4.
\]
In particular,
\[
\gamma_c(\operatorname{Cr}_n)=4,
\]
every inclusion-minimal connected dominating set has cardinality \(4\), the number of minimum connected dominating sets is
\[
\binom{n}{2}\left(\binom{n}{2}-1\right),
\]
and the total number of connected dominating sets is
\[
(2^n-n-1)^2-\binom{n}{2}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A dominating set \(S\) satisfies that every vertex outside \(S\) has a neighbor in \(S\). It is connected dominating when the induced graph \(\operatorname{Cr}_n[S]\) is connected. The theorem concerns crown graphs with \(n\ge3\); the smaller deleted-matching graphs are disconnected and are outside this statement.

The polynomial \(C(G;x)\) is defined here by
\[
C(G;x)=\sum_{S\text{ connected dominating}}x^{|S|}.
\]

## Proof
Let \(S\) be a connected dominating set and let \(P,Q\) be as above.

First, \(|P|\ge2\). If \(P=\varnothing\), then \(S\subseteq B\); a singleton \(S=\{b_i\}\) leaves \(a_i\) undominated, while any larger \(S\) induces an edgeless graph and is disconnected. If \(P=\{i\}\), domination of \(b_i\) forces \(b_i\in S\), because \(a_i\) is the only selected vertex on the opposite side and is not adjacent to \(b_i\). But then \(b_i\) is isolated in the induced graph on \(S\), since there are no edges inside \(B\) and \(a_i b_i\) is the deleted matching edge. Hence \(S\) cannot be connected. By symmetry, \(|Q|\ge2\).

Conversely, if \(|P|\ge2\), then every vertex of \(B\) has a selected neighbor in \(A\): a vertex \(b_j\) is nonadjacent to at most the single vertex \(a_j\), so among at least two selected \(A\)-vertices at least one is adjacent to it. Similarly, \(|Q|\ge2\) implies that all vertices of \(A\) are dominated. Thus every set satisfying the two size inequalities is dominating.

It remains to determine when the induced subgraph on such a set is connected. The induced graph on \(A_P\cup B_Q\) is the complete bipartite graph \(K_{|P|,|Q|}\) with precisely the edges \(a_i b_i\) removed for indices \(i\in P\cap Q\). If \(|P|=|Q|=2\) and \(P=Q=\{i,j\}\), the induced graph consists of the two disjoint edges \(a_i b_j\) and \(a_j b_i\), so it is disconnected.

Now suppose the induced graph is disconnected while \(|P|,|Q|\ge2\). Choose \(a_i\) and \(b_j\) in different components. Since vertices in different components cannot be adjacent, necessarily \(i=j\). Because \(|Q|\ge2\), choose \(k\in Q\setminus\{i\}\); then \(a_i b_k\) is an edge, so \(b_k\) lies in the component of \(a_i\). Because \(|P|\ge2\), choose \(r\in P\setminus\{i\}\); then \(a_r b_i\) is an edge, so \(a_r\) lies in the component of \(b_i\). If \(r\ne k\), then \(a_r b_k\) is an edge joining the two components, impossible. Hence \(r=k\), and the same argument shows there can be no third selected index on either side. Therefore \(P=Q=\{i,k\}\). This proves the connectedness criterion.

Counting all choices with \(|P|,|Q|\ge2\) gives
\[
\left(\sum_{p=2}^n\binom{n}{p}x^p\right)^2=\big((1+x)^n-1-nx\big)^2.
\]
Exactly \(\binom{n}{2}\) choices have \(|P|=|Q|=2\) and \(P=Q\), each contributing \(x^4\); subtracting them gives the displayed polynomial.

The least possible cardinality is therefore \(4\), and its coefficient is
\[
\binom{n}{2}^2-\binom{n}{2}=\binom{n}{2}\left(\binom{n}{2}-1\right).
\]
If a connected dominating set has more than two selected vertices on one side, one can delete a vertex on that side while preserving the criterion; in the only delicate case of three selected vertices on one side and two on the other, delete a vertex so that the remaining two index sets are unequal. Hence every inclusion-minimal connected dominating set has exactly two selected vertices on each side and thus size \(4\). Finally, evaluating the polynomial at \(x=1\) yields the stated total count.

## Verification
The symbolic proof establishes the statement for every \(n\ge3\). The standalone checker `verify.py` independently constructs the crown graph, tests domination and induced connectivity directly for every subset, and compares those results with the stated criterion for \(3\le n\le9\). It also reconstructs every coefficient, checks the minimum coefficient and total count, and verifies that all inclusion-minimal connected dominating sets in the tested range have size \(4\).

Replay with:

`python3 verify.py`

Expected output:

`VERIFY_OK n_range=3..9 subset_checks=349504 criterion_checks=349504 coefficient_checks=91 minimal_checks=2786 max_order=18`

The finite computation is a stress test, not a substitute for the arbitrary-\(n\) proof.

## Relationship to prior work
Camby and Schaudt's connected-domination paper gives a standard connected-domination framework and is publicly dated 2013-03-12; its full text lists primary MSC 05C69. It does not specialize to crown graphs.

A later same-object source by Kumar, Pomeroy, and Tran proves only the scalar statement \(\gamma_c(\operatorname{Cr}_n)=4\) for \(n\ge3\) in Lemma 5.1 and explicitly notes that the authors could not find a reference for that lemma. The present theorem does not claim that scalar value as new; it classifies every connected dominating set, proves that all inclusion-minimal connected dominating sets are minimum, and gives the exact polynomial and multiplicities.

Wolfram GraphData exposes connected-domination polynomials and connected-dominating-set counts for named finite graph instances, and MathWorld tabulates the crown connected-domination number \(4\). Those database facilities can verify individual cases but do not supply the symbolic family classification or the closed formula proved here.

## Limitations
The literature search cannot rule out every unindexed source or unpublished note using another notation for crown graphs. The most relevant located same-object source gives the minimum value only, and the general database facilities found are finite-instance tools rather than a symbolic crown-family theorem. The checker is exhaustive only through order \(18\); the general statement rests on the proof above.

## References
1. Eglantine Camby and Oliver Schaudt, “A Note on Connected Dominating Set in Graphs Without Long Paths And Cycles,” arXiv:1303.2868v1, first posted 2013-03-12. The accessible full text lists MSC 05C69, 05C75, 05C38.
2. Arvind Kumar, Joshua Pomeroy, and Le Tran, “Binomial edge ideals of crown graphs,” arXiv:2507.03889v1, first posted 2025-07-05. Lemma 5.1 proves \(\gamma_c(C_{n,n})=4\) for \(n\ge3\).
3. Wolfram Research, `GraphData` documentation, entries for `ConnectedDominatingSets`, `ConnectedDominatingSetCount`, and `ConnectedDominationPolynomial`.
4. Eric W. Weisstein, “Connected Domination Number,” MathWorld; the family table lists the crown graph value \(4\).
