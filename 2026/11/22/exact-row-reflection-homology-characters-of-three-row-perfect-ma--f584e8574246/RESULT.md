# Exact row-reflection homology characters of three-row perfect-matching complexes

## Finding
Let \(G_n=P_3\mathbin{\square}P_{2n}\), where \(n\ge 1\), and let \(\Delta_n=\mathcal M_p(G_n)\) be its perfect-matching extendibility simplicial complex: vertices are edges of \(G_n\), and a set of edges is a face precisely when it is contained in a perfect matching. The involution \(\rho(r,j)=(2-r,j)\) interchanges the top and bottom rows. Its **reduced rational Lefschetz number** is
\[
\widetilde L(\rho;\Delta_n)=
\begin{cases}
0,&n\equiv1\pmod3,\\
1,&n\equiv2\pmod3,\\
-1,&n\equiv0\pmod3.
\end{cases}
\]
By Chandrakar--Chau--Goyal--Karki--Subhash's nonequivariant homotopy theorem, for \(n\ge2\) the only nonzero reduced rational homology is \(\widetilde H_{n-1}(\Delta_n;\mathbb Q)\cong\mathbb Q^{F_{n-1}}\), where \(F_1=F_2=1\) are the Fibonacci numbers. Consequently the exact row-reflection trace on this homology is
\[
 t_n=(-1)^{n-1}\widetilde L(\rho;\Delta_n),
\]
and its positive and negative eigenspace ranks are respectively
\[
 m_n^{\pm}=\frac{F_{n-1}\pm t_n}{2}.
\]
The rational reduced homology of the geometric quotient \(|\Delta_n|/\langle\rho\rangle\) is concentrated in degree \(n-1\), with rank \(m_n^+\). In particular this quotient is rationally acyclic for \(n=1,2,3\); the **first nonzero positive-degree quotient homology occurs at \(n=4\)**, and its rank is one. For \(n\ge4\) the quotient rank is positive and grows at the Fibonacci rate, while \(|t_n|\le1\).

## Assumptions and scope
The grid is the Cartesian graph of three rows and \(2n\) columns with unit horizontal and vertical edges. Perfect-matching extendibility, not the ordinary matching complex, defines \(\Delta_n\). The row involution acts on graph edges, hence simplicially on \(\Delta_n\). All homology is reduced unless otherwise indicated; all character and quotient statements use rational coefficients. An independent integral module decomposition or integral torsion classification of the quotient is not claimed.

## Proof
**Invariant simplex-orbits and their signs.** Fix the row order top, middle, bottom. Under \(\rho\), the two vertical edges in each column are exchanged, but share their middle-row endpoint; therefore neither can occur in a \(\rho\)-invariant matching. At every boundary between consecutive columns \(j\) and \(j+1\), an invariant simplex may contain the pair of top-and-bottom horizontal edges (symbol \(T_j\)), the fixed middle horizontal edge (symbol \(D_j\)), both, or neither. Write their forced horizontal-edge mask as \(s\in\{0,5,2,7\}\), in bit order top \(=1\), middle \(=2\), bottom \(=4\), and assign weights \(w(s)=1,-1,-1,1\), respectively.

For an invariant face with \(a\) selected two-edge orbits and \(b\) selected fixed-edge orbits, its simplex dimension is \(2a+b-1\). The orientation sign of \(\rho\) is \((-1)^a\). Its summand in the reduced Lefschetz alternating trace is therefore \(-(-1)^{a+b}\). This also holds for the empty face, interpreted in reduced degree \(-1\). Thus, if \(Q_n\) is the weighted sum \(\sum(-1)^{a+b}\) over *all invariant faces including the empty face*, then \(\widetilde L(\rho;\Delta_n)=-Q_n\).

**Exact matching-extension automaton.** A perfect matching of the rectangular grid is a domino tiling. In a particular column, let \(p\in\{0,\ldots,7\}\) encode the rows already covered by horizontal dominoes entering from the left, and \(q\) the rows covered by horizontal dominoes leaving to the right. There is a valid completion within the column exactly when
\[
 (p\mathbin{\&}q)=0
 \quad\text{and}\quad 7\mathbin{\oplus}(p\mathbin{|}q)\in\{0,3,6\},
\]
where \(\&\), \(\oplus\), and \(|\) denote bitwise AND, XOR, and OR. The three allowed complements mean no uncovered cells, or one of the two vertical adjacent pairs. For forced selected orbit-mask \(s\), only outgoing \(q\) containing the bits of \(s\) are permitted.

