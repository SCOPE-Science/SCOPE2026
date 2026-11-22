# A sharp sphere-to-contractible transition for directed feedback theta networks

## Finding
For integers \(m\ge2\) and \(r\ge1\), take internally disjoint directed paths \(P_i:s\to t\) of lengths \(L_i\ge2\) and a single internally disjoint directed return path \(Q:t\to s\) of length \(r\), with exactly their indicated arcs. Let \(X(D)\) be the ordinary simplicial **multipath complex**: a face is an arc subset whose components are directed simple paths or isolated vertices. Put \(h=\#\{i:L_i\ge3\}\).

For at least one long forward arm, the complete *integral homotopy* classification is
\[
X(D)\simeq
\begin{cases}
S^{r+L-2},&h=1\text{ and the unique long arm has length }L,\\
\ast,&h\ge2.
\end{cases}
\]
Thus one forward arm longer than two edges produces exactly one sphere, while two long arms cause contractibility for **all** lengths and all numbers of additional two-edge arms. The all-two-edge regime \(h=0\) is previously classified and is not part of the claimed novelty.

## Assumptions and scope
The digraph has distinct terminals \(s,t\). The forward arms share only their terminals, and the return path meets them only at the terminals. All graph vertices and arcs are distinct except the shared terminals, and no opposite or extra arcs are present. Each forward path has at least two arcs; at least one has at least three. The return path has at least one arc. Every simplicial vertex represents a directed arc, not a graph vertex. A valid face has selected indegree and outdegree at most one at every digraph vertex and contains no directed cycle. Homotopy types are of geometric realizations and all homological consequences are integral.

## Proof
Let \(E_i\) be the arc set of forward path \(P_i\), and let \(C\) be the \(r\)-arc set of the return path. Write \(a_i\) for the first arc and \(b_i\) for the last arc of \(P_i\), and \(I_i=E_i\setminus\{a_i,b_i\}\) for its private internal arcs, of cardinality \(L_i-2\). Put \(I=\coprod_i I_i\). Internal arcs never conflict at a vertex with any other selected arc; within a branch they form consistently directed subpaths. The only local restrictions are choosing at most one of the \(a_i\) and at most one of the \(b_i\). The only possible directed cycles are the complete unions \(E_i\cup C\).

Let \(K\) be the complex of arc subsets on the forward paths satisfying just these indegree/outdegree restrictions. It is \(K_{m,m}*\Delta(I)\), where the bipartite graph \(K_{m,m}\) is regarded as a one-dimensional simplicial complex on the first and last arcs (including their singleton vertices). Let \(K'\subseteq K\) consist of faces containing no entire forward arm \(E_i\). This is a subcomplex. The face classification yields the **exact simplicial gluing**
\[
X(D)=(K*\partial\Delta(C))\ \cup_{K'*\partial\Delta(C)}\ (K'*\Delta(C)).
\]
When \(r=1\), the boundary \(\partial\Delta(C)\) has only the empty face, with the standard augmented-complex join convention. Both pieces and their intersection are subcomplexes. The second piece is contractible. Taking its homotopy cofiber, and using that joining with a boundary simplex corresponds to iterated reduced suspension of the cofiber, gives
\[
X(D)\simeq\Sigma^{r-1}\operatorname{Cofib}(K'\hookrightarrow K).
\]
Because at least one \(I_i\) is nonempty, \(K\) is a cone and is contractible. Therefore
\[
X(D)\simeq\Sigma^r K'.
\]
All these statements concern actual homotopy types, not just homology: simplicial inclusions are cofibrations, and ordinary homotopy-pushout and suspension identities apply.

**One long arm.** Suppose only \(I_j\) is nonempty, with \(q=|I_j|=L-2\ge1\). Write \(H=K_{m,m}\), let \(e=\{a_j,b_j\}\) be the corresponding diagonal edge, and set \(H_0=H\setminus\{e\}\) (retaining both endpoints). Then
\[
K'=(H_0*\Delta(I_j))\cup(e*\partial\Delta(I_j)),
\]
with intersection \(\partial e*\partial\Delta(I_j)\simeq S^{q-1}\). Both large pieces are contractible, so their homotopy pushout is \(K'\simeq S^q\). This also covers \(q=1\) with the empty-boundary convention: the intersection is the two endpoints of \(e\), an \(S^0\). Thus \(X(D)\simeq\Sigma^r S^{L-2}=S^{r+L-2}\).

**Two or more long arms.** Choose a private internal arc \(x\in I_i\) and another \(y\in I_j\) with \(i\ne j\). Every face of \(K'\) can be extended by at least one of \(x,y\): adding either arc creates no local degree conflict, and an added arc could complete a forbidden forward path only for its own branch. At most one branch can be completed, because selected first arcs and selected last arcs each have cardinality at most one. Consequently \(K'\) is the union of the two closed stars of \(x\) and \(y\). Their intersection is exactly the closed star of \(\{x,y\}\): simultaneous addition causes no further conflict. Each star and their intersection are contractible, whence \(K'\) is contractible by the homotopy-pushout/nerve argument. The suspension formula then proves \(X(D)\simeq\ast\).

## Verification
The accompanying standalone standard-library program `verify_mixed_feedback.py` constructs each graph from its directed arcs, independently checks selected indegrees/outdegrees and directed cycles, and compares every subset against the face classification. It independently computes all reduced mod-two Betti numbers for twelve mixed-length cases, including one long arm, two or three long arms, one- and two-arc return paths, and varying long-arm lengths. Every tested instance agrees with the exact statement; the recorded output is `verify_mixed_feedback_output.txt`. These finite tests are not the infinite or integral proof; the preceding cofiber and contractible-star arguments establish that proof.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith introduced and classified multipath complexes of directed polygons and several other families, but not these mixed-length feedback networks. The previously described consistently oriented triangular books classify the special all-two-edge forward-arm case with a one-edge return, while an earlier fixed-length multi-arm classification covers the all-two-edge forward-arm family for longer returns. Those results do not imply either the one-long-arm homotopy sphere or the contractibility caused by a second long arm. A source–sink feedback theorem establishes top-dimensional homology classes from directed Hamiltonian paths, but does not provide this mixed-length homotopy classification; an unrelated Mayer path-homology computation studies a different invariant. The new result is the length-transition classification for \(h\ge1\), not the known all-short baseline.

## Limitations
Only internally disjoint simple forward and return paths in the specified orientations are treated. Reverse arcs, extra chords, multiple return paths, or length-one forward arms are not covered. Nothing is asserted about equivariant fixed-point or quotient homotopy, except what follows from ordinary homotopy. The comparisons cannot exclude unknown or unindexed equivalent work. Finite computations by themselves cannot certify the all-parameter theorem or integral homotopy equivalence.

## References
1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first posted 2022-08-09), §§2–5. https://arxiv.org/abs/2208.04656
2. *Equivariant collapse of consistently oriented triangular-book multipath complexes* (2026-11-08), publicly available mathematical result, covering the special case of a one-edge common return and all two-edge forward arms.
3. *Source–sink feedback edges split off Hamiltonian-path spheres in multipath complexes* (2026-10-25), publicly available mathematical result, concerning a different top-dimensional retract.
