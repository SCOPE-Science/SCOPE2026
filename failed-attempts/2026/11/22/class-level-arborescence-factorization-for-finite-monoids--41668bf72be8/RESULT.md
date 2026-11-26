# Class-level arborescence factorization for finite monoids

## Finding

Let \(M\) be any nonempty finite monoid, and let \(P=M/\mathcal J\) denote its Green \(\mathcal J\)-class poset, ordered by principal-ideal inclusion. For \(J\in P\), write \(w_J=|J|\). Its greatest class \(U\) is the group of units; put \(u=w_U\). The *divisibility digraph* has vertices \(M\), with \(a\to b\) for distinct \(a,b\) precisely when \(a\in MbM\). An *in-arborescence toward \(e\)* is a spanning directed tree in which each vertex other than \(e\) has one outgoing arc and eventually reaches \(e\).

Assign a variable \(t_J\) to an arc within \(J\), and a variable \(z_{JK}\) to an arc from \(J\) to a strictly greater class \(K\). Define

\[
Q_J(\mathbf z)=\sum_{K>J}w_Kz_{JK},\qquad
\mathcal A_e(\mathbf t,\mathbf z)=\sum_{T\text{ an in-arborescence toward }e}\prod_{a\to b\in T}x_{[a],[b]},
\]

where \(x_{J,J}=t_J\) and \(x_{J,K}=z_{JK}\) for \(J<K\). For **every unit** \(e\in U\), the complete class-edge enumerator is

\[
\boxed{\mathcal A_e(\mathbf t,\mathbf z)=
 u^{u-2}t_U^{u-1}\prod_{J\ne U}Q_J(\mathbf z)\bigl(w_Jt_J+Q_J(\mathbf z)\bigr)^{w_J-1}.}
\]

For \(u=1\), define the displayed top-class factor to be \(1\). No nonunit can be the root of such an arborescence. In particular, putting \(q_J=\sum_{K>J}w_K\), the number for each specified unit root is

\[
\boxed{A_e=u^{u-2}\prod_{J\ne U}q_J(w_J+q_J)^{w_J-1}.}
\]

If an in-arborescence toward a fixed unit is chosen uniformly, then, *jointly across all non-top classes* \(J\), the numbers \(B_J\) of arcs exiting \(J\) to larger classes are independent, with

\[
\boxed{B_J\ \overset{d}{=}\ 1+\operatorname{Binomial}\left(w_J-1,\frac{q_J}{w_J+q_J}\right).}
\]

More precisely, for each class the target-class count vector is distributed as one compulsory draw from \(K>J\) with probabilities \(w_K/q_J\), plus \(w_J-1\) independent trials, each choosing a target \(K>J\) with probability \(w_K/(w_J+q_J)\), or choosing no exit with probability \(w_J/(w_J+q_J)\). These descriptions are about *class-level counts*, not independence of individual vertex parents.

## Assumptions and scope

The monoid is finite, associative and unital, but need not be commutative, inverse, regular or a transformation monoid. No auxiliary probabilistic distribution on the monoid is assumed. The \(\mathcal J\)-order is inclusion of two-sided principal ideals. All polynomial identities hold over \(\mathbb Z[\mathbf t,\mathbf z]\); specializations can therefore be made over any commutative coefficient ring. The directed-tree convention is explicitly **toward** the root, as opposed to the opposite orientation sometimes used in the arborescence literature.

## Proof

**1. Top class.** In a finite monoid, the \(\mathcal J\)-class of \(1\) consists precisely of the units. Indeed, \(1=xay\) implies that \(xa\) has right inverse \(y\), hence is a unit in a finite monoid. Thus \(x\), and then \(a\), is a unit. Every principal ideal is contained in \(M=M1M\), so this class is greatest. The divisibility condition \(a\in MbM\) is equivalent to \(MaM\subseteq MbM\). Consequently, arcs within a class go in both directions, arcs between classes go strictly upward, and incomparable classes have no arcs. As a unit cannot reach a nonunit along directed arcs, no nonunit can root an in-arborescence.

**2. Local-to-global decomposition.** Fix a unit root \(e\). Each vertex outside \(e\) chooses one outgoing arc. Any directed cycle of selected arcs must remain entirely within a single \(\mathcal J\)-class: strict upward class changes cannot form a cycle. Conversely, if every non-top class has no internal directed cycle and at least one arc to a higher class, and the top class forms an in-arborescence toward \(e\), then all vertices eventually reach \(e\). Hence the admissible choices in different classes are independent *combinatorially* and the enumerator factors as their generating polynomials.

**3. A single non-top class.** Fix \(J\ne U\), and abbreviate \(w=w_J\), \(t=t_J\), \(Q=Q_J(\mathbf z)\). Exactly \(k\) of its \(w\) labelled vertices, for some \(1\le k\le w\), send their arcs to higher classes. Choose their locations in \(\binom wk\) ways. Their remaining internal arcs form a rooted directed forest with these \(k\) designated roots. The complete-graph rooted-forest formula gives \(k w^{w-k-1}\) such forests for \(1\le k<w\), and one for \(k=w\). The latter also equals the formula under the natural integer interpretation. Each forest contributes \(t^{w-k}\); each external arc independently contributes the sum of its target weights \(Q\). Therefore the class enumerator equals

