# Finite topological-evidence models have a least dense specialization core
## Finding

Let
\[
S=(X,\le,\mathcal T)
\]
be a finite up-space with nonempty \(X\): \(\le\) is a preorder and every open set in \(\mathcal T\) is an up-set for \(\le\). Let \(R\) be the specialization preorder of \(\mathcal T\):
\[
xRy
\quad\Longleftrightarrow\quad
\forall U\in\mathcal T\,(x\in U\Rightarrow y\in U).
\]

Then:

1. \(\mathcal T\) is automatically an Alexandrov topology and is exactly the family of \(R\)-up-sets;
2. \(\le\subseteq R\);
3. if \(M_R\) denotes the union of all maximal \(R\)-equivalence classes, then \(M_R\) is the unique least dense open set.

Consequently, in the intuitionistic topological evidence semantics of Sedlár, a proposition \(P\subseteq X\) is coherently justified,
\[
\text{there exists a dense open }U\subseteq P,
\]
if and only if
\[
M_R\subseteq P.
\]
Thus on finite models coherent justification depends only on the maximal specialization classes, not on the full topology.

There is an exact chain classification. Fix
\[
C_n=\{0<1<\cdots<n-1\}.
\]
The \(\le\)-up-sets are the tails
\[
U_i=\{i,i+1,\ldots,n-1\}
\qquad(0\le i<n),
\]
together with
\[
U_n=\varnothing.
\]
Every subfamily of these tails containing \(U_0\) and \(U_n\) is a topology, so there are exactly
\[
2^{n-1}
\]
up-space topologies on the fixed labelled chain.

For each such topology, the least dense open set is its least nonempty open tail. Hence exactly \(n\) distinct coherent-justification operators occur, one for each terminal interval
\[
B_r=\{n-r,\ldots,n-1\},
\qquad 1\le r\le n.
\]
The number of topologies whose coherent-justification core is \(B_r\) is
\[
\begin{cases}
2^{n-r-1},&1\le r<n,\\
1,&r=n.
\end{cases}
\]

## Assumptions and scope

Sedlár defines an up-space as a preorder equipped with a topology all of whose opens are up-sets, and interprets \(\Box\) as topological interior. The global modality \(\mathrm A\) expresses truth at all states. Proposition 2.9 identifies coherent justification of the truth set of \(\varphi\) with the existence of a dense open set contained in that truth set.

The finite theorem concerns the topology and the coherent-justification condition. It does not identify distinct up-space topologies modulo modal equivalence, and the count \(2^{n-1}\) is for a fixed labelled intuitionistic chain.

The specialization relation \(R\) can be strictly coarser than the original intuitionistic information order \(\le\); the finite result only forces the topology to be Alexandrov with respect to \(R\).

## Proof

Because \(X\) is finite, \(\mathcal T\subseteq\mathcal P(X)\) is finite. Therefore the intersection of an arbitrary subfamily of \(\mathcal T\) is the intersection of finitely many distinct opens and is open. Hence \(\mathcal T\) is Alexandrov.

For every Alexandrov topology, the topology is exactly the up-set topology of its specialization preorder. Thus
\[
\mathcal T=\mathcal T_R.
\]
Since every \(U\in\mathcal T\) is a \(\le\)-up-set, if \(x\le y\) and \(x\in U\), then \(y\in U\). By definition of specialization,
\[
x\le y\Rightarrow xRy,
\]
so
\[
\le\subseteq R.
\]

Let \(Q=X/{\sim_R}\) be the finite quotient poset of \(R\)-equivalence classes, and let \(M_R\) be the union of its maximal classes. Every class in \(Q\) lies below some maximal class, so for each \(x\in X\) there is \(m\in M_R\) with
\[
xRm.
\]
Therefore \(M_R\) is dense in the Alexandrov topology: the least open neighbourhood
\[
R[x]=\{y:xRy\}
\]
of every \(x\) meets \(M_R\).

The set \(M_R\) is also open. Indeed, if \(x\in M_R\) and \(xRy\), maximality of the class of \(x\) forces \(y\sim_R x\), hence \(y\in M_R\).

