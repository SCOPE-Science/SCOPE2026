# An exact independent-join rank transfer for graphical Lie algebras

## Finding

Let \(q\) be a prime power, \(G\) a finite simple graph on \(m\geq1\) vertices, and \(\overline K_n\) an edgeless graph on \(n\geq1\) vertices. Put \(H=G\vee\overline K_n\), the graph obtained by connecting every new vertex to every old vertex, **but adding no edges between new vertices**. For an edge-weight vector \(y\in\mathbb F_q^{E(G)}\), let \(B_G(y)\) denote the \(m\)-by-\(m\) alternating weighted adjacency matrix, and put
\[
R_G(q;z)=\sum_{y\in\mathbb F_q^{E(G)}}z^{\operatorname{rank}(B_G(y))/2}=\sum_r g_r(G,q)z^r.
\]
The following explicit coefficients depend only on \(m,n,q\), and the prior rank index \(r\). Consequently, the entire rank distribution of \(H\) is determined by the rank distribution of \(G\), without further information about its weight patterns or graph isomorphism type.

For \(0\leq t\leq\min(m,n)\), put
\[
P_q(n,t)=\prod_{i=0}^{t-1}(q^n-q^i).
\]
For \(0\leq u\leq r\), put
\[
I_q(r,u)=\frac{\prod_{i=0}^{u-1}(q^{2r-i}-q^i)}{\prod_{i=0}^{u-1}(q^u-q^i)}.
\]
Let
\[
\sigma_q(s)=q^{s^2}\prod_{i=1}^{s}(q^{2i}-1),\qquad
H_q(s,j)=\frac{\sigma_q(s)}{\sigma_q(j)\sigma_q(s-j)}
\]
for \(0\leq j\leq s\). Empty products equal one. Let \(\begin{bmatrix}h\\e\end{bmatrix}_q\) denote the Gaussian binomial coefficient. All factors with invalid integer arguments are defined as zero. Define \(h=m-2r\), and for \(0\leq d\leq m\), \(j\geq0\), set
\[
S_q(m,r;d,j)
=\sum_{e=0}^{\min(h,d)}
\begin{bmatrix}h\\e\end{bmatrix}_q
q^{(h-e)(d-e)}
I_q(r,d-e-2j)
H_q(r-d+e+2j,j).
\]
In the sum, a term is zero unless the arguments of both \(I_q\) and \(H_q\) are valid. Then the **independent-join transfer** is
\[
\boxed{
R_H(q;z)=\sum_{r\geq0}g_r(G,q)
\sum_{t=0}^{\min(m,n)}P_q(n,t)
\sum_{j\geq0}S_q(m,r;m-t,j)z^{t+j}.}
\]
The displayed sums are finite, and the theorem holds in every characteristic, including two. The transfer coefficients are nonnegative integers and their sum over the output ranks equals \(q^{mn}\) for each fixed base matrix.

**Complete tripartite corollary.** For all positive \(a,b,c\), take \(G=K_{a,b}\) and \(n=c\). Its base coefficients are
\[
\boxed{g_r(K_{a,b},q)=
\begin{bmatrix}a\\r\end{bmatrix}_q
\prod_{i=0}^{r-1}(q^b-q^i),\quad 0\leq r\leq\min(a,b).}
\]
Substituting these into the transfer gives every alternating rank multiplicity of \(K_{a,b,c}\) as an explicit Gaussian-binomial finite sum, for all \(a,b,c\) and every finite field. For odd \(q\), write \(N=a+b+c\), let \(A_k=[z^k]R_{K_{a,b,c}}(q;z)\), and let \(\mathbf G_{K_{a,b,c}}(\mathbb F_q)\) be the associated finite graphical class-two group. The number of its irreducible complex characters of degree \(q^k\) is exactly
\[
\boxed{\operatorname{ch}_{q^k}=q^{N-2k}A_k.}
\]
This determines the **complete character-degree distribution** of every complete tripartite graphical group in odd characteristic, including all three part sizes at least two.

For instance, for \(K_{2,2,2}\) over \(\mathbb F_3\), the alternating rank-half multiplicities for \(k=0,1,2,3\) are \((1,1376,198288,331776)\); the corresponding numbers of characters of degrees \(1,3,9,27\) are \((729,111456,1784592,331776)\), respectively.

