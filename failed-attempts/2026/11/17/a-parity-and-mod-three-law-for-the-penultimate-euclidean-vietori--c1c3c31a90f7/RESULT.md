# A parity and mod-three law for the penultimate Euclidean Vietoris–Rips complexes of regular antiprisms

## Finding
For each integer \(n\ge4\), let \(A_n\) be the vertex set of the **unit-edge regular \(n\)-gonal antiprism**, equipped with ordinary ambient Euclidean distance. Let \(a_n\) be its second-largest distinct intervertex distance and \(b_n\) its largest. Its inclusive Vietoris–Rips complex at the penultimate distance has the following **integral homotopy classification**:
\[
\operatorname{VR}_{\le a_n}(A_n)\simeq
\begin{cases}
S^{n-1},&n\text{ odd},\\
S^{2n/3-1}\vee S^{2n/3-1},&n\equiv0\pmod6,\\
S^{(2n-2)/3},&n\equiv4\pmod6,\\
S^{(2n-4)/3},&n\equiv2\pmod6.
\end{cases}
\]
The squared distance thresholds are exactly
\[
\begin{aligned}
 n\text{ odd}:\quad&a_n^2=\frac1{4\sin^2(\pi/(2n))},&\quad b_n^2&=a_n^2+1;\\
 n\text{ even}:\quad&a_n^2=\frac1{\sin^2(\pi/n)},&\quad b_n^2&=a_n^2+1-\frac1{2\cos^2(\pi/(2n))}.
\end{aligned}
\]
In fact, for odd \(n\) the penultimate complex is **simplicially isomorphic** to the boundary of the \(n\)-dimensional cross-polytope. For even \(n\) it is **simplicially isomorphic** to the ordinary independence complex \(\operatorname{Ind}(C_{2n})\) of a single \(2n\)-cycle. For every \(a_n\le r<b_n\), the complex is unchanged, and for \(r\ge b_n\) it is a full simplex, hence contractible. Thus these are the exact last noncontractible stages and exact death thresholds; earlier stages and their persistence maps are not classified.

## Assumptions and scope
Write \(\alpha=\pi/(2n)\), \(R=1/(2\sin(\pi/n))\), and \(h>0\) with
\[
h^2=1-4R^2\sin^2\alpha=1-\frac1{4\cos^2\alpha}.
\]
There are precisely \(2n\) vertices indexed modulo \(2n\):
\[
v_j=\bigl(R\cos(\pi j/n),\ R\sin(\pi j/n),\ (-1)^j h/2\bigr),\qquad 0\le j<2n.
\]
Same-layer rim edges and successive unlike-layer edges have Euclidean length one. This defines the convex uniform antiprism for every \(n\ge4\); the shape uses chordal Euclidean distance, **not** shortest-path distance on its one-skeleton. The inclusive complex has a simplex on every nonempty set of vertices whose pairwise Euclidean distances are at most \(r\). The penultimate value means the second-largest **distinct** distance, and both endpoint equalities use the inclusive convention.

## Proof
**Step 1: Exact metric shells.** Let \(k\in\{1,\ldots,n\}\) be the smaller cyclic index separation between two vertices. Their squared Euclidean distance depends only on \(k\) and is
\[
q_k=4R^2\sin^2(k\alpha)+\begin{cases}0,&k\text{ even},\\h^2,&k\text{ odd}.\end{cases}
\]
The first term is strictly increasing for \(1\le k\le n\), so among separations of a fixed parity the distances strictly increase with \(k\). Set \(t=4R^2\sin^2\alpha=1/(4\cos^2\alpha)\) and note \(h^2=1-t\).

**Step 2: Odd polygon order.** If \(n\) is odd, the largest odd-parity shell is \(q_n\), and the largest even-parity shell is \(q_{n-1}\). Direct subtraction gives \(q_n-q_{n-1}=h^2+t=1>0\). Hence **exactly** the \(n\) pairs \(\{j,j+n\}\), indexed once by \(0\le j<n\), realize the largest distance. The runner-up is \(q_{n-1}\): by monotonicity it suffices to compare \(q_{n-1}\) and \(q_{n-2}\), and
\[
q_{n-2}=4R^2\cos^2(2\alpha)+h^2=4R^2-1+1-t=4R^2\cos^2\alpha=q_{n-1}.
\]
Using \(\sin(2\alpha)=2\sin\alpha\cos\alpha\) gives \(q_{n-1}=1/(4\sin^2\alpha)\), proving the stated thresholds. At the inclusive penultimate radius all edges are present except a perfect matching of \(n\) disjoint forbidden pairs. The clique complex of the allowed graph is the join of \(n\) copies of \(S^0\), the cross-polytope boundary \(S^{n-1}\).

