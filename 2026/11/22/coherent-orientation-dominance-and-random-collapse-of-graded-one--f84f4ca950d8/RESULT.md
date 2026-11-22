# Coherent-orientation dominance and random collapse of graded one-point types

## Finding
Let \(\mathcal U\) be the Fraïssé limit of finite, three-sorted oriented simple graphs with sorts \(A,B,C\), with arcs permitted only between different sorts, and with no directed triangle. Both orientations and the absence of an arc are allowed between a pair of different sorts. Let \(D\) be a finite, individually named induced base consisting of \(r\ge1\) vertices of sort \(A\) and \(s\ge1\) of sort \(B\), with every cross-sort pair oriented exactly once. For a complete nonalgebraic one-point type of a new sort-\(C\) vertex, give weight \(z\) for each named vertex incident to an arc and weight \(1\) for each nonincident named vertex. Let \(P_D(z)\) be the sum of these weights, and let \(\mathsf c_k(D)=[z^k]P_D(z)\).

Define
\[
P^*_{r,s}(z)=(1+2z)^r(1+z)^s+(1+z)^r(1+2z)^s-(1+z)^{r+s}.
\]
Then for every orientation \(D\) of \(K_{r,s}\), \(\mathsf c_k(D)\le[z^k]P^*_{r,s}(z)\) for every \(0\le k\le r+s\). Equality holds at degrees zero, one and two for every orientation. Write \(d_D^+(v),d_D^-(v)\) for outdegree and indegree in \(D\). The first possible difference is exactly
\[
[z^3](P^*_{r,s}-P_D)=\sum_{v\in D}d_D^+(v)d_D^-(v),
\]
interpreted as zero if \(r+s<3\). A nonconstant orientation (containing both edge directions relative to the \(A,B\) bipartition) has a strictly smaller coefficient in *every* degree \(3\le k\le r+s\), and the two coherent orientations are exactly the orientations attaining the coefficientwise maximum. In particular their number of sort-\(C\) one-types is \(2^r3^s+3^r2^s-2^{r+s}\).

For the balanced case \(r=s=n\), orient the \(n^2\) base edges independently and fairly, and write \(T_n=P_D(1)\). Then
\[
\mathbb E T_n=\sum_{p,q\ge0,\ p+q\le n}\frac{n!}{p!q!(n-p-q)!}\bigl(1+2^{-p}+2^{-q}\bigr)^n,
\quad
\frac{T_n}{2\cdot4^n}\longrightarrow1
\]
in \(L^1\) and almost surely for any joint realization of the random orientation matrices. The coherent extremum is \(2\cdot6^n-4^n\), so its ratio to a typical random count grows asymptotically as \((3/2)^n\).

## Assumptions and scope
All structures are in the three-sorted finite relational language, with sort names retained. Every arc joins distinct sorts; there are no digons, loops, or directed 3-cycles. The old base has *all* \(A\)-to-\(B\) cross-sort pairs oriented, with no old sort-\(C\) parameters. New sort-\(C\) points are outside the base. The graded polynomial records adjacency, not arc direction, although the types themselves distinguish the two directions. The almost-sure statement refers to any common probability space carrying a sequence of matrices with the stated fair independent within-matrix entries; independence between different matrix sizes is unnecessary.

The finite class has hereditary closure, joint embedding and free amalgamation: take the union over the common induced substructure and add no arcs across new vertices. A forbidden triangle cannot be introduced across the amalgam. Its countable homogeneous limit is therefore well-defined, and each finite admissible new-point incidence pattern occurs infinitely often. Hence counting admissible status assignments exactly counts complete nonalgebraic one-types over an individually named finite base.

## Proof
**Status reduction.** Assign to each old parameter one of \(0,+,-\), meaning respectively no arc, an arc from the new vertex, and an arc to the new vertex. For an old arc \(a\to b\), the status pair \((+, -)\) is forbidden (it completes \(a\to b\to x\to a\)); for an old arc \(b\to a\), the pair \((- ,+)\) is forbidden. No other directed triangle can involve the new vertex, since the base has only sorts \(A,B\). Thus these local constraints are necessary and sufficient.

**Finite bipartite Hölder lemma, with strictness.** Fix nonempty supports \(S_A,S_B\), of sizes \(p,q\), on which statuses are restricted to \(+,-\). Let \(Z(M)\) count permitted two-sign configurations for the induced orientation matrix \(M\). For each column \(j\), define \(f_j(u)=\sum_{v\in\{+,-\}}\prod_{i=1}^{p}K_{ij}(u_i,v)\), where \(K_{ij}\) is the 0–1 compatibility matrix for that edge. Then \(Z(M)=\sum_u\prod_{j=1}^{q}f_j(u)\). Hölder gives \(Z(M)\le\prod_j(\sum_u f_j(u)^q)^{1/q}\), and hence is at most the count for some matrix with every column equal to one original column. Apply the same argument over rows to this latter matrix. The resulting matrix is constant; for either constant orientation its count is \(2^p+2^q-1\). If two columns differ, the first Hölder inequality is strict: for a column pattern \(v\), choose the first-side sign vector having \(+\) on every edge of orientation \(1\) and \(-\) on every edge of orientation \(0\). Then \(f_v\) takes value \(2\) at that sign vector, whereas any different column pattern takes value at most \(1\) there. Reversing the roles of the two distinct columns shows their functions cannot be proportional. If all columns coincide but the row signs differ, the second Hölder step is strict by the analogous argument. The same reasoning works when one side has size one: only the nontrivial Hölder step is needed. Thus
\[
Z(M)\le2^p+2^q-1,
\]
with equality if and only if the induced orientation is constant. For empty support on either side, there are \(2^{p+q}\) sign choices, agreeing with \(2^p+2^q-1\).

