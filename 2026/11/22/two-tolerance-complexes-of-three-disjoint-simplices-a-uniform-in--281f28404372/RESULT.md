# Two-tolerance complexes of three disjoint simplices: a uniform integral sphere-wedge formula

## Finding

Let \(A_1,A_2,A_3\) be pairwise disjoint finite vertex sets with \(n_i=|A_i|\ge 2\). The initial simplicial complex \(K\) is the **disjoint union of three filled simplices**, \(\Delta(A_1)\sqcup\Delta(A_2)\sqcup\Delta(A_3)\), rather than the one-dimensional edge graph on these vertices. Let \(X=\mathcal T_2(K)\) consist of subsets \(\sigma\) satisfying \(|\sigma\setminus A_i|\le 2\) for at least one index \(i\). Set \(x=n_1-1\), \(y=n_2-1\), \(z=n_3-1\) and

\[
B_3=xy+yz+zx+2xyz,\qquad
B_4=\binom{x}{2}\binom{y}{2}+\binom{y}{2}\binom{z}{2}+\binom{z}{2}\binom{x}{2}.
\]

**Theorem.** For every triple of integers \(n_1,n_2,n_3\ge2\), there is an integral homotopy equivalence

\[
|X|\simeq\bigvee^{B_3}S^3\ \vee\ \bigvee^{B_4}S^4.
\]

Thus \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{B_3}\), \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{B_4}\), and all other reduced integral homology groups vanish. Both multiplicities are exact; there is no integral torsion. Two different dimensions occur precisely when at least two of the three vertex blocks have size at least three. For the infinite family \((n_1,n_2,n_3)=(2,3,m)\), \(m\ge3\), the multiplicities simplify to \(B_3=7m-5\) and \(B_4=\binom{m-1}{2}\); its first case is \(\bigvee^{16}S^3\vee S^4\).

## Assumptions and scope

All homotopy types are those of ordinary geometric realizations of finite abstract simplicial complexes, and all homology is over \(\mathbb Z\) unless a coefficient ring is indicated. An empty face belongs to every complex. For any vertex set \(A\), write \(D(A)\) for the discrete complex whose vertices are the elements of \(A\), and \(S(A)=\operatorname{sk}_1\Delta(A)\) for the complete one-skeleton on \(A\). These include the case \(|A|=2\), where \(S(A)\) is an interval. The join symbol is \(*\). All complexes are nonvoid and all three vertex blocks have cardinality at least two.

## Proof

**Step 1: a three-piece cover and exact intersections.** Define \(U_i=\{\sigma\subseteq A_1\sqcup A_2\sqcup A_3:|\sigma\setminus A_i|\le2\}\). Then \(X=U_1\cup U_2\cup U_3\), and \(U_i=\Delta(A_i)*\operatorname{sk}_1\Delta(A_j\sqcup A_k)\) for \(\{i,j,k\}=\{1,2,3\}\). In particular each \(U_i\) is contractible.

Put \(D_i=D(A_i)\), \(S_i=S(A_i)\) and \(B=D_1*D_2*D_3\). Checking the three integer block-intersection counts gives, without omitted cases,

\[
U_i\cap U_j=(S_i*S_j)\cup B\cup S_k\quad(\{i,j,k\}=\{1,2,3\}),
\]

and

\[
T=U_1\cap U_2\cap U_3=B\cup S_1\cup S_2\cup S_3.
\]

Indeed, for the pair intersection with counts \((r_i,r_j,r_k)\), the inequalities \(r_j+r_k\le2\) and \(r_i+r_k\le2\) give exactly: \(r_k=0\) and \(r_i,r_j\le2\); or \(r_k=1\) and \(r_i,r_j\le1\); or \(r_k=2\) and \(r_i=r_j=0\). The triple intersection imposes all three pair-sum inequalities; its faces select at most one vertex from every block, or up to two vertices from a single block and none from the others.

**Step 2: integral homology of the triple intersection.** A discrete set with \(n_i\) vertices has \(\widetilde H_0(D_i)=\mathbb Z^{n_i-1}\), so the integral join formula yields

\[
B\simeq\bigvee^{xyz}S^2.
\]

In particular \(B\) is path-connected and simply connected, with \(H_2(B)=\mathbb Z^{xyz}\). Attach each graph \(S_i\) to \(B\) along its discrete vertex set \(D_i\). Since these attachments add only one-dimensional cells, they preserve \(H_2(B)\) integrally. Moreover, the \(\binom{n_i}{2}\) edges of \(S_i\), each connecting vertices already connected in \(B\), create independent degree-one loops. It follows that