\[
\sum_{k=1}^{w}\binom wk k w^{w-k-1}t^{w-k}Q^k
=\sum_{k=1}^{w}\binom{w-1}{k-1}w^{w-k}t^{w-k}Q^k
=Q(wt+Q)^{w-1}.
\]

The forest formula can be proved without assuming any arborescence result for semigroups: remove the \(k\) selected roots' rows and columns from the Laplacian \(wI-\mathbf 1\mathbf 1^{\mathsf T}\) of the complete digraph. For \(k<w\), the minor has eigenvalues \(w\), with multiplicity \(w-k-1\), and \(k\), once. The all-minors matrix-tree theorem gives \(k w^{w-k-1}\); if \(k=w\), the unique empty forest is counted.

**4. Top class and multiplication.** The \(u\) units induce a complete bidirected graph. For a prescribed root \(e\), Cayley's formula gives \(u^{u-2}\) trees with \(u-1\) arcs (one tree when \(u=1\)). Multiplying this contribution by every independent non-top class contribution proves the first displayed factorization. Setting every variable equal to one proves the numerical count.

**5. Probability law.** Normalize the factorization by its value at all variables equal to one. For \(J\ne U\), write \(Q_J(\mathbf z)=\sum_{K>J}w_Kz_{JK}\) and \(q_J=Q_J(\mathbf 1)\). Its normalized factor is

\[
\frac{Q_J(\mathbf z)}{q_J}\left(\frac{w_J+Q_J(\mathbf z)}{w_J+q_J}\right)^{w_J-1}.
\]

This is precisely the probability generating function of the stated compulsory higher-class draw plus \(w_J-1\) independent categorical trials. The product across \(J\) proves independence of the *exit-count vectors*; setting all \(z_{JK}=s_J\) gives the shifted-binomial marginal laws.

## Verification

A standalone standard-library checker (`check.py`) independently constructs weighted directed Laplacians, computes their exact rational-elimination cofactors, enumerates small rooted functional digraphs to reject cycles, and compares against the product formula. It checks nine prescribed posets, weighted as well as unweighted, and derives the principal-ideal orders from the actual multiplication tables of the two-point full transformation monoid and the two-point symmetric inverse monoid. It also verifies the two-point Boolean meet-semilattice and an exact exit-count distribution. Running `python check.py` prints `GREEN_DIVISIBILITY_ARBORESCENCES_OK`.

For the full transformation monoid on two letters, the \(\mathcal J\)-class sizes are \(2,2\), giving \(A_e=8\). For the symmetric inverse monoid on two letters, the sizes are \(1,4,2\), giving \(A_e=2592\). For the four-element Boolean meet-semilattice, \(A_e=3\). More generally, the full transformation monoid on \(n\) letters has rank-\(r\) class size \(\binom nr r!\left\{\begin{smallmatrix}n\\r\end{smallmatrix}\right\}\), so the theorem supplies a closed product for every \(n\) using Stirling numbers of the second kind.

## Relationship to prior work

Yang, Shao and Zeng (arXiv:2611.13455v1, November 10, 2026) prove that every semigroup divisibility graph is the weighted blow-up of its Green \(\mathcal J\)-poset. Their theorem supplies the crucial edge description, but the paper's results concern component structure, reconstruction and saturation; it does not give the rooted in-arborescence class-enumerator or its exit-count probability law. The classical Cayley rooted-forest identity supplies the local forest counts. The general Kirchhoff-polynomial decomposition of Mihalák, Uznański and Yordanov studies arbitrary digraphs and does not specialize to a Green-class product or a class-exit probability law. The present formula combines the ideal-order structure with a classwise forest decomposition to obtain the full polynomial and stochastic independence. Thus the structural graph theorem and the counting result should not be confused.

## Limitations

The result treats finite monoids and arborescences toward a **specified** root, with edge weights constant on source/target Green-class pairs. It does not count unrooted trees, directed trees with arcs away from a root, individual edge-labelled Kirchhoff coefficients, or tree isomorphism types. The proof uses standard graph-enumeration principles; historical priority of the exact Green-class specialization is not claimed to be independently certified. A complete indexed-literature search cannot rule out an unindexed earlier formula. Computed examples only check finite instances; the proof above is the all-monoid argument.

## References

1. Xuan Yang, Yong Shao, Lingli Zeng, *Divisibility graphs of semigroups as weighted poset blow-ups*, arXiv:2611.13455v1, November 10, 2026. https://arxiv.org/abs/2611.13455
2. Matúš Mihalák, Przemysław Uznański, Pencho Yordanov, *Prime Factorization of the Kirchhoff Polynomial: Compact Enumeration of Arborescences*, arXiv:1507.07727, 2015. https://arxiv.org/abs/1507.07727
3. Arnon Avron and Nachum Dershowitz, *Cayley's formula: A page from the book* (rooted-forest enumeration). https://www.cs.tau.ac.il/~nachumd/papers/Cayley.pdf
