# The fiber-swap homology characters of clique-doubled cycles

## Finding
For every integer \(n\ge5\), let \(G_n=C_n\circ K_2\) be the lexicographic graph product, and let \(X_n=\operatorname{Ind}(G_n)\). The vertex set of \(G_n\) is \(\{(i,c):i\in\mathbb Z/n,\ c\in\{0,1\}\}\); two distinct vertices are adjacent exactly when their first coordinates agree or are adjacent on \(C_n\). Let \(N_n=(C_2)^n\) independently swap the two vertices with each fixed first coordinate. For \(S\subseteq\mathbb Z/n\), write \(\chi_S(t)=(-1)^{\sum_{i\in S}t_i}\).

The complete degree-by-degree rational \(N_n\)-homology representation is as follows. When \(S=\varnothing\), the trivial-isotypic reduced homology is
\[
\widetilde H_q(X_n;\mathbb Q)_{\chi_\varnothing}\cong
\begin{cases}
\mathbb Q^2,&n\equiv0\pmod3,\ q=n/3-1,\\
\mathbb Q,&n\equiv1\pmod3,\ q=(n-4)/3,\\
\mathbb Q,&n\equiv2\pmod3,\ q=(n-2)/3,\\
0,&\text{otherwise}.
\end{cases}
\]
If \(S\ne\varnothing\) is not independent in \(C_n\), its isotypic homology vanishes. If \(S\ne\varnothing\) is independent, enumerate its \(r\) vertices in cyclic order and denote successive positive gaps by \(\delta_1,\ldots,\delta_r\), so \(\delta_j\ge2\), \(\sum_j\delta_j=n\), and for \(r=1\) the gap is \(n\). If any \(\delta_j\equiv1\pmod3\), the \(\chi_S\) homology vanishes. Otherwise it is one-dimensional in precisely the degree
\[
q=r-1+\sum_{j=1}^r\left\lfloor\frac{\delta_j-2}{3}\right\rfloor.
\]
Consequently every nontrivial linear character of the fiber-swap group occurs at most once, in a completely specified degree. This is a character-level refinement, not a new nonequivariant homotopy classification.

## Assumptions and scope
All simplicial chain complexes are augmented, including the empty simplex in degree \(-1\), and all representation statements use rational coefficients. For a simplicial complex containing only the empty face, its reduced augmented homology in degree \(-1\) is \(\mathbb Q\). The cycle is simple, with \(n\ge5\). Each occurrence and vanishing statement concerns every homological degree, not merely the Euler characteristic. The empty subset and singleton cyclic-gap conventions are essential.

## Proof
**Equivariant chain decomposition.** Every face of \(X_n\) chooses at most one color in each index of an independent subset \(A\) of \(C_n\). Order the first coordinates increasingly. If \(V_i=\mathbb Q\langle e_{i,0},e_{i,1}\rangle\), then in degree \(q\) the simplicial chain group is the direct sum of \(\bigotimes_{i\in A}V_i\) over all independent \(A\) of size \(q+1\); in degree \(-1\) it is \(\mathbb Q\). The factor corresponding to \(i\) has a \(+1\)-eigenvector \(p_i=(e_{i,0}+e_{i,1})/2\) and a \(-1\)-eigenvector \(m_i=(e_{i,0}-e_{i,1})/2\) under the local transposition. The simplicial augmentation sends \(p_i\) to \(1\) and \(m_i\) to \(0\). Thus every \(\chi_S\)-isotypic chain is spanned by independent \(A\supseteq S\), with \(m_i\) for \(i\in S\) and \(p_i\) for \(i\in A\setminus S\). Its differential deletes only a positive-eigenvector factor, using the ordinary oriented simplicial signs. If \(S\) is not independent, no such face exists. If \(S\) is independent, the possible \(A\setminus S\) are exactly the faces of the link \(L_S=\operatorname{Ind}(C_n-N_{C_n}[S])\). Orientation by moving the fixed \(S\)-factors to the front gives an isomorphism of chain complexes with a degree shift of \(|S|\) (and, if desired, a global boundary sign). Therefore
\[
\widetilde H_q(X_n;\mathbb Q)_{\chi_S}\cong\widetilde H_{q-|S|}(L_S;\mathbb Q),
\]
where for \(S=\varnothing\) this is the usual augmented cycle independence-complex chain complex. In particular the decomposition respects the group action, rather than merely splitting Betti numbers.

