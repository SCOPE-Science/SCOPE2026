# One complementary chord induces a parity bifurcation in triangular-graph XOR dynamics

## Finding
Let \(n\ge4\), let \(T(n)=J(n,2)=L(K_n)\) be the graph on the two-subsets of \([n]\), adjacent when they meet in one point, and adjoin **one previously absent edge**, joining any two disjoint two-subsets. Denote the resulting simple graph by \(G_n\). On the finite field \(\mathbb F_q\), \(q=2^f\) with \(f\ge1\), evolve all \(N=\binom n2\) vertex values simultaneously by the sum of their open-neighbor values. Write \(F\) for this linear update and \(\tau(x)\) for the smallest nonnegative number of steps after which \(x\) lies on a periodic orbit.

The single new edge yields the following **complete temporal classification** for every admissible \(n,q\), independently of the choice of its disjoint endpoint pair:

**Odd \(n\ge5\).** The operator has \(\operatorname{rank}F=n+1\) and satisfies \(F^5=F\), with sharp entry bound \(\tau\le1\). Exactly \(q^{n+1}\) states are recurrent. Among them there are \(q^{n-3}\) fixed states, \((q^{n-1}-q^{n-3})/2\) primitive two-cycle orbits and \((q^{n+1}-q^{n-1})/4\) primitive four-cycle orbits. Every listed orbit type is nonempty. Every periodic state has exactly \(q^{N-n-1}\) initial preimages under the one-step map, and an orbit of period \(d\) has basin size \(d q^{N-n-1}\).

**Even \(n\ge4\).** The operator has \(\operatorname{rank}F=n\), satisfies \(F^5=F^3\), and its recurrent subspace has dimension two. There are \(q\) fixed states and \((q^2-q)/2\) primitive two-cycle orbits, with no other periods. For every recurrent orbit of length \(d\), its basin has exactly \(d q^{N-2}\) initial states. Let \(C_t=|\{x:\tau(x)\le t\}|\). Then
\[
 C_0=q^2,\qquad C_1=q^{N-n+2}.
\]
For \(n=4\), \(C_2=q^N\), and the sharp entry bound is two. For every even \(n\ge6\),
\[
 C_2=q^{N-2},\qquad C_3=q^N,
\]
with the sharp entry bound three. Consequently, \(1-q^{-2}\) of all initial states in the latter family require the final three updates.

In contrast, before the new edge is added the triangular-graph update is an idempotent (\(F_0^2=F_0\)) when \(n\) is odd and is nilpotent in two steps (\(F_0^2=0\)) when \(n\) is even. Thus the edit creates four-cycles from a fixed-point-only system in odd order, and creates persistent two-cycles from complete extinction in even order. For \(q=2\), the five-point example has exactly 4 fixed states, 6 primitive two-cycles, and 12 primitive four-cycles; the six-point example has 2 fixed states and one two-cycle.

## Assumptions and scope
Vertices of \(T(n)\) are the unordered two-subsets of \([n]\). A pair of these vertices is connected by an edge exactly when their two-subsets intersect in one point. Since the symmetric group on \([n]\) acts transitively on ordered pairs of disjoint two-subsets, it suffices to take the added edge between \(e=\{1,2\}\) and \(f=\{3,4\}\); all other choices are isomorphic. The update uses no self-loops or state-dependent choices, and all arithmetic is in characteristic two. A fixed state is a primitive orbit of length one. A primitive orbit of length \(d\) contains \(d\) distinct configurations. A basin includes the orbit itself, and \(\tau=0\) for recurrent states. The theorem does not extend as stated to odd-characteristic fields or multiple added edges.

## Proof
Write \(V=\mathbb F_q^{\binom{[n]}2}\). Let \(H\) be the \(n\)-by-\(N\) unoriented edge-vertex incidence matrix of the complete graph, so every column has precisely two unit entries. In characteristic two, the adjacency matrix of the original triangular graph is \(A_0=H^T H\): diagonal entries are two and hence zero, and off-diagonal entries register intersection in exactly one point. With \(e,f\) also denoting the corresponding coordinate unit vectors, the perturbed matrix is
\[
 A=A_0+ef^T+fe^T.
\]
Set \(\alpha=He=\mathbf e_1+\mathbf e_2\) and \(\beta=Hf=\mathbf e_3+\mathbf e_4\), so \(\alpha^T\alpha=\beta^T\beta=\alpha^T\beta=0\). For an arbitrary configuration \(x\), put \(t=Hx\), \(u=e^Tx\), \(v=f^Tx\), \(a=\alpha^Tt\), and \(b=\beta^Tt\).