\[
H_2(T)=\mathbb Z^{xyz},\qquad
H_1(T)=\bigoplus_{i=1}^3\mathbb Z^{\binom{n_i}{2}}.
\]

No homology of \(T\) occurs above degree two.

**Step 3: integral homology of every pair intersection.** Fix \(i<j\), with remaining index \(k\), and set \(A=S_i*S_j\). The complete one-skeleton has \(\widetilde H_1(S_i)=\mathbb Z^{\binom{n_i-1}{2}}\); it is connected even when \(n_i=2\). The join formula therefore makes \(A\) two-connected, with

\[
H_3(A)=\mathbb Z^{\binom{n_i-1}{2}\binom{n_j-1}{2}};
\]

its other positive homology groups vanish. The intersection \(A\cap B=D_i*D_j\) is the complete bipartite graph, with \(H_1(A\cap B)=\mathbb Z^{(n_i-1)(n_j-1)}\) and trivial higher homology. The integral Mayer–Vietoris exact sequence for \(Y=A\cup B\) gives

\[
H_3(Y)=H_3(A),\qquad
0\longrightarrow H_2(B)\longrightarrow H_2(Y)\longrightarrow
H_1(D_i*D_j)\longrightarrow0,\qquad H_1(Y)=0.
\]

The quotient on the right is free; hence the injection \(H_2(B)\hookrightarrow H_2(Y)\) is **primitive and split over \(\mathbb Z\)**. Consequently

\[
H_2(Y)=\mathbb Z^{(n_i-1)(n_j-1)n_k}.
\]

Finally \(U_i\cap U_j=Y\cup S_k\), with \(Y\cap S_k=D_k\). Attaching \(S_k\) along its vertices adds no cells of dimension greater than one, and therefore preserves degree-two and degree-three homology. It contributes \(\binom{n_k}{2}\) new first-homology generators, yielding

\[
\begin{aligned}
H_1(U_i\cap U_j)&=\mathbb Z^{\binom{n_k}{2}},\\
H_2(U_i\cap U_j)&=\mathbb Z^{(n_i-1)(n_j-1)n_k},\\
H_3(U_i\cap U_j)&=\mathbb Z^{\binom{n_i-1}{2}\binom{n_j-1}{2}}.
\end{aligned}
\]

Every pair intersection is path-connected and simply connected before attaching its third-block graph, and has no homology above degree three.

**Step 4: the two crucial integral incidence maps.** Under inclusion \(T\hookrightarrow U_i\cap U_j\), the \(H_1(T)\)-summand indexed by block \(k\) maps isomorphically onto \(H_1(U_i\cap U_j)\). Its summands indexed by \(i,j\) map to zero, because they lie in the simply connected \(S_i*S_j\), using connecting paths entirely within \(D_i*D_j\). Thus the signed Čech differential

\[
H_1(T)\longrightarrow\bigoplus_{i<j}H_1(U_i\cap U_j)
\]

is an integral isomorphism: after ordering by omitted block it is a diagonal matrix with signs \(\pm1\).

Also \(H_2(T)=H_2(B)\), and each of its three inclusion maps to \(H_2(U_i\cap U_j)\) is the primitive direct-summand inclusion proved in Step 3. Hence the signed map

\[
H_2(T)\longrightarrow\bigoplus_{i<j}H_2(U_i\cap U_j)
\]

is split-injective. Its cokernel is torsion-free, of rank

\[
\sum_{i<j}(n_i-1)(n_j-1)n_k-xyz
=xy+yz+zx+2xyz=B_3.
\]

**Step 5: the cover spectral sequence.** Apply the integral Mayer–Vietoris spectral sequence of the three-subcomplex cover; the first page has \(E^1_{p,q}=\bigoplus_{|I|=p+1}H_q(U_I)\) and homological total degree \(p+q\), for \(0\le p\le2\). The contractible \(U_i\) have no positive-degree homology. The first-homology map of Step 4 eliminates the potential degree-two contribution. The primitive second-homology map yields the free group of rank \(B_3\) in degree three. The degree-three groups of pair intersections survive in degree four, summing to rank

\[
\sum_{i<j}\binom{n_i-1}{2}\binom{n_j-1}{2}=B_4.
\]