## Assumptions and scope

A graph is finite, undirected, simple, and labeled. Each edge weight is independently chosen from the entire field, including zero; the count is not conditioned on support. The alternating matrix has entries \(B_{ij}=y_{ij}\), \(B_{ji}=-y_{ij}\) when \(i<j\), with zero diagonal and zero entries on nonedges. In characteristic two, this remains an alternating form, and ranks remain even. The polynomial exponent is **half** the matrix rank. The rank-transfer and tripartite formulas require only that \(q\) be a prime power; the character-theoretic conclusion assumes odd characteristic. The three tripartite parts are all nonempty.

## Proof

**1. Rank under a free rectangular extension.** Fix an alternating \(m\)-by-\(m\) matrix \(A\) of rank \(2r\). Every extension by \(n\) mutually nonadjacent universal vertices has matrix
\[
M=\begin{pmatrix}A&B\\-B^{\mathsf T}&0\end{pmatrix},\qquad B\in\operatorname{Mat}_{m\times n}(\mathbb F_q).
\]
Let \(t=\operatorname{rank}B\) and \(W=\ker B^{\mathsf T}\), so \(\dim W=m-t\). A vector \((x,y)\) lies in \(\ker M\) if and only if \(x\in W\) and \(By=-Ax\). The second equation is solvable precisely when \(Ax\) annihilates \(W\) under the natural pairing, equivalently when \(x\) lies in the radical of \(A|_{W\times W}\). If this restriction has rank \(2j\), there are \(q^{m-t-2j}\) choices for \(x\), and each admits \(q^{n-t}\) choices for \(y\). Therefore
\[
\dim\ker M=m+n-2t-2j,\qquad
\boxed{\operatorname{rank}M=2(t+j).}
\]
For a fixed \((m-t)\)-subspace \(W\), the number of matrices \(B\) having \(\ker B^{\mathsf T}=W\) is the number of injections \(\mathbb F_q^m/W\hookrightarrow\mathbb F_q^n\), namely \(P_q(n,t)\).

**2. Rank-restricted subspace census.** Write \(U=\operatorname{rad}A\), \(\dim U=h=m-2r\), and choose a complementary nondegenerate symplectic space \(V_0\) of dimension \(2r\). For a \(d\)-subspace \(W\), put \(e=\dim(W\cap U)\), and let \(S\subset V_0\) be its projected image. Then \(\dim S=d-e\), the restricted alternating rank on \(W\) equals that on \(S\), and for fixed \(e\)-subspace \(E\subset U\) and fixed \(S\), exactly \(q^{(h-e)(d-e)}\) subspaces \(W\) occur (their choices are graphs of linear maps \(S\to U/E\)). There are \(\begin{bmatrix}h\\e\end{bmatrix}_q\) choices for \(E\).

For a subspace \(S\) of dimension \(a=d-e\) and alternating rank \(2j\), its radical \(T=S\cap S^\perp\) has dimension \(u=a-2j\). It is totally isotropic in \(V_0\). Counting ordered independent vectors with successive orthogonality constraints gives exactly \(I_q(r,u)\) possible \(T\)'s. For each such \(T\), the quotient \(T^\perp/T\) is a nondegenerate symplectic space of dimension \(2(r-u)\). The image \(S/T\) must be a nondegenerate \(2j\)-subspace. The symplectic group acts transitively on these with stabilizer the product of the symplectic groups of the subspace and its orthogonal complement, so their number is \(H_q(r-u,j)\). The preimage in \(T^\perp\) is uniquely \(S\), making this count exact. Summing over \(e\) yields \(S_q(m,r;d,j)\).

**3. Assembly.** Every rank-\(2r\) base matrix has exactly the same extension census, since all alternating matrices of a given rank are congruent, including in characteristic two. Multiply the subspace count by the injection count, then by \(g_r(G,q)\), and sum. This proves the boxed transfer. It also gives \(\sum_{j}S_q(m,r;d,j)=\begin{bmatrix}m\\d\end{bmatrix}_q\); summing over ranks of \(B\) counts all \(q^{mn}\) extensions.