**Path recurrence.** For the path \(P_m\) on \(m\) vertices, with \(P_0\) empty, the classical vertex-deletion cofibration at the second vertex gives \(\operatorname{Ind}(P_m)\simeq\Sigma\operatorname{Ind}(P_{m-3})\) for \(m\ge3\). Indeed deleting that vertex leaves an isolated endpoint, making the deletion complex contractible, and its closed-neighborhood deletion is \(P_{m-3}\). The initial independence complexes are \(\operatorname{Ind}(P_0)=\{\varnothing\}\), \(\operatorname{Ind}(P_1)\) contractible and \(\operatorname{Ind}(P_2)\simeq S^0\). This yields
\[
\operatorname{Ind}(P_{3k})\simeq S^{k-1},\quad
\operatorname{Ind}(P_{3k+1})\simeq *,\quad
\operatorname{Ind}(P_{3k+2})\simeq S^{k}\quad(k\ge0),
\]
under the augmented convention at \(k=0\) for the first case.

**Cyclic gaps.** Let \(S\ne\varnothing\) be independent. Each cyclic gap of size \(\delta\) between consecutive chosen indices has \(\max(\delta-3,0)\) vertices outside the closed neighborhood of \(S\). These vertices form a path; gaps are disjoint. Therefore \(L_S\) is the join of the path independence complexes of lengths \(\ell_j=\max(\delta_j-3,0)\). The path recurrence makes the join acyclic if and only if some \(\delta_j\equiv1\pmod3\). Otherwise each path contributes a sphere with augmented degree \(\lfloor(\delta_j-2)/3\rfloor-1\), using \(S^{-1}\) for an empty path. Their join has reduced homology one-dimensional in degree \(\sum_j\lfloor(\delta_j-2)/3\rfloor-1\). After the shift by \(r=|S|\), this is exactly the displayed degree. No other degree remains.

**Empty character.** For \(S=\varnothing\), the link is \(\operatorname{Ind}(C_n)\). Delete one cycle vertex and use its link: \(\operatorname{Ind}(P_{n-3})\to\operatorname{Ind}(P_{n-1})\to\operatorname{Ind}(C_n)\). The path calculation shows that for \(n\equiv0\pmod3\) the map is nullhomotopic for dimensional reasons, giving two spheres of dimension \(n/3-1\); for \(n\equiv1\pmod3\) the domain is contractible and the codomain is a sphere of dimension \((n-4)/3\); for \(n\equiv2\pmod3\) the codomain is contractible and the cofiber is a sphere of dimension \((n-2)/3\). This proves every remaining case.

## Verification
The standalone file `verify.py` reconstructs colored independent faces and computes full augmented simplicial boundary ranks over the prime field of order 101 for \(5\le n\le9\), independently comparing the total graded Betti numbers with the sums of the claimed character multiplicities. It also checks all \(2^n\) local-swap Lefschetz traces for \(5\le n\le8\), and selected traces for \(9\le n\le12\), against the direct fixed-face formula. The script checks the combinatorial link-chain indexing and outputs `VERIFY_OK`. These finite computations are corroboration, not a substitute for the uniform rational chain proof. The file `verify_output.txt` records the execution.

## Relationship to prior work
Carnero Bravo's *Polyhedral joins and graph complexes* (arXiv:2307.14321, initially public July 26, 2023), Theorems 20 and 28, determines an unsuspended **nonequivariant** homotopy decomposition for independence complexes of cycle lexicographic products. Its homotopy and consequent ordinary Betti-number results are not claimed as new here. Fu and Grbić's *Simplicial G-complexes and representation stability of polyhedral products* (arXiv:1803.11047, initially public March 29, 2018) establishes equivariant methods for polyhedral **products** under simplicial base-index permutations. Neither of these inspected results states a local \((C_2)^n\)-fiber-swap character criterion for the cycle lexicographic-product independence complex. The distinction between polyhedral products and polyhedral joins, and between base-index and within-fiber actions, matters: the present explicit link-chain decomposition and cyclic-gap criterion are the additional statements. Equivalent unpublished or unindexed work cannot be ruled out by a search.

## Limitations
The theorem gives rational \(N_n\)-module characters only; it does not classify integral \(N_n\)-lattices, extend to the full semidirect dihedral automorphism group, or provide a new homotopy decomposition. A standard general link-chain argument is used, and originality concerns its complete arithmetic character classification for this concrete graph family rather than the general idea of decomposing chain complexes into eigencharacters. The verification range is finite. No independent validation is claimed.

## References
- X. Fu and J. Grbić, *Simplicial G-complexes and representation stability of polyhedral products*, arXiv:1803.11047 (first public March 29, 2018), *Algebraic & Geometric Topology* 20 (2020), 215–238.
- A. Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first public July 26, 2023); Theorems 20 and 28 in version 3.
- D. Kozlov, classical path and cycle independence-complex homotopy recurrence; the needed recurrence and cycle argument are also supplied above.