Every nonempty intersection is connected, so the row \(q=0\) is the augmented chain complex of a filled two-simplex and contributes only ordinary \(H_0\). There are no other surviving positive-degree entries or higher differentials: the only possible sources in the triple column are already zero after the two incidence maps. Therefore \(H_1(X)=H_2(X)=0\), \(H_3(X)=\mathbb Z^{B_3}\), \(H_4(X)=\mathbb Z^{B_4}\), and higher homology vanishes, with no integral extensions or torsion.

**Step 6: from homology to actual homotopy type.** The three contractible \(U_i\) and all their nonempty intersections are connected, and their nerve is a filled two-simplex. Generalized van Kampen gives \(\pi_1(X)=0\). Together with \(H_2(X)=0\), the degree-two Hurewicz theorem gives \(\pi_2(X)=0\).

The homotopy colimit of the intersection diagram models the union of a simplicial-subcomplex cover. Replacing its three contractible singleton-index objects \(U_i\) by points is an objectwise weak equivalence. Pair intersections have simplicial dimension at most three, while \(T\) has dimension at most two. The diagram's homotopy colimit therefore gives a CW model of dimension at most four (pair intersections add at most one parameter, the triple intersection two). A two-connected CW complex of dimension at most four with free homology only in dimensions three and four is a wedge of three- and four-spheres: Hurewicz maps \(\pi_3\to H_3\) isomorphically, the low-dimensional Whitehead exact sequence makes \(\pi_4\to H_4\) surjective, and maps of spheres representing respective integral bases give a homology equivalence from the stated wedge. This is a homotopy equivalence by the simply-connected Whitehead theorem. The theorem follows. \(\square\)

## Verification

The complete independent finite face and modular-boundary checker is included as `CHECK.py`, with its actual output in `CHECK_OUTPUT.txt`. To reproduce: run `python3 CHECK.py` using Python 3.8 or later; no third-party packages are required. For block sizes \((2,2,2)\), \((2,3,3)\), \((2,3,4)\), \((3,3,3)\), \((3,3,4)\), and \((4,4,4)\), it enumerates every face (not only facets), constructs each signed simplicial boundary matrix, checks all ranks modulo two, additionally checks ranks modulo three and five for the first four profiles, and compares Euler characteristics and all Betti ranks to the formulas. An auxiliary exact integer Smith-normal-form check of \((2,3,3)\) and \((3,3,3)\) was also carried out, finding only unit nonzero diagonal factors; its code, results and recorded output are in `INTEGRAL_CHECK.py`, `INTEGRAL_CHECK.txt`, and `INTEGRAL_CHECK_OUTPUT.txt` (optional SymPy 1.12+ dependency). The proof of arbitrary block sizes is Steps 1–6; numerical tests cannot certify infinite ranges or all prime torsion.

## Relationship to prior work

Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers* (arXiv:2611.14384v1, first posted 10 November 2026), proves collapsibility and Leray bounds for chordal graphs and, in particular, unions of tolerance balls; Section 4, Theorem 4.2 and Corollary 4.3 give an upper bound but do not identify these homotopy types or their two Betti multiplicities. Kim and Lew, *Leray Numbers of Tolerance Complexes* (Combinatorica 43 (2023), DOI below), establish the tolerance construction and homological bounds, including a sharp two-block sphere example. Their results do not state the present three-block integral homotopy classification.

A previously calculated special case with \((n_1,n_2,n_3)=(3,3,3)\) has type \(\bigvee^{28}S^3\vee\bigvee^3S^4\); that finite case is **not** claimed as new. The present assertion is the uniform classification for arbitrary three sizes, its splitting proof with primitive integral maps, and the mixed-dimensional threshold. The two-block classifications and one-tolerance classifications concern different domains and do not imply the stated formula for three disjoint **filled** simplices at tolerance two.

## Limitations

Only three disjoint filled simplices and tolerance exactly two are treated, with every block of size at least two. The theorem asserts ordinary integral homotopy type, not a symmetric-group-equivariant equivalence or full attaching-map data for a chosen triangulation. No result is claimed for four or more blocks, other tolerance parameters, or general chordal graphs. Priority assessments are provisional and do not certify absence of unindexed equivalent literature; independent mathematical review has not been performed.

## References

1. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384v1 (10 November 2026), https://arxiv.org/html/2611.14384v1 .
2. M. Kim and A. Lew, *Leray Numbers of Tolerance Complexes*, *Combinatorica* **43** (2023), 985–1006, https://doi.org/10.1007/s00493-023-00044-5 .
3. Standard integral Mayer–Vietoris and join theorems, Hurewicz and Whitehead theorems, and the Čech/Mayer–Vietoris spectral sequence of a finite simplicial cover are invoked with their usual integral formulations.