**Coefficientwise extremality.** Sum the last bound over all supports of size \(p\) and \(q\). The coherent polynomial becomes
\[
\sum_{p=0}^r\sum_{q=0}^s\binom rp\binom sq(2^p+2^q-1)z^{p+q}=P^*_{r,s}(z).
\]
Supports of at most two vertices have at most one cross-edge and attain equality. A mixed two-edge star on three supported vertices has four compatible two-sign assignments rather than five; its unique deficit is one. Every three-element support not forming such a mixed star has zero deficit. Thus the cubic difference equals the number of oppositely directed incident-edge pairs, namely \(\sum_vd_D^+(v)d_D^-(v)\). Since the underlying complete bipartite graph is connected, every nonconstant orientation contains such a mixed two-edge star. Extending its three-vertex support to any support size \(k\in[3,r+s]\) gives a strict contribution at degree \(k\), and the remaining contributions are nonnegative. This proves strictness at every such degree and the equality characterization.

**Exact expectation.** For a fixed assignment of statuses to the \(A\)-vertices, let \(p\) be its number of \(+\) statuses and \(q\) its number of \(-\) statuses. A \(B\)-vertex can have status zero unconditionally; status \(+\) is valid with probability \(2^{-q}\), and status \(-\) with probability \(2^{-p}\). The edge choices for distinct \(B\)-vertices are independent. Summing over their three statuses and then over all old \(A\)-status assignments proves the expectation formula in the Finding section.

**Almost-sure collapse.** Every base orientation permits all status assignments using only \(0,+\), and separately those using only \(0,-\). Their intersection contains only the all-zero assignment. Thus \(T_n\ge L_n:=2\cdot4^n-1\) deterministically.

To bound the expectation, put \(h=\lceil3\log_2 n\rceil\) for large \(n\), and split its sum into \(p=0\) or \(q=0\) and the remaining terms. The \(p=0\) contribution is \(S_n=\sum_{q=0}^n\binom nq(2+2^{-q})^n\). The summands with \(q\ge h\) are at most \(\binom nq2^n\exp(O(n^{-2}))\), while those with \(q<h\) contribute at most \(3^n\exp(O((\log n)^2))\). Since \(S_n\ge4^n\), it follows that \(S_n=4^n(1+O(n^{-2}))\). The \(q=0\) terms contribute the same bound.

For \(p,q\ge h\), the remaining terms total at most \(3^n\exp(O(n^{-2}))\). If \(1\le p<h\le q\), their sum is at most \(\exp(O((\log n)^2))(3+o(1))^n\), since \(2^{-p}\le1/2\) and there are at most \(\binom np2^{n-p}\) assignments with a specified \(p\). The symmetric case \(1\le q<h\le p\) is identical. Finally, \(1\le p,q<h\) contributes at most \(2^n\exp(O((\log n)^2))\). All mixed-sign contributions are \(o(4^n/n^2)\). Consequently
\[
0\le\mathbb E(T_n-L_n)=O(4^n/n^2).
\]
Markov's inequality yields \(L^1\) convergence of \(T_n/(2\cdot4^n)\) to 1 and a summable bound \(O(n^{-2})\) for the probability of any fixed positive relative excess. The first Borel–Cantelli lemma proves the stated almost-sure convergence, without a cross-\(n\) independence hypothesis.

## Verification
`verify.py` independently enumerates status words for all matrices of sizes at most \(3\times3\), and checks the exact factorized coefficient recurrence for all \(8858\) orientations in the sizes \(1\times1,1\times2,2\times1,2\times2,2\times3,3\times2,3\times3,3\times4,4\times3\). It verifies coefficientwise domination, strictness for mixed orientations, the exact cubic difference, and agreement between the two enumeration methods on \(666\) small matrices. The companion `verification_output.txt` records the deterministic output. The probabilistic limit and all-order coefficientwise conclusion rest on the written proofs, not on finite enumeration.

## Relationship to prior work
Fraïssé free amalgamation provides the ambient homogeneous structure, and Hatami's general weak Hölder property for complete bipartite graphs gives a broad non-strict matrix partition-function inequality. The non-strict supportwise inequality itself is therefore not claimed as a new general graph-norm theorem. The contribution is the exact incidence-graded strictness and cubic directed-two-path deficit in the finite-base logical setting, together with an exact first-moment formula and an almost-sure \(4^n\) versus \(6^n\) separation for fair random and coherent orientations. Galvin–Tetali's regular bipartite homomorphism extremal theorem concerns a different graph-family extremization and does not assert this orientation-law random limit.

## Limitations
The theorem concerns new points of the third sort over complete bipartite orientations in the other two sorts. It makes no claim for old bases with absent cross-edges, arbitrary triangles outside this free-amalgamation class, higher arities, biased random base orientations or nonuniform assignment activities. The prior general weak Hölder inequality is expressly credited; an equivalent probabilistic limit in unindexed literature remains a historical-priority risk. Independent mathematical review has not been performed.

## References
- Hamed Hatami, *Graph norms and Sidorenko's conjecture*, arXiv:0806.0047, first posted 2008-05-31; see Section 2.4, in particular the complete-bipartite weak Hölder statement. https://arxiv.org/abs/0806.0047
- Gabriel Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762, first posted 2015-05-04; see introduction and general free-amalgamation framework. https://arxiv.org/abs/1505.00762
- David Galvin and Prasad Tetali, *On weighted graph homomorphisms*, arXiv:1206.3160, first posted 2012-06-14; see the weighted homomorphism inequality for regular bipartite graphs. https://arxiv.org/abs/1206.3160
