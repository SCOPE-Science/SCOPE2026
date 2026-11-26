# A six-periodic mirror character for three-row perfect-matching complexes

## Finding
Let \(G_n=P_3\square P_{2n}\) be the Cartesian grid with three rows and \(2n\) columns, and let \(X_n=\mathcal M_p(G_n)\) be its simplicial perfect-matching complex: vertices are grid edges and faces are edge subsets extendable to a perfect matching. Let \(u\) reflect the top and bottom rows while fixing all columns. For every integer \(n\ge2\), the integral reduced homology of \(X_n\) is concentrated in degree \(n-1\), where it has rank \(F_{n-1}\) (the known nonequivariant theorem of Chandrakar, Chau, Goyal, Karki, and Subhash). The new assertion is that \(u\) has the following complete rational top-homology character:

\[
\operatorname{tr}\bigl(u_*\mid\widetilde H_{n-1}(X_n;\mathbb Q)\bigr)
=\begin{cases}
1,&n\equiv0,5\pmod6,\\
0,&n\equiv1,4\pmod6,\\
-1,&n\equiv2,3\pmod6.
\end{cases}
\]

Consequently, the actual geometric reflection quotient has rational reduced homology only in degree \(n-1\), with
\[
\dim_{\mathbb Q}\widetilde H_{n-1}(|X_n|/\langle u\rangle;\mathbb Q)
=\frac{F_{n-1}+\operatorname{tr}(u_*)}{2}.
\]
In particular the quotient is rationally acyclic in all positive degrees for \(n=2,3\), while its top rational Betti number is positive for every \(n\ge4\). Here \(F_1=F_2=1\), and the theorem does not assert an integral quotient homotopy classification.

## Assumptions and scope
All graphs are finite, simple, and **Cartesian** products. Number rows \(0,1,2\) from top to bottom and columns \(1,\ldots,2n\). A grid edge is a vertex of the perfect-matching complex precisely if it occurs in some full domino tiling; a set of such edges is a simplex if some full domino tiling contains all of them. The involution sends row \(r\) to row \(2-r\), preserving columns. All quotients refer to genuine geometric realizations, not vertex-orbit quotients of abstract complexes. The nonequivariant wedge-of-spheres theorem is used with explicit attribution; its proof and its Betti numbers are not claimed as new.

## Proof
**1. Reduction to fixed invariant simplices.** Write \(L=2n\). Under \(u\), each vertical edge in a column is exchanged with the other vertical edge in that column. Since those edges share the middle-row vertex, no invariant simplex contains that orbit. At each horizontal boundary \(j\in\{1,\ldots,L-1\}\), the only possible invariant edge-orbits are the two-element orbit \(T_j\) of top- and bottom-row horizontal edges, and the one-element orbit \(M_j\) of the middle-row horizontal edge. Thus every invariant simplex is uniquely described by a word of \(L-1\) subsets of \(\{T_j,M_j\}\); it is a simplex exactly when all compulsory edges in the word extend to a perfect matching.

