# Spectra and spanning-tree complexity of two-token sliding on categorical clique products

## Finding
For arbitrary integers \(m,n\ge3\), consider the categorical product \(D_{m,n}=K_m\times K_n\). Its vertices are cells \((i,j)\), with \(1\le i\le m\) and \(1\le j\le n\); two distinct cells are adjacent precisely when *both* coordinates differ. The token-sliding graph \(\mathsf{TS}_k(D_{m,n})\) has the independent \(k\)-vertex subsets as states, with an edge between two states when one token slides across one edge of \(D_{m,n}\) and independence is preserved.

**Freezing transition.** For every \(k\ge3\), this state graph has no edges, and the number of states is
\[
N_k=m\binom nk+n\binom mk,
\]
where \(\binom ak=0\) for \(k>a\). Thus no independent configuration of three or more tokens can make even one legal slide.

**Two-token spectrum.** The graph \(T_{m,n}=\mathsf{TS}_2(D_{m,n})\) is connected and bipartite, with
\[
|V(T_{m,n})|=\frac{mn(m+n-2)}2,\qquad |E(T_{m,n})|=mn(m-1)(n-1).
\]
Its adjacency eigenvalues, listed with multiplicity *for each sign*, are
\[
\begin{array}{c|c}
\text{eigenvalues}&\text{multiplicity for each sign}\\\hline
\pm 2\sqrt{(m-1)(n-1)}&1\\
\pm\sqrt{2(m-1)(n-2)}&n-1\\
\pm\sqrt{2(n-1)(m-2)}&m-1\\
\pm\sqrt{(m-2)(n-2)}&(m-1)(n-1).
\end{array}
\]
Additionally, zero has multiplicity \(mn(m+n-6)/2\). Whenever two listed numerical eigenvalues coincide, add their multiplicities.

**Spanning-tree enumerator.** The exact number of spanning trees of \(T_{m,n}\) equals
\[
\boxed{\displaystyle
\tau(T_{m,n})=\frac4{mn}
[2(m-1)]^{mn(n-3)/2}
[2(n-1)]^{mn(m-3)/2}
[2n(m-1)]^{n-1}
[2m(n-1)]^{m-1}
[3mn-2m-2n]^{(m-1)(n-1)}.}
\]
For example, \(\tau(T_{3,3})=466560000\), and \(\tau(T_{3,4})=205437507062464512\).

## Assumptions and scope
Graphs are finite, simple, undirected, and labelled. Only categorical/direct products are considered, *not* Cartesian products. Both factors have order at least three; no statement is made for degenerate factors of order two. The state graphs retain all labelled independent subsets, not their isomorphism classes. The spanning-tree formula applies to \(k=2\) only; an edgeless higher-token graph cannot support a spanning tree when it has multiple states. The assertion of no slides also holds when the state set is empty.

## Proof
**1. Independent sets and the freeze.** Suppose a set of at least two cells contains two distinct cells \((i,a)\) and \((i,b)\) in the same row. Every cell not in row \(i\) that is nonadjacent to both would have to use both distinct column indices \(a,b\), which is impossible. Thus an independent set containing that pair is entirely in row \(i\). If instead two cells are in a common column, all other cells lie in that column. Since any pair of independent cells shares a row or column, these are all possibilities for independent sets of size at least two. For \(k\ge3\), each state lies in one unique row or one unique column, yielding the count \(N_k\). If a legal slide changed one cell of such a state, the remaining \(k-1\ge2\) cells still lie in their original common row or column, forcing the new cell into the same row or column; such a move cannot cross an edge of the categorical product. Therefore all higher-token states are isolated.

**2. An incidence tensor for two tokens.** The two types of states are
\[
H_{i,\{a,b\}}=\{(i,a),(i,b)\},\qquad
V_{j,\{r,s\}}=\{(r,j),(s,j)\}.
\]
No slide joins two states of the same type, because the moved cell would remain in its original row or column, which is not an edge of \(D_{m,n}\). Moreover,
\[
H_{i,\{a,b\}}\sim V_{j,\{r,s\}}
\quad\Longleftrightarrow\quad i\in\{r,s\}\text{ and }j\in\{a,b\}.
\]
For example, when \(j=a\) and \(r=i\), the token at \((i,b)\) moves to \((s,a)\). This is legal since \(i\ne s\), \(a\ne b\), and the remaining token at \((i,a)\) is nonadjacent to \((s,a)\). The reverse implication follows because the shared token must occupy a common row-column incidence. Thus every horizontal state has degree \(d_H=2(m-1)\), every vertical state degree \(d_V=2(n-1)\), and counting either side gives the vertex and edge formulas above.