**1. Surjective small-coordinate model and first rank.** The sum of the entries of \(t\) is zero. Conversely, the graph \(K_n\) with the two disjoint edges \(\{1,2\},\{3,4\}\) removed is connected for every \(n\ge4\). Its incidence columns therefore span the hyperplane \(\sum t_i=0\). Holding \(u,v\) prescribed and varying all other edge coordinates realizes every \(t\) in this hyperplane. Thus the map \(x\mapsto(t,u,v)\) is onto the \((n+1)\)-dimensional space \(W=\{t:\sum t_i=0\}\times\mathbb F_q^2\).

For any \((t,u,v)\in W\) the update is
\[
 Ax=\Phi(t,u,v):=H^Tt+ve+uf.
\]
The vector \(H^Tt\) is a complete-graph cut vector. Every nonzero such cut has at least \(n-1\) coordinates, whereas every vector in \(\operatorname{span}\{e,f\}\) has at most two. Therefore \(\operatorname{im}(H^T|_{\sum t_i=0})\) meets \(\operatorname{span}\{e,f\}\) trivially. The kernel of \(H^T\) consists precisely of constant vectors; such a nonzero vector belongs to the even-sum hyperplane if and only if \(n\) is even. Hence \(\Phi\) has rank \(n+1\) for odd \(n\) (and is injective) and rank \(n\) for even \(n\). Because \(x\mapsto(t,u,v)\) is surjective, these are the exact ranks of \(A\).

**2. All iterates reduce to four scalar coordinates.** The incidence identity \(HH^T=(n\bmod2)I+J\), with \(J\) the all-one matrix, and \(Jt=0\) imply that the small-coordinate triple evolves by
\[
 t'=\varepsilon t+v\alpha+u\beta,\qquad
 u'=a+v,\qquad v'=b+u,\qquad a'=\varepsilon a,\quad b'=\varepsilon b,
\]
where \(\varepsilon=n\bmod2\). These identities hold for **all** inputs, without restricting to recurrent states. Let \(T\) denote this map on \(W\). It satisfies the intertwining identity \(A\Phi=\Phi T\), and \(A^j x=\Phi T^{j-1}(t,u,v)\) for each positive integer \(j\).

**3. Odd case.** Now \(\varepsilon=1\), so \(a,b\) are constant in time and
\[
 (u_1,v_1)=(a+v,b+u),\quad
 (u_2,v_2)=(a+b+u,a+b+v),\quad
 (u_3,v_3)=(b+v,a+u),\quad
 (u_4,v_4)=(u,v).
\]
The sums of the four successive \(u\)- and \(v\)-values both vanish; hence the accumulated increments in \(t\) also vanish, and \(T^4=I_W\). The conjugacy between \(T\) on \(W\) and \(A\) on \(\operatorname{im}A\), via injective \(\Phi\), proves \(A^5=A\), all recurrence at time one, and precisely \(q^{n+1}\) recurrent states. The fixed triples obey \(u=v=a=b=0\). The two functionals \(a,b\) are independent on the even-sum hyperplane for odd \(n\ge5\), giving fixed-space dimension \(n-3\). The triples fixed by \(T^2\) obey exactly the independent conditions \(a=b\) and \(u+v=a\), giving fixed-space dimension \(n-1\). Subtracting configurations fixed by the shorter powers and dividing by orbit lengths yields the stated primitive orbit counts.

**4. Even case and exact rank filtration.** Here \(\varepsilon=0\), so \(a'=b'=0\). Put \(P=A_0e=H^T\alpha\), \(Q=A_0f=H^T\beta\). Direct substitution into the preceding update formula gives
\[
 A^2x=vP+uQ+(b+u)e+(a+v)f
\]
and
\[
 A^3x=(b+u)(P+f)+(a+v)(Q+e).
\]
The vectors \(P+f\) and \(Q+e\) are independent because \(P,Q\) vanish at the two chord coordinates. Furthermore \(A(P+f)=Q+e\) and \(A(Q+e)=P+f\): use \(A_0^2=0\), \(Ae=P+f\), \(Af=Q+e\), and \(AP=AQ=0\). Thus \(\operatorname{im}A^3\) is exactly a two-dimensional recurrent subspace with the swap action. It contains \(q\) fixed states and \((q^2-q)/2\) two-cycles. Also \(A^5=A^3\).