For the oriented simplicial Lefschetz sum, a selected fixed singleton contributes \(-1\) to \((-1)^{|\sigma|}\operatorname{sgn}(u|_\sigma)\). A selected transposed pair also contributes \((-1)^2(-1)=-1\). Therefore, if \(W_L\) denotes the signed sum over all extendable invariant-simplex words, including the empty word, then
\[
W_L=\sum_{\substack{\sigma\in X_n\\u\sigma=\sigma}}
(-1)^{|\sigma|}\operatorname{sgn}(u|_\sigma)
=\sum_{\text{extendable words}}(-1)^{\#\text{ selected orbits}}.
\]
The empty simplex is included exactly once.

**2. Exact seven-state completion transfer.** Encode occupied rows at a column boundary by a three-bit mask in \(\{0,\ldots,7\}\), using top, middle, bottom as bits \(1,2,4\). If \(a\) is the mask occupied from the left and \(b\) the mask occupied by horizontal edges leaving to the right, the remaining vertices must be paired by internal vertical edges. Consequently, a one-column transition is possible **if and only if**
\[
 a\mathbin{\&}b=0,\qquad 7\mathbin{\oplus}a\mathbin{\oplus}b\in\{0,3,6\},
\]
where \(\&\) and \(\oplus\) mean bitwise AND and XOR. The four compulsory-edge choices at a boundary have required outgoing masks and signed weights
\[
(0,+1),\quad(5,-1),\quad(2,-1),\quad(7,+1).
\]
For a set \(S\) of possible incoming masks and a required outgoing mask \(x\), define \(\Phi_x(S)\) to be the set of all \(b\) for which there exists \(a\in S\) with a one-column transition \(a\to b\) and \(b\mathbin{\&}x=x\). Crucially, this is **determinization**: a selected word is counted just once even if several tilings extend it.

Starting from \(S_0=\{0\}\), exactly seven states are reachable. In breadth-first order, scanning compulsory choices as above, they are
\[
\{0\},\ \{1,4,7\},\ \{7\},\ \{0,3,6\},\ \varnothing,\ \{3,6\},\ \{1,4\}.
\]
Summing the four signed outgoing transitions yields the integral matrix
\[
M=\begin{pmatrix}
0&1&-1&0&0&0&0\\
0&0&0&1&0&-1&0\\
1&0&0&0&-1&0&0\\
0&1&-1&0&0&0&0\\
0&0&0&0&0&0&0\\
0&0&0&0&-1&0&1\\
0&0&0&1&0&-1&0
\end{pmatrix},\qquad
 t=(0,1,1,0,0,0,1)^{\mathsf T}.
\]
The terminal vector marks states admitting completion of the last column with no rightward edges. Therefore
\[
W_L=e_1^{\mathsf T}M^{L-1}t.
\]
Direct exact integer multiplication gives \(M^8=M^2\). Accordingly \(W_{L+6}=W_L\) for every even \(L\ge4\). Direct evaluation at \(L=2,4,6,8\) gives respectively \(0,-1,1,0\). Thus
\[
W_{2n}=\begin{cases}1,&n\equiv0\pmod3,\\0,&n\equiv1\pmod3,\\-1,&n\equiv2\pmod3.\end{cases}
\]
The small case \(L=2\) is included by direct evaluation rather than by extending the matrix-power identity to an unjustified exponent.

**3. Lefschetz character and quotient.** The known theorem gives, for \(n\ge2\), no reduced homology outside degree \(n-1\). The *augmented* oriented Lefschetz sum is \(-W_{2n}\), since the empty face has chain degree \(-1\). Thus
\[
(-1)^{n-1}\operatorname{tr}(u_*\mid\widetilde H_{n-1})=-W_{2n},\quad
\operatorname{tr}(u_*)=(-1)^nW_{2n}.
\]
This is the asserted six-residue trace. The rational \(C_2\)-representation is determined by its dimension and trace: its invariant dimension is half their sum. A finite-group simplicial action becomes without inversions after barycentric subdivision, so rational quotient homology agrees with invariant rational homology. Applying this to \(u\) proves the quotient formula and degree concentration. The first two nonzero-degree cases have dimensions \((1-1)/2=0\); for \(n\ge4\), the Fibonacci rank exceeds the possible trace magnitude except when it already gives a positive invariant dimension.

## Verification
The standalone `CHECK.py` reconstructs the one-column domino transitions from the mask criterion, traverses the complete reachable determinized state graph, checks the exact seven-state order, constructs \(M\) and \(t\), and verifies the **whole-matrix** identity \(M^8=M^2\) by integer multiplication. It checks the resulting periodic sequence through \(n=49\), which is a sanity test only; the matrix identity proves the recurrence for all \(n\). A structurally separate routine enumerates all full grid perfect matchings for \(n=1,\ldots,6\), forms their row-reflection edge-orbits, enumerates every extendable invariant simplex, and verifies that the signed fixed-simplex sum agrees with the transfer value. Run `python3 CHECK.py` with Python 3.9 or later, without external dependencies. The algorithm does not assume that an invariant face extends to an **invariant** perfect matching.

## Relationship to prior work
Chandrakar, Chau, Goyal, Karki, and Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph* (arXiv:2611.18058v1, public 2026-11-13), Theorem 3.5, prove the nonequivariant Fibonacci sphere-wedge classification used as an input; their manuscript does not determine a mirror character or geometric quotient homology. The published *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex* gives the \(n=2\) reflection character \(-1\), consistent with but insufficient to imply the six-periodic all-order formula. *A boundary-sensitive eight-column classification of three-row perfect-matching complexes* computes only the first four even widths and their nonequivariant homotopy types. Results on ordinary matching complexes of three-row grids concern a different simplicial complex (all matchings rather than only extendable matchings) and do not imply this assertion.

## Limitations
The theorem determines a rational character for one natural involution and rational homology of its geometric quotient, not the full two-reflection action, the integral lattice decomposition, integral quotient torsion, or the quotient homotopy type. The nonequivariant homotopy input comes from the cited 2026 theorem. The integer transfer proves all orders without extrapolating from finite experiments. An unindexed equivalent computation remains a publication-priority risk.

## References
1. H. Chandrakar, T. Chau, S. Goyal, R. Karki, and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058v1, initially public 2026-11-13. https://arxiv.org/abs/2611.18058
2. *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-five-cycle-core-and-signed-reflection-homology-for-the-three-b--521893fb03dc
3. *A boundary-sensitive eight-column classification of three-row perfect-matching complexes*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-boundary-sensitive-eight-column-classification-of-three-row-pe--c400769702b4
4. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public 2024-07-08. https://arxiv.org/abs/2407.05809