Now let \(U\) be any dense open set. For each maximal class \(C\), density implies
\[
U\cap C\ne\varnothing,
\]
because the least open neighbourhood of a point of \(C\) is exactly \(C\). If \(u\in U\cap C\), then \(U\), being an \(R\)-up-set, contains every point \(R\)-equivalent to \(u\). Hence
\[
C\subseteq U.
\]
This holds for every maximal class, so
\[
M_R\subseteq U.
\]
Thus \(M_R\) is the unique least dense open set.

Sedlár's coherent-justification condition is
\[
(\exists U\in\mathcal T)\,
(U\text{ dense and }U\subseteq P).
\]
Since every dense open contains \(M_R\), this implies \(M_R\subseteq P\). Conversely \(M_R\) itself is dense and open, so \(M_R\subseteq P\) suffices.

Now specialize to \(C_n\). Its up-sets are linearly ordered by inclusion:
\[
U_0\supset U_1\supset\cdots\supset U_n.
\]
Any subfamily containing \(U_0=X\) and \(U_n=\varnothing\) is automatically closed under arbitrary unions and finite intersections, because every nonempty collection of selected tails has a largest and a smallest member. The \(n-1\) intermediate tails can therefore be selected independently, proving the count
\[
2^{n-1}.
\]

The least nonempty selected tail is the least dense open and is some \(B_r=U_{n-r}\). If \(r=n\), no intermediate tail is selected, giving one topology. If \(r<n\), the tail \(U_{n-r}\) must be selected, every strictly smaller tail must be absent, and the \(n-r-1\) larger intermediate tails may be selected freely. Hence the multiplicity is
\[
2^{n-r-1}.
\]

## Verification

The proof is exact.

The bundled checker performs two independent finite tests. First, it enumerates every preorder on at most four labelled points, forms its Alexandrov up-set topology, computes maximal specialization classes, and verifies that their union is the least dense open set.

Second, for chains of sizes \(1\) through \(10\), it enumerates all candidate up-space topologies obtained by selecting intermediate tails. It checks that there are exactly \(2^{n-1}\), reconstructs the specialization preorder, computes the least dense open set, and verifies the multiplicity formula for each terminal-block size.

The computation is a consistency check only; the proof above establishes the theorem for every finite up-space and every finite chain.

## Relationship to prior work

Sedlár's 2026 paper introduces the non-classical topological evidence setting used here. It defines up-spaces, recalls the specialization preorder, notes that a general topology need not coincide with the Alexandrov topology generated by that preorder, and proves that coherent justification is expressible by the existence of a dense open support.

De Groot and Shillito's earlier work on intuitionistic \(\mathsf{iS4}\) emphasizes the same distinction: general up-spaces strictly extend bi-relational semantics because not every upset topology is Alexandrov. Their finite-model results may use relational models, but they do not state that every finite up-space itself collapses to its specialization preorder.

The present result isolates the finite boundary of that distinction and adds the least-dense-open theorem. On finite carriers, the genuinely topological freedom disappears: the topology is determined by a preorder, and coherent justification is exactly truth on all maximal specialization classes. On an intuitionistic chain this yields the exact \(2^{n-1}\) topology census and the distribution of the \(n\) possible coherent-justification cores.

## Limitations

The Alexandrov collapse is finite. Infinite up-spaces can have topologies strictly coarser than the Alexandrov topology of their specialization preorder, which is one of the motivations for the topological semantics.

The count \(2^{n-1}\) is specific to the fixed total intuitionistic order. For a general finite preorder, admissible topologies correspond to preorder extensions, whose enumeration is more complicated.

The theorem classifies coherent-justification cores, not full theories: different topologies with the same least dense open can still differ on \(\Box\)-formulas.

## References

[1] Igor Sedlár, “Non-classical Topological Evidence Logic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 691–710. arXiv:2606.31888. DOI:10.4204/EPTCS.447.39.

[2] Jim de Groot and Ian Shillito, “Intuitionistic S4 as a logic of topological spaces,” *Journal of Logic and Computation* 35(7) (2025), exae030. DOI:10.1093/logcom/exae030.