For \(n\ge6\), the functionals \(a,b,u,v\) on the input space are independent, and \(P,Q,e,f\) are independent: the cut vectors \(P,Q\) are independent modulo the two chord coordinates, as can be seen from their differing incidences with a fifth point and the zero cut coordinates at \(e,f\). Therefore \(\operatorname{rank}A^2=4\). In the exceptional \(n=4\) case, \(\alpha+\beta=\mathbf1\) gives \(a=b\) on the even-sum hyperplane and \(P=Q\), whence \(\operatorname{im}A^2=\operatorname{span}\{P+e,P+f\}\) has dimension two. Therefore the sharp settling time is three in even orders at least six and two in order four. The inequality of successive image dimensions makes these bounds sharp.

**5. Every basin and entrance shell.** For any linear map, if its recurrent subspace \(R\) has dimension \(r\) and is contained in \(\operatorname{im}A^t\), every recurrent state has \(q^{N-\operatorname{rank}A^t}\) preimages under \(A^t\); hence
\[
 C_t=q^{r+N-\operatorname{rank}A^t}.
\]
The recurrent subspace lies in every power image since \(A\) permutes it. The ranks derived above are \((n+1,n+1,\ldots)\) for odd \(n\), \((n,4,2,2,\ldots)\) for even \(n\ge6\), and \((4,2,2,\ldots)\) for \(n=4\). These give every displayed entrance formula. At the full settling time the fibers have size \(q^{N-r}\), and each primitive orbit contains \(d\) distinct recurrent states, giving the claimed basin formula. \(\square\)

## Verification
`verify_rank.py` constructs the modified triangular adjacency matrix independently from two-subset intersections and tests characteristic-two rank, all power identities, fixed-space dimensions, and the unmodified nilpotence/idempotence claim for every \(4\le n\le16\). `verify_states.py` independently evolves every one of the \(64\), \(1024\), and \(32768\) binary configurations for \(n=4,5,6\), confirming entry layers, primitive orbit counts, and **each** orbit's basin size. It additionally evolves all \(4096\) configurations over \(\mathbb F_4\) for \(n=4\), using coefficientwise XOR in a fixed binary basis for the field. Both programs were executed successfully. Their finite tests corroborate, but do not replace, the proof for all sizes and finite characteristic-two fields.

## Relationship to prior work
Peeters' published treatment of Johnson-graph modular adjacency matrices (Section 4.1) gives the **unperturbed** characteristic-two annihilating polynomials and ranks. Ciandrini and coauthors' 2008 preprint (first public version 2008-09-09) proves general linear-XOR cycle/basin principles on Boolean networks but does not analyze this single complementary edge inserted into \(J(n,2)\). A separately published published-finding corpus theorem deletes an **existing** Johnson adjacency edge, for even \(n,k\), and obtains a sixteen-state recurrent space with periods three and six; here the new edge joins **nonadjacent** vertices, and the even-order recurrent space has four states over \(\mathbb F_2\), with periods one and two. Neither perturbation is a specialization of the other. The available comparison for the two-set Kneser graph concerns the **complementary graph itself**, not the triangular graph with one chord. General exact ranks of an unedited adjacency matrix and general Fitting decomposition do not determine the perturbed powers; the explicit cross-incidence calculation above supplies those missing steps.

## Limitations
Only one added edge, between disjoint two-subsets, is classified. Different missing-edge operations, odd-characteristic updates, additional loops, or nonlinear updates may have different temporal spectra. The four-point instance also belongs to the well-studied family of complete graphs with deleted matchings and is not relied on as a novelty witness; the claim concerns the full infinite \(n\)-family and its parity split. The finite computations are not a substitute for the general proof. Historical priority against inaccessible or unindexed equivalent graph-perturbation results is uncertain. Independent external validation has not been performed.

## References
- R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics **15** (2002), 127–149, Section 4.1, https://doi.org/10.1023/A:1013842904024; full text https://www2.math.ethz.ch/EMIS/journals/JACO/Volume15_2/v121065651493101.fulltext.pdf. An earlier research memorandum is catalogued in 1994 without a verified day of public release.
- L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526v1, first publicly submitted 2008-09-09, https://arxiv.org/abs/0809.1526.
- *One-edge defects create universal six-cycles in nilpotent Johnson parity dynamics*, published published-finding corpus research, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-one-edge-defects-create-universal-six-cycles-in-nilpotent-johnso--6ee185cd61fc.
- S. M. Johnson graphs background, https://aeb.win.tue.nl/graphs/Johnson.html.