**4. Complete tripartite specialization.** The alternating matrix of \(K_{a,b}\) is \(\begin{psmallmatrix}0&X\\-X^{\mathsf T}&0\end{psmallmatrix}\) for arbitrary \(a\)-by-\(b\) matrix \(X\), and its rank is \(2\operatorname{rank}X\). Selecting the image and an injective map from an \(r\)-dimensional quotient proves the Gaussian formula for \(g_r\). The join with an edgeless \(c\)-vertex graph is exactly \(K_{a,b,c}\). For odd \(q\), the class-two orbit method parameterizes characters using coadjoint orbits: at fixed edge-dual parameter \(y\) of alternating rank \(2k\), there are \(q^{N-2k}\) coadjoint orbits in the vertex-dual coordinates, each of size \(q^{2k}\) and associated to a character of degree \(q^k\). This proves the character formula. Independently, \(\sum_k q^{N-2k}A_kq^{2k}=q^{N+|E(K_{a,b,c})|}\), the required character-degree square sum.

## Verification

The standalone `verify.py` constructs weighted adjacency matrices and computes their ranks by finite-field Gaussian elimination, independently of the transfer's proof. It separately evaluates the proposed finite sum and compares all coefficients. Exhaustive cases cover the joins of two isolated vertices, a single edge, a three-vertex path, and a four-cycle by one or two mutually independent universal vertices. Field sizes include \(2,3,4\); the order-four field is represented by an explicit extension of \(\mathbb F_2\). In particular the tests exhaust all \(3^{12}=531441\) edge assignments for \(K_{2,2,2}\) over \(\mathbb F_3\), as well as all \(2^{12}=4096\) assignments over \(\mathbb F_2\). A separate identity check verifies the restricted-subspace partition across \(q\in\{2,3,4\}\), \(m\leq6\), and all admissible base ranks and subspace dimensions.

Run `python verify.py` from a folder containing the standalone script; compare with `verification_output.txt`. The final markers are `SYMPLECTIC_SUBSPACE_PARTITION_PASS` and `INDEPENDENT_JOIN_DIRECT_RANK_PASS`. Exhaustive finite-field experiments are corroboration only, not proofs for arbitrary parameters.

## Relationship to prior work

The graphical Lie-algebra construction and its isomorphism classification are given by Mainkar (first publicly posted October 12, 2013); this paper motivates the graph-algebra family but does not enumerate finite-field alternating ranks. O'Brien and Voll (2012) supply the group-character orbit framework, not the graph-specific restricted-rank count. Lewis and collaborators (2010) enumerate ranks of unrestricted alternating matrices and related constrained matrix families, but not the present block-join transfer. Rossmann (2021) explicitly asks for character-degree counts of graphical groups; his join formulas describe **conjugacy-class** counts rather than the coadjoint rank polynomial. Published graph-specific results covering trees, cycles, and single-vertex coning are related. The present formula includes single-vertex coning and familiar bipartite cases as covered boundaries, but its independent multi-vertex extension, and the all-parameter complete tripartite character spectrum when \(a,b,c\geq2\), do not follow by iterating the one-vertex coning formula: iteration inserts edges among the newly added vertices. The symplectic subspace-enumeration ingredients are classical; the claimed contribution is their exact assembly as a universal rank transform for independent-set joins, with the stated tripartite application.

## Limitations

This is a finite-field enumeration theorem, not a classification of individual weight assignments up to graph automorphisms. The character-degree statement is restricted to odd characteristic. The transfer treats joins with an **edgeless** added graph, not arbitrary joins of two nonempty graphs with their own internal edges. An as-yet-unlocated broader theorem about ranks of structured alternating matrices could subsume this transfer; historical priority remains provisional. No independent validation has been performed.

## References

1. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414 (first posted 2013-10-12), especially the graph-to-Lie construction and Theorem 1.1; https://arxiv.org/abs/1310.3414.
2. E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*, arXiv:1203.3050 (first posted 2012-03-14), orbit-method formulae; https://arxiv.org/abs/1203.3050.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (first posted 2021-07-12), especially Section 1.6, Question 1.10, and Section 5; https://arxiv.org/abs/2107.05564.
4. J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam and Y. X. Zhang, *Matrices with restricted entries and q-analogues of permutations*, arXiv:1011.4539 (first posted 2010-11-20), especially Section 3.2; https://arxiv.org/abs/1011.4539.