Let \(B_t\) denote the unsigned vertex-edge incidence matrix of the complete graph \(K_t\), of size \(t\) by \(\binom t2\). With states ordered horizontally then vertically, the biadjacency matrix of \(T_{m,n}\) is exactly, up to indexing permutations,
\[
M=B_m\otimes B_n^{\mathsf T}.
\]
Here \(\otimes\) is the Kronecker product. A direct entrywise calculation gives
\[
B_tB_t^{\mathsf T}=(t-2)I_t+J_t,
\]
with eigenvalues \(2(t-1)\) once and \(t-2\) with multiplicity \(t-1\). As \(m,n\ge3\), both incidence matrices have full row rank. The singular values of \(M\) are therefore precisely the four products of square roots of these eigenvalues, with multiplicities \(1,n-1,m-1,(m-1)(n-1)\). The adjacency matrix is
\[
A=\begin{pmatrix}0&M\\M^{\mathsf T}&0\end{pmatrix},
\]
so its nonzero eigenvalues are the positive and negative singular values. Its remaining eigenvalues are zero with multiplicity
\[
\left(m\binom n2+n\binom m2\right)-2mn
=\frac{mn(m+n-6)}2.
\]
The top singular value \(\sqrt{d_Hd_V}\) is simple. The graph is connected: the two-step graph on horizontal states has Gram matrix \(MM^{\mathsf T}\), the Kronecker product of the positive-entry matrix \(B_mB_m^{\mathsf T}\) and the connected positive-diagonal matrix \(B_n^{\mathsf T}B_n\) (whose support is the line graph of \(K_n\), with loops). It is irreducible; every vertical vertex is adjacent to a horizontal vertex. Equivalently, the simplicity of the top singular value and the positivity of the row and column sums imply one connected bipartite component.

**3. Laplacian factors and Kirchhoff's theorem.** The Laplacian has block form
\[
L=\begin{pmatrix}d_HI&-M\\-M^{\mathsf T}&d_VI\end{pmatrix}.
\]
For each nonzero singular value \(s\), the corresponding two Laplacian eigenvalues are the roots of \((d_H-\lambda)(d_V-\lambda)=s^2\). Their product is \(d_Hd_V-s^2\). For the top singular value these roots are \(0\) and \(d_H+d_V\). For the three other singular-value classes, the products of the paired eigenvalues are, respectively,
\[
2n(m-1),\qquad 2m(n-1),\qquad 3mn-2m-2n.
\]
Since \(M\) has rank \(mn\), the unmatched Laplacian eigenvalues are \(d_H\) repeated \(m\binom n2-mn=mn(n-3)/2\) times, and \(d_V\) repeated \(n\binom m2-mn=mn(m-3)/2\) times. Multiply all nonzero Laplacian eigenvalues and divide by \(|V(T_{m,n})|=mn(m+n-2)/2\), as required by Kirchhoff's matrix-tree theorem. The leading ratio becomes \((d_H+d_V)/|V|=4/(mn)\), giving the displayed spanning-tree formula.

## Verification
The accompanying standalone `verify.py` enumerates independent states directly from the categorical-product adjacency rule, forms legal token moves directly, and compares the complete numerical adjacency spectrum against the derived exact-radical spectrum for nine graphs, totalling 605 two-token states. It checks edge counts, bipartiteness and connectedness, and verifies the spanning-tree count by **exact integer Laplacian cofactors** for the \((m,n)=(3,3)\) and \((3,4)\) cases. It also checks the frozen-state count and absence of legal moves for eleven higher-token profiles. Finite tests corroborate but do not replace the parameter-uniform proof. Run with Python 3 and `numpy`, `networkx`, `sympy`: `OPENBLAS_NUM_THREADS=1 python verify.py`.

## Relationship to prior work
Avis and Hoang introduced a systematic structural study of independent-set token-sliding reconfiguration graphs, including the induced-subgraph relation to unrestricted token graphs, in arXiv:2203.16861 (first public March 31, 2022). They do not provide this product-host spectrum or spanning-tree formula. Reyes, Dalfó and Fiol (arXiv:2310.16929) study spectra of *unrestricted* token graphs, whose state sets contain nonindependent subsets and therefore differ materially from the present independent-only reconfiguration graphs. Hoang (arXiv:2606.03765) considers realizability of *target* graphs, including Cartesian-product targets, rather than these token-sliding graphs of categorical-product hosts. The new assertions are the incidence-tensor identification, full spectrum, tree complexity and sharp freezing transition; standard incidence singular values and Kirchhoff's theorem are used as ingredients, not claimed as new.

## Limitations
The originality assessment is based on accessible primary full texts and focused literature searches; an equivalent description under different spectral or incidence-product terminology may exist. The elementary freeze observation alone is not the substantive mathematical contribution; the principal outcome is the full spectral factorization and exact spanning-tree count for the natural two-token reconfiguration family. This proof has not received independent mathematical audit. The numerical verification covers only the listed finite profiles. Statements are restricted to \(m,n\ge3\).

## References
1. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, first submitted 2022-03-31, https://arxiv.org/html/2203.16861v3.
2. M. A. Reyes, C. Dalfó and M. A. Fiol, *On the spectra and spectral radii of token graphs*, arXiv:2310.16929, first submitted 2023-10-25, https://arxiv.org/html/2310.16929v1.
3. D. A. Hoang, *Token-sliding realizability for complements, Cartesian-products, and grid graph families*, arXiv:2606.03765, first submitted 2026-06-02, https://arxiv.org/html/2606.03765v1.