**Step 3: Even polygon order.** If \(n\) is even, the largest odd-parity shell is \(q_{n-1}\), and the largest even-parity shell is \(q_n\). Their difference is
\[
q_{n-1}-q_n=h^2-t=1-2t=1-\frac1{2\cos^2\alpha}>0
\]
because \(0<\alpha\le\pi/8\) implies \(\cos^2\alpha>1/2\). It remains to prove that \(q_n\) is **second-largest**, rather than some smaller odd separation. By parity monotonicity we need only check \(q_n>q_{n-3}\). The triple-angle formula gives \(\sin(3\alpha)/\sin\alpha=3-4\sin^2\alpha>2\), while \(t=1/(4\cos^2\alpha)\ge1/4\); thus
\[
q_n-q_{n-3}=t\left(1+\left(\frac{\sin(3\alpha)}{\sin\alpha}\right)^2\right)-1>\frac54-1>0.
\]
Consequently \(q_n=4R^2=1/\sin^2(\pi/n)\) is the runner-up. The sole forbidden distance shell consists of index separations \(n-1\), i.e. the undirected edges \(\{j,j+(n-1)\}\) modulo \(2n\). Since \(\gcd(n-1,2n)=1\) for even \(n\), these edges form **one** cycle of length \(2n\), not several disjoint cycles. The inclusive penultimate Rips complex is therefore exactly \(\operatorname{Ind}(C_{2n})\).

**Step 4: Integral homotopy and the endpoint.** The classical cycle independence-complex computation (Kozlov; see Adamaszek) gives
\[
\operatorname{Ind}(C_m)\simeq
\begin{cases}
S^{k-1}\vee S^{k-1},&m=3k,\\
S^{k-1},&m=3k+1,\\
S^k,&m=3k+2.
\end{cases}
\]
It follows from the suspension relation \(\operatorname{Ind}(C_m)\simeq\Sigma\operatorname{Ind}(C_{m-3})\) and the elementary initial cases \(m=3,4,5\), respectively three isolated vertices, two disjoint edges, and a five-cycle. Substitute \(m=2n\) to obtain the three even-order residue cases. The largest distance is attained at the forbidden pairs described above; at radius \(b_n\) those final edges appear and the flag complex becomes a simplex. All assertions follow for every integer \(n\ge4\).

## Verification
The standalone `verify.py` reconstructs the Euclidean coordinates and pair distances for every \(4\le n\le60\), checks the analytic shell values, and confirms the exact forbidden-pair graph by a separate coordinate calculation. For \(4\le n\le9\), it exhaustively enumerates every independent face and computes reduced mod-two Betti ranks from its simplicial boundary matrices, checking the formula dimension by dimension. Run `python3 verify.py`; it must terminate with `VERIFY_OK`. This finite verification is supporting evidence, **not** a substitute for Steps 1–4, which prove all parameter cases and integral homotopy types.

## Relationship to prior work
Saleh, Titz Mite, and Witzel classify the vertex Rips complexes of the five Platonic solids and explicitly identify Archimedean solids as a possible extension. Their work does not contain antiprism families. Adamaszek reports the classical Kozlov cycle independence-complex homotopy recurrence, used here as a credited ingredient. Adams, Chowdhury, Jaffe, and Sibanda study the **planar boundary** of a regular polygon rather than the two-layer, three-dimensional antiprism vertex metric, so their results do not imply the metric-shell classification here.

A related earlier finite calculation treats the full Euclidean filtration of the regular **hexagonal** antiprism and covers its \(n=6\) instance; the present theorem does not claim that special case as independently new. The new statement is the exact **uniform infinite-family** parity distinction, the farthest-pair perfect-matching versus Hamiltonian-cycle dichotomy, the sharp analytical distance thresholds, and the resulting mod-three topological law for all even orders. Related finite graph-metric results on antiprisms or other polyhedra use a different distance function. An analogous statement under different terminology or unindexed work remains possible.

## Limitations
Only the penultimate stage and subsequent contractible stage are classified, **not** the full filtration, earlier Betti numbers, inclusion maps into the penultimate stage, equivariant homotopy actions, or other geometric scalings beyond the unit-edge normalization. The homotopy conclusion uses a known published classification of independence complexes of ordinary cycles; that classification is not original to this result. Search evidence does not logically establish universal originality.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28, primary MSC 55N31, https://arxiv.org/pdf/2302.14388.
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250v1, first public 2011-06-30, https://arxiv.org/pdf/1106.6250; cites the Kozlov ordinary-cycle recurrence.
3. H. Adams, S. Chowdhury, A. Q. Jaffe, and B. Sibanda, *Vietoris–Rips complexes of regular polygons*, arXiv:1807.10971v1, first public 2018-07-28, https://arxiv.org/pdf/1807.10971.