To detect *existence* of a completing tiling without double counting it, determinize this eight-mask nondeterministic rule. Start with the possible incoming-mask set \(S_0=\{0\}\). After a boundary symbol \(s\), replace a possible-mask set \(S\) by the union of all valid outgoing masks \(q\) over \(p\in S\), subject to \(q\supseteq s\). Exactly seven subsets are reachable. In the deterministic breadth-first order they are
\[
 \bigl(\{0\},\{1,4,7\},\{7\},\{0,3,6\},\varnothing,\{3,6\},\{1,4\}\bigr).
\]
Summing the four signed transitions produces the following **exact integer matrix** (rows are source states, columns target states):
\[
 A=\begin{pmatrix}
 0&1&-1&0&0&0&0\\
 0&0&0&1&0&-1&0\\
 1&0&0&0&-1&0&0\\
 0&1&-1&0&0&0&0\\
 0&0&0&0&0&0&0\\
 0&0&0&0&-1&0&1\\
 0&0&0&1&0&-1&0
 \end{pmatrix}.
\]
A possible-mask set is accepting if its elements include some \(p\) which completes the *last* column with outgoing mask zero. The accepting vector is
\[
 b=(0,1,1,0,0,0,1)^{\mathsf T}.
\]
For the \(2n-1\) internal column boundaries, each invariant extendible face is encoded by exactly one sequence of orbit choices, while deterministic set propagation records whether at least one tiling extends it. Hence, with \(e_0=(1,0,0,0,0,0,0)^{\mathsf T}\),
\[
 Q_n=e_0^{\mathsf T}A^{2n-1}b.
\]
Integer multiplication of the displayed matrix proves the exact identities
\[
 A^6b=b,\qquad
 e_0^{\mathsf T}Ab=0,\quad e_0^{\mathsf T}A^3b=-1,\quad e_0^{\mathsf T}A^5b=1.
\]
Thus \(Q_n\) has period three and values \(0,-1,1\) in residue classes \(n\equiv1,2,0\pmod3\). The asserted reduced Lefschetz formula follows. This is an all-length finite-state proof, not an extrapolation from examples.

**Homology representation and quotient.** For \(n\ge2\), use the published integral sphere-wedge classification of \(\Delta_n\) to concentrate the reduced Lefschetz trace in degree \(n-1\). Since \(\rho^2=1\), the rational eigenvalues are \(\pm1\). Their sum is \(t_n\), and their total dimension is \(F_{n-1}\), giving the two rank formulas. Barycentric subdivision removes simplicial inversions, and averaging over the order-two group gives \(\widetilde H_*(|\Delta_n|/\langle\rho\rangle;\mathbb Q)\cong\widetilde H_*(\Delta_n;\mathbb Q)^{\rho}\). The base cases follow from \(F_1=F_2=1\), \(F_3=2\), and \(t_2=t_3=-1,t_4=0\). For \(n\ge4\), \(F_{n-1}\ge2\) and \(|t_n|\le1\), so \(m_n^+>0\). For \(n=1\), the published theorem says \(\Delta_1\) is contractible.

## Verification
`CHECK.py` reconstructs the seven deterministic subset states from the local domino-tiling condition, verifies every entry of \(A\) and \(b\), the integer identity \(A^6b=b\), and the three base evaluations. As a separate cross-check it enumerates every perfect domino tiling of the \(3\times2n\) grids for \(1\le n\le8\), derives all invariant faces as subsets of those tilings, and directly evaluates their signed face sums. `EXPECTED.txt` is the reproducible stdout. Invoke `python CHECK.py` from the directory containing these files. The finite enumerations are independent checks only; the matrix identity proves the infinite-length result.

## Relationship to prior work
The November 13, 2026 preprint by Chandrakar, Chau, Goyal, Karki, and Subhash establishes the nonequivariant Fibonacci sphere-wedge classification of the same perfect-matching complexes. Its complete main-results section and concluding discussion contain no reflection character or invariant quotient-rank theorem. The 2026 note *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex* computes the special \(n=2\) row-reflection sign \(-1\), in agreement with the formula, but does not imply the statement for all \(n\). Results on the **ordinary** matching complex of a three-row grid calculate different simplicial objects and do not supply the character for this perfect-matching **subcomplex**. The present result is the new all-\(n\) equivariant refinement, proved by exact row-orbit extension rather than by a nonequivariant homotopy classification alone.

## Limitations
The reflection is specifically top/bottom row interchange, not end-to-end column reversal or the combined half turn; no full Klein-four representation or integral quotient homotopy type is claimed. The proof relies on the published sphere-wedge theorem for the degree and total rank, while its new character calculation is self-contained. Search and full-text comparison cannot rule out equivalent unindexed or unpublished results. No independent review has been conducted.

## References
1. H. Chandrakar, T. Chau, S. Goyal, R. Karki, and B. Subhash, *Perfect Matching Complexes of 3×2n Grid Graph*, first posted November 13, 2026, arXiv:2611.18058, https://arxiv.org/abs/2611.18058.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, first posted July 8, 2024, arXiv:2407.05809, https://arxiv.org/abs/2407.05809 (two-row comparison).
3. *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex*, mathematical note, 2026 (\(n=2\) comparison).
4. *Orthogonal-reflection Lefschetz formulas for 3×n grid matching complexes*, mathematical note, 2026 (ordinary matching-complex comparison).
