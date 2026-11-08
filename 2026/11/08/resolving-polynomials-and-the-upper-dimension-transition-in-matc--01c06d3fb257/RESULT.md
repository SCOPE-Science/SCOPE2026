# Resolving polynomials and the upper-dimension transition in matching-deleted bicliques

## Finding

For integers \(a,b\ge 3\) and \(0\le t\le\min\{a,b\}\), let \(G_{a,b,t}\) be the graph obtained from the complete bipartite graph \(K_{a,b}\) by deleting \(t\) independent edges. Put \(p=a-t\), \(q=b-t\), and define
\[
Q(z)=z(z+2),\qquad
A_r(z)=\begin{cases}1,&r=0,\\z^r+r z^{r-1},&r\ge1.\end{cases}
\]
Let \(R_{a,b,t}(z)\) enumerate **all** resolving sets \(S\) of \(G_{a,b,t}\), weighted by \(z^{|S|}\). Then
\[
\boxed{R_{a,b,t}(z)=Q(z)^t A_p(z)A_q(z)
+\mathbf{1}_{t\ge1}\,t Q(z)^{t-1}z^{p+q}.}
\]
When \(t=0\), the second summand is absent, rather than being interpreted using a negative power.

Let \(M_{a,b,t}(z)\) enumerate inclusion-minimal resolving sets. The complete answer is
\[
\boxed{M_{a,b,t}(z)=
\begin{cases}
pq\,2^t z^{t+p+q-2}+\mathbf{1}_{t\ge1}t2^{t-1}z^{t+p+q-1},&p,q>0,\\
(r2^t+t2^{t-1})z^{t+r-1},&\{p,q\}=\{0,r\},\ r>0,\\
t2^{t-1}z^{t-1},&p=q=0.
\end{cases}}
\]
The second and third cases necessarily have \(t\ge1\) under the stated assumptions. In particular, all inclusion-minimal resolving sets have the same size if and only if \(t=0\) or \(p=0\) or \(q=0\). Otherwise, there are exactly two possible sizes, consecutive integers \(t+p+q-2\) and \(t+p+q-1\), with multiplicities \(pq2^t\) and \(t2^{t-1}\), respectively. Thus the upper metric dimension exceeds the ordinary metric dimension by exactly one precisely when \(0<t<\min\{a,b\}\).

For the crown graph \(G_{n,n,n}\), \(n\ge3\), the formula specializes to \(R_{n,n,n}(z)=Q(z)^n+nQ(z)^{n-1}\), and there are exactly \(n2^{n-1}\) inclusion-minimal resolving sets, all of size \(n-1\). If each vertex is chosen independently as a landmark with probability \(s_n=1-c/\sqrt n\), for a fixed \(c\ge0\) and sufficiently large \(n\), the probability of a resolving landmark set tends to \(e^{-c^2}(1+c^2)\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Label the bipartition of \(G_{a,b,t}\) as \(U=\{u_1,\ldots,u_a\}\) and \(V=\{v_1,\ldots,v_b\}\), where precisely the edges \(u_i v_i\) for \(1\le i\le t\) are missing. A resolving set distinguishes every two vertices by their distance vectors to the selected vertices. An inclusion-minimal resolving set is one whose every proper subset fails to resolve; these need not all be minimum-cardinality resolving sets. The upper metric dimension is the largest cardinality of an inclusion-minimal resolving set. The lower bounds \(a,b\ge3\) are necessary for the distance simplifications in this theorem; no assertion is made for smaller bipartition classes.

## Proof

**1. Exact distances.** All two distinct vertices of \(U\) have distance two: because \(b\ge3\), some vertex of \(V\) is adjacent to both (each \(u_i\) has at most one missing neighbor), and similarly for \(V\). For any \(i\le t\), the nonadjacent pair \(u_i,v_i\) has distance three: choose a distinct index on either side to make a three-edge path. Every other cross-part pair has distance one. In particular the graph is connected, and every cross-part pair is distinguished by any nonempty landmark set: distances from any landmark to vertices of opposite bipartition classes have opposite parity.

**2. An if-and-only-if classification.** Given \(S\subseteq U\cup V\), write \(k\) for the number of deleted-edge pairs \(\{u_i,v_i\}\) disjoint from \(S\), \(x\) for the number of unselected unmatched vertices \(u_{t+1},\ldots,u_a\), and \(y\) for the number of unselected unmatched vertices \(v_{t+1},\ldots,v_b\). Then
\[
\boxed{S\text{ resolves }G_{a,b,t}\quad\Longleftrightarrow\quad k+x\le1\text{ and }k+y\le1.}
\]
Indeed, consider two distinct unselected vertices on the \(U\)-side. Every selected \(U\)-vertex has distance two to both. A selected \(V\)-vertex distinguishes them precisely when it is the uniquely deleted partner of one of them: its distances to the two vertices are three and one. Therefore the \(U\)-vertices not individually identifiable by any selected deleted partner are exactly the \(k+x\) unselected vertices consisting of the \(U\)-ends of empty deleted pairs and the unmatched unselected \(U\)-vertices. A pair of them is indistinguishable if and only if \(k+x\ge2\). The same argument on \(V\) gives \(k+y\le1\). Every pair across \(U,V\) is distinguished by the parity observation whenever these conditions hold, since they ensure \(S\ne\varnothing\). This proves the equivalence.

**3. Complete generating polynomial.** The inequalities permit either \(k=0\) or \(k=1\). If \(k=0\), each of the \(t\) deleted pairs contributes one endpoint (two choices, weight \(z\)) or both endpoints (one choice, weight \(z^2\)), giving \(Q(z)^t\). The unmatched vertices on either side may have at most one omission, giving \(A_p(z)A_q(z)\). If \(k=1\), choose the unique completely omitted pair in \(t\) ways. Every unmatched vertex must be selected, and all other deleted pairs must be nonempty, giving \(tQ(z)^{t-1}z^{p+q}\). The cases are disjoint and exhaustive, proving \(R_{a,b,t}\).

**4. Inclusion-minimal sets.** Resolving is monotone under adding vertices, so it suffices to test deletion of individual selected vertices. A resolving set with \(k=1\) is inclusion-minimal exactly when each other deleted pair contributes precisely one endpoint: a second endpoint could be removed without spoiling the inequalities, whereas deleting any singleton endpoint creates \(k=2\), and deleting any unmatched vertex makes \(k+x\ge2\) or \(k+y\ge2\). This yields \(t2^{t-1}\) sets of size \(t-1+p+q\) when \(t\ge1\).

For \(k=0\), any deleted pair containing both endpoints has a removable endpoint, so every pair must contribute precisely one endpoint. If \(p>0\), exactly one unmatched \(U\)-vertex must be omitted: otherwise an unmatched selected \(U\)-vertex can be removed. If \(q>0\), exactly one unmatched \(V\)-vertex must likewise be omitted. These omissions make every selected deleted-pair singleton essential, since removing it would create \(k=1\) while leaving \(x=1\) or \(y=1\). When \(p=q=0\), however, removing a singleton from any pair would still leave a resolving set with \(k=1\); so this case contributes no minimal sets with \(k=0\). The choices produce precisely \(pq2^t\) sets of size \(t+p+q-2\) if both \(p,q\) are positive, or \(r2^t\) sets of size \(t+r-1\) if exactly one is positive and equals \(r\). This proves the full polynomial \(M_{a,b,t}\) and its phase transition.

**5. Crown reliability.** In \(G_{n,n,n}\), the classification reduces to requiring at most one deleted pair to be completely absent. Independent vertex retention with probability \(s\) makes a given pair absent with probability \(h=(1-s)^2\), independently across pairs. Therefore
\[
\Pr(S\text{ resolves})=(1-h)^n+nh(1-h)^{n-1}.
\]
With \(s_n=1-c/\sqrt n\), the number of absent pairs converges to a Poisson variable of mean \(c^2\), yielding the asserted limit.

## Verification

Run `python3 verify.py` using Python 3.9+ (standard library only). It constructs graph distances by independent breadth-first search and, for all \(41\) parameter triples \(3\le a,b\le5\), \(a+b\le10\), \(0\le t\le\min\{a,b\}\), tests every subset directly against the metric definition and the classification. It also independently checks both polynomial coefficient distributions and inclusion-minimality by single-vertex deletion. The run completed with \(15{,}872\) subsets, \(4{,}473\) resolving sets, and \(979\) inclusion-minimal resolving sets, with all comparisons passing. These finite checks do not replace the unrestricted proof.

## Relationship to prior work

Saputro, Baskoro, Salman, Suprijanto, and Baca (arXiv:1101.3624, 2011, Theorem 1) established the ordinary metric dimension \(n-1\) of the crown graph \(K_{n,n}\) minus a perfect matching, but not the complete resolving polynomial or the inclusion-minimal-set census. Galby, Khazaliya, Mc Inerney, Sharma, and Tale (arXiv:2206.15424, first publicly submitted 2022-06-30) investigate algorithmic metric dimension under structural parameters; their results do not enumerate resolving sets of matching-deleted bicliques. Shahida and Sunitha (2020) study resolvability and metric dimension for several graph classes, with no such complete matching-deletion enumeration in the inspected treatment. The published general characterization of resolving sets in connected chain graphs **already covers** the boundary subfamilies with \(t=0\) or \(t=1\): deleting no edge or one edge leaves a chain graph. Those cases are included for a unified formula but are not claimed as independently new. For \(t\ge2\), the graph contains an induced two-edge matching and is not a chain graph, so that result does not imply the present general polynomial. Published work on edge-metric bases of crown graphs studies distances from edges rather than ordinary vertex landmarks and likewise does not supply this theorem. The formula here refines previously known scalar extremal information rather than claiming those extremal facts as new.

## Limitations

The theorem does not extend without further analysis to \(a<3\) or \(b<3\). Exhaustive checks only cover the explicitly reported small instances. The mathematical novelty and publication priority remain provisional: equivalent results in unindexed or uninspected literature cannot be ruled out. The result has not undergone independent mathematical audit.

## References

1. S. W. Saputro, E. T. Baskoro, A. N. M. Salman, D. Suprijanto, and M. Baca, *The Metric Dimension of Regular Bipartite Graphs*, arXiv:1101.3624 (first submitted 2011-01-19), especially Theorem 1 and Section 2. https://arxiv.org/abs/1101.3624
2. E. Galby, L. Khazaliya, F. Mc Inerney, R. Sharma, and P. Tale, *Metric Dimension Parameterized by Feedback Vertex Set and Other Structural Parameters*, arXiv:2206.15424 (first submitted 2022-06-30). https://arxiv.org/abs/2206.15424
3. K. S. Shahida and M. S. Sunitha, *Results on Resolvability and Metric Dimension in Graphs*, Advances in Mathematics: Scientific Journal 9 (2020), 1859–1866, DOI:10.37418/amsj.9.4.43.
4. G. Chartrand, C. Poisson, and P. Zhang, *Resolvability and the Upper Dimension of Graphs*, Computers & Mathematics with Applications 39 (2000), 19–28.
5. *Resolving sets and the resolving polynomial of chain graphs* (2026), publicly available scientific research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-resolving-sets-and-the-resolving-polynomial-of-chain-graphs--30553b031b4a; its main claim covers the boundary subcases \(t=0,1\).
